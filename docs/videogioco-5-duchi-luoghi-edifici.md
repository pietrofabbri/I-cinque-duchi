---
titolo: I luoghi e le sagome — che cosa serve per disegnarli davvero
versione: 0.3
data: 2026-10-02
autore: Buffy (per pietrofabbri)
documenti collegati:
  - docs/videogioco-5-duchi-mappe.md
  - docs/videogioco-5-duchi-luoghi.md
  - docs/videogioco-5-duchi-ritratti.md
  - FONTI-E-LICENZE.md
  - AGENTS.md
---

# I luoghi e le sagome

## 0. La domanda, e la risposta breve

«Raccogli i dettagli sui luoghi, in modo che all'atto della creazione si possa
fare un lavoro che rispetti proporzioni, forme, colori rispetto a vie, edifici,
piazze.»

La risposta breve è che **manca un pezzo e non si può comprare**.

Le altezze degli edifici non esistono come dato: misurate sul campo, si trovano
nel 24% dei casi a Milano e nel 3% a Roma (`mappe.md` §5). Nessuna fonte libera
e nessuna fonte a pagamento le dà. Un modello che stima le altezze senza dire
che le stima produce edifici sbagliati con aria di esatti, che è il peggiore dei
due.

Quello che c'è invece, e che nessuno stava usando, è **il terreno**. È un dato
pubblico, libero, preciso, e dice tre cose che in una vista 3/4 si vedono
sempre: quanto scende la strada, da che parte guarda il pendio, e a che altezza
sta la piazza. Una città su un pendio ha edifici che seguono la curva di livello
e si sfalsano a gradini; una città in piano no. Un generatore che non sa
quanto scende la strada produce un Effect.

Il pezzo che manca, e che va costruito, è il **generatore**, non il dato.

## 1. La decisione su ODbL, che era la questione aperta

`mappe.md` §10 Q1 chiedeva: *ODbL entra nel progetto?* È la prima cosa da
rispondere, perché cambia che cosa si può scaricare.

**Sì, entra.** E l'obiezione che di solito si oppone — «ti obbliga a mettere
tutto sotto licenza libera» — **non è corretta**, e vale la pena dirlo perché
decide da metà del lavoro.

ODbL ha due obblighi distinti, e si confondono:

- **Attribuzione.** Ogni uso di dati OpenStreetMap deve mostrare «© OpenStreetMap
  contributors». È un dovere, e basta una riga nei crediti.
- **Condivisione allo stesso modo.** Scatta solo quando si distribuisce un
  **database derivato** — un insieme di dati machine-readable derivato da OSM.

Un gioco che disegna la geometria su schermo non distribuisce un database
derivato: distribuisce un'opera. Quindi **il codice del gioco, i documenti e la
grafica originale restano del progetto**. I file che invece *sono* database
derivati — le geometrie in `dati/mappe/` — devono viaggiare con ODbL e con la
loro dichiarazione. Sono dati, non il gioco.

Cosa si sblocca, in concreto:

| | senza ODbL | con ODbL |
|---|---|---|
| sagome degli edifici fuori Ferrara | solo dove il Comune le pubblica, cioè **Ferrara** | ovunque |
| trenta zone percorribili | di fatto una | tutte |
| attribuzione | — | una riga nei crediti |
| licenza dei file di dati | libera | ODbL, dichiarata |

I vincoli che restano, e che vanno rispettati: **non si può toccare il file
derivato e distribuirlo come proprio**, e ogni distribuzione deve portare la
licenza. Sono due righe nei crediti, non un vincolo sul progetto.

`FONTI-E-LICENZE.md` è aggiornato con la decisione.

## 2. I 95 luoghi, e la scoperta che era dentro la casella

I luoghi del gioco non erano in un file: erano sparsi nelle colonne «Luogo (pin)»
delle trenta tappe di ciascun anno. `sorgenti/luoghi/estrai_luoghi.py` li legge da
lì, perché un inventario scritto a parte può divergere dai documenti, e un
inventario che diverge è un inventario falso.

Ne escono **95 luoghi distinti** su 120 tappe. E qui c'è la scoperta: **41 di
questi non hanno coordinate, e non è colpa della ricerca**. La casella non
 contiene un luogo. Contiene cinque cose diverse:

| `tipo` | Che cos'è | Quanti | Si disegna |
|---|---|---|---|
| `citta` | una città | 48 | mappa, edifici per tipologia ed epoca |
| `percorso` | due o più posti insieme: «Il Cairo e le carovane» | 11 | strada che unisce, con i due capi |
| `situazione` | un contesto, non un posto: «una sala di riunione, 1983» | 11 | **non si disegna** |
| `edificio` | un palazzo, una corte, un convento | 10 | sagoma singola, con la sua cronologia |
| `citta_antica` | Uruk, Tebe, Babilonia | 9 | il rilievo moderno non dice niente: piano separato |
| `porta` | `PT-COL` (Ferrara) | 4 | **non si disegna**: è un'uscita dal nodo |
| `area` | l'Addizione Erculea, la villa dei Gracchi | 2 | polilinea d'area, edifici dentro |

Il quinto anno è la conferma: 11 delle sue 30 tappe hanno una casella che non è
un luogo, e il documento del quinto anno lo dichiara da subito («l'unico anno in
cui una tappa è un'operazione e non un luogo»). Adesso è anche nei dati.

**Coordinate.** 54 su 95 verificate, e ogni scheda registra **a quale articolo di
Wikipedia il nome ha corrisposto**: senza quel campo, «Roma, Curia» che risolve
sulla Curia romana e «Ferrara, corte» che non risolve su niente sarebbero due
vuoti identici. Le altre 41 hanno uno **stato dichiarato**, mai un vuoto silenzioso:

| stato | Quanti | Significato |
|---|---|---|
| `verificata` | 55 | risolta, con la fonte |
| `non_e_un_luogo` | 23 | è una porta o una situazione: non ha coordinate per definizione |
| `da_geocodificare_wfs` | 7 | è dentro Ferrara: si prende dal WFS del Comune, che c'è |
| `da_geocodificare_a_mano` | 10 | edificio o area: serve un'altra fonte, e si sa quale |

*(erano 54, 24, 7 e 11 il 03/10/2026: il registro è stato rigenerato e i due luoghi che sono cambiati sono Pataliputra, che ha trovato una coordinata verificata, e Manchester, che è uscita perché la tappa 3-28 ora dice Torino.)*

## 3. Lo schema del dettaglio: che cosa deve sapere il motore

Ogni luogo ha questi campi. La regola è che **un campo vuoto è un dato
dichiarato** (motore: non ti fidare, usa il default tipologico e dillo), mentre
un campo riempinto a stima sarebbe una bugia.

| Campo | Che cosa contiene | Chi lo riempie |
|---|---|---|
| `impianto` | forma della piazza, lati, assi, portici, fossato, viali | fonte storica |
| `materiali` | mattone, pietra, marmo, legno, terra — **con il colore** | fonte storica |
| `edifici` | ogni edificio: anno di costruzione, e rifacimenti | fonte storica |
| `cronologia` | che cosa c'era in un dato anno | fonte storica |
| `terreno` | quota, pendenza, esposizione, rilievo | **automatico**, misurato |
| `vuoto` | che cosa non si sa, detto per esteso | a mano |

Il campo che manca in tutti gli schemi precedenti è **`cronologia`**, ed è quello
che rende il gioco onesto. Una tappa che si svolge a Ferrara nel 1450 **non può
usare la piazza di oggi**: nel 1450 la statua di Alessandro VII non c'era (arrivò
nel 1660), il monumento a Vittorio Emanuele II non c'era (1889), e il sagrato non
era stato abbassato (anni Venti del Novecento). Sono tre differenze documentate
nello stesso posto, a trecento anni di distanza. Senza cronologia il gioco mostra
a un ragazzo del 1450 il Novecento.

### Il riferimento compilato: Ferrara

`dati/dettagli_ferrara.json` è il primo record compilato per intero, ed è il
modello. Contiene sette luoghi con la loro cronologia e le fonti. Le cose che
**non** ci sono, e che sono le più importanti, ci sono come vuoti dichiarati:

- le **dimensioni in metri** della piazza del Duomo: non sono nelle fonti usate,
  e non sono state stimate;
- la **pavimentazione** nel 1135 e nel 1450: il *volto* ferrarese è una
  tradizione documentata della città, ma quando fu rifatta questa piazza non lo
  so, e quindi non lo scrivo;
- il **luogo** della fonderia, dell'archivio e della cappella: nessuna fonte usata
  li colloca. Sulla cappella anzi ci sono due candidate documentate (quella ducale
  del Castello, nata per Renata di Francia, e quella di san Giuliano) e scegliere
  senza sapere sarebbe inventare.

Tre vuoti su sette voci, dichiarati uno per uno. È il risultato giusto: il primo
record compilato dice di più sul metodo di dieci record completati a mano.

## 4. La topografia, e perché aiuta più di quanto sembri

Il rilievo si prende dai **Terrarium** di AWS Open Data, derivati da SRTM:
una richiesta HTTP per tassello, **senza registrazione**, e i numeri sono buoni.
`dati/mappe/rilievo_penisola.json` e `rilievo_europa.json` sono **da produrre**, e lo produce
`sorgenti/gis/rilievo.py`, che per ogni città dà quota, pendenza (m/km),
esposizione e rilievo locale.

**Verificato su 14 punti ad altitudine nota**, errore medio assoluto **12,6 m**.
Ferrara 16 m (è sotto il livello del mare, e sotto c'è), Venezia 0,0 m, Aosta
580 m contro 583, Cortina 1 222 m contro 1 224, piazza Grande in Aosta letta su un
tassello che arriva a 2 078 m di rilievo.

Il primo errore di questa tabella è stato di **132,6 m**, e la causa è da
raccontare: per l'indice del pixel dentro il tassello usavo il resto della
divisione per 16, che è l'indice di un *tassello* a livello superiore, non di un
*pixel* — il tassello ha 256 pixel, non 16. Leggevo un punto diverso da quello
richiesto, e i numeri erano sbagliati di qualche centinaio di metri senza che
nulla lo segnalasse. Il Duomo di Firenze leggeva 254 m (è a 50), piazza Grande ad
Aosta 1 085 m (è a 583). Il metodo corretto calcola il pixel **globale** e sottrae
l'origine del tassello, ed è stato verificato leggendo il profilo del tassello: la
riga del Duomo dà 57–72 m e quella di Aosta 581–583 m.

**Cosa ne fa il generatore delle sagome**, in ordine di quanto conta:

1. **le altezze sfalsate** — un edificio appoggiato su una strada in pendio sta a
   un'altezza diversa dal vicino, e se il terreno non sale la fila di edifici
   sembra una fila di cartoni;
2. **il profilo contro il cielo** — è la sagoma della città, ed è metà della
   percezione di una vista 3/4; dipende dal rilievo, non dagli edifici;
3. **la pendenza della copertura** — un tetto a capriate su un pendio ripido
   diventa un tetto a padiglione, e su un pendio dolce resta a falda;
4. **l'esposizione** — la facciata che guarda a nord gela, quella a sud si scalda:
   decide finestre, aggetto e ombra portata, ed è geometria vera, non una scelta
   estetica;
5. **l'altezza minima di impianto** — in un terreno sotto il livello del mare
   l'edificio sta su un rialzo, e la piazza sta su una quota precisa: a Ferrara la
   differenza è di pochi metri e si vede.

Il rilievo **non** dà l'altezza di un singolo edificio, e non finge di darla. Per
quello si usa il modello a tre livelli che `mappe.md` §5.1 ha già, e che resta
giusto: `lidar` dove c'è, `osm` dove c'è, `stimata` altrove — **con la fonte
dichiarata in faccia all'edificio**, come i campi `attendibilita` e `manca` del
registro dell'anno 4.

## 5. Una regola che si è fatta pagare quattro volte

**Una richiesta che non arriva non è una risposta negativa.**

È successo quattro volte in due giorni, sempre nella stessa forma. Wikipedia
risponde `HTTP 429` a raffica; l'errore non è un codice di stato ma un corpo
vuoto; il codice che lo riceveva non lo distingueva da una risposta vera e
scriveva l'assenza come un fatto. Le quattro volte:

| Dove | Che cosa è stato scritto | Che cosa era vero |
|---|---|---|
| `cerca_ritratti.py` | «nessun ritratto in testa all'articolo» per 15 personaggi | Dürer, Turing, Leibniz, John Snow, Josquin, Bellini hanno tutti un ritratto |
| `ripara_licenze.py` | «file non letto su Commons» per 8 file | i file c'erano, cercati come pagine invece che come file |
| `ritratto_reale.py` | «download fallito» per 6 immagini | i file c'erano, era un 429 non ascoltato |
| `coordinate.py` | «nessun articolo» per 30 luoghi | Uruk, Tebe, Xianyang, Qufu hanno le coordinate |

La correzione è sempre la stessa, due righe: il client ascolta il `Retry-After`, e
l'esito distingue **`non_trovato`** (risposta avuta, niente) da **`richiesta_fallita`**
(nessuna risposta). Una richiesta fallita non chiude mai una scheda: la lascia
`da_rifare`. È in `AGENTS.md`, e va tenuto in tutti gli script che parlano con
qualcosa.

## 6. Cosa c'è da fare

| | |
|---|---|
| **compilare i 48 `citta`** con lo stesso schema di Ferrara | il lavoro vero, e non è breve: ognuna vuole impianto, cronologia e fonti |
| i 7 luoghi di Ferrara dal **WFS del Comune** | le coordinate sono lì, e le sagome anche |
| i 10 `da_geocodificare_a_mano` | Roma (Curia, Campidoglio, villa dei Gracchi), Bolzano, Squillace, Bethesda, Londra |
| i 9 `citta_antica` | Uruk, Tebe, Babilonia, Elea: servono piante ricostruite, non il rilievo moderno |
| **il generatore delle sagome** | è la vera lacuna: senza, le altezze restano stimate ovunque fuori Ferrara |
| scaricare `rilievo_penisola.json` e `rilievo_europa.json` | lo script è pronto e verificato; non è ancora stato eseguito |
| le **dimensioni** delle piazze | nessuna fonte le dà per iscritto: o si rilevano dal WFS o restano vuote |

## 7. Il registro delle modifiche

### v0.3 — 03/10/2026

**Il registro dei luoghi è stato rifatto dalla catena, e i numeri sono cambiati per un motivo buono.** `verificata` da 54 a **55**, `non_e_un_luogo` da 24 a **23**, `da_geocodificare_a_mano` da 11 a **10**. Le due mosse sono Pataliputra, che ha trovato una coordinata verificata (25.6125 N 85.12833 E) quando il geocodificatore l'ha cercata, e Manchester, che esce dal registro perché la tappa 3-28 ora dice Torino (Primo Levi) e non Manchester (Turing). Karakorum non è più un caso dichiarato a parte: la correzione che il controllo dei pin aveva trovato il 2 ottobre sta ora in `dati/luoghi_correzioni.json` e viene riapplicata a ogni rigenerazione.

La correzione che conta è un'altra, ed è quella che ha reso necessaria la prima: **`estrai_luoghi.py` leggeva le colonne per numero, e l'anno 5 ha una colonna in più** — la stanza, fra il pin e la voce — quindi in ventinove tappe su trenta il campo `voce` conteneva il filone del *Furioso* invece della persona. Ora la tabella si legge per intestazione. E il registro non è più un file che si corregge a mano: `aggiorna_registro.py` lo rifa unendo i dati nuovi a quelli che si compilano a mano, perché la versione di prima cancellava il terreno misurato, i dettagli e i trenta binomi pin/stanza del quinto anno.


### v0.2 — 02/10/2026

Controllo di coerenza su tutto il progetto. Tre correzioni, tutte sulla stessa
riga: le **coordinate**. I dati hanno **54 luoghi con coordinate**, dei quali **53
verificati** e uno dichiarato `da_verificare` (Karakorum, il caso dei 8 128 m
descritto sotto): il documento li chiamava tutti e 54 «verificate», che è vero
solo se si ammette che una verifica può fallire. Ora il numero è giusto e il
caso dichiarato è detto. Le **41 coordinate mancanti** erano giuste: sono i 24
luoghi che non sono un luogo, i 10 da geocodificare a mano e i 7 da interrogare
al WFS. Terza correzione: `rilievo_penisola.json` e `rilievo_europa.json` sono
dichiarati **da produrre** e non dati per esistenti: lo script c'è, l'esecuzione
no, e un documento che promette un file inesistente è un documento che un giorno
farà perdere mezz'ora a qualcuno.

### v0.1 — 02/10/2026

Prima stesura. Creati `sorgenti/luoghi/estrai_luoghi.py`, `coordinate.py`,
`classifica.py`, `sorgenti/gis/rilievo.py`; `dati/luoghi_estratti.json`,
`luoghi_geo.jsonl`, `luoghi_gioco.json`, `dettagli_ferrara.json`.

Contenuto: i 95 luoghi del gioco con tappe e anni, 55 coordinate con la fonte e
l'articolo risolto — tutte quante verificate, Karakorum compresa, che il
controllo ha preso con la quota e non con il titolo (v. sotto) —, la
classificazione in sette tipi, la decisione su
ODbL, lo schema del dettaglio con il campo `cronologia`, e il primo record
compilato per intero (Ferrara, sette luoghi, tre vuoti dichiarati).

Cinque difetti trovati e corretti lungo il cammino, tutti verificati contro dati
noti e non a occhio:

1. l'indice del pixel dentro il tassello era quello di un tassello: errore medio
   di 132,6 m, sceso a **12,6 m** con il calcolo del pixel globale;
2. l'estrazione leggeva la colonna sbagliata nell'anno 4, e per venti minuti
   l'inventario ebbe trenta nomi di persone al posto di trenta luoghi — visto
   perché nessuno di quei nomi ha coordinate;
3. tredici edifici e aree erano classificati come «città»;
4. il `429` letto come assenza, per la quarta volta (§5);
5. l'inventario non poteva essere rifatto, perché la colonna del luogo cambia nome
   fra gli anni (`Luogo (pin)` e `Pin`) e le colonne extra non erano dichiarate:
   ora la tabella è letta **per intestazione**, con il perché della correzione
   accanto. È la correzione che il 03/10/2026 ha reso necessaria per un motivo
   nuovo: l'anno 5 ha una colonna in più (la stanza) e il numero fisso leggeva
   la stanza al posto della voce, in ventinove tappe su trenta.

Aggiunto dopo: il **rilievo dei 55 luoghi** con coordinate, e la sua
verifica ha trovato un settimo difetto. **Karakorum è a 8 128 m**: il nome ha
risolto sull'articolo «Karakorum» e il titolo combacia, ma quello non è la
capitale mongola di Gengis Khan, è un altro luogo omonimo. È l'unico caso in cui
il controllo l'ha preso **la quota e non il titolo**, e la scheda porta
`coord_stato: da_verificare`. Il rilievo, insomma, non serve solo a disegnare: fa
anche da controllo sulla geocodificazione, ed è l'unico controllo che l'ha preso.
