"""Verifica gli **incontri** dei centocinquanta livelli.

Il file `dati/incontri_livelli.json` mette in una riga per tappa le tre cose che
il progetto aveva separate: **dove si va, chi si incontra, e chi c'è di facoltativa**.
Questo controllo è quello che tiene insieme le tre, e nasce da un difetto vero: il
quinto anno dichiarava **2 voci collettive su 30** e la tabella ne portava **3**.

I controlli sono cinque, e l'ultimo è quello per cui il file esiste.

  C1  le tappe sono esattamente 5 x 30, nessuna due volte, nessuna fuori schema
  C2  **ogni tappa ha una voce obbligatoria**, un luogo, e il mezzo o la sua
      dichiarazione di assenza: nessuna tappa dove il giocatore non incontra nessuno
  C3  **ogni voce porta la prova della sua classificazione**, e la prova è una
      delle quattro dichiarate: una voce di cui non si sa come è stata decisa è
      una voce che il prossimo lettore classificherà diversamente
  C4  **i facoltativi sono distinti dalla voce obbligatoria**, e nessun tappa porta
      la stessa persona due volte nella stessa casella
  C5  **il numero delle voci collettive è quello che i documenti dichiarano**:
      questo è il controllo che ha trovato il difetto del quinto anno, e vale
      perché il numero è scritto a mano in quattro documenti diversi

C5 è il controllo che vale, e vale per una ragione che non è la solita: gli altri
confrontano il dato con **altri dati**, e non vedono le frasi. Qui si confronta il
dato con **quello che quattro documenti scrivono a mano**, ed è l'unico modo perché
un numero dichiarato resti vero quando la tabella sotto cambia.

**C3 e il campo `prova`.** Una voce collettiva è una voce *senza nome proprio*
(anni 2-5 §5), e il progetto la marca a mano nella tabella con la parola
«collettivo» e l'attendibilità `C`. Il file registra **quale prova ha deciso**:
`marcatura_nella_tabella` è la buona, `iniziale_maiuscola` è il ripiego. Un
documento che aggiunge una voce a metà senza marcarla viene classificato dal
ripiego, e C3 lo segnala invece di lasciarlo passare.

Uso:  python3 sorgenti/verifica_incontri.py
"""
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INCONTRI = os.path.join(RADICE, "dati", "incontri_livelli.json")
DOCS = os.path.join(RADICE, "docs")

# I documenti che dichiarano quante voci collettive ha l'anno, e la frase da cui
# leggerlo. Il numero e' scritto a mano, ed e' per questo che va controllato: la
# frase e' dentro il documento, non dentro il dato.
DICHIARATI = [
    (2, "videogioco-5-duchi-anno2-penisola.md", r"sono (\d+) su 30"),
    (3, "videogioco-5-duchi-anno3-europa.md", r"sono \*\*(\d+) su 30\*\*"),
    (4, "videogioco-5-duchi-anno4-mondo.md", r"sono \*\*(\d+) su 30\*\*"),
    (5, "videogioco-5-duchi-anno5-mondo.md", r"sono \*\*(\d+) su 30\*\*"),
]

PROVE = {"marcatura_nella_tabella", "codice", "catalogo_anno1",
         "iniziale_maiuscola", "iniziale_minuscola"}

MEZZI_NOTI = {"a_piedi", "cavallo", "galera", "pipa", "nave", "carovana",
              "diligenza", "treno", "aereo", "crociera", "moto", "sci",
              "elicottero", "monopattino"}


def numero_dichiarato(anno, nome, pattern):
    """Il numero che il documento scrive, o None se non lo scrive."""
    path = os.path.join(DOCS, nome)
    if not os.path.exists(path):
        return None, "manca %s" % nome
    testo = open(path, encoding="utf-8").read()
    # La frase comincia con l'iniziale maiuscola in alcuni documenti («Sono 3 su
    # 30») e minuscola in altri: il confronto non distingue i due casi, perche'
    # non e' un dato che cambia con la maiuscola.
    m = re.search(pattern, testo, re.I)
    if not m:
        return None, "nessuna frase che dichiari il numero"
    return int(m.group(1)), None


def main():
    if not os.path.exists(INCONTRI):
        print("non trovo %s: esegui prima estrai_incontri.py"
              % os.path.relpath(INCONTRI, RADICE))
        return 1
    d = json.load(open(INCONTRI, encoding="utf-8"))
    incontri = d["incontri"]
    problemi = []

    # C1: il conto
    attesi = ["%d-%d" % (a, n) for a in range(1, 6) for n in range(1, 31)]
    ids = [x["livello"] for x in incontri]
    for lid in sorted(set(ids)):
        if ids.count(lid) > 1:
            problemi.append("C1  livello ripetuto: %s" % lid)
    mancanti = [t for t in attesi if t not in ids]
    inpiu = [t for t in ids if t not in attesi]
    if mancanti:
        problemi.append("C1  %d livelli mancanti: %s"
                        % (len(mancanti), ", ".join(mancanti[:10])))
    if inpiu:
        problemi.append("C1  %d livelli fuori schema: %s"
                        % (len(inpiu), ", ".join(inpiu[:10])))

    per_anno = {}
    for x in incontri:
        per_anno.setdefault(x["anno"], []).append(x)

    for x in incontri:
        lid = x["livello"]

        # C2: la tappa e' giocabile
        voce = x["voce_obbligatoria"]
        if not voce.get("nome"):
            problemi.append("C2  %s: nessuna voce obbligatoria" % lid)
        if not x.get("luogo"):
            problemi.append("C2  %s: nessun luogo" % lid)
        if x.get("mezzo_stato") != "dichiarato" and x.get("mezzo") is not None:
            problemi.append("C2  %s: mezzo %r con stato %r"
                            % (lid, x.get("mezzo"), x.get("mezzo_stato")))
        if x.get("mezzo_stato") == "dichiarato" and x.get("mezzo") not in MEZZI_NOTI:
            problemi.append("C2  %s: il mezzo %r non è fra quelli di percorsi.md §1"
                            % (lid, x.get("mezzo")))
        if x.get("mezzo") is None and x.get("mezzo_stato") == "dichiarato":
            problemi.append("C2  %s: mezzo dichiarato ma assente" % lid)

        # C3: la prova della classificazione
        if voce.get("prova") not in PROVE:
            problemi.append("C3  %s: la voce %r ha una prova %r che non è una delle "
                            "quattro dichiarate"
                            % (lid, voce.get("nome"), voce.get("prova")))
        elif voce.get("prova") == "iniziale_maiuscola":
            # Il ripiego e' accettato, ma solo se il nome **non** e' gia' noto
            # come collettivo: altrimenti vuol dire che una voce collettiva ha
            # preso un nome proprio e nessuno l'ha marcata. Il caso inverso — un
            # nome proprio senza codice — e' normale e non si segnala.
            collettivi_noti = {f["nome"] for x in incontri
                               for f in (x.get("facoltativi") or [])
                               if f.get("tipo") == "collettivo"}
            if voce.get("nome") in collettivi_noti:
                problemi.append("C3  %s: la voce %r e' collettiva altrove fra le "
                                "facoltative, e qui e' stata trattata come "
                                "personaggio" % (lid, voce.get("nome")))

        # C4: i facoltativi
        fac = x.get("facoltativi")
        if fac is None:
            problemi.append("C4  %s: la colonna dei facoltativi non è dichiarata" % lid)
        else:
            nomi = [f.get("nome") for f in fac]
            if voce.get("nome") in nomi:
                problemi.append("C4  %s: %r è insieme la voce obbligatoria e un "
                                "facoltativo" % (lid, voce.get("nome")))
            dup = {n for n in nomi if nomi.count(n) > 1}
            if dup:
                problemi.append("C4  %s: facoltativo ripetuto: %s"
                                % (lid, ", ".join(sorted(dup))))
            for f in fac:
                if not f.get("nome"):
                    problemi.append("C4  %s: un facoltativo senza nome" % lid)
                if f.get("prova") not in PROVE:
                    problemi.append("C4  %s: il facoltativo %r ha una prova %r che "
                                    "non è una delle dichiarate"
                                    % (lid, f.get("nome"), f.get("prova")))

    # C5: i numeri che i documenti dichiarano
    tabella_c5 = []
    for anno, nome, pattern in DICHIARATI:
        dichiarato, errore = numero_dichiarato(anno, nome, pattern)
        trovate = sum(1 for x in per_anno.get(anno, [])
                      if x["voce_obbligatoria"].get("tipo") == "collettivo")
        if dichiarato is None:
            problemi.append("C5  anno %d: %s" % (anno, errore))
            tabella_c5.append((anno, "?", trovate))
        elif dichiarato != trovate:
            problemi.append("C5  anno %d: il documento dichiara %d voci collettive, "
                            "il dato ne ha %d"
                            % (anno, dichiarato, trovate))
            tabella_c5.append((anno, dichiarato, trovate))
        else:
            tabella_c5.append((anno, dichiarato, trovate))

    # il riepilogo
    print("incontri: %s" % os.path.relpath(INCONTRI, RADICE))
    print("  %d tappe su %d attese" % (len(incontri), len(attesi)))
    for anno in sorted(per_anno):
        xs = per_anno[anno]
        nomi = {x["voce_obbligatoria"]["nome"] for x in xs}
        coll = sum(1 for x in xs if x["voce_obbligatoria"].get("tipo") == "collettivo")
        fac = sum(len(x.get("facoltativi") or []) for x in xs)
        print("  anno %d: %2d tappe, %2d voci distinte, %d facoltativi, "
              "%d collettive, mezzo %s"
              % (anno, len(xs), len(nomi), fac, coll,
                 xs[0]["mezzo"] if xs[0]["mezzo"] else xs[0]["mezzo_stato"]))
    print("  collettive: dichiarato / dato")
    for anno, dich, trov in tabella_c5:
        segno = "OK" if dich == "?" or int(dich) == trov else "DIVERSO"
        print("    anno %d: %s / %d  %s" % (anno, dich, trov, segno))

    if problemi:
        print("\nPROBLEMI: %d" % len(problemi))
        for p in problemi[:60]:
            print("  " + p)
        if len(problemi) > 60:
            print("  ... e altri %d" % (len(problemi) - 60))
        return 1
    print("\nOK: nessun problema")
    return 0


if __name__ == "__main__":
    sys.exit(main())