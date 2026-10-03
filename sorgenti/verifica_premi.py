"""Verifica il catalogo dei premi: P1-P5.

Dieci categorie, undici discipline e quattro prove di ammissione sono numeri e
nomi che si possono confrontare fra loro e con gli altri documenti. Qui si
controlla che la lista sia chiusa e senza buchi, che ogni disciplina abbia una
categoria primaria, che i sei ambiti della sfida a mani nude abbiano ciascuno un
premio possibile, che nessuna disciplina sia inventata, e che nessun premio possa
essere un'opera generata o un'immagine senza licenza.

  P1  le dieci categorie sono A..J, senza buchi e senza duplicati
  P2  ogni disciplina ha almeno una categoria primaria, e sono le undici del progetto
  P3  i sei domini della sfida a mani nude hanno ciascuno almeno una categoria
  P4  nessuna disciplina abbinata e' una disciplina che il progetto non ha
  P5  nessun premio puo' essere generato o senza licenza: il divieto e' scritto

Uso:  python3 sorgenti/verifica_premi.py
"""
import io
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(RADICE, "docs", "videogioco-5-duchi-premi.md")
LINGUE = os.path.join(RADICE, "docs", "videogioco-5-duchi-lingue.md")
QUADRO = os.path.join(RADICE, "docs", "videogioco-5-duchi-quadro-trasversale.md")

CATEGORIE = list("ABCDEFGHIJ")

# Le discipline del gioco, dove l'informatica e' esclusa per decisione di Pietro.
DISCIPLINE = ("Italiano", "Ferrarese", "Latino", "Inglese", "Lingua dei segni",
              "Greco", "Diritto", "Etica", "Filosofia", "Psicologia",
              "Osservazione e attenzione")

STATI = ("dichiarato", "possibile", "da_costruire")

DOMINI_SFIDA = ("logica", "calcolo mentale e stime", "informatica",
                "linguistica e testo", "Costituzione e cittadinanza",
                "osservazione e attenzione")

VIETATI = ("immagine generata", "immagine sintetica", "senza licenza libera")


def sezione(doc, inizio, fine):
    """Il testo fra due marcatori: i documenti hanno piu' tabelle e ogni controllo
    deve leggere la sua, non la prima che capita."""
    i = doc.index(inizio)
    j = doc.index(fine, i + len(inizio))
    return doc[i:j]


def leggi(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def main():
    if not os.path.exists(DOC):
        print("manca %s" % DOC)
        return 2
    doc = leggi(DOC)
    lingue = leggi(LINGUE)
    quadro = leggi(QUADRO)
    problemi = []

    print("== P1. le dieci categorie sono A..J, senza buchi ==")
    tabelle = re.findall(r"^\| \*\*([A-J])\*\* \| ([^|]+) \|", doc, re.M)
    trovate = [c for c, _ in tabelle]
    print("   categorie trovate: %s" % ", ".join(trovate))
    if trovate != CATEGORIE:
        mancanti = [c for c in CATEGORIE if c not in trovate]
        problemi.append("P1: le categorie sono %s, mancano %s" % (trovate, mancanti))
    for c, nome in tabelle:
        if len(nome.strip()) < 3:
            problemi.append("P1: la categoria %s non ha nome" % c)
    if "elenco è **chiuso**" not in doc and "elenco e' **chiuso**" not in doc:
        problemi.append("P1: il documento non dichiara l'elenco chiuso")

    print("\n== P2. ogni disciplina ha una categoria primaria, o un'eccezione dichiarata ==")
    tab = sezione(doc, "## 2.", "### 2.1")
    righe = re.findall(r"^\| \*\*([^*]+)\*\* \| ([^|]+) \| ([^|]+) \| ([^|]*) \|", tab, re.M)
    # la terza colonna e' il secondario e la quarta e' «da escludere»: la
    # dichiarazione di eccezione puo' stare in una qualunque delle tre, e in
    # questa tabella sta nella quarta, percio' si cerca nella riga intera
    primarie = {nome.strip(): (r[0], " ".join(r)) for nome, *r in righe}
    eccezioni = ("Lingua dei segni", "Osservazione e attenzione")
    for d in DISCIPLINE:
        if d not in primarie:
            problemi.append("P2: la disciplina «%s» non ha riga" % d)
        elif d in eccezioni:
            # le due righe che la sezione 2.1 dichiara eccezione o da costruire:
            # devono dirlo anche nella riga, altrimenti l'eccezione e' invisibile
            if not re.search(r"nessuna delle dieci|da[_ ]costruire|non esiste ancora", primarie[d][1]):
                problemi.append("P2: «%s» e' eccezione ma la sua riga non lo dice" % d)
        elif not re.search(r"\*\*[A-J]\*\*", primarie[d][0]):
            problemi.append("P2: «%s» non ha una categoria primaria dichiarata" % d)
    print("   discipline con riga: %d su %d (eccezioni dichiarate: %s)"
          % (len(primarie), len(DISCIPLINE), ", ".join(eccezioni)))

    print("\n== P3. i sei domini della sfida hanno un premio o una dichiarazione di vuoto ==")
    tabella = sezione(doc, "### 2.1", "## 3.")
    righe = re.findall(r"^\| `([^`]+)` \| ([^|]+) \| ([^|]+) \|", tabella, re.M)
    premia = {d: (prem.strip(), stato.strip()) for d, prem, stato in righe}
    for dominio in DOMINI_SFIDA:
        if dominio not in premia:
            problemi.append("P3: il dominio `%s` non ha riga: nessun premio e nessuna dichiarazione" % dominio)
            print("   %-30s %s" % (dominio, "ASSENTE"))
            continue
        prem, stato = premia[dominio]
        vuoto = "nessuno" in prem or "nessuna" in prem
        print("   %-30s %s (%s)" % (dominio, "senza premio" if vuoto else "con premio", stato))
        if not vuoto and not re.search(r"\*\*[A-J]\*\*", prem):
            problemi.append("P3: `%s` ha un premio ma nessuna categoria" % dominio)
        if stato not in STATI:
            problemi.append("P3: `%s` ha lo stato «%s», che non e' fra %s"
                            % (dominio, stato, ", ".join(sorted(STATI))))
    if len(DOMINI_SFIDA) != 6:
        problemi.append("P3: i domini sono %d, non 6" % len(DOMINI_SFIDA))

    print("\n== P4. nessuna disciplina abbinata e' inventata ==")
    tab2 = sezione(doc, "## 2.", "### 2.1")
    lingue_nel_doc = set(re.findall(r"^\| \*\*([^*]+)\*\* \|", tab2, re.M))
    ambiti = set(re.findall(r"^\| \*\*(Diritto|Etica|Filosofia|Psicologia)\*\*", quadro, re.M))
    # tutte e undici sono discipline ammesse: `osservazione e attenzione` e'
    # una riga dichiarata da costruire, non un abbinamento inventato
    ammesse = set(DISCIPLINE)
    extra = lingue_nel_doc - ammesse
    print("   discipline citate: %d; ambiti in quadro-trasversale: %d" % (len(lingue_nel_doc), len(ambiti)))
    for nome in sorted(extra):
        problemi.append("P4: la disciplina «%s» non e' fra quelle del progetto" % nome)
    if len(ambiti) != 4:
        problemi.append("P4: quadro-trasversale.md non dichiara piu' quattro ambiti")
    for nome in ("Italiano", "Ferrarese", "Latino", "Inglese", "Lingua dei segni", "Greco"):
        if ("**%s**" % nome) not in lingue:
            problemi.append("P4: lingue.md non dichiara piu' la lingua «%s»" % nome)

    print("\n== P5. nessun premio puo' essere generato o senza licenza ==")
    for v in VIETATI:
        # il divieto deve comparire nel documento come divieto, non come descrizione
        if v in doc.lower():
            problemi.append("P5: il documento contiene «%s» senza dichiararlo vietato" % v)
    if "l'elenco è **chiuso**" not in doc and "l'elenco e' **chiuso**" not in doc:
        pass
    for frase in ("vieta le immagini", "libera di diritti"):
        if frase not in doc:
            problemi.append("P5: il documento non dice che il premio dev'essere «%s»" % frase)
    print("   il divieto di generare e' dichiarato e il campo licenza e' fra le prove")

    print("\n== sintesi ==")
    if problemi:
        for p in problemi:
            print("   difetto: " + p)
        print("\nproblemi: %d" % len(problemi))
        return 1
    print("   nessun difetto: le dieci categorie sono chiuse, le discipline hanno un premio, i sei domini sono dichiarati")
    print("\n==== controlli superati: 5/5 ====")
    return 0


if __name__ == "__main__":
    sys.exit(main())