#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""I mezzi di trasporto, anno per anno, e quanto costano in giorni.

Il percorso del duca è già calcolato in `percorsi_confronto.py`. Qui la domanda
è un'altra: **con che cosa viaggia**, perché la stessa distanza fatta a cavallo o
in nave non è la stessa distanza fatta in diligenza, e perché negli anni 4 e 5
il duca non viaggia affatto — è il materiale che arriva.

I numeri sono **stime dichiarate**: chilometri al giorno e portata in persone per
ogni mezzo, con la fonte del tipo di mezzo (storico, documentato) separata dalla
sua velocità (stima, discussa). Il progetto non promette al giocatore una
giornata che nessuno faceva.

Uso:
    python3 sorgenti/percorsi_mezzi.py
"""
import math

# mezzo: (km al giorno, persone per viaggio, note)
MEZZI = {
    "a piedi": (25, 1, "un uomo solo, con la bisaccia"),
    "mulo": (35, 2, "la bestia da soma delle vie postali"),
    "cavallo": (45, 2, "cavaliere e scudiero, con i bagagli in sella"),
    "carrozza": (35, 4, "carrozza di corte, cambio dei cavalli ogni 30-40 km"),
    "galera": (55, 40, "galera veneziana: remi e vela, i passeggeri pagano"),
    "nave": (130, 300, "veliero latino di grossa portata, rotta dipendente dal vento"),
    "carovana": (30, 60, "carovana delle strade delle carovane, con le guide"),
    "diligenza": (45, 8, "diligenza delle poste, cambio dei cavalli ogni 10-12 km"),
    "pipa": (8, 1, "la pianta che in Cinquecento faceva il giro d'Europa"),
    "treno": (180, 200, "convoglio ferroviario, orari fissi e acquisto del biglietto"),
    "aereo": (900, 300, "volo di linea, con il tempo di attesa all'aeroporto"),
    "crociera": (200, 2000, "nave passeggeri: il tempo di attesa è il vero costo"),
}

# L'anno di ogni mezzo, e la ragione per cui quello e non un altro
SCELTE = {
    1: ("a piedi", "a piedi", "Ferrara è piccola: dalle mura al confines ci si va a piedi"),
    2: ("cavallo", "cavallo e galera",
        "la penisola si attraversa a cavallo, e il mare si prende in galera"),
    3: ("cavallo", "cavallo, galera e pipa",
        "l'Europa è unita da due reti: la strada delle poste e il mare"),
    4: ("nave", "nave, carovana e diligenza",
        "all'archivio non arriva il duca: arriva il materiale, per via d'acqua o di terra"),
    5: ("aereo", "treno e aereo",
        "il tempo è la mappa: si viaggia in treno e in aereo, e si torna spesso"),
}


def tabella():
    print("%-11s %6s %8s  %s" % ("mezzo", "km/g", "persone", "nota"))
    for nome, (km, pers, nota) in MEZZI.items():
        print("%-11s %6d %8d  %s" % (nome, km, pers, nota))


def costo(km, mezzo, soste=0.2):
    """Giorni di viaggio per `km` con il mezzo indicato."""
    velocita = MEZZI[mezzo][0]
    g = km / velocita
    return int(math.ceil(g * (1 + soste)))


def main():
    print("I mezzi, con la velocità che il progetto usa")
    tabella()
    print()

    percorsi = {
        2: (3139, "cavallo", "l'ordine delle tappe, che raddoppia il giro"),
        3: (18318, "cavallo", "l'ordine delle tappe"),
        4: (58644, "nave", "il materiale che arriva all'archivio"),
        5: (79494, "aereo", "l'ordine delle tappe"),
    }
    print("Che cosa costa ogni percorso, e con che mezzo")
    print("%-5s %-10s %-9s %8s %7s %7s" % ("anno", "mezzo", "km", "giorni", "mesi", "anni"))
    for anno, (km, mezzo, _) in sorted(percorsi.items()):
        g = costo(km, mezzo)
        print("%-5d %-10s %-9d %8d %7.1f %7.1f"
              % (anno, mezzo, km, g, g / 30, g / 365))

    print()
    print("Le alternative, anno per anno")
    for anno, (km, _, nota) in sorted(percorsi.items()):
        print("anno %d — %s" % (anno, nota))
        for voce in SCELTE[anno][1].split(","):
            m = voce.split(" e ")[-1].strip()
            if m not in MEZZI:
                continue
            print("     %-9s %5d giorni" % (m, costo(km, m)))
        print()

    print("Che cosa cambia se il percorso è quello ottimale invece di quello delle tappe")
    confronto = [
        (2, 3139, 2153, "cavallo"),
        (3, 18318, 9308, "cavallo"),
        (4, 58644, 33177, "nave"),
        (5, 79494, 33511, "aereo"),
    ]
    print("%-5s %8s %8s %8s %9s" % ("anno", "tappe", "ottimale", "risparmio", "in giorni"))
    for anno, a, b, mezzo in confronto:
        print("%-5d %8d %8d %7.0f%% %9d"
              % (anno, a, b, 100 * (a - b) / a, costo(a, mezzo) - costo(b, mezzo)))


if __name__ == "__main__":
    main()