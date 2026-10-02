#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica i file sorgente dei titoli dei livelli linguistici.

Sei lingue (IT, FE, LA, EN, SI, EL), cinque anni, trenta livelli ciascuno:
900 record. Una riga per livello, campi separati da "|":

    lingua|anno|numero|titolo|fonte

`fonte` dichiara la provenienza del titolo:
  titolo  il titolo è quello scritto da Pietro
  tema    il titolo è una proposta costruita a partire dall'elenco di temi

Uso:
    python3 sorgenti/lingue/verifica_titoli.py
    python3 sorgenti/lingue/verifica_titoli.py --unisci   # rigenera
                                                     # titoli_livelli.txt
"""

import os
import re
import sys

LINGUE = ["IT", "FE", "LA", "EN", "SI", "EL"]
NOMI = {
    "IT": "italiano",
    "FE": "ferrarese",
    "LA": "latino",
    "EN": "inglese",
    "SI": "lingua dei segni italiana",
    "EL": "greco",
}

BASE = os.path.dirname(os.path.abspath(__file__))
UNITO = os.path.join(BASE, "titoli_livelli.txt")

RE = re.compile(r"^([A-Z]{2,3})\|([1-5])\|([1-9]|[12][0-9]|30)\|(.+)\|(titolo|tema)$")

# Un titolo è scritto in italiano (o in greco, o in inglese): niente
# sostituzione di carattere, niente romanzo corrotto, niente lettere a caso
# cadute dentro una parola. Solo lettere, cifre, spazi e pochissima punteggiatura.
CARATTERI_OK = re.compile(
    r"^[A-Za-zÀ-ÿͰ-Ͽἀ-῿0-9\s'’.,;:!?()\-—–/&·«»…]+$"
)

HEADER = """# I 900 titoli dei livelli linguistici: sei lingue, cinque anni, trenta livelli ciascuno.
#
# FORMATO, una riga per livello, campi separati da "|":
#   lingua|anno|numero|titolo|fonte
#
# `fonte` dichiara da dove viene il titolo, e non è una decorazione:
#   titolo  il titolo è quello scritto da Pietro, riga per riga
#   tema    il titolo è stato costruito a partire dall'elenco di temi che
#           Pietro ha dato per quell'anno (la lista è nel documento di
#           progetto, §3.4): il titolo è una proposta, e come tale va
#           trattata finché non è confermata. Un titolo costruito che sembra
#           definitorio è la cosa peggiore che possa capitare in un progetto
#           di scuola.
#
# LINGUE: IT italiano · FE ferrarese · LA latino · EN inglese · SI lingua dei
# segni italiana · EL greco.
#
# Il file è generato: si controlla con
#   python3 sorgenti/lingue/verifica_titoli.py
# e si ricostruisce dalle sei parti con
#   python3 sorgenti/lingue/verifica_titoli.py --unisci
#
"""


def percorso(codice):
    """Il file sorgente di una lingua: le sei parti, una per lingua.

    `titoli_livelli.txt` non è un sorgente ma un output: contiene i 900 record
    uniti nell'ordine delle lingue. Viene ricostruito con `--unisci`.
    """
    return os.path.join(BASE, "parte_%s.txt" % codice.lower())


def leggi(percorso):
    record = []
    with open(percorso, encoding="utf-8") as f:
        for n, riga in enumerate(f, 1):
            riga = riga.rstrip("\n")
            if not riga.strip() or riga.lstrip().startswith("#"):
                continue
            record.append((n, riga))
    return record


def controlla(codice):
    """Un file è valido se ha 150 record, tutti conformi, e i titoli sono puliti."""
    problemi = []
    visti = set()
    record = leggi(percorso(codice))
    if len(record) != 150:
        problemi.append("%s: %d record invece di 150" % (codice, len(record)))
    for n, riga in record:
        m = RE.match(riga)
        if not m:
            problemi.append("riga %d: non conforme al formato\n    %s" % (n, riga))
            continue
        lingua, anno, numero, titolo, fonte = m.groups()
        if lingua != codice:
            problemi.append("riga %d: lingua %s dentro il file %s" % (n, lingua, codice))
        chiave = (lingua, anno, numero)
        if chiave in visti:
            problemi.append("riga %d: livello %s ripetuto" % (n, ".".join(chiave)))
        visti.add(chiave)
        if not CARATTERI_OK.match(titolo):
            sospetti = sorted(set(titolo) - set(
                "abcdefghijklmnopqrstuvwxyz"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "ÀÉÈÌÒÙáéèìòù"
                "àèéìíîòóùúçÀÈÉÌÒÙÇ"
                "äöüßÄÖÜ"
                "čćžšđČĆŽŠĐ"
                "ăâîșțĂÂÎȘȚ"
                "żźŻŹ"
                "ğışçöüĞİŞÇÖÜ"
                "αβγδεζηθικλμνξοπρστυφχψω"
                "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
                "ἀἁἂἃἄἅἈἉᾶῆῃᾳ"
                "0 1 2 3 4 5 6 7 8 9"
                " '’,;:!?()-&/·«»…"
                "-—–."
            ))
            problemi.append(
                "riga %d: caratteri sospetti %s in %r"
                % (n, " ".join(repr(c) for c in sospetti[:6]), titolo)
            )
    for anno in "12345":
        numeri = sorted(int(n) for l, a, n in visti if l == codice and a == anno)
        attesi = list(range(1, 31))
        if numeri != attesi:
            mancanti = sorted(set(attesi) - set(numeri))
            problemi.append(
                "anno %s: %d livoli invece di 30%s"
                % (anno, len(numeri), (", mancano " + ", ".join(map(str, mancanti))) if mancanti else "")
            )
    return problemi


def unisci():
    """Ricostruisce `titoli_livelli.txt` dalle sei parti, nell'ordine delle lingue."""
    corpo = []
    for codice in LINGUE:
        for _, riga in leggi(percorso(codice)):
            corpo.append(riga)
    with open(UNITO, "w", encoding="utf-8") as f:
        f.write(HEADER)
        f.write("\n".join(corpo))
        f.write("\n")
    return len(corpo)


def controlla_unito(problemi):
    """Il file unito, quando esiste, deve dire esattamente quello che le parti dicono."""
    if not os.path.exists(UNITO):
        return 0
    atteso = []
    for codice in LINGUE:
        for _, riga in leggi(percorso(codice)):
            atteso.append(riga)
    ottenuto = [riga for _, riga in leggi(UNITO)]
    if ottenuto != atteso:
        problemi.append(
            "titoli_livelli.txt non corrisponde alle sei parti: "
            "rigenerarlo con --unisci"
        )
    return len(ottenuto)


def main():
    argomenti = sys.argv[1:]
    if "--unisci" in argomenti:
        print("rigenerati %d record in titoli_livelli.txt" % unisci())

    problemi = []
    for codice in LINGUE:
        problemi += controlla(codice)
    controlla_unito(problemi)
    totale = 0
    per_anno = {}
    for codice in LINGUE:
        for _, riga in leggi(percorso(codice)):
            m = RE.match(riga)
            if m:
                totale += 1
                per_anno[m.group(2)] = per_anno.get(m.group(2), 0) + 1

    print("record: %d" % totale)
    for anno in sorted(per_anno):
        print("  anno %s: %d livelli (6 lingue x 30)" % (anno, per_anno[anno]))
    print("problemi: %d" % len(problemi))
    for p in problemi:
        print("  " + p)
    return 1 if problemi else 0


if __name__ == "__main__":
    sys.exit(main())
