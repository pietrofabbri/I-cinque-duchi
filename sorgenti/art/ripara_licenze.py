"""Ripara le licenze mancanti in `ritratti_disponibili.json`.

Il difetto: l'endpoint REST dei riassunti restituisce l'immagine in testata con
il nome del file **come thumbnail**, cioe' con il prefisso di dimensione
(`3840px-Albrecht_Dürer_...`). Quel nome funziona per il download, ma non
esiste come scheda su Commons: `imageinfo` lo cerca e non lo trova, e la scheda
finisce con «file non letto su Commons», che e' un'altra risposta falsa.

Qui si toglie il prefisso, si interroga Commons sul nome vero e la licenza
torna. Se anche il nome ripulito non esiste, la scheda resta `da_rivedere`:
nessuna conclusione senza risposta.
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request
import urllib.error

ART = os.path.dirname(os.path.abspath(__file__))
ESITO = os.path.join(ART, "ritratti_disponibili.json")
UA = "i-cinque-duchi/0.3 (progetto didattico per liceo; pietrofabbri)"

LIB_OK = re.compile(
    r"public domain|pubblico dominio|\bpd\b|cc0|no restrictions|attribution"
    r"|cc[- ]?by(?![a-z])|creative commons", re.I)
LIB_NO = re.compile(r"non[- ]?commercial|fair use|\bcc by[- ]nc|no deriv", re.I)

PREFISSO = re.compile(r"^\d+px-")
ALTRO = re.compile(r"^\d+px-[A-Za-z0-9_]+-")


def chiedi(titoli, tries=4):
    corpo = urllib.parse.urlencode({
        "action": "query", "format": "json", "prop": "imageinfo",
        "iiprop": "extmetadata|url|size",
        "titles": "|".join("File:" + t for t in titoli)}).encode()
    for k in range(tries):
        try:
            r = urllib.request.Request("https://commons.wikimedia.org/w/api.php",
                                       data=corpo, headers={
                                           "User-Agent": UA,
                                           "Accept": "application/json",
                                           "Content-Type":
                                               "application/x-www-form-urlencoded"})
            with urllib.request.urlopen(r, timeout=60) as f:
                return json.load(f)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 10 * (k + 1)
                print("   %d, attendo %.0f s" % (e.code, att), flush=True)
                time.sleep(att)
                continue
            return None
        except Exception:
            time.sleep(3 * (k + 1))
    return None


def normalizza_chiave(t):
    return t.split(":", 1)[-1].replace("_", " ").strip()


if __name__ == "__main__":
    esiti = json.load(open(ESITO, encoding="utf-8"))

    # i nomi di cui provare la forma ripulita, senza duplicati
    candidati = []
    for e in esiti:
        if e["motivo"].startswith("richiesta_fallita") and e.get("immagine"):
            n = e["immagine"]
            for nuovo in {PREFISSO.sub("", n), ALTRO.sub("", n), n}:
                if nuovo and nuovo not in candidati:
                    candidati.append(nuovo)
    print("nomi da riprovare: %d" % len(candidati))

    su = {}
    for i in range(0, len(candidati), 25):
        blocco = candidati[i:i + 25]
        d = chiedi(blocco)
        if not d:
            print("  blocco %d fallito" % i)
            continue
        for _, p in (d.get("query", {}).get("pages") or {}).items():
            if "missing" in p:
                continue
            ii = (p.get("imageinfo") or [None])[0]
            if not ii:
                continue
            em = ii.get("extmetadata", {})
            su[normalizza_chiave(p["title"])] = {
                "licenza": (em.get("LicenseShortName", {}) or {}).get("value", ""),
                "autore": re.sub(r"<[^>]+>", "",
                                 (em.get("Artist", {}) or {}).get("value", ""))[:120],
                "url": ii.get("url"),
                "larghezza": ii.get("width"), "altezza": ii.get("height")}
        print("  letti %d/%d" % (len(su), len(candidati)), flush=True)
        time.sleep(1.0)

    riparati = 0
    for e in esiti:
        if not (e["motivo"].startswith("richiesta_fallita") and e.get("immagine")):
            continue
        n = e["immagine"]
        for nuovo in (n, PREFISSO.sub("", n), ALTRO.sub("", n)):
            det = su.get(normalizza_chiave(nuovo))
            if not det:
                continue
            if LIB_NO.search(det["licenza"]) or not LIB_OK.search(det["licenza"]):
                e["motivo"] = "licenza non utilizzabile: " + det["licenza"]
                e["dettagli"] = det
            else:
                e["dettagli"] = det
                e["immagine_reale"] = nuovo
                e["motivo"] = "ok"
                print("  riparato %-6s %-34s %s" % (e["codice"], e["nome"][:34],
                                                    det["licenza"]))
                riparati += 1
            break

    with open(ESITO, "w", encoding="utf-8") as f:
        json.dump(esiti, f, ensure_ascii=False, indent=1)
    print("\nriparate: %d" % riparati)
    print("ancora da rivedere: %d" % sum(1 for e in esiti
                                         if e["motivo"].startswith("richiesta_fallita")))
