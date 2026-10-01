"""Cerca i ritratti autentici dei personaggi del gioco e ne controlla la licenza.

Percorso, in poche richieste:
1. l'API di Wikipedia risolve fino a 50 titoli per volta e restituisce
   l'immagine in testa all'articolo;
2. il nome del file va su Wikimedia Commons, che restituisce licenza e autore;
3. **sono accettate solo** pubblico dominio, CC0, CC BY e CC BY-SA: sono le
   licenze che il progetto usa gia'. Il resto e' scartato e registrato.

Non scarica immagini: qui si interroga e si decide. Il download e la riduzione a
48x54 sono in `ritratto_reale.py`, che riguarda solo questo elenco.

DIFETTO CORRETTO NELLA SECONDA VERSIONE, E DA NON RIPETERE
----------------------------------------------------------
La prima versione chiedeva 50 nomi per richiesta e, quando la risposta non
arrivava, semplicemente non aveva piu' immagini: scriveva allora
«nessun ritratto in testa all'articolo di Wikipedia». Ma Wikipedia risponde
**HTTP 429 Too Many Requests** quando le richieste si susseguono troppo
veloce, e quel codice di errore finiva letto come «non esiste».

Il risultato era che quindici personaggi con un ritratto celebre e documentato
— Durer, Turing, Leibniz, John Snow, Alonzo Church, Josquin, Bellini — venivano
dichiarati privi di ritratto. Non era un errore di ricerca: era un fatto falso
scritto come se fosse vero, in un progetto che chiede esattamente di non farlo.

Due correzioni, qui dentro:
- `Client` rispetta un intervallo minimo fra le richieste, e su 429 aspetta il
  tempo indicato da `Retry-After` invece di arrendersi;
- l'esito distingue `non_trovato` (risposta avuta, nessuna immagine) da
  `richiesta_fallita` (nessuna risposta). **Una richiesta fallita non genera mai
  una conclusione**: un personaggio resta `da_rivedere` finche' non e' stato
  interrogato con successo.

Nota sul perche' non si usa il motore di ricerca di Wikidata: `wbsearchentities`
risponde in circa 5 secondi a nome e per 213 nomi servirebbero quasi venti
minuti; inoltre il servizio SPARQL di Wikidata e' in questo momento limitato a
una richiesta al minuto per un guasto in corso.
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ART = os.path.join(RADICE, "sorgenti", "art")
ROSTER = os.path.join(ART, "roster.json")
ESITO = os.path.join(ART, "ritratti_disponibili.json")

UA = "i-cinque-duchi/0.3 (progetto didattico per liceo; pietrofabbri)"

# Licenze accettate: pubblico dominio, CC0, CC BY e CC BY-SA, che sono le
# uniche che il progetto usa gia'. «Attribution» e «No restrictions» sono i
# nomi brevi che Commons da' rispettivamente a CC BY e a CC0, e vanno accettati:
# la prima versione li scartava perche' cercava solo le sigle.
LIB_OK = re.compile(
    r"public domain|pubblico dominio|\bpd\b|cc0|no restrictions|attribution"
    r"|cc[- ]?by(?![a-z])|creative commons", re.I)
LIB_NO = re.compile(r"non[- ]?commercial|fair use|\bcc by[- ]nc|no deriv", re.I)

PAUSA = 5.0          # secondi fra due richieste allo stesso servizio
NON_TROVATO = "non_trovato"
FALLITO = "richiesta_fallita"


class Client:
    """Richieste a Wikipedia e Commons, con il passo lento e la pazienza per i
    429. Un insuccesso e' un insuccesso: non viene mai trasformato in una
    risposta negativa, perche' su questa distinzione si regge tutta la
    distinzione fra «non c'e'» e «non ho potuto guardare»."""

    def __init__(self, pausa=PAUSA):
        self.pausa = pausa
        self._ultimo = {}
        self.rientri = 0

    def _aspetta(self, host):
        t = self._ultimo.get(host)
        if t is not None:
            d = self.pausa - (time.time() - t)
            if d > 0:
                time.sleep(d)
        self._ultimo[host] = time.time()

    def get(self, url, params, tries=5):
        host = urllib.parse.urlparse(url).netloc
        for k in range(tries):
            self._aspetta(host)
            full = url + "?" + urllib.parse.urlencode(params)
            try:
                r = urllib.request.Request(
                    full, headers={"User-Agent": UA, "Accept": "application/json"})
                with urllib.request.urlopen(r, timeout=60) as f:
                    return json.load(f)
            except urllib.error.HTTPError as e:
                if e.code in (429, 503):
                    # il servizio chiede di aspettare: si ascolta, non si insiste
                    att = float(e.headers.get("Retry-After") or 0) or 8 * (k + 1)
                    self.rientri += 1
                    print("    429/503, attendo %.0f s" % att, flush=True)
                    time.sleep(att)
                    continue
                if k == tries - 1:
                    return {"_errore": "HTTP %d" % e.code}
                time.sleep(2 * (k + 1))
            except Exception as e:
                if k == tries - 1:
                    return {"_errore": str(e)[:80]}
                time.sleep(2 * (k + 1))
        return {"_errore": "insuccesso dopo %d tentativi" % tries}

    def post(self, url, params, tries=5):
        host = urllib.parse.urlparse(url).netloc
        for k in range(tries):
            self._aspetta(host)
            try:
                corpo = urllib.parse.urlencode(params).encode()
                r = urllib.request.Request(url, data=corpo, headers={
                    "User-Agent": UA, "Accept": "application/json",
                    "Content-Type": "application/x-www-form-urlencoded"})
                with urllib.request.urlopen(r, timeout=60) as f:
                    return json.load(f)
            except urllib.error.HTTPError as e:
                if e.code in (429, 503):
                    att = float(e.headers.get("Retry-After") or 0) or 8 * (k + 1)
                    self.rientri += 1
                    print("    429/503, attendo %.0f s" % att, flush=True)
                    time.sleep(att)
                    continue
                if k == tries - 1:
                    return {"_errore": "HTTP %d" % e.code}
                time.sleep(2 * (k + 1))
            except Exception as e:
                if k == tries - 1:
                    return {"_errore": str(e)[:80]}
                time.sleep(2 * (k + 1))
        return {"_errore": "insuccesso dopo %d tentativi" % tries}

    def api(self, wiki, params, host="wikipedia.org"):
        return self.get("https://" + wiki + "." + host + "/w/api.php", params)


def lotti(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def normalizza(nome):
    """Toglie dal nome quello che non fa parte del titolo dell'articolo.

    Necessario perche' il roster porta ancora il seguito delle schede: nomi come
    «Leon Battista Alberti *(aggiunta» o «Guido Monaco (Guido d'Arezzo) a
    Pomposa» non sono titoli, e mandarli cosi' a Wikipedia non trovava nulla
    senza che l'errore fosse distinguibile da un ritratto inesistente."""
    n = re.sub(r"\*\s*\(aggiunta.*$", "", nome)
    n = re.sub(r"\(aggiunta.*$", "", n)
    n = re.sub(r"\s*\ba\s+[A-ZÀ-Ý][\w'’ ]*$", "", n)
    n = re.sub(r"\(Guido d'Arezzo\)", "", n)
    n = re.sub(r"\(Novello\)", "", n)
    n = re.sub(r",\s*detto il.*$", "", n)
    n = re.sub(r",\s*il\s+\".*?\".*$", "", n)
    n = re.sub(r"\s*\([^)]*\)", "", n)
    return re.sub(r"\s+", " ", n).strip(" .,")


# Titoli scelti guardando i risultati della ricerca, non a memoria. Ogni voce
# porta con se' perche' il titolo diretto non funziona: senza questa nota il
# prossimo che ci mette le mani riscrive la stessa ricerca a memoria.
TITOLI = {
    "P03": ("Guido d'Arezzo", "it"),
    "P10": ("Azzo II d'Este", "it"),
    "P15": ("Nicolò II d'Este", "it"),
    "P27": ("Taddeo Crivelli", "it"),
    "P31": ("Biagio Rossetti", "it"),
    "P40": ("Ludovico Bonaccioli", "it"),
    "P46": ("Giovanni Battista Canani", "it"),
    "P47": ("Benvenuto Tisi", "it"),
    "P58": ("Clemente VIII", "it"),
    "P59": ("Bartolomeo Chiozzi", "it"),
    "P60": ("Riccardo Bacchelli", "it"),
    "P67": ("Domenico Malagutti", "it"),
    "P68": ("Giacomo Succi (medico)", "it"),
    "P70": ("Gioacchino Bonnet", "it"),
    "P76": ("Carlo Savonuzzi", "it"),
    "P77": ("Alda Costa", "it"),
    "P80": ("Renata Viganò", "it"),
    "P83": ("Giulio Natta", "it"),
    "Q62": ("Leon Battista Alberti", "it"),
    "Q108": ("Federico II del Sacro Romano Impero", "it"),
    "Q117": ("Josquin Desprez", "it"),
    "Q120": ("Giovanni Bellini", "it"),
    "Q124": ("Albrecht Dürer", "it"),
    "Q125": ("Aldo Manuzio", "it"),
    "Q126": ("William Caxton", "en"),
    "Q128": ("Alan Turing", "en"),
    "Q207": ("Gottfried Wilhelm Leibniz", "en"),
    "Q308": ("Sergej Korolëv", "en"),
    "Q309": ("John Snow", "en"),
    "Q314": ("Alonzo Church", "en"),
    "Q319": ("Donald Davies (engineer)", "en"),
    "Q324": ("James Ellis (cryptographer)", "en"),
}
# duplicati di schede: la stessa persona compare due volte, con due codici
DUPLICA = {"P31": "Q64"}


def pageimages(cli, wiki, titoli):
    """titoli -> nome del file dell'immagine in testa. None = non interrogato."""
    d = cli.api(wiki, {"prop": "pageimages", "piprop": "original",
                       "redirects": "1", "titles": "|".join(titoli)})
    if "_errore" in d:
        print("    richiesta fallita su %s: %s" % (wiki, d["_errore"]), flush=True)
        return None
    q = d.get("query", {})
    alias = {}
    for r in (q.get("normalized") or []) + (q.get("redirects") or []):
        alias[r["to"]] = r["from"]
    fuori = {}
    for pag in (q.get("pages") or {}).values():
        titolo = pag.get("title")
        ori = (pag.get("original") or {}).get("source")
        if not titolo or not ori:
            continue
        # il nome del file arriva codificato per l'URL (spazi %20, apostrofi
        # %27): senza decodificarlo, Commons non lo trova
        nome = urllib.parse.unquote(ori.split("/")[-1].split("?")[0])
        fuori[titolo] = nome
        for nuovo, vecchio in alias.items():
            if nuovo == titolo:
                fuori[vecchio] = nome
    return fuori


def licenze_commons(cli, file_names):
    """Commons: nome file -> licenza, autore, url."""
    d = cli.post("https://commons.wikimedia.org/w/api.php", {
        "action": "query", "format": "json", "prop": "imageinfo",
        "iiprop": "extmetadata|url|size",
        "titles": "|".join("File:" + f for f in file_names)})
    if "_errore" in d:
        print("    richiesta fallita su Commons: %s" % d["_errore"], flush=True)
        return None
    su = {}
    for _, p in (d.get("query", {}).get("pages") or {}).items():
        ii = (p.get("imageinfo") or [None])[0]
        if not ii:
            continue
        em = ii.get("extmetadata", {})
        # Commons restituisce il titolo con spazi («File:Leonardo self.jpg»)
        # mentre la richiesta usava i trattini bassi: senza normalizzare, ogni
        # file sembra non trovarsi
        chiave = p["title"].split(":", 1)[-1].replace("_", " ").strip()
        su[chiave] = {
            "licenza": (em.get("LicenseShortName", {}) or {}).get("value", ""),
            "autore": re.sub(r"<[^>]+>", "",
                             (em.get("Artist", {}) or {}).get("value", ""))[:120],
            "url": ii.get("url"),
            "larghezza": ii.get("width"),
            "altezza": ii.get("height"),
        }
    return su


if __name__ == "__main__":
    roster = json.load(open(ROSTER, encoding="utf-8"))
    cli = Client()

    esiti = {}
    for p in roster:
        esiti[p["codice"]] = dict(
            codice=p["codice"], nome=p["nome"], anno=p["anno"], tipo=p["tipo"],
            vivo=bool(p.get("vivo")), titolo=None, pagina=None, immagine=None,
            dettagli=None, motivo="")

    # 1. le schede collettive e le persone vive non si cercano: non hanno un
    #    volto unico, o non hanno il diritto di averne uno qui
    for e in esiti.values():
        if e["tipo"] == "collettivo":
            e["motivo"] = "collettivo: non ha un volto unico"
        elif e["vivo"]:
            e["motivo"] = "persona viva: solo emblema"

    da_cercare = [e for e in esiti.values() if not e["motivo"]]
    print("da cercare: %d su %d" % (len(da_cercare), len(esiti)), flush=True)

    # 2. titoli diretti, con i titoli scelti a mano dove il nome del roster
    #    non coincide con il titolo dell'articolo
    per_gruppo = {}
    for e in da_cercare:
        titolo, wiki = TITOLI.get(e["codice"], (normalizza(e["nome"]), "it"))
        e["titolo"] = titolo
        per_gruppo.setdefault(wiki, []).append(e)

    trovate = {}
    for wiki, gruppo in per_gruppo.items():
        for blocco in lotti(gruppo, 40):
            titoli = [e["titolo"] for e in blocco]
            out = pageimages(cli, wiki, titoli)
            if out is None:
                for e in blocco:
                    e["motivo"] = FALLITO + ": wikipedia non raggiungibile"
                continue
            for e in blocco:
                img = out.get(e["titolo"])
                if img:
                    e["immagine"] = img
                    e["pagina"] = e["titolo"]
                    trovate[img] = None
                else:
                    e["motivo"] = NON_TROVATO + ": nessuna immagine in testa all'articolo"
            print("  %s: interrogati %d" % (wiki, len(blocco)), flush=True)

    # 3. seconda chance sull'altra lingua, per chi e' rimasto senza: su en
    #    wikipedia i titoli di molti nomi non italiani sono diversi
    rimasti = [e for e in da_cercare if not e["immagine"] and not e["motivo"].startswith(FALLITO)]
    if rimasti:
        print("seconda chance su en per %d schede" % len(rimasti), flush=True)
        for e in rimasti:
            titolo, _ = TITOLI.get(e["codice"], (None, None))
            if titolo is None:
                continue
            out = pageimages(cli, "en", [titolo])
            if out and out.get(titolo):
                e["immagine"] = out[titolo]
                e["pagina"] = titolo
                trovate[out[titolo]] = None

    # 4. licenze, a lotti da 40 per non superare il limite di lunghezza
    licenze = {}
    for blocco in lotti(sorted(trovate), 30):
        su = licenze_commons(cli, blocco)
        if su is None:
            continue
        licenze.update(su)
        print("  commons: %d file" % len(licenze), flush=True)

    for e in da_cercare:
        if not e["immagine"]:
            continue
        det = licenze.get(e["immagine"].replace("_", " ").strip())
        if not det:
            e["motivo"] = FALLITO + ": file non letto su Commons"
            continue
        if LIB_NO.search(det["licenza"]) or not LIB_OK.search(det["licenza"]):
            e["motivo"] = "licenza non utilizzabile: " + det["licenza"]
            e["dettagli"] = det
            continue
        e["dettagli"] = det
        e["motivo"] = "ok"

    # 5. i duplicati ricevono la stessa immagine della scheda gemella
    for gemello, doppio in DUPLICA.items():
        if gemello in esiti and doppio in esiti and esiti[gemello]["motivo"] == "ok":
            esiti[doppio]["immagine"] = esiti[gemello]["immagine"]
            esiti[doppio]["dettagli"] = esiti[gemello]["dettagli"]
            esiti[doppio]["pagina"] = esiti[gemello]["pagina"]
            esiti[doppio]["motivo"] = "ok (stessa persona di " + gemello + ")"

    lista = [esiti[p["codice"]] for p in roster]
    with open(ESITO, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=1)

    ok = [e for e in lista if e["motivo"].startswith("ok")]
    import collections
    print("\ntotale %d" % len(lista))
    print("  ritratti autentici utilizzabili : %d" % len(ok))
    print("  emblemi (collettivi o vivi)     : %d"
          % sum(1 for e in lista if "emblema" in e["motivo"] or "collettivo" in e["motivo"]))
    print("  senza ritratto, verificato       : %d"
          % sum(1 for e in lista if e["motivo"].startswith(NON_TROVATO)))
    print("  DA RIVEDERE (richieste fallite)  : %d"
          % sum(1 for e in lista if e["motivo"].startswith(FALLITO)))
    print("  rientri per 429/503 durante la ricerca: %d" % cli.rientri)
    print("\nlicenze accettate:")
    for k, v in collections.Counter(e["dettagli"]["licenza"] for e in ok).most_common():
        print("   %4d  %s" % (v, k))
    print("\nDA RIVEDERE:")
    for e in lista:
        if e["motivo"].startswith(FALLITO):
            print("  %-6s %-40s %s" % (e["codice"], e["nome"][:40], e["motivo"]))
