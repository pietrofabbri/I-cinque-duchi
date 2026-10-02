#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calcola il percorso del duca: distanze fra i pin di ogni anno e tempi di viaggio.

Il gioco ha deciso che ogni tappa ha un solo pin, e i pin sono sparsi su un
continente intero. La domanda che ne segue è se quei trenta luoghi si possano
visitare in un ordine che un uomo del Quattrocento attraverserebbe davvero, e
quanto tempo ci vuole. Il calcolo non indaga nulla: usa la formula
dell'haversine sulle coordinate che sono già in `dati/luoghi_gioco.json`, e i
mezzi di trasporto sono quelli dell'epoca.

I tempi sono **stime dichiarate**, non dati: sono la velocità media giornaliera
di un mezzo, cioè quanti chilometri al giorno una persona poteva fare davvero,
divisi in tappe da sosta. Servono a una cosa sola, che è capire se un percorso
è possibile, e non sostituiscono un controllo storico sulle fonti.

Uso:
    python3 sorgenti/percorsi_calcola.py            # tutti gli anni
    python3 sorgenti/percorsi_calcola.py 3          # un anno
"""
import json
import math
import os
import sys
import unicodedata

RADICE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LUOGHI = os.path.join(RADICE, "dati", "luoghi_gioco.json")

RAGGIO = 6371.0

# Chilometri al giorno, per mezzo ed epoca. I valori sono deliberatamente
# prudenti: una distanza percorsa «in media» non è una distanza percorsa «in
# giornata», e il progetto non può promettere al giocatore una giornata che
# nessuno faceva.
MEZZI = {
    "a piedi": 25,
    "cavallo": 45,
    "carrozza": 35,
    "barca": 60,
    "nave": 130,
    "carovana": 30,
    "diligenza": 45,
    "treno": 180,
    "aereo": 900,
    "navi a vapore": 200,
    "corrente": 40,
}

# L'anno 4 e il 5 vedono il duca non viaggiare (l'archivio, il cantiere), ma
# gli arriva materiale da ogni parte. Le distanze sono comunque calcolate, perché
# servono a capire quanto materiale «arriva» e da quanto lontano.
EPOCHE = {
    1: ("a piedi", 1470),
    2: ("cavallo", 1500),
    3: ("cavallo", 1530),
    4: ("diligenza", 1750),
    5: ("treno", 1970),
}


def haversine(lat1, lon1, lat2, lon2):
    """Chilometri in linea d'aria fra due punti."""
    f1, f2 = math.radians(lat1), math.radians(lat2)
    df = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(df / 2) ** 2 + math.cos(f1) * math.cos(f2) * math.sin(dl / 2) ** 2
    return 2 * RAGGIO * math.asin(math.sqrt(a))


def chiave(nome):
    """Il nome senza accenti e senza punteggiatura, per unire forme diverse."""
    n = unicodedata.normalize("NFKD", nome)
    n = "".join(c for c in n if not unicodedata.combining(c))
    return "".join(c for c in n.lower() if c.isalnum() or c == " ")


def normalizza(nome):
    """Le stesse chiavi, con gli zeri e gli spazi normalizzati."""
    n = unicodedata.normalize("NFKD", nome)
    n = "".join(c for c in n if not unicodedata.combining(c))
    n = n.lower()
    for segno in ("`", "'", "’"):
        n = n.replace(segno, "")
    return " ".join(n.split())


def tempo(km, mezzo):
    """Giorni di viaggio, arrotondati verso l'alto, con una sosta ogni tre."""
    velocita = MEZZI[mezzo]
    giorni = km / velocita
    return max(1, int(math.ceil(giorni + max(0, giorni // 3))))


def raccogli():
    with open(LUOGHI, encoding="utf-8") as f:
        dati = json.load(f)
    per_anno = {}
    for l in dati["luoghi"]:
        if not l.get("pin") or not l.get("lat"):
            continue
        for anno in l.get("anni", []):
            per_anno.setdefault(anno, {}).setdefault(normalizza(l["luogo"]), l)
    return per_anno


def percorso(anno, per_anno):
    """Il percorso nell'ordine dei numeri di tappa, se i pin lo dichiarano.

    I luoghi hanno `tappe` con i numeri, quindi l'ordine esiste già nei dati e
    non va indovinato. Dove il numero non c'è, il luogo va a fine percorso e
    viene detto.
    """
    luoghi = per_anno.get(anno, {})
    con_numero, senza = [], []
    for nome, l in luoghi.items():
        numeri = [int(t.split("-")[1]) for t in l.get("tappe", []) if "-" in t]
        if numeri:
            con_numero.append((min(numeri), nome, l))
        else:
            senza.append((nome, l))
    con_numero.sort()
    return con_numero, senza


def main():
    argomenti = [a for a in sys.argv[1:] if a.isdigit()]
    anni = [int(a) for a in argomenti] or [2, 3, 4, 5]
    per_anno = raccogli()

    for anno in anni:
        con_numero, senza = percorso(anno, per_anno)
        mezzo, epoca = EPOCHE.get(anno, ("cavallo", 1500))
        print("=" * 72)
        print("anno %d — mezzo %s, epoca %d" % (anno, mezzo, epoca))
        print("pin con numero di tappa: %d, senza: %d" % (len(con_numero), len(senza)))
        totale = 0
        giorni = 0
        precedente = None
        for numero, nome, l in con_numero:
            lat, lon = l["lat"], l["lon"]
            if precedente is None:
                segno = "partenza"
                km = 0
            else:
                km = haversine(precedente[1], precedente[2], lat, lon)
                segno = "%5d km" % int(km)
            g = tempo(km, mezzo)
            totale += km
            giorni += g
            if km > 900:
                segno += "  LONTANO"
            print("  %2d  %-34s %-12s %3d g   %s"
                  % (numero, nome[:34], segno, g, l.get("tipo", "")))
            precedente = (nome, lat, lon)
        print("  --- percorso: %d km in %d giorni (%d mesi)"
              % (int(totale), giorni, round(giorni / 30)))
        if senza:
            print("  --- senza numero di tappa:")
            for nome, l in senza:
                print("      %s" % nome)


if __name__ == "__main__":
    main()