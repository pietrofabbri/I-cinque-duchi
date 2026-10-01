"""Controlla la coerenza del repository: versioni, riferimenti, cifre dichiarate.

Un progetto con diciotto documenti e ventitré file di dati invecchia in un modo
particolare: non in quel che dice, ma in quel che **non si aggiorna**. Una
tabella che punta alla versione 0.1 di un documento che è già alla 0.2 non è
sbagliata in sé: è semplicemente rimasta indietro, e il lettore non ha modo di
saperlo.

Perciò qui si controllano quattro cose, e tutte e quattro solo cose che si possono
controllare senza giudicare:

1. **le versioni**: ogni riferimento «documento.md (vN.N)» deve combaciare con
   l'intestazione YAML del documento, e la tabella del `README.md` deve
   combaciare anch'essa;
2. **i file citati**: ogni percorso che un documento promette deve esistere — con
   due eccezioni dichiarate, perché sono due cose diverse: il file **da produrre**
   (la differenza fra «non esiste» e «non esiste ancora» è tutta la differenza) e
   il file che sta **solo sul ramo remoto** quando il checkout è parziale;
3. **le cifre dichiarate**: quando un documento scrive «30 citazioni, 82 versi,
   0 problemi» o «95 luoghi» o «169 ritratti», la cifra deve uscire dai dati;
4. **le tappe**: le trenta del quinto anno esistono nella tabella di
   `anno5-mondo.md` e hanno ciascuna una persona.

Uso:  python3 verifica_coerenza.py
      python3 verifica_coerenza.py --solo versioni
      python3 verifica_coerenza.py --elenco /tmp/albero.txt

L'opzione `--elenco` serve quando il checkout è parziale: il file è l'elenco dei
percorsi del repository (uno per riga, come l'output di `gh api … /git/trees`),
e serve perché un controllo che dice «manca `prototipo/index.html`» quando il
file c'è sul ramo è un controllo che non viene letto.
"""
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(RADICE, "docs")
DATI = os.path.join(RADICE, "dati")

# verbi e formule che, nella stessa frase, dichiarano che il file non deve ancora
# esistere. Solo all'infinito presente: «i fogli sono prodotti» non è una
# dichiarazione di futuro, e una parola che può volgere due sensi fa da schermo.
FUTURO = re.compile(r"\b(da produrre|da generare|da costruire|da definire|da creare|"
                     r"da scaricare|da rifare|ancora da|non è ancora stato|"
                     r"non esistono ancora|non esiste ancora|"
                     r"produrre|generare|costruire|definire|scaricare|rifare)\b")


def frasi(testo, posizione):
    """Il paragrafo che contiene una citazione: il contesto minimo per giudicarla.

    Il paragrafo e non la riga, perché nei documenti di questo progetto la
    riga va a capo a ottantacinque caratteri e una dichiarazione come «da
    produrre» finisce quasi sempre sulla riga dopo.
    """
    inizio = testo.rfind("\n\n", 0, posizione) + 2
    fine = testo.find("\n\n", posizione)
    return testo[inizio:fine if fine > 0 else len(testo)]


def esiste(percorso, lontano):
    """Il file c'è qui, o c'è nel ramo. L'elenco arriva dalla riga di comando."""
    return os.path.exists(os.path.join(RADICE, percorso)) or percorso in lontano


def senza_registro(testo):
    """Il testo di un documento senza il registro delle modifiche.

    Il registro racconta **come era** il documento quando l'avevano scritto, e le
    sue cifre sono quelle di allora: controllarle come se fossero cifre di adesso
    produrrebbe un falso allarme su ogni versione che ha cambiato un numero. Il
    registro si controlla a mano, perché il suo compito è proprio ricordare il
    passato.
    """
    m = re.search(r"^#+ .*[Rr]egistro", testo, re.M)
    return testo[:m.start()] if m else testo


def versioni_reali():
    """nome file -> versione, letta dall'intestazione YAML."""
    out = {}
    for nome in sorted(os.listdir(DOCS)):
        if not nome.endswith(".md"):
            continue
        percorso = os.path.join(DOCS, nome)
        testo = open(percorso, encoding="utf-8").read(2000)
        if not testo.startswith("---"):
            out[nome] = None
            continue
        m = re.search(r"^versione:\s*(\S+)\s*$", testo, re.M)
        out[nome] = m.group(1) if m else None
    return out


def controlla_versioni(ver):
    problemi = []
    # (a) la tabella del README
    readme = open(os.path.join(RADICE, "README.md"), encoding="utf-8").read()
    for nome, v in re.findall(r"\| `?([\w./-]+\.md)`? \|[^|]*\| *([\d.]+) *\|", readme):
        if nome.startswith("docs/"):
            continue
        reale = ver.get(nome)
        if reale is None:
            problemi.append("README: %s non è fra i documenti di docs/" % nome)
        elif reale != v:
            problemi.append("README: tabella dice %s v%s, il documento è v%s" % (nome, v, reale))
    # (b) i riferimenti incrociati dentro i documenti e nelle guide
    tutti = {n: open(os.path.join(DOCS, n), encoding="utf-8").read() for n in ver}
    percorso = dict(tutti)
    percorso["README.md"] = readme
    percorso["AGENTS.md"] = open(os.path.join(RADICE, "AGENTS.md"), encoding="utf-8").read()
    percorso["FONTI-E-LICENZE.md"] = open(os.path.join(RADICE, "FONTI-E-LICENZE.md"),
                                           encoding="utf-8").read()
    for chi, testo in percorso.items():
        for nome, v in re.findall(r"(videogioco-5-duchi-[\w-]+\.md)\s*\((v[\d.]+)\)", testo):
            reale = ver.get(nome)
            if reale is None:
                problemi.append("%s: cita %s, che non è fra i documenti" % (chi, nome))
            elif reale != v[1:]:
                problemi.append("%s: cita %s %s, il documento è v%s" % (chi, nome, v, reale))
    return problemi


def controlla_file(lontano=frozenset()):
    """Ogni percorso di file che un documento promette deve esistere.

    Tre esiti e non due: il file c'è, il file è **dichiarato come da produrre**
    nella stessa frase, o il file non c'è e nessuno lo aveva detto. Il secondo
    caso non è un problema: è un progetto, e un progetto che non ha ancora fatto
    una cosa deve poterlo scrivere.
    """
    problemi = []
    candidati = []
    for nome in sorted(os.listdir(DOCS)):
        if nome.endswith(".md"):
            candidati.append((nome, open(os.path.join(DOCS, nome), encoding="utf-8").read()))
    candidati.append(("README.md", open(os.path.join(RADICE, "README.md"), encoding="utf-8").read()))
    candidati.append(("AGENTS.md", open(os.path.join(RADICE, "AGENTS.md"), encoding="utf-8").read()))
    for chi, testo in candidati:
        for percorso in set(re.findall(r"`((?:sorgenti|dati|docs|prototipo)/[\w./-]+)`", testo)):
            pulito = percorso.rstrip(".,;:")
            if "*" in pulito or pulito.endswith("/"):
                continue
            if esiste(pulito, lontano):
                continue
            dove = testo.find("`%s`" % percorso)
            frase = frasi(testo, dove) if dove >= 0 else ""
            if FUTURO.search(frase.lower()):
                continue
            problemi.append("%s: il file `%s` non esiste e nessuno lo dichiara come "
                            "da produrre" % (chi, pulito))
    return problemi


def controlla_cifre():
    """Le cifre scritte nei documenti contro i dati.

    Non solo i numeri con le cifre: anche quelli in lettere. «quindici `A`, dieci
    `S`, cinque `I`» è una cifra come «82», ed è quella che un umano dimentica
    più spesso, perché si corregge una parola e non ci si accorge che il conteggio
    è cambiato.
    """
    problemi = []
    PAROLE = {"uno": 1, "due": 2, "tre": 3, "quattro": 4, "cinque": 5, "sei": 6,
              "sette": 7, "otto": 8, "nove": 9, "dieci": 10, "quindici": 15,
              "sedici": 16, "trenta": 30, "quarantasei": 46}

    # i luoghi del gioco
    with open(os.path.join(DATI, "luoghi_gioco.json"), encoding="utf-8") as f:
        luoghi = json.load(f)
    righe = luoghi["luoghi"] if isinstance(luoghi, dict) else luoghi
    distinti = {r.get("luogo") or r.get("nome") for r in righe}
    quanti = len(distinti)
    for nome, testo in ((n, open(os.path.join(DOCS, n), encoding="utf-8").read())
                        for n in os.listdir(DOCS) if n.endswith(".md")):
        for dichiarato in re.findall(r"i (\d+) luoghi del gioco", testo):
            if int(dichiarato) != quanti:
                problemi.append("%s: dichiara %s luoghi, i dati ne hanno %d"
                                % (nome, dichiarato, quanti))

    # le citazioni del Furioso
    percorso = os.path.join(DATI, "furioso", "citazioni.json")
    if os.path.exists(percorso):
        with open(percorso, encoding="utf-8") as f:
            cit = json.load(f)
        righe = cit["citazioni"]
        tappe = len({r["tappa"] for r in righe})
        versi = sum(len(r["versi"]) for r in righe)
        for nome in os.listdir(DOCS):
            if not nome.endswith(".md"):
                continue
            testo = open(os.path.join(DOCS, nome), encoding="utf-8").read()
            for a, b in re.findall(r"(\d+) citazioni, (\d+) versi", testo):
                if (int(a), int(b)) != (tappe, versi):
                    problemi.append("%s: dichiara %s citazioni e %s versi, i dati sono %d e %d"
                                    % (nome, a, b, tappe, versi))
        # la distribuzione dei legami, che nei documenti è scritta in lettere
        conta = {}
        for r in righe:
            conta[r["legame"]] = conta.get(r["legame"], 0) + 1
        for nome in os.listdir(DOCS):
            if not nome.endswith(".md"):
                continue
            testo = senza_registro(open(os.path.join(DOCS, nome), encoding="utf-8").read())
            for gruppo in re.findall(r"((?:[a-zà-ù]+ )?`([BSICA])`, ?(?:[a-zà-ù]+ )?`([BSICA])`,"
                                     r" ?(?:[a-zà-ù]+ )?`([BSICA])`)", testo):
                parole = re.findall(r"[a-zà-ù]+", gruppo[0])
                for parola, tipo in zip(parole, gruppo[1:]):
                    if parola in PAROLE and conta.get(tipo, 0) != PAROLE[parola]:
                        problemi.append("%s: dichiara %s legami `%s`, i dati sono %d"
                                        % (nome, parola, tipo, conta.get(tipo, 0)))
    return problemi


def controlla_tappe():
    """Ogni tappa dell'anno 5 citata deve esistere nella tabella di anno5-mondo.md.

    E le trenta devono essere proprio quelle: `5-31` non è una tappa, e una tappa
    che sparisce dalla tabella mentre resta nel JSON è una tappa che il gioco
    promette e non consegna.
    """
    problemi = []
    con = open(os.path.join(DOCS, "videogioco-5-duchi-anno5-mondo.md"), encoding="utf-8").read()
    tappe = set(re.findall(r"\b(5-\d{1,2})\b", con))
    attese = {"5-%d" % i for i in range(1, 31)}
    percorso = os.path.join(DATI, "furioso", "citazioni.json")
    if os.path.exists(percorso):
        with open(percorso, encoding="utf-8") as f:
            cit = json.load(f)
        citate = {r["tappa"] for r in cit["citazioni"]}
        for r in cit["citazioni"]:
            if r["tappa"] not in tappe:
                problemi.append("citazioni.json: la tappa %s non compare in anno5-mondo.md"
                                % r["tappa"])
        if citate != attese:
            problemi.append("citazioni.json: le tappe sono %d e non le tranne attese "
                            "(%s)" % (len(citate), ", ".join(sorted(attese ^ citate))))
        mancanti = attese - tappe
        if mancanti:
            problemi.append("anno5-mondo.md: non ci sono le righe delle tappe %s"
                            % ", ".join(sorted(mancanti)))
    return problemi


def controlla_personaggi():
    """Ogni tappa deve avere un personaggio: è la regola di `luoghi.md`."""
    problemi = []
    con = open(os.path.join(DOCS, "videogioco-5-duchi-anno5-mondo.md"), encoding="utf-8").read()
    righe = re.findall(r"^\| \*\*(5-\d{1,2})\*\* \|(.+)$", con, re.M)
    for tappa, resto in righe:
        colonne = [c.strip() for c in resto.split("|")]
        if len(colonne) < 5 or not colonne[3]:
            problemi.append("anno5-mondo.md: la riga di %s non ha il personaggio" % tappa)
    if len(righe) != 30:
        problemi.append("anno5-mondo.md: %d righe di tappa nella tabella, attese 30" % len(righe))
    return problemi


if __name__ == "__main__":
    ver = versioni_reali()
    insiemi = [("versioni", controlla_versioni(ver))]
    if "--solo" not in sys.argv:
        lontano = frozenset()
        if "--elenco" in sys.argv:
            percorso = sys.argv[sys.argv.index("--elenco") + 1]
            lontano = frozenset(r.strip() for r in open(percorso, encoding="utf-8")
                                if r.strip())
        insiemi += [("file citati", controlla_file(lontano)),
                    ("cifre dichiarate", controlla_cifre()),
                    ("tappe dell'anno 5", controlla_tappe()),
                    ("personaggi obbligatori", controlla_personaggi())]
    totale = 0
    for nome, problemi in insiemi:
        print("%-24s %d" % (nome, len(problemi)))
        for p in problemi:
            print("   " + p)
        totale += len(problemi)
    print("\nproblemi di coerenza: %d" % totale)
    sys.exit(1 if totale else 0)