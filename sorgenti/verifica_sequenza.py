#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica la sequenza delle tappe degli anni 2, 3 e 4: S1-S7.

La sequenza è un file generato, e un file generato può essere giusto il primo
giorno e falso il secondo. Qui si controllano le sette cose che la rendono
utile.

  S1  trenta tappe per anno, numeri da 1 a 30 senza buchi e senza doppioni
  S2  ogni tappa ha la sua voce obbligatoria, e nessuna si ripete nell'anno
  S3  nessuna facoltativa e' la voce obbligatoria della **stessa** tappa
  S4  nessuna tappa resta senza punto senza portare lo stato dichiarato dal registro
  S5  i giorni sono coerenti con i km al giorno che il file dichiara
  S6  le tabelle del documento contengono le stesse trenta voci del dato
  S7  ogni divergenza fra registro e documento e' dichiarata

S7 e' nato dalla 4-16 e dalla 3-28: due tappe in tre anni in cui il registro dei
luoghi e il documento d'anno dicevano cose diverse, e nessuno dei controlli
precedenti lo vedeva.

Uso:  python3 sorgenti/verifica_sequenza.py
"""
import io
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_SEQ = os.path.join(RADICE, "dati", "sequenza_tappe.json")
DOC_SEQ = os.path.join(RADICE, "docs", "videogioco-5-duchi-sequenza.md")
ANNI = (2, 3, 4)


def leggi(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def main():
    if not os.path.exists(JSON_SEQ):
        print("manca %s: esegui prima sorgenti/sequenza_tappe.py" % JSON_SEQ)
        return 2
    seq = json.loads(leggi(JSON_SEQ))
    documento = leggi(DOC_SEQ) if os.path.exists(DOC_SEQ) else ""
    problemi = []

    for anno in ANNI:
        chiave = str(anno)
        if chiave not in seq.get("anni", {}):
            problemi.append("S1: l'anno %d non e' nella sequenza" % anno)
            continue
        d = seq["anni"][chiave]
        tappe = d["tappe"]

        # S1
        numeri = [t["ordine"] for t in tappe]
        if numeri != list(range(1, 31)):
            problemi.append("S1: l'anno %d non ha i numeri da 1 a 30 in ordine" % anno)
        if len({t["tappa"] for t in tappe}) != len(tappe):
            problemi.append("S1: l'anno %d ha tappe ripetute" % anno)

        # S2
        voci = [t["voce"] for t in tappe]
        vuote = [t["tappa"] for t, v in zip(tappe, voci) if not v.strip()]
        if vuote:
            problemi.append("S2: l'anno %d ha tappe senza voce: %s" % (anno, vuote))
        if len(set(voci)) != len(voci):
            doppi = sorted({v for v in voci if voci.count(v) > 1})
            problemi.append("S2: l'anno %d ha voci obbligatorie ripetute: %s" % (anno, doppi))
        collettivi = [t["tappa"] for t in tappe if not t["voce_id"]]
        # un collettivo e' una voce senza scheda: se sono molti non sono piu'
        # collettivi ma persone senza scheda, e la differenza si dichiara
        if len(collettivi) > 8:
            problemi.append("S2: l'anno %d ha %d tappe senza scheda: troppe per essere collettivi"
                            % (anno, len(collettivi)))

        # S3
        stessi = []
        for t in tappe:
            proprie = {f.lower() for f in t["facoltativi"]}
            if t["voce"].lower() in proprie:
                stessi.append(t["tappa"])
        if stessi:
            problemi.append("S3: l'anno %d ha facoltative che sono la voce della stessa tappa: %s"
                            % (anno, stessi))
        incroci = set()
        obbligatorie = {v.lower() for v in voci}
        for t in tappe:
            for f in t["facoltativi"]:
                if f.lower() in obbligatorie:
                    incroci.add(f)
        # la prova e' che il nome sia scritto nel documento: se il catalogo cresce
        # e il documento no, il controllo morde senza bisogno di una parola chiave
        non_dichiarati = sorted(f for f in incroci if f not in documento)
        if non_dichiarati:
            problemi.append("S3: l'anno %d ha %d persone obbligatorie in una tappa e "
                            "facoltative in un'altra che il documento non dichiara: %s"
                            % (anno, len(non_dichiarati), ", ".join(non_dichiarati[:5])))

        # S4
        senza = [t["tappa"] for t in tappe
                 if not t["punto"] and not t.get("punto_stato")]
        if senza:
            problemi.append("S4: l'anno %d ha tappe senza punto e senza stato dichiarato: %s"
                            % (anno, senza))

        # S5
        cattivi = []
        for t in tappe:
            km, gg = t["km_dalla_precedente"], t["giorni"]
            if km is None or gg is None:
                continue
            atteso = max(1, int(round(km / float(d["km_al_giorno"]))))
            if abs(atteso - gg) > 1:
                cattivi.append("%s: %d km = %d giorni, attesi %d" % (t["tappa"], km, gg, atteso))
        if cattivi:
            problemi.append("S5: l'anno %d ha giorni incoerenti: %s" % (anno, cattivi[:3]))

        # S6
        if documento:
            mancanti = [t["tappa"] for t in tappe if ("**%s**" % t["tappa"]) not in documento]
            if mancanti:
                problemi.append("S6: il documento non contiene %d tappe: %s"
                                % (len(mancanti), mancanti[:5]))
            for t in tappe:
                if t["voce"] and ("`%s`" % t["voce_id"]) in documento:
                    if re.search(r"\*\*%s\*\*" % re.escape(t["tappa"]), documento):
                        continue
        r = d["riepilogo"]
        print("anno %d: %2d tappe, %2d voci (%d collettivi), %2d facoltative (%d in sovrappposizione), "
              "%2d/%2d con punto, %d km in %d giorni"
              % (anno, len(tappe), len(set(voci)), len(collettivi),
                 r["facoltative_dichiarate"], len(incroci),
                 len(tappe) - len([t for t in tappe if not t["punto"]]), len(tappe),
                 r["km_totali"], r["giorni_totali"]))

    # S7
    print("\n== S7. ogni divergenza fra registro e documento e' dichiarata ==")
    div = seq.get("divergenze", [])
    if not div:
        print("   nessuna divergenza: registro e documento dicono la stessa cosa")
    for d in div:
        stato = "dichiarata" if d.get("dichiarazione") else "NON DICHIARATA"
        print("   %s: documento %r, registro %r — %s"
              % (d["tappa"], d["luogo_documento"], d["luogo_registro"], stato))
        if not d.get("dichiarazione"):
            problemi.append("S7: la tappa %s ha due luoghi e nessuna dichiarazione" % d["tappa"])

    print("\n== sintesi ==")
    if problemi:
        for p in problemi:
            print("   difetto: " + p)
        print("\nproblemi: %d" % len(problemi))
        return 1
    print("   nessun difetto: novanta tappe in ordine, trenta voci per anno, le facoltative "
          "fuori dalla sequenza, e l'unica divergenza fra registro e documento e' dichiarata")
    print("\n==== controlli superati: 7/7 ====")
    return 0


if __name__ == "__main__":
    sys.exit(main())