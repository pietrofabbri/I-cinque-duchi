#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controlla i colori cartografici: che siano in un file, che non mentano sulla
provenienza, e che nessuno sia rimasto nel codice.

Il problema che chiude e' l'I19 dell'audit: i colori delle carte stavano
**nel codice**, dove nessuno li leggeva. Sono dodici esadecimali scritti in
`verifica_mappe_disegno.py`, e due persone che colorano la stessa carta in due
modi diversi producono due carte diverse — che e' esattamente la ragione per
cui questo progetto ha una tavolozza dichiarata per le immagini e non ne aveva
una per le mappe.

Sette controlli, e tutti e sette guardano cose che si possono guardare senza
giudicare:

C1  ogni esadecimale dichiarato e' un esadecimale, e le chiavi sono uniche
C2  ogni voce che dice «viene dalla tavolozza» dice il vero: l'esadecimale e'
    identico a quello della chiave di `tavolozza.json`
C3  ogni voce dichiarata a mano porta **motivo** e **criterio**: un colore senza
    ragione non e' una dichiarazione, e' una scelta che nessuno puo' discutere
C4  **nessun colore vive solo nel codice**: ogni esadecimale che compare in
    `verifica_mappe_disegno.py` e' dichiarato in questo file
C5  ogni voce dichiarata e' o usata dal disegno, o elencata fra le
    `non_disegnate` con il perche'
C6  **la cartella `dati/mappe/` contiene solo file a delta**, come `mappe.md` e
    `AGENTS.md` dichiarano
C7  ogni file di mappa del pacchetto ha almeno un colore dichiarato che lo
    riguarda: una categoria senza colore non e' una categoria senza colore, e'
    un colore che si è dimenticato

C6 esiste perche' un file di copertura era finito in quella cartella per
errore e faceva saltare il lettore con un `IndexError` che non diceva niente:
il difetto era invisibile proprio perche' la cartella non aveva nessun controllo
sulla propria forma.

Uso:  python3 sorgenti/verifica_colori.py
"""
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLORI = os.path.join(RADICE, "dati", "fonti_visive", "colori_cartografici.json")
TAVOLOZZA = os.path.join(RADICE, "dati", "fonti_visive", "tavolozza.json")
MAPPE = os.path.join(RADICE, "dati", "mappe")
DISEGNO = os.path.join(RADICE, "sorgenti", "gis", "verifica_mappe_disegno.py")

HEX = re.compile(r"^[0-9A-Fa-f]{6}$")
ESADECIMALE = re.compile(r"#?([0-9A-Fa-f]{6})\b")

# Ogni file di mappa e la chiave di colore che lo riguarda. Non e' un elenco
# di cose che potrebbero servire: e' la copertura minima, e il controllo C7
# segnala sia un file che non c'e' sia un file senza colore che lo riguarda.
COPERTURA = {
    "mondo_110_terre.json": ["poligono_bordo"],
    "mondo_110_paesi.json": ["stato_riempimento", "stato_bordo"],
    "mondo_110_regioni.json": ["poligono_bordo"],
    "mondo_110_fiumi.json": ["fiume"],
    "mondo_110_laghi.json": ["lago"],
    "europa_50_terre.json": ["poligono_bordo"],
    "europa_50_paesi.json": ["stato_riempimento", "stato_bordo"],
    "europa_50_regioni.json": ["poligono_bordo"],
    "europa_50_fiumi.json": ["fiume"],
    "europa_50_laghi.json": ["lago"],
    "europa_50_citta.json": ["citta", "citta_bordo", "etichetta_mappa"],
    "europa_50_regioni_amministrative.json": ["unita_amministrativa",
                                             "unita_amministrativa_bordo"],
    "penisola_10_coste.json": ["costa"],
    "penisola_10_paesi.json": ["stato_riempimento_anno2", "stato_bordo_anno2"],
    "penisola_10_regioni.json": ["unita_amministrativa", "unita_amministrativa_bordo"],
    "penisola_10_regioni_fisiche.json": ["poligono_bordo"],
    "penisola_10_fiumi.json": ["fiume"],
    "penisola_10_laghi.json": ["lago"],
    "penisola_10_citta.json": ["citta", "citta_bordo", "etichetta_mappa"],
    "mondo_admin1.json": ["stato_riempimento", "stato_bordo"],
    "mondo_110_altitudine.json": ["cima", "cima_bordo"],
    "europa_50_altitudine.json": ["cima", "cima_bordo"],
    "penisola_10_altitudine.json": ["cima", "cima_bordo"],
}


def carica(percorso):
    with open(percorso, encoding="utf-8") as f:
        return json.load(f)


def verifica():
    problemi = []
    colori = carica(COLORI)
    tavolozza = {v["chiave"]: v["hex"].upper()
                 for v in carica(TAVOLOZZA)["voci"]}
    voci = colori["voci"]
    per_chiave = {}

    # C1 — gli esadecimali sono esadecimali, e le chiavi non si ripetono
    for v in voci:
        k = v.get("chiave")
        if k in per_chiave:
            problemi.append("C1: la chiave %r compare due volte nel file dei colori" % k)
        per_chiave[k] = v
        if not HEX.match(v.get("hex") or ""):
            problemi.append("C1: %s ha hex %r, che non è un esadecimale a sei cifre"
                            % (k, v.get("hex")))

    # C2 — chi dice «viene dalla tavolozza» dice il vero
    for v in voci:
        if v.get("origine") != "tavolozza":
            continue
        k = v.get("chiave_tavolozza")
        if k not in tavolozza:
            problemi.append("C2: %s dice di venire dalla tavolozza, ma la chiave %r "
                            "non c'è in tavolozza.json" % (v["chiave"], k))
        elif tavolozza[k].upper() != v["hex"].upper():
            problemi.append("C2: %s dichiara %s dalla tavolozza, ma la chiave %r vale %s "
                            "e non %s" % (v["chiave"], v["hex"], k, tavolozza[k],
                                          v["hex"]))
        elif v.get("origine") == "tavolozza" and not v.get("motivo"):
            problemi.append("C3: %s non dice perché usa quella voce della tavolozza"
                            % v["chiave"])

    # C3 — ogni colore dichiarato a mano porta motivo e criterio
    for v in voci:
        if v.get("origine") == "dichiarata":
            for campo in ("motivo", "criterio"):
                if not v.get(campo):
                    problemi.append("C3: %s è dichiarata a mano ma non dice %s: un "
                                    "colore senza ragione non è una dichiarazione"
                                    % (v["chiave"], campo))

    # C4 — nessun colore vive solo nel codice
    sorgente = open(DISEGNO, encoding="utf-8").read()
    # il docstring e i commenti parlano di `#rrggbb` e di `#f6fafc` come
    # esempi: cercare li conta come colori e produce un rumore di fondo.
    codice = "\n".join(l for l in sorgente.split("\n")
                       if not l.lstrip().startswith("#")
                       and '"""' not in l)
    nel_codice = {m.group(1).upper() for m in ESADECIMALE.finditer(sorgente)
                  if m.group(1).upper() != "RRGGBB"}
    dichiarati = {v["hex"].upper() for v in voci}
    per_eta = dichiarati | {"".join(chr(int(c, 16)) for c in v["hex"]) for v in voci}
    for colore in sorted(nel_codice):
        if colore in dichiarati or colore in per_eta:
            continue
        problemi.append("C4: il colore #%s è scritto in %s e non è dichiarato in "
                        "%s: è un colore che vive solo nel codice"
                        % (colore, os.path.basename(DISEGNO),
                           os.path.relpath(COLORI, RADICE)))

    # C5 — ogni voce è usata dal disegno, o dichiarata come non disegnata
    non_disegnate = {v["chiave"] for v in colori.get("non_disegnate", [])}
    for v in voci:
        k = v["chiave"]
        if k in non_disegnate:
            continue
        if '"%s"' % k not in sorgente:
            problemi.append("C5: %s è dichiarata ma nessuna pagina la usa, e non è "
                            "fra le `non_disegnate`: un colore che nessuno vede non "
                            "è una dichiarazione, è una promessa" % k)

    # C6 — la cartella delle mappe contiene solo file a delta
    #
    # Il file si legge TUTTO, e non i primi duecento caratteri: `q` e `f` sono
    # in testa, ma `p` sta in fondo, e in un file da 450 kB sta ben oltre il
    # duecentesimo carattere. La prima versione di questo controllo guardava
    # solo la testa e dichiarava non-a-delta tutti e diciannove i file delle
    # mappe: il controllo che esiste per segnalare un intruso nella cartella
    # segnalava la cartella intera, e il suo unico difetto era dichiarare
    # sbagliato tutto quello che c'era.
    for nome in sorted(os.listdir(MAPPE)):
        if not nome.endswith(".json"):
            continue
        with open(os.path.join(MAPPE, nome), encoding="utf-8") as f:
            testo = f.read()
        if '"q":' not in testo[:64] or '"f":[' not in testo[:64] or '"p":[' not in testo:
            problemi.append("C6: %s non è nel formato a delta, e `mappe.md` e "
                            "`AGENTS.md` dichiarano che tutto quello che c'è in "
                            "dati/mappe/ lo è: il lettore va in crash su un JSON "
                            "valido" % nome)

    # C7 — ogni file di mappa ha un colore che lo riguarda
    presenti = {n for n in os.listdir(MAPPE) if n.endswith(".json")}
    for nome in sorted(COPERTURA):
        if nome not in presenti:
            problemi.append("C7: la copertura dichiara %s, che non è in dati/mappe/"
                            % nome)
            continue
        for chiave in COPERTURA[nome]:
            if chiave not in per_chiave:
                problemi.append("C7: %s ha bisogno del colore %s, che non è "
                                "dichiarato" % (nome, chiave))
    for nome in sorted(presenti - set(COPERTURA)):
        problemi.append("C7: %s è in dati/mappe/ ma nessun colore lo riguarda: "
                        "aggiungilo alla copertura o dichiara perché non ne ha "
                        "bisogno" % nome)

    return colori, problemi


if __name__ == "__main__":
    colori, problemi = verifica()
    voci = colori["voci"]
    print("colori cartografici: %d dichiarati in %s"
          % (len(voci), os.path.relpath(COLORI, RADICE)))
    per_origine = {}
    for v in voci:
        per_origine[v["origine"]] = per_origine.get(v["origine"], 0) + 1
    for origine, n in sorted(per_origine.items()):
        print("  %-10s %d" % (origine, n))
    print("senza riempimento dichiarato: %d" % len(colori.get("senza_riempimento", [])))
    print("non dichiarati: %d" % len(colori.get("non_dichiarati", [])))
    print("problemi: %d" % len(problemi))
    for p in problemi:
        print("  " + p)
    if not problemi:
        print("nessun colore vive solo nel codice, e nessuna voce mente sulla "
              "sua provenienza")
    sys.exit(1 if problemi else 0)