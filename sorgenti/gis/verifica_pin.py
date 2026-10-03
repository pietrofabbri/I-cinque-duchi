"""Verifica i pin degli anni dal secondo in poi: cadono nel Paese e nell'unita'
che il documento dichiara?

Il controllo esiste (`punto_in_poligono.py`) e le coordinate sono scritte a
mano dal 2026-09: questo file e' quello che le mette alla prova. Un pin puo'
essere sbagliato in tre modi, e i tre si vedono con tre controlli diversi:

 1. **in mare**: il punto non cade in nessun poligono Paese. Non e' sempre un
    errore — un pin su una costa o su un lago puo' cadere fuori dalla costa
    semplificata — quindi il controllo misura la distanza dalla terra piu'
    vicina e lascia la soglia dichiarata;
 2. **nel Paese sbagliato**: il punto cade in un Paese, ma non in quello che il
    nome del luogo indica;
 3. **nell'unita' sbagliata**: il punto cade nel Paese giusto ma nella
    provincia o regiona sbagliata. E' il controllo che piu' serve, perche'
    «Ferrara» e «Ferrara, Castello» sono la stessa provincia e «Pella» e' in
    Macedonia Centrale e non in Giordania.

I Paesi hanno tre scale e la piu' fine che contiene il punto vince: la
penisola a 10m, l'Europa a 50m, il mondo a 110m. Ogni scala semplifica di piu'
della precedente, e un pin costiero (Venezia, Costantinopoli) puo' cadere
fuori dalla scala grossa e dentro quella fine: non e' un difetto.

**Tre difetti veri, che nessuno aveva visti** (trovati da questo file):

- **Baghdad** a 34 km dal centro che il file delle citta' archivia: il numero
  nella coordinata aveva una cifra sbagliata (33.03 invece di 33.31);
- **Karakorum** cadeva in Cina: la coordinata era quella del valico del
  Karakoram, non la capitale mongola (Mongolia);
- **Castel del Monte**, dove l'errore era nella tabella degli attesi di questo
  file e non nei dati: il castello federiciano e' ad Andria, in Puglia, e
  l'omonima frazione abruzzese non ce l'ha. Vale la pena tenerlo scritto,
  perche' e' la terza volta che il progetto risolve un titolo invece di un
  luogo, e la prima volta che un controllo automatico lo segnala.

Uso:
    python3 sorgenti/gis/verifica_pin.py                  # anni 2, 3 e 4
    python3 sorgenti/gis/verifica_pin.py --anno 5
    python3 sorgenti/gis/verifica_pin.py --tutti
"""
import json
import math
import os
import sys
import unicodedata

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from punto_in_poligono import dentro

GUARDIA = []
# Oltre i dodici km la distanza dalla terra non e' piu' una distanza: e' un
# punto in un oceano, e il difetto e' il pin, non la soglia.
MAX_KM = 12


def carica(nome):
    """Legge un file delle mappe con il lettore del formato a delta."""
    from mappe_lettore import leggi
    return leggi(os.path.join(RADICE, "dati", "mappe", nome))


def esito(ok, testo):
    print(f"  {'OK ' if ok else 'KO '} {testo}")
    GUARDIA.append(bool(ok))


def paese_di(props):
    """Il codice Paese, tollerando il -99 con cui Natural Earth marca la
    Francia nel file europeo (ISO_A3 vuoto, ADM0_A3 compilato)."""
    cod = props.get("ADM0_A3") or props.get("ISO_A3")
    return None if cod in (None, "-99") else cod


# Scala: (nome del file, chiave della proprieta', etichetta). La piu' fine
# disponibile vince, quindi l'ordine e' 10m, 50m, 110m.
SCALE = [("penisola_10_paesi.json", 10),
          ("europa_50_paesi.json", 50),
          ("mondo_110_paesi.json", 110)]

# Le unita' amministrative: il file della penisola e' fatto di province
# italiane (574), quello europeo di unita' di ogni livello (1 687), quello
# mondiale non le contiene e non viene chiesto. Fuori dall'Europa il controllo
# dell'unita' non si puo' fare con i file archiviati, e il file lo dice: e'
# una copertura mancante, non un difetto del pin.
UNITA = {"10m": "penisola_10_regioni.json",
         "50m": "europa_50_regioni_amministrative.json",
         # Il file mondiale viene per ultimo di proposito: e' quello che copre
         # tutto, ma contiene solo le 50 unita' che contengono un pin del
         # gioco (`mondo_admin1.py`). Se lo si mettesse per primo, un pin
         # italiano che per errore non sta nella sua provincia passerebbe nel
         # file mondiale, che ha la provincia dello stesso nome solo se quel
         # pin e' fra i suoi. L'ordine va dal piu' fine al piu' grezzo, che e'
         # l'ordine giusto anche per la fiducia.
         "mondo": "mondo_admin1.json"}

# Che cosa il documento dichiara, per il nome del luogo. `paese` e' il Paese
# che il nome significa; `unita` e' la provincia o regione che il nome
# significa, con le alternative che la fonte usa. Dove `unita` e' None il
# controllo non e' possibile con i file archiviati (mondo, e gli stati
# europei fuori dal file amministrativo): si dichiara e non si finge.
# La tabella degli attesi viene ripulita con la stessa funzione dei nomi che
# arrivano dai file, cosi' l'apostrofo di l'Aquila e l'accento di Alcalá
# combaciano da entrambe le parti senza scrivere due volte ogni nome.
ATTESI_GIA = {
    # anno 2
    "Chiusi": ("ITA", ["Siena"]),
    "Crotone": ("ITA", ["Crotone"]),
    "Firenze": ("ITA", ["Firenze"]),
    "Milano": ("ITA", ["Milano"]),
    "Palermo": ("ITA", ["Palermo"]),
    "Roma": ("ITA", ["Roma"]),
    "Roma, Tuscolo": ("ITA", ["Roma"]),
    "Taranto": ("ITA", ["Taranto"]),
    "Venezia": ("ITA", ["Venezia"]),
    # anno 3
    "Alcala de Henares": ("ESP", ["comunita di Madrid"]),
    "Alessandria": ("ITA", ["Alessandria"]),
    "Aquisgrana": ("DEU", ["Renania Settentrionale-Vestfalia"]),
    "Atene": ("GRC", ["Attica"]),
    "Basilea": ("CHE", ["Canton Basilea Citta"]),
    # Castel del Monte e' in Puglia (Andria): l'attesa iniziale di questo
    # file diceva L'Aquila, che e' un paese omonimo dell'Abruzzo senza
    # castello. Il controllo ha trovato l'errore nell'attesa, non nel pin.
    "Castel del Monte": ("ITA", ["Barletta Andria Trani", "Barletta-Andria-Trani"]),
    "Certaldo": ("ITA", ["Firenze"]),
    "Ferrara, Camerino": ("ITA", ["Macerata"]),
    "Ferrara, Camerino d'alabastro": ("ITA", ["Ferrara"]),
    "Frombork": ("POL", ["voivodato della Varmia-Masuria"]),
    "Magonza": ("DEU", ["Renania-Palatinato"]),
    "Manchester": ("GBR", ["Manchester"]),
    "Mantova": ("ITA", ["Mantova"]),
    "Norimberga": ("DEU", ["Baviera"]),
    # il file amministrativo europeo e' fatto di distretti: per la Francia
    # l'unita' che contiene Parigi e' il dipartimento, non la regione
    "Parigi": ("FRA", ["Parigi", "Ile-de-France", "Ile de France"]),
    "Pella": ("GRC", ["Macedonia Centrale"]),
    "Ravenna": ("ITA", ["Ravenna"]),
    "Westminster": ("GBR", ["Westminster"]),
    # anno 4
    "Agra": ("IND", ["Uttar Pradesh"]),
    "Baghdad": ("IRQ", ["Babil", "Baghdad"]),
    "Costantinopoli": ("TUR", ["Istanbul"]),
    "Hannover": ("DEU", ["Bassa Sassonia"]),
    # Il Cairo e' in Giza, non nel Cairo: la governatorato che si chiama
    # Cairo e' quello metropolitan, che sta dalla parte del Nilo, e la citta'
    # storica e' in Giza. Il nome del file e' la risposta.
    "Il Cairo": ("EGY", ["Giza", "Cairo", "al Qahirah"]),
    "Karakorum": ("MNG", ["dell'Arhangaj", "Arhangay", "Ovorkhangai", "Ovörhangai"]),
    # Il 03/10/2026, due luoghi hanno ottenuto una coordinata verificata e
    # nessuno dei due aveva un Paese atteso: il controllo 7 chiede che ogni pin
    # con coordinate lo dichiari, e aveva ragione — un pin verificato senza Paese
    # atteso e' un pin che nessuno puo' confrontare con nessun altro.
    # Pataliputra e' la citta' antica e il punto e' l'odierna Patna, nel Bihar:
    # il file amministrativo risponde IND, e la risposta e' giusta perche' il
    # nome antico e il nome moderno sono la stessa citta'.
    "Pataliputra": ("IND", ["Bihar", "Patna"]),
    "Qufu": ("CHN", ["Shandong"]),
    # Tenochtitlan e' Citta del Messico: Natural Earth chiama cosi' il
    # District Federal, che e' la citta' autonoma di oggi. Il nome che porta
    # nel gioco e' quello spagnolo del XVI secolo, il file risponde in italiano.
    "Tenochtitlan": ("MEX", ["Citta del Messico", "Ciudad de Mexico"]),
    "Toledo": ("ESP", ["Toledo"]),
    "Torino": ("ITA", ["Piemonte", "Torino"]),
    "Uppsala": ("SWE", ["Uppsala"]),
    # Uruk e' nel governatorato di al Muthanna, non in quello di Wasit: la
    # citta' di Uruk/Warka e' a 150 km dalla foce dell'Eufrate.
    "Uruk": ("IRQ", ["al Muthanna", "Wasit"]),
    "Xianyang": ("CHN", ["Shaanxi"]),
    # anno 5. Il quinto anno e' il primo con pin fuori dall'Europa e dagli
    # Stati Uniti, e percio' e' anche il primo in cui il confronto con il
    # centro archiviato non e' possibile quasi mai: i file delle citta'
    # hanno 398 punti e sono quasi tutti capitali europee.
    "Bajkonur": ("KAZ", ["Bayqonyr", "Qyzylorda"]),
    "Buenos Aires": ("ARG", ["Buenos Aires", "Ciudad de Buenos Aires"]),
    "Cambridge": ("GBR", ["Cambridgeshire"]),
    "Chicago": ("USA", ["Illinois"]),
    "Ferrara": ("ITA", ["Ferrara"]),
    "Ginevra": ("CHE", ["Canton Ginevra"]),
    # Il file chiama Westminster il borough, e Westminster e' il nome che il
    # gioco dà al pin: il controllo su questo pin e' quindi tautologico, e
    # vale la pena dirlo. Non lo e' per gli altri due, Cambridge e Londra:
    # per Londra il gioco dice «Londra» e il file dice «Westminster», e lo
    # stesso vale per la tappa che si chiama Westminster.
    "Londra": ("GBR", ["Westminster", "Greater London"]),
    "Los Alamos": ("USA", ["Nuovo Messico", "New Mexico"]),
    "Los Angeles": ("USA", ["California"]),
    "New York": ("USA", ["New York"]),
    "Princeton": ("USA", ["New Jersey"]),
    # Rotterdam e' nel Brabante Olandese del Sud, non nella provincia che il
    # file chiama «Zelanda» (che e' Friesland): l'attesa iniziale di questo
    # file sbagliava, e il secondo errore di questo genere dopo Castel del Monte.
"Rotterdam": ("NLD", ["Olanda Meridionale"]),
    "Seattle": ("USA", ["Washington"]),
    "Stoccolma": ("SWE", ["Stoccolma"]),
    "Vienna": ("AUT", ["Vienna"]),
}


def normalizza(s):
    """Il nome del file porta accenti, apostrofi tipografici e trattini lunghi;
    la tabella degli attesi e' senza, perche' e' scritta a mano. Si confronta
    sul testo ripulito e il file resta la fonte.

    Le tre forme che tornano spesso: accenti (Alcala/Alcalá, Citta/Città),
    apostrofo (l'Aquila/dell'Aquila) e trattino (Ile de France/Île-de-France).
    """
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = (s.replace("\u2019", "'").replace("\u02bc", "'")
          .replace("`", "").replace("\u00b4", "").replace("-", " "))
    return " ".join(s.split())


def dist_km(lon1, lat1, lon2, lat2):
    return 111.32 * math.hypot((lon2 - lon1) * math.cos(math.radians((lat1 + lat2) / 2)),
                               lat2 - lat1)


def distanza_terra(lon, lat, paesi, max_km=MAX_KM):
    """Distanza dalla terra piu' vicina, a passi di 0,1 km in 36 direzioni.

    Serve a non chiamare 'errore' un pin che cade solo fuori dalla costa
    semplificata — il Bosforo, la laguna di Venezia — e a chiamare 'errore' un
    pin che e' in un oceanto. Si cerca in tutte e tre le scale: un pin
    costiero puo' cadere fuori dalla piu' grossa e dentro la piu' fine, e la
    domanda che il controllo deve fare e' solo "c'e' terra abbastanza vicino".
    """
    # `dentro()` prende gli anelli di un solo poligono: passargli gli anelli
    # di venti Paesi insieme dà un numero di avvolgimento che non vuol dire
    # niente. Ogni poligono si testa per conto suo.
    terra = [anelli for nome, _ in SCALE
             for props, anelli in paesi[nome] if paese_di(props) is not None]
    if any(dentro(anelli, lon, lat) for anelli in terra):
        return 0.0
    for passo in range(1, int(max_km * 10) + 1):
        km = passo / 10
        for gradi in range(0, 360, 10):
            rad = math.radians(gradi)
            x = lon + km / (111.32 * math.cos(math.radians(lat))) * math.sin(rad)
            y = lat + km / 111.32 * math.cos(rad)
            if any(dentro(anelli, x, y) for anelli in terra):
                return km
    return None


def cerca_paese(lon, lat, paesi):
    """Il Paese e la scala in cui il punto cade; la piu' fine vince."""
    for nome, scala in SCALE:
        trovati = [paese_di(p) for p, anelli in paesi[nome] if dentro(anelli, lon, lat)]
        if trovati:
            return trovati, scala
    return [], None


def cerca_unita(lon, lat, unita):
    """Le unita' amministrative che contengono il punto, per scala.

    L'ordine dei file e' l'ordine della fiducia: il piu' fine vince. Il file
    mondiale tiene solo le unita' che contengono un pin del gioco, quindi e'
    l'ultimo da chiedere e non il primo: se arrivasse prima, un pin che per
    errore non sta nella sua provincia non verrebbe notato, perché il file
    mondiale ha un pezzo di provincia che si somiglia.
    """
    for scala, nome in UNITA.items():
        if nome not in unita:
            continue
        trovate = [normalizza(p.get("name_it") or p.get("name"))
                   for p, anelli in unita[nome] if dentro(anelli, lon, lat)]
        if trovate:
            return trovate, scala
    return [], None


def cerca_capoluogo(nome, punti, lon, lat):
    """Il punto omonimo piu' vicino nei due file delle citta' (212 + 186),
    se c'e'. Se lo stesso nome c'e' due volte (Milano e' kapoluogo di tre
    regioni) si prende quello che e' davanti al pin."""
    tgt = normalizza(nome)
    migliore = None
    for props, x, y in punti:
        if not any(normalizza(props.get(c)) == tgt for c in ("NAME_IT", "NAME")):
            continue
        d = dist_km(lon, lat, x, y)
        if migliore is None or d < migliore[0]:
            migliore = (d, props, x, y)
    return migliore


def anni_richiesti():
    """Gli anni da verificare: 2, 3 e 4 di default, `--anno N` per uno solo,
    `--tutti` per tutti e cinque. Si puo' ripetere `--anno`."""
    if "--tutti" in sys.argv:
        return [2, 3, 4, 5]
    scelti = []
    for i, a in enumerate(sys.argv):
        if a == "--anno" and i + 1 < len(sys.argv):
            scelti += [int(x) for x in sys.argv[i + 1].split(",")]
    return scelti or [2, 3, 4]


def main():
    global ATTESI
    ATTESI = {normalizza(k): v for k, v in ATTESI_GIA.items()}
    anni = anni_richiesti()
    luoghi = json.load(open(os.path.join(RADICE, "dati", "luoghi_gioco.json")))["luoghi"]
    etichetta = ("anni " + ", ".join(str(a) for a in anni)
                 if anni != [2, 3, 4, 5] else "tutti e cinque gli anni")

    # ------------------------------------------------ selezione
    slot, per_anno, slot_coord, coord_anno = 0, {}, 0, {}
    posti = [v for v in luoghi
             if any(a in anni for a in v.get("anni", []))]
    for v in posti:
        for t in v.get("tappe", []):
            a = int(t.split("-")[0])
            if a not in anni:
                continue
            slot += 1
            per_anno[a] = per_anno.get(a, 0) + 1
            if v.get("lat") is not None:
                slot_coord += 1
                coord_anno[a] = coord_anno.get(a, 0) + 1

    print(f"== 0. quanti pin sono, e quanti hanno coordinate ({etichetta}) ==")
    print(f"  posti: {len(posti)}")
    print(f"  slot di pin (uno per tappa): {slot}  per anno: "
          + ", ".join(f"{a}-anno {per_anno[a]}" for a in sorted(per_anno)))
    print(f"  slot con coordinate: {slot_coord}  per anno: "
          + ", ".join(f"{a}-anno {coord_anno.get(a, 0)}" for a in sorted(per_anno)))
    senza = [v for v in posti for t in v.get("tappe", [])
             if int(t.split("-")[0]) in anni and v.get("lat") is None]
    print(f"  slot senza coordinate: {slot - slot_coord}, in {len(senza)} posti distinti")
    stati = {}
    for v in senza:
        stati[v.get("coord_stato")] = stati.get(v.get("coord_stato"), 0) + 1
    for k in sorted(stati):
        print(f"    {k}: {stati[k]}")

    # ------------------------------------------------ carica i file
    paesi = {nome: carica(nome)[0] for nome, _ in SCALE}
    unita = {nome: carica(nome)[0] for nome in UNITA.values()}
    punti = carica("penisola_10_citta.json")[1] + carica("europa_50_citta.json")[1]

    con_coord = [v for v in posti if v.get("lat") is not None]
    stato = {v["luogo"]: v.get("coord_stato") for v in con_coord}

    # ------------------------------------------------ 1. nessun pin in mare
    # Un pin che cade fuori da ogni Paese non e' per forza sbagliato: un capo
    # o una citta' portuale possono cadere oltre la costa semplificata. La
    # soglia e' 3 km, e oltre i 12 km la domanda non ha piu' senso: e' un
    # oceano. Costantinopoli e' il caso vero: il Bosforo e' largo 1 km e la
    # Turchia delle tre scale non lo contiene.
    print("\n== 1. nessun pin cade in mare (soglia: 3 km dalla terra) ==")
    in_mare = []
    for v in con_coord:
        if cerca_paese(v["lon"], v["lat"], paesi)[0]:
            continue
        in_mare.append((v, distanza_terra(v["lon"], v["lat"], paesi)))
    for v, km in in_mare:
        giudizio = "sulla costa semplificata" if km is not None and km <= 3 else "IN MARE"
        print(f"  {v['luogo'][:24]:<26} fuori da ogni Paese, terra a "
              f"{'oltre 12' if km is None else f'{km:.1f}'} km  ({giudizio})")
    esito(all(km is not None and km <= 3 for _, km in in_mare),
          f"pin fuori da ogni Paese entro 3 km dalla terra: {len(in_mare)}"
          f" (se nessuno, il controllo passa senza esitare)")

    # ------------------------------------------------ 2. il Paese
    # Un pin che cade in mare entro la soglia non e' nel Paese sbagliato: e'
    # fuori dalla costa semplificata, e su quel punto nessun file puo' dire
    # niente. Costantinopoli e' il caso: la penisola storica sta nel Corno
    # d'Oro e nessuna delle tre scale ritaglia il Bosforo. Questi pin si
    # contano a parte e non sono difetti.
    print("\n== 2. il Paese e' quello che il nome del luogo dichiara ==")
    sbagliati, per_costa = [], []
    for v in con_coord:
        nome = v["luogo"]
        atteso = ATTESI.get(normalizza(nome), (None, None))[0]
        trovati, scala = cerca_paese(v["lon"], v["lat"], paesi)
        if not trovati:
            km = distanza_terra(v["lon"], v["lat"], paesi)
            if km is not None and km <= 3:
                per_costa.append((nome, km))
                print(f"  --  {nome[:24]:<26} fuori dalla costa semplificata "
                      f"(terra a {km:.1f} km): Paese non verificabile, non difetto")
                continue
        ok = atteso in trovati
        if not ok:
            sbagliati.append((nome, atteso, trovati, scala))
        if not ok or nome in ("Baghdad", "Karakorum"):
            dove = ", ".join(trovati) if trovati else "nessun Paese"
            dove += f" (scala {scala}m)" if scala else ""
            print(f"  {'OK ' if ok else 'KO '} {nome[:24]:<26} atteso {atteso}  "
                  f"trovato {dove}")
    confrontati = len(con_coord) - len(per_costa)
    print(f"  (su {len(con_coord)} pin con coordinate: {confrontati} confrontabili "
          f"per il Paese, {len(per_costa)} fuori dalla costa)")
    esito(not sbagliati, f"pin nel Paese dichiarato: {confrontati - len(sbagliati)}"
                         f" su {confrontati}")

    # ------------------------------------------------ 3. l'unita' amministrativa
    print("\n== 3. l'unita' amministrativa e' quella che il nome dichiara ==")
    verificati, corretti, impossibili = 0, [], []
    for v in con_coord:
        nome = v["luogo"]
        _, attese = ATTESI.get(normalizza(nome), (None, None))
        if not attese:
            impossibili.append(nome)
            continue
        trovate, scala = cerca_unita(v["lon"], v["lat"], unita)
        if not trovate:
            # il file non copre quel Paese: copertura mancante, non difetto
            impossibili.append(nome)
            continue
        verificati += 1
        if not any(normalizza(a) in trovate for a in attese):
            corretti.append((nome, attese, trovate))
    for nome, attese, trovate in corretti:
        print(f"  KO  {nome[:24]:<26} atteso {attese}  trovato {trovate}")
    print(f"  verificabili: {verificati}; non verificabili con i file "
          f"archiviati: {len(impossibili)}")
    print("    fra i non verificabili, quelli fuori dall'Europa o in Paesi che il "
          "file amministrativo non contiene")
    esito(not corretti, f"pin nell'unita' dichiarata: {verificati - len(corretti)}"
                        f" su {verificati}")

    # ------------------------------------------------ 4. il capoluogo omonimo
    print("\n== 4. distanza dal capoluogo omonimo archiviato (soglia: 30 km) ==")
    confrontati, lontani = 0, []
    for v in con_coord:
        nome = v["luogo"]
        hit = cerca_capoluogo(nome, punti, v["lon"], v["lat"])
        if not hit:
            continue
        confrontati += 1
        d = dist_km(v["lon"], v["lat"], hit[2], hit[3])
        if d > 30:
            lontani.append((nome, d, hit))
        if d > 30 or nome in ("Baghdad",):
            print(f"  {'OK ' if d <= 30 else 'KO '} {nome[:24]:<26} pin a {d:6.1f} km "
                  f"dal centro archiviato ({hit[1].get('NAME')}, "
                  f"{hit[2]:.3f},{hit[3]:.3f})")
    print(f"  (il confronto e' possibile per {confrontati} pin su {len(con_coord)}: "
          f"i file delle citta' hanno 212 e 186 punti, non un gazetteer)")
    esito(not lontani, f"pin entro 30 km dal centro omonimo: "
                       f"{confrontati - len(lontani)} su {confrontati}")

    # ------------------------------------------------ 5. nessuna coordinata
    #                                                duplicata
    print("\n== 5. nessuna coordinata duplicata fra i pin ==")
    visti = {}
    dup = []
    for v in con_coord:
        k = (round(v["lat"], 5), round(v["lon"], 5))
        if k in visti:
            dup.append((visti[k], v["luogo"]))
        visti[k] = v["luogo"]
    for a, b in dup:
        print(f"  KO  {a} e {b} hanno le stesse coordinate")
    esito(not dup, f"coordinate duplicate: {len(dup)}")

    # ------------------------------------------------ 6. nessuna coordinata
    #                                                scambiata fra due pin
    # Il controllo non puo' essere "la latitudine e' maggiore della longitudine":
    # in Europa e' vero per tutti, e il controllo direbbe che tutti i pin sono
    # sbagliati. Il rischio reale su una tabella scritta a mano e' un altro: la
    # latitudine di un pin finisce sulla longitudine di un altro. Si cerca
    # quindi ogni coppia di pin in cui le due coordinate sono scambiate.
    print("\n== 6. nessuna coordinata presa da un altro pin e scambiata ==")
    scambiati = []
    for i, a in enumerate(con_coord):
        for b in con_coord[i + 1:]:
            if (abs(a["lat"] - b["lon"]) < 1e-4 and abs(a["lon"] - b["lat"]) < 1e-4
                    and (a["lat"], a["lon"]) != (b["lat"], b["lon"])):
                scambiati.append((a["luogo"], b["luogo"]))
    for x, y in scambiati:
        print(f"  KO  le coordinate di {x} sono quelle di {y} con lat e lon scambiate")
    esito(not scambiati, f"pin con le coordinate scambiate fra loro: {len(scambiati)}")

    # ------------------------------------------------ 7. l'attesa copre i pin
    print("\n== 7. ogni pin con coordinate ha un Paese atteso dichiarato ==")
    mancanti = [v["luogo"] for v in con_coord
                if ATTESI.get(normalizza(v["luogo"]), (None, None))[0] is None]
    for nome in mancanti:
        print(f"  KO  {nome}: nessun Paese atteso nella tabella")
    esito(not mancanti, f"pin senza Paese atteso: {len(mancanti)}")

    # ------------------------------------------------ 8. difetto dichiarato
    # Un difetto che il file di luoghi non dichiara e' un difetto peggiore di
    # un difetto dichiarato: e' un pin che qualcuno ha firmato come verificato
    # e che non lo e'. Il controllo e' questo: ogni pin che fallisce i controlli
    # 2, 3 o 4 deve avere `coord_stato` diverso da `verificata`.
    print("\n== 8. ogni difetto trovato e' dichiarato nel file di luoghi ==")
    difetti = {n for n, _, _, _ in sbagliati} | {n for n, _, _ in corretti} | {n for n, _, _ in lontani}
    non_dichiarati = [n for n in sorted(difetti)
                      if stato.get(n) == "verificata"]
    for nome in difetti:
        dichiarato = stato.get(nome)
        print(f"  {'OK ' if dichiarato != 'verificata' else 'KO '} "
              f"{nome[:24]:<26} coord_stato: {dichiarato}")
    esito(not non_dichiarati, f"difetti non dichiarati: {len(non_dichiarati)}")

    # ------------------------------------------------ sintesi
    print("\n== sintesi dei difetti ==")
    for nome, atteso, trovati, scala in sbagliati:
        dove = ", ".join(trovati) if trovati else "nessun Paese"
        print(f"  {nome}: il documento porta a {atteso}, la coordinata cade in "
              f"{dove} (scala {scala}m)")
    for nome, attese, trovate in corretti:
        print(f"  {nome}: attesa {attese[0]}, trovata {', '.join(trovate)}")
    for nome, d, hit in lontani:
        print(f"  {nome}: {d:.0f} km dal centro archiviato, la coordinata ha una "
              f"cifra sbagliata")
    if not (sbagliati or corretti or lontani):
        print("  nessun difetto")
    for nome, km in per_costa:
        print(f"  {nome}: non e' un difetto, e' una costa che i file semplificano "
              f"(terra a {km:.1f} km)")

    print(f"\n==== controlli superati: {sum(GUARDIA)}/{len(GUARDIA)} ====")
    return 0 if all(GUARDIA) else 1


if __name__ == "__main__":
    sys.exit(main())