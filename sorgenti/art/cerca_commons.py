"""Cerca su Commons, e non su Wikipedia, un'immagine con licenza libera per le
schede rimaste senza ritratto.

Perche' la ricerca va fatta qui e non li': diverse immagini che si trovano in
testata agli articoli di Wikipedia sono ospitate nel deposito locale di quella
Wikipedia e **non** su Commons. Non hanno quindi licenza libera: sono protette
da copyright e si possono usare solo secondo le regole locali di quella
Wikipedia, che il progetto non segue. E' il caso di Giulio Natta, di Riccardo
Bacchelli e di Alonzo Church.

Su Commons si puo' invece caricare la ricerca anche sui **nomi di file**, con il
prefisso `filetype:bitmap`, che e' quello che serve quando non si conosce il
titolo esatto dell'immagine.
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

# chi cerca un'immagine libera, e con quale termine: i termini sono scelti
# guardando i nomi delle persone, non tradotti alla cieca
RICERCHE = {
    "P01": ["Maurelio Ferrara santo", "Saint Maurelius"],
    "P07": ["Obizzo I d'Este", "Obizzo d'Este"],
    "P09": ["Aldobrandino d'Este"],
    "P10": ["Obizzo II d'Este", "Obizzo III d'Este"],
    "P15": ["Niccolò II d'Este", "Nicolò II d'Este"],
    "P31": ["Biagio Rossetti"],
    "P40": ["Ludovico Bonaccioli", "Bonaccioli"],
    "P46": ["Giovanni Battista Canani", "Canani"],
    "P59": ["Bartolomeo Chiozzi"],
    "P60": ["Riccardo Bacchelli"],
    "P67": ["Domenico Malagutti", "Guercinian"],
    "P68": ["Giacomo Succi"],
    "P70": ["Gioacchino Bonnet", "Nino Bonnet"],
    "P76": ["Carlo Savonuzzi"],
    "P77": ["Alda Costa"],
    "P80": ["Renata Viganò"],
    "P83": ["Giulio Natta"],
    "Q27": ["Cornelia mother Gracchi", "Cornelia Africana"],
    "Q308": ["Sergey Korolev", "Korolëv"],
    "Q314": ["Alonzo Church"],
    "Q319": ["Donald Davies packet switching"],
    "Q324": ["James Ellis cryptography"],
}


def get(url, params, tries=4):
    for k in range(tries):
        try:
            r = urllib.request.Request(url + "?" + urllib.parse.urlencode(params),
                                       headers={"User-Agent": UA,
                                                "Accept": "application/json"})
            with urllib.request.urlopen(r, timeout=60) as f:
                return json.load(f)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 10 * (k + 1)
                time.sleep(att)
                continue
            return {"_errore": "HTTP %d" % e.code}
        except Exception:
            time.sleep(3 * (k + 1))
    return {"_errore": "insuccesso"}


def cerca(termini, limite=12):
    """Nomi di file su Commons che contengono i termini."""
    out = []
    for t in termini:
        d = get("https://commons.wikimedia.org/w/api.php", {
            "action": "query", "format": "json", "list": "search",
            "srnamespace": "6", "srlimit": str(limite), "srsearch": t})
        if "_errore" in d:
            print("   ricerca fallita su %r: %s" % (t, d["_errore"]))
            continue
        for r in d.get("query", {}).get("search", []):
            if r["title"] not in out:
                out.append(r["title"])
        time.sleep(0.6)
    return out


def licenze(titoli):
    d = get("https://commons.wikimedia.org/w/api.php", {
        "action": "query", "format": "json", "prop": "imageinfo",
        "iiprop": "extmetadata|url|size", "titles": "|".join(titoli)})
    if "_errore" in d:
        return None
    su = {}
    for _, p in (d.get("query", {}).get("pages") or {}).items():
        if "missing" in p:
            continue
        ii = (p.get("imageinfo") or [None])[0]
        if not ii:
            continue
        em = ii.get("extmetadata", {})
        su[p["title"]] = {
            "licenza": (em.get("LicenseShortName", {}) or {}).get("value", ""),
            "autore": re.sub(r"<[^>]+>", "",
                             (em.get("Artist", {}) or {}).get("value", ""))[:120],
            "url": ii.get("url"),
            "larghezza": ii.get("width"), "altezza": ii.get("height")}
    return su


if __name__ == "__main__":
    esiti = json.load(open(ESITO, encoding="utf-8"))
    per_codice = {e["codice"]: e for e in esiti}

    for codice, termini in RICERCHE.items():
        e = per_codice[codice]
        print("### %s  %s" % (codice, e["nome"]))
        titoli = cerca(termini)
        if not titoli:
            print("    nessun file su Commons\n", flush=True)
            continue
        # i nomi di file plausibili: devono contenere il cognome
        cognome = max(e["nome"].split(), key=len).lower()
        utili = [t for t in titoli if cognome[:6] in t.lower()] or titoli[:6]
        su = licenze(utili[:25])
        if not su:
            print("    licenze non lette\n", flush=True)
            continue
        for t, det in su.items():
            ok = bool(LIB_OK.search(det["licenza"])) and not LIB_NO.search(det["licenza"])
            print("    %s %-62s %s" % ("LIBERA" if ok else "no    ",
                                       t[:62], det["licenza"][:28]))
        print(flush=True)
