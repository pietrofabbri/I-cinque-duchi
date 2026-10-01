"""Estrae dai documenti degli anni la lista dei luoghi che il gioco usa davvero.

La fonte non e' una lista scritta a parte: sono le colonne «Luogo (pin)» e
«Facoltativi» delle trenta tappe di ciascun anno. Il vantaggio e' che l'inventario
non puo' divergere dai documenti: se il progetto sposta una tappa, l'inventario
si sposta con lei, e non resta un elenco di nomi che non piu' esistono nel testo.

Non decide niente: raccoglie. Le coordinate, il rilievo e i dettagli
architettonici vengono aggiunti dopo, e ognuno porta la propria fonte.
"""
import json
import os
import re

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(RADICE, "docs")
DOCUMENTI = {
    1: "videogioco-5-duchi-anno1-ferrara.md",
    2: "videogioco-5-duchi-anno2-penisola.md",
    3: "videogioco-5-duchi-anno3-europa.md",
    4: "videogioco-5-duchi-anno4-mondo.md",
    5: "videogioco-5-duchi-anno5-mondo.md",
}
# la colonna del luogo e' la quarta in tutti gli anni. Nell'anno 4 la colonna
# si chiama `Pin` e non `Luogo (pin)`, e c'e' una colonna in piu' — la porta —
# ma sta DOPO la voce, non prima: la prima versione puntava al posto sbagliato e
# si trovava con trenta nomi di persone al posto di trenta luoghi. E' stato
# visto perche' nessuno di quei nomi ha coordinate, mentre tutti i luoghi le
# hanno. La tabella delle colonne va riletta ogni volta che un documento cambia.
COLONNA_LUOGO = {1: 3, 2: 3, 3: 3, 4: 3, 5: 3}

RIGA = re.compile(r"^\|\s*\*\*([1-5]-\d+)\*\*\s*\|")


def celle(riga):
    # si taglia la riga su '|' senza righe vuote: una cella che contiene una
    # pipe sfuggita romperebbe il conteggio delle colonne
    parti = riga.strip().strip("|").split("|")
    return [p.strip() for p in parti]


def togli_codice(testo):
    """'**Ötzi** (Q01)' -> 'Ötzi'; toglie anche il grassetto e il rimando."""
    t = re.sub(r"\*\*", "", testo)
    t = re.sub(r"\s*\((P|Q)\d+[^)]*\)", "", t)
    t = re.sub(r"\s*\(collettivo\)", "", t)
    t = re.sub(r"\s*\(facoltativa?\)", "", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip(" .;,")


def estrai(anno, percorso):
    out = []
    if not os.path.exists(percorso):
        return out
    dentro = False
    for riga in open(percorso, encoding="utf-8"):
        if riga.startswith("| Livello |") or riga.startswith("| Codice |"):
            dentro = True
            continue
        if dentro and riga.startswith("|---"):
            continue
        m = RIGA.match(riga)
        if dentro and m:
            c = celle(riga)
            if len(c) <= max(COLONNA_LUOGO.values()):
                continue
            codice = m.group(1)
            if not codice.startswith(str(anno) + "-"):
                continue
            out.append({"tappa": codice, "luogo": togli_codice(c[COLONNA_LUOGO[anno]]),
                        "voce": togli_codice(c[COLONNA_LUOGO[anno] + 1])
                        if len(c) > COLONNA_LUOGO[anno] + 1 else ""})
    return out


if __name__ == "__main__":
    tutti = []
    for anno, nome in DOCUMENTI.items():
        righe = estrai(anno, os.path.join(DOC, nome))
        if not righe:
            print("anno %d: nessuna tappa trovata in %s" % (anno, nome))
        tutti.extend([dict(r, anno=anno) for r in righe])

    # i pin sono unici per definizione: un posto che compare due volte e' un
    # posto solo, e si contano le tappe che ci arrivano
    per_luogo = {}
    for r in tutti:
        k = r["luogo"]
        per_luogo.setdefault(k, []).append(r["tappa"])

    print("tappe con un luogo: %d" % len(tutti))
    print("luoghi distinti:     %d" % len(per_luogo))
    print("\nluoghi che ricompaiono in piu' tappe:")
    for k, v in sorted(per_luogo.items(), key=lambda x: -len(x[1])):
        if len(v) > 1:
            print("  %-46s %s" % (k, ", ".join(v)))

    with open(os.path.join(RADICE, "dati", "luoghi_estratti.json"), "w",
              encoding="utf-8") as f:
        json.dump({"tappe": tutti,
                   "luoghi": [{"luogo": k, "tappe": v} for k, v in
                              sorted(per_luogo.items())]},
                  f, ensure_ascii=False, indent=1)
    print("\nscritto dati/luoghi_estratti.json")
