"""Misura il terreno di un punto con lo stesso algoritmo di `rilievo.py`, senza
Pillow.

`rilievo.py` decodifica i tasselli Terrarium con PIL. Su questa macchina PIL non
e' installato, e il progetto non installa pacchetti per un controllo. Il PNG di
Terrarium e' RGB a 8 bit con compressione zlib: si decodifica con la libreria
standard in quarantanta righe, con gli stessi cinque filtri di riga che
specifica il PNG, e il risultato e' lo stesso identico valore per ogni pixel.

Uso:
    python3 sorgenti/gis/rilievo_senza_pil.py 44.36611 33.31528
    python3 sorgenti/gis/rilievo_senza_pil.py --json 44.36611 33.31528
"""
import json
import math
import os
import struct
import sys
import urllib.error
import urllib.request
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rilievo as R

ORIGINE = R.ORIGINE
ZOOM = R.ZOOM
CACHE = {}


def decodifica_png(blob):
    """Un PNG in una griglia di triple (R, G, B)."""
    if blob[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("non e' un PNG")
    i, idat, w, h, ct = 8, b"", None, None, None
    while i < len(blob):
        ln = struct.unpack(">I", blob[i:i + 4])[0]
        tipo = blob[i + 4:i + 8]
        dati = blob[i + 8:i + 8 + ln]
        i += 12 + ln
        if tipo == b"IHDR":
            w, h, _profondita, ct = struct.unpack(">IIBB", dati[:10])
        elif tipo == b"IDAT":
            idat += dati
        elif tipo == b"IEND":
            break
    grezzo = zlib.decompress(idat)
    bpp = {0: 1, 2: 3, 4: 2, 6: 4}[ct]          # byte per pixel
    passo = w * bpp
    griglia, riga_prec, k = [], bytearray(passo), 0
    for _ in range(h):
        filtro = grezzo[k]
        k += 1
        riga = bytearray(grezzo[k:k + passo])
        k += passo
        # i cinque filtri di riga del formato PNG (RFC 2083, 6.2)
        for x in range(passo):
            a = riga[x - bpp] if x >= bpp else 0
            b = riga_prec[x]
            c = riga_prec[x - bpp] if x >= bpp else 0
            if filtro == 1:
                riga[x] = (riga[x] + a) & 255
            elif filtro == 2:
                riga[x] = (riga[x] + b) & 255
            elif filtro == 3:
                riga[x] = (riga[x] + ((a + b) >> 1)) & 255
            elif filtro == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                riga[x] = (riga[x] + (a if pa <= pb and pa <= pc
                                      else b if pb <= pc else c)) & 255
        griglia.append([(riga[i], riga[i + 1], riga[i + 2])
                        for i in range(0, passo, bpp)])
        riga_prec = riga
    return griglia


def tassello(lat, lon):
    chiave = (ZOOM, R.deg2tile(lat, lon, ZOOM))
    if chiave not in CACHE:
        x, y = chiave[1]
        url = f"{R.BASE}/{ZOOM}/{x}/{y}.png"
        req = urllib.request.Request(url, headers={"User-Agent": R.UA})
        with urllib.request.urlopen(req, timeout=60) as f:
            grezzo = f.read()
        CACHE[chiave] = [[(R_ * 256 + G + B / 256.0) - ORIGINE
                          for (R_, G, B) in riga]
                         for riga in decodifica_png(grezzo)]
    return CACHE[chiave]


def mediana(v):
    v = sorted(v)
    return v[len(v) // 2]


def misura(lat, lon):
    """Le stesse cinque chiavi di `rilievo.py`, calcolate come li calcola lui:
    mediana su 7x7 pixel, gradiente su 5 pixel, strisce con mediana."""
    x, y = R.deg2tile(lat, lon, ZOOM)
    g = tassello(lat, lon)
    h, w = len(g), len(g[0])
    i, j = R.pixel_dentro(lat, lon, ZOOM, x, y)
    if not (0 <= i < w and 0 <= j < h):
        return None

    RAGGIO = 3
    finestra = [g[jj][ii]
                for jj in range(max(0, j - RAGGIO), min(h, j + RAGGIO + 1))
                for ii in range(max(0, i - RAGGIO), min(w, i + RAGGIO + 1))]
    finestra.sort()
    quota = mediana(finestra)
    scarto = finestra[-1] - finestra[0]

    passi = 5
    m = R.metri_per_pixel(lat, ZOOM)
    righe = list(range(max(0, j - RAGGIO), min(h, j + RAGGIO + 1)))
    colonne = list(range(max(0, i - RAGGIO), min(w, i + RAGGIO + 1)))
    gx = mediana([g[jj][min(i + passi, w - 1)] for jj in righe]) - \
        mediana([g[jj][max(i - passi, 0)] for jj in righe])
    gy = mediana([g[min(j + passi, h - 1)][ii] for ii in colonne]) - \
        mediana([g[max(j - passi, 0)][ii] for ii in colonne])
    dist = 2 * passi * m
    pend = math.hypot(gx, gy) / dist * 1000.0
    espo = 0.0 if abs(gx) < 1e-6 and abs(gy) < 1e-6 else \
        (math.degrees(math.atan2(-gx, gy)) + 360.0) % 360.0
    valori = [v for riga in g for v in riga]
    return {"quota": round(quota, 1), "pend": round(pend, 1),
            "espo": round(espo, 1), "rel": round(max(valori) - min(valori), 1),
            "scarto": round(scarto, 1), "fonte": "terrarium/SRTM",
            "stato": "misurata"}


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    solo_json = "--json" in sys.argv
    for n in range(0, len(args) - 1, 2):
        lon, lat = float(args[n]), float(args[n + 1])
        m = misura(lat, lon)
        if solo_json:
            print(json.dumps(m, ensure_ascii=False))
        else:
            print(f"{lat} {lon} -> {m}")