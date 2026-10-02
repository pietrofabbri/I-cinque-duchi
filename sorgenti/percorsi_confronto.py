#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confronta i percorsi possibili del duca, anno per anno.

Il calcolo di `percorsi_calcola.py` dice quanto è lunga la sequenza dei pin **come
sono ordinati dai numeri di tappa**. Questo script risponde a una domanda
diversa, che è quella che Pietro ha posto: che cosa succede se il percorso
**non** segue l'ordine delle tappe ma copre **tutta la mappa**, e che cosa
costano i ritorni.

Tre varianti, calcolate con la stessa formula:

  obbligatorio   i pin nell'ordine dei numeri di tappa: è il percorso che il
                 gioco propone oggi
  completo       tutti i pin del catalogo, compresi quelli fuori percorso,
                 nell'ordine che un giro più corto visiterebbe: il vicino
                 più vicino, che è l'euristica che funziona su questi insiemi
  circolare      il percorso completo chiuso in cerchio, con il ritorno dal
                 último al primo: è la forma che risponde alla domanda sul
                 tornare indietro

Il mezzo è quello dell'epoca, e la velocità è dichiarata in `percorsi_calcola.py`.
Nessun numero qui è un fatto storico: è un calcolo sulla distanza in linea
d'aria, che è il minimo teorico e non il cammino reale.

Uso:
    python3 sorgenti/percorsi_confronto.py
"""
import json
import math
import os
import collections

RADICE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LUOGHI = os.path.join(RADICE, "dati", "luoghi_gioco.json")

RAGGIO = 6371.0
MEZZI = {2: ("cavallo", 45), 3: ("cavallo", 45), 4: ("nave", 130), 5: ("aereo", 900)}
NOMI = {2: "Italia", 3: "Europa", 4: "mondo (l'archivio)", 5: "il presente"}


def hav(a, b):
    f1, f2 = math.radians(a[0]), math.radians(b[0])
    df = math.radians(b[0] - a[0])
    dl = math.radians(b[1] - a[1])
    x = math.sin(df / 2) ** 2 + math.cos(f1) * math.cos(f2) * math.sin(dl / 2) ** 2
    return 2 * RAGGIO * math.asin(math.sqrt(x))


def giorni(km, velocita):
    g = km / velocita
    return max(1, int(math.ceil(g + max(0, g // 3))))


def ordina_per_tappa(luoghi):
    return sorted(luoghi, key=lambda l: min(
        [int(t.split("-")[1]) for t in l.get("tappe", []) if "-" in t] or [99]))


def vicino_più_vicino(partenza, resto):
    """Il giro più corto che parte da `partenza`: il vicino più vicino."""
    ordine = [partenza]
    resto = list(resto)
    while resto:
        prossimo = min(resto, key=lambda l: hav(ordine[-1]["punto"], l["punto"]))
        ordine.append(prossimo)
        resto.remove(prossimo)
    return ordine


def lunghezza(ordine, velocita):
    km = 0
    gg = 0
    for a, b in zip(ordine, ordine[1:]):
        d = hav(a["punto"], b["punto"])
        km += d
        gg += giorni(d, velocita)
    return int(km), gg


def raccogli():
    with open(LUOGHI, encoding="utf-8") as f:
        dati = json.load(f)
    per = collections.defaultdict(dict)
    for l in dati["luoghi"]:
        if not l.get("lat"):
            continue
        for anno in l.get("anni", []):
            per[anno][l["luogo"]] = {"nome": l["luogo"],
                                     "punto": (l["lat"], l["lon"]),
                                     "tipo": l.get("tipo", ""),
                                     "tappe": l.get("tappe", []),
                                     "pin": l.get("pin")}
    return per


def main():
    per = raccogli()
    righe = []
    for anno in (2, 3, 4, 5):
        mezzo, velocita = MEZZI[anno]
        tutti = list(per[anno].values())
        obbligatori = [l for l in tutti if l["pin"]]
        tappa = ordina_per_tappa(obbligatori)

        km_a, gg_a = lunghezza(tappa, velocita)

        # Il giro completo parte da Ferrara, che è la base del gioco, e
        # visita tutti i luoghi del catalogo **partendo dalla base**: anche se
        # la base è già un pin, il giro la tocca due volte, all'inizio e alla
        # fine, perché tornare a Ferrara è il modo in cui un viaggio finisce.
        base = [l for l in tutti if "Ferrara" in l["nome"]]
        partenza = base[0] if base else tappa[0]
        resto = [l for l in tutti if l is not partenza]
        giro = vicino_più_vicino(partenza, resto)
        km_b, gg_b = lunghezza([partenza] + giro, velocita)

        # il giro chiuso: si torna dall'ultimo alla base
        km_c, gg_c = km_b, gg_b
        if giro:
            chiusura = hav(giro[-1]["punto"], partenza["punto"])
            km_c += int(chiusura)
            gg_c += giorni(chiusura, velocita)

        righe.append((anno, len(obbligatori), len(tutti), km_a, gg_a,
                      km_b, gg_b, km_c, gg_c, mezzo))
        print("anno %d — %s, mezzo %s" % (anno, NOMI[anno], mezzo))
        print("  pin in percorso obbligatorio : %2d   %5d km  %3d giorni"
              % (len(obbligatori), km_a, gg_a))
        print("  tutti i luoghi del catalogo  : %2d   %5d km  %3d giorni  (%.1f volte)"
              % (len(tutti), km_b, gg_b, (km_b / km_a if km_a else 0)))
        print("  giro chiuso, col ritorno    : %2d   %5d km  %3d giorni"
              % (len(tutti), km_c, gg_c))
        print()

    print("riepilogo")
    print("%-5s %-9s %8s %8s %10s %10s" % ("anno", "mezzo", "obbl.", "tutti", "gg obbl.", "gg tutti"))
    for anno, no, nt, kma, gga, kmb, ggb, kmc, ggc, mezzo in righe:
        print("%-5d %-9s %8d %8d %10d %10d" % (anno, mezzo, no, nt, gga, ggb))


if __name__ == "__main__":
    main()