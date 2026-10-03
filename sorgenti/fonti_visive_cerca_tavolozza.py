"""Cerca i campionari di colore per la tavolozza, su Wikimedia Commons.

La tavolozza (`dati/fonti_visive/tavolozza.json`) non si sceglie a occhio: si
costruisce da una fonte e si dichiara. Questo file è il primo passo, e cerca i
**campionari**: i pigmenti e le tinture da cui prendere i colori.

Le quattro voci sono le stesse che `fonti_visive.md` §3.4 dichiara, e sono
scelte perché coprano i tre sistemi di immagini che il gioco ha:

- **terre d'oliva** — il paesaggio ferrarese, cioè i fondi geografici dell'anno 1;
- **tinte dei manoscritti miniati** — le immagini degli oggetti linguistici;
- **motivi dei tessili** — gli oggetti e le scene con persone;
- **colori degli affreschi** — i ritratti e le architetture.

Il difetto della ricerca su Commons, dichiarato in `fonti_visive.md` §5, si
ripete qui ed è per questo che il file dichiara i campioni uno per uno: una
ricerca per parola restituisce immagini che hanno il nome del colore ma non il
colore. Un campione di «verde senape» che è una fotografia di una bottiglia
non è un campione di verde senape, e il file lo segnala come
`campione_non_confermato` invece di farlo entrare in tavolozza.

Uso:  python3 sorgenti/fonti_visive_cerca_tavolozza.py
      python3 sorgenti/fonti_visive_cerca_tavolozza.py --prova
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USCITA = os.path.join(RADICE, "dati", "fonti_visive", "tavolozza_candidati.json")
UA = "i-cinque-duchi/0.1 (progetto didattico per liceo; pietrofabbri)"
API = "https://commons.wikimedia.org/w/api.php"

# Le quattro famiglie, ognuna con i termini cercati. I termini sono in
# inglese perche' su Commons le categorie tecniche sono in inglese, e questo e'
# il motivo per cui la ricerca precedente ha funzionato: cercare «terre
# d'oliva Ferrara» in italiano non porta niente.
FAMIGLIE = [
    {"famiglia": "terre_oliva", "uso": "fondi geografici dell'anno 1",
     "termini": ["olive oil painting pigment", "terre verte verte d'oliva",
                 "green earth pigment", "terre d'Italie palette"]},
    {"famiglia": "tinte_miniatura", "uso": "immagini degli oggetti linguistici",
     "termini": ["illuminated manuscript pigments palette",
                 "manuscript illumination colours", "azurite malachite pigment"]},
    {"famiglia": "tessili", "uso": "oggetti e scene con persone",
     "termini": ["Italian Renaissance textile pattern", "velvet brocade Italian",
                 "damask fabric Renaissance"]},
    {"famiglia": "affreschi", "uso": "ritratti e architetture",
     "termini": ["fresco pigment palette", "pigments Renaissance painting",
                 "earth pigments palette museum"]},
]


def api(parametri, tentativi=4):
    """Una chiamata all'API. Un 429 o un 503 non e' una risposta: si aspetta e
    si ritenta, perche' una risposta non riuscita che diventasse «nessun
    campione» metterebbe una vuoto falso in tavolozza.json."""
    url = API + "?" + urllib.parse.urlencode(parametri)
    for k in range(tentativi):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as f:
                return json.loads(f.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 4 * (k + 1)
                print(f"  {e.code}, attendo {att:.0f} s", flush=True)
                time.sleep(att)
                continue
            print("  HTTP %d su %s" % (e.code, termine(parametri)))
            return None
        except Exception as e:
            print("  %s: %s" % (type(e).__name__, e))
            time.sleep(3 * (k + 1))
    return None


def termine(parametri):
    return parametri.get("gsrsearch", "?")[:60]


def cerca(testo, limite=12):
    """Immagini su Commons che portano il termine nel titolo o nella descrizione."""
    d = api({
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": "filetype:bitmap " + testo, "gsrnamespace": "6",
        "gsrlimit": str(limite), "prop": "imageinfo",
        "iiprop": "url|size|extmetadata|mime",
    })
    if not d or "query" not in d:
        return []
    out = []
    for pag in d["query"].get("pages", {}).values():
        ii = (pag.get("imageinfo") or [{}])[0]
        meta = ii.get("extmetadata") or {}
        out.append({
            "file": "File:" + pag.get("title", "").replace("File:", ""),
            "termine": testo,
            "licenza": (meta.get("LicenseShortName") or {}).get("value", ""),
            "autore": (meta.get("Artist") or {}).get("value", "")[:120],
            "data": (meta.get("DateTimeOriginal") or {}).get("value", "")[:10],
            "larghezza": ii.get("width"),
            "altezza": ii.get("height"),
            "mime": ii.get("mime"),
            "url": "https://commons.wikimedia.org/wiki/" +
                   urllib.parse.quote(pag.get("title", "").replace(" ", "_")),
        })
    return out


def main():
    solo_prova = "--prova" in sys.argv
    risultati = []
    for famiglia in FAMIGLIE:
        trovati = []
        for t in famiglia["termini"]:
            campioni = cerca(t)
            print("  %-22s %-46s %d" % (famiglia["famiglia"], t[:44], len(campioni)))
            trovati += campioni
            time.sleep(0.4)
        # un file puo' uscire da due termini: si tiene il primo e lo si dichiara
        visti = {}
        for c in trovati:
            visti.setdefault(c["file"], c)
        risultati.append({
            "famiglia": famiglia["famiglia"],
            "uso": famiglia["uso"],
            "termini": famiglia["termini"],
            "candidati": list(visti.values()),
            "stato": "campione_non_confermato",
            "nota": "nessun campione e' stato guardato: il file li porta "
                    "come candidati e non entra in tavolozza.json",
        })
    tot = sum(len(r["candidati"]) for r in risultati)
    print("famiglie: %d  campioni candidati: %d" % (len(risultati), tot))
    if solo_prova:
        return 0
    os.makedirs(os.path.dirname(USCITA), exist_ok=True)
    with open(USCITA, "w", encoding="utf-8") as f:
        json.dump({"versione": 1, "data": "2026-10-02",
                   "fonte": "Wikimedia Commons",
                   "risultati": risultati}, f, ensure_ascii=False, indent=1)
    print("scritto", os.path.relpath(USCITA, RADICE))
    return 0


if __name__ == "__main__":
    sys.exit(main())