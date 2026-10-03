#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controlla i file delle cime: che siano quello che dichiarano di essere.

`altitudine.py` produce tre file di punti. Il pericolo di questo tipo di dato
e' che sembra inutile pero' e' falso: un numero senza contesto e' un numero di
cui non si puo' fidare, e su una mappa un punto alla quota sbagliata e' una
montagna che non esiste.

Sette controlli, tutti su cose verificabili:

D1  ogni punto cade dentro il riquadro che il suo file dichiara
D2  ogni punto ha un nome e una quota intera
D3  la quota e' in un intervallo dichiarato: sotto il livello del mare esiste
    (la depressione di Turfan e' a -154 m) e sopra i novemila non
D4  il numero di punti di ogni file e' quello che il manifest dichiara
D5  il massimo del file del mondo e' l'Everest a 8848 m, e il file contiene almeno
    una quota **negativa**: se un domani i due estremi spariscono, non e' che il
    mondo si e' accorciato, e' che il file e' stato tagliato male
D6  nessun punto e' duplicato dentro un file
D7  se un punto compare in due file, la sua quota e' la stessa: i tre file sono
    selezioni diverse della stessa fonte, non tre versioni dello stesso elenco

D5 e D7 sono i due che valgono. D5 perche' l'altitudine e' l'unico dato di
questi file che si puo' controllare contro un fatto che tutti conoscono, e D7
perche' il difetto che i tre file hanno davvero — non essere annidati — e' un
difetto che nessuno vedrebbe finche' un punto non torna.

Uso:  python3 sorgenti/gis/verifica_altitudine.py
"""
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mappe_lettore import leggi

MAPPE = os.path.join(RADICE, "dati", "mappe")
MANIFEST = os.path.join(RADICE, "dati", "altitudine_manifest.json")

# Gli stessi riquadri di `altitudine.py`, dichiarati qui per poterli controllare
# invece di rileggerli: un controllo che prende il valore che deve verificare
# verifica che il valore è conforme a se stesso.
RIQUADRI = {
    "mondo_110_altitudine": [-180.0, -90.0, 180.0, 90.0],
    "europa_50_altitudine": [-25.0, 33.0, 46.0, 73.0],
    "penisola_10_altitudine": [5.0, 34.0, 20.0, 49.5],
}
QUOTA_MIN, QUOTA_MAX = -500, 9000
EVEREST = ("Everest", 8848)


def carica(nome):
    """(punti, geometrie vuote): i file di cime sono tutti sezione `p`."""
    _, punti = leggi(os.path.join(MAPPE, nome + ".json"))
    return punti


def verifica():
    problemi = []
    with open(MANIFEST, encoding="utf-8") as f:
        manifest = json.load(f)
    dichiarati = {v["nome"]: v for v in manifest["file"]}

    punti_per_file = {}
    for nome, box in sorted(RIQUADRI.items()):
        if nome not in dichiarati:
            problemi.append("D4: %s non è fra i file del manifest" % nome)
            continue
        punti = carica(nome)
        punti_per_file[nome] = punti

        # D1 — il punto cade nel riquadro che il file dichiara
        for props, x, y in punti:
            if not (box[0] <= x <= box[2] and box[1] <= y <= box[3]):
                nome_p = props.get("name_it") or props.get("name") or "?"
                problemi.append("D1: %s in %s è a (%.3f, %.3f), fuori dal riquadro "
                                "che il file dichiara" % (nome_p, nome, x, y))

        # D2 — nome e quota
        for props, x, y in punti:
            nome_p = props.get("name_it") or props.get("name")
            if not nome_p:
                problemi.append("D2: un punto di %s non ha né name_it né name: "
                                "una cima senza nome non è una cima che il gioco "
                                "può citare" % nome)
            q = props.get("elevation")
            if not isinstance(q, int) or isinstance(q, bool):
                problemi.append("D2: %s ha elevation %r, che non è un intero"
                                % (nome_p, q))

        # D3 — la quota è in un intervallo dichiarato
        for props, x, y in punti:
            q = props.get("elevation")
            if isinstance(q, int) and not (QUOTA_MIN <= q <= QUOTA_MAX):
                dove = props.get("name_it") or props.get("name")
                problemi.append("D3: %s è a %d m, fuori dall'intervallo dichiarato "
                                "[%d, %d]: o è un errore di lettura, o è un punto "
                                "che non è una cima" % (dove, q, QUOTA_MIN, QUOTA_MAX))

        # D4 — il conto del file è quello del manifest
        attesi = dichiarati[nome]["punti_nel_file"]
        if len(punti) != attesi:
            problemi.append("D4: %s ha %d punti e il manifest ne dichiara %d"
                            % (nome, len(punti), attesi))

    # D5 — gli estremi conosciuti, e le quote negative
    mondo = punti_per_file.get("mondo_110_altitudine", [])
    if mondo:
        alti = [p for p, _, _ in mondo if isinstance(p.get("elevation"), int)]
        massimo = max(alti, key=lambda p: p["elevation"])
        nome_max = massimo.get("name_it") or massimo.get("name")
        if (nome_max, massimo["elevation"]) != EVEREST:
            problemi.append("D5: la cima più alta del file del mondo è %s a %d m, "
                            "e non %s a %d m" % (nome_max, massimo["elevation"],
                                                 EVEREST[0], EVEREST[1]))
        negativi = [(p.get("name_it") or p.get("name"), p["elevation"])
                    for p, _, _ in mondo if isinstance(p.get("elevation"), int)
                    and p["elevation"] < 0]
        if not negativi:
            problemi.append("D5: il file del mondo non ha nessuna quota negativa: la "
                            "Valle della Morte e la depressione di Turfan sono sotto "
                            "il livello del mare, e senza di loro il file dice che il "
                            "pianeta non scende mai sotto zero")

    # D6 — nessun duplicato dentro un file
    for nome, punti in sorted(punti_per_file.items()):
        visti = {}
        for props, x, y in punti:
            k = (round(x, 4), round(y, 4))
            if k in visti:
                problemi.append("D6: in %s il punto (%.4f, %.4f) compare due volte (%s "
                                "e %s)" % (nome, x, y,
                                           visti[k],
                                           props.get("name_it") or props.get("name")))
            visti[k] = props.get("name_it") or props.get("name")

    # D7 — la stessa cima ha la stessa quota in tutti i file in cui compare
    quote = {}
    for nome, punti in punti_per_file.items():
        for props, x, y in punti:
            k = (round(x, 4), round(y, 4))
            if k in quote and quote[k] != props.get("elevation"):
                problemi.append("D7: la cima a (%.4f, %.4f) vale %d m in un file e "
                                "%s m in un altro: i tre file presi dalla stessa "
                                "fonte non possono discordare sulla quota"
                                % (x, y, quote[k], props.get("elevation")))
            quote.setdefault(k, props.get("elevation"))

    return manifest, punti_per_file, problemi


if __name__ == "__main__":
    manifest, punti_per_file, problemi = verifica()
    for nome in sorted(punti_per_file):
        punti = punti_per_file[nome]
        quote = [p.get("elevation") for p, _, _ in punti
                 if isinstance(p.get("elevation"), int)]
        print("%-26s %4d cime, da %s a %d m"
              % (nome, len(punti), min(quote) if quote else "-",
                 max(quote) if quote else 0))
    print("problemi: %d" % len(problemi))
    for p in problemi:
        print("  " + p)
    if not problemi:
        print("le tre scale non sono annidate, ed è dichiarato: sono selezioni "
              "diverse della stessa fonte globale")
    sys.exit(1 if problemi else 0)