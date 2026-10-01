"""Risolve i nomi dei luoghi in articoli di Wikipedia e ne prende le coordinate.

La regola che governa tutto questo: **si registra anche a quale articolo il nome
ha corrisposto**. «Roma, Curia» puo' risolvere sulla Curia romana o su una citta'
omonima, e senza il titolo risolto una coordinata giusta a meta' strada e'
indistinguibile da una sbagliata. Il campo `titolo_risolto` e' quello che
permette a chi legge di controllare.

Nessuna coordinata viene inventata ne' dedotta da una citta' vicina: se il nome
non risolve, la scheda resta senza coordinate e lo dice.
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request
import urllib.error

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INGRESSO = os.path.join(RADICE, "dati", "luoghi_estratti.json")
USCITA = os.path.join(RADICE, "dati", "luoghi_geo.jsonl")
UA = "i-cinque-duchi/0.1 (progetto didattico per liceo; pietrofabbri)"

PAUSA = 3.0

# Il lavoro e' incrementale e riprende: una riga per luogo, scritta subito.
# Novantaotto richieste con i tempi di attesa non entrano in una sola sessione,
# e un processo che muore a meta' non deve perdere quello che ha gia' fatto.
# `python3 coordinate.py [quanti]` risolve al massimo quel numero di luoghi e
# basta: si richiama finche' non ha finito.


def get(url, params, tentativi=5):
    for k in range(tentativi):
        try:
            r = urllib.request.Request(url + "?" + urllib.parse.urlencode(params),
                                       headers={"User-Agent": UA,
                                                "Accept": "application/json"})
            with urllib.request.urlopen(r, timeout=60) as f:
                return json.load(f)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 8 * (k + 1)
                time.sleep(att)
                continue
            return {"_errore": "HTTP %d" % e.code}
        except Exception as e:
            if k == tentativi - 1:
                return {"_errore": str(e)[:70]}
            time.sleep(4 * (k + 1))
    return {"_errore": "insuccesso"}


def prova_titoli(wiki, titoli):
    """titolo -> coordinate, oppure None se l'articolo non c'e'.

    Restituisce la stringa `'fallito'` se la richiesta e' fallita, e None se la
    risposta e' arrivata e l'articolo non ha coordinate. La distinzione e'
    indispensable: e' la quarta volta che questo progetto legge un errore di
    rete come una risposta negativa. Un 429 qui diventava «Uruk non ha
    coordinate», mentre Uruk le ha: 31,33° N 45,64° E. Il 429 viene ascoltato e
    la scheda resta da rifare, non diventa un fatto.
    """
    d = get("https://%s.wikipedia.org/w/api.php" % wiki,
            {"action": "query", "format": "json", "prop": "coordinates",
             "redirects": "1", "titles": "|".join(titoli)})
    if "_errore" in d:
        return "fallito"
    q = d.get("query", {})
    alias = {}
    for r in (q.get("normalized") or []) + (q.get("redirects") or []):
        alias[r["from"]] = r["to"]
    fuori = {}
    for pag in (q.get("pages") or {}).values():
        titolo = pag.get("title")
        if "missing" in pag or not titolo:
            continue
        co = (pag.get("coordinates") or [None])[0]
        if not co:
            continue
        voce = {"titolo_risolto": titolo, "lat": round(co["lat"], 5),
                "lon": round(co["lon"], 5)}
        fuori[titolo] = voce
        for vecchio, nuovo in alias.items():
            if nuovo == titolo:
                fuori[vecchio] = voce
    return fuori


def ripulisci(nome):
    """«Roma, Curia» -> si prova prima «Roma, Curia», poi «Curia»."""
    parti = [p.strip() for p in nome.split(",") if p.strip()]
    if len(parti) > 1:
        return [", ".join(parti), parti[-1], " ".join(reversed(parti))]
    return [nome]


if __name__ == "__main__":
    import sys
    dati = json.load(open(INGRESSO, encoding="utf-8"))
    tutti = [l["luogo"] for l in dati["luoghi"]]

    fatti = {}
    if os.path.exists(USCITA):
        for riga in open(USCITA, encoding="utf-8"):
            riga = riga.strip()
            if riga:
                try:
                    v = json.loads(riga)
                except ValueError:
                    continue          # riga interrotta: si ripete quel luogo
                # una risposta 'da_rifare' non chiude la scheda: la successiva
                # riga vale, quindi i tentativi inutili non contano
                if v.get("stato") == "da_rifare":
                    fatti.pop(v["luogo"], None)
                    continue
                fatti[v["luogo"]] = v
    da_fare = [l for l in tutti if l not in fatti]
    limite = int(sys.argv[1]) if len(sys.argv) > 1 else len(da_fare)
    da_fare = da_fare[:limite]
    print("gia' risolti %d, da risolvere in questo giro %d (su %d)"
          % (len(fatti), len(da_fare), len(da_fare)))
    if not da_fare:
        print("finito")
    else:
        with open(USCITA, "a", encoding="utf-8") as f:
            for n, nome in enumerate(da_fare, 1):
                esito = None
                tutte_fallite = True
                for prova in ripulisci(nome):
                    for wiki in ("it", "en"):
                        d = prova_titoli(wiki, [prova])
                        if d == "fallito":
                            continue          # rete: non e' una risposta
                        tutte_fallite = False
                        if d and prova in d:
                            esito = dict(d[prova], prova_usata=prova, wiki=wiki)
                            break
                    if esito:
                        break
                if esito is None:
                    # solo se tutte le richieste sono fallite per rete, il luogo
                    # resta da rifare: non si scrive un'assenza che non e' stata
                    # verificata
                    esito = {"titolo_risolto": None,
                             "stato": "da_rifare" if tutte_fallite else "senza_articolo"}
                esito.pop("errore", None)
                esito["luogo"] = nome
                f.write(json.dumps(esito, ensure_ascii=False) + "\n")
                f.flush()
                print("  %d/%d  %-40s %s" % (n, len(da_fare), nome[:40],
                                            esito.get("titolo_risolto")
                                            or esito.get("stato")), flush=True)
                time.sleep(PAUSA)

    fatti = {}
    for riga in open(USCITA, encoding="utf-8"):
        riga = riga.strip()
        if riga:
            v = json.loads(riga)
            fatti[v["luogo"]] = v
    risolti = {k: v for k, v in fatti.items() if v.get("titolo_risolto")}
    mancanti = [k for k, v in fatti.items() if not v.get("titolo_risolto")]
    da_rifare = [l for l in tutti if l not in fatti]
    print("\nrisolti %d su %d" % (len(risolti), len(tutti)))
    if mancanti:
        print("verificati e senza articolo (%d):" % len(mancanti))
        for m in sorted(mancanti):
            print("   " + m)
    if da_rifare:
        print("da rifare, rete non raggiungibile (%d)" % len(da_rifare))

    sospetti = []
    for nome, v in sorted(risolti.items()):
        parole = [p for p in re.split(r"[\s,]+", nome.lower())
                  if len(p) > 3 and p not in ("della", "delle", "dello", "dove",
                                              "gli", "nel", "alla", "caravane")]
        titolo = v["titolo_risolto"].lower()
        if parole and not any(p in titolo for p in parole):
            sospetti.append((nome, v["titolo_risolto"]))
    if sospetti:
        print("\nda controllare a mano: il titolo risolto non contiene il nome")
        for nome, titolo in sospetti:
            print("   %-38s -> %s" % (nome, titolo))
    print("\nscritto %s" % USCITA)
