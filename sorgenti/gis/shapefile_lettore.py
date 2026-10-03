"""Lettore di shapefile (.shp + .dbf) senza dipendenze esterne.

`scarica_ne.py` e `mappe_formato.py` scrivono i 19 file di `dati/mappe/` e
 normalmente si appoggiano a **pyshp**, che su questa macchina non è
installato e che il progetto non installa: si può fare a meno di una libreria,
perché il formato ESRI Shapefile è documentato e semplice.

I tre pezzi che servono qui:

- **.shp**: intestazione di 100 byte, poi un record per geometria. Il record
  dice il tipo (1 = Point, 5 = poligono, 8 = MultiPoint) e poi quattro numeri:
  il bounding box e tre interi che sono l'inizio e la fine dei pezzi di
  contenuto. I pezzi sono liste di vertici, separate dalla bandierina 0, e ogni
  lista chiusa è un **anello esterno**; un anello con verso opposto è un
  **buco**, e la polygon-part list dice a quale anello esterno appartiene.
  Per i punti la struttura è diversa e più semplice: dopo il tipo vengono
  subito X e Y (`punti()`).
- **.shx**: indice dei record, 8 byte ciascuno. Non serve per leggere in
  ordine, e quindi non si legge.
- **.dbf**: tabella senza nome proprio, con record a lunghezza fissa. I nomi
  dei campi sono in un header che li termina con 0x0D, le larghezze sono
  dichiarate, e i valori sono testo niente-popolato a destra.

Il documentatore di Natural Earth scrive geometrie **multiparte**: un poligono
può essere fatto di più anelli esterni (isole, pezzi di costa), e senza
ricostruire le parti il winding number dà risultati che sembrano giusti e non
lo sono. Per questo `parti()` è separata da `leggi()` e restituisce ogni
poligono con i suoi anelli, buchi compresi, nell'ordine in cui la fonte li
dichiara.
"""
import os
import struct

# codici di forma, solo quelli che il progetto usa
FORME = {0: "Null", 1: "Point", 3: "PolyLine", 5: "Polygon", 8: "MultiPoint"}


def _testo(grezzo):
    """I .dbf di Natural Earth sono in UTF-8 (lo dice il file .cpg), ma non
    tutti: un nome in latino-1 non si decodifica in UTF-8. Si prova UTF-8 e si
    cade su latino-1, che non sbaglia mai."""
    grezzo = grezzo.split(b"\x00")[0].rstrip()
    try:
        return grezzo.decode("utf-8").strip()
    except UnicodeDecodeError:
        return grezzo.decode("latin-1").strip()


def _legga_dbf(percorso):
    """(nomi dei campi, lista di righe come dizionari)."""
    with open(percorso, "rb") as f:
        raw = f.read()
    n_rec, lung, dim_riga = struct.unpack("<I H H", raw[4:12])
    campi, i = [], 32
    while raw[i] != 0x0D:
        # il descrittore di un campo è 32 byte: 11 di nome, 1 di tipo,
        # 4 riservati, **1 di lunghezza**, 1 di cifre decimali, 14 riservati.
        # Prendere il byte 11 (il tipo) invece del 16 (la lunghezza) legge
        # 'C' di Character come larghezza 67, e il file si apre ma tutte le
        # righe diventano spazzatura: è successo, e i nomi che tornavano erano
        # sequenze di caratteri di controllo.
        nome = raw[i:i + 11].split(b"\x00")[0].decode("latin-1").strip()
        campi.append((nome, raw[i + 16]))
        i += 32
    # la prima riga comincia DOPO l'header, che è `lung` byte: usare
    # dim_riga * (n + 1) funziona solo se header e riga hanno la stessa
    # lunghezza, e in questo file non è vero. Con l'offset sbagliato ogni
    # nome esce troncato o spostato, e i nomi sono l'unica cosa che conta.
    righe = []
    for n in range(n_rec):
        base = lung + dim_riga * n
        # Il primo byte di ogni record è il **flag di cancellazione**: uno
        # spazio se il record c'è, un asterisco se è stato cancellato. Va
        # saltato sempre, e i campi cominciano dopo. Non saltarlo sposta
        # tutti i campi di un byte: i nomi escono con una cifra davanti
        # ('1Roma', '2Italy') e i numeri con un carattere in più.
        cancellato = raw[base:base + 1] == b"*"
        base += 1
        riga = {}
        if not cancellato:
            for nome, larg in campi:
                riga[nome] = _testo(raw[base:base + larg])
                base += larg
        righe.append(riga)          # l'indice resta quello del record
    return campi, righe


def parti(percorso_shp, percorso_dbf=None):
    """Ogni poligono come (proprieta, [anello esterno, buchi, ...]).

    Gli anelli sono in gradi decimali e chiusi, come li vuole
    `punto_in_poligono.py`.
    """
    with open(percorso_shp, "rb") as f:
        raw = f.read()
    codice = struct.unpack("<i", raw[32:36])[0]
    if codice != 5:
        raise ValueError("solo i poligoni (5), questo e' %s" % FORME.get(codice, codice))

    campi, righe = ([], [])
    if percorso_dbf and os.path.exists(percorso_dbf):
        campi, righe = _legga_dbf(percorso_dbf)

    # l'intestazione occupa i primi 100 byte; i record cominciano lì e ogni
    # record ha 8 byte di intestazione propria prima del contenuto
    offset, risultati = 100, []
    while offset < len(raw):
        numero, lung = struct.unpack(">ii", raw[offset:offset + 8])
        corpo = raw[offset + 8:offset + 8 + lung * 2]
        offset += 8 + lung * 2

        forma = struct.unpack("<i", corpo[0:4])[0]
        if forma != 5:                      # i poligoni multiparte non hanno
            continue                       # parte di polygon: si saltano
        # dopo il tipo e il bounding box (4 + 32 byte) vengono due interi:
        # quante parti ha il poligono e quanti punti in totale. Poi le parti,
        # quattro interi ciascuna, e subito dopo tutti i punti.
        # NB: l'offset 36 e' il primo intero utile; sbagliarlo di quattro
        # byte fa leggere il numero di punti come numero di parti, e il file
        # si legge ma restituisce geometrie a caso.
        campi_poly, punti_tot = struct.unpack("<2i", corpo[36:44])
        if campi_poly < 1 or campi_poly > 10000:
            continue

        # NEL POLIGONO le parti sono **solo gli indici di inizio**, quattro byte
        # ciascuno, non sedici: la specifica ESRI mette il bounding box della
        # parte una volta sola, nel record. E la parte k finisce dove
        # comincia la parte k+1. Leggerle come blocchi da 16 byte sposta
        # tutto di 12 byte per parte, e il file si legge ma restituisce
        # geometrie a caso: e' successo, e il controllo che lo ha preso e' la
        # lunghezza del record, che non torna piu' (44 + 4*parti + 16*punti
        # deve essere uguale alla lunghezza dichiarata).
        starts = [struct.unpack("<i", corpo[44 + 4 * k:48 + 4 * k])[0]
                  for k in range(campi_poly)]

        # e subito dopo le parti stanno i punti, tutti insieme
        base_punti = 44 + 4 * campi_poly
        punti = []
        for k in range(punti_tot):
            x, y = struct.unpack("<dd", corpo[base_punti + 16 * k:
                                             base_punti + 16 * k + 16])
            punti.append((x, y))

        def anello(da, a):
            anello_punti = punti[da:a]
            if anello_punti and anello_punti[0] != anello_punti[-1]:
                anello_punti = anello_punti + [anello_punti[0]]
            return anello_punti

        if starts != sorted(starts):
            raise ValueError("record %d: indici di parte non in ordine" % numero)
        starts = starts + [punti_tot]

        # UN record e' UNA geometria con piu' anelli: l'anello esterno e i suoi
        # buchi insieme. Non si divide in piu' poligoni, perche' un record e'
        # una unita' amministrativa e i suoi pezzi (isole, lembi, laghi) le
        # appartengono: spezzarli produrrebbe piu' poligoni con lo stesso nome
        # e nessuno saprebbe quale sia quello giusto.
        props = righe[numero - 1] if len(righe) >= numero else {}
        anelli = [anello(starts[k], starts[k + 1]) for k in range(len(starts) - 1)]
        anelli = [a for a in anelli if len(a) >= 4]
        if anelli:
            risultati.append((props, anelli))
    return risultati


def punti(percorso_shp, percorso_dbf=None):
    """Ogni punto come (proprieta, lon, lat): forme 1 (Point) e 8 (MultiPoint).

    Aggiunto per `geography_regions_elevation_points`, che sono punte e non
    poligoni: `parti()` su quei file solleva «solo i poligoni (5)», che e'
    esattamente il messaggio giusto per un file sbagliato e il messaggio
    sbagliato per un file giusto.

    I due formati hanno intestazioni diverse, ed e' la trappola che questa
    funzione evita:

    - **Point (1)**: dopo il tipo vengono subito X e Y, due doppi da 8 byte.
      Nessun bounding box, nessun contatore: 20 byte di contenuto.
    - **MultiPoint (8)**: dopo il tipo c'e' il bounding box (4 doppi, 32 byte),
      poi il numero di punti (un intero da 4 byte), poi i punti. 40 byte di
      intestazione prima del primo punto.

    Il pericolo e' il simmetrico di quello dei poligoni: se si legge X dal
    posto sbagliato in un MultiPoint si legge il bounding box, cioe' un
    numero grande, e il file si apre e restituisce punti a latitudine 90. Il
    controllo che se ne accorge e' `verifica_altitudine.py`, che chiede che
    ogni punto sia dentro il mondo.
    """
    with open(percorso_shp, "rb") as f:
        raw = f.read()

    campi, righe = ([], [])
    if percorso_dbf and os.path.exists(percorso_dbf):
        campi, righe = _legga_dbf(percorso_dbf)

    offset, risultati = 100, []
    while offset < len(raw):
        numero, lung = struct.unpack(">ii", raw[offset:offset + 8])
        corpo = raw[offset + 8:offset + 8 + lung * 2]
        offset += 8 + lung * 2
        if len(corpo) < 4:
            continue
        forma = struct.unpack("<i", corpo[0:4])[0]
        if forma == 1:
            if len(corpo) < 20:
                continue
            x, y = struct.unpack("<dd", corpo[4:20])
            punti_riga = [(x, y)]
        elif forma == 8:
            # 4 del tipo, 32 del bounding box, 4 del numero di punti
            if len(corpo) < 40:
                continue
            quanti = struct.unpack("<i", corpo[36:40])[0]
            if quanti < 1 or quanti > 100000:
                continue
            punti_riga = [struct.unpack("<dd", corpo[40 + 16 * k:56 + 16 * k])
                          for k in range(quanti)]
        else:
            continue
        props = righe[numero - 1] if len(righe) >= numero else {}
        for xy in punti_riga:
            risultati.append((props, xy[0], xy[1]))
    return risultati


def leggi(percorso):
    """Come `parti`, ma con i campi utili ripuliti: i numeri diventano numeri
    e le stringhe vuote diventano None, cosi' il file di uscita non porta
    dentro dodici spazi."""
    def pulisci(props):
        fuori = {}
        for k, v in props.items():
            if v == "":
                continue
            if k.startswith("woe") or k.startswith("LABEL") or k.startswith("NAME"):
                continue
            if k.endswith("YEAR") or k.endswith("MINOR") or k.endswith("MAX"):
                try:
                    fuori[k] = int(float(v))
                    continue
                except ValueError:
                    pass
            fuori[k] = v
        return fuori

    return [(pulisci(p), anelli) for p, anelli in parti(percorso, percorso[:-4] + ".dbf")]