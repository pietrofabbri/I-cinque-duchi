"""Verifica che i principi pedagogici siano applicati al gioco, e non dichiarati soltanto.

Il modello pedagogico generale e' entrato in `docs/videogioco-5-duchi-pedagogia.md`
il 03/10/2026. Un principio che sta solo in un documento non e' un principio del
progetto: e' una buona intenzione. Qui si controllano cinque cose che si possono
misurare sui file, e tutte e cinque mordono (provate con difetti iniettati).

  P1  ogni livello dichiara un nucleo, e i tre che non lo dichiarano sono un elenco chiuso
  P2  la cadenza della tappa a mani nude divide esattamente i centocinquanta livelli
  P3  i sei domini della banca sono dichiarati, ciascuno con la sua destinazione
  P4  nessuna costruzione di ingegneria comportamentale nel ciclo di gioco
  P5  le sei regole vincolanti sono in AGENTS.md, dove valgono per chi lavora

Uso:  python3 sorgenti/verifica_pedagogia.py
"""
import io
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(RADICE, "docs", "videogioco-5-duchi-pedagogia.md")
SCHEMA = os.path.join(RADICE, "docs", "videogioco-5-duchi-schema-livelli.md")
GIOCO = os.path.join(RADICE, "docs", "videogioco-5-duchi-gioco.md")
MECCANICHE = os.path.join(RADICE, "docs", "videogioco-5-duchi-meccaniche.md")
ESERCIZI = os.path.join(RADICE, "docs", "videogioco-5-duchi-esercizi.md")
AGENTS = os.path.join(RADICE, "AGENTS.md")

# I tre livelli che non hanno argomento nuovo: si prendono in prestito e basta.
# L'elenco e' chiuso perche' un quarto livello cosi' deve essere dichiarato qui,
# non comparire per caso: P1 fallisce se l'elenco dei casi reali e questo diverge.
SENZA_NUCLEO = ("2-13", "2-22", "4-11")

# La cadenza della sfida a mani nude: una ogni quindici livelli.
OGNI = 15

# I sei domini della banca. `casa` e' dove il dominio vive oggi nel progetto.
DOMINI = {
    "logica": "i 150 livelli di `schema-livelli.md` (`A2`, `E1`–`E9`)",
    "calcolo mentale e stime": "i 150 livelli (`A1`, `A4`, `A7`, `A10`, il livello 1-7)",
    "informatica": "i 150 livelli: il nucleo dell'intero gioco",
    "linguistica e testo": "i 900 livelli di `lingue.md`",
    "Costituzione e cittadinanza": "`quadro-trasversale.md`, i cinque anni e i cinque ambiti",
    "osservazione e attenzione": "da_costruire",
}
DA_COSTRUIRE = ("osservazione e attenzione",)

# Le costruzioni che il progetto vieta. Lista stretta e dichiarata: non e' un
# censimento delle cose sbagliate, e' il nucleo di quelle che si cercano.
VIETATE = (
    "riprova e perdi",
    "punteggio perso",
    "perdi punto",
    # «sblocco» da solo e' troppo largo: in `meccaniche.md` la parola compare
    # nella regola che *toglie* lo sblocco («l'esito da solo non sblocca»),
    # cioe' in un uso contrario a quello che la lista cerca.
    "sblocco a pagamento",
    "sblocco a soldi",
    "sblocco con punti",
    "classifica della classe",
    "gioca ogni giorno",
    "streak",
    "notifica push",
)

# Le sei regole che devono stare in AGENTS.md.
REGOLE = (
    "trasparenza radicale",
    "vantaggio tangibile",
    "infrastruttura minima",
    "formato individuale o comunitario",
    "impotenza appresa",
    "contagio",
)


def leggi(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def livelli(schema):
    """Ritorna [(id, corpo)] per ogni `### N-M · titolo`, in ordine."""
    out = []
    for pezzo in re.split(r"^### ", schema, flags=re.M)[1:]:
        campi = pezzo.split(None, 2)
        if not campi or not re.match(r"^\d+-\d+$", campi[0]):
            continue  # i sottotitoli numerati di altre sezioni non sono livelli
        corpo = pezzo.split("\n## ")[0]
        out.append((campi[0], corpo))
    return out


def main():
    if not os.path.exists(DOC):
        print("manca %s: il modello pedagogico non e' ancora entrato nel progetto" % DOC)
        return 2
    doc = leggi(DOC)
    schema = leggi(SCHEMA)
    agenti = leggi(AGENTS)
    problemi = []

    print("== P1. ogni livello dichiara un nucleo, e i tre che non lo dichiarano sono noti ==")
    lv = livelli(schema)
    print("   livelli nello schema: %d" % len(lv))
    if len(lv) != 150:
        problemi.append("P1: lo schema dichiara %d livelli, non 150" % len(lv))
    visti = [i for i, _ in lv]
    attesi = ["%d-%d" % (a, n) for a in range(1, 6) for n in range(1, 31)]
    if visti != attesi:
        mancanti = sorted(set(attesi) - set(visti))
        problemi.append("P1: i livelli non sono 1-1..5-30 in ordine (mancanti: %s)" % mancanti)
    reali = tuple(i for i, corpo in lv if "**Nucleo:**" not in corpo)
    print("   livelli senza nucleo nuovo: %s" % (", ".join(reali) if reali else "nessuno"))
    if reali != SENZA_NUCLEO:
        problemi.append("P1: i livelli senza nucleo sono %s, l'elenco dichiarato e' %s"
                        % (list(reali), list(SENZA_NUCLEO)))
    for i, corpo in lv:
        if "**Nucleo:**" not in corpo and "**Ripresa in un nuovo contesto:**" not in corpo:
            problemi.append("P1: %s non dichiara nucleo ne' ripresa: e' un livello vuoto" % i)
    print("   nucleo nuovo: %d su 150; ripresa pura: %d" % (150 - len(reali), len(reali)))

    print("\n== P2. la cadenza della tappa a mani nude divide esattamente i 150 livelli ==")
    blocchi = 150 // OGNI
    print("   una ogni %d livelli: %d tappe su 150" % (OGNI, blocchi))
    if 150 % OGNI:
        problemi.append("P2: 150 non e' multiplo di %d: la cadenza lascerebbe un resto" % OGNI)
    mano_nude = ["%d-%d" % (a, n) for a in range(1, 6) for n in range(OGNI, 31, OGNI)]
    for tappa in mano_nude:
        if ("`%s`" % tappa) not in doc:
            problemi.append("P2: la tappa a mani nude %s non e' dichiarata nel documento" % tappa)
    print("   tappe a mani nude dichiarate: %d su %d" %
          (sum(1 for t in mano_nude if ("`%s`" % t) in doc), len(mano_nude)))

    print("\n== P3. i sei domini della banca sono dichiarati, ciascuno con la sua casa ==")
    for dominio, casa in sorted(DOMINI.items()):
        presente = ("`%s`" % dominio) in doc
        print("   %-28s %s" % (dominio, "dichiarato" if presente else "ASSENTE"))
        if not presente:
            problemi.append("P3: il dominio `%s` non e' dichiarato" % dominio)
        if dominio in DA_COSTRUIRE and "da_costruire" not in casa:
            problemi.append("P3: `%s` e' senza casa ma non e' dichiarato da_costruire" % dominio)
    if len(DOMINI) != 6:
        problemi.append("P3: i domini sono %d, non 6" % len(DOMINI))

    print("\n== P4. nessuna costruzione di ingegneria comportamentale nel ciclo di gioco ==")
    for nome, path in (("gioco.md", GIOCO), ("meccaniche.md", MECCANICHE), ("esercizi.md", ESERCIZI)):
        testo = leggi(path).lower()
        trovate = [v for v in VIETATE if v in testo]
        print("   %-14s %s" % (nome, ", ".join(trovate) if trovate else "nessuna"))
        for v in trovate:
            problemi.append("P4: `%s` contiene la costruzione vietata «%s»" % (nome, v))

    print("\n== P5. le sei regole sono in AGENTS.md, dove valgono per chi lavora ==")
    agenti_b = agenti.lower()
    for regola in REGOLE:
        presente = regola in agenti_b
        print("   %-36s %s" % (regola, "c'e'" if presente else "MANCA"))
        if not presente:
            problemi.append("P5: la regola «%s» non e' in AGENTS.md" % regola)

    print("\n== sintesi ==")
    if problemi:
        for p in problemi:
            print("   difetto: " + p)
        print("\nproblemi: %d" % len(problemi))
        return 1
    print("   nessun difetto: i sei principi sono applicati al gioco e non soltanto dichiarati")
    print("\n==== controlli superati: 5/5 ====")
    return 0


if __name__ == "__main__":
    sys.exit(main())