"""Impacchetta dati e grafica della zona 1 in un file JS (zona1_dati.js) da incorporare nel prototipo.
- Z1DATA: edifici (sagoma, altezza LIDAR, falde del tetto assegnate), zona, pedonali, tappe vicine.
- Z1ART: immagini PNG in data URI (sprite, facciata, ritratti).
"""
import json, base64, math

d = json.load(open('gis/zona1_mappa.json'))
r1 = lambda v: round(v, 1)

def pip(pt, ring):
    x, y = pt; ins = False
    for i in range(len(ring)):
        (x1, y1), (x2, y2) = ring[i], ring[(i + 1) % len(ring)]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1: ins = not ins
    return ins

B = d['edifici']
for b in B:
    b['f'] = []
for f in d['falde']:
    xs = [p[0] for p in f['p']]; ys = [p[1] for p in f['p']]
    c = (sum(xs) / len(xs), sum(ys) / len(ys))
    for b in B:
        if pip(c, b['p']) and not any(pip(c, h) for h in b['holes']):
            b['f'].append([[r1(v) for v in f['o']], f['s'], [[r1(u), r1(v)] for u, v in f['p']]])
            break

out = {
    'r': d['rettangolo'], 't1': d['tappa1'], 'tv': d['tappe_vicine'],
    'zona': [[r1(u), r1(v)] for u, v in d['zona']],
    'ped': [[[r1(u), r1(v)] for u, v in p['p']] for p in d['pedonali']],
    'ed': [{'id': b['id'], 'k': b['k'], 'h': b['h'], 'hs': b['hs'],
            'p': [[r1(u), r1(v)] for u, v in b['p']],
            'ho': [[[r1(u), r1(v)] for u, v in h] for h in b['holes']],
            'f': b['f']} for b in B],
}

def uri(path):
    return 'data:image/png;base64,' + base64.b64encode(open(path, 'rb').read()).decode()

A = 'art/out/'
art = {k: uri(A + v) for k, v in {
    'borso': 'borso.png', 'maurelio': 'maurelio.png', 'giorgio': 'giorgio.png', 'lapide': 'lapide.png',
    'facciata': 'facciata.png', 'statua_borso': 'statua_borso.png', 'statua_niccolo': 'statua_niccolo.png',
    'cartello': 'cartello.png', 'r_borso': 'ritratto_borso.png', 'r_maurelio': 'ritratto_maurelio.png',
    'r_giorgio': 'ritratto_giorgio.png'}.items()}

js = ('/* zona1_dati.js — generato da gis/zona1_pack.py. Dati: Comune di Ferrara, open data (CC BY 4.0). */\n'
      'const Z1DATA=' + json.dumps(out, separators=(',', ':')) + ';\n'
      'const Z1ART=' + json.dumps(art, separators=(',', ':')) + ';\n')
open('zona1_dati.js', 'w').write(js)
print('zona1_dati.js', len(js), 'byte; falde assegnate', sum(len(b['f']) for b in out['ed']))
