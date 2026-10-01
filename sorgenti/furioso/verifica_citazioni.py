"""Verifica che le citazioni di dati/furioso/citazioni.json stiano davvero nel testo.

Questo script non genera niente: controlla. Rilegge l'indice delle ottave,
per ogni tappa dell'anno prende il canto, l'ottava e i versi, e chiede al testo
se sono la stessa cosa. Se una riga del JSON è stata corretta a mano — di
spesso un accento, una virgola, un apostrofo — lo dice e basta: è una riga da
correggere, non un errore da discutere.

È il controllo che rende lecitizia la tabella del documento: senza di esso le
citazioni sarebbero «quelle che ricordo», e in questo progetto una citazione
ricordata a memoria è una citazione falsa.E controlla anche le cose che nessuno controllerebbe:
* che nessuna tappa citi due volte la stessa ottava;
* che nessuna citazione cada su un'ottava che ha già un difetto di
trascrizione dichiarato (sei o sedici versi invece di sette od otto);
* che nessuna citazione cada su un'ottava il cui numero compare due volte
nella trascrizione, perché lì il testo è ambiguo per costruzione;
* che ogni citazione cada in un canto che il suo filone dichiara;
* che due tappe confinanti non citino ottave dello stesso canto a meno di tre;
* che il legame `I` vada solo a un luogo dichiarato inesistente.

Uso:  python3 verifica_citazioni.py          -> tutto bene, o l'elenco dei problemi
      python3 verifica_citazioni.py --gutenberg -> riscontro sull'altra edizione
      python3 verifica_citazioni.py --tabella -> la tabella, per il documento
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import estrai_ottave as E  # noqa: E402

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSON = os.path.join(RADICE, "dati", "furioso", "citazioni.json")
MARCATORE = re.compile(r"^\{\{O\s*\|\s*(\d{1,3})\s*\|")


def ottave_ambigue():
    """Chiavi (canto, ottava) il cui numero compare più volte nella trascrizione.

    Rilegge il JSONL delle pagine: è l'unico posto dove l'ambiguità esiste,
    e rileggere un file diverso da quello da cui è nato l'indice è il modo più
    onesto di trovarla.
    """
    conteggio = {}
    for riga in open(E.PAGINE, encoding="utf-8"):
        r = json.loads(riga)
        for numero in MARCATORE.findall(r["wikitext"]):
            chiave = (r["canto"], int(numero))
            conteggio[chiave] = conteggio.get(chiave, 0) + 1
    return {k for k, v in conteggio.items() if v > 1}


def distanza(a, b):
    """|a-b| fra ottave dello stesso canto, 999 fra canti diversi."""
    return abs(a[1] - b[1]) if a[0] == b[0] else 999


def verifica_filoni(documento):
    """Ogni citazione deve cadere nei canti che il suo filone dichiara.

    DIFETTO TROVATO DA QUESTO CONTROLLO, e la ragione per cui il controllo
    esiste: tre citazioni erano state assegnate a un filone i cui canti non
    la contenevano. Il canto 7 era finito dentro «la guerra e il patto» (che
    e' la battaglia di Parigi) quando racconta il ponte d'Erifilla, e il canto 23
    dentro lo stesso filone quando e' gia' la palinodia di Orlando. Il nome
    del filone e' la prima cosa che il giocatore legge, e un nome che non
    descrive il racconto e' una bugia che si vede subito.
    """
    problemi = []
    canti_dichiarati = {}
    for codice, f in documento.get("filoni", {}).items():
        canti = set()
        for pezzo in re.findall(r"\d+", f.get("canti", "")):
            canti.add(int(pezzo))
        for pezzo in re.findall(r"(\d+)\s*-\s*(\d+)", f.get("canti", "")):
            for n in range(int(pezzo[0]), int(pezzo[1]) + 1):
                canti.add(n)
        canti_dichiarati[codice] = canti
    for r in documento["citazioni"]:
        canti = canti_dichiarati.get(r["filone"])
        if canti and r["canto"] not in canti:
            problemi.append("%s: il filone %s dichiara i canti %s e non contiene il canto %d, "
                            "che è quello citato" % (r["tappa"], r["filone"],
                                                     r["filone_canti"], r["canto"]))
    return problemi


def verifica_vicinanze(documento):
    """Due tappe confinanti non citano ottave dello stesso canto a meno di tre.

    Un giocatore che va dalla tappa 5-8 alla 5-9 e ritrova lo stesso canto a
    tre ottave di distanza ha l'impressione che il gioco si sia ripetuto, e ha
    ragione. Il testo non e' corto: sono quarantasei canti.
    """
    problemi = []
    ordinate = sorted(documento["citazioni"], key=lambda r: int(r["tappa"].split("-")[1]))
    for a, b in zip(ordinate, ordinate[1:]):
        chiave_a = (a["canto"], a["ottava"])
        chiave_b = (b["canto"], b["ottava"])
        if distanza(chiave_a, chiave_b) < 3:
            problemi.append("%s e %s citano lo stesso canto a meno di tre ottave di distanza "
                            "(%d,%d e %d,%d): il giocatore le vede di fila e crede che sia un caso"
                            % (a["tappa"], b["tappa"], chiave_a[0], chiave_a[1],
                               chiave_b[0], chiave_b[1]))
    return problemi


def verifica_legami(documento):
    """Il legame `I` solo per un luogo che non esiste, e l'elenco dichiarato.

    DIFETTO TROVATO DA QUESTO CONTROLLO: la tappa 5-17 aveva il legame `I` su
    «i monti Rifei», che sono una catena vera. Il testo citato è fantastico
    (l'ippogrifo non esiste) e il legame era stato scelto sul tono della
    citazione invece che sul luogo: la regola di `luoghi.md` §1.2 — dove `I`
    significa * questo luogo non esiste * — era violata nel modo più invisibile,
    perché nella scheda sembrava tutto coerente.

    Perché un elenco e non un controllo automatico: «esiste o non esiste» è una
    domanda di geografia e di testo, non di programma. Si puó pero' vietare che
    un `I` arrivi a un luogo che nessuno ha dichiarato inesistente, e cosi il
    prossimo errore di questo tipo si vede subito.
    """
    problemi = []
    dichiarati = set(documento.get("luoghi_inesistenti", {}))
    usati = set()
    for r in documento["citazioni"]:
        if r["legame"] == "I":
            usati.add(r["luogo"])
            if r["luogo"] not in dichiarati:
                problemi.append("%s: legame `I` su «%s», che non è fra i luoghi "
                                "dichiarati inesistenti: `I` vale solo per un luogo "
                                "che non esiste" % (r["tappa"], r["luogo"]))
    for luogo in sorted(dichiarati - usati):
        problemi.append("il luogo «%s» è dichiarato inesistente ma nessuna "
                        "citazione lo usa con il legame `I`" % luogo)
    return problemi


def verifica():
    with open(JSON, encoding="utf-8") as f:
        documento = json.load(f)
    ottave = E.indicizza("wikisource")
    ambigue = ottave_ambigue()
    problemi = []
    controllate = 0
    usate = {}
    for r in documento["citazioni"]:
        chiave = (r["canto"], r["ottava"])
        versi = ottave.get(chiave)
        if not versi:
            problemi.append("%s: la tappa %s non esiste" % (r["tappa"], r["riferimento"]))
            continue
        for k, atteso in enumerate(r["versi"]):
            # il confronto va fatto contro la posizione dichiarata, non contro
            # il primo verso: è il numero che distingue «la citazione» da
            # «una frase che somiglia a una citazione»
            posizione = r["numeri_versi"][k] if k < len(r["numeri_versi"]) else len(versi) + 1
            if posizione > len(versi):
                problemi.append("%s: il verso %d non esiste, l'ottava ne ha %d"
                                % (r["tappa"], posizione, len(versi)))
                break
            controllate += 1
            if E.normalizza(atteso) != E.normalizza(versi[posizione - 1]):
                problemi.append("%s: il verso %d non combacia\n    json: %s\n    testo: %s"
                                % (r["tappa"], posizione, atteso, versi[posizione - 1]))
        if len(versi) not in (7, 8):
            problemi.append("%s: l'ottava ha %d versi, non è la forma del poema"
                            % (r["tappa"], len(versi)))
        if chiave in ambigue:
            problemi.append("%s: il numero dell'ottava compare due volte nella trascrizione, "
                            "il testo è ambiguo" % r["tappa"])
        if r["legame"] not in ("B", "A", "S", "I", "C"):
            problemi.append("%s: legame %r fuori dalla regola dei luoghi" % (r["tappa"], r["legame"]))
        for campo in ("parafrasi", "moto", "emozione", "tema", "luogo", "filone_titolo"):
            if not r.get(campo):
                problemi.append("%s: il campo %s è vuoto" % (r["tappa"], campo))
        if len(r["parafrasi"]) < 120:
            problemi.append("%s: la parafrasi è troppo breve (%d caratteri): il livello "
                            "chiede una frase, non un titolo" % (r["tappa"], len(r["parafrasi"])))
        usate.setdefault(chiave, []).append(r["tappa"])
    for chiave, tappe in usate.items():
        if len(tappe) > 1:
            problemi.append("l'ottava %d,%d è citata due volte: %s"
                            % (chiave[0], chiave[1], ", ".join(tappe)))
    attese = ["5-%d" % i for i in range(1, 31)]
    mancanti = [t for t in attese if t not in [r["tappa"] for r in documento["citazioni"]]]
    if mancanti:
        problemi.append("tappe senza citazione: %s" % ", ".join(mancanti))
    problemi += verifica_filoni(documento)
    problemi += verifica_vicinanze(documento)
    problemi += verifica_legami(documento)
    return documento, controllate, problemi


def riscontro_gutenberg(documento):
    """Confronta le citazioni dei canti 1-16 con l'altra edizione disponibile.

    L'edizione del 1928 modernizza la grafia («sciolto» per «sciolto» è uguale,
    ma «né» diventa «né» e «inchiostro» perde l'ï). Se una citazione cambiasse
    di significato, cambierebbe l'insegnamento. Si controlla quindi che le
    trenta citazioni che cadono nella prima parte — quella che il *Gutenberg*
    contiene — dicano la stessa cosa anche lì.

    Non tutte le trenta sono confrontabili: il *Gutenberg* si ferma al canto 16.
    Quelle che lo sono, sono elencate una per una; quelle che non lo sono sono
    dichiarate, non tacite.

    L'apostrofo non conta come differenza: «degl'infideli» e «degli infideli»
    sono la stessa parola in due edizioni, e segnalarlo sarebbe rumore. Il
    rumore è nemico — un controllo che segnala duecento cose non viene letto,
    e un controllo che non si legge non controlla.
    """
    mine = E.indicizza("gutenberg")
    nostre = E.indicizza("wikisource")
    problemi = []
    confrontate = 0
    saltate = []
    for r in documento["citazioni"]:
        chiave = (r["canto"], r["ottava"])
        loro = mine.get(chiave)
        if not loro:
            saltate.append(r["tappa"])
            continue
        confrontate += 1
        nostri = nostre[chiave]
        if len(loro) != len(nostri):
            # Le due edizioni non hanno lo stesso numero di versi nella stessa
            # ottava: confronto posizionale impossibile, e un confronto alla
            # cieca produrrebbe una raffica di falsi allarmi. Si dichiara la
            # differenza e si lascia la citazione «da confrontare a occhio».
            problemi.append("%s: le due edizioni hanno un numero di versi diverso in %s "
                            "(%d contro %d): confronto posizionale impossibile, "
                            "da confrontare a occhio" % (r["tappa"], r["riferimento"],
                                                         len(nostri), len(loro)))
            continue
        for k, posizione in enumerate(r["numeri_versi"]):
            if posizione > len(loro):
                problemi.append("%s: l'edizione Gutenberg non ha il verso %d di %s"
                                % (r["tappa"], posizione, r["riferimento"]))
                continue
            a = E.normalizza(r["versi"][k]).replace("'", "")
            b = E.normalizza(loro[posizione - 1]).replace("'", "")
            if a != b:
                problemi.append("%s: le due edizioni divergono sul verso %d di %s\n"
                                "    1928:      %s\n    Gutenberg: %s"
                                % (r["tappa"], posizione, r["riferimento"],
                                   r["versi"][k], loro[posizione - 1]))
    return confrontate, saltate, problemi


if __name__ == "__main__":
    documento, controllate, problemi = verifica()
    if "--gutenberg" in sys.argv:
        confrontate, saltate, problemi2 = riscontro_gutenberg(documento)
        print("riscontro con l'edizione Gutenberg (canti 1-16): %d citazioni confrontate, %d problemi"
              % (confrontate, len(problemi2)))
        print("non confrontabili (fuori dalla prima parte): %s" % ", ".join(saltate))
        for p in problemi2:
            print("  " + p)
        sys.exit(1 if problemi2 else 0)
    if "--tabella" in sys.argv:
        print("| tappa | filone | riferimento | legame | luogo del Furioso |")
        print("|---|---|---|---|---|")
        for r in documento["citazioni"]:
            print("| %s | %s | %s | `%s` | %s |" % (r["tappa"], r["filone"],
                                                     r["riferimento"], r["legame"], r["luogo"]))
    else:
        print("citazioni: %d, versi riscontrati: %d, problemi: %d"
              % (len(documento["citazioni"]), controllate, len(problemi)))
        for p in problemi:
            print("  " + p)
        if not problemi:
            print("tutti i versi stanno nel testo, nel canto e nell'ottava dichiarati")