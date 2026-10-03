"""Costruisce la tavolozza del gioco dai pigmenti storici, e non a occhio.

`fonti-visive.md` 4.2 pone la domanda e dice anche la regola: la tavolozza si
scrive **in un posto solo** (`dati/fonti_visive/tavolozza.json`), e ogni
immagine dichiara se entra coi colori della fonte o ricolorata. Questo file
produce quel file.

Il punto difficile non e' scrivere dei colori: e' **non sceglierli**. Un colore
scelto dall'occhio di chi scrive il codice e' un colore che nessun altro
riproduce, ed e' la ragione per cui due persone che colorano lo stesso dipinto
fanno due giochi diversi.

**La regola che questo file applica: un colore entra solo se una fonte
machine-readable lo dichiara.** Le due fonti sono entrambe verificabili da
programma, e ognuna viene citata nella voce che usa:

  wikidata_p465      il pigmento su Wikidata, per `P462` (proprieta' "colore")
                     porta a un oggetto colore, e quell'oggetto dichiara
                     l'esadecimale in `P465` (colore RGB canonico)
  wikipedia_infobox  l'esadecimale scritto nel campo colore dell'infobox
                     dell'artista del pigmento
  dichiarata         non e' un pigmento e non si finge che lo sia: e' un colore
                     di interfaccia, dichiarato per quello che e'

**Il difetto che la prima stesura di questo file aveva, e che e' la ragione
per cui non produceva niente.** Cercava il pigmento per nome con
`wbsearchentities` e poi leggeva `P462` sperando che fosse l'esadecimale. Sono
due errori:

1. la ricerca per nome non trova il pigmento. «vermilion» restituisce una
   citta' dell'Alberta, «red ochre» restituisce un premio, «minium» un
   genere di alga: il primo risultato non e' mai quello che si cerca. Per questo
   qui gli oggetti sono **espliciti** (`Q3348755` e non «yellow ochre»), e sono
   dichiarati accanto al nome, cosi' chi legge puo' controllarli a occhio;
2. `P462` non e' l'esadecimale, e' un collegamento a un altro oggetto. Su
   `Q1054292` (red ochre) `P462` vale `Q3348759`, che e' il *colore* «red
   ocher», e l'esadecimale `DD985C` sta li', in `P465`. La stringa che arriva
   al posto del colore e' un dizionario `{"entity-type": "item", ...}`, e
   senza accorgersene finisce nel file come colore. Per questo qui si
   controlla il tipo del valore e si scende di un passo.

Restano cinque pigmenti che **nessuna** delle due fonti dichiara in
esadecimale: il bianco di piombo, l'azzurite, la malachite, l'orpimento e il
giallo di piombo-stagno. Non si inventano: finiscono in
`pigmenti_senza_colore_macchina` con la prova, e le voci che servivano sono
state ricostruite su pigmenti che hanno invece una dichiarazione. Il giallo
che manca e' il giallo di Napoli (`FADA5E`), non il giallo di piombo-stagno:
sono due pigmenti diversi e la voce si chiama come il colore che usa.

I pigmenti scelti sono quelli che le fonti del progetto nominano, non quelli
che piacciono: la tavolozza del Fitzwilliam Museum elenca per un manoscritto
senese del 1446 «ochre, earth and lead white» per le carni, «ultramarine
blue, malachite green, insect-based organic pink, red earth and bright
lead-tin yellow» per i drappi. Sono quelli del Quattrocento, che e' il secolo
del progetto.

Uso:  python3 sorgenti/tavolozza_campioni.py
      python3 sorgenti/tavolozza_campioni.py --prova
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USCITA = os.path.join(RADICE, "dati", "fonti_visive", "tavolozza.json")
WD = "https://www.wikidata.org/w/api.php"
UA = "i-cinque-duchi/0.1 (progetto didattico per liceo; pietrofabbri)"

# Le voci della tavolozza. `ruolo` dice a che cosa serve il colore nel gioco.
# `wikidata` e' l'oggetto del pigmento, dichiarato per esteso perche' la ricerca
# per nome sbaglia: vedi la nota in cima al file. `pagina` e' l'artista di
# Wikipedia che dichiara l'esadecimale nell'infobox, quando la fonte e' quella.
# `hex` senza pigmento e' un colore dichiarato, e va motivato.
VOCI = [
    # --- terre e carni: i fondi e i volti
    {"chiave": "terra_gialla", "ruolo": "sabbia, terra, muri di terra",
     "pigmento": "Yellow ochre", "wikidata": "Q3348755",
     "pagina": "Yellow ochre", "famiglia": "terre_oliva"},
    {"chiave": "terra_rossa", "ruolo": "terreno ferrarese, mattoni",
     "pigmento": "Red ochre", "wikidata": "Q1054292",
     "pagina": "Red ochre", "famiglia": "terre_oliva"},
    {"chiave": "verde_terra", "ruolo": "paesaggio della pianura padana",
     "pigmento": "Green earth", "wikidata": "Q1552133",
     "pagina": "Green earth", "famiglia": "terre_oliva"},
    {"chiave": "bruno", "ruolo": "ombre, legno, terra profonda",
     "pigmento": "Umber", "wikidata": "Q901731",
     "pagina": "Umber", "famiglia": "terre_oliva"},
    # --- il bianco non e' un pigmento di miniatura: e' la carta e la calce
    {"chiave": "bianco_calce", "ruolo": "calce, muri, fondi delle miniature",
     "hex": "F5F2E8", "origine_dichiarata":
     "calce e carta, non pigmento: il bianco di piombo e' il pigmento "
     "storico, ma nessuna fonte machine-readable ne dichiara l'esadecimale "
     "(vedi pigmenti_senza_colore_macchina), e un bianco inventato sarebbe "
     "un colore a occhio. Qui il bianco e' la superficie su cui stanno gli "
     "altri, e si dichiara come tale"},
    # --- blu: il cielo e l'acqua, e il colore che costava di piu'
    {"chiave": "azzurro_oltremare", "ruolo": "cielo, acqua, ori preziosi",
     "pigmento": "Ultramarine", "wikidata": "Q219660",
     "pagina": "Ultramarine", "famiglia": "tinte_miniatura"},
    {"chiave": "blu", "ruolo": "strati profondi, distanza",
     "pigmento": "Smalt", "wikidata": "Q898977",
     "pagina": "Smalt", "famiglia": "tinte_miniatura"},
    {"chiave": "azzurro", "ruolo": "cielo lontano, ombre fredde",
     "hex": "4C7FA8", "origine_dichiarata":
     "azzurite dichiarata a occhio e non usata: il pigmento e' visitato in "
     "pigmenti_senza_colore_macchina, e l'artista ne da solo una descrizione "
     "in parole («azure-blue, dark to pale blue»), non un esadecimale. Il "
     "valore qui e' dichiarato e dichiarato come tale: se un domani vuole il "
     "colore dell'azzurite, va cercato un campione guardato a vista"},
    # --- rossi: il sangue e il pericolo
    {"chiave": "vermiglio", "ruolo": "segnalazione, errore, allarme",
     "pigmento": "Cinnabar", "wikidata": "Q104614",
     "pagina": "Vermilion", "famiglia": "tinte_miniatura"},
    {"chiave": "rosso_minio", "ruolo": "mattoni, tetti, corpi d'armi",
     "pigmento": "Minium", "wikidata": "Q17141476",
     "pagina": "Minium", "famiglia": "terre_oliva"},
    # --- verdi: i giardini e il verde d'uovo
    {"chiave": "verde_rame", "ruolo": "vegetazione, acqua ferma",
     "pigmento": "Verdigris", "wikidata": "Q2351119",
     "pagina": "Verdigris", "famiglia": "tinte_miniatura"},
    # --- gialli: l'oro e la luce
    {"chiave": "giallo", "ruolo": "luce, sole, segnalazione buona",
     "pigmento": "Naples yellow", "wikidata": None,
      "pagina": "Naples yellow", "famiglia": "tinte_miniatura",
     "nota": "il giallo di piombo-stagno, che e' il pigmento del Fitzwilliam, "
             "non ha esadecimale dichiarato da nessuna delle due fonti: questa "
             "voce usa il giallo di Napoli, che e' un altro pigmento, e lo "
             "dichiara"},
    # --- gli ori, che non si possono fare con un pigmento
    {"chiave": "oro", "ruolo": "oro foglia: tesori, cornici, lettering",
     "hex": "B08D3E", "origine_dichiarata":
     "l'oro foglia non ha un colore unico: cambia con la luce. Il valore qui "
     "e' quello medio dichiarato dal progetto, non un campione"},
]

# I ruoli che NON vengono da un pigmento storico. Sono colori di interfaccia e
# di stato, e il progetto deve dirlo: un colore di stato che si presenta come
# una tinta di manoscritto e' una bug che aspetta di essere notata.
STATO = [
    {"chiave": "sfondo", "ruolo": "fondo della scena",
     "hex": "EDE4D3", "origine_dichiarata":
     "carta, non pigmento: il fondo e' la carta, e la carta non e' un colore "
     "che si sceglie ma una superficie su cui gli altri stanno"},
    {"chiave": "inchiostro", "ruolo": "testo, etichette, numeri",
     "hex": "2B2622", "origine_dichiarata":
     "nero di fumo, che e' un pigmento (carbone di legna), ma qui serve come "
     "testo e non come campione: un testo nero non e' un campione di nero"},
    {"chiave": "ok", "ruolo": "livello superato",
     "hex": "4A7C59", "origine_dichiarata":
     "verde di stato, non storico: dichiarato come tale perche' il verde di "
     "Verdigris su schermo sembrerebbe una scelta estetica"},
    {"chiave": "attenzione", "ruolo": "avviso, verifica dovuta",
     "hex": "B8862B", "origine_dichiarata": "giallo di stato, non storico"},
    {"chiave": "errore", "ruolo": "errore, difetto, dichiarazione richiesta",
     "hex": "A6362A", "origine_dichiarata":
     "rosso di stato, non storico: e' vicino al vermiglio perche' l'occhio "
     "deve capire subito, e la vicinanza e' voluta"},
]

# I pigmenti visitati che nessuna delle due fonti dichiara in esadecimale. Non
# sono un errore: sono il risultato della ricerca, e vengono scritti nel file
# perche' la prossima persona non li cerchi di nuovo e non creda che sia un
# difetto del file invece che delle fonti.
SENZA = [
    {"pigmento": "Lead white", "wikidata": "Q116470614",
     "prova": "l'artista dichiara 'white pigment' e nessun esadecimale; "
              "l'artista italiano non esiste, 'Basic lead carbonate' non ha "
              "il campo"},
    {"pigmento": "Azurite", "wikidata": "Q2875250",
     "prova": "l'artista dichiara 'Azure-blue, dark to pale blue; pale blue in "
              "transmitted light': una descrizione, non un colore"},
    {"pigmento": "Malachite", "wikidata": "Q164411",
     "prova": "nessun P462 e nessun P465; l'artista dichiara una scala di "
              "verdi in parole, e l'oggetto 'malachite green' e' un "
              "composto chimico, non un colore"},
    {"pigmento": "Orpiment", "wikidata": "Q419183",
     "prova": "nessun P462 e nessun P465; l'artista dichiara 'Lemon-yellow to "
              "golden or brownish yellow'"},
    {"pigmento": "Lead-tin yellow", "wikidata": "Q883704",
     "prova": "nessun P462 e nessun P465 su nessuno dei tre oggetti "
              "(il pigmento e i tipi I e II); l'artista non dichiara il campo"},
]

# Le dichiarazioni che la ricerca ha trovato e che il file **non** usa, con la
# ragione. Vanno scritte perche' una tavolozza che nasconde le fonti che
# contraddicono quella scelta e' una tavolozza che mente per omissione.
ALTRE = [
    {"voce": "vermiglio", "fonte": "wikidata_p465", "oggetto": "Q737438",
     "hex": "E34234",
     "nota": "l'oggetto colore 'vermilion' dichiara E34234, l'artista sul "
             "pigmento dichiara FF4000. Due fonti, due esadecimali, e nessuna "
             "delle due e' sbagliata: e' lo stesso colore a due precisioni "
             "diverse. Il file tiene FF4000 e dichiara la differenza"},
]

# Il campo colore di un infobox: il nome del campo, e un esadecimale **puro**,
# di 6 cifre, o di 3 preceduto da cancelletto. La regola stretta serve perche'
# i campi colore di Wikipedia spesso contengono testo: «Lemon-yellow to golden
# or brownish yellow» e' un campo colore, ma non un colore, e un confronto
# troppo largo lo accetterebbe. C'e' anche `rgb(r, g, b)`, che si converte.
RE_INFOX = re.compile(
    r"(?im)^\s*\|\s*(?:colou?r|rgb|hex)\s*=\s*"
    r"(?:rgb\s*\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    r"|(#[0-9a-f]{3}|#[0-9a-f]{6}|[0-9a-f]{6})\s*$)")
RE_HEX = re.compile(r"^(?:[0-9A-F]{3}|[0-9A-F]{6})$")


def api(host, parametri, tentativi=5):
    url = host + "?" + urllib.parse.urlencode(parametri)
    for k in range(tentativi):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as f:
                return json.loads(f.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 10 * (k + 1)
                print("  %d, attendo %.0f s" % (e.code, att), flush=True)
                time.sleep(att)
                continue
            return None
        except Exception:
            time.sleep(6 * (k + 1))
    return None


def proprieta(entita, nome):
    """I valori della proprieta' `nome`, senza mai restituire un dizionario.

    Il controllo sul tipo e' la correzione del difetto: `P462` su un pigmento
    restituisce un oggetto (un dizionario), non una stringa, e la versione
    precedente lo scriveva nel file come se fosse un colore.
    """
    fuori = []
    for c in (entita.get("claims", {}) or {}).get(nome) or []:
        dv = (c.get("mainsnak", {}) or {}).get("datavalue") or {}
        v = dv.get("value")
        if isinstance(v, str):
            fuori.append(v.lstrip("#").upper())
        elif isinstance(v, dict) and v.get("entity-type") == "item":
            fuori.append(v["id"])           # un collegamento, non un colore
    return fuori


def entita(qid):
    d = api(WD, {"action": "wbgetentities", "format": "json", "ids": qid,
                 "props": "claims|labels|descriptions", "languages": "en|it"})
    if not d or "entities" not in d:
        return None
    return d["entities"].get(qid)


def colore_wikidata(qid):
    """Il colore dichiarato su Wikidata, e da dove viene.

    Due passi, nell'ordine in cui sono affidabili: prima `P465` sul pigmento
    stesso, che e' la dichiarazione piu' specifica; poi `P462`, che porta
    all'oggetto colore, e li' il `P465` di quell'oggetto.
    """
    e = entita(qid)
    if not e:
        return None, [], "risposta assente"
    catena = [qid]
    diretti = [h for h in proprieta(e, "P465") if RE_HEX.match(h)]
    if diretti:
        catena.append("P465")
        scarti = []
        for altro in proprieta(e, "P462"):
            ae = entita(altro)
            if not ae:
                continue
            for h in proprieta(ae, "P465"):
                if RE_HEX.match(h) and h not in diretti:
                    scarti.append("%s dichiara %s, un colore generico e non il "
                                  "pigmento: tiene %s" % (altro, h, diretti[0]))
        return diretti[0], catena, scarti

    for altro in proprieta(e, "P462"):
        ae = entita(altro)
        if not ae:
            continue
        catena.append("P462 " + altro)
        for h in proprieta(ae, "P465"):
            if RE_HEX.match(h):
                catena.append("P465")
                return h, catena, []
    return None, catena, ""


def blocco_infobox(wikitext):
    """Il testo del primo infobox, e non tutto l'artista.

    Serve perche' un articolo lungo contiene campi colore anche nel corpo e
    nella navigazione, e quelli non sono la dichiarazione del pigmento.
    """
    m = re.search(r"\{\{\s*[Ii]nfobox", wikitext)
    if not m:
        return ""
    i, profondita = m.start(), 0
    while i < len(wikitext) - 1:
        due = wikitext[i:i + 2]
        if due == "{{":
            profondita += 1
            i += 2
            continue
        if due == "}}":
            profondita -= 1
            i += 2
            if profondita == 0:
                return wikitext[m.start():i]
            continue
        i += 1
    return wikitext[m.start():]


def colore_infobox(pagina):
    """L'esadecimale dichiarato nel campo colore dell'infobox di un artista."""
    host = "https://en.wikipedia.org/w/api.php"
    d = api(host, {"action": "parse", "format": "json", "page": pagina,
                   "prop": "wikitext", "redirects": "1"})
    wt = (((d or {}).get("parse") or {}).get("wikitext") or {}).get("*", "")
    if not wt:
        return None, "wikitext assente"
    m = RE_INFOX.search(blocco_infobox(wt))
    if not m:
        return None, "nessun campo colore con esadecimale"
    r, g, b = m.group(1), m.group(2), m.group(3)
    if r and g and b:
        return "%02X%02X%02X" % (int(r), int(g), int(b)), None
    h = m.group(4)
    if h.startswith("#") and len(h) == 4:
        h = "".join(c * 2 for c in h[1:])
    return h.upper(), None


def main():
    solo_prova = "--prova" in sys.argv
    tavolozza, senza = [], []

    for v in VOCI:
        if v.get("hex"):
            tavolozza.append({"chiave": v["chiave"], "ruolo": v["ruolo"],
                              "hex": v["hex"].upper(),
                              "origine": "dichiarata",
                              "nota": v.get("origine_dichiarata", ""),
                              "famiglia": v.get("famiglia")})
            continue

        colore, catena, scarti = (None, [], "")
        if v.get("wikidata"):
            colore, catena, scarti = colore_wikidata(v["wikidata"])
            origine = "wikidata_p465"
        if not colore and v.get("pagina"):
            colore, difetto = colore_infobox(v["pagina"])
            if colore:
                origine = "wikipedia_infobox"
                catena = catena + ["infobox " + v["pagina"]]
                if difetto:
                    scarti = "; ".join(x for x in [scarti, difetto] if x)
            else:
                scarti = "; ".join(x for x in [scarti, difetto] if x)

        if colore:
            voce = {"chiave": v["chiave"], "ruolo": v["ruolo"],
                    "hex": colore, "origine": origine,
                    "pigmento": v["pigmento"], "famiglia": v.get("famiglia"),
                    "catena": catena}
            if v.get("wikidata"):
                voce["wikidata"] = v["wikidata"]
            if v.get("pagina"):
                voce["pagina"] = v["pagina"]
            if v.get("nota"):
                voce["nota"] = v["nota"]
            if scarti:
                voce["scarti"] = scarti
            tavolozza.append(voce)
            print("  %-18s %-16s %-8s %-18s %s"
                  % (v["chiave"], v["pigmento"], colore, origine,
                     " ".join(catena)))
        else:
            senza.append(v)
            print("  %-18s %-16s NESSUN COLORE (%s)"
                  % (v["chiave"], v["pigmento"], scarti or "fonti assenti"))
        time.sleep(0.6)

    for v in STATO:
        tavolozza.append({"chiave": v["chiave"], "ruolo": v["ruolo"],
                          "hex": v["hex"].upper(), "origine": "stato",
                          "nota": v["origine_dichiarata"]})

    da_pigmento = [v for v in tavolozza if v["origine"] in
                   ("wikidata_p465", "wikipedia_infobox")]
    print("\ntavolozza: %d voci (%d da pigmento, %d dichiarate, %d di stato)"
          % (len(tavolozza), len(da_pigmento), len(tavolozza) - len(da_pigmento)
             - len(STATO), len(STATO)))
    if senza:
        print("  senza colore dichiarato:",
              ", ".join(v["chiave"] for v in senza))
    if solo_prova:
        return 0

    os.makedirs(os.path.dirname(USCITA), exist_ok=True)
    doc = {
        "versione": 1,
        "data": "2026-10-03",
        "principio": "nessun colore e' scelto a occhio: un colore entra solo se "
                     "una fonte machine-readable lo dichiara, e la voce porta "
                     "la fonte. Le due fonti sono Wikidata (P462 porta "
                     "all'oggetto colore, P465 ne dichiara l'esadecimale) e "
                     "l'infobox dell'artista del pigmento su Wikipedia. Le "
                     "voci che non hanno pigmento sono marcate 'dichiarata' o "
                     "'stato' e non si fingono storiche",
        "uso": "le immagini entrano con i colori della fonte e portano "
               "l'etichetta che le dice che cosa sono (fotografia, dipinto, "
               "incisione, miniatura, rilievo, stampa): la tavolozza "
               "dichiara i colori del gioco, non ricolora le fonti",
        "voci": tavolozza,
        "senza_colore_dichiarato": [v["chiave"] for v in senza],
        "pigmenti_senza_colore_macchina": SENZA,
        "altre_dichiarazioni": ALTRE,
        "famiglie_raccolte": sorted({v["famiglia"] for v in tavolozza
                                     if v.get("famiglia")}),
        "famiglie_senza_voce": {
            "tessili": "i drappi avrebbero la malachite, che non ha "
                       "esadecimale dichiarato: il verde dei tessili e' "
                       "quello della terra verde, dichiarato",
            "affreschi": "gli affreschi avrebbero l'azzurite e l'orpimento, "
                         "che non hanno esadecimale dichiarato: l'azzurro e' "
                         "dichiarato a occhio e l'oro copre il giallo",
        },
        "campioni_cercati": "dati/fonti_visive/tavolozza_candidati.json",
        "campioni_guardati": 0,
        "nota_campioni": "nessun campione e' stato guardato a vista: la "
                         "ricerca su Commons ha restituito immagini il cui "
                         "titolo non promette il colore (il difetto e' "
                         "dichiarato in fonti-visive.md 5). I colori qui "
                         "vengono da fonti machine-readable, non dai "
                         "campioni: se un domani vuole i colori dai campioni, "
                         "va fatto riconoscendo le immagini a vista",
        "difetti_dichiarati": [
            "i cinque pigmenti di pigmenti_senza_colore_macchina non hanno "
            "esadecimale da nessuna delle due fonti: le voci che servivano "
            "sono state ricostruite su altri pigmenti, e il file non inventa",
            "lo smalt e l'umbra dichiarano un colore diverso dal loro "
            "oggetto colore (003399 contro 0000FF, 635147 contro 964B00): "
            "tiene il colore del pigmento, e la differenza e' negli scarti "
            "della voce",
            "il vermiglio ha due dichiarazioni in due fonti diverse: e' in "
            "altre_dichiarazioni",
            "due famiglie di campionari ('tessili' e 'affreschi') non hanno "
            "una voce propria: e' in famiglie_senza_voce",
            "l'azzurro e' l'unico colore dichiarato a occhio fra i colori di "
            "pigmento, e la voce dice perche'",
        ],
    }
    with open(USCITA, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print("scritto", os.path.relpath(USCITA, RADICE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
