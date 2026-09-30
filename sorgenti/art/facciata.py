"""Facciata della Cattedrale di San Giorgio in pixel art (vista frontale per la mappa 3/4).
Riferimenti: xilografie ottocentesche della facciata (Wikimedia Commons, pubblico dominio) e foto
"Ferrara, duomo, facciata.JPG" (sailko, CC BY 2.5) usate solo come modello di forme e colori.
Scala: 1 tessera = 16 px = 2 m circa. Larghezza 352 px (22 tessere); altezza compressa per la vista 3/4.
Elementi: tre cuspidi con rosoni, pinnacoli sui quattro pilastri, due ordini di logge gotiche,
parte bassa romanica bianca e rosa, protiro centrale con leoni stilofori, lunetta di San Giorgio,
loggia con la Madonna e timpano del Giudizio.
"""
from PIL import Image, ImageDraw
import os
os.makedirs('out', exist_ok=True)

W, H = 352, 216
C = dict(M=(236, 228, 218), m=(203, 191, 178), P=(228, 186, 172), p=(196, 150, 138),
         D=(62, 48, 50), d=(104, 86, 84), L=(140, 123, 112), R=(170, 82, 66), r=(122, 52, 42),
         S=(150, 146, 140), s=(112, 108, 104), G=(214, 170, 72), K=(40, 30, 30))
import sys
KF = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0   # fattore di scala (facciata reale 39,8 m = 509 px)
class _G:
    def __init__(s, d): s.d = d
    def _p(s, pts):
        if isinstance(pts, tuple) and len(pts) == 4 and not isinstance(pts[0], tuple):
            return tuple(round(v * KF) for v in pts)
        if isinstance(pts, tuple) and len(pts) == 2 and not isinstance(pts[0], tuple):
            return tuple(round(v * KF) for v in pts)
        return [(round(x * KF), round(y * KF)) for x, y in pts]
    def point(s, xy, fill): x, y = xy; s.d.rectangle((round(x * KF), round(y * KF), round((x + 1) * KF) - 1, round((y + 1) * KF) - 1), fill=fill)
    def rectangle(s, b, fill): s.d.rectangle((round(b[0] * KF), round(b[1] * KF), round((b[2] + 1) * KF) - 1, round((b[3] + 1) * KF) - 1), fill=fill)
    def line(s, pts, fill, width=1): s.d.line(s._p(tuple(pts)) if len(pts) == 4 else s._p(pts), fill=fill, width=max(1, round(width * KF * 0.8)))
    def polygon(s, pts, fill=None): s.d.polygon(s._p(pts), fill=fill)
    def ellipse(s, b, fill): s.d.ellipse(tuple(round(v * KF) for v in b), fill=fill)
im = Image.new('RGBA', (round(W * KF), round(H * KF)), (0, 0, 0, 0))
g = _G(ImageDraw.Draw(im))
P = lambda x, y, c: g.point((x, y), C[c])
R_ = lambda x0, y0, x1, y1, c: g.rectangle((x0, y0, x1, y1), fill=C[c])

piers = [(0, 9), (112, 121), (230, 239), (342, 351)]
secs = [(10, 111), (122, 229), (240, 341)]

def arch(x0, x1, top, bot, fill, pointed=True):
    w = x1 - x0 + 1; cx = (x0 + x1) / 2
    for y in range(top, bot + 1):
        k = y - top
        if pointed:
            half = min(w / 2, (k + 1) * (w / 2) / max(1, w * 0.6))
        else:
            r = w / 2; dy = max(0, r - k)
            half = (r * r - dy * dy) ** .5 if k < r else r
        a = int(round(cx - half)); b = int(round(cx + half)) - 1
        if b >= a:
            g.rectangle((a, y, b, y), fill=C[fill])

# ---- cuspidi ----
for i, (a, b) in enumerate(secs):
    apex = 12 if i == 1 else 20
    base = 62
    cx = (a + b) // 2
    g.polygon([(a, base), (cx, apex), (b, base)], fill=C['M'])
    g.line([(a, base), (cx, apex), (b, base)], fill=C['L'])
    # archetti pensili lungo gli spioventi
    for t in range(0, 100, 7):
        f = t / 100
        for side in (0, 1):
            x = int(a + (cx - a) * f) if side == 0 else int(b - (b - cx) * f)
            y = int(base + (apex - base) * f) + 3
            P(x, y, 'd'); P(x, y + 1, 'm')
    # rosone
    oy = apex + (base - apex) * 0.52; r = 9 if i == 1 else 7
    g.ellipse((cx - r - 1, oy - r - 1, cx + r + 1, oy + r + 1), fill=C['L'])
    g.ellipse((cx - r, oy - r, cx + r, oy + r), fill=C['D'])
    for k in range(8):
        import math
        an = k * math.pi / 4
        g.line((cx, oy, cx + math.cos(an) * r, oy + math.sin(an) * r), fill=C['m'])
    g.ellipse((cx - 2, oy - 2, cx + 2, oy + 2), fill=C['M'])
    # archetti ciechi nella cuspide
    for x in range(a + 12, b - 10, 9):
        yy = int(base - 4 - (1 - abs(x - cx) / (cx - a)) * (base - apex) * 0.25)
        arch(x, x + 5, yy - 9, yy, 'm')

# ---- pilastri e pinnacoli ----
for (a, b) in piers:
    R_(a, 10, b, H - 12, 'M'); R_(b - 2, 10, b, H - 12, 'm')
    cx = (a + b) // 2
    g.polygon([(a + 1, 12), (cx, 0), (b - 1, 12)], fill=C['M'])
    g.line([(a + 1, 12), (cx, 0), (b - 1, 12)], fill=C['L'])
    for y in (30, 64, 96, 128):
        R_(a, y, b, y + 1, 'L')

# ---- primo ordine di logge (gotico) ----
def loggia(y0, y1, step, pointed):
    for (a, b) in secs:
        R_(a, y0 - 2, b, y0 - 1, 'L')
        R_(a, y0, b, y1, 'M')
        x = a + 3
        while x + step - 3 <= b - 2:
            arch(x, x + step - 4, y0 + 2, y1 - 1, 'd', pointed)
            arch(x + 1, x + step - 5, y0 + 5, y1 - 1, 'D', pointed)
            P(x + (step - 4) // 2, y1 - 3, 'm')
            g.line((x + step - 3, y0 + 2, x + step - 3, y1), fill=C['m'])
            x += step
        R_(a, y1 + 1, b, y1 + 2, 'L')
loggia(66, 94, 9, True)
loggia(99, 121, 8, False)

# ---- parte bassa romanica (bianco e rosa) ----
for (a, b) in secs:
    R_(a, 125, b, H - 12, 'M')
    for x in range(a, b + 1, 6):
        R_(x, 125, x + 2, H - 12, 'P')
    # grandi arcate cieche
    for (u, v) in ((a + 6, (a + b) // 2 - 3), ((a + b) // 2 + 3, b - 6)):
        arch(u, v, 132, H - 14, 'm', False)
        arch(u + 2, v - 2, 134, H - 14, 'P', False)
for (a, b) in (secs[0], secs[2]):  # porte laterali
    cx = (a + b) // 2
    arch(cx - 9, cx + 9, H - 44, H - 12, 'L', False)
    arch(cx - 7, cx + 7, H - 42, H - 12, 'K', False)
    R_(cx - 1, H - 34, cx, H - 12, 'd')

# ---- protiro centrale ----
cx = (secs[1][0] + secs[1][1]) // 2
# timpano del Giudizio
g.polygon([(cx - 30, 150), (cx, 126), (cx + 30, 150)], fill=C['M'])
g.line([(cx - 30, 150), (cx, 126), (cx + 30, 150)], fill=C['L'])
for x in range(cx - 22, cx + 23, 4):
    P(x, 145, 'd'); P(x, 142, 'd' if abs(x - cx) < 16 else 'M')
# loggia con la Madonna sopra il protiro
R_(cx - 16, 104, cx + 16, 126, 'M')
g.polygon([(cx - 18, 106), (cx, 96), (cx + 18, 106)], fill=C['M'])
g.line([(cx - 18, 106), (cx, 96), (cx + 18, 106)], fill=C['L'])
arch(cx - 11, cx + 11, 108, 124, 'D', False)
R_(cx - 2, 112, cx + 2, 124, 'M'); R_(cx - 1, 110, cx + 1, 111, 'G')  # Madonna stilizzata
# arco e colonne
R_(cx - 30, 150, cx + 30, H - 12, 'M')
arch(cx - 26, cx + 26, 152, H - 12, 'L', False)
arch(cx - 22, cx + 22, 156, H - 12, 'm', False)
arch(cx - 18, cx + 18, 160, H - 12, 'K', False)
# lunetta con San Giorgio (sagoma chiara)
arch(cx - 15, cx + 15, 163, 178, 'M', False)
for (x, y) in [(-6, 174), (-5, 173), (-4, 173), (-3, 173), (-2, 173), (-1, 173), (0, 173), (1, 173), (2, 172), (3, 171), (4, 172),
               (-5, 175), (-5, 176), (-1, 175), (-1, 176), (0, 170), (0, 171), (0, 172), (-1, 169), (5, 176), (6, 177), (7, 177)]:
    P(cx + x, y, 'd')
R_(cx - 15, 179, cx + 15, 180, 'L')
# portone
R_(cx - 13, 181, cx + 13, H - 12, 'D'); R_(cx, 181, cx, H - 12, 'K')
for y in range(184, H - 12, 5):
    R_(cx - 12, y, cx + 12, y, 'd')
# colonne sui leoni
for sx in (-1, 1):
    x = cx + sx * 26
    R_(x - 2, 150, x + 2, H - 22, 'M'); R_(x + 1, 150, x + 2, H - 22, 'm')
    R_(x - 3, 150, x + 3, 152, 'L')
    # leone stiloforo (marmo rosso di Verona), disegnato a mano, rivolto verso l'esterno
    LION = ["......rrrr....",
            ".....rRRRRr...",
            "....rRRKRRRr..",
            "rr..rRRRRRRRr.",
            "rRrrRRRRRRRRr.",
            ".rRRRRRRRRrr..",
            ".rRRRRRRRRRr..",
            ".rRRRRRRRRRr..",
            ".rRrrRRrrRRr..",
            ".rRr.rRr.rRr..",
            ".rrr.rrr.rrr.."]
    for yy, row in enumerate(LION):
        for xx, ch in enumerate(row):
            if ch != '.':
                px = x - 7 + (xx if sx > 0 else 13 - xx)
                P(px, H - 23 + yy, ch)
# gradini
R_(0, H - 12, W - 1, H - 9, 'S'); R_(0, H - 8, W - 1, H - 5, 's'); R_(cx - 36, H - 12, cx + 36, H - 5, 'S')
R_(0, H - 4, W - 1, H - 1, 'S')

im.save('out/facciata.png')
bg = Image.new('RGBA', im.size, (150, 150, 150, 255)); bg.alpha_composite(im)
bg.resize((im.width * 2, im.height * 2), Image.NEAREST).save('out/_preview_facciata.png')
print(im.size)
