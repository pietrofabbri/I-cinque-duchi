#!/usr/bin/env python3
"""Validatore ed esportatore della mappa dell'informatica.
Uso:  python3 valida-mappa.py mappa-informatica-?.md [--esporta]
Controlli: ID duplicati, prerequisiti inesistenti, riferimenti "sblocca" inesistenti,
cicli, radici, archi verso aree non dettagliate, inversioni di livello
(nodo con livello minimo inferiore al livello minimo di un suo prerequisito).
Con --esporta scrive grafo-informatica.json e grafo-informatica-archi.csv / -nodi.csv.
Formato riga: - **ID** Titolo · [livello] · ⟵ prerequisiti · ⟶ sblocca
Un riferimento a un nodo intermedio (es. A5.3) vale come "tutti i suoi figli"."""
import re, sys, json, csv
files = [f for f in sys.argv[1:] if not f.startswith('--')]
export = '--esporta' in sys.argv
ID = r'\b([A-W]\d+(?:\.\d+)*)'
nodes, dup = {}, []
for f in files:
    for line in open(f, encoding='utf-8'):
        m = re.match(r'- \*\*([A-W][\d.]+)\*\* (.*)', line)
        if not m: continue
        nid, rest = m.group(1), m.group(2)
        if nid in nodes: dup.append(nid)
        parts = [p.strip() for p in rest.split(' · ')]
        title = parts[0]
        lev = re.search(r'\[(\d)(?:–(\d))?\]', rest)
        lmin, lmax = (int(lev.group(1)), int(lev.group(2) or lev.group(1))) if lev else (None, None)
        pre = re.search(r'⟵ ([^·]*)', rest); out = re.search(r'⟶ ([^·]*)', rest)
        nodes[nid] = dict(id=nid, area=nid[0], titolo=title, liv_min=lmin, liv_max=lmax,
                          prereq=re.findall(ID, pre.group(1)) if pre else [],
                          sblocca=re.findall(ID, out.group(1)) if out else [], file=f)
areas = {n[0] for n in nodes}
def expand(p): return [p] if p in nodes else [k for k in nodes if k.startswith(p + '.')]
missing = [(n, p) for n, d in nodes.items() for p in d['prereq'] if p[0] in areas and not expand(p)]
bad_out = [(n, p) for n, d in nodes.items() for p in d['sblocca'] if p[0] in areas and not expand(p)]
external = sorted({(n, p) for n, d in nodes.items() for p in d['prereq'] if p[0] not in areas})
g = {n: sorted({q for p in d['prereq'] if p[0] in areas for q in expand(p)}) for n, d in nodes.items()}
sys.setrecursionlimit(100000); state, cycles, depth = {}, [], {}
def dfs(u, path):
    state[u] = 1; best = 0
    for v in g[u]:
        if state.get(v) == 1: cycles.append(path + [u, v]); continue
        if not state.get(v): dfs(v, path + [u])
        best = max(best, depth.get(v, 0) + 1)
    depth[u] = best; state[u] = 2
for n in g:
    if not state.get(n): dfs(n, [])
inv = [(n, q) for n in g for q in g[n] if nodes[n]['liv_min'] and nodes[q]['liv_min'] and nodes[n]['liv_min'] < nodes[q]['liv_min']]
print(f"File: {len(files)}  Nodi: {len(nodes)}  Archi di prerequisito (espansi): {sum(len(v) for v in g.values())}")
print(f"Duplicati: {dup or 'nessuno'}")
print(f"Prerequisiti inesistenti: {missing or 'nessuno'}")
print(f"Riferimenti 'sblocca' inesistenti: {bad_out or 'nessuno'}")
print(f"Cicli: {cycles or 'nessuno'}")
print(f"Radici ({sum(1 for d in nodes.values() if not d['prereq'])}):", [n for n, d in nodes.items() if not d['prereq']])
print(f"Archi verso aree non dettagliate ({len(external)}):", external)
print(f"Catena di prerequisiti più lunga: {max(depth.values())} passi")
print(f"Inversioni di livello (nodo più 'basso' di un suo prerequisito): {len(inv)}")
for a in sorted(areas):
    k = [n for n in nodes if n[0] == a]
    print(f"  Area {a}: {len(k)} nodi")
if export:
    for n in nodes: nodes[n]['prereq_espansi'] = g[n]; nodes[n]['profondita'] = depth[n]
    json.dump({'versione': '1.0', 'nodi': list(nodes.values())}, open('grafo-informatica.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open('grafo-informatica-nodi.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh); w.writerow(['id', 'area', 'titolo', 'liv_min', 'liv_max', 'profondita', 'prerequisiti_diretti'])
        for d in nodes.values(): w.writerow([d['id'], d['area'], d['titolo'], d['liv_min'], d['liv_max'], d['profondita'], ' '.join(d['prereq'])])
    with open('grafo-informatica-archi.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh); w.writerow(['da_prerequisito', 'a_nodo'])
        for n in g:
            for q in g[n]: w.writerow([q, n])
    print("Esportati: grafo-informatica.json, grafo-informatica-nodi.csv, grafo-informatica-archi.csv")
if inv and '--dettagli' in sys.argv:
    for n, q in inv: print(f"  {n} [{nodes[n]['liv_min']}] ⟵ {q} [{nodes[q]['liv_min']}]")
