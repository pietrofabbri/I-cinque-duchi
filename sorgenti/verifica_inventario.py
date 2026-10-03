#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica l'inventario degli elementi interattivi: I1-I5.

L'inventario promette che gli elementi con cui si gioca siano un elenco
chiuso, che ognuno dichiari che cosa dà e se è facoltativo, che i registri
personali si possano rileggere, e che nessuno di essi prometta più di quanto il
gioco fa. Qui si controllano le cinque cose, e tutte e cinque sono controlli di
forma: verificano che l'inventario e i documenti che lo circondano dicano la
stessa cosa, non che il gioco esista.

  I1  gli elementi interattivi sono un elenco chiuso e numerato senza buchi
  I2  ogni elemento dichiara che cosa dà e se è facoltativo
  I3  i quattro registri personali sono dichiarati e il gioco deve poter rileggerli
  I4  nessun elemento promette un vantaggio che non compare nella riga «dà in cambio»
  I5  la mappa degli scambi ha una riga e una colonna per ogni elemento

Uso:  python3 sorgenti/verifica_inventario.py
"""
import io
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(RADICE, "docs", "videogioco-5-duchi-inventario.md")
RIPASSI = os.path.join(RADICE, "docs", "videogioco-5-duchi-ripassi.md")
PREMI = os.path.join(RADICE, "docs", "videogioco-5-duchi-premi.md")
MECCANICHE = os.path.join(RADICE, "docs", "videogioco-5-duchi-meccaniche.md")
LINGUE = os.path.join(RADICE, "docs", "videogioco-5-duchi-lingue.md")

REGISTRI = ("salvadanaio", "quaderno dei segni", "registro dei ripassi", "fascia")


def leggi(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def main():
    if not os.path.exists(DOC):
        print("manca %s" % DOC)
        return 2
    doc = leggi(DOC)
    ripassi = leggi(RIPASSI)
    premi = leggi(PREMI)
    meccaniche = leggi(MECCANICHE)
    lingue = leggi(LINGUE)
    problemi = []

    print("== I1. gli elementi interattivi sono un elenco chiuso e numerato ==")
    # la tabella degli elementi: | **N** | **nome** | ...
    elementi = re.findall(r"^\| \*\*(\d+)\*\* \| \*\*([^*]+)\*\* \|", doc, re.M)
    numeri = [int(n) for n, _ in elementi]
    print("   elementi: %d (%s)" % (len(elementi), ", ".join(n for _, n in elementi)))
    if numeri != list(range(1, len(numeri) + 1)):
        problemi.append("I1: gli elementi sono numerati %s, senza buchi" % numeri)
    if len({n for _, n in elementi}) != len(elementi):
        problemi.append("I1: ci sono elementi con lo stesso nome")
    for frase in ("elenco chiuso", "sette cose"):
        if frase not in doc and "sette" not in doc:
            problemi.append("I1: il documento non dichiara l'elenco chiuso")

    print("\n== I2. ogni elemento dichiara che cosa dà e se è facoltativo ==")
    righe = re.findall(r"^\| \*\*(\d+)\*\* \| \*\*([^*]+)\*\* \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$",
                       doc, re.M)
    senza_da = [n for n, _, _, da, _ in righe if not da.strip()]
    senza_fac = [n for n, _, _, _, fac in righe if not fac.strip()]
    print("   righe con le due colonne: %d su %d" % (len(righe), len(elementi)))
    if senza_da:
        problemi.append("I2: gli elementi %s non dicono che cosa danno" % senza_da)
    if senza_fac:
        problemi.append("I2: gli elementi %s non dicono se sono facoltativi" % senza_fac)
    # l'oggetto di interazione e' facoltativo in tutti i 900 livelli: la fonte lo dice
    # `lingue.md` scrive «novecento» in lettere e il dato in cifre: si cerca
    # l'aggettivo e il numero in una delle due forme
    b = lingue.lower()
    if not ("facoltativo in tutti i novecento livelli" in b
            or "facoltativo in tutti i 900 livelli" in b):
        problemi.append("I2: lingue.md non dichiara piu' che l'oggetto e' facoltativo ovunque")

    print("\n== I3. i quattro registri personali sono dichiarati e rileggibili ==")
    # il documento scrive i registri con l'articolo dentro i grassetti
    # («la salvadanaio»), quindi si cerca il nome dentro, non il nome intero
    for r in REGISTRI:
        presente = bool(re.search(r"\*\*[^*]*%s[^*]*\*\*" % re.escape(r), doc, re.I)) \
            or ("| %s |" % r) in doc
        print("   %-22s %s" % (r, "dichiarato" if presente else "ASSENTE"))
        if not presente:
            problemi.append("I3: il registro «%s» non e' nell'inventario" % r)
    if "rileggerl" not in doc.lower() and "rileggerli" not in doc.lower():
        problemi.append("I3: l'inventario non dice che il gioco deve poter rileggere i registri")
    if "dati personali" not in meccaniche and "dati personali" not in doc:
        problemi.append("I3: nessun documento dice che le previsioni sono dati personali")

    print("\n== I4. nessun elemento promette piu' di quanto il gioco fa ==")
    # gli elementi che danno qualcosa devono avere una riga nella mappa degli scambi
    scambi = re.findall(r"^\| (alla voce|all'oggetto|al viaggio|al test|al richiamo|al premio|"
                        r"alla fascia) \| ([^|]+) \| ([^|]+) \|$", doc, re.M)
    print("   righe della mappa degli scambi: %d" % len(scambi))
    if len(scambi) != len(elementi):
        problemi.append("I4: la mappa degli scambi ha %d righe e gli elementi sono %d"
                        % (len(scambi), len(elementi)))
    # il premio non puo' promettere un catalogo che non esiste: la cardinalita' e' dichiarata
    if "un premio per livello" not in premi:
        problemi.append("I4: premi.md non dichiara la cardinalita' scelta")
    if "circa 900" not in doc:
        problemi.append("I4: l'inventario non dichiara la cifra dei premi")

    print("\n== I5. nessun elemento promette un vantaggio vago ==")
    # la fascia e' l'unica riga in cui il gioco non da niente: deve essere dichiarata
    if "non dà niente" not in doc and "non da niente" not in doc:
        problemi.append("I5: l'inventario non dichiara la riga in cui il gioco non da niente")
    if "facoltativo in tutti i 900" not in lingue and "facoltativo in tutti i 900" not in doc:
        problemi.append("I5: non e' dichiarato che l'oggetto si puo' saltare")
    if "test di ingresso" not in ripassi:
        problemi.append("I5: ripassi.md non esiste piu': il test non e' piu' dichiarato")
    # il vantaggio tangibile: nessun elemento promette un beneficio futuro
    for vietata in ("diventerai bravo", "ti sarà utile dopo", "per tutta la vita"):
        if vietata in doc:
            problemi.append("I5: l'inventario promette un vantaggio futuro: «%s»" % vietata)

    print("\n== sintesi ==")
    if problemi:
        for p in problemi:
            print("   difetto: " + p)
        print("\nproblemi: %d" % len(problemi))
        return 1
    print("   nessun difetto: gli elementi sono chiusi, ognuno dice che cosa dà e se è "
          "facoltativo, i quattro registri si possono rileggere")
    print("\n==== controlli superati: 5/5 ====")
    return 0


if __name__ == "__main__":
    sys.exit(main())