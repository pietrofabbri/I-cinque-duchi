"""Genera le tabelle degli **itinerari** da `dati/incontri_livelli.json`.

Il documento `videogioco-5-duchi-itinerari.md` porta, per ogni tappa, **dove si
va, con quale mezzo, e chi si incontra** — l'obbligatorio e i facoltativi. Le
tabelle non si scrivono a mano: si generano da un dato che a sua volta è estratto
dalle tabelle degli anni, e ogni cifra del documento viene dal conto.

**Perché generare e non scrivere.** Sono centocinquanta righe e ognuna ha quattro
cose. Scritte a mano, due righe su centocinquanta finiscono con una cifra che il
dato non conferma, ed è esattamente il difetto che ha fatto nascere questo
lavoro: il quinto anno dichiarava due voci collettive e ne aveva tre. Il
documento è quindi **generato**, e il verifica_incontri.py tiene il conto.

Uso:
    python3 sorgenti/genera_itinerari.py            # stampa le tabelle
    python3 sorgenti/genera_itinerari.py --anno 3   # un anno solo
"""
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INCONTRI = os.path.join(RADICE, "dati", "incontri_livelli.json")

# I mezzi con le loro parole, presi da percorsi.md §1. Il numero non e' qui: la
# velocita' e' di `percorsi_mezzi.py`, e duplicarla sarebbe un secondo numero che
# invecchia.
MEZZO = {
    "a_piedi": "a piedi",
    "cavallo": "a cavallo",
    "galera": "in galera",
    "pipa": "in pipa",
    "nave": "in nave",
    "carovana": "in carovana",
    "diligenza": "in diligenza",
    "treno": "in treno",
    "aereo": "in aereo",
    "crociera": "in crociera",
    "moto": "in moto",
    "sci": "gli sci",
    "elicottero": "in elicottero",
    "monopattino": "in monopattino",
}


def voce_testo(v):
    """Una voce nel testo: il nome, il codice, e la marcatura se e' collettiva."""
    s = v["nome"]
    if v.get("codice"):
        s += " (%s)" % v["codice"]
    if v.get("tipo") == "collettivo":
        s += " *(collettivo)*"
    return s


def facoltativi_testo(fac):
    """I facoltativi in una casella: separati da punto e virgola, col nome solo."""
    if not fac:
        return "—"
    out = []
    for f in fac:
        t = f["nome"]
        if f.get("nota"):
            t += " (%s)" % f["nota"]
        out.append(t)
    return "; ".join(out)


def main():
    if not os.path.exists(INCONTRI):
        print("non trovo %s: esegui prima estrai_incontri.py"
              % os.path.relpath(INCONTRI, RADICE))
        return 1
    d = json.load(open(INCONTRI, encoding="utf-8"))
    per_anno = {}
    for x in d["incontri"]:
        per_anno.setdefault(x["anno"], []).append(x)

    anni = sorted(per_anno)
    if len(sys.argv) > 1 and sys.argv[1].startswith("--anno"):
        anni = [int(sys.argv[2])]

    for anno in anni:
        xs = per_anno[anno]
        mezzo = xs[0]["mezzo"]
        etichetta = MEZZO.get(mezzo, "**non dichiarato**")
        print("\n### Anno %d — %s\n" % (anno, etichetta.capitalize()
                                        if mezzo else "il mezzo non è dichiarato"))
        print("| Livello | Dove si va | Chi incontri (obbligatorio) | Facoltativi |")
        print("|---|---|---|---|")
        for x in xs:
            dove = x["luogo"] or "—"
            if x.get("stanza"):
                dove += " — *stanza:* %s" % x["stanza"]
            print("| **%s** | %s | %s | %s |"
                  % (x["livello"], dove, voce_testo(x["voce_obbligatoria"]),
                     facoltativi_testo(x.get("facoltativi"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())