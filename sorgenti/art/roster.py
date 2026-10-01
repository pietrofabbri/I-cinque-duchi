"""Costruisce l'elenco completo dei personaggi del gioco: 213 voci.

- anno 1: dai dati, `dati/videogioco-5-duchi-anno1-personaggi.json` (93 voci)
- anni 2-5: dai documenti di progetto, dalle intestazioni `### Qxx · Nome` (30 per anno)

Per ogni voce tiene: codice, nome pulito (senza la parte fra parentesi o dopo
il trattino lungo), anno di gioco, categorie, tipo, e se la persona e' viva.
"""
import json
import os
import re

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS = os.path.join(RADICE, "docs")
DATI = os.path.join(RADICE, "dati")


def pulisci(nome):
    """'Ötzi — uomo dell'età del Rame' -> 'Ötzi'."""
    nome = re.split(r"\s+[—–]\s+", nome)[0]
    nome = re.sub(r"\s*\*.*?\*", "", nome)
    nome = re.sub(r"\s*\(.*?\)", "", nome)
    nome = re.sub(r"\s*\[.*?\]", "", nome)
    return nome.strip(" ,")


def anno1():
    with open(os.path.join(DATI, "videogioco-5-duchi-anno1-personaggi.json"),
              encoding="utf-8") as f:
        d = json.load(f)
    out = []
    for p in d["personaggi"]:
        out.append({
            "codice": p["id"],
            "nome": p["nome"],
            "anno": 1,
            "categorie": p.get("categorie") or [],
            "tipo": p.get("tipo") or "persona",
            "periodo": p.get("periodo") or "",
            "legame_luogo": p.get("legame_luogo") or "",
            "certezza": p.get("certezza") or [],
        })
    return out


def anni2345():
    file = {2: "videogioco-5-duchi-anno2-penisola.md",
            3: "videogioco-5-duchi-anno3-europa.md",
            4: "videogioco-5-duchi-anno4-mondo.md",
            5: "videogioco-5-duchi-anno5-mondo.md"}
    out = []
    for anno, nome in file.items():
        percorso = os.path.join(DOCS, nome)
        if not os.path.exists(percorso):
            continue
        with open(percorso, encoding="utf-8") as f:
            righe = f.read().split("\n")
        for i, r in enumerate(righe):
            m = re.match(r"^###\s+(Q\d+)\s+·\s+(.*)$", r)
            if not m:
                continue
            codice, grezzo = m.group(1), m.group(2)
            testo = "\n".join(righe[i:i + 8])
            per = re.search(r"\*\*Periodo:\*\*\s*([^.*]*)", testo)
            periodo = per.group(1).strip() if per else ""
            vivo = bool(re.search(r"(19\d\d|20\d\d)\s*[—–-]\s*(\.|in formazione|$)", periodo)) \
                or "in formazione" in testo[:600]
            out.append({
                "codice": codice,
                "nome": pulisci(grezzo),
                "anno": anno,
                "categorie": [],
                "tipo": "collettivo" if "collettivo" in testo[:600].lower() else "persona",
                "periodo": periodo,
                "legame_luogo": "",
                "certezza": [],
                "vivo": vivo,
            })
    return out


if __name__ == "__main__":
    roster = anno1() + anni2345()
    per_anno = {}
    for r in roster:
        per_anno[r["anno"]] = per_anno.get(r["anno"], 0) + 1
    vivi = [r for r in roster if r.get("vivo")]
    collettivi = [r for r in roster if r["tipo"] == "collettivo"]
    print("totale:", len(roster))
    print("per anno:", dict(sorted(per_anno.items())))
    print("viventi:", len(vivi), [r["nome"] for r in vivi])
    print("collettivi:", len(collettivi), [r["nome"] for r in collettivi][:12])
    with open(os.path.join(RADICE, "sorgenti", "art", "roster.json"), "w",
              encoding="utf-8") as f:
        json.dump(roster, f, ensure_ascii=False, indent=1)
    print("scritto in sorgenti/art/roster.json")