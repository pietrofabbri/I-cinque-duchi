"""Disegna in SVG le mappe estratte, per controllarle a vista.

Nessuna libreria: i file si aprono con doppio clic nel browser. Serve a vedere
se coste, confini e posizioni delle citta' sono davvero quelli giunti, prima di
fidarsi dei numeri e prima di archiviare.
"""
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mappe_lettore import leggi

OUT = os.path.join(RADICE, "dati", "mappe")
SVG = os.path.join(RADICE, "verifica")
os.makedirs(SVG, exist_ok=True)


def pagina(nome, titolo, bbox, W=940, H=640, stile="", nome_pt=None):
    geom, punti = leggi(os.path.join(OUT, nome))
    x0, y0, x1, y1 = bbox
    s = min(W / (x1 - x0), H / (y1 - y0))
    ox = (W - (x1 - x0) * s) / 2
    oy = (H - (y1 - y0) * s) / 2

    def sch(pt):
        return (ox + (pt[0] - x0) * s, oy + (y1 - pt[1]) * s)

    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
           'viewBox="0 0 %d %d">' % (W, H, W, H)]
    svg.append('<rect width="%d" height="%d" fill="#f6fafc"/>' % (W, H))
    svg.append('<g fill="none" stroke="#3c5a70" stroke-width="0.9" ' + stile + ">")
    for props, anelli in geom:
        for a in anelli:
            if len(a) < 2:
                continue
            p = " ".join("%.1f,%.1f" % sch(pt) for pt in a)
            svg.append('<polygon points="%s"/>' % p)
    svg.append("</g>")
    svg.append('<g fill="#c0392b" stroke="#7b241c" stroke-width="0.6">')
    for props, x, y in punti:
        X, Y = sch((x, y))
        svg.append('<circle cx="%.1f" cy="%.1f" r="2.4"/>' % (X, Y))
    svg.append("</g>")
    if nome_pt:
        svg.append('<g font-family="sans-serif" font-size="8.5" fill="#123">')
        for props, x, y in punti:
            nm = props.get(nome_pt) or props.get("NAMEASCII") or ""
            if not nm:
                continue
            X, Y = sch((x, y))
            svg.append('<text x="%.1f" y="%.1f">%s</text>' % (X + 4, Y + 3, nm))
        svg.append("</g>")
    svg.append('<text x="14" y="26" font-size="15" font-family="sans-serif" '
               'fill="#0d1b26">%s</text>' % titolo)
    svg.append('<text x="14" y="44" font-size="10" font-family="sans-serif" '
               'fill="#54687a">%d geometrie, %d punti &#183; %s</text>'
               % (len(geom), len(punti), nome))
    svg.append("</svg>")
    path = os.path.join(SVG, nome.replace(".json", ".svg"))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(path)


IT = [5.0, 34.0, 20.0, 49.5]
EU = [-25.0, 33.0, 46.0, 73.0]

pagina("penisola_10_coste.json", "Anno 2 — coste d'Italia e isole", IT,
       stile='stroke="#1d6fa5" stroke-width="1.2"')
pagina("penisola_10_paesi.json", "Anno 2 — paesi confinanti", IT,
       stile='fill="#e6eddc" stroke="#6d8f5c" stroke-width="1"')
pagina("penisola_10_regioni.json", "Anno 2 — regioni e province", IT,
       stile='fill="#eef0e2" stroke="#87996a" stroke-width="0.7"')
pagina("penisola_10_fiumi.json", "Anno 2 — fiumi e laghi", IT,
       stile='stroke="#2e7dbf" stroke-width="1.4"')
pagina("penisola_10_citta.json", "Anno 2 — città (punti reali)", [6.0, 36.0, 19.0, 47.5],
       nome_pt="NAME_IT")
pagina("europa_50_paesi.json", "Anno 3 — Europa", EU,
       stile='fill="#eae7dd" stroke="#8a7f5c"')
pagina("europa_50_citta.json", "Anno 3 — città europee", [-11.0, 36.0, 32.0, 61.0],
       nome_pt="NAMEASCII")
pagina("mondo_110_paesi.json", "Anno 4 — il mondo", [-175.0, -50.0, 180.0, 78.0],
       W=1120, H=560, stile='fill="#eae7dd" stroke="#8a7f5c"')