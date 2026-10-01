"""Lettore del formato compatto a delta usato dalle mappe del progetto.

Formato (`*.json`, che non e' JSON valido: e' un formato proprio, come quello di
`gis/citta_centro.json`):

  {"q": <gradi per unita' intera>,
   "f": [ [{props}], [dx,dy;dx,dy;...], [dx,dy;...], [{props}], [anello], ... ],
   "p": [ [{props}, x, y], [{props}, x, y], ... ]}

Perche' non JSON valido: a 20 000 unita' per grado la quantizzazione e' di mezzo
metro e il delta dalla soglia precedente porta i numeri a poche cifre. Lo stesso
GeoJSON con coordinate decimali occupa cinque o dieci volte tanto.

`leggi()` restituisce sempre coordinate in gradi decimali: il motore non deve
sapere nulla della codifica.
"""
import json


def _gruppi(s):
    """Separa in elementi di primo livello, rispettando le parentesi quadre."""
    out, k, n = [], 0, len(s)
    while k < n:
        while k < n and s[k] in ", \t\r\n":
            k += 1
        if k >= n:
            break
        if s[k] != "[":
            k += 1
            continue
        prof = 0
        for i in range(k, n):
            if s[i] == "[":
                prof += 1
            elif s[i] == "]":
                prof -= 1
                if prof == 0:
                    out.append(s[k:i + 1])
                    k = i + 1
                    break
        else:
            raise ValueError("parentesi non chiuse")
    return out


def _split_top(s, sep=","):
    """Divide su un separatore che sta fuori da ogni parentesi graffa."""
    parti, buf, prof = [], [], 0
    for ch in s:
        if ch in "{[":
            prof += 1
        elif ch in "}]":
            prof -= 1
        if ch == sep and prof == 0:
            parti.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parti.append("".join(buf))
    return parti


def _corpo(t, i):
    """Dalla posizione di '[' (l'apertura dell'array) restituisce il contenuto
    dell'array, togliendo la parentesi che lo racchiude. Non si appoggia agli
    offset delle sezioni successive: si conta la profondita'."""
    k = t.index("[", i)
    prof = 0
    for j in range(k, len(t)):
        if t[j] == "[":
            prof += 1
        elif t[j] == "]":
            prof -= 1
            if prof == 0:
                return t[k + 1:j]
    raise ValueError("array non chiuso")


def _anello(s, q):
    """'dx,dy;dx,dy;...' -> [(lon, lat), ...]"""
    pts, x, y = [], 0, 0
    for seg in s.split(";"):
        if not seg:
            continue
        dx, dy = seg.split(",")
        x += int(dx)
        y += int(dy)
        pts.append((x / q, y / q))
    return pts


def leggi(path):
    """Ritorna (geometrie, punti); ogni geometria e' (props, [anello, ...])."""
    with open(path, encoding="utf-8") as f:
        t = f.read()
    q = float(t.split('"q":', 1)[1].split(",", 1)[0])

    # le due sezioni sono array: `i_f` e `i_p` puntano alla loro apertura "[",
    # quindi va tolta una parentesi per sezione, altrimenti l'intera sezione
    # viene letta come un unico gruppo e non si vede nulla.
    i_f = t.index('"f":[')
    i_p = t.index('"p":[')
    sez_f = _corpo(t, i_f)
    sez_p = _corpo(t, i_p)

    geom, props, anelli = [], None, []
    for g in _gruppi(sez_f):
        if g.startswith("[{"):                    # [{...}] = proprieta'
            if props is not None:
                geom.append((props, anelli))
                anelli = []
            props = json.loads(g)[0]
        elif props is not None:                    # ["dx,dy;..."] = un anello
            anelli.append(_anello(g[1:-1], q))
    if props is not None:
        geom.append((props, anelli))

    punti = []
    for g in _gruppi(sez_p):
        parti = _split_top(g[1:-1])
        punti.append((json.loads(parti[0]), float(parti[1]), float(parti[2])))
    return geom, punti