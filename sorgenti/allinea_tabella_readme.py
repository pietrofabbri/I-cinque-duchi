"""Allinea la tabella dei documenti del README alle versioni reali dei documenti.

**Perché questo script esiste.** Il 3 ottobre 2026 uno script di aggiornamento
delle versioni ha scritto il numero nella **cella sbagliata** della tabella del
README: otto righe su trenta hanno perso il nome del documento che descrivevano, e
la coerenza riportava **zero** — perché una riga senza nome non nomina nessun
documento e quindi non può contraddirlo. Le righe sono state ricostruite a mano e
`verifica_coerenza.py` ha imparato a controllarle, ma la causa era il modo in cui la
tabella veniva aggiornata, e va toglie la causa.

**Le tre regole, che sono la lezione.**

1. La tabella si modifica **per numero di colonna letta dall'intestazione**, non
   contando le barre: la colonna del documento e quella della versione sono le
   seconde e le quinte di una riga che ne ha quattro, e sbagliarle costa un file.
2. **Una riga senza nome non viene toccata**: se la casella del documento è vuota o
   non finisce in `.md`, lo script lo dice e non scrive niente. Il motivo è che
   una riga malformata è un problema da segnalare, non da indovinare.
3. **Il file non viene riscritto se non cambia niente**, e il comando dice quante
   righe ha toccato: uno script che scrive sempre è uno script che può rompere
   sempre.

**Tre difetti che la prova ha fatto trovare** (nessuno dei tre si vedeva
leggendo il codice, e tutti e tre hanno distrutto o bloccato la tabella):

- confrontava `.md` **prima** di togliere i backtick, e la casella finisce col
  backtick: nessuna delle trenta righe era riconosciuta;
- ricostruiva la riga con `group(0)[:start(2)] + "|".join(...)`, e quel
  prefisso finisce già con la barra che chiude il numero: due barre;
- aggiungeva la barra di chiusura una seconda volta, perché le celle
  terminano con una casella vuota e il join finisce già con la barra.

La lezione: **una riga di tabella si riscrive dalle celle, non si taglia**, e
ogni riga va provata contro una copia con dentro versioni sbagliate e una casella
svuotata, se non altro perché il difetto compare solo quando lo script scrive.

Uso:
    python3 sorgenti/allinea_tabella_readme.py           # scrive
    python3 sorgenti/allinea_tabella_readme.py --prova   # dice, non scrive
"""
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(RADICE, "docs")
README = os.path.join(RADICE, "README.md")

# La riga della tabella: numero, documento, descrizione, versione. Le colonne si
# prendono dalla posizione ma si **controllano** prima di scrivere: senza il
# controllo, sbagliare la posizione distrugge il documento.
RIGA = re.compile(r"^\| *(\d+) *\|(.*)$")


def versioni():
    """Il numero reale di versione di ogni documento in docs/."""
    out = {}
    for nome in sorted(os.listdir(DOCS)):
        if not nome.endswith(".md"):
            continue
        for riga in open(os.path.join(DOCS, nome), encoding="utf-8"):
            if riga.startswith("versione:"):
                out[nome] = riga.split(":", 1)[1].strip()
                break
    return out


def main():
    prova = "--prova" in sys.argv
    ver = versioni()
    righe = open(README, encoding="utf-8").read().split("\n")
    cambiate, saltate = [], []

    for i, testo in enumerate(righe):
        m = RIGA.match(testo)
        if not m:
            continue
        numero, resto = m.group(1), m.group(2)
        # `resto` comincia con la barra che chiude la casella del numero, quindi
        # la prima parte di `celle` e' un pezzo di riga vuota: il documento e'
        # celle[1] e la versione e' celle[-2]. Contarlo a occhio e' il difetto che
        # questo script sostituisce.
        celle = [""] + resto.split("|")
        assert len(celle) >= 5, "riga %s: %d caselle, non quattro" % (numero, len(celle) - 2)
        grezzo = celle[1].strip()
        # I backtick vanno tolti **prima** del confronto con `.md`: la casella
        # contiene `nome.md`, quindi finisce con il backtick e non col nome. Era
        # l'errore che faceva saltare tutte le trenta righe.
        if not (grezzo.startswith("`") and grezzo.endswith("`")):
            saltate.append((numero, grezzo[:30] or "(vuota)"))
            continue
        nome = grezzo[1:-1]
        if not nome.endswith(".md"):
            # regola 2: non si indovina
            saltate.append((numero, nome[:30]))
            continue
        if nome not in ver:
            saltate.append((numero, nome))
            continue
        if celle[-2].strip() == ver[nome]:
            continue
        cambiate.append((numero, nome, celle[-2].strip(), ver[nome]))
        celle[-2] = " %s " % ver[nome]
        # La riga si **riscrive** dalle celle, non si taglia: `group(0)[:start(2)]`
        # finisce gia' con la barra che chiude il numero, e aggiungereci il join
        # metteva due barre e falsava tutte le righe toccate.
        # `celle` finisce con una casella vuota, quindi il join finisce gia' con
        # la barra di chiusura della riga: aggiungerne un'altra faceva `| 0.1 | |`.
        righe[i] = "| %s |%s" % (m.group(1), "|".join(celle[1:]))

    for numero, nome, prima, dopo in cambiate:
        print("  riga %-3s %-44s %s -> %s" % (numero, nome[:44], prima, dopo))
    for numero, cosa in saltate:
        print("  riga %-3s saltata: %s non è un documento di docs/" % (numero, cosa))

    print("\nrighe allineate: %d; righe saltate: %d" % (len(cambiate), len(saltate)))
    if prova:
        print("--prova: non scrivo")
        return
    if cambiate:
        with open(README, "w", encoding="utf-8") as f:
            f.write("\n".join(righe))
        print("scritto README.md")
    else:
        print("README.md era già allineato")


if __name__ == "__main__":
    main()