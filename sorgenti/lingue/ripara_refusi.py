#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ripara i refusi dei file sorgente dei titoli.

I refusi sono quasi tutti della stessa specie: il separatore `|` e una lettera
del campo `fonte` sono spariti, e qualche titolo ha dentro lettere di un'altra
scrittura. Le riparazioni sono esplicite, una per una, e non una regola
generica: in un progetto di scuola un titolo generato non si distingue da un
titolo inventato, ed è esattamente quello che non si deve lasciar passare.
"""

import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

# Riparazione esplicita: (file, numero di riga, testo rotto, testo giusto).
# Il confronto è per numero di riga e per presenza del testo rotto: se il
# file è già a posto la riga non viene toccata e lo script lo dice.
RIPARA = [
    (
        "parte_si.txt",
        40,
        "着小",
        " e il volto",
    ),
    (
        "parte_si.txt",
        84,
        "Comparative linguistics of sign languages",
        "Lingue dei segni a confronto: la linguistica applicata",
    ),
    (
        "parte_si.txt",
        120,
        "SignLanguage corpora: che cosa",
        "Corpus di segni: che cosa",
    ),
]

# Il refuso di specie: il campo `fonte` era `tema`, ma la barra e una lettera
# sono andate perse, così la riga ha finito per terminare con `teme`. Il titolo
# non cambia, cambia solo la parentesi che lo chiude.
SUFFISSO = "tema"
SUFFISSO_ROTTO = "teme"


def ripara_fonte(righe):
    """`...teme` in fondo a una riga già conforme diventa `...|tema`."""
    toccate = 0
    for i, riga in enumerate(righe):
        campi = riga.split("|")
        if len(campi) != 4 or campi[0] not in ("FE", "LA", "EN", "SI", "EL"):
            continue
        if not riga.endswith(SUFFISSO_ROTTO):
            continue
        titolo = riga[: -len(SUFFISSO_ROTTO)]
        # «sisteme» finisce anche per «teme»: la riga è rotta solo se prima dei
        # quattro caratteri c'è uno spazio o un segnale di punteggiatura, non
        # un'altra lettera.
        if titolo and not titolo[-1].isalnum():
            righe[i] = "%s|%s" % (titolo.rstrip(), SUFFISSO)
            toccate += 1
    return toccate


def ripara_esplicite(righe, nome):
    toccate = 0
    for file_, numero, rotto, giusto in RIPARA:
        if file_ != nome:
            continue
        posizione = numero - 1
        if posizione >= len(righe):
            continue
        attuale = righe[posizione]
        if rotto in attuale:
            righe[posizione] = attuale.replace(rotto, giusto)
            toccate += 1
    return toccate


def main():
    totale = 0
    for nome in sorted(os.listdir(BASE)):
        if not nome.startswith("parte_") or not nome.endswith(".txt"):
            continue
        percorso = os.path.join(BASE, nome)
        with open(percorso, encoding="utf-8") as f:
            righe = f.read().split("\n")
        n = ripara_fonte(righe) + ripara_esplicite(righe, nome)
        if n:
            with open(percorso, "w", encoding="utf-8") as f:
                f.write("\n".join(righe))
        print("%s: %d righe riparate" % (nome, n))
        totale += n
    print("totale: %d" % totale)
    return 0


if __name__ == "__main__":
    sys.exit(main())
