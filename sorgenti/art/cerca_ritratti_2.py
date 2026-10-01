"""Seconda passata: recupera i ritratti dei personaggi che la ricerca in blocco
non ha risolto, usando l'endpoint REST delle riassunti.

Perche' un endpoint diverso: la API `action=query` di Wikipedia, usata dalla
prima passata, risponde 429 a raffica e i nomi dei 150 personaggi già risolti
non hanno motivo di essere richiesti di nuovo. Il REST `page/summary` ha
limiti propri, accetta un titolo per richiesta e restituisce sia l'immagine in
testata sia la sua dimensione, che serve al ritaglio.

Anche qui vale la regola della prima passata: **una richiesta fallita non
produce una conclusione**. Il campo `motivo` distingue `non_trovato` da
`richiesta_fallita`, e il secondo lascia la scheda `da_rivedere`.
"""
import json
import os
import time
import urllib.parse
import urllib.request
import urllib.error

ART = os.path.dirname(os.path.abspath(__file__))
ESITO = os.path.join(ART, "ritratti_disponibili.json")
PRIMA = os.path.join(ART, "ritratti_disponibili_prima.json")
UA = "i-cinque-duchi/0.3 (progetto didattico per liceo; pietrofabbri)"

LIB_OK = __import__("re").compile(
    r"public domain|pubblico dominio|\bpd\b|cc0|no restrictions|attribution"
    r"|cc[- ]?by(?![a-z])|creative commons", __import__("re").I)
LIB_NO = __import__("re").compile(r"non[- ]?commercial|fair use|\bcc by[- ]nc|no deriv", __import__("re").I)

# Scelte fatte guardando i risultati di ricerca, non a memoria. La voce e'
# (titolo, wiki) e la nota dice perche' il titolo diretto non funziona.
TITOLI = {
    "P01": ("Maurelio di Ferrara", "it"),
    "P03": ("Guido d'Arezzo", "it"),
    "P05": ("Casato (famiglia)", "it"),
    "P07": ("Obizzo I d'Este", "it"),
    "P09": ("Aldobrandino d'Este", "it"),
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
    "P63": ("Periodo napoleonico", "it"),
    "P66": ("Bersaglieri", "it"),
    "P67": ("Domenico Malagutti", "it"),
    "P68": ("Giacomo Succi", "it"),
    "P70": ("Gioacchino Bonnet", "it"),
    "P76": ("Carlo Savonuzzi", "it"),
    "P77": ("Alda Costa", "it"),
    "P80": ("Renata Viganò", "it"),
    "P83": ("Giulio Natta", "it"),
    "P88": ("Ebraismo", "it"),
    "P89": ("Università di Ferrara", "it"),
    "P90": ("Artigianato", "it"),
    "P91": ("Sant'Antonio in Polesine (Ferrara)", "it"),
    "P92": ("Po (fiume)", "it"),
    "P93": ("Ferrara", "it"),
    "Q27": ("Cornelia (madre dei Gracchi)", "it"),
    "Q62": ("Leon Battista Alberti", "it"),
    "Q91": ("Copista", "it"),
    "Q90": ("Corriere (messaggero)", "it"),
    "Q92": ("Consiglio (assemblea)", "it"),
    "Q108": ("Federico II del Sacro Romano Impero", "it"),
    "Q117": ("Josquin Desprez", "it"),
    "Q120": ("Giovanni Bellini", "it"),
    "Q124": ("Albrecht Dürer", "de"),
    "Q125": ("Aldo Manuzio", "it"),
    "Q126": ("William Caxton", "en"),
    "Q128": ("Alan Turing", "en"),
    "Q129": ("Privilegio di stampa", "it"),
    "Q207": ("Gottfried Wilhelm Leibniz", "en"),
    "Q220": (" Censura", "it"),
    "Q230": ("Anonimato", "it"),
    "Q305": ("Algoritmo di Chudnovsky", "it"),
    "Q308": ("Sergej Korolëv", "en"),
    "Q309": ("John Snow", "en"),
    "Q313": ("Calcolatrice", "it"),
    "Q314": ("Alonzo Church", "en"),
    "Q318": ("Rete informatica", "it"),
    "Q319": ("Donald Davies (engineer)", "en"),
    "Q324": ("James Ellis (cryptographer)", "en"),
}


def prendi(url, tries=4):
    for k in range(tries):
        try:
            r = urllib.request.Request(url, headers={"User-Agent": UA,
                                                      "Accept": "application/json"})
            with urllib.request.urlopen(r, timeout=45) as f:
                corpo = f.read()
            if not corpo.strip():
                return {"_errore": "corpo vuoto"}
            return json.loads(corpo)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 10 * (k + 1)
                print("      %d, attendo %.0f s" % (e.code, att), flush=True)
                time.sleep(att)
                continue
            if k == tries - 1:
                return {"_errore": "HTTP %d" % e.code}
        except Exception as e:
            if k == tries - 1:
                return {"_errore": type(e).__name__ + ": " + str(e)[:70]}
            time.sleep(3 * (k + 1))
    return {"_errore": "insuccesso"}


def riassunto(wiki, titolo):
    u = ("https://" + wiki + ".wikipedia.org/api/rest_v1/page/summary/"
         + urllib.parse.quote(titolo.replace(" ", "_"), safe=""))
    d = prendi(u)
    if "_errore" in d:
        return d
    orig = (d.get("originalimage") or {})
    if not orig.get("source"):
        return {"_errore": "nessuna immagine"}
    return {"immagine": urllib.parse.unquote(orig["source"].split("/")[-1].split("?")[0]),
            "descrizione": (d.get("description") or "")[:120],
            "larghezza": orig.get("width"), "altezza": orig.get("height"),
            "pagina": d.get("title", titolo)}


def licenze(names):
    corpo = urllib.parse.urlencode({
        "action": "query", "format": "json", "prop": "imageinfo",
        "iiprop": "extmetadata|url|size",
        "titles": "|".join("File:" + n for n in names)}).encode()
    for k in range(4):
        try:
            r = urllib.request.Request("https://commons.wikimedia.org/w/api.php",
                                       data=corpo, headers={
                                           "User-Agent": UA,
                                           "Accept": "application/json",
                                           "Content-Type": "application/x-www-form-urlencoded"})
            with urllib.request.urlopen(r, timeout=60) as f:
                d = json.load(f)
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 10 * (k + 1)
                time.sleep(att)
                continue
            return None
        except Exception:
            time.sleep(3 * (k + 1))
    else:
        return None
    su = {}
    for _, p in (d.get("query", {}).get("pages") or {}).items():
        ii = (p.get("imageinfo") or [None])[0]
        if not ii:
            continue
        em = ii.get("extmetadata", {})
        chiave = p["title"].split(":", 1)[-1].replace("_", " ").strip()
        su[chiave] = {
            "licenza": (em.get("LicenseShortName", {}) or {}).get("value", ""),
            "autore": __import__("re").sub(
                r"<[^>]+>", "", (em.get("Artist", {}) or {}).get("value", ""))[:120],
            "url": ii.get("url"),
            "larghezza": ii.get("width"), "altezza": ii.get("height")}
    return su


if __name__ == "__main__":
    esiti = json.load(open(ESITO, encoding="utf-8"))
    per_codice = {e["codice"]: e for e in esiti}

    # si riparte dai 150 della prima passata: sono gia' stati risolti e hanno un
    # record di licenza su Commons, non c'e' ragione di richiederli di nuovo
    prima = {e["codice"]: e for e in json.load(open(PRIMA, encoding="utf-8"))}
    recuperati = 0
    for e in esiti:
        if e["motivo"].startswith("ok"):
            continue
        vecchio = prima.get(e["codice"])
        if vecchio and vecchio["motivo"] == "ok":
            e.update(immagine=vecchio["immagine"], dettagli=vecchio["dettagli"],
                     pagina=vecchio.get("pagina"), titolo=vecchio.get("titolo"),
                     motivo=vecchio["motivo"])
            recuperati += 1
    print("recuperati dalla prima passata: %d" % recuperati)

    candidati = [e for e in esiti if not e["motivo"].startswith("ok")
                 and e["codice"] in TITOLI and e["motivo"] != "collettivo: non ha un volto unico"]
    print("da interrogare uno per uno: %d\n" % len(candidati))

    nuovi = []
    for e in candidati:
        titolo, wiki = TITOLI[e["codice"]]
        d = riassunto(wiki, titolo)
        if "_errore" in d:
            e["motivo"] = "richiesta_fallita: " + d["_errore"]
            print("  %-6s %-38s FALLITA (%s)" % (e["codice"], e["nome"][:38], d["_errore"]))
            continue
        e["immagine"] = d["immagine"]
        e["titolo"] = titolo
        e["pagina"] = d["pagina"]
        e["nota_immagine"] = d["descrizione"]
        nuovi.append(e)
        print("  %-6s %-38s %s" % (e["codice"], e["nome"][:38], d["immagine"][:60]))
        time.sleep(3.0)

    if nuovi:
        print("\nlicenze per %d file nuovi" % len(nuovi))
        su = licenze(sorted({e["immagine"] for e in nuovi}))
        if su is None:
            for e in nuovi:
                e["motivo"] = "richiesta_fallita: Commons non raggiungibile"
        else:
            for e in nuovi:
                det = su.get(e["immagine"].replace("_", " ").strip())
                if not det:
                    e["motivo"] = "richiesta_fallita: file non letto su Commons"
                elif LIB_NO.search(det["licenza"]) or not LIB_OK.search(det["licenza"]):
                    e["motivo"] = "licenza non utilizzabile: " + det["licenza"]
                    e["dettagli"] = det
                else:
                    e["dettagli"] = det
                    e["motivo"] = "ok"
                    print("  ok %-6s %-30s %s" % (e["codice"], e["nome"][:30], det["licenza"]))

    # la scheda Q64 e' la stessa persona di P31: condivide l'immagine
    for gemello, doppio in (("P31", "Q64"),):
        a, b = per_codice[gemello], per_codice[doppio]
        if a["motivo"].startswith("ok"):
            b["immagine"] = a["immagine"]
            b["dettagli"] = a["dettagli"]
            b["motivo"] = "ok (stessa persona di %s)" % gemello

    with open(ESITO, "w", encoding="utf-8") as f:
        json.dump(esiti, f, ensure_ascii=False, indent=1)

    ok = [e for e in esiti if e["motivo"].startswith("ok")]
    print("\ntotale %d" % len(esiti))
    print("  ritratti autentici  : %d" % len(ok))
    print("  emblemi             : %d" % sum(1 for e in esiti
                                            if "emblema" in e["motivo"] or "collettivo" in e["motivo"]))
    print("  non trovato         : %d" % sum(1 for e in esiti if e["motivo"].startswith("non_trovato")))
    print("  DA RIVEDERE         : %d" % sum(1 for e in esiti if e["motivo"].startswith("richiesta_fallita")))
