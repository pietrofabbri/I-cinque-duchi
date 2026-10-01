"""Estrae ottave dall'Orlando furioso, per canto e numero, da due fonti.

Perché serve uno script e non la memoria: una citazione del Furioso scritta a
rischio è una citazione falsa, e questo progetto non può permetterselo ne' una
volta. Qui ogni citazione esce dal testo con il suo canto e la sua ottava, e si
può riscontrare riga per riga.

Due fonti, due edizioni, due problemi diversi:

* **Project Gutenberg 3747**, testo piatto: 16 canti (solo la prima parte) e
  testo di un'edizione *modernizzata* («inchiostro» per «inchïostro»). Il
  lettore è lineare: intestazione di canto, poi numero, riga vuota, otto versi.
* **Wikisource it, edizione 1928** (Biblioteca BEIC, pubblico dominio), testo
  completo in 46 canti: non è un testo piatto ma il *wikitext* delle pagine
  del digitalizzato, e il numero d'ottava è esplicito: `{{O|8|of}}`.

Il default è Wikisource, perché 46 canti sono la vicenda e 16 no. Il resto del
progetto deve poter scegliere: `--fonte gutenberg` per le verifiche a riscontro
sull'altra edizione.

Uso:  python3 estrai_ottave.py 4 4             -> canto 4, ottava 4
       python3 estrai_ottave.py 12 30 45        -> un intervallo
       python3 estrai_ottave.py --cerca "senno"
       python3 estrai_ottave.py --salva         -> rigenera il testo normalizzato
       python3 estrai_ottave.py --canti         -> copertura, lacune, controli
"""
import json
import os
import re
import sys
import unicodedata

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(RADICE, "dati", "furioso")
GUTENBERG = os.path.join(D, "orlando_furioso.txt")
PAGINE = os.path.join(D, "pagine_wikisource.jsonl")
NORMALIZZATO = os.path.join(D, "orlando_furioso_1928.txt")

NUMERI = {
    "PRIMO": 1, "SECONDO": 2, "TERZO": 3, "QUARTO": 4, "QUINTO": 5, "SESTO": 6,
    "SETTIMO": 7, "OTTAVO": 8, "NONO": 9, "DECIMO": 10, "UNDICESIMO": 11,
    "DODICESIMO": 12, "TREDICESIMO": 13, "QUATTORDICESIMO": 14,
    "QUINDICESIMO": 15, "SEDICESIMO": 16, "DICESIMOSETTE": 17,
    "DICESIMOTTO": 18, "DICESIMONONO": 19, "VENTI": 20,
    "VENTUNO": 21, "VENTIDUE": 22, "VENTITRE": 23, "VENTIQUATTO": 24,
    "VENTICINQUE": 25, "VENTISESE": 26, "VENTISETTE": 27, "VENTOTTO": 28,
    "VENTINOVE": 29, "TRENTESIMO": 30, "TRENTUNO": 31, "TRENTADUE": 32,
    "TRENTATRE": 33, "TRENTAQUATRO": 34, "TRENTACINQUE": 35,
    "TRENTASEI": 36, "TRENTASETTE": 37, "TRENTOTTO": 38, "TRENTANOVE": 39,
    "QUARANTESIMO": 40, "QUARANTUNO": 41, "QUARANTADUE": 42,
    "QUARANTATRE": 43, "QUARANTAQUATRO": 44, "QUARANTACINQUE": 45,
    "QUARANTASEI": 46,
}
INTESTAZIONE = re.compile(r"^\s*CANTO\s+([A-Z]+)\s*$")
NUMERO_OTTAVA = re.compile(r"^\s*(\d{1,3})\s*$")
MARCA_OTTAVA_WS = re.compile(r"^\{\{O\s*\|\s*(\d{1,3})\s*\|")
VERSO_WS = re.compile(r"^[A-Za-zÀ-ÿ—–«]")   # i dialoghi aprono con il trattino
TEMPLATE_TESTO = re.compile(r"\{\{TestoCitato\s*\|[^|}]*\|([^|}]*)\}\}")
ALTRO_TEMPLATE = re.compile(r"\{\{[A-Za-z]+\s*(\|[^{}]*)?\}\}")
TAG = re.compile(r"<[^>]+>")

# Le difetti della trascrizione sono una quarantina su 4 796 ottave: sono
# un dato, non un'urgenza. Per questo sono dichiarati ma silenziosi, e si
# vedono solo con `--difetti`. Un controllo che urla ogni volta che si lancia
# viene smesso di leggere, e un controllo che non si legge non controlla.
SEGNALA = False


def normalizza(s):
    """Minuscole, senza accenti e senza punteggiatura: serve solo a cercare.

    DIFETTO CORRETTO: la punteggiatura veniva sostituita con uno spazio e gli
    spazi non venivano ricomposti. Ogni trattino e ogni virgola lasciava quindi
    due spazi di fila, e una ricerca di tre parole («ferma baiardo mio») non
    trovava mai niente in un testo pieno di dialoghi, cioè nei passaggi più
    vivi del poema. La ricerca falliva e non c'era nessun errore: diceva solo
    «nessuna ottava contiene...». Ora gli spazi sono uno solo.
    """
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("’", "'").replace("ò", "o").replace("ì", "i")
    s = re.sub(r"[^a-z0-9' ]", " ", s)
    return re.sub(r"\s{2,}", " ", s).strip()


def ripulisci(s):
    """Wikisource -> testo. Restituisce None se la riga non e' un verso.

    Tre casi, in ordine: i template che portano testo dentro la riga
    (`{{TestoCitato|Corano|Alcorano}}` dentro «l'Alcorano» vanno tenuti, con la
    forma *leggibile*, cioe' il secondo argomento); i template di stile e le
    intestazioni, che spariscono; i tag HTML del transclusion.
    """
    if "<" in s:
        s = TAG.sub(" ", s)
    if "{{" in s:
        s = TEMPLATE_TESTO.sub(r"\1", s)
        s = ALTRO_TEMPLATE.sub(" ", s)
    s = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", s)   # collegamenti
    s = re.sub(r"'{2,}", "", s)                              # apici di Template:Lang
    s = s.replace(" ", " ").strip()
    s = re.sub(r"\s{2,}", " ", s)
    return s or None


def da_wikisource():
    """(canto, ottava) -> versi, presi dal wikitext delle pagine BEIC.

    Due difetti possibili, e sono entrambi silenziosi.

    * **L'ottava tagliata dal salto di pagina.** Il digitalizzato cambia foglio
      nel mezzo di un'ottava: gli ultimi versi stanno sulla pagina prima e
      i primi sulla dopo. Il lettore che azzera tutto a ogni `{{O|...}}`
      scrive metà ottava sotto l'ottava successiva, e il risultato è un testo
      che sembra giusto. Qui i versi a cavallo passano all'ottava giusta.
    * **L'ottava senza verso.** Le ottave che cominciano con un dialogo sono
      introdotte da un trattino (`— Ferma, Baiardo mio, deh, ferma il piede!`).
      Un lettore che ammette solo le lettere perde metà di quelle ottave e
      non se ne accorge: sono le più vive, sono quelle che fanno ridere.
    * **Il numero scritto due volte.** In certe pagine il trascrittore scrive
      due volte lo stesso numero (`16 17 19 19` nella pagina 52 del volume I):
      è un refuso, e non un'ottava ripetuta. Ci sono due modi di risolverlo,
      e questo progetto sceglie di non farne nessuno: si potrebbe *rinumerare*
      (la pagina avrebbe 16, 17, 18, 19) e si avrebbe un testo senza buchi,
      ma allora il numero stampato sul libro e il numero del nostro indice
      non coinciderebbero più, e una verifica sul libro cartaceo — l'unica che
      conta a scuola — darebbe un numero diverso. Qui il primo testo che
      arriva con quel numero resta il primo, il secondo va in una lista a
      parte, e la chiave viene dichiarata come ambigua. Un dato incerto
      dichiarato vale più di un dato incerto riparato in silenzio.
    * **Le lacune vere.** Non tutte le ottave sono numerate nella trascrizione
      e alcune pagine mancano. Se manca un'ottava, l'indice la salta e non lo
      dice: la citazione successiva sembra sbagliata per un numero che è
      sbagliato due volte. Per questo `controlla` conta e dichiara ogni
      lacuna, e non le deduce dal buon umore.
    """
    if not os.path.exists(PAGINE):
        raise SystemExit("mancano le pagine Wikisource: %s (lancia scarica_wikisource.py)" % PAGINE)
    canto_precedente = None
    problemi_aperti = []
    ottave = {}
    ripetute = {}
    numero = None
    parziali = []

    def chiudi(canto, n, blocco):
        """Mette l'ottava al suo posto, o la dichiara ambigua.

        Sette versi non sono un difetto: sono la **rima extranea**, il verso
        senza rima con cui Ariosto chiude metà delle ottave (`e l'altro è
        l'Alcorano.`), e nella stampa del 1928 è messo fra parentesi per
        distinguerlo. Contare anche quello come errore sarebbe rumore, e il
        rumore è nemico: quando un controllo segnala duecento cose, le due
        che contano non si leggono più.
        """
        if len(blocco) not in (7, 8):
            problemi_aperti.append((canto, n, len(blocco)))
        if (canto, n) in ottave:
            ripetute.setdefault((canto, n), []).append(list(blocco))
        else:
            ottave[(canto, n)] = list(blocco)

    for riga in open(PAGINE, encoding="utf-8"):
        r = json.loads(riga)
        canto = r["canto"]
        if numero is not None and canto != canto_precedente:
            # una pagina non comincia mai dentro un'ottava: se resta qualcosa
            # aperto, e' un difetto di copertura e va detto, non taciuto
            chiudi(canto_precedente, numero, parziali)
            numero, parziali = None, []
        canto_precedente = canto
        for grezza in r["wikitext"].split("\n"):
            s = grezza.strip()
            m = MARCA_OTTAVA_WS.match(s)
            if m:
                if numero is not None:
                    chiudi(canto, numero, parziali)
                numero = int(m.group(1))
                parziali = []
                continue
            if numero is None:
                continue
            verso = ripulisci(s)
            if verso and VERSO_WS.match(verso):
                parziali.append(verso)
    if numero is not None:
        chiudi(canto_precedente, numero, parziali)
    for c, n, k in problemi_aperti:
        if SEGNALA:
            print("ATTENZIONE: canto %d ottava %d con %d versi, invece di 8" % (c, n, k))
    if SEGNALA:
        for (c, n), blocchi in sorted(ripetute.items()):
            print("ATTENZIONE: canto %d ottava %d: il numero compare %d volte nella "
                  "trascrizione; l'indice tiene la prima, le altre vanno verificate a "
                  "occhio" % (c, n, len(blocchi) + 1))
    return ottave


def da_gutenberg():
    """(canto, ottava) -> testo dell'ottava, dal testo piatto di Gutenberg.

    La struttura del file e' questa: intestazione di canto, e poi per ogni
    ottava un numero su una riga propria, una riga vuota, e gli otto versi.

    DIFETTO CORRETTO NELLA PRIMA VERSIONE: la riga vuota fra il numero e il
    primo verso azzerava il segnalino «sto leggendo un numero», e i versi non
    entravano mai nella lista. Il risultato era un indice vuoto, senza errori:
    lo script non si rompeva, semplicemente non trovava niente, ed e' il
    peggiore tipo di difetto — silenzioso.
    """
    if not os.path.exists(GUTENBERG):
        raise SystemExit("manca il testo: %s" % GUTENBERG)
    ottave = {}
    canto = 0
    attesa = 0
    versi = []
    numero_appena_letto = False
    for riga in open(GUTENBERG, encoding="utf-8-sig"):
        riga = riga.rstrip("\n")
        m = INTESTAZIONE.match(riga)
        if m:
            if versi:
                ottave[(canto, attesa)] = list(versi)
            canto = NUMERI.get(m.group(1).strip(), 0)
            attesa = 0
            versi = []
            numero_appena_letto = False
            continue
        if canto == 0:
            continue
        if not riga.strip():
            continue                      # la vuota non interrompe niente
        m = NUMERO_OTTAVA.match(riga)
        if m and not numero_appena_letto:
            if versi:
                ottave[(canto, attesa)] = list(versi)
            attesa = int(m.group(1))
            versi = []
            numero_appena_letto = True
            continue
        versi.append(riga.strip())
        numero_appena_letto = False
    if versi:
        ottave[(canto, attesa)] = list(versi)
    return ottave


def indicizza(fonte="wikisource"):
    return da_wikisource() if fonte == "wikisource" else da_gutenberg()


def salva_testo(ottave, percorso=NORMALIZZATO):
    """Riscrive l'indice nel formato piatto, cosi' anche l'altra fonte e' leggibile."""
    per_canto = {}
    for (c, n), versi in sorted(ottave.items()):
        per_canto.setdefault(c, []).append((n, versi))
    with open(percorso, "w", encoding="utf-8") as f:
        f.write("ORLANDO FURIOSO DI MESSER LUDOVICO ARISTO\n")
        f.write("Trascrizione dell'edizione 1928 (Biblioteca BEIC, tre volumi)\n")
        f.write("pubblicata in Wikisource; testo in pubblico dominio.\n")
        f.write("Generata da sorgenti/furioso/estrai_ottave.py --salva\n\n")
        for c in sorted(per_canto):
            f.write("CANTO %d\n\n" % c)
            for n, versi in per_canto[c]:
                f.write("%d\n\n" % n)
                for v in versi:
                    f.write(v + "\n")
                f.write("\n")
    return percorso


def controlla(ottave, attendute=None):
    """Restituisce un elenco di problemi. Vuoto significa 'tutto bene'."""
    problemi = []
    per_canto = {}
    for (c, n) in ottave:
        per_canto.setdefault(c, set()).add(n)
    for c in sorted(per_canto):
        numeri = per_canto[c]
        mancanti = [n for n in range(1, max(numeri) + 1) if n not in numeri]
        if mancanti:
            problemi.append("canto %d: %d ottave mancanti (%s%s)"
                            % (c, len(mancanti), ", ".join(str(x) for x in mancanti[:6]),
                               ", ..." if len(mancanti) > 6 else ""))
        strane = [n for n in numeri if len(ottave[(c, n)]) not in (7, 8)]
        if strane:
            problemi.append("canto %d: %d ottave con un numero di versi anomalo (%s)"
                            % (c, len(strane), ", ".join(str(x) for x in strane[:6])))
    return problemi


def mostra(ottave, canto, numeri):
    for n in numeri:
        versi = ottave.get((canto, n))
        print("\n--- canto %d, ottava %d" % (canto, n))
        if versi:
            for r in versi:
                print("   " + r)
        else:
            print("   (non esiste)")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--difetti" in argv:
        SEGNALA = True
        argv.remove("--difetti")
    fonte = "wikisource"
    if "--fonte" in argv:
        i = argv.index("--fonte")
        fonte = argv[i + 1]
        del argv[i:i + 2]
    if fonte == "gutenberg":
        if "--cerca" in argv:
            i = argv.index("--cerca")
            termine = normalizza(argv[i + 1])
            ottave = indicizza("gutenberg")
            trovate = 0
            for (c, n), versi in sorted(ottave.items()):
                if termine in normalizza(" ".join(versi)):
                    mostra(ottave, c, [n])
                    trovate += 1
                    if trovate >= 8:
                        break
            if not trovate:
                print("nessuna ottava contiene %r" % argv[i + 1])
            sys.exit(0)
        numeri = [int(x) for x in argv if x.isdigit()]
        if numeri:
            ottave = indicizza("gutenberg")
            print("fonte: Project Gutenberg 3747 (%d ottave, 16 canti, edizione modernizzata)"
                  % len(ottave))
            mostra(ottave, numeri[0], numeri[1:])
        else:
            ottave = indicizza("gutenberg")
            print("fonte: Project Gutenberg 3747, %d ottave" % len(ottave))
            for p in controlla(ottave):
                print("  " + p)
        sys.exit(0)

    ottave = indicizza("wikisource")
    if "--salva" in argv:
        print("scritto: %s" % salva_testo(ottave))
    if "--canti" in argv or not argv:
        canti = sorted({c for c, _ in ottave})
        print("ottave indicizzate: %d, canti: %d" % (len(ottave), len(canti)))
        for c in canti:
            numeri = sorted(n for cc, n in ottave if cc == c)
            print("  canto %2d: %3d ottave (%d..%d)" % (c, len(numeri), numeri[0], numeri[-1]))
        problemi = controlla(ottave)
        print("problemi dichiarati: %d (usa --difetti per l'elenco)" % len(problemi))
        if SEGNALA:
            for p in problemi:
                print("  " + p)
    if "--cerca" in argv:
        i = argv.index("--cerca")
        termine = normalizza(argv[i + 1])
        trovate = 0
        for (c, n), versi in sorted(ottave.items()):
            if termine in normalizza(" ".join(versi)):
                mostra(ottave, c, [n])
                trovate += 1
                if trovate >= 8:
                    break
        if not trovate:
            print("nessuna ottava contiene %r" % argv[i + 1])
    numeri = [int(x) for x in argv if x.isdigit()]
    if numeri:
        mostra(ottave, numeri[0], numeri[1:])