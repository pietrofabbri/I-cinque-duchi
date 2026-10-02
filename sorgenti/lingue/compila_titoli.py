#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la sezione dei 900 titoli per il documento di progetto.

Legge le sei parti dei titoli e scrive la sezione §6 del documento
`docs/videogioco-5-duchi-lingue.md`, sei tabelle (una per lingua), ciascuna con
cinque anni da trenta livelli. I titoli restano quelli di
`sorgenti/lingue/titoli_livelli.txt`: qui non se ne corregge nessuno.

Uso:
    python3 sorgenti/lingue/compila_titoli.py            # scrive su stdout
    python3 sorgenti/lingue/compila_titoli.py --verifica  # conta e confronta
"""

import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(BASE, "..", ".."))

LINGUE = [
    ("IT", "Italiano", "cibi"),
    ("FE", "Ferrarese", "detti popolari"),
    ("LA", "Latino", "superstizioni"),
    ("EN", "Inglese", "musiche"),
    ("SI", "Lingua dei segni italiana (LIS)", "artigianato tipico"),
    ("EL", "Greco", "bevande"),
]

RE = re.compile(r"^([A-Z]{2,3})\|([1-5])\|([1-9]|[12][0-9]|30)\|(.+)\|(titolo|tema)$")

FAMIGLIE = {
    1: "Fondamenta",
    2: "Struttura",
    3: "Comprensione",
    4: "Produzione",
    5: "Consapevolezza linguistica",
}


def leggi():
    titoli = {}
    for codice, _, _ in LINGUE:
        percorso = os.path.join(BASE, "parte_%s.txt" % codice.lower())
        for riga in open(percorso, encoding="utf-8"):
            riga = riga.rstrip("\n")
            if not riga.strip() or riga.startswith("#"):
                continue
            m = RE.match(riga)
            if not m:
                print("NON CONFORME: %s" % riga, file=sys.stderr)
                continue
            lingua, anno, numero, titolo, fonte = m.groups()
            titoli[(lingua, int(anno), int(numero))] = (titolo, fonte)
    return titoli


def tabella(codice, nome, oggetto, titoli):
    righe = [
        "### 6.%d %s" % (LINGUE.index((codice, nome, oggetto)) + 1, nome),
        "",
        "Oggetto di interazione: **%s** (§5). Trenta livelli all'anno, "
        "cinque blocchi da sei (§3): Fondamenta 1-6, Struttura 7-12, "
        "Comprensione 13-18, Produzione 19-24, Consapevolezza linguistica 25-30." % oggetto,
        "",
        "| N. | Anno 1 | Anno 2 | Anno 3 | Anno 4 | Anno 5 |",
        "|---|---|---|---|---|---|",
    ]
    for numero in range(1, 31):
        celle = []
        for anno in range(1, 6):
            titolo, fonte = titoli[(codice, anno, numero)]
            segno = "" if fonte == "titolo" else " †"
            celle.append("%d. %s%s" % (numero, titolo, segno))
        righe.append("| %d | %s |" % (numero, " | ".join(celle)))
    righe.append("")
    return "\n".join(righe)


def sezione(titoli):
    da_pietro = sum(1 for v in titoli.values() if v[1] == "titolo")
    proposte = len(titoli) - da_pietro
    out = [
        "## 6. I novecento titoli",
        "",
        "I titoli sono in `sorgenti/lingue/titoli_livelli.txt`, **%d record**, "
        "una riga per livello, nel formato `lingua|anno|numero|titolo|fonte`. "
        "Ogni riga dichiara la sua provenienza, e non è una decorazione:" % len(titoli),
        "",
        "| `fonte` | Che cosa vuol dire | Quanti |",
        "|---|---|---|",
        "| `titolo` | il titolo è quello scritto da Pietro, riga per riga | %d |"
        % da_pietro,
        "| `tema` | il titolo è stato costruito a partire dall'elenco di temi che "
        "Pietro ha dato per quell'anno: è una **proposta**, e come tale va trattata "
        "finché non è confermata | %d |" % proposte,
        "",
        "I titoli marcati con **†** nell'elenco seguente sono di fonte `tema`: "
        "sono proposte, non decisioni. Un titolo costruito che sembra definitorio "
        "è la cosa peggiore che possa capitare in un progetto di scuola, e per "
        "questo il documento li dichiara invece di mascherarli.",
        "",
        "La ripartizione per lingua è molto disuguale, ed è il primo fatto da "
        "guardare quando si rilegge l'elenco:",
        "",
        "| Lingua | Di Pietro | Proposti | Totale |",
        "|---|---|---|---|",
    ]
    for codice, nome, _ in LINGUE:
        p = sum(1 for (l, _, _), v in titoli.items() if l == codice and v[1] == "titolo")
        out.append("| %s | %d | %d | %d |" % (nome, p, 150 - p, 150))
    out += [
        "",
        "L'italiano è intero di Pietro, il greco è la lingua in cui le sue "
        "indicazioni erano un elenco di temi e non una lista di titoli: è la "
        "ragione per cui quasi tutti i titoli greci sono proposti. Su quelli di "
        "Pietro non si discute; sui proposti si discute, uno per volta.",
        "",
        "I **livelli informatici** hanno un titolo proprio, in "
        "`videogioco-5-duchi-schema-livelli.md` (v1.1), e non compaiono qui: "
        "le due liste sono distinte (§7 Q1).",
        "",
    ]
    for codice, nome, oggetto in LINGUE:
        out.append(tabella(codice, nome, oggetto, titoli))
    return "\n".join(out)


def main():
    titoli = leggi()
    attesi = 900
    if len(titoli) != attesi:
        print("attesi %d titoli, trovati %d" % (attesi, len(titoli)), file=sys.stderr)
    if "--verifica" in sys.argv:
        da_titolo = sum(1 for v in titoli.values() if v[1] == "titolo")
        print("titoli: %d (di Pietro: %d, proposti: %d)"
              % (len(titoli), da_titolo, len(titoli) - da_titolo))
        return 0
    print(sezione(titoli))
    return 0


if __name__ == "__main__":
    sys.exit(main())
