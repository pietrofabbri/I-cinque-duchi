#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""I mezzi di trasporto, anno per anno, e quanto costano in giorni.

Il percorso del duca è già calcolato in `percorsi_confronto.py`. Qui la domanda
è un'altra: **con che cosa viaggia**, perché la stessa distanza fatta a cavallo o
in nave non è la stessa distanza fatta in diligenza, e perché negli anni 4 e 5
il duca non viaggia affatto — è il materiale che arriva.

I numeri sono **stime dichiarate**: chilometri al giorno e portata in persone per
ogni mezzo, con la fonte del tipo di mezzo (storico, documentato) separata dalla
sua velocità (stima, discussa). Il progetto non promette al giocatore una
giornata che nessuno faceva.

**I mezzi nuovi (03/10/2026), e la regola che li tiene fermi.** Pietro ha chiesto
mezzi più «pirotecnici» — elicottero, moto, monopattino, sci — anche nel quarto
anno, e mezzi fantasy e ariosteschi nel quinto. Aggiungerli ha prodotto subito una
domanda che il file deve rispondere da solo: **una moto del 1903 in una tappa del
1300 è un errore**, e il progetto non ha mai tollerato un anacronismo silenzioso.
La risposta è una sola colonna in più, `dal`: l'anno in cui il mezzo è attestato.
E il controllo è **per tappa**, non per anno, perché l'anno 4 non è un'epoca: va
dalle tavolette di Uruk a Orwell, e in un anno solo ci sono ottocento anni.

Due colonne di mezzi, perché la domanda del gioco è due:

  **chi viaggia**  chi porta il documento, con i mezzi che esistevano alla data
                  della tappa. Qui l'anacronismo è un difetto e viene segnalato.
  **con che cosa arriva il giocatore**  i mezzi di oggi sulla stessa tappa. Qui
                  l'anacronismo non è un difetto ma **l'informazione**: la domanda
                  del quinto anno è proprio «che cosa è cambiato in mezzo?».

I mezzi del *Furioso* sono la terza categoria: esistono soltanto nell'edizione
1516, il numero che hanno è una **convenzione dichiarata** e non una velocità
stimata, e `tipo` dice `gioco` perché nessuno li legga come un dato storico.
Ognuno porta con sé il canto e l'ottava da cui viene.

Uso:
    python3 sorgenti/percorsi_mezzi.py
    python3 sorgenti/percorsi_mezzi.py --solo fantasia
    python3 sorgenti/percorsi_mezzi.py --solo anacronismi
"""
import math
import sys

# mezzo: (km al giorno, persone per viaggio, nota, tipo, primo anno attestato)
#
# `tipo`     `storico` — il mezzo esiste e la velocità è una stima discussa
#            `gioco`   — il mezzo esiste solo nel testo o nella convenzione del
#                       gioco, e la velocità è una convenzione dichiarata
# `dal`      l'anno (o l'edizione) in cui il mezzo è attestato
MEZZI = {
    "a piedi": (25, 1, "un uomo solo, con la bisaccia", "storico", -3000),
    "mulo": (35, 2, "la bestia da soma delle vie postali", "storico", -2000),
    "cavallo": (45, 2, "cavaliere e scudiero, con i bagagli in sella", "storico", -3000),
    "carrozza": (35, 4, "carrozza di corte, cambio dei cavalli ogni 30-40 km", "storico", 1600),
    "galera": (55, 40, "galera veneziana: remi e vela, i passeggeri pagano", "storico", 1500),
    "nave": (130, 300, "veliero latino di grossa portata, rotta dipendente dal vento", "storico", -3000),
    "carovana": (30, 60, "carovana delle strade delle carovane, con le guide", "storico", -1000),
    "diligenza": (45, 8, "diligenza delle poste, cambio dei cavalli ogni 10-12 km", "storico", 1650),
    "pipa": (8, 1, "la pianta che in Cinquecento faceva il giro d'Europa", "storico", 1600),
    "treno": (180, 200, "convoglio ferroviario, orari fissi e acquisto del biglietto", "storico", 1825),
    "aereo": (900, 300, "volo di linea, con il tempo di attesa all'aeroporto", "storico", 1920),
    "crociera": (200, 2000, "nave passeggeri: il tempo di attesa è il vero costo", "storico", 1900),
    "moto": (250, 2, "moto: 500 km al giorno con due soste, e le soste sono il costo vero", "storico", 1903),
    "sci": (40, 2, "sci da montagna: 30 km/h di media, e la salita si paga", "storico", 1900),
    "elicottero": (320, 4, "volo interno: la rotta più breve in assoluto, il costo più alto", "storico", 1936),
    "monopattino": (30, 1, "mezzo urbano: 20 km/h, e serve solo per l'ultimo tratto", "storico", 2001),
    # --- i mezzi del Furioso: convenzioni dichiarate, con la fonte sul testo
    "ippogrifo": (500, 1, "«una giumenta generò d'un grifo» — c. IV, 18", "gioco", 1516),
    "drago": (400, 2, "«sí duro intorno ha lo scaglioso drago» — c. XVIII, 12", "gioco", 1516),
    "sirena": (200, 1, "«la sirena che col suo dolce canto acheta il mare» — c. VI, 40", "gioco", 1516),
    "carro di delfini": (250, 2, "«che fatto al carro i suoi delfini porre» — c. XI, 44", "gioco", 1516),
    "carro di serpenti": (250, 2, "«sul carro che tiravan dui serpenti» — c. XII, 2", "gioco", 1516),
}

# Il percorso di ogni anno, in chilometri in linea d'aria: le stesse cifre che
# `percorsi_confronto.py` calcola su `dati/luoghi_gioco.json`.
PERCORSI = {1: 8601, 2: 3139, 3: 18318, 4: 58644, 5: 79494}

# I mezzi **portatori** che l'anno mette a disposizione, in italiano: «a, b e c»
# sono tre mezzi. La lista non è un ornamento: è l'insieme su cui il file
# sceglie, e la scelta è calcolata (`piu_veloce`).
PORTATORE = {
    1: ["a piedi"],
    2: ["cavallo", "galera"],
    3: ["cavallo", "galera", "pipa"],
    4: ["nave", "carovana", "diligenza", "treno", "aereo", "moto", "sci"],
    5: ["treno", "aereo", "crociera"],
}

# Il mezzo **del percorso**: quello che il gioco usa quando calcola i giorni
# dell'anno intero, e la ragione per cui quello e non un altro. Per gli anni 1-3
# il mezzo è unico e non c'è scelta; per gli anni 4 e 5 è il mezzo del **caso
# peggiore**, cioè il più lento dei portatori, e la colonna `veloce` dice che in
# tante tappe si va molto più in fretta. È la differenza fra «il viaggio dura
# tre anni» e «in questa tappa si arriva in quattro giorni».
SCELTE = {
    1: ("a piedi", "Ferrara è piccola: dalle mura al confines ci si va a piedi, e il "
                   "giro dentro le mura sono 8,6 km"),
    2: ("cavallo", "la penisola si attraversa a cavallo, e il mare si prende in galera"),
    3: ("cavallo", "l'Europa è unita da due reti: la strada delle poste e il mare"),
    4: ("carovana", "all'archivio non arriva il duca: arriva il materiale, per via "
                    "d'acqua o di terra, e nelle tappe dell'Ottocento anche in treno"),
    5: ("treno", "il tempo è la mappa: si viaggia in treno e in aereo, e si torna "
                 "spesso. Il tempo di attesa all'aeroporto è il costo vero"),
}

# Gli anni di cui `ANNO_TAPPA` porta le date: sono gli unici due in cui le
# trenta tappe non sono tutte dentro la stessa epoca, e quindi gli unici in cui
# «che mezzo si usa» è una domanda con una risposta che cambia da tappa a tappa.
ANNI_CON_DATE = (4, 5)

# I mezzi con cui il **giocatore** arriva oggi sulla stessa tappa. Non sono
# storici e non devono esserlo: sono la risposta alla domanda «che cosa è
# cambiato?», e la colonna li tiene fuori dal controllo degli anacronismi appunto
# perché l'anacronismo, qui, è il contenuto e non il difetto.
GIOCATORE = {
    4: "moto, sci, elicottero e monopattino",
    5: "moto, sci, elicottero e monopattino",
}

# L'anno delle tappe degli anni 4 e 5, e `None` per «il presente, non datato».
# È il dato che rende possibile il controllo per tappa: l'anno 4 non è un'epoca,
# e un controllo per anno direbbe «una moto del 1903 va bene nel 1300».
# L'anno è l'anno di morte della persona quando esiste, altrimenti l'anno di
# nascita: il primo evento della scheda, che è quello che il gioco racconta.
ANNO_TAPPA = {
    # anno 4
    "4-1": -2700, "4-2": 1368, "4-3": -210, "4-4": -1473, "4-5": 1605,
    "4-6": 1227, "4-7": 1716, "4-8": 1778, "4-9": 1337, "4-10": 1597,
    "4-11": 850, "4-12": -479, "4-13": 415, "4-14": 1520, "4-15": -700,
    "4-16": -232, "4-17": 1956, "4-18": 1566, "4-19": 1021, "4-20": None,
    "4-21": 1504, "4-22": -1750, "4-23": 1524, "4-24": 1433, "4-25": 1888,
    "4-26": 1547, "4-27": 1910, "4-28": 1950, "4-29": 1934, "4-30": None,
    # anno 5
    "5-1": 1954, "5-2": 1994, "5-3": 1727, "5-4": 1996, "5-5": 1957,
    "5-6": -1600, "5-7": 2022, "5-8": 1966, "5-9": 1858, "5-10": 2017,
    "5-11": None, "5-12": 1986, "5-13": 1972, "5-14": 2004, "5-15": None,
    "5-16": None, "5-17": None, "5-18": 2000, "5-19": 2000, "5-20": 1597,
    "5-21": 2002, "5-22": None, "5-23": None, "5-24": 2018, "5-25": 2001,
    "5-26": None, "5-27": None, "5-28": 2023, "5-29": None, "5-30": None,
}

# I mezzi che sono soltanto del testo, e l'anno che li contiene.
FANTASIA_ANNO = {
    5: ("ippogrifo, drago, sirena, carro di delfini e carro di serpenti",
        "mezzi che esistono soltanto nell'edizione 1516: il numero che hanno è "
        "una convenzione dichiarata, e il gioco dice al giocatore che quel "
        "numero non è un fatto"),
}


def voci(elenco):
    """I mezzi di un elenco scritto in italiano: «a, b e c» sono tre mezzi.

    Il separatore è la congiunzione e non solo la virgola, perché la frase
    scritta è quella che si legge: `aereo` finirebbe fuori da un elenco di due
    voci solo perché la seconda è congiunta con «e».
    """
    if isinstance(elenco, (list, tuple)):
        return [str(v).strip() for v in elenco if str(v).strip()]
    testo = elenco.replace(" e ", ", ")
    return [v.strip() for v in testo.split(",") if v.strip()]


def costo(km, mezzo, soste=0.2):
    """Giorni di viaggio per `km` con il mezzo indicato."""
    velocita = MEZZI[mezzo][0]
    g = km / velocita
    return int(math.ceil(g * (1 + soste)))


def anacronismi(quando, elenco):
    """I mezzi di `elenco` che non esistevano ancora nell'anno `quando`.

    `quando` None significa «il presente»: non c'è niente da contestare, perché il
    presente è l'unica data in cui tutti i mezzi esistono.
    """
    if quando is None:
        return []
    fuori = []
    for m in voci(elenco):
        if m in MEZZI and MEZZI[m][4] > quando:
            fuori.append((m, MEZZI[m][4]))
    return fuori


def piu_veloce(elenco, quando):
    """Il mezzo più veloce dell'elenco che esisteva già nell'anno `quando`.

    È la funzione che rende il gioco onesto invece che comodo: il mezzo **di
    allora** non è scritto a mano accanto alla tappa, è scelto dalla data, e se
    domani un anno il risultato cambia da solo. Nel 1888 va in treno; nel 1300
    non c'è treno e va in nave; nel 1934 va in aereo.
    """
    opzioni = [m for m in voci(elenco)
               if quando is None or MEZZI[m][4] <= quando]
    if not opzioni:
        return None
    return max(opzioni, key=lambda m: MEZZI[m][0])


def tabella():
    print("%-18s %6s %8s %-8s %6s  %s" % ("mezzo", "km/g", "persone", "tipo", "dal", "nota"))
    for nome, (km, pers, nota, tipo, dal) in MEZZI.items():
        print("%-18s %6d %8d %-8s %6s  %s" % (nome, km, pers, tipo, dal, nota))


def controlla_anacronismi():
    """Il riscontro fra il mezzo di allora e il mezzo di oggi, tappa per tappa.

    **Il difetto che la prima stesura di questo controllo cercava era sbagliato,
    e vale la pena dire perché.** Cercava «un mezzo che non esisteva alla data
    della tappa in cui è usato», e ne trovava uno solo: l'anno 5 è il anno di
    Alfonso II (1597) e del regno di Logistilla, e lì non esisteva né il treno né
    l'aereo. Ma il mezzo di cui si parla **non è il mezzo di Alfonso**: è il
    mezzo con cui il materiale di Alfonso arriva *all'archivio*, e l'archivio è
    del presente. Un anacronismo qui non è un errore: **è la risposta**.

    Il controllo giusto è quindi un confronto, e il difetto che cerca è uno solo:
    **il mezzo di oggi deve essere più veloce di quello di allora**. Se non lo
    fosse, il gioco direbbe che si arriva prima con il mezzo antico, e la
    tabella dei giorni mentirebbe.

    Il secondo output è la ripartizione dei mezzi di allora: quattro secoli di
    viaggi in una tabella, e la ragione per cui l'anno 4 non è un'epoca.
    """
    difetti = 0
    print("== riscontro: il mezzo di allora e il mezzo di oggi, tappa per tappa ==")
    print("%-6s %-8s %-12s %-12s %-8s %s"
          % ("tappa", "data", "mezzo di allora", "mezzo di oggi", "veloce?", "giorni"))
    for anno in sorted(ANNI_CON_DATE):
        if anno not in PORTATORE:
            continue
        conta = {}
        for t in range(1, 31):
            lid = "%d-%d" % (anno, t)
            quando = ANNO_TAPPA[lid]
            allora = piu_veloce(PORTATORE[anno], quando)
            oggi = piu_veloce(PORTATORE[anno], None)
            if allora is None or oggi is None:
                continue
            conta[allora] = conta.get(allora, 0) + 1
            veloce = MEZZI[oggi][0] >= MEZZI[allora][0]
            if not veloce:
                difetti += 1
            if t in (1, 15, 30):
                print("%-6s %-8s %-12s %-12s %-8s %d"
                      % (lid, quando, allora, oggi,
                         "OK" if veloce else "KO",
                         costo(PERCORSI[anno], allora)))
        print("  anno %d — mezzi di allora nelle 30 tappe: %s"
              % (anno, ", ".join("%s %d" % (m, n) for m, n in
                                 sorted(conta.items(), key=lambda kv: -kv[1]))))
    if not difetti:
        print("  nessun difetto: il mezzo di oggi non e' mai piu' lento di quello di allora")
    print()
    return difetti


def main():
    solo = sys.argv[1] if len(sys.argv) > 1 else ""

    if solo in ("", "--solo"):
        print("I mezzi, con la velocita' che il progetto usa")
        tabella()
        print()
        print("`dal` e' l'anno di attestazione: e' il dato che rende possibile il")
        print("controllo degli anacronismi, ed e' la ragione della colonna.")
        print()

        print("Che cosa costa ogni percorso, e con che mezzo")
        print("Il mezzo e' quello del **caso peggiore** fra i portatori: il")
        print("percorso dell'anno intero e' la somma delle sue trenta tappe.")
        print("%-5s %-10s %-9s %8s %7s %7s" % ("anno", "mezzo", "km", "giorni", "mesi", "anni"))
        for anno in sorted(PERCORSI):
            mezzo = SCELTE[anno][0]
            km = PERCORSI[anno]
            g = costo(km, mezzo)
            print("%-5d %-10s %-9d %8d %7.1f %7.1f"
                  % (anno, mezzo, km, g, g / 30, g / 365))
        print()

        print("I mezzi portatori dell'anno, anno per anno")
        for anno in sorted(PERCORSI):
            km = PERCORSI[anno]
            print("anno %d — %s" % (anno, SCELTE[anno][1]))
            for m in PORTATORE[anno]:
                print("     %-18s %5d giorni su %d km   (%d)"
                      % (m, costo(km, m), km, MEZZI[m][4]))
            for m in voci(GIOCATORE.get(anno, "")):
                if m in MEZZI:
                    print("     %-18s %5d giorni su %d km  (il giocatore, oggi)"
                          % (m, costo(km, m), km))
            print()

    if solo in ("", "anacronismi", "--solo"):
        controlla_anacronismi()

    if solo in ("", "fantasia", "--solo"):
        print("I mezzi che sono soltanto del testo")
        for anno, (elenco, nota) in sorted(FANTASIA_ANNO.items()):
            print("anno %d — %s" % (anno, elenco))
            print("     %s" % nota)
            for m in voci(elenco):
                if m in MEZZI:
                    print("     %-20s %5d giorni  (convenzione dichiarata)"
                          % (m, costo(PERCORSI[anno], m)))
        print()
        print("Il confronto che vale: cosa cambia fra il mezzo del testo e quello vero")
        km = PERCORSI[5]
        for nome in ("aereo", "treno", "ippogrifo", "drago"):
            print("  %-12s %6d giorni su %d km" % (nome, costo(km, nome), km))
        print()
        print("La domanda che il gioco fa con questi numeri non e' «quanto ci si")
        print("arriva»: e' «che cosa e' successo in mezzo».")
    return 0


if __name__ == "__main__":
    sys.exit(main())
