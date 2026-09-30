import json
from civici import to_wgs84
d=json.load(open("civici_cache.json")); rows=d["rows"]; pts=d["pts"]
IDX={}
for r,p in zip(rows,pts):
    if p: IDX.setdefault(r["VIA_NOME_U"],[]).append((int(float(r["NUMERO"] or 0)),r["ESPONENTE"].replace('\x00','').strip(),p))
def g(via,num,esp=""):
    for n,e,p in IDX.get(via,[]):
        if n==num and e==esp:
            la,lo=to_wgs84(*p); return round(la,6),round(lo,6)
    return None
def allof(via): return sorted((n,e,tuple(round(x,6) for x in to_wgs84(*p))) for n,e,p in IDX.get(via,[]))
