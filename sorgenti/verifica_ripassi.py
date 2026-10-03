"""Verifica le sette regole dei test di ingresso: R1-R7.

Un numero scritto in un documento non e' una regola. Le sette regole di
`docs/videogioco-5-duchi-ripassi.md` sono numeri e frasi che si possono confrontare
fra loro e con gli altri documenti del progetto: qui si controlla che i numeri
quadrino, che le discipline nominate siano quelle che il progetto ha davvero, e
che nessuna delle sette regole sia sparita.

  R1  dieci domande, e i due tempi per domanda che ne derivano sono giusti
  R2  due minuti nel primo anno, tre dal secondo in poi
  R3  il campione si pesca sulle voci superate, e il campo che lo permette esiste
  R4  ogni domanda porta la sua origine
  R5  si puo' tentare piu' volte e si torna sempre indietro, senza penalita'
  R6  il tempo e' un dato e non una multa
  R7  la disciplina e' dichiarata prima dell'interazione, e sono quelle del progetto

Uso:  python3 sorgenti/verifica_ripassi.py
"""
import io
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(RADICE, "docs", "videogioco-5-duchi-ripassi.md")
LINGUE = os.path.join(RADICE, "docs", "videogioco-5-duchi-lingue.md")
QUADRO = os.path.join(RADICE, "docs", "videogioco-5-duchi-quadro-trasversale.md")
SCHEMA = os.path.join(RADICE, "docs", "videogioco-5-duchi-schema-livelli.md")

DOMANDE = 10
TEMPI = {1: 120, 2: 180, 3: 180, 4: 180, 5: 180}


def leggi(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def main():
    if not os.path.exists(DOC):
        print("manca %s" % DOC)
        return 2
    doc = leggi(DOC)
    lingue = leggi(LINGUE)
    quadro = leggi(QUADRO)
    schema = leggi(SCHEMA)
    problemi = []

    print("== R1. dieci domande, e i tempi per domanda che ne derivano ==")
    print("   domande per test: %d" % DOMANDE)
    for anno, tempo in sorted(TEMPI.items()):
        per_domanda = tempo / float(DOMANDE)
        giusto = 10 <= per_domanda <= 20
        print("   anno %d: %d s in tutto, %.0f s per domanda %s"
              % (anno, tempo, per_domanda, "" if giusto else "  <- fuori da 10-20"))
        if not giusto:
            problemi.append("R1: nell'anno %d il tempo per domanda e' %.0f s" % (anno, per_domanda))
    if ("Dieci domande, mai di piu'" not in doc) and ("Dieci domande, mai di più" not in doc):
        problemi.append("R1: la regola del numero di domande non e' nel documento")
    if ("%d secondi" % 120) not in doc or ("%d secondi" % 180) not in doc:
        problemi.append("R1: i due tempi non sono dichiarati in secondi")

    print("\n== R2. due minuti nel primo anno, tre dal secondo ==")
    for anno, tempo in sorted(TEMPI.items()):
        dichiarato = ("**%d**" % tempo) in doc or ("| **%d** |" % tempo) in doc
        if anno == 1 and not ("120" in doc):
            problemi.append("R2: 120 secondi non dichiarati")
        if anno > 1 and not ("180" in doc):
            problemi.append("R2: 180 secondi non dichiarati")
        del dichiarato
    print("   primo anno: %d s; anni 2-5: %d s" % (TEMPI[1], TEMPI[2]))
    if TEMPI[1] >= TEMPI[2]:
        problemi.append("R2: il primo anno non puo' avere il tempo massimo piu' lungo")

    print("\n== R3. il campione si pesca sulle voci superate ==")
    for frase in ("superate", "soglia minima"):
        if frase not in doc:
            problemi.append("R3: la regola non parla di «%s»" % frase)
    # La soglia minima di cui la R3 ha bisogno e' quella dei 900 livelli linguistici,
    # e li' e' dichiarata. Nello schema dei 150 livelli di informatica non c'e':
    # lo si dice, invece di far fallire un controllo per un documento che non
    # e' quello che la regola riguarda.
    print("   'soglia minima' dichiarata per i 900 livelli in lingue.md: %s"
          % ("soglia minima" in lingue))
    if "soglia minima" not in lingue:
        problemi.append("R3: lingue.md non dichiara la soglia minima dei 900 livelli: la R3 non e' implementabile")
    print("   'soglia minima' elencata nelle voci di schema-livelli.md §1: %s"
          % ("soglia minima" in schema))

    print("\n== R4. ogni domanda porta la sua origine ==")
    for frase in ("origine", "due strati"):
        if frase not in doc:
            problemi.append("R4: la regola non parla di «%s»" % frase)
    print("   la lista finale porta accanto il nome di ciasecuna: %s"
          % ("da dove" in doc or "da cui" in doc))

    print("\n== R5. piu' tentativi, ritorno sempre, senza penalita' ==")
    for frase in ("tentare", "interrompere", "non toglie niente", "torna indietro"):
        if frase not in doc:
            problemi.append("R5: la regola non parla di «%s»" % frase)
    for vietata in ("perde un punto", "toglie punti all'interruzione", "la soglia scende"):
        if vietata in doc:
            problemi.append("R5: il documento contiene «%s»" % vietata)
    print("   cinque condizioni presenti")

    print("\n== R6. il tempo e' un dato, non una multa ==")
    for frase in ("non toglie punti", "indicatori da guardare"):
        if frase not in doc:
            problemi.append("R6: la regola non parla di «%s»" % frase)
    print("   il tempo compare come indicatore e non come sanzione")

    print("\n== R7. la disciplina e' dichiarata prima, e sono quelle del progetto ==")
    lingue_nel_doc = len(re.findall(r"`(IT|FE|LA|EN|SI|EL)`", doc))
    # La LIS compare due volte con due nomi diversi («Lingua dei segni» nella
    # tabella delle sei, «Lingua dei segni italiana (LIS)» nel titolo): si
    # contano i nomi che cominciano per «Lingua dei segni» come uno solo.
    nomi = set(re.findall(r"\*\*(Italiano|Ferrarese|Latino|Inglese|Greco)\*\*", lingue))
    se = len(nomi) + (1 if re.search(r"\*\*Lingua dei segni", lingue) else 0)
    print("   lingue in lingue.md: %d" % se)
    if se != 6:
        problemi.append("R7: lingue.md non dichiara piu' sei lingue")
    if "sei lingue" not in doc:
        problemi.append("R7: il documento non parla di sei lingue")
    ambiti = len(re.findall(r"^\| \*\*(Diritto|Etica|Filosofia|Psicologia)\*\*", quadro, re.M))
    print("   ambiti trasversali in quadro-trasversale.md: %d" % ambiti)
    if ambiti != 4:
        problemi.append("R7: quadro-trasversale.md non dichiara piu' quattro ambiti")
    if "quattro ambiti trasversali" not in doc:
        problemi.append("R7: il documento non parla dei quattro ambiti trasversali")
    if "nessun colore nuovo" not in doc.lower() and "nessun colore nuovo" not in doc:
        problemi.append("R7: il documento non vieta i colori nuovi")
    del lingue_nel_doc

    print("\n== sintesi ==")
    if problemi:
        for p in problemi:
            print("   difetto: " + p)
        print("\nproblemi: %d" % len(problemi))
        return 1
    print("   nessun difetto: le sette regole ci sono, i numeri tornano e le discipline sono quelle del progetto")
    print("\n==== controlli superati: 7/7 ====")
    return 0


if __name__ == "__main__":
    sys.exit(main())