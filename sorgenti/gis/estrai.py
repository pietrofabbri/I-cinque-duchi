"""Ricompone i dati passati a pezzi dal browser integrato (risultati salvati dal tool)."""
import json,sys
D='/root/.claude/projects/-home-claude/012f2e0f-dd6f-5f88-a845-4cfa173f7777/tool-results/'
def leggi(ids):
    parts={}
    for f in ids:
        t=json.load(open(D+f'mcp-remote-devices-Claude_Browser__javascript_tool-{f}.txt'))[0]['text']
        s,_=json.JSONDecoder().raw_decode(t)
        k,v=s.split('|',1); parts[k]=v
    return ''.join(parts[k] for k in sorted(parts,key=lambda k:int(k.replace('CHUNK',''))))
