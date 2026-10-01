"""Estrae da Natural Earth le geometrie che servono, in formato compatto a delta.

Tre correzioni rispetto alla prima stesione, tutte trovate dalla verifica numerica
(`verifica_mappe_numeriche.py`) e tutte annotate dove servono:

1. il delta riparte **da capo a ogni anello**, non solo a ogni geometria: prima il
   lettore ripartiva da zero e lo scrittore no, e tutti gli anelli interni (i
   "buchi" dei laghi, le isole dentro altre) risultavano spostati di chilometri;
2. i poligoni **non vengono ritagliati** al riquadro. Il ritaglio geometrico
   (Sutherland-Hodgman) produce un anello auto-intersecante quando il poligono
   esce e rientra, e un anello cosi' faceva dire al punto-in-poligono che Venezia
   era dentro la Baviera. Si scarta invece, anello per anello, cio' che non tocca
   il riquadro, e si lascia il ritaglio al motore;
3. la semplificazione di un anello chiuso va fatta togliendo il vertice finale
   duplicato (`dp_chiuso`): con l'anello chiuso il segmento di chiusura ha
   lunghezza zero e l'algoritmo butta via quasi tutto, riducendo la Sardegna a un
   segno.

Il formato e' spiegato in `mappe_lettore.py`.
"""
import json
import math
import os
import sys

# Radice del progetto: due livelli sopra questa cartella.
RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shapefile

# I shapefile scaricati e i file prodotti stanno in una cartella di lavoro
# fuori dal repository: i dati geografici grezzi sono grandi e il progetto
# tiene solo i file estratti, che sono molto piu' piccoli.
LAVORO = os.environ.get("MAPPE_LAVORO", "/tmp/ne-mappe")
NE, OUT = os.path.join(LAVORO, "ne"), os.path.join(RADICE, "dati", "mappe")
os.makedirs(OUT, exist_ok=True)

TYPE = {0: "null", 1: "punto", 3: "linea", 5: "poligono", 8: "multipunto"}


def le(shp):
    r = shapefile.Reader(os.path.join(NE, shp))
    campi = [f[0] for f in r.fields[1:]]
    for sr in r.iterShapeRecords():
        if not sr.shape.points:
            continue
        d = dict(zip(campi, sr.record))
        gt = TYPE.get(sr.shape.shapeType, "poligono")
        pts = sr.shape.points
        # in un PointShape pyshp lascia `parts` vuoto: senza questo caso il
        # ciclo qui sotto non produrrebbe nessun segmento e la citta' sparisce
        parti = list(sr.shape.parts) or [0]
        parti = parti + [len(pts)]
        minimo = 4 if gt == "poligono" else (1 if gt == "punto" else 2)
        segs = [pts[parti[i]:parti[i + 1]] for i in range(len(parti) - 1)]
        segs = [s for s in segs if len(s) >= minimo]
        if segs:
            yield d, gt, segs


def dp_chiuso(pts, tol, min_pt=4):
    """Douglas-Peucker su un anello chiuso.

    Va chiamato togliendo il vertice finale duplicato: con l'anello chiuso,
    il segmento che unisce l'ultimo vertice al primo e' di lunghezza zero, e
    l'algoritmo lo tratta come un punto. Il risultato e' che vengono tenuti
    solo i punti lontani dall'inizio e tutti gli altri vengono buttati via: la
    Sardegna si riduceva a un segno e Cagliari ne cadeva fuori. E' il difetto
    piu' subdolo incontrato, perche' il file restava ben formato e il difetto
    si vedeva solo con il punto-in-poligono.
    """
    if len(pts) > 1 and pts[0] == pts[-1]:
        aperto = pts[:-1]
    else:
        aperto = pts
    out = dp(aperto, tol, min_pt)
    if len(out) >= 3:
        out = out + [out[0]]
    return out


def dp(pts, tol, min_pt=4):
    """Douglas-Peucker iterativo: tiene i punti che superano la tolleranza."""
    if len(pts) <= min_pt:
        return pts
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        i, j = stack.pop()
        if j <= i + 1:
            continue
        ax, ay, bx, by = pts[i][0], pts[i][1], pts[j][0], pts[j][1]
        dx, dy = bx - ax, by - ay
        n = dx * dx + dy * dy
        best, bi = -1.0, -1
        for k in range(i + 1, j):
            px, py = pts[k][0], pts[k][1]
            if n == 0:
                dd = math.hypot(px - ax, py - ay)
            else:
                t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / n))
                dd = math.hypot(px - (ax + t * dx), py - (ay + t * dy))
            if dd > best:
                best, bi = dd, k
        if best > tol:
            keep[bi] = True
            stack += [(i, bi), (bi, j)]
    return [p for p, k in zip(pts, keep) if k]


def _dentro(p, box):
    x0, y0, x1, y1 = box
    return x0 <= p[0] <= x1 and y0 <= p[1] <= y1


def _bbox(segs):
    xs = [p[0] for s in segs for p in s]
    ys = [p[1] for s in segs for p in s]
    return (min(xs), min(ys), max(xs), max(ys))


def _interseca(b, box):
    return not (b[2] < box[0] or b[0] > box[2]
                or b[3] < box[1] or b[1] > box[3])


def _tocca(punti, box, cuscinetto=0.0):
    """Il segmento (o l'anello) passa dentro il riquadro, se tolto il cuscinetto?"""
    x0, y0, x1, y1 = box
    if cuscinetto:
        x0 -= cuscinetto
        x1 += cuscinetto
        y0 -= cuscinetto
        y1 += cuscinetto
    dentro = False
    for x, y in punti:
        if x0 <= x <= x1 and y0 <= y <= y1:
            return True
    # controllo sui segmenti: due punti fuori possono attraversare il riquadro
    for i in range(len(punti) - 1):
        ax, ay = punti[i]
        bx, by = punti[i + 1]
        if min(ax, bx) > x1 or max(ax, bx) < x0:
            continue
        if min(ay, by) > y1 or max(ay, by) < y0:
            continue
        return True
    return dentro


def taglia(segs, gt, box, tol):
    """Semplifica e, se c'e' un riquadro, scarta cio' che non lo tocca.

    Nota importante: i poligoni NON vengono ritagliati geometricamente. Il
    ritaglio con riquadro (Sutherland-Hodgman) produce un anello che si
    auto-interseca quando il poligono esce e rientra dal riquadro, e un anello
    cosi' falsifica sia il disegno sia ogni controllo punto-in-poligono: la
    prima versione di questo script arrivava a dire che Venezia era dentro la
    Baviera. Si tiene quindi il poligono intero e lascia al motore il compito di
    tagliare la finestra, che e' un'operazione gratuita e corretta.

    Gli anelli che stanno fuori dal riquadro vengono pero' scartati uno a uno:
    un Paese che confina appena con l'Italia deve portare solo i suoi anelli
    vicini, non tutta la Francia.
    """
    out = []
    minimo = 4 if gt == "poligono" else 2
    if box is not None and not _interseca(_bbox(segs), box):
        return []
    for s in segs:
        if box is not None and not _tocca(s, box):
            continue
        if gt == "poligono":
            # un anello va semplificato come anello chiuso, vedi `dp_chiuso`
            s2 = dp_chiuso(s, tol, 4)
            if len(s2) > 1 and s2[0] == s2[-1]:
                s2 = s2[:-1]
        else:
            s2 = dp(s, tol, 2)
        if len(s2) >= minimo:
            out.append(s2)
    return out


def scrivi(path, feats, punti, q):
    """Il delta riparte a ogni anello: il lettore fa lo stesso."""
    with open(path, "w", encoding="utf-8") as f:
        f.write('{"q":%g,"f":[' % q)
        for n, (props, segs) in enumerate(feats):
            if n:
                f.write(",")
            # ogni geometria e' [props, anello1, anello2, ...] e le props sono
            # un array: se fossero un oggetto il file non sarebbe JSON valido
            f.write(json.dumps([props], ensure_ascii=False, separators=(",", ":")))
            for seg in segs:
                px = py = 0
                buf, prec = [], None
                for x, y in seg:
                    ix, iy = int(round(x * q)), int(round(y * q))
                    if (ix, iy) == prec:
                        continue
                    prec = (ix, iy)
                    buf.append("%d,%d" % (ix - px, iy - py))
                    px, py = ix, iy
                if len(buf) > 2:
                    f.write(",[" + ";".join(buf) + "]")
        f.write('],"p":[')
        for n, (props, x, y) in enumerate(punti):
            if n:
                f.write(",")
            f.write(json.dumps([props, round(x, 5), round(y, 5)],
                               ensure_ascii=False, separators=(",", ":")))
        f.write("]}")
    return os.path.getsize(path)


EUROPA = [-26.0, 33.0, 46.0, 73.0]
ITALIA = [5.0, 34.0, 20.0, 49.5]
GIRO = [5.0, 34.0, 20.0, 49.5]   # riquadro dell'anno 2

LAVORI = [
    ("mondo_110_paesi", "110m/cultural/ne_110m_admin_0_countries", 0.30, 100,
     ["name_it", "name", "CONTINENT", "POP_EST", "ISO_A3", "ADM0_A3"], None),
    ("mondo_110_terre", "110m/physical/ne_110m_land", 0.30, 100,
     ["featurecla"], None),
    ("mondo_110_fiumi", "110m/physical/ne_110m_rivers_lake_centerlines", 0.30, 100,
     ["name", "name_it"], None),
    ("mondo_110_laghi", "110m/physical/ne_110m_lakes", 0.25, 100,
     ["name", "name_it"], None),
    ("mondo_110_regioni", "110m/physical/ne_110m_geography_regions_polys", 0.40, 100,
     ["name", "featurecla", "LABELRANK"], None),

    ("europa_50_paesi", "50m/cultural/ne_50m_admin_0_countries", 0.06, 2000,
     ["name_it", "name", "CONTINENT", "POP_EST", "ISO_A3", "ADM0_A3"], EUROPA),
    ("europa_50_terre", "50m/physical/ne_50m_land", 0.06, 2000,
     ["featurecla"], EUROPA),
    ("europa_50_fiumi", "50m/physical/ne_50m_rivers_lake_centerlines", 0.08, 2000,
     ["name", "name_it"], EUROPA),
    ("europa_50_laghi", "50m/physical/ne_50m_lakes", 0.06, 2000,
     ["name", "name_it"], EUROPA),
    ("europa_50_citta", "50m/cultural/ne_50m_populated_places", 0, 2000,
     ["NAME", "NAMEASCII", "NAME_IT", "POP_MAX", "ADM1NAME", "ADM0NAME",
      "FEATURECLA", "SOV_A3"], EUROPA),
    ("europa_50_regioni", "50m/physical/ne_50m_geography_regions_polys", 0.15, 2000,
     ["name", "featurecla", "LABELRANK"], EUROPA),

    ("penisola_10_paesi", "10m/cultural/ne_10m_admin_0_countries", 0.002, 20000,
     ["name_it", "name", "ISO_A2", "ADM0_A3", "POP_EST", "ADMIN"], ITALIA),
    ("penisola_10_regioni", "10m/cultural/ne_10m_admin_1_states_provinces", 0.006, 20000,
     ["name_it", "name", "admin", "adm1_code", "type_en", "iso_3166_2"], ITALIA),
    ("europa_50_regioni_amministrative", "10m/cultural/ne_10m_admin_1_states_provinces", 0.05, 2000,
     ["name_it", "name", "admin", "adm1_code", "type_en"], EUROPA),
    ("penisola_10_coste", "10m/physical/ne_10m_coastline", 0.002, 20000,
     ["featurecla"], ITALIA),
    ("penisola_10_fiumi", "10m/physical/ne_10m_rivers_lake_centerlines_scale_rank", 0.012, 20000,
     ["name", "name_it", "scalerank"], ITALIA),
    ("penisola_10_laghi", "10m/physical/ne_10m_lakes", 0.012, 20000,
     ["name", "name_it"], ITALIA),
    ("penisola_10_citta", "10m/cultural/ne_10m_populated_places", 0, 20000,
     ["NAME", "NAMEASCII", "NAME_IT", "POP_MAX", "ADM1NAME", "ADM0NAME",
      "FEATURECLA", "SOV_A3", "WORLDCITY"], ITALIA),
    ("penisola_10_regioni_fisiche", "10m/physical/ne_10m_geography_regions_polys", 0.03, 20000,
     ["NAME", "NAME_IT", "FEATURECLA", "LABELRANK"], ITALIA),
]

if __name__ == "__main__":
    tot = 0
    for nome, shp, tol, q, chiavi, box in LAVORI:
        feats, punti = [], []
        for d, gt, segs in le(shp):
            props = {k: d.get(k) for k in chiavi
                     if d.get(k) not in (None, "")}
            if gt in ("punto", "multipunto"):
                x, y = segs[0][0][0], segs[0][0][1]
                if box and not _dentro((x, y), box):
                    continue
                punti.append((props, x, y))
                continue
            if gt == "null":
                continue
            segs = taglia(segs, gt, box, tol)
            if segs:
                feats.append((props, segs))
        nv = sum(len(s) for _, ss in feats for s in ss)
        size = scrivi(f"{OUT}/{nome}.json", feats, punti, q)
        tot += size
        print(f"  {nome:<30} {len(feats):>5} geom  {len(punti):>4} punti  "
              f"{nv:>6} vertici  {size//1024:>5} kB")
    print(f"\nTOTALE {tot//1024} kB in {OUT}")