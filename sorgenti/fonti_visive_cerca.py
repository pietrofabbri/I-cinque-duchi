"""Cerca su Wikimedia Commons le fonti visive per ciò che il gioco non ha
ancora una veste grafica.

Il gioco ha: i **fondi geografici** (19 file Natural Earth), i **213 ritratti**
dei personaggi, e le **180 immagini degli oggetti** linguistici. Non ha altre
cinque cose, e sono elencate qui perché ognuna ha una fonte diversa e un
problema diverso:

  mezzo        i mezzi di trasporto del percorso del duca: nessuno ha un'immagine
  edificio     le sagome degli edifici, che vengono da OpenStreetMap
  epigrafe     le iscrizioni, che sono fonti e non immagini
  incidente    i dettagli storici che hanno bisogno di un'immagine (un incendio,
               una battaglia) e che non hanno nessuna fonte dichiarata
  colore       le tavolozze di riferimento, per non dipingere tutto a caso

Per ogni voce si cercano i nomi dei file su Commons, con la stessa regola dei
ritratti e degli oggetti: **la ricerca propone, una persona decide**, e la
decisione si registra in `dati/fonti_visive/attestazione.json` con etichetta e
motivo.

Uso:
    python3 sorgenti/fonti_visive_cerca.py                 # tutte le categorie
    python3 sorgenti/fonti_visive_cerca.py mezzo edificio  # due categorie
"""
import collections
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

RADICE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CARTELLA = os.path.join(RADICE, "dati", "fonti_visive")
ESITO = os.path.join(CARTELLA, "fonti_visive.json")
ATTESTAZIONE = os.path.join(CARTELLA, "attestazione.json")

API = "https://commons.wikimedia.org/w/api.php"
UA = "i-cinque-duchi/0.1 (progetto didattico per liceo; pietrofabbri)"

# Le voci da cercare, per categoria. I termini sono scelti uno per uno: la
# ricerca automatica sbaglia il soggetto se si traduce alla cieca, e su questi
# nomomi la traduzione non funziona.
VOCI = {
    "mezzo": {
        "a piedi": ["Quattrocento pedestrian Renaissance painting", "medieval pilgrim walking"],
        "mulo": ["mulo di somma incisione", "pack mule drawing 19th century"],
        "cavallo": ["cavaliere quattrocento dipinto", "horse rider Renaissance painting"],
        "galera": ["galera veneziana", "Venetian galley painting"],
        "nave": ["nave veneziana quattrocento", "carrack painting 16th century"],
        "carovana": ["carovana del sale", "caravan desert painting"],
        "diligenza": ["diligenza ottocento", "stagecoach painting"],
        "treno": ["prima ferrovia Italia", "early railway locomotive 19th century"],
        "aereo": ["primo aereo linea", "early airliner 1950s"],
        "carrozza": ["carrozza di corte rinascimento", "Renaissance court carriage"],
        "pipa": ["pipa botanical illustration", "Tabernaemontana plant"],
    },
    "edificio": {
        "cattedrale": ["Ferrara cathedral facade", "duomo di Ferrara esterno"],
        "castello": ["Castello Estense Ferrara", "castello medioevale Italian"],
        "palazzo": ["Palazzo Schifanoia Ferrara", "Palazzo dei Diamanti Ferrara"],
        "chiesa": ["chiesa romanica facciata Italia", "Italian Romanesque church facade"],
        "mura": ["mura di Ferrara", "Ferrara city walls"],
        "casa": ["casa torre Emilia", "Emilian medieval house"],
    },
    "epigrafe": {
        "lapide": ["Roman funerary inscription stone", "epigrafe romana Museo"],
        "lastra": ["Roman funerary relief marble", "stele funeraria greca"],
        "iscrizione": ["Greek inscription stone museum", "iscrizione greca antica"],
    },
    "incidente": {
        "incendio": ["incendio di Ferrara archivio", "incendio biblioteca antica"],
        "carestia": ["carestia 1520 incisione", "famine Europe 16th century engraving"],
        "moria": ["peste Italia 1520", "plague Italy engraving"],
    },
    "colore": {
        "tavolozza affreschi": ["affresco quattrocento campionatura", "Italian fresco palette"],
        "tessile": ["tappeto persiano motivo", "Islamic textile pattern"],
        "tinta": ["colori manoscritto miniato quattrocento", "illuminated manuscript pigments"],
        "terra": ["terre d'oliva Ferrara paesaggio", "Ferrara landscape painting Renaissance"],
    },
}

# La stessa libreria di licenze di `cerca_immagini_oggetti.py`, e per gli stessi
# motivi: una licenza non libera non entra.
LIB_OK = re.compile(
    r"public domain|pubblico dominio|\bpd\b|cc0|no restrictions"
    r"|cc[- ]?by(?![a-ns])|cc[- ]?by[- ]sa|attribution", re.I)
LIB_NO = re.compile(r"non[- ]?commercial|fair use|\bcc by[- ]nc|no deriv", re.I)


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
                time.sleep(float(e.headers.get("Retry-After") or 0) or 8 * (k + 1))
                continue
            return {"_errore": "HTTP %d" % e.code}
        except Exception:
            time.sleep(2 * (k + 1))
    return {"_errore": "insuccesso"}


def cerca(termini, limite=6):
    """Nomi di file su Commons per i termini, con licenza, autore e dimensioni."""
    out = []
    for termine in termini:
        d = get({
            "action": "query", "format": "json", "generator": "search",
            "gsrsearch": "filetype:bitmap %s" % termine, "gsrnamespace": "6",
            "gsrlimit": str(limite), "prop": "imageinfo",
            "iiprop": "extmetadata|url|size",
        })
        if "_errore" in d:
            continue
        for pagina in (d.get("query", {}).get("pages", {}) or {}).values():
            ii = (pagina.get("imageinfo") or [{}])[0]
            meta = ii.get("extmetadata", {}) or {}

            def val(k):
                return (meta.get(k, {}) or {}).get("value", "") or ""

            lic = re.sub(r"<[^>]+>", " ", val("LicenseShortName")) or val("License")
            autore = re.sub(r"<[^>]+>", " ", val("Artist")).strip() or \
                re.sub(r"<[^>]+>", " ", val("Credit")).strip()
            data = re.sub(r"<[^>]+>", " ", val("DateTimeOriginal")).strip()
            if LIB_NO.search(lic) or not LIB_OK.search(lic):
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


def main():
    categorie = [a for a in sys.argv[1:] if not a.startswith("--")]
    categorie = [c for c in categorie if c in VOCI] or list(VOCI)
    os.makedirs(CARTELLA, exist_ok=True)

    esito = {"versione": 1, "data": time.strftime("%Y-%m-%d"),
             "nota": "Proposte, non scelte: la ricerca propone, una persona "
                     "guarda e registra in attestazione.json.",
             "risultati": {}}
    for cat in categorie:
        esito["risultati"][cat] = []
        for voce, termini in VOCI[cat].items():
            candidati = cerca(termini)
            esito["risultati"][cat].append({
                "voce": voce, "termini": [termini[0]] + list(termini),
                "candidati": candidati,
            })
            print("%-9s %-22s %d candidati" % (cat, voce[:22], len(candidati)))
            time.sleep(0.3)

    with open(ESITO, "w", encoding="utf-8") as f:
        json.dump(esito, f, ensure_ascii=False, indent=1)
    print("scritto:", os.path.relpath(ESITO, RADICE))

    # il riepilogo
    totale = sum(len(v["candidati"]) for c in esito["risultati"].values()
                 for v in c)
    senza = [(c, v["voce"]) for c, voci in esito["risultati"].items()
             for v in voci if not v["candidati"]]
    print("candidati: %d" % totale)
    print("voci senza immagine: %d" % len(senza))
    for c, v in senza:
        print("   %s %s" % (c, v))
    return 0


if __name__ == "__main__":
    sys.exit(main())