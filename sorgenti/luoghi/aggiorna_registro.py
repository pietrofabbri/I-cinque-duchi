"""Rigenera `dati/luoghi_gioco.json` dagli estratti e dalle coordinate, senza
perdere quello che c'era.

**Perche' questo script esiste.** `classifica.py` rifacendo il registro da capo
 cancella quattro cose che nessuno puo' ricreare con un comando: il terreno
misurato su SRTM (54 record), il campo `controllo`, i `dettagli` compilati a
mano e il blocco `tappe` con i trenta binomi pin/stanza del quinto anno. Il 3
ottobre la correzione della tappa 4-16 e' stata scritta a mano nel registro
perche' il generatore, se l'avesse riscritto, avrebbe cancellato tutto il resto:
la correzione esiste ma non e' venuta da nessuna rigenerazione, e quindi
nessuno poteva dire se il generatore l'avrebbe riprodotta.

La prova e' stata lanciata: il generatore, cosi' com'era, ricreava la 4-16 con
il **vecchio** valore («Tunisi e Il Cairo») perche' l'estratto intermedio
`dati/luoghi_estratti.json` era rimasto indietro rispetto ai documenti. Due
buoni in uno: il file intermedio era vecchio, e nessuno lo aveva visto.

**Il metodo e' l'unione, non la sovrascrittura.** I campi che vengono dai
documenti (luogo, tappe, anni, pin, tipo, coordinate, stato) si aggiornano
sempre; i campi che si compilano a mano (terreno, controllo, dettagli) si
portano dietro per nome di luogo e si segnalano quando il nome non c'e' piu'.
Un campo che sparisce non viene ricreato: viene detto, e la riga resta in
`persi`.

Uso:
    python3 sorgenti/luoghi/aggiorna_registro.py            # scrive
    python3 sorgenti/luoghi/aggiorna_registro.py --prova    # non scrive
"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classifica import (applica_correzione, che_tipo, le_correzioni,  # noqa: E402
                        stato_di)

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ESTRATTI = os.path.join(RADICE, "dati", "luoghi_estratti.json")
GEO = os.path.join(RADICE, "dati", "luoghi_geo.jsonl")
CORREZIONI = os.path.join(RADICE, "dati", "luoghi_correzioni.json")
REGISTRO = os.path.join(RADICE, "dati", "luoghi_gioco.json")

# I campi che vengono dai documenti e dalle coordinate: si riscrivono sempre.
DA_DOCUMENTI = ("luogo", "tipo", "tappe", "anni", "pin", "lat", "lon",
                "articolo", "fonte_coord", "coord_stato", "perche")
# I campi che si compilano a mano: si portano dietro per nome di luogo, e se
# il nome non c'e' piu' restano in `persi` invece di sparire.
DA_MANO = ("dettagli", "terreno", "controllo")


def costruisci(verbale):
    estratti = json.load(open(ESTRATTI, encoding="utf-8"))
    geo = {}
    for riga in open(GEO, encoding="utf-8"):
        riga = riga.strip()
        if not riga:
            continue
        d = json.loads(riga)
        if d.get("stato") == "da_rifare":
            continue
        geo[d["luogo"]] = d

    vecchio = {}
    blocco_tappe = []
    if os.path.exists(REGISTRO):
        precedente = json.load(open(REGISTRO, encoding="utf-8"))
        for l in precedente.get("luoghi", []):
            vecchio[l["luogo"]] = l
        blocco_tappe = precedente.get("tappe", [])

    tappe = collections.defaultdict(list)
    anni = collections.defaultdict(set)
    for t in estratti["tappe"]:
        tappe[t["luogo"]].append(t["tappa"])
        anni[t["luogo"]].add(t["anno"])

    corretti = le_correzioni()
    applicate = []
    record, per_tipo, per_stato = [], collections.Counter(), collections.Counter()
    cambi, portati, persi = [], 0, []
    for nome in sorted(tappe):
        tipo, perche = che_tipo(nome)
        g = dict(geo.get(nome, {}))
        presente = nome in geo
        stato = stato_di(nome, tipo, g, presente)
        c = corretti.get(nome)
        if c:
            if applica_correzione(g, c):
                applicate.append(nome)
                stato = "verificata"
                perche = (perche + " " if perche else "") + (
                    "Correzione del %s: %s" % (c["data"], c["difetto"].rstrip(".")))
        r = {
            "luogo": nome,
            "tipo": tipo,
            "tappe": sorted(tappe[nome]),
            "anni": sorted(anni[nome]),
            "pin": len(tappe[nome]),
            "lat": g.get("lat"),
            "lon": g.get("lon"),
            "articolo": g.get("titolo_risolto"),
            "fonte_coord": ("wikipedia:" + g["wiki"]) if g.get("titolo_risolto") else None,
            "coord_stato": stato,
            "perche": perche,
        }
        if c and nome in applicate:
            r["correzione"] = {
                "dall_articolo": c["dall_articolo"],
                "correzione": c["correzione"],
                "fonte": c["fonte"],
                "controllo": c["controllo"],
            }
        # i campi a mano: nel registro vecchio se ci sono, nell'ordine dichiarato
        prec = vecchio.get(nome, {})
        for campo in DA_MANO:
            if campo in prec:
                r[campo] = prec[campo]
                portati += 1
        if prec:
            for campo in DA_DOCUMENTI:
                if prec.get(campo) != r[campo] and verbale:
                    cambi.append("  %-34s %s: %r -> %r"
                                 % (nome, campo, prec.get(campo), r[campo]))
        else:
            persi.append(nome)
        per_tipo[tipo] += 1
        per_stato[stato] += 1
        record.append(r)

    # i nomi che il registro aveva e l'estratto non ha piu': si dicono, non si
    # cancellano in silenzio. Uno di questi fu la 4-16 con il vecchio valore.
    spariti = sorted(set(vecchio) - set(tappe))
    return {"luoghi": record, "tappe": blocco_tappe}, cambi, persi, spariti, \
        per_tipo, per_stato, portati, applicate


def main():
    prova = "--prova" in sys.argv
    verbale = True
    registro, cambi, persi, spariti, per_tipo, per_stato, portati, applicate = \
        costruisci(verbale)

    print("luoghi: %d" % len(registro["luoghi"]))
    print("correzioni applicate: %d %s" % (len(applicate),
                                            ", ".join(applicate) or "(nessuna)"))
    print("blocchi `tappe` conservati: %d" % len(registro["tappe"]))
    print("campi portati dal registro precedente: %d" % portati)
    print("\nper tipo:")
    for t, n in per_tipo.most_common():
        print("  %-14s %3d" % (t, n))
    print("\nper stato della coordinata:")
    for s, n in per_stato.most_common():
        print("  %-30s %3d" % (s, n))
    if cambi:
        print("\ncambi (dal registro precedente):")
        for c in cambi:
            print(c)
    if persi:
        print("\nnuovi, senza campi a mano: %d" % len(persi))
    if spariti:
        print("\nATTENZIONE: nomi nel registro precedente e non piu' nell'estratto:")
        for n in spariti:
            print("  %s" % n)

    if prova:
        print("\n--prova: non scrivo nulla")
        return
    with open(REGISTRO, "w", encoding="utf-8") as f:
        json.dump(registro, f, ensure_ascii=False, indent=1)
    print("\nscritto %s" % REGISTRO)


if __name__ == "__main__":
    main()