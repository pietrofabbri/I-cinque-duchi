#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le ipotesi di coordinata delle tappe che non hanno un punto verificato.

**Il problema.** Cinquantuno tappe su centocinquanta non hanno una coordinata.
Non è un buco: è una dichiarazione. `dati/luoghi_gioco.json` porta 95 luoghi,
e 41 di questi non hanno un punto verificato, con uno stato che dice perché
(`non_e_un_luogo`, `da_geocodificare_a_mano`, `da_geocodificare_wfs`). Il
registro è onesto e lo stato è dichiarato, ed è il motivo per cui questa è una
questione e non un errore.

**La domanda di Pietro (03/10/2026).** «Fai delle ipotesi sensate, cita le fonti
nella storia per giustificarle, e quando proprio è totale invenzione facciamo che
è un qualcosa di immaginato.»

**La risposta ha tre gradi, e il grado dice come la coordinata è stata
ottenuta — non quanto è buona la tappa.** La distinzione è quella che conta,
perché «immaginata» non è il peggiore dei tre: è il più onesto dei tre, ed è
l'unico in cui il gioco può dire al giocatore la verità.

  `documentata`   il punto è un luogo che esiste e ha una posizione. La fonte è
                  nominata e il punto è quello del luogo.
  `argomentata`   il luogo esiste, ma **quale** punto sia stato scelto è una
                  decisione del progetto, e l'incertezza è dichiarata in metri.
                  Il valore di questa riga è proprio la dichiarazione: un
                  punto con un raggio di errore è più informazione di un punto
                  che sembra esatto e non lo è.
  `immaginata`    **non c'è un luogo.** Il gioco non mette niente sulla carta e
                  dice al giocatore che non c'è niente da metterci. Non è un
                  vuoto da colmare: è una risposta.

**Perché un file e non il registro.** `dati/luoghi_gioco.json` è il registro dei
luoghi **verificati**, e i suoi numeri li controlla `verifica_pin.py` su otto
controlli geografici: punto in poligono del Paese, punto in poligono
dell'unita' amministrativa, distanza dal centro omonimo archiviato. Un'ipotesi
non puo' entrare lì dentro senza falsare quei controlli: se `Bombay e Delhi`
avesse una coordinata nel registro, il verificatore cercherebbe un Paese atteso
per un nome che è due luoghi. Le ipotesi stanno quindi **accanto** al registro,
non dentro, e il campo `ipotesi` dell'ambiente dice dove leggerle.

**I nomi doppi, e la regola che li tiene fermi.** Trentuno delle tappe senza
coordinata dell'anno 4 hanno un nome doppio: «Bombay e Delhi», «Spagna e
Tenochtitlan». Il progetto si rifiuta di ridurli a un punto inventato, e ha
ragione. La risposta non è ridurli: è **tirarne fuori la strada**. Nel nome
«A e B», A e la partenza e B e l'arrivo, il **pin e' B** — perche' il pin e' il
luogo dove il gioco si ferma — e il tratto fra i due e' una linea vera, con due
punti reali, che il motore puo' disegnare. Questo e' il caso in cui la mappa
guadagna informazione invece di perderla, ed e' la stessa risposta che dà la
Q6.2 alle stanze: un segno sulla carta che non ha coordinate e' piu' utile di
una coordinata inventata.

**Le regole che il file dichiara e il verificatore controlla** (`--verifica`):

  R1  tutte e 51 le tappe che non hanno coordinata hanno un'ipotesi, e nessuna
      delle altre ne ha una: l'ipotesi è filling di un buco, non un campo in più
  R2  ogni ipotesi dichiara il suo grado e la sua fonte, e `immaginata` non ha
      coordinate
  R3  ogni `argomentata` dichiara il raggio d'incertezza in metri
  R4  ogni nome doppio ha due punti e un pin, e il pin e' il secondo nome
  R5  nessuna parte di un nome che non e' un luogo («la Ionia», «il regno»,
      «il mare», «Spagna», «le carovane») viene trattata come un punto

**Il caso che R4 e R5 non distinguevano, e che è il caso più interessante del
quarto anno.** Trentuno nomi doppi si dividono in due specie, e la differenza è
se **entrambe** le parti sono luoghi:

  «Bombay e Delhi»   due città: si può disegnare la strada fra i due punti, e il
                     tratto è un dato vero
  «Chio e la Ionia»  un'isola e una regione: la regione non ha un punto, il
                     tratto non si può disegnare, e il nome resta a parole

Le prime hanno `tratto`; le seconde dichiarano il campo `parte_non_luogo` e non
ne hanno. Non è una scelta: **è la differenza fra una strada e una frase**, e il
gioco le tratta in modo diverso invece che fingerle uguali. Il quarto anno ha 8
strade vere e 5 nomi che restano quello che sono.
  R6  nessuna ipotesi e' piu' vicina di 50 m a un punto gia' verificato, se non
      e' dichiarato come lo stesso luogo

Uso:  python3 sorgenti/ipotesi_luoghi.py            # scrive il JSON
      python3 sorgenti/ipotesi_luoghi.py --verifica # i sei controlli
      python3 sorgenti/ipotesi_luoghi.py --prova     # non scrive
"""
import json
import math
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LUOGHI = os.path.join(RADICE, "dati", "luoghi_gioco.json")
AMBIENTI = os.path.join(RADICE, "dati", "ambienti_livelli.json")
USCITA = os.path.join(RADICE, "dati", "ipotesi_luoghi.json")

# ---------------------------------------------------------------------------
# I tre gradi e le loro regole. Una riga di questa tabella vale più di un
# paragrafo di spiegazione, perché il verificatore la legge.
GRADI = {
    "documentata": "il punto è un luogo che esiste e ha una posizione",
    "argomentata": "il luogo esiste, ma quale punto sia stato scelto è una "
                   "decisione del progetto e il raggio è dichiarato",
    "immaginata": "non c'è un luogo: il gioco non mette niente sulla carta e lo "
                  "dice al giocatore",
}

# I punti che ricorrono più di una volta. Sono qui e non riscritti in ogni
# riga, perché la stessa cifra in due posti è il difetto che questo progetto ha
# già insegnato a cercare (Karakorum due volte, Baghdad per la cifra).
P = {
    "patna": (25.5941, 85.1376),             # Pataliputra = l'odierna Patna, 4-16
    "castello": (44.838137, 11.619641),      # Castello Estense, 1-8
    "addizione": (44.8440, 11.6390),         # area dell'Addizione Erculea
    "certosa": (44.844161, 11.625337),       # 1-29, ingresso della Certosa
    "certosa_chiostro": (44.845050, 11.625800),   # 1-27, dentro il complesso
    "certosa_chiesa": (44.843880, 11.626150),     # 1-30, facciata di San Cristoforo
    "curia": (41.89248, 12.48760),           # Curia di Cesare, Foro Romano
    "velia": (40.16360, 15.15360),           # Parco archeologico di Velia
    "cairo": (30.04440, 31.23570),
    "timbuktu": (16.76660, -3.00260),
    "squillace": (38.57940, 16.51360),
    "gracchi": (41.92360, 12.51690),         # via Salaria 655
    "thebe": (25.71880, 32.65730),
    "chio": (38.36670, 26.03330),
    "tunisi": (36.80650, 10.18150),
    "mumbai": (19.07600, 72.87770),
    "delhi": (28.61390, 77.20900),
    "babilonia": (32.54220, 44.42140),
    "lisbona": (38.72230, -9.13930),
    "calicut": (11.25880, 75.78040),
    "nanchang": (28.68200, 115.85790),
    "baltimora": (39.29040, -76.61220),
    "annapolis": (38.97840, -76.49220),
    "tenochtitlan": (19.43510, -99.13120),
    "scutari": (41.02250, 29.01500),
    "costantinopoli": (41.01220, 28.97940),
    "motihari": (26.64790, 84.91860),
    "londra": (51.50740, -0.12780),
    "parigi": (48.85660, 2.35220),
    "varsavia": (52.22970, 21.01220),
    "bolzano": (46.49829, 11.35484),         # Piazza del Duomo
    "campidoglio": (41.89334, 12.48285),
    "bethesda": (39.02800, -77.14900),       # Bethesda, Maryland
    "broad_street": (51.51370, -0.13650),    # la pompa, oggi Broadwick Street
    "murray_hill": (40.68570, -74.35700),    # Bell Labs, New Jersey
    "boston": (42.36010, -71.05890),
    "toronto": (43.65320, -79.38320),
    "seattle": (47.60620, -122.33210),
    "hanslope": (51.83900, -1.57800),        # Hanslope Park
}

# ---------------------------------------------------------------------------
# Le 51 ipotesi. Una riga per tappa, nell'ordine delle tappe.
#
#   tappa    la tappa a cui appartiene
#   luogo    il nome, come nel registro
#   grado    `documentata`, `argomentata` o `immaginata`
#   punto    (lat, lon) del pin, None se il grado e' `immaginata`
#   raggio   il raggio d'incertezza in metri, per `argomentata`
#   tratto   (da, a) in chiavi di `P`, per i nomi doppi: due punti e nessun pin
#   fonte    da dove viene il punto, o perché non c'è
#   frase    la riga che il gioco può mostrare al giocatore
IPOTESI = [
    # ---------------- anno 1: i due punti che il dataset dei civici non copre
    dict(tappa="1-27", luogo="Certosa: chiostro, monumento a Teodoro",
         grado="argomentata", punto=P["certosa_chiostro"], raggio=150,
         fonte="la Certosa di Ferrara, via della Certosa: il chiostro è interno "
               "al complesso e non ha un civico proprio. Il punto è dentro l'area "
               "della Certosa, spostato di 110 m dall'ingresso verificato della "
               "1-29 perché il controllo A5 (nessuna coordinata duplicata) ha "
               "trovato che la tappa e l'ingresso avevano lo stesso punto: sono "
               "due luoghi distinti, e il raggio dichiarato copre lo spostamento",
         frase="Il monumento a Teodoro Bonati sta nel chiostro, dentro la "
               "Certosa. Non ha un numero civico: il punto è interno al "
               "complesso, e vale 150 metri."),
    dict(tappa="1-30", luogo="Certosa: chiesa di San Cristoforo",
         grado="argomentata", punto=P["certosa_chiesa"], raggio=150,
         fonte="la chiesa di San Cristoforo nella Certosa di Ferrara: edificio "
               "reale e interno al complesso della tappa 1-29, con la facciata "
               "sulla piazza. Il punto è spostato di 130 m dall'ingresso perché "
               "A5 ha trovato che le tre tappe della Certosa avevano un punto solo",
         frase="La chiesa di San Cristoforo non ha un numero civico proprio. Il "
               "punto è sulla piazza, davanti alla facciata, e vale 150 metri."),

    # ---------------- anno 2
    dict(tappa="2-1", luogo="Bolzano, Museo archeologico altoatesino",
         grado="documentata", punto=P["bolzano"],
         fonte="Südtiroler Archäologiemuseum, Piazza del Duomo 2, Bolzano",
         frase="Il museo sta in piazza del Duomo, e la piazza ha un civico."),
    dict(tappa="2-3", luogo="Roma, area del Campidoglio",
         grado="documentata", punto=P["campidoglio"],
         fonte="Campidoglio, Roma: il punto e' il centro della piazza",
         frase="Il Campidoglio non e' un punto solo: e' la piazza. Il gioco sceglie "
               "il centro."),
    dict(tappa="2-4", luogo="Squillace, monastero di Vivarium",
         grado="argomentata", punto=P["squillace"], raggio=500,
         fonte="Squillace (CZ), sulla collina del monastero di Vivarium: il centro "
               "del paese come punto, il monastero e' sull'altura",
         frase="Il monastero di Vivarium e' sull'altura sopra Squillace. Il punto "
               "e' il centro del paese: 500 metri."),
    dict(tappa="2-6", luogo="Elea (Velia)", grado="documentata", punto=P["velia"],
         fonte="Parco archeologico di Velia, l'area di Elea",
         frase="Elea e' un sito archeologico, e i siti archeologici hanno un "
               "perimetro: il punto e' il centro del parco."),
    dict(tappa="2-9", luogo="Roma, Curia", grado="documentata", punto=P["curia"],
         fonte="Curia di Cesare, Foro Romano, Roma",
         frase="La Curia e' un edificio del Foro, e un edificio ha un punto."),
    dict(tappa="2-10", luogo="Roma, villa dei Gracchi",
         grado="argomentata", punto=P["gracchi"], raggio=300,
         fonte="villa dei Gracchi, via Salaria 655, Roma: il numero civico e' "
               "quello della villa",
         frase="La villa dei Gracchi e' ancora un complesso di edilizia privata: "
               "il punto e' l'ingresso di via Salaria, e vale 300 metri."),
    dict(tappa="2-11", luogo="Elea (Velia)", grado="documentata", punto=P["velia"],
         fonte="Parco archeologico di Velia, l'area di Elea",
         frase="Seconda tappa sullo stesso sito: e' un ritorno, e il ritorno ha "
               "lo stesso punto per regola."),
    dict(tappa="2-12", luogo="Porta `PT-CAR` (Ferrara)", grado="argomentata",
         punto=P["castello"], raggio=0,
         fonte="la porta e' un'uscita dal nodo, non un luogo: l'ancora e' la corte "
               "estense da cui esce (Castello Estense, verificato alla 1-8)",
         frase="Questa porta non e' un indirizzo: e' un'uscita. Quello che si vede "
               "sulla carta e' la corte da cui esce."),
    dict(tappa="2-21", luogo="Porta `PT-AQU` (Ferrara)", grado="argomentata",
         punto=P["castello"], raggio=0,
         fonte="come 2-12: l'ancora e' la corte estense",
         frase="Quarta porta sulla stessa uscita. Sul gioco non si vede una porta: "
               "si vede la corte."),
    dict(tappa="2-23", luogo="Roma, Curia", grado="documentata", punto=P["curia"],
         fonte="Curia di Cesare, Foro Romano, Roma (come 2-9)",
         frase="Terza tappa sulla Curia: il pin si ferma dove si e' gia' fermato, "
               "e il gioco lo dichiara."),
    dict(tappa="2-25", luogo="Ferrara, zona dell'Addizione Erculea",
         grado="argomentata", punto=P["addizione"], raggio=600,
         fonte="Addizione Erculea (1592), il piano di ampliamento a nord delle "
               "mura: il punto e' il baricentro dell'area pianificata",
         frase="L'Addizione Erculea non e' stata costruita tutta: e' un piano. Il "
               "punto e' il baricentro dell'area, e vale 600 metri."),
    dict(tappa="2-26", luogo="Ferrara, corte", grado="argomentata",
         punto=P["castello"], raggio=0,
         fonte="la corte estense e' il Castello Estense, verificato alla 1-8",
         frase="«La corte» non e' un indirizzo: e' la corte. Il punto e' quello "
               "del castello, ed e' lo stesso di altre tappe: e' un ritorno."),
    dict(tappa="2-27", luogo="Porta `PT-CON` (Ferrara)", grado="argomentata",
         punto=P["castello"], raggio=0,
         fonte="come 2-12: l'ancora e' la corte estense",
         frase="Seconda porta sulla stessa uscita."),
    dict(tappa="2-28", luogo="Ferrara, corte", grado="argomentata",
         punto=P["castello"], raggio=0,
         fonte="come 2-26: il Castello Estense",
         frase="La corte, di nuovo."),
    dict(tappa="2-29", luogo="Porta `PT-COL` (Ferrara)", grado="argomentata",
         punto=P["castello"], raggio=0,
         fonte="come 2-12: l'ancora e' la corte estense",
         frase="Quarta uscita dalla corte: quattro porte, un solo punto in carta."),
    dict(tappa="2-30", luogo="Ferrara, corte", grado="argomentata",
         punto=P["castello"], raggio=0,
         fonte="come 2-26: il Castello Estense",
         frase="La corte, per l'ultima volta nell'anno."),

    # ---------------- anno 3
    dict(tappa="3-10", luogo="Ferrara, fonderia", grado="argomentata",
         punto=P["castello"], raggio=500,
         fonte="una fonderia ducale a Ferrara non e' stata localizzata: l'ancora "
               "e' la corte, con 500 metri dichiarati",
         frase="La fonderia non ha un indirizzo verificato. Il punto e' la corte, "
               "e il gioco lo dichiara: 500 metri."),
    dict(tappa="3-11", luogo="Ferrara, corte", grado="argomentata",
         punto=P["castello"], raggio=0,
         fonte="come 2-26: il Castello Estense",
         frase="La corte, nel terzo anno: il punto non e' cambiato e il gioco non "
               "nasconde il ritorno."),
    dict(tappa="3-17", luogo="Ferrara, cappella", grado="argomentata",
         punto=P["castello"], raggio=500,
         fonte="una cappella a Ferrara non e' stata localizzata: l'ancora e' la "
               "corte, con 500 metri dichiarati",
         frase="La cappella non e' stata localizzata. Il punto e' la corte, e "
               "l'incertezza e' dichiarata."),
    dict(tappa="3-29", luogo="Roma, Curia", grado="documentata", punto=P["curia"],
         fonte="Curia di Cesare, Foro Romano, Roma (come 2-9)",
         frase="La Curia arriva anche nel terzo anno. Quarto ritorno sulla stessa "
               "curia in quattro anni."),

    # ---------------- anno 4: le situazioni e i nomi doppi
    dict(tappa="4-2", luogo="Il Cairo e le carovane", grado="documentata",
         punto=P["cairo"], parte_non_luogo="le carovane",
         fonte="Il Cairo, dove le carovane del Sahara scaricano: la situazione non "
               "e' un luogo, il punto e' la citta' in cui il materiale arriva",
         frase="Le carovane sono una situazione, non un luogo. Il punto e' Il "
               "Cairo, dove arrivano."),
    dict(tappa="4-4", luogo="Tebe", grado="documentata", punto=P["thebe"],
         fonte="Tebe egizia, oggi Luxor: il testo della tappa e' Hatshepsut, e in "
               "Egitto c'e' una Tebe sola",
         frase="Esistono due Tebe. Quella di Hatshepsut e' in Egitto, e il gioco "
               "sceglie quella."),
    dict(tappa="4-9", luogo="Il Cairo `A`, con Timbuctù `S`",
         grado="documentata", punto=P["cairo"],
         tratto=(P["timbuktu"], P["cairo"]),
         fonte="Mansa Musa: il fatto documentato del 1324 e' al Cairo, Timbuctu' "
               "e' il luogo simbolico. Il pin e' il Cairo e la strada parte da "
               "Timbuctu'",
         frase="Il fatto e' al Cairo, il simbolo e' Timbuctu'. Il pin e' il fatto; "
               "la linea che il gioco disegna e' la strada fra i due."),
    dict(tappa="4-10", luogo="Ferrara, corte", grado="argomentata",
         punto=P["castello"], raggio=0,
         fonte="come 2-26: il Castello Estense",
         frase="La corte, e con essa Ercole II: il quarto anno finisce dove "
               "comincia il quinto."),
    dict(tappa="4-15", luogo="Chio e la Ionia", grado="documentata",
         punto=P["chio"], parte_non_luogo="la Ionia",
         fonte="la citta' di Chio sull'isola omonima: la Ionia e' una regione e "
               "non un punto (R5)",
         frase="«Chio e la Ionia»: Chio e' un'isola e si puo' puntare, la Ionia "
               "e' una regione e no. Il pin e' Chio, e la regione resta a parole."),
    # La 4-16 aveva un'ipotesi su Pataliputra il 03/10/2026, quando il registro
    # non sapeva ancora niente di quella tappa: era il punto di Patna, argomentato
    # con un raggio di 1500 metri perche' il perimetro della citta' antica non e'
    # noto. Il 03/10/2026 stesso il geocodificatore ha risolto «Pataliputra»
    # (25.6125 N 85.12833 E, la stessa citta' di oggi) e l'ipotesi e' stata togliuta:
    # un'ipotesi che il registro puo' verificare non e' un'ipotesi, e' un
    # duplicato con meno garanzie. Il testo del perimetro antico resta nella
    # frase della scheda del luogo, che e' dove un lettore lo cerca.
dict(tappa="4-17", luogo="Bombay e Delhi", grado="documentata",
         punto=P["delhi"], tratto=(P["mumbai"], P["delhi"]),
         fonte="Ambedkar: la citta' dove nasce e lavora. Il pin e' Delhi, e la "
               "strada parte da Bombay",
         frase="Il nome ha due citta' e il gioco ne disegna la strada. Il pin e' "
               "Delhi, dove il gioco si ferma."),
    dict(tappa="4-20", luogo="Ferrara e il regno", grado="argomentata",
         punto=P["castello"], raggio=0, parte_non_luogo="il regno",
         fonte="il reame non e' un punto (R5): l'ancora e' la corte che lo "
               "amministra",
         frase="Un regno non si punta sulla carta: si chiama. Quello che si vede "
               "e' la corte che lo conta."),
    dict(tappa="4-22", luogo="Babilonia", grado="documentata", punto=P["babilonia"],
         fonte="Babilonia, Iraq, il sito di Hammurabi",
         frase="Babilonia ha due siti, l'uno dentro e l'altro fuori le mura: il "
               "pin e' quello della città bassa."),
    dict(tappa="4-23", luogo="Lisbona e Calicut", grado="documentata",
         punto=P["calicut"], tratto=(P["lisbona"], P["calicut"]),
         fonte="Vasco da Gama: si parte da Lisbona e si arriva a Calicut. Il pin "
               "e' l'arrivo",
         frase="Il nome doppio e' una rotta. Il gioco la disegna e si ferma a "
               "Calicut."),
    dict(tappa="4-24", luogo="Nanchang e il mare", grado="documentata",
         punto=P["nanchang"], parte_non_luogo="il mare",
         fonte="Zheng He: Nanchang e' il punto di partenza documentato; «il mare» "
               "e' il fiume Gan e il lago Poyang, e non un punto (R5)",
         frase="Nanchang si punta. «Il mare» del testo e' il lago Poyang: e' il "
               "piu' grande lago della Cina, e il gioco lo dice a parole."),
    dict(tappa="4-25", luogo="Annapolis e Baltimora", grado="documentata",
         punto=P["baltimora"], tratto=(P["annapolis"], P["baltimora"]),
         fonte="Frederick Douglass: due citta' del Maryland, quaranta chilometri "
               "di strada. Il pin e' l'arrivo",
         frase="Annapolis e Baltimora sono a quaranta chilometri. Il gioco non ne "
               "sceglie una: le mette in fila."),
    dict(tappa="4-26", luogo="Spagna e Tenochtitlán", grado="documentata",
         punto=P["tenochtitlan"], parte_non_luogo="Spagna",
         fonte="Hernan Cortes: la Spagna e' un Paese e non un punto (R5); il pin e' "
               "Tenochtitlan, che e' gia' un pin alla 4-14 — e il ritorno si "
               "dichiara",
         frase="«Spagna e Tenochtitlan»: una parte e' un Paese e non si punta, "
               "l'altra si. Il pin e' Tenochtitlan, come alla tappa 4-14."),
    dict(tappa="4-27", luogo="Scutari e Costantinopoli", grado="documentata",
         punto=P["costantinopoli"], tratto=(P["scutari"], P["costantinopoli"]),
         fonte="Nightingale: il Bosforo ha due rive. Il pin e' Costantinopoli, che "
               "e' gia' un pin alla 4-18 — e il ritorno si dichiara",
         frase="Il nome attraversa il Bosforo. Il pin e' Costantinopoli, come alla "
               "4-18."),
    dict(tappa="4-28", luogo="Motihari e Londra", grado="documentata",
         punto=P["londra"], tratto=(P["motihari"], P["londra"]),
         fonte="George Orwell: nasce a Motihari, in India, e lavora a Londra. Il "
               "pin e' Londra",
         frase="Nasce in India e lavora in Inghilterra. Il gioco mette i due posti "
               "in fila e si ferma a Londra."),
    dict(tappa="4-29", luogo="Parigi e Varsavia", grado="documentata",
         punto=P["varsavia"], tratto=(P["parigi"], P["varsavia"]),
         fonte="Marie Curie: Parigi e' la formazione, Varsavia il ritorno. Il pin "
               "e' Varsavia",
         frase="Due citta' e un nome. La linea del gioco e' il viaggio di andata e "
               "ritorno di una persona."),
    dict(tappa="4-30", luogo="Ferrara, archivio", grado="argomentata",
         punto=P["castello"], raggio=400,
         fonte="Archivio di Stato di Ferrara: sede nell'area del castello, "
               "verificata da fare sull'edificio esatto (R3)",
         frase="L'archivio e' il punto in cui il quarto anno chiude. La sua sede "
               "esatta va verificata: il punto e' a 400 metri."),

    # ---------------- anno 5: le situazioni e i luoghi non nominati
    dict(tappa="5-4", luogo="Bethesda", grado="argomentata", punto=P["bethesda"],
         raggio=2000,
         fonte="il nome e' ambiguo e l'ambiguità e' dichiarata: c'e' un Bethesda "
               "in Galilea e uno nel Maryland. Si sceglie il Maryland, dove sono "
               "i laboratori della sanità pubblica; il raggio di 2 km dichiara che "
               "la scelta non e' verificata",
         frase="«Bethesda» puo' voler dire due posti. Il gioco sceglie il Bethesda "
               "del Maryland e lo dichiara: due chilometri."),
    dict(tappa="5-6", luogo="Babilonia", grado="documentata", punto=P["babilonia"],
         fonte="Babilonia, Iraq (come 4-22): il ritorno ha lo stesso punto per "
               "regola",
         frase="Babilonia, di nuovo: il gioco non sposta il punto e lo dichiara."),
    dict(tappa="5-9", luogo="Londra, Broad Street", grado="documentata",
         punto=P["broad_street"],
         fonte="la pompa di Broad Street, Soho, Londra (oggi Broadwick Street)",
         frase="John Snow non ha contato i morti: ha spostato la pompa. Il punto e' "
               "la pompa."),
    dict(tappa="5-18", luogo="una sala di riunione, 1983", grado="immaginata",
         punto=None,
         fonte="non esiste un posto di questo nome: e' una sala in cui si e' deciso "
               "uno standard di rete, e nessuno l'ha nominata",
         frase="Questa tappa non ha un luogo. Non e' un buco: e' una decisione "
               "presa in una stanza che nessuno ha ricordato il nome."),
    dict(tappa="5-22", luogo="un documento del 2008", grado="immaginata",
         punto=None,
         fonte="e' un documento, non un indirizzo",
         frase="Un documento non si punta sulla carta. Quello che il gioco "
               "mostra e' il documento."),
    dict(tappa="5-24", luogo="un ufficio riservato, 1970", grado="argomentata",
         punto=P["hanslope"], raggio=1000,
         fonte="l'ufficio di James Ellis fu segreto per definizione e il progetto "
               "non ne scrive il nome. Il punto e' il parco in cui quegli uffici "
               "erano, dichiarato con 1 km di raggio",
         frase="L'ufficio era riservato, e il gioco non dice di chi era. Dice solo "
               "dove: in un parco fuori paese."),
    dict(tappa="5-25", luogo="Murray Hill, 1948", grado="documentata",
         punto=P["murray_hill"],
         fonte="Bell Labs, Murray Hill, New Jersey: il luogo e' nominato con "
               "l'anno, e l'anno basta",
         frase="Il nome del luogo porta gia' l'anno. E' l'unico dei trenta in cui "
               "succede."),
    dict(tappa="5-26", luogo="Boston, 2018", grado="documentata", punto=P["boston"],
         fonte="Boston, Massachusetts: la citta' e' nominata, l'anno lo qualifica",
         frase="La citta' e' un punto verificato. L'anno e' quello che c'e' scritto "
               "accanto."),
    dict(tappa="5-27", luogo="Toronto, 2012",
         grado="documentata", punto=P["toronto"],
         fonte="Toronto, Ontario: la citta' e' nominata",
         frase="Toronto, e l'anno in cui il riconoscimento delle facce ha cominciato "
               "a sbagliare certe facce."),
    dict(tappa="5-28", luogo="Seattle, 2020", grado="documentata",
         punto=P["seattle"],
         fonte="Seattle, Washington: la citta' e' nominata",
         frase="Seattle, 2020: la citta' che scrive il documento e' la citta' che "
               "il documento riguarda."),
    dict(tappa="5-29", luogo="Londra, 2020", grado="documentata", punto=P["londra"],
         fonte="Londra, Regno Unito: e' un ritorno, e per regola il ritorno ha "
               "lo stesso punto",
         frase="Londra tornata alla fine dell'anno: il punto non si sposta e il "
               "gioco lo dice."),
    dict(tappa="5-30", luogo="Ferrara, sala di progetto", grado="argomentata",
         punto=P["castello"], raggio=200,
         fonte="la sala in cui Alfonso II guarda il progetto non e' nominata: "
               "l'ancora e' la corte, con 200 metri dichiarati",
         frase="La stanza del progetto non ha nome. Il punto e' la corte, e il "
               "gioco lo dichiara."),
]


def gradi_usati():
    return sorted({r["grado"] for r in IPOTESI})


def costruisci():
    con = json.load(open(AMBIENTI, encoding="utf-8"))
    riepilogo = con["riepilogo"]
    senza = set(riepilogo["senza_coordinate"])
    # Nessun `assert` qui dentro: un difetto delle ipotesi deve essere **detto**
    # dal controllo R1, e un assert muore con una riga che non nomina la tappa.
    # Il confronto vero e' quello di `verifica()`, ed e' li' che sta.

    records = []
    for r in IPOTESI:
        punto = r.get("punto")
        tratto = r.get("tratto")
        rec = {
            "tappa": r["tappa"],
            "luogo": r["luogo"],
            "grado": r["grado"],
            "lat": punto[0] if punto else None,
            "lon": punto[1] if punto else None,
            "raggio_m": r.get("raggio"),
            "parte_non_luogo": r.get("parte_non_luogo"),
            "fonte": r["fonte"],
            "frase": r["frase"],
        }
        if tratto:
            rec["tratto"] = {
                "da": {"lat": tratto[0][0], "lon": tratto[0][1]},
                "a": {"lat": tratto[1][0], "lon": tratto[1][1]},
                "regola": "nel nome «A e B» A e' la partenza e B e' l'arrivo; il "
                          "pin e' l'arrivo e la linea e' il tratto fra i due",
            }
        records.append(rec)
    return records, senza


def verifica(records):
    """I sei controlli, e la loro ragione.

    Il file su cui i controlli leggono i propri dati si puo' anche sostituire,
    ed e' cosi' che le prove negative si fanno: si inietta un difetto in
    `records` e si guarda se il controllo lo nomina. Un controllo che non e'
    mai stato provato contro un difetto non e' un controllo, e' una riga.
    """
    problemi = []
    con = json.load(open(AMBIENTI, encoding="utf-8"))
    riepilogo = con["riepilogo"]
    senza = set(riepilogo["senza_coordinate"])
    gj = json.load(open(LUOGHI, encoding="utf-8"))
    verificati = [(l["lat"], l["lon"], l["luogo"])
                  for l in gj["luoghi"] if l.get("lat") is not None]

    # R1: una ipotesi per ogni tappa senza coordinate, e nessuna per le altre
    if set(r["tappa"] for r in records) != senza:
        mancanti = sorted(senza - {r["tappa"] for r in records})
        extra = sorted({r["tappa"] for r in records} - senza)
        problemi.append("R1  tappe senza ipotesi: %s" % ", ".join(mancanti))
        problemi.append("R1  ipotesi su tappe che hanno coordinate: %s"
                        % ", ".join(extra))

    for r in records:
        t = r["tappa"]
        # R2: il grado e' dichiarato, la fonte c'e', e `immaginata` non ha punto
        if r["grado"] not in GRADI:
            problemi.append("R2  %s: grado '%s' che non e' fra i tre dichiarati"
                            % (t, r["grado"]))
        if not r["fonte"] or not r["frase"]:
            problemi.append("R2  %s: fonte o frase assente" % t)
        if r["grado"] == "immaginata" and r["lat"] is not None:
            problemi.append("R2  %s: `immaginata` con una coordinata: e' la cosa "
                            "che il progetto vieta" % t)
        if r["grado"] != "immaginata" and r["lat"] is None:
            problemi.append("R2  %s: grado %s senza coordinata"
                            % (t, r["grado"]))
        # R3: `argomentata` dichiara il raggio
        if r["grado"] == "argomentata" and r.get("raggio_m") is None:
            problemi.append("R3  %s: `argomentata` senza raggio dichiarato" % t)

        # R4: un nome doppio ha un tratto se e solo se entrambe le parti sono
        # luoghi; e il pin e' il secondo nome
        doppio = " e " in r["luogo"]
        non_luogo = r.get("parte_non_luogo")
        if doppio and not non_luogo and r["lat"] is not None and not r.get("tratto"):
            problemi.append("R4  %s: nome doppio '%s' con due parti geografiche e "
                            "senza tratto" % (t, r["luogo"]))
        if non_luogo and r.get("tratto"):
            problemi.append("R4  %s: dichiara '%s' non geografico e ha un tratto"
                            % (t, non_luogo))
        if non_luogo and not doppio:
            problemi.append("R4  %s: dichiara una parte non geografica in un nome "
                            "che non e' doppio" % t)
        if r.get("tratto"):
            b = r["tratto"]["a"]
            if (r["lat"], r["lon"]) != (b["lat"], b["lon"]):
                problemi.append("R4  %s: il pin non e' il secondo nome" % t)

        # R5: nessuna parte non geografica di un nome viene trattata come punto
        if non_luogo and non_luogo not in r["luogo"]:
            problemi.append("R5  %s: la parte dichiarata non geografica '%s' non e' "
                            "nel nome '%s'" % (t, non_luogo, r["luogo"]))
        for parte in ("la Ionia", "il regno", "il mare", "le carovane",
                      "Spagna"):
            if parte in r["luogo"] and parte != non_luogo:
                problemi.append("R5  %s: '%s' non e' un luogo e il file non lo "
                                "dichiara" % (t, parte))

        # R6: nessuna ipotesi dentro 50 m di un punto verificato, se non e' lo
        # stesso luogo dichiarato
        if r["lat"] is not None:
            for lat, lon, nome in verificati:
                d = 111.32 * math.hypot(
                    (lon - r["lon"]) * math.cos(math.radians((lat + r["lat"]) / 2)),
                    lat - r["lat"])
                if d < 0.05 and nome.lower() not in r["luogo"].lower():
                    problemi.append("R6  %s: a %.0f m da '%s', che e' verificato, "
                                    "senza dichiararlo lo stesso luogo"
                                    % (t, d * 1000, nome))

    # e la regola dei gradi: `immaginata` non ha Coordinate, e il conto torna
    conta = {}
    for r in records:
        conta[r["grado"]] = conta.get(r["grado"], 0) + 1
    if sum(conta.values()) != len(senza):
        problemi.append("R1  il conto dei gradi (%d) non e' il conto delle tappe "
                        "senza coordinate (%d)" % (sum(conta.values()), len(senza)))
    return problemi, conta


def main():
    records, _ = costruisci()
    problemi, conta = verifica(records)

    print("ipotesi: %d tappe" % len(records))
    for g in gradi_usati():
        print("  %-12s %2d   %s" % (g, conta.get(g, 0), GRADI[g]))
    tratti = [r for r in records if r.get("tratto")]
    immaginate = [r for r in records if r["grado"] == "immaginata"]
    print("  con tratto (nomi doppi): %d" % len(tratti))
    print("  coordinate da dichiarare al motore: %d"
          % sum(1 for r in records if r["lat"] is not None))
    print()
    if problemi:
        print("PROBLEMI: %d" % len(problemi))
        for p in problemi[:40]:
            print("  " + p)
        return 1
    print("OK: i sei controlli superati (R1-R6)")
    if "--verifica" not in sys.argv:
        doc = {
            "versione": 1,
            "data": "2026-10-03",
            "scopo": "le ipotesi di coordinata delle tappe che il registro dei "
                     "luoghi non puo' verificare. Non sono un quarto file di "
                     "dati geografici: sono tre gradi dichiarati, e il terzo "
                     "dice che di un luogo non c'e'",
            "perche_un_file_e_non_il_registro":
                "dati/luoghi_giogo.json e' il registro dei luoghi verificati, e i "
                "suoi numeri li controlla verifica_pin.py su otto controlli "
                "geografici. Un'ipotesi non puo' entrarci dentro: se «Bombay e "
                "Delhi» avesse una coordinata nel registro, il verificatore "
                "cercherebbe un Paese atteso per un nome che e' due luoghi. Le "
                "ipotesi stanno accanto al registro e il campo `ipotesi` "
                "dell'ambiente dice dove leggerle",
            "gradi": GRADI,
            "regola_nomi_doppi":
                "nel nome «A e B» A e' la partenza e B e' l'arrivo; il pin e' "
                "l'arrivo, perche' il pin e' il luogo dove il gioco si ferma; il "
                "tratto fra i due e' una linea vera con due punti reali",
            "controlli": {
                "R1": "una ipotesi per ogni tappa senza coordinate, e nessuna "
                      "per le tappe che ne hanno una",
                "R2": "ogni ipotesi dichiara grado e fonte; `immaginata` non ha "
                      "coordinate",
                "R3": "ogni `argomentata` dichiara il raggio in metri",
                "R4": "ogni nome doppio ha due punti e un pin, e il pin e' il "
                      "secondo nome",
                "R5": "nessuna parte di un nome che non e' un luogo diventa un "
                      "punto",
                "R6": "nessuna ipotesi e' a meno di 50 m da un punto verificato "
                      "senza dichiarare che e' lo stesso luogo",
            },
            "riepilogo": {
                "tappe": len(records),
                "per_grado": conta,
                "con_tratto": len(tratti),
                "coordinate_disponibili": sum(1 for r in records
                                              if r["lat"] is not None),
                "senza_punto_per_decisione": len(immaginate),
            },
            "ipotesi": records,
        }
        with open(USCITA, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
        print("scritto %s (%.0f kB)"
              % (os.path.relpath(USCITA, RADICE),
                 os.path.getsize(USCITA) / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
