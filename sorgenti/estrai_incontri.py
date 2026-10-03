"""Estrae gli **incontri** dei centocinquanta livelli dalle tabelle degli anni.

Che cosa fa, in una riga: per ogni tappa dice **chi è la voce** (l'obbligatorio che
il giocatore incontra), **chi sono i facoltativi** che lo aspettano nella stessa
stanza, **dove** e **con quale mezzo** ci si arriva. È il dato che mancava: i
progetti hanno le tappe, hanno i luoghi, hanno i mezzi, ma non avevano mai messo
insieme **le tre cose in una riga per tappa**, cioè l'itinerario.

**Perché le colonne si leggono per intestazione e non per numero.** Il quinto
anno ha una colonna in più rispetto al secondo — la stanza, fra il pin e la voce
— e l'anno 1 ha una tabella tutta sua, senza il grassetto e con una colonna in più
per l'aggancio. Contare le barre, come faceva `estrai_luoghi.py` fino al 2
ottobre, ha già prodotto un difetto in ventinove tappe su trenta: la trappola è
silenziosa, perché la riga resta lunga uguale e nessuno se ne accorge. Qui la
colonna cercata si cerca **per nome**, e se non c'è la riga viene **saltata e
detta**, non interpretata a tentativi.

**Le tre cose che l'estrattore non può fare, e che dichiara.**

- **Il mezzo non è nelle tabelle.** Le tappe dicono dove, non come si arriva: il
  mezzo è in `percorsi.md` §1, con il suo anno di attestazione, ed è una scelta per
  tappa. Qui viene messo un **mezzoProposed** dichiarato come tale, non un dato:
  l'estrattore non inventa collegamenti, e ogni giudizio sul mezzo resta al motore
  (`percorsi_calcola.py`), che ha le distanze.
- **La distanza fra tappe non si calcola qui.** Ci vuole il punto, e il punto sta
  in `dati/luoghi_gioco.json`. Questo file dice **chi incontra chi e dove**, non
  quanto ci si mette.
- **La facoltatività non è sempre dichiarata.** Dove la colonna c'è, si legge;
  dove non c'è, il campo resta `None` e vuol dire **non dichiarato**, che è diverso
  da «nessuna». Un campo che vale `[]` e un campo che non c'è non si confondono.

Uso:
    python3 sorgenti/estrai_incontri.py            # scrive il file
    python3 sorgenti/estrai_incontri.py --prova    # dice, non scrive
"""
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(RADICE, "docs")
USCITA = os.path.join(RADICE, "dati", "incontri_livelli.json")

# Il mezzo che il motore dovrebbe usare per ciascun anno, perche' e' quello che i
# documenti indicano come dominante. `None` vuol dire **non dichiarato**: il quinto
# anno non ha un mezzo solo, e sceglierne uno sarebbe inventarlo.
MEZZO_DICHIARATO = {
    1: "a_piedi",
    2: "cavallo",
    3: "cavallo",
    4: "nave",
    5: None,
}

# Le tabelle, e le colonne da cercare. Il nome della colonna e' il dato: se un
# giorno un documento la rinomina, la riga viene saltata e detta, non letta a caso.
TABELLE = [
    {"anno": 1, "file": "videogioco-5-duchi-anno1-mappa.md", "riga": "| Tappa |",
     "voce": "Personaggio", "luogo": "Luogo (indirizzo)", "facoltativi": "Facoltativi"},
    {"anno": 2, "file": "videogioco-5-duchi-anno2-penisola.md", "riga": "| Livello |",
     "voce": "Voce", "luogo": "Luogo (pin)", "facoltativi": "Facoltativi (2)"},
    {"anno": 3, "file": "videogioco-5-duchi-anno3-europa.md", "riga": "| Livello |",
     "voce": "Voce", "luogo": "Luogo (pin)", "facoltativi": "Facoltativi (2)"},
    {"anno": 4, "file": "videogioco-5-duchi-anno4-mondo.md", "riga": "| Livello |",
     "voce": "Voce", "luogo": "Pin", "facoltativi": "Facoltativi (2)"},
    {"anno": 5, "file": "videogioco-5-duchi-anno5-mondo.md", "riga": "| Livello |",
     "voce": "Voce", "luogo": "Pin (dove siamo oggi)", "facoltativi": "Facoltativi",
     "in_colonna": "Stanza (dove sta accadendo)"},
]

# La voce e' un nome proprio fra parentesi con un codice: **Ötzi** (Q01). Il
# codice e' l'unico identificatore stabile, il nome si puo' scrivere in due modi.
VOCE = re.compile(r"\*\*(?P<nome>[^*]+?)\*\*\s*(?:\((?P<codice>P\d+|Q\d+)\))?")

PERSONAGGI_1 = os.path.join(RADICE, "dati", "videogioco-5-duchi-anno1-personaggi.json")


# La voce collettiva e' **marcata nei documenti**: la casella della voce porta la
# parola «collettivo» seguita dal codice di attendibilita' (anni 2-5 §5:
# "`collettivo` = voce senza nome proprio, con attendibilita' `C`"). Questa e'
# la prova buona, e viene prima di ogni'altra; la maiuscola e' solo il ripiego
# per quando la marcatura manca, e va detto quale delle due ha deciso.
MARCATURA_COLLETTIVO = re.compile(r"collettiv[oi]", re.I)


def _classifica(casella, nome, codice):
    """Il tipo di una voce e **quale prova** lo ha deciso.

    Le quattro prove, in ordine: la marcatura scritta a mano nella tabella, il
    codice, il catalogo dei 93 nomi dell'anno 1, l'iniziale. Ogni risultato dice
    quale ha deciso, cosi' che un nome classificato male si vede subito.
    """
    if casella and MARCATURA_COLLETTIVO.search(casella):
        return "collettivo", "marcatura_nella_tabella"
    if codice:
        return "personaggio", "codice"
    if nome in NOMI_NOTI:
        return "personaggio", "catalogo_anno1"
    if nome and nome[0].isupper():
        return "personaggio", "iniziale_maiuscola"
    return "collettivo", "iniziale_minuscola"


def _nomi_noti():
    """I nomi propri che il progetto conosce, per non scambiare un nome per una voce.

    Il file dell'anno 1 porta i 93 personaggi con il loro codice. Gli anni 2-5
    usano la serie `Q` e non hanno un catalogo analogo, quindi per quegli anni il
    confronto non puo' essere completo: **e' un limite dichiarato, non un fatto**.
    Un nome che non e' in elenco non viene dichiarato collettivo per questo, ma
    resta comunque con `codice` null, e il documento lo dice.
    """
    try:
        d = json.load(open(PERSONAGGI_1, encoding="utf-8"))
    except Exception:                                       # noqa: BLE001
        return set()
    return {p["nome"] for p in d.get("personaggi", []) if p.get("nome")}


NOMI_NOTI = _nomi_noti()


# I facoltativi sono separati da `;` quasi sempre, e ogni nome puo' avere il suo
# codice. Si tiene anche il testo intero, perche' qualche voce e' collettiva e non
# ha nessun codice da prendere.
def facoltativi(testo):
    """I facoltativi di una tappa, o None se la colonna non c'era."""
    if testo is None:
        return None
    testo = testo.strip()
    if not testo or testo in ("—", "-", "–"):
        return []
    out = []
    for pezzo in re.split(r"[;·]", testo):
        pezzo = pezzo.strip().strip("*").strip()
        if not pezzo:
            continue
        # La marcatura di facoltativita' sta dentro le parentesi accanto al nome
        # («Ibn Khaldun (facoltativa forte)», «Cesare (ritorno)»): va tolta dal
        # nome e tenuta come nota, altrimenti il nome del personaggio porta
        # dentro una frase che non e' il suo nome.
        nota = None
        mn = re.search(r"\((?P<nota>[^)]{3,})\)\s*$", pezzo)
        if mn and not re.match(r"^(P|Q)\d+$", mn.group("nota")):
            nota = mn.group("nota").strip()
            pezzo = pezzo[:mn.start()].strip()
        m = VOCE.search(pezzo)
        nome = (m.group("nome") if m else pezzo).strip()
        codice = m.group("codice") if m else None
        # Una voce collettiva e' una voce **senza nome proprio** (anni 2-5 §5:
        # "viene per non scaricare su una persona un argomento tecnico"), e non
        # una voce il cui nome sembra strano. Il test e' sull'elenco dei nomi
        # noti, non sull'aspetto della parola: «i monaci buddisti» e «Cesare»
        # si somigliano e sono due cose opposte.
        tipo, prova = _classifica(pezzo, nome, codice)
        out.append({"nome": nome, "codice": codice, "nota": nota,
                    "tipo": tipo, "prova": prova,
                    "facoltativa": tipo == "collettivo"
                                   or (codice or "").startswith("P")})
    return out


def intestazione(testo):
    """Le colonne della tabella, ripulite dai marcatori del grassetto."""
    return [c.strip().strip("*").strip() for c in testo.strip().strip("|").split("|")]


def main():
    prova = "--prova" in sys.argv
    righe = []
    saltate = []

    for tab in TABELLE:
        path = os.path.join(DOCS, tab["file"])
        testo = open(path, encoding="utf-8").read().split("\n")
        # l'intestazione: la prima riga che contiene il marcatore della tabella
        i = next((k for k, r in enumerate(testo) if tab["riga"] in r), None)
        if i is None:
            saltate.append("anno %d: non trovo l'intestazione %r in %s"
                           % (tab["anno"], tab["riga"], tab["file"]))
            continue
        colonne = intestazione(testo[i])
        indice = {}
        for chiave in ("voce", "luogo", "facoltativi", "in_colonna"):
            if chiave in tab and tab[chiave] not in colonne:
                saltate.append("anno %d: la colonna %r non c'è (ci sono %s)"
                               % (tab["anno"], tab[chiave], ", ".join(colonne)))
                indice[chiave] = None
                continue
            indice[chiave] = colonne.index(tab[chiave]) if chiave in tab else None

        # il livello sta nella prima colonna, in tutti e cinque gli anni
        for k in range(i + 2, len(testo)):
            r = testo[k]
            if not r.startswith("|"):
                break
            celle = [c.strip() for c in r.strip().strip("|").split("|")]
            m = re.match(r"^\**(\d-\d+)\**$", celle[0])
            if not m:
                if len(celle) != len(colonne):
                    saltate.append("anno %d riga %d: %d celle contro %d colonne"
                                   % (tab["anno"], k + 1, len(celle), len(colonne)))
                continue
            liv = m.group(1)
            if len(celle) != len(colonne):
                saltate.append("anno %d tappa %s: %d celle contro %d colonne"
                               % (tab["anno"], liv, len(celle), len(colonne)))
                continue

            def _idx(chiave):
                j = indice.get(chiave)
                return None if (j is None or j >= len(celle)) else j

            jv = _idx("voce")
            grezza = celle[jv] if jv is not None else None
            vm = VOCE.search(grezza or "")
            voce = {"nome": (vm.group("nome") if vm else (grezza or "")).strip(),
                    "codice": vm.group("codice") if vm else None}
            if voce["codice"] is None and not voce["nome"]:
                saltate.append("anno %d tappa %s: nessuna voce" % (tab["anno"], liv))
            # La regola e' quella dichiarata nei documenti degli anni: una voce
            # `collettivo` e' **senza nome proprio** («i copisti e gli
            # amanuensi», «la strada della fuga di Rinaldo»), e `personaggio` e'
            # un nome proprio. Il catalogo dei 93 nomi dell'anno 1 e' la prova
            # piu' forte quando c'e'; per gli anni 2-5, che non hanno catalogo,
            # la prova e' l'iniziale maiuscola, che e' la convenzione dei
            # documenti e non un'ipotesi: si dichiara nel file come `prova`.
            voce["tipo"], voce["prova"] = _classifica(grezza, voce["nome"],
                                                       voce["codice"])

            righe.append({
                "livello": liv,
                "anno": tab["anno"],
                "argomento": celle[1] if len(celle) > 1 else "",
                "luogo": celle[_idx("luogo")] if _idx("luogo") is not None else None,
                "stanza": celle[_idx("in_colonna")] if _idx("in_colonna") is not None else None,
                "voce_obbligatoria": voce,
                "facoltativi": facoltativi(celle[_idx("facoltativi")] if _idx("facoltativi") is not None else None),
                "mezzo": MEZZO_DICHIARATO[tab["anno"]],
                "mezzo_stato": "dichiarato" if MEZZO_DICHIARATO[tab["anno"]]
                               else "non_dichiarato",
            })

    # il conto, che e' la parte che serve
    per_anno = {}
    for r in righe:
        a = per_anno.setdefault(r["anno"], {"tappe": 0, "facoltativi": 0,
                                            "voci_nominali": 0, "facoltative_nominali": 0})
        a["tappe"] += 1
        a["facoltativi"] += len(r["facoltativi"] or [])
        if r["voce_obbligatoria"]["codice"]:
            a["voci_nominali"] += 1
        for f in r["facoltativi"] or []:
            if f["facoltativa"]:
                a["facoltative_nominali"] += 1

    print("tappe lette: %d" % len(righe))
    for anno in sorted(per_anno):
        a = per_anno[anno]
        print("  anno %d: %d tappe, %d facoltativi (%d con codice)"
              % (anno, a["tappe"], a["facoltativi"], a["facoltative_nominali"]))
    if saltate:
        print("\nSALTATE %d:" % len(saltate))
        for s in saltate[:20]:
            print("  " + s)

    out = {
        "versione": 1,
        "data": "2026-10-03",
        "scopo": "gli incontri dei centocinquanta livelli: chi e' la voce "
                 "obbligatoria, chi sono i facoltativi, dove, e con quale mezzo",
        "come_si_estrae": "colonne per intestazione dalle tabelle delle tappe "
                          "degli anni 1-5, mai per numero: il quinto anno ha una "
                          "colonna in piu' (la stanza) e l'anno 1 ne ha un'altra "
                          "(l'aggancio)",
        "avvertenza_mezzo": "il mezzo e' quello dichiarato per anno in "
                            "percorsi.md §1, e per il quinto anno NON e' "
                            "dichiarato: ci sono ventidue mezzi e la scelta e' "
                            "del motore, che ha le distanze",
        "avvertenza_voce": "una voce senza codice puo' essere collettiva (una "
                           "macchina, gli ingegneri delle reti) e allora non ha "
                           "scheda: il campo `codice` vale null e va detto",
        "mezzo_dichiarato": MEZZO_DICHIARATO,
        "tappe": len(righe),
        "per_anno": {str(k): v for k, v in sorted(per_anno.items())},
        "saltate": len(saltate),
        "incontri": righe,
    }

    if prova:
        print("--prova: non scrivo")
        return 0
    with open(USCITA, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("scritto %s" % os.path.relpath(USCITA, RADICE))
    return 0


if __name__ == "__main__":
    sys.exit(main())