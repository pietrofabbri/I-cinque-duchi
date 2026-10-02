"""Cerca su Wikimedia Commons le immagini libere degli oggetti di interazione
delle sei lingue, e dice per ognuna che cosa è stato trovato.

La regola del progetto sui ritratti (`ritratti.md` §1: due immagini, non una)
qui diventa quattro categorie, perché un oggetto non è una persona:

  foto      fotografia o foto d'archivio dell'oggetto reale
  dipinto   dipinto, incisione, xilografia che ritrae l'oggetto
  stampa    riproduzione di un'opera a stampa, di un manoscritto, di una
            partitura, di un'epigrafe
  nessuna   non esiste immagine libera, e l'oggetto va disegnato

Le query sono scelte a mano per voce, non tradotte alla cieca: «lambrusco» in
inglese non trova niente, «Lambrusco wine bottle» sì. Una ricerca automatica che
non guarda le risposte sbaglia, e sbaglia anche qui.

Il file di uscita è `dati/lingue/immagini_oggetti.json`: **proposte**, non
scelte. Le scelte le fa una persona, guardando le immagini, e si registra in
`sorgenti/lingue/attestazione_oggetti.json` con etichetta e motivo — la stessa
regola dei ritratti.

Uso:
    python3 sorgenti/lingue/cerca_immagini_oggetti.py           # tutte le lingue
    python3 sorgenti/lingue/cerca_immagini_oggetti.py EL        # una lingua
    python3 sorgenti/lingue/cerca_immagini_oggetti.py --ripeti  # rilegge il JSON
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.abspath(os.path.join(BASE, "..", ".."))
ASSOC = os.path.join(RADICE, "dati", "lingue", "associazioni.json")
ESITO = os.path.join(RADICE, "dati", "lingue", "immagini_oggetti.json")
CARTELLA = os.path.join(RADICE, "dati", "lingue")


def esito_di(lingua):
    """Un file per lingua: la ricerca resta frazionabile e non si perde."""
    return os.path.join(CARTELLA, "immagini_%s.json" % lingua.lower())

UA = "i-cinque-duchi/0.1 (progetto didattico per liceo; pietrofabbri)"

# Termini di ricerca per voce, **allineati all'ordine delle trenta voci** in
# `associazioni.json`. Il primo termine che dà un risultato libero vince, e la
# ricerca passa al termine successivo solo se i primi non danno niente.
TERMINI = {
    "IT": [
        ("pizza", "pizza italiana"),
        ("ragù", "ragu bolognese"),
        ("cacio e pepe", "cacio e pepe"),
        ("tiramisù", "tiramisu"),
        ("polenta", "polenta"), ("carbonara", "carbonara"),
        ("saltimbocca", "saltimbocca"),
        ("mortadella", "mortadella"),
        ("aceto balsamico", "aceto balsamico Tradizionale"),
        ("prosciutto", "prosciutto di Parma"),
        ("focaccia", "focaccia"), ("sabaion", "sabaione"),
        ("zuppa di lenticchie", "zuppa di lenticchie"),
        ("piadina", "piadina"),
        ("risotto", "risotto alla milanese"),
        ("gnocco", "gnocchi di patate"),
        ("tagliatelle", "tagliatelle"),
        ("bagna cauda", "bagna cauda"),
        ("panna cotta", "panna cotta"),
        ("bistecca", "bistecca alla fiorentina"),
        ("olive", "olive da tavola"),
        ("pesto", "pesto alla genovese"),
        ("pandoro", "pandoro"),
        ("grana", "Grana Padano"),
        ("confetto", "confetti di Siena"),
        ("amaretti", "amaretti di Saronno"),
        ("limoncello", "limoncello"),
        ("lambrusco", "Lambrusco wine bottle"),
        ("budino", "budino cremoso"),
        ("pane", "pane di Ferrara"),
    ],
    "LA": [
        ("auspicia", "auspicia"),
        ("presagium", "Roman augury"),
        ("auspex", "auspex bird reading"),
        ("exta hepatum", "exta hepatum haruspex"),
        ("haruspex", "haruspex"),
        ("sacerdos", "Roman priest relief"),
        ("fulmen", "fulmen lightning Jupiter"),
        ("pestis", "plague of Rome"),
        ("somnium", "Artemidorus Oneirocritica"),
        ("numeri romani", "Roman numerals cliff"),
        ("kalendarium", "Roman calendar Fasti"),
        ("menses romani", "Roman calendar months"),
        ("ludi Romani", "ludi Romani fresco"),
        ("pompa", "pompa circensis relief"),
        ("votum", "votive stele"),
        ("sacramentum", "congiuratio oath Romans"),
        ("maledictio", "curse tablet defixio"),
        ("tabu", "taboo Polynesian"),
        ("nomen omen", "Roman naming omen"),
        ("fatum", "Fatum painting"),
        ("omen", "Roman omen"),
        ("miraculum", "miraculum classical"),
        ("haruspex natalium", "birth omen Rome"),
        ("funus Romanum", "Roman funeral procession"),
        ("ignis sacer", "Vesta sacred fire"),
        ("animalia sacra", "Roman sacred animals"),
        ("templum", "Roman templum"),
        ("carmenQuadragesimum", "carmen quadragesimum"),
        ("vita romana", "Roman daily life mosaic"),
        ("proverbia latina", "Latine proverbia"),
    ],
    "EN": [
        ("folk music", "English folk music"),
        ("delta blues", "Delta blues"),
        ("blues", "blues musicians"),
        ("jazz", "jazz band"),
        ("bebop", "bebop"),
        ("rock and roll", "rock and roll"),
        ("rock music", "rock music"),
        ("punk", "punk band"),
        ("hip hop", "hip hop"),
        ("rap", "rapper"),
        ("soul music", "soul music"),
        ("funk", "funk music"),
        ("reggae", "reggae"),
        ("ska", "ska band"),
        ("country music", "country music"),
        ("musica classica", "orchestra classical"),
        ("opera", "opera house performance"),
        ("musica da camera", "chamber music"),
        ("minimalismo", "minimalist music"),
        ("musica elettronica", "electronic music instrument"),
        ("musica sperimentale", "experimental music"),
        ("canto corale", "choir"),
        ("lied", "Lied art song"),
        ("colonna sonora", "film score"),
        ("musical", "musical theatre stage"),
        ("musica di protesta", "protest song"),
        ("canto gregoriano", "Gregorian chant manuscript"),
        ("musica popolare", "folk song traditional"),
        ("testo canzone", "song lyrics manuscript"),
        ("intervista musicista", "musician interview"),
    ],
    "SI": [
        ("intaglio pietra dura", "hardstone intaglio"),
        ("ceramica", "Italian ceramics"),
        ("maiolica", "maiolica"),
        ("smaltatura", "enamelwork cloisonne"),
        ("vetro", "Murano glass"),
        ("ricamo", "embroidery"),
        ("merletto", "lace making"),
        ("tessitura a telaio", "weaving loom"),
        ("intreccio", "basket weaving"),
        ("canna", "rush weaving"),
        ("ebanisteria", "cabinetmaking"),
        ("intaglio legno", "wood carving"),
        ("tornio", "woodturning lathe"),
        ("cuoio", "leatherworking"),
        ("correggia", "leather belt craft"),
        ("calzolaio", "shoemaking"),
        ("restauro", "restoration painting"),
        ("incisione", "engraving"),
        ("liuteria", "violin making"),
        ("clarinetto", "clarinet"),
        ("occhiali", "eyeglasses antique"),
        ("pasta", "fresh pasta"),
        ("ricamo a punto", "needlework"),
        ("legno d'albero", "woodturning"),
        ("vernice", "lacquer work"),
        ("doratura", "gilding"),
        ("filigrana", "filigree"),
        ("lavori d'agro", "agricultural craft"),
        ("gesto e oggetto", "hand tool craft"),
        ("trasmissione tecnica", "apprenticeship craft"),
    ],
    "EL": [
        ("vino", "Greek wine"),
        ("vino produzione", "ancient Greek wine press"),
        ("oliva", "olive oil amphora"),
        ("olio oliva", "Greek olive oil"),
        ("acqua", "Greek water"),
        ("symposion", "symposium ancient Greek"),
        ("deipnon", "Greek banquet"),
        ("kylix", "kylix"),
        ("consumo rituale", "libation ancient Greece"),
        ("vino Maronea", "Maronia wine"),
        ("vino Creta", "Cretan wine"),
        ("kykeon", "kykeon"),
        ("birra", "ancient Greek beer"),
        ("caffè", "Greek coffee"),
        ("the", "Greek tea"),
        ("coppe dipinte", "Greek kylix painting"),
        ("inventari simposi", "symposium inventory"),
        ("vasi nomi", "Greek vase shapes"),
        ("vini dirottati", "Greek wine adulteration"),
        ("sete", "Thirst Greek myth"),
        ("ospitalità", "xenia hospitality"),
        ("brindisi", "Greek toast"),
        ("temperanza", "symposiarch"),
        ("vini Peloponneso", "Peloponnesian wine"),
        ("vini isole", "island wine Greece"),
        ("mosto", "must grape"),
        ("conservazione", "wine amphora storage"),
        ("trasporto botti", "wine transport amphora"),
        ("tavola", "symposium klinai"),
        ("brindisi atleti", "ancient Greek athletes"),
    ],
}

# Il ferrarese non ha un oggetto fisico: le sue trenta voci sono campi da
# rilevare, e non esiste immagine che li rappresenti. Non è una ricerca
# saltata: è una categoria, dichiarata come tale.

LIB_OK = re.compile(
    r"public domain|pubblico dominio|\bpd\b|cc0|no restrictions"
    r"|cc[- ]?by(?![a-ns])|cc[- ]?by[- ]sa|attribution", re.I)
LIB_NO = re.compile(r"non[- ]?commercial|fair use|\bcc by[- ]nc|no deriv", re.I)

API = "https://commons.wikimedia.org/w/api.php"


def get(params, tries=4):
    for k in range(tries):
        try:
            r = urllib.request.Request(
                API + "?" + urllib.parse.urlencode(params),
                headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(r, timeout=60) as f:
                return json.load(f)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 8 * (k + 1)
                time.sleep(att)
                continue
            return {"_errore": "HTTP %d" % e.code}
        except Exception:
            time.sleep(2 * (k + 1))
    return {"_errore": "insuccesso"}


def cerca(termini, limite=8):
    """Nomi di file su Commons per un termine, con la licenza di ognuno."""
    out = []
    for termine in termini:
        d = get({
            "action": "query", "format": "json", "generator": "search",
            "gsrsearch": "filetype:bitmap %s" % termine, "gsrnamespace": "6",
            "gsrlimit": str(limite), "prop": "imageinfo",
            "iiprop": "extmetadata|url|size", "iiurlwidth": "160",
        })
        if "_errore" in d:
            continue
        for pagina in (d.get("query", {}).get("pages", {}) or {}).values():
            ii = (pagina.get("imageinfo") or [{}])[0]
            meta = ii.get("extmetadata", {}) or {}

            def val(k):
                return (meta.get(k, {}) or {}).get("value", "") or ""

            lic = re.sub(r"<[^>]+>", " ", val("LicenseShortName")) or val("License")
            autore = re.sub(r"<[^>]+>", " ", val("Artist")).strip()
            if not autore:
                autore = re.sub(r"<[^>]+>", " ", val("Credit")).strip()
            data = re.sub(r"<[^>]+>", " ", val("DateTimeOriginal")).strip()
            if LIB_NO.search(lic):
                continue
            if not LIB_OK.search(lic):
                continue
            out.append({
                "file": pagina.get("title", ""),
                "termino": termine,
                "licenza": lic.strip()[:80],
                "autore": autore[:120],
                "data": data[:60],
                "larghezza": ii.get("width"),
                "altezza": ii.get("height"),
                "url": ii.get("descriptionurl", ""),
            })
        if out:
            break
        time.sleep(0.4)
    return out


def unisci():
    """Unisce i file per lingua nel file unito, nell'ordine delle sei lingue."""
    unito = []
    for lingua in ("IT", "FE", "LA", "EN", "SI", "EL"):
        percorso = esito_di(lingua)
        if not os.path.exists(percorso):
            print("manca: %s" % percorso, file=sys.stderr)
            continue
        with open(percorso, encoding="utf-8") as f:
            unito += json.load(f)["risultati"]
    esito = {
        "versione": 1,
        "data": time.strftime("%Y-%m-%d"),
        "nota": "Proposte, non scelte, e non ancora guardate a vista: le scelte le "
                "fa una persona e si registrano in "
                "sorgenti/lingue/attestazione_oggetti.json con etichetta e "
                "motivo, come per i ritratti.",
        "risultati": unito,
    }
    with open(ESITO, "w", encoding="utf-8") as f:
        json.dump(esito, f, ensure_ascii=False, indent=1)
    print("unite %d voci in %s" % (len(unito), os.path.basename(ESITO)))
    return 0


def main():
    argomenti = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--unisci" in sys.argv:
        return unisci()
    if "--ripeti" in sys.argv and os.path.exists(ESITO):
        with open(ESITO, encoding="utf-8") as f:
            dati = json.load(f)
        for a in dati["risultati"]:
            print("%s %-3d %-34s %d candidati" % (a["lingua"], a["numero"],
                                                 a["voce"][:34], len(a["candidati"])))
        return 0

    with open(ASSOC, encoding="utf-8") as f:
        assoc = {a["lingua"]: a for a in json.load(f)["associazioni"]}

    lingue = argomenti or ["IT", "LA", "EN", "SI", "EL"]
    ricalcola = "--ricalcola" in sys.argv
    risultati = []
    for lingua in lingue:
        voci = assoc[lingua]["voci"]
        termini = TERMINI.get(lingua, [])
        for i, voce in enumerate(voci):
            if lingua == "FE":
                risultati.append({
                    "lingua": "FE", "numero": i + 1, "voce": voce,
                    "termini": [],
                    "categoria": "nessuna",
                    "motivo": "campo di rilevazione, non oggetto: non esiste "
                              "immagine che rappresenti un campo di raccolta",
                    "candidati": [],
                })
                print("FE %-3d %-34s — campo di rilevazione" % (i + 1, voce[:34]))
                continue
            if i >= len(termini):
                print("MANCA IL TERMINE %s %d" % (lingua, i + 1), file=sys.stderr)
                continue
            if ricalcola and os.path.exists(esito_di(lingua)):
                # i candidati sono già stati trovati: si rilegge il file e si
                # aggiunge solo il campo `termini`, senza interrogare la rete
                with open(esito_di(lingua), encoding="utf-8") as f:
                    vecchio = json.load(f)
                candidati = next(
                    (x["candidati"] for x in vecchio["risultati"]
                     if x["numero"] == i + 1), [])
            else:
                candidati = cerca(termini[i])
            risultati.append({
                "lingua": lingua, "numero": i + 1, "voce": voce,
                "termini": [t[0] for t in termini[i]] + [t[1] for t in termini[i]],
                "categoria": "da_vedere" if candidati else "nessuna",
                "motivo": "" if candidati else "nessun risultato libero per i termini usati",
                "candidati": candidati,
            })
            print("%s %-3d %-34s %d candidati" % (lingua, i + 1, voce[:34], len(candidati)))
            time.sleep(0.3)

    esito = {
        "versione": 1,
        "data": time.strftime("%Y-%m-%d"),
        "nota": "Proposte, non scelte, e non ancora guardate a vista: le scelte le "
                "fa una persona e si registrano in "
                "sorgenti/lingue/attestazione_oggetti.json con etichetta e "
                "motivo, come per i ritratti.",
        "lingue": lingue,
        "risultati": risultati,
    }
    destinazione = esito_di(lingue[0]) if len(lingue) == 1 else ESITO
    with open(destinazione, "w", encoding="utf-8") as f:
        json.dump(esito, f, ensure_ascii=False, indent=1)
    print("scritto:", os.path.relpath(destinazione, RADICE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
