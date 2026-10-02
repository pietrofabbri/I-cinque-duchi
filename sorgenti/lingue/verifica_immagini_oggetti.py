#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica le immagini degli oggetti di interazione.

Fa sei controlli sui dati di `dati/lingue/immagini_oggetti.json`, che sono
**proposte** e non scelte: il verificatore guarda i numeri, non le immagini.
Le scelte le fa una persona e si registrano in
`dati/lingue/attestazione_oggetti.json` con etichetta e motivo, come per i
ritratti.

I controlli:

  G1  copertura    ogni voce ha candidati, e le trenta ferraresi dichiarano
                  perché non ne possono avere
  G2  licenze      ogni candidato ha una licenza libera riconosciuta
  G3  misura      ogni candidato è abbastanza grande per la scheda del gioco
  G4  proporzione **per voce**: esiste almeno un candidato con la forma giusta
                  per entrare nella scheda senza essere straziato dal ritaglio
  G5  completezza  autore e indirizzo ci sono in ogni candidato
  G6  pertinenza   dichiarata, non automatica: quante voci restano da guardare
                  a vista e quante rischiano di avere un'immagine sbagliata
  G7  scivolamento  **avviso, non problema**: nessun candidato della voce nomina
                  l'oggetto né i termini cercati, il che vuol dire che la
                  ricerca ha scoperto una coincidenza di lettere. Non dice che
                  l'immagine sia sbagliata: dice che va guardata per prima

Il punto di G6 e G7 è la lezione già imparata con i ritratti, dove una ricerca
automatica ha restituito un gatto per Renata Viganò e una ceramica iraniana per
i mercanti di Ferrara. Una ricerca che trova il file «giusto» non ha ancora
trovato l'oggetto giusto, e G7 lo rende visibile senza guardare le immagini.
"""
import collections
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.abspath(os.path.join(BASE, "..", ".."))
DATI = os.path.join(RADICE, "dati", "lingue", "immagini_oggetti.json")
ATTESTAZIONE = os.path.join(RADICE, "dati", "lingue", "attestazione_oggetti.json")

# La scheda dell'oggetto nel gioco. I ritratti sono 48×54; l'oggetto ha poco
# più di spazio, perché si vede meglio, ma non il doppio.
LARGHEZZA_SCHEDA = 96
ALTEZZA_SCHEDA = 72

# Sotto questa misura l'immagine nel gioco verrebbe ingrandita, e il gioco non
# ingrandisce: non entra.
LARGHEZZA_MINIMA = 160
ALTEZZA_MINIMA = 120

# La scheda è 4:3. Si accetta una fascia attorno: ritagliare una foto in 4:3
# spesso toglie l'oggetto, e obbligare al ritaglio peggiorerebbe proprio la
# rappresentazione che il progetto vuole fedele.
PROPORZIONE = LARGHEZZA_SCHEDA / ALTEZZA_SCHEDA
TOLLERANZA = 0.45

LIB_OK = re.compile(
    r"public domain|pubblico dominio|\bpd\b|cc0|no restrictions"
    r"|cc[- ]?by(?![a-ns])|cc[- ]?by[- ]sa|attribution", re.I)
LIB_NO = re.compile(r"non[- ]?commercial|fair use|\bcc by[- ]nc|no deriv", re.I)


def candito_buono(c):
    """Un candidato che si può usare: licenza libera, abbastanza grande, con
    autore e indirizzo. Non dice che sia l'oggetto giusto: quello lo dice una
    persona."""
    if LIB_NO.search(c.get("licenza", "")):
        return False, "licenza non libera"
    if not LIB_OK.search(c.get("licenza", "")):
        return False, "licenza non riconosciuta"
    if not c.get("autore") or not c.get("url"):
        return False, "mancano autore o indirizzo"
    larghezza = c.get("larghezza") or 0
    altezza = c.get("altezza") or 0
    if not larghezza or not altezza:
        return False, "mancano le dimensioni"
    if larghezza < LARGHEZZA_MINIMA or altezza < ALTEZZA_MINIMA:
        return False, "troppo piccola"
    return True, ""


def proporzione_buona(c):
    larghezza = c.get("larghezza") or 0
    altezza = c.get("altezza") or 0
    if not larghezza or not altezza:
        return False
    p = larghezza / altezza
    return abs(p - PROPORZIONE) / PROPORZIONE <= TOLLERANZA


def scivolato(voce, termini, nome_file):
    """Il file è stato trovato per una coincidenza di lettere?

    Il metodo: dal nome del file si tolgono i termini cercati e le parole della
    voce. Se rimane un nome proprio che non compare da nessuna parte, il file
    c'entra per caso. È successo davvero: alla voce «la correggia» è stato
    proposto il file di un pittore che si chiama Correggio, e alla voce «gli
    occhiali» una moschea di Istanbul.

    Non è un controllo che «sa» se l'immagine è giusta: è un controllo che
    dice che il nome del file non parla dell'oggetto, e quindi che la scelta va
    guardata per prima.
    """
    testo = nome_file.replace("File:", "")
    testo = re.sub(r"[\d\(\)\[\]&,.\-—_%+']", " ", testo)
    noto = (voce + " " + " ".join(termini)).lower()
    residui = []
    for p in re.findall(r"[A-Za-zÀ-ÿ]{4,}", testo):
        if p.lower() in noto:
            continue
        residui.append(p)
    if not residui:
        return ""
    return ", ".join(residui[:3])


COMUNE = {
    # parole che compaiono in millemila nomi di file e non dicono niente
    "file", "image", "photo", "wikipedia", "commons", "jpg", "jpeg", "png",
    "gis", "svg", "italian", "italy", "italiano", "italiana", "greek",
    "greek", "ancient", "roman", "greece", "italia", "italian", "deutsch",
    "english", "france", "french", "germany", "spain", "greece", "turkey",
    "und", "der", "die", "das", "des", "von", "les", "des", "pour", "avec",
    "photo", "white", "black", "red", "green", "blue", "old", "new", "the",
    "chr", "st", "di", "da", "de", "del", "la", "le", "el", "los", "das",
    "cropped", "detail", "close", "view", "logo", "map", "chart", "cover",
}


def tutto_a_rischio(voce, termini, candidati):
    """Nessun candidato della voce nomina l'oggetto.

    Il confronto è con la voce **e con i termini cercati**: il file di un'anfora
    greca non contiene la parola «coppa» ma contiene «kylix», che è il termine
    giusto, e va tenuto. Il caso peggiore è quando non contiene né l'uno né
    l'altro: alla voce «la correggia» il file migliore era
    «Antonio Allegri da Correggio.jpg».
    """
    noto = {p.lower() for p in re.findall(r"[A-Za-zÀ-ÿ]{4,}", voce + " " + " ".join(termini))}
    for c in candidati:
        testo = re.sub(r"[\d\(\)\[\]&,.\-—_%+']", " ", c["file"].replace("File:", ""))
        parole = {p.lower() for p in re.findall(r"[A-Za-zÀ-ÿ]{4,}", testo)} - COMUNE
        if parole & noto:
            return False
    return True


def main():
    if not os.path.exists(DATI):
        print("manca", DATI)
        return 1
    with open(DATI, encoding="utf-8") as f:
        risultati = json.load(f)["risultati"]

    problemi = []
    copertura = collections.defaultdict(lambda: {"voci": 0, "con": 0, "senza": 0,
                                                "senza_proporzione": 0, "candidati": 0})
    licenze = collections.Counter()
    rischi = set()
    da_vedere = 0

    for a in risultati:
        lingua = a["lingua"]
        v = copertura[lingua]
        v["voci"] += 1
        etichetta = "%s %d (%s)" % (lingua, a["numero"], a["voce"])

        # G1 — copertura
        if not a["candidati"]:
            v["senza"] += 1
            if not a.get("motivo"):
                problemi.append("G1 %s: nessun candidato e nessun motivo dichiarato" % etichetta)
            continue
        v["con"] += 1
        da_vedere += 1
        if a["categoria"] != "da_vedere":
            problemi.append("G1 %s: ha candidati ma la categoria è %r" % (etichetta, a["categoria"]))

        usabili = 0
        per_proporzione = 0
        for c in a["candidati"]:
            v["candidati"] += 1
            licenze[c.get("licenza", "")[:30] or "(nessuna)"] += 1
            buono, motivo = candito_buono(c)
            if not buono:
                problemi.append("G2/G3/G5 %s: %s — %s" % (etichetta, c["file"], motivo))
                continue
            usabili += 1
            if proporzione_buona(c):
                per_proporzione += 1

        # G7 — la voce è a rischio quando nessun candidato nomina l'oggetto
        if usabili and tutto_a_rischio(a["voce"], a.get("termini", []), a["candidati"]):
            esempi = ", ".join(c["file"][:34] for c in a["candidati"][:2])
            rischi.add((etichetta, esempi, "nessun candidato nomina l'oggetto"))

        # G4 — la voce è coperta solo se almeno un candidato è-usabile ha la
        # forma giusta. Se tutti gli usabili sono strisce o strani, la voce
        # non è coperta e va cercata meglio.
        if usabili == 0:
            v["senza"] += 1
            problemi.append("G4 %s: nessun candidato usabile fra %d proposti"
                            % (etichetta, len(a["candidati"])))
        elif per_proporzione == 0:
            v["senza_proporzione"] += 1
            problemi.append("G4 %s: i %d candidati usabili sono tutti lontani "
                            "dalla proporzione della scheda (%.2f): vanno cercati "
                            "meglio, non ritagliati a forza"
                            % (etichetta, usabili, PROPORZIONE))

    ferraresi = [a for a in risultati if a["lingua"] == "FE"]
    for a in ferraresi:
        if a["candidati"]:
            problemi.append("G1 FE %d: un campo di rilevazione non ha immagine, ma ne ha una"
                            % a["numero"])

    scelte = 0
    if os.path.exists(ATTESTAZIONE):
        with open(ATTESTAZIONE, encoding="utf-8") as f:
            scelte = len(json.load(f).get("scelte", []))

    print("voci: %d" % len(risultati))
    for lingua in sorted(copertura):
        v = copertura[lingua]
        print("  %s: %2d voci, %2d con immagini libere, %2d senza, %d da cercare meglio"
              % (lingua, v["voci"], v["con"], v["senza"], v["senza_proporzione"]))
    print("candidati proposti: %d" % sum(v["candidati"] for v in copertura.values()))
    print("licenze dei candidati: %d diverse" % len(licenze))
    for k, n in licenze.most_common(8):
        print("    %4d  %s" % (n, k))
    print("G6 voci da guardare a vista: %d (il controllo automatico non può "
          "sapere se l'immagine è dell'oggetto giusto)" % da_vedere)
    voci_a_rischio = sorted({r[0] for r in rischi})
    print("G7 AVVISI, non problemi: %d voci in cui nessun candidato nomina "
          "l'oggetto, e che vanno quindi guardate per prime" % len(voci_a_rischio))
    for etichetta, esempi, scivolo in sorted(rischi)[:10]:
        print("    %-30s %s" % (etichetta, esempi))
    if len(rischi) > 10:
        print("    ... e altre %d voci" % (len(rischi) - 10))
    print("    G7 non dice che l'immagine sia sbagliata: dice che il suo nome")
    print("    non parla dell'oggetto, e quindi che guardarla è la prima cosa.")
    print("immagini già scelte a vista: %d" % scelte)
    print("problemi: %d" % len(problemi))
    for p in problemi:
        print("  " + p)
    return 1 if problemi else 0


if __name__ == "__main__":
    sys.exit(main())
