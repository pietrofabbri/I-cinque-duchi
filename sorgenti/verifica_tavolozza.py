"""Verifica la tavolozza del gioco: che i colori ci siano ancora, e che la
tavolozza sia coerente con se stessa.

`verifica_coerenza.py` guarda i documenti fra loro. Questo file guarda una cosa
diversa e piu' scomoda: **se i colori dichiarati ci sono ancora**. Una tavolozza
copiata a mano va bene finche' nessuno la tocca; il giorno in cui qualcuno
cambia un esadecimale su Wikidata, il file mente e nessuno se ne accorge. Qui si
va a leggere la fonte di ogni voce e si confronta.

I controlli sono cinque, e sono tutti sul file, non sulla fonte:

  A1  ogni voce ha un esadecimale di sei cifre
  A2  le chiavi sono uniche: due voci con lo stesso nome sono due colori che si
      contendono lo stesso nome nel motore
  A3  ogni voce da pigmento porta la sua fonte (Wikidata o infobox) e la sua
      catena, e la catena dice da dove arriva l'esadecimale
  A4  la fonte dichiara ancora quell'esadecimale  (il controllo che va in rete)
  A5  le voci dichiarate e di stato non si presentano come storiche: portano una
      nota che dice che cosa sono

Un sesto controllo, A6, e' quello che serve di piu' e non e' un controllo: il
confronto fra i colori di stato. Due colori di stato che si somigliano troppo
sono due colori che il motore non puo' distinguere, e il file non se ne accorge
guardando gli esadecimali uno per uno.

Uso:
    python3 sorgenti/verifica_tavolozza.py
    python3 sorgenti/verifica_tavolozza.py --offline   # salta A4
"""
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tavolozza_campioni as tc                        # noqa: E402

TAV = os.path.join(tc.RADICE, "dati", "fonti_visive", "tavolozza.json")
RE_HEX = re.compile(r"^[0-9A-F]{6}$")
# La soglia di differenza fra due colori di stato. Sotto, l'occhio non
# distingue e il gioco non puo' segnalare nulla: il difetto sarebbe silenzioso.
SOGLIA_STATO = 60.0


def distanza(a, b):
    """La distanza euclidea fra due colori, in 0-441 (massimo: nero e bianco).

    E' la distanza negli spazi RGB, che non e' la distanza che l'occhio
    percepisce: quella e' molto piu' complicata e molto meno riproducibile. Qui
    serve una soglia dichiarata e non un giudizio, e questa si sa spiegare in
    una riga.
    """
    return sum((int(a[i:i + 2], 16) - int(b[i:i + 2], 16)) ** 2
               for i in (0, 2, 4)) ** 0.5


def main():
    offline = "--offline" in sys.argv
    with open(TAV, encoding="utf-8") as f:
        doc = json.load(f)
    voci = doc["voci"]
    problemi = []

    # A1 e A2: la forma del file
    for v in voci:
        if not RE_HEX.match(v.get("hex") or ""):
            problemi.append("A1  %s: esadecimale '%s' non valido"
                           % (v["chiave"], v.get("hex")))
    chiavi = [v["chiave"] for v in voci]
    for k in sorted({c for c in chiavi if chiavi.count(c) > 1}):
        problemi.append("A2  chiave duplicata: %s" % k)

    # A3 e A5: ogni voce dichiara da dove viene
    for v in voci:
        if v["origine"] in ("wikidata_p465", "wikipedia_infobox"):
            if not v.get("catena"):
                problemi.append("A3  %s: voce da pigmento senza catena" % v["chiave"])
            if v["origine"] == "wikidata_p465" and not v.get("wikidata"):
                problemi.append("A3  %s: dice wikidata ma non porta l'oggetto"
                               % v["chiave"])
            if v["origine"] == "wikipedia_infobox" and not v.get("pagina"):
                problemi.append("A3  %s: dice infobox ma non porta la pagina"
                               % v["chiave"])
        else:
            if not (v.get("nota") or "").strip():
                problemi.append("A5  %s: voce '%s' senza nota che dica che "
                               "cosa e'" % (v["chiave"], v["origine"]))

    # A4: la fonte dichiara ancora quell'esadecimale
    a4 = 0
    if not offline:
        for v in voci:
            if v["origine"] == "wikidata_p465":
                colore, catena, _ = tc.colore_wikidata(v["wikidata"])
                a4 += 1
            elif v["origine"] == "wikipedia_infobox":
                colore, _ = tc.colore_infobox(v["pagina"])
                a4 += 1
            else:
                continue
            if colore != v["hex"]:
                problemi.append("A4  %s: il file dice %s, la fonte dice %s"
                               % (v["chiave"], v["hex"], colore or "niente"))
            if v["origine"] == "wikidata_p465" and catena != v["catena"]:
                problemi.append("A4  %s: la catena e' cambiata (%s invece di %s)"
                               % (v["chiave"], catena, v["catena"]))
            time.sleep(0.6)

    # A6: i colori di stato devono essere distinguibili fra loro
    stato = [v for v in voci if v["origine"] == "stato"]
    for i, a in enumerate(stato):
        for b in stato[i + 1:]:
            d = distanza(a["hex"], b["hex"])
            if d < SOGLIA_STATO:
                problemi.append(
                    "A6  %s e %s sono troppo vicini (%.0f, sotto %.0f): il "
                    "gioco non li distingue"
                    % (a["chiave"], b["chiave"], d, SOGLIA_STATO))

    # il riepilogo, che e' la parte che serve
    per_origine = {}
    for v in voci:
        per_origine[v["origine"]] = per_origine.get(v["origine"], 0) + 1
    print("tavolozza: %s" % os.path.relpath(TAV, tc.RADICE))
    print("  %d voci: %s" % (len(voci), ", ".join(
        "%d %s" % (n, o) for o, n in sorted(per_origine.items()))))
    print("  campioni guardati a vista: %d" % doc.get("campioni_guardati", -1))
    print("  pigmenti visitati senza esadecimale: %d"
          % len(doc.get("pigmenti_senza_colore_macchina", [])))
    if not offline:
        print("  fonti ricontrollate in rete: %d" % a4)
    else:
        print("  fonti ricontrollate in rete: 0 (--offline)")
    print("  coppie di stato verificate: %d" % (len(stato) * (len(stato) - 1) // 2))

    if problemi:
        print("\nPROBLEMI: %d" % len(problemi))
        for p in problemi:
            print("  " + p)
        return 1
    print("\nOK: nessun problema")
    return 0


if __name__ == "__main__":
    sys.exit(main())
