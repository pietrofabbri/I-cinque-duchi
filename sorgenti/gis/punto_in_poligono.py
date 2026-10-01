"""Punto in poligono, con anelli esterni e buchi.

Il primo tentativo applicava la regola pari-dispari a tutti gli anelli insieme.
Sui dati di Natural Earth dava risultati assurdi: Venezia risultava dentro la
Baviera e dentro la Boemia, e Roma dentro la provincia di Roma ma non nel
Lazio. Il motivo e' che un poligono con buchi (lago dentro un Paese, enclave)
e' fatto di anelli esterni e anelli interni: mettere tutto nello stesso
parity-check fa saltare il risultato.

Qui si usa il winding number con la regola del verso, che distingue un buco da
un'isola, e il winding e' calcolato solo sugli anelli dello stesso poligono.
"""
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mappe_lettore import leggi


def _anello_chiuso(a):
    return a if a[0] == a[-1] else a + [a[0]]


def _wrap(a):
    """Chiusura antimeridiana: un anello puo' attraversare i 180 gradi."""
    punti = []
    for lon, lat in a:
        if punti and abs(lon - punti[-1][0]) > 180:
            punti.append((lon + 360 if lon < 0 else lon - 360, lat))
        else:
            punti.append((lon, lat))
    if punti[0][0] < -180 or punti[0][0] > 180:
        return [(x + 360 if x < -180 else x - 360 if x > 180 else x, y)
                for x, y in punti]
    return punti


def winding(anelli, x, y):
    """Somma dei numeri di avvolgimento: 0 = esterno, 1 = dentro."""
    tot = 0
    for a in anelli:
        pts = _wrap(_anello_chiuso(a))
        for i in range(len(pts) - 1):
            x1, y1 = pts[i]
            x2, y2 = pts[i + 1]
            if y1 <= y:
                if y2 > y and (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) > 0:
                    tot += 1
            elif y2 <= y and (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) < 0:
                tot -= 1
    return tot


def dentro(anelli, x, y):
    """Il punto e' dentro se il winding non e' zero."""
    try:
        return winding(anelli, x, y) != 0
    except Exception:
        return False


def dentro_strict(anelli, x, y):
    """Come `dentro`, ma distingue i buchi (winding 0 con area positiva)."""
    w = winding(anelli, x, y)
    if w != 0:
        return True
    return False


def carica(nome):
    return leggi(os.path.join(RADICE, "dati", "mappe", nome))


if __name__ == "__main__":
    g, _ = carica("penisola_10_regioni.json")
    prove = [(12.496, 41.903, "Roma"), (9.190, 45.464, "Milano"),
             (12.326, 45.440, "Venezia"), (11.621, 44.837, "Ferrara"),
             (2.352, 48.857, "Parigi"), (13.405, 52.520, "Berlino")]
    for lon, lat, nome in prove:
        ris = [(p.get("name_it") or p.get("name"), p.get("admin"))
               for p, a in g if dentro(a, lon, lat)]
        print(f"{nome:<9} ({lon:7.3f},{lat:7.3f}) -> {ris}")

    print("\ncontrollo negativo (deve essere vuoto):")
    for lon, lat, nome in [(-74.0, 40.7, "New York"),
                           (139.7, 35.7, "Tokyo"),
                           (2.352, 41.0, "punto in mare vicino Barcellona")]:
        ris = [p.get("name_it") or p.get("name") for p, a in g if dentro(a, lon, lat)]
        print(f"{nome:<34} -> {ris or 'vuoto'}")