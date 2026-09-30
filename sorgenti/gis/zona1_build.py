"""Costruisce i dati della zona percorribile della tappa 1-1 (piazza della Cattedrale).

Fonti (open data del Comune di Ferrara, WFS sit.comune.fe.it, lette con il browser integrato):
- Ferrara:Edifici_preview            -> sagome degli edifici (gis/edifici_centro_local.json)
- Ferrara:Fabbricati_USAGE_preview   -> altezza H misurata con LIDAR (gis/zona1_dati.json)
- Ferrara:Aree_pedonali_esistenti    -> piazze e vie pedonali (gis/zona1_dati.json)
- Ferrara:Potenziale_solare_edifici  -> falde dei tetti con orientamento (gis/zona1_dati.json)

Sistema della mappa di gioco (vista dall'alto 3/4, stile GBA):
- origine F = centro della facciata della Cattedrale; asse "giu" = normale uscente della facciata (verso ONO),
  asse "destra" = SSO. Cosi la facciata guarda verso chi gioca e la Loggia dei Merciai sta a destra.
- u = metri verso destra, v = metri verso il basso. 1 tessera = 1,25 m = 16 px.
Uscita: gis/zona1_mappa.json
"""
import json, math

LAT0, LON0 = 44.8375, 11.62
KX = 111320 * math.cos(math.radians(LAT0)); KY = 110540
M_PER_TILE = 1.25

E = json.load(open('gis/edifici_centro_local.json'))['edifici']
Z = json.load(open('gis/zona1_dati.json'))
MAP = json.load(open('videogioco-5-duchi-anno1-mappa.json'))

# --- facciata: lato 0-1 del poligono 129472 (Cattedrale) ---
cat = [e for e in E if e[0] == 129472][0][3][0][0]
A, B = cat[0], cat[2]
L = math.hypot(B[0] - A[0], B[1] - A[1])
d = ((B[0] - A[0]) / L, (B[1] - A[1]) / L)
n = (-d[1], d[0])                     # anello orario: normale uscente a sinistra
F = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
up = (-n[0], -n[1]); right = (up[1], -up[0])

def to_map(p):
    x, y = p[0] - F[0], p[1] - F[1]
    return (round(x * right[0] + y * right[1], 2), round(x * n[0] + y * n[1], 2))

def to_local(u, v):
    return (F[0] + u * right[0] + v * n[0], F[1] + u * right[1] + v * n[1])

def to_ll(u, v):
    x, y = to_local(u, v)
    return (LAT0 + y / KY, LON0 + x / KX)

# --- punto della tappa 1: 10 m davanti al centro della facciata ---
P1 = (0.0, 10.0)
lat1, lon1 = to_ll(*P1)

# --- tappe vicine in coordinate di mappa ---
tappe = []
for t in MAP['tappe']:
    c = t.get('coordinate')
    if not c: continue
    x = (c['lon'] - LON0) * KX; y = (c['lat'] - LAT0) * KY
    uv = P1 if t['livello'] == '1-1' else to_map((x, y))
    tappe.append((t['livello'], uv))

# --- cella di Voronoi della tappa 1 (taglio per semipiani) entro 150 m ---
def clip(poly, a, b, c):  # tiene a*u+b*v <= c
    out = []
    for i in range(len(poly)):
        p, q = poly[i], poly[(i + 1) % len(poly)]
        fp = a * p[0] + b * p[1] - c; fq = a * q[0] + b * q[1] - c
        if fp <= 0: out.append(p)
        if fp * fq < 0:
            t = fp / (fp - fq); out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out
R = 150
cell = [(P1[0] + R * math.cos(k * math.pi / 32), P1[1] + R * math.sin(k * math.pi / 32)) for k in range(64)]
for lv, q in tappe:
    if lv == '1-1': continue
    a, b = q[0] - P1[0], q[1] - P1[1]
    c = (q[0] ** 2 + q[1] ** 2 - P1[0] ** 2 - P1[1] ** 2) / 2
    cell = clip(cell, a, b, c)
cell = [(round(u, 2), round(v, 2)) for u, v in cell]

# --- rettangolo della mappa di gioco ---
U0, U1, V0, V1 = -135.0, 70.0, -110.0, 70.0

def inside_box(poly):
    return any(U0 - 30 < u < U1 + 30 and V0 - 60 < v < V1 + 30 for u, v in poly)

# --- altezze: fabbricato catastale che contiene il baricentro ---
def pip(pt, ring):
    x, y = pt; ins = False
    for i in range(len(ring) - 1):
        (x1, y1), (x2, y2) = ring[i], ring[i + 1]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1: ins = not ins
    return ins
fab = [(f[0][0], f[1]) for f in Z['fabbricati'] if f[1]]
def height_at(pt):
    best = None
    for H, g in fab:
        for poly in g:
            if pip(pt, poly[0]):
                if H and (best is None or H > best): best = H
    return best

def centroid(r):
    xs = [p[0] for p in r[:-1]]; ys = [p[1] for p in r[:-1]]
    return (sum(xs) / len(xs), sum(ys) / len(ys))

buildings = []
for e in E:
    for poly in e[3]:
        ring = poly[0]
        m = [to_map(p) for p in ring]
        if not inside_box(m): continue
        # altezza: media dei campioni interni che cadono in un fabbricato
        H = height_at(centroid(ring))
        if H is None:
            H = 11.0; src = 'stima'
        else:
            src = 'lidar'
        kind = 'cattedrale' if e[0] == 129472 else 'edificio'
        buildings.append({'id': e[0], 'k': kind, 'h': round(H, 1), 'hs': src,
                          'p': [list(q) for q in m[:-1]],
                          'holes': [[list(to_map(p)) for p in h[:-1]] for h in poly[1:]]})

# --- falde dei tetti (orientamento in gradi da nord, pendenza) ---
falde = []
for (orient, pend), g in [(f[0], f[1]) for f in Z['falde'] if f[1]]:
    for poly in g:
        m = [to_map(p) for p in poly[0]]
        if not inside_box(m): continue
        # orientamento nel sistema di mappa: angolo della direzione di discesa rispetto a "giu"
        a = math.radians(orient)                      # 0 = nord, 90 = est
        dx, dy = math.sin(a), math.cos(a)              # vettore locale
        du = dx * right[0] + dy * right[1]; dv = dx * n[0] + dy * n[1]
        falde.append({'o': [round(du, 3), round(dv, 3)], 's': pend, 'p': [list(q) for q in m[:-1]]})

ped = []
for (nome,), g in [(f[0], f[1]) for f in Z['pedonali'] if f[1]]:
    for poly in g:
        m = [to_map(p) for p in poly[0]]
        if inside_box(m): ped.append({'nome': nome, 'p': [list(q) for q in m[:-1]]})

out = {
    'versione': '0.1', 'descrizione': 'Zona percorribile della tappa 1-1, generata da gis/zona1_build.py',
    'fonte': 'Comune di Ferrara, open data WFS sit.comune.fe.it (Edifici, Fabbricati_USAGE, Aree_pedonali_esistenti, Potenziale_solare_edifici)',
    'sistema': {'origine_locale_m': F, 'giu': n, 'destra': right, 'm_per_tessera': M_PER_TILE,
                'nota': 'u verso destra (SSO), v verso il basso (ONO): la facciata della Cattedrale guarda chi gioca'},
    'rettangolo': [U0, U1, V0, V1],
    'tappa1': {'uv': P1, 'lat': round(lat1, 6), 'lon': round(lon1, 6)},
    'tappe_vicine': [{'livello': lv, 'uv': [round(q[0], 1), round(q[1], 1)]} for lv, q in tappe
                     if U0 - 200 < q[0] < U1 + 200 and V0 - 200 < q[1] < V1 + 200],
    'zona': cell, 'edifici': buildings, 'falde': falde, 'pedonali': ped,
}
json.dump(out, open('gis/zona1_mappa.json', 'w'), separators=(',', ':'))
print('edifici', len(buildings), 'falde', len(falde), 'pedonali', len(ped), 'zona', len(cell))
print('tappa1', out['tappa1'])
print('vicine', out['tappe_vicine'])
us = [p[0] for p in cell]; vs = [p[1] for p in cell]
print('zona u', min(us), max(us), 'v', min(vs), max(vs))
print('altezze lidar', sum(b['hs'] == 'lidar' for b in buildings), 'cattedrale h', [b['h'] for b in buildings if b['k'] == 'cattedrale'])
