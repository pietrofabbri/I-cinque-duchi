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
# Il numero di colonna e' fragile, e il difetto del 03/10/2026 lo ha provato:
# nell'anno 5 la tabella ha UNA COLONNA IN PIU' rispetto agli altri anni — la
# `Stanza`, cioe' dove sta accadendo, che sta FRA il pin e la voce. Il numero
# fisso ha preso la stanza come se fosse la voce, e in ventinove tappe su
# trenta ha messo nel campo `voce` il filone del *Furioso` invece della persona.
# Il sintomo e' che il nome della voce sembrava gia' un titolo: «la strada della
# fuga di Rinaldo `F2` 1,32». Nessuno se n'era accorto perche' nessuno leggeva
# 120 nomi di persona in un colpo solo.
# Per questo la tabella delle colonne si legge per INTESTAZIONE, non per numero:
# e' l'unico modo che regge quando un documento aggiunge una colonna.
COLONNA_LUOGO = {1: 3, 2: 3, 3: 3, 4: 3, 5: 3}
# La colonna della voce non e' sempre quella dopo il luogo, ed e' quello il punto.
COLONNA_VOCE = {1: 4, 2: 4, 3: 4, 4: 4, 5: 5}
# Le intestazioni che contano, con i loro possibili nomi: `Pin`, `Luogo (pin)`,
# `Luogo` nell'anno 1; `Voce` e `Personaggi` per la persona che guida la tappa.
INT_PINS = ("pin (dove siamo oggi)", "pin", "luogo (pin)", "luogo")
INT_VOCI = ("voce", "personaggi")

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


def intestazione(riga):
    """La riga di intestazione dice DOVE sta il pin e DOVE sta la voce.

    Non si conta la posizione: si cerca il nome della colonna. Il numero di
    colonna si sbaglia appena un documento aggiunge una colonna — e nel quinto
    anno la colonna della stanza c'e' stata messa proprio fra le due che
    servivano, cosi' il numero indicava la stanza e non la voce. Un nome di
    colonna, invece, resta giusto anche se a sinistra ne compare una nuova.

    Ritorna `(indice_pin, indice_voce, nomi_trovati)`; gli indici sono `None`
    quando la colonna non c'e' e l'estrazione di quell'anno salta.
    """
    nomi = [c.strip().strip("*").lower() for c in celle(riga)]
    pin = voce = None
    trovati = []
    for i, n in enumerate(nomi):
        if n in INT_PINS and pin is None:
            pin, _ = i, trovati.append(n)
        elif n in INT_VOCI and voce is None:
            voce, _ = i, trovati.append(n)
    return pin, voce, trovati


def estrai(anno, percorso):
    out = []
    if not os.path.exists(percorso):
        return out
    dentro = False
    pin = voce = None
    for riga in open(percorso, encoding="utf-8"):
        if riga.startswith("| Livello |") or riga.startswith("| Codice |"):
            pin, voce, trovati = intestazione(riga)
            dentro = pin is not None and voce is not None
            continue
        if dentro and riga.startswith("|---"):
            continue
        m = RIGA.match(riga)
        if dentro and m:
            c = celle(riga)
            if len(c) <= max(pin, voce):
                continue
            codice = m.group(1)
            if not codice.startswith(str(anno) + "-"):
                continue
            out.append({"tappa": codice, "luogo": togli_codice(c[pin]),
                        "voce": togli_codice(c[voce]) if len(c) > voce else ""})
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
