"""Scarica il testo integrale dell'Orlando furioso dall'edizione del 1928.

Perché Wikisource e non altro. Le altre strade sono state scartate una per
una, e le ragioni vanno dette, perché sono il tipo di difetto che non si vede:

* **Project Gutenberg 3747** contiene soltanto i **16 canti** della prima
  parte, in un'edizione *modernizzata* («inchiostro» per «inchïostro»).
  Serve per una citazione, non per un gioco che ha 30 livelli.
* **Liber Liber** restituisce 404 sull'URL del testo e un HTML da 1,9 MB
  mescolato con le introduzioni di un curatore moderno. Testo non estraibile.
* **Internet Archive** `orlandofuriosod00ariogoog` è un **OCR rovinato**:
  «nocquer taii» per «no' quer' tai», doppi spazi ovunque. Su un OCR non si
  cita, e una citazione sbagliata in un compito è un danno, non un vezzo.
* **Wikisource it, `Orlando furioso (1928)`**: edizione della Biblioteca BEIC
  in pubblico dominio, trascritta dal digitalizzato, 46 sottopagine. Il testo
  è nella zona `Pagina:` e porta il numero d'ottava esplicito: `{{O|8|of}}`.

La regola che governa anche questo file: *una richiesta che non arriva non è
una risposta negativa*. Se una chiamata API fallisce, si distingue `non
trovato` (la pagina non esiste davvero) da `richiesta_fallita` (rete, 429,
timeout) e si riprova; `Retry-After` viene rispettato.

Uso:  python3 scarica_wikisource.py            -> dati/furioso/pagine_wikisource.jsonl
      python3 scarica_wikisource.py --verifica  -> riverifica la copertura
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
API = "https://it.wikisource.org/w/api.php"
OUT = os.path.join(RADICE, "dati", "furioso", "pagine_wikisource.jsonl")
UTENTE = "cinque-duchi/0.1 (progetto didattico)"
CANTI = 46

# La pagina di un canto non contiene il testo: contiene un <pages .../> che
# richiama le pagine del digitalizzato. Per questo non basta prop=revisions
# sul canto, e non basta prop=extracts (restituisce 0 caratteri, perché il
# testo vive nelle sotto-pagine e non viene incluso nell'estrazione).
PAGES = re.compile(r'<pages\s+index="([^"]+)"\s+from=(\d+)\s+to=(\d+)')


def chiama(parametri, tentativi=5):
    """Chiamata all'API con distinzione netta fra 'non trovato' e 'fallita'."""
    url = API + "?" + urllib.parse.urlencode(parametri)
    errore = None
    for n in range(tentativi):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UTENTE})
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            corpo = e.read().decode("utf-8", "replace")[:200]
            errore = "HTTP %s %s" % (e.code, corpo)
            if e.code == 429:
                attesa = int(e.headers.get("Retry-After", "30"))
                print("   429: attendo %ds (Retry-After)" % attesa)
                time.sleep(attesa + 1)
                continue
            if 500 <= e.code < 600:
                time.sleep(3 * (n + 1))
                continue
            raise SystemExit("richiesta fallita e non riprendibile: %s" % errore)
        except Exception as e:                      # rete, DNS, timeout
            errore = "%s: %s" % (type(e).__name__, e)
            time.sleep(3 * (n + 1))
    raise SystemExit("richiesta fallita dopo %d tentativi: %s" % (tentativi, errore))


def contenuto(pagina):
    d = chiama({"action": "query", "prop": "revisions", "rvprop": "content",
                "rvslots": "main", "rvprop2": "", "format": "json",
                "formatversion": "2", "titles": pagina})
    p = d["query"]["pages"][0]
    if "revisions" not in p:
        return None                                  # non_trovato
    return p["revisions"][0]["slots"]["main"]["content"]


def mappa_pagine():
    """(canto) -> [(titolo Pagina:, numero)] per tutti i 46 canti."""
    titoli = ["Orlando furioso (1928)/Canto %d" % i for i in range(1, CANTI + 1)]
    mappa = {}
    for inizio in range(0, len(titoli), 20):
        lotto = titoli[inizio:inizio + 20]
        d = chiama({"action": "query", "prop": "revisions", "rvprop": "content",
                    "rvslots": "main", "format": "json", "formatversion": "2",
                    "titles": "|".join(lotto)})
        for p in d["query"]["pages"]:
            testo = p.get("revisions", [{}])[0].get("slots", {}).get("main", {}).get("content", "")
            blocchi = PAGES.findall(testo)
            if not blocchi:
                raise SystemExit("nessun <pages/> in %s: formato cambiato?" % p["title"])
            canto = int(p["title"].rsplit(" ", 1)[1])
            pagine = []
            for indice, da, a in blocchi:
                for n in range(int(da), int(a) + 1):
                    pagine.append((indice, n))
            mappa[canto] = pagine
        time.sleep(0.5)
    return mappa


def scarica(mappa):
    titoli = []
    for canto in sorted(mappa):
        for indice, n in mappa[canto]:
            titoli.append((canto, "Pagina:%s/%d" % (indice, n)))
    print("pagine da scaricare: %d" % len(titoli))
    righe = []
    mancanti = []
    for inizio in range(0, len(titoli), 50):
        lotto = titoli[inizio:inizio + 50]
        d = chiama({"action": "query", "prop": "revisions", "rvprop": "content",
                    "rvslots": "main", "format": "json", "formatversion": "2",
                    "titles": "|".join(t[1] for t in lotto)})
        per_titolo = {}
        for p in d["query"]["pages"]:
            per_titolo[p["title"]] = p.get("revisions", [{}])[0].get("slots", {}).get("main", {}).get("content", "")
        for canto, titolo in lotto:
            testo = per_titolo.get(titolo)
            if testo is None:
                mancanti.append(titolo)             # non_trovato, non fallita
                continue
            righe.append({"canto": canto, "pagina": titolo, "wikitext": testo})
        print("  %d/%d" % (min(inizio + 50, len(titoli)), len(titoli)))
        time.sleep(0.4)
    return righe, mancanti


if __name__ == "__main__":
    if "--verifica" in sys.argv:
        righe = [json.loads(l) for l in open(OUT, encoding="utf-8")]
    else:
        mappa = mappa_pagine()
        righe, mancanti = scarica(mappa)
        if mancanti:
            print("pagine non trovate (%d): %s" % (len(mancanti), mancanti[:5]))
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "w", encoding="utf-8") as f:
            for r in righe:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print("scritte %d righe in %s" % (len(righe), OUT))

    per_canto = {}
    for r in righe:
        per_canto.setdefault(r["canto"], 0)
        per_canto[r["canto"]] += 1
    print("canti coperti: %d/%d" % (len(per_canto), CANTI))
    for c in range(1, CANTI + 1):
        if c not in per_canto:
            print("  canto %d: ASSENTE" % c)
    print("pagine per canto: min %d, max %d"
          % (min(per_canto.values()), max(per_canto.values())))