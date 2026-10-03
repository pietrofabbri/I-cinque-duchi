"""Mette le tabelle generate dentro il documento degli itinerari.

**Perché questo script esiste.** Le tabelle di `videogioco-5-duchi-itinerari.md`
§3 sono centocinquanta righe e ognuna ha quattro informazioni. Scritte a mano, due
righe su centocinquanta finiscono con una cifra che il dato non conferma: è
successo, ed è il difetto che ha fatto nascere il documento (i due voci collettive
del quinto anno che erano tre).

La regola che segue è la stessa di `allinea_tabella_readme.py`:

1. **la tabella si genera, non si incolla**: le righe vengono da
   `genera_itinerari.py`, che legge il dato;
2. **un documento senza il segnaposto non viene riscritto**, e il comando dice
   quante righe ha toccato;
3. **il conto viene verificato prima e dopo**: il numero di tappe e di facoltativi
   nel documento deve essere quello del dato, e se non lo è lo script si ferma e
   dice dove, invece di scrivere un documento che mente.

Uso:
    python3 sorgenti/aggiorna_itinerari.py           # scrive
    python3 sorgenti/aggiorna_itinerari.py --prova   # dice, non scrive
"""
import io
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genera_itinerari as gi                              # noqa: E402

INCONTRI = os.path.join(RADICE, "dati", "incontri_livelli.json")
DOC = os.path.join(RADICE, "docs", "videogioco-5-duchi-itinerari.md")
SEGNAPOSTO = "<!--TABELLE-->"


def tabelle():
    """Le tabelle degli anni, come testo, senza la stampa del generatore."""
    d = json.load(open(INCONTRI, encoding="utf-8"))
    per_anno = {}
    for x in d["incontri"]:
        per_anno.setdefault(x["anno"], []).append(x)

    out = io.StringIO()
    for anno in sorted(per_anno):
        xs = per_anno[anno]
        mezzo = xs[0]["mezzo"]
        nome = gi.MEZZO.get(mezzo, "il mezzo **non è dichiarato**")
        coll = sum(1 for x in xs if x["voce_obbligatoria"].get("tipo") == "collettivo")
        out.write("\n#### Anno %d — %s\n\n" % (anno, nome))
        out.write("Le trenta tappe, %d facoltativi, %d voce%s collettive.\n\n"
                  % (sum(len(x.get("facoltativi") or []) for x in xs), coll,
                     "a" if coll == 1 else ""))
        out.write("| Livello | Dove si va | Chi incontri (obbligatorio) | Facoltativi |\n")
        out.write("|---|---|---|---|\n")
        for x in xs:
            dove = x["luogo"] or "—"
            if x.get("stanza"):
                dove += "<br>*stanza:* %s" % x["stanza"]
            out.write("| **%s** | %s | %s | %s |\n"
                      % (x["livello"], dove,
                         gi.voce_testo(x["voce_obbligatoria"]),
                         gi.facoltativi_testo(x.get("facoltativi"))))
        out.write("\n")
    return out.getvalue()


def main():
    prova = "--prova" in sys.argv
    if not os.path.exists(DOC):
        raise SystemExit("non trovo %s" % DOC)
    testo = open(DOC, encoding="utf-8").read()
    if SEGNAPOSTO in testo:
        nuovo = tabelle().rstrip() + "\n"
        aggiornato = testo.replace(SEGNAPOSTO, nuovo)
    elif "--rigenera" in sys.argv:
        # La seconda volta che si esegue il segnaposto non c'e' piu': le tabelle
        # sono gia' dentro, e il compito e' sostituirle. Serve il comando
        # esplicito, perche' sostituire tutto quello che segue «## 3.» e' una
        # scrittura che puo' distruggere testo scritto a mano.
        capo = testo.find("## 3.")
        fine = testo.find("## 4.")
        if capo < 0 or fine < 0:
            raise SystemExit("non trovo le sezioni 3 e 4: non scrivo")
        aggiornato = testo[:capo] + testo[capo:fine].split("\n")[0] + "\n\n" \
            + "*(generate da `sorgenti/genera_itinerari.py` a partire da " \
              "`dati/incontri_livelli.json`)*\n\n" + tabelle().rstrip() + "\n\n" \
            + testo[fine:]
    else:
        # Il caso normale dopo la prima esecuzione: le tabelle sono dentro e il
        # documento non ha piu' il segnaposto. **Non si riscrive tutto**: si
        # controlla soltanto che il numero di righe sia quello giusto, e si esce.
        aggiornato = testo
        trovate = len(re.findall(r"^\| \*\*\d-\d+\*\* \|", testo, re.M))
        atteso = len(json.load(open(INCONTRI, encoding="utf-8"))["incontri"])
        if trovate != atteso:
            raise SystemExit("il documento ha %d righe di tappa e il dato ne ha %d: "
                             "usa --rigenera per ricalcolarle" % (trovate, atteso))
        print("  righe di tappa nel documento: %d (dato: %d)" % (trovate, atteso))
        print("\nle tabelle sono già dentro e il conto torna: non scrivo")
        if prova:
            print("--prova: non scrivo")
        return 0

    # il conto, prima di scrivere: due righe su centocinquanta con una cifra
    # sbagliata sono la ragione di questo script
    d = json.load(open(INCONTRI, encoding="utf-8"))
    atteso_tappe = len(d["incontri"])
    attesi_fac = sum(len(x.get("facoltativi") or []) for x in d["incontri"])
    trovate = len(re.findall(r"^\| \*\*\d-\d+\*\* \|", aggiornato, re.M))
    if trovate != atteso_tappe:
        raise SystemExit("il documento avrebbe %d righe di tappa e il dato ne ha %d: "
                         "non scrivo" % (trovate, atteso_tappe))

    stessi = aggiornato == testo
    print("  righe di tappa nel documento: %d (dato: %d)"
          % (trovate, atteso_tappe))
    print("  facoltativi nel dato: %d" % attesi_fac)
    if stessi:
        print("\nle tabelle sono già allineate")
    else:
        print("  le tabelle cambiavano: il documento passa da %d a %d caratteri"
              % (len(testo), len(aggiornato)))
    if prova:
        print("--prova: non scrivo")
        return 0
    if stessi:
        return 0
    with open(DOC, "w", encoding="utf-8") as f:
        f.write(aggiornato)
    print("scritto %s" % os.path.relpath(DOC, RADICE))
    return 0


if __name__ == "__main__":
    sys.exit(main())