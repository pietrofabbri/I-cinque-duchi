---
titolo: Videogioco "I cinque duchi" — i percorsi del duca: mezzi di trasporto, copertura della mappa e ritorni
versione: 0.4
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte: calcolo sulle coordinate di dati/luoghi_gioco.json
documenti collegati: videogioco-5-duchi-luoghi.md (v0.5), videogioco-5-duchi-anno2-penisola.md (v0.2), videogioco-5-duchi-anno3-europa.md (v0.4), videogioco-5-duchi-anno4-mondo.md (v0.5), videogioco-5-duchi-anno5-mondo.md (v0.5), videogioco-5-duchi-audit.md (v0.8), AGENTS.md
---

# I percorsi del duca

## 0. Che cosa chiede questo documento, e che cosa risponde

Il gioco ha 150 tappe, e ogni tappa ha **un solo pin**: il luogo dove il gioco si ferma. Questi pin sono sparsi su un continente intero, o sul mondo intero. La domanda che ne segue è semplice e non era mai stata posta per iscritto:

> **Un uomo di quell'epoca, con i mezzi di quell'epoca, può visitare tutti questi luoghi? In che ordine? Con che cosa viaggia? E se torna indietro, che cosa ci guadagna il gioco?**

Questo documento risponde con dei numeri, non con delle opinioni. I numeri vengono da tre script, tutti ripetibili:

| Script | Che cosa calcola |
|---|---|
| `sorgenti/percorsi_calcola.py` | le distanze fra i pin nell'ordine delle tappe, e i giorni di viaggio |
| `sorgenti/percorsi_confronto.py` | le tre varianti di percorso: **quello delle tappe**, **il giro che copre tutto**, e il giro chiuso col ritorno |
| `sorgenti/percorsi_mezzi.py` | i mezzi di trasporto dell'epoca, e che cosa cambia se il mezzo cambia |

**Che cosa non sono questi numeri.** Non sono distanze stradali: sono **distanze in linea d'aria**, calcolate con la formula dell'haversine sulle coordinate che sono già in `dati/luoghi_gioco.json`. La distanza stradale del Cinquecento è sempre maggiore, e a volte molto maggiore, perché le strade seguono le valli, i guadi e le dogane. Quindi ogni cifra qui è **il minimo teorico**, e il percorso reale è più lungo di quello che il gioco promette. I giorni sono una stima con una velocità dichiarata, non una data storica: servono a capire se un percorso è possibile, non a dire quando si partiva.

---

## 1. I mezzi di trasporto, anno per anno

Il mezzo di trasporto è la prima cosa da capire, perché **determina la velocità con cui la mappa si attraversa** e quindi il numero di tappe che ci stanno in un anno scolastico.

| Mezzo | km al giorno | Persone | Tipo | `dal` | Anno | Nota |
|---|---|---|---|---|---|---|
| A piedi | 25 | 1 | storico | −3000 | **1** | un uomo solo, con la bisaccia |
| Cavallo | 45 | 2 | storico | −3000 | **2, 3** | cavaliere e scudiero, bagagli in sella |
| Galera | 55 | 40 | storico | 1500 | 2, 3 | galera veneziana, i passeggeri pagano |
| Pipa | 8 | 1 | storico | 1600 | 3 | la pianta che in Cinquecento faceva il giro d'Europa |
| Nave | 130 | 300 | storico | −3000 | **4** | veliero latino, rotta dipendente dal vento |
| Carovana | 30 | 60 | storico | −1000 | 4 | strada delle carovane, con le guide |
| Diligenza | 45 | 8 | storico | 1650 | 4 | diligenza delle poste, cambio cavalli ogni 10-12 km |
| Treno | 180 | 200 | storico | 1825 | 4, **5** | convoglio ferroviario, orari fissi, biglietto |
| Aereo | 900 | 300 | storico | 1920 | 4, **5** | volo di linea, con l'attesa all'aeroporto |
| Crociera | 200 | 2000 | storico | 1900 | 5 | nave passeggeri: l'attesa è il costo vero |
| **Moto** | 250 | 2 | storico | **1903** | **4**, 5 | 500 km al giorno con due soste, e le soste sono il costo |
| **Sci** | 40 | 2 | storico | **1900** | **4**, 5 | 30 km/h di media, e la salita si paga |
| **Elicottero** | 320 | 4 | storico | **1936** | 4, 5 | la rotta più breve in assoluto, il costo più alto |
| **Monopattino** | 30 | 1 | storico | **2001** | 4, 5 | 20 km/h: mezzo urbano, serve per l'ultimo tratto |

**Le due colonne nuove, e perché non sono un vezzo.** `tipo` dice se il numero è una stima discussa (`storico`) o una convenzione dichiarata (`gioco`). `dal` è l'anno di attestazione del mezzo, ed è il dato che rende possibile il controllo degli anacronismi: **è la ragione per cui la colonna esiste.** Senza `dal`, un elicottero in una tappa del 1300 passerebbe inosservato.

### 1.1 I mezzi che sono soltanto del testo

Il quinto anno è anche l'anno dei mezzi che esistono solo nell'edizione del 1516, e sono cinque. Non sono un vezzo: sono **la regola dei due strati applicata alla velocità** (`luoghi.md` §4.5). Il pin è reale e va in treno; la stanza è del poema e si attraversa a cavallo di Astolfo.

| Mezzo | km al giorno | Persone | Il verso, e donde viene |
|---|---|---|---|
| **Ippogrifo** | 500 | 1 | «una giumenta generò d'un grifo» — c. IV, 18 |
| **Drago** | 400 | 2 | «sí duro intorno ha lo scaglioso drago» — c. XVIII, 12 |
| **Sirena** | 200 | 1 | «la sirena che col suo dolce canto acheta il mare» — c. VI, 40 |
| **Carro di delfini** | 250 | 2 | «che fatto al carro i suoi delfini porre» — c. XI, 44 |
| **Carro di serpenti** | 250 | 2 | «sul carro che tiravan dui serpenti» — c. XII, 2 |

**Il numero che hanno non è una velocità, e il gioco lo dice.** Sono convenzioni dichiarate, il campo `tipo` dice `gioco` perché nessuno le legga come un dato storico, e ogni versione della tabella porta la scritta. Il confronto che vale non è «quanto ci si arriva»: sui 79 494 km del quinto anno l'aereo fa 106 giorni, il treno 530, l'ippogrifo 191 — e la domanda che il gioco pone è **«che cosa è successo in mezzo?»**.

### 1.2 Il riscontro fra il mezzo di allora e il mezzo di oggi

*(03/10/2026 — `sorgenti/percorsi_mezzi.py`)*

Aggiungere i mezzi nuovi ha reso insufficiente il controllo per anno, e il perché merita di essere scritto: **l'anno 4 non è un'epoca.** Va dalle tavolette di Uruk a Orwell, e in un anno solo ci sono tremilaseicento anni. Un controllo che dicesse «nell'anno 4 si può andare in elicottero» direbbe una cosa vera per la tappa 4-29 e falsa per la tappa 4-1.

La prima stesura del controllo cercava quindi «un mezzo che non esisteva alla data della tappa in cui è usato», e **ne trovava uno solo: l'anno 5 è l'anno di Alfonso II (1597), e lì non esisteva né il treno né l'aereo.** Ma il mezzo di cui si parla non è il mezzo di Alfonso: è il mezzo con cui il materiale di Alfonso arriva *all'archivio*, e l'archivio è del presente. **Un anacronismo qui non è un errore: è la risposta.**

Il controllo giusto è un confronto, e cerca un difetto solo: **il mezzo di oggi non può essere più lento di quello di allora.** Il risultato è anche la tabella più informativa del capitolo — la ripartizione dei mezzi che escono dalle trenta date di un anno:

| Anno | Mezzi di allora nelle trenta tappe |
|---|---|
| **4** | nave 23, aereo 5, treno 1, moto 1 |
| **5** | aereo 26, treno 1 |

Il ventitré su trenta dell'anno 4 è la nave, e i cinque aerei sono le tappe degli anni Trenta: il file **calcola** il mezzo di ogni tappa dalla data, non lo dichiara a mano. Se si domanda un anno, il risultato cambia da solo.

### 1.3 Le due colonne di mezzi, e perché sono due domande

Il quarto anno ha **due** serie di mezzi, ed è la parte di questo capitolo che non si può comprimere:

- **chi viaggia** — chi porta il documento, con i mezzi che esistevano alla data della tappa. Qui l'anacronismo è un difetto e il controllo lo segnala;
- **con che cosa arriva il giocatore** — gli stessi luoghi, con i mezzi di oggi: moto, sci, elicottero, monopattino. Qui l'anacronismo non è un difetto ma **il contenuto della domanda**, perché la domanda del gioco è «che cosa è cambiato?». Per questo la seconda colonna sta **fuori** dal controllo degli anacronismi, ed è dichiarato che sta fuori.

Il caso che rende la distinzione inevitabile è l'anno 4: **monopattino 2001 per raggiungere Tebe, e il giocatore ci va oggi in monopattino.** Le due cifre non si contraddicono, sono due domande diverse, e il gioco le mostra entrambe perché il ragazzo vede che dal 2001 a oggi un luogo è diventato vicino.

**Perché questi e non altri.**

**L'anno 1 si fa a piedi.** Ferrara è piccola: dalle mura ai confini del territorio ci si va a piedi, e il percorso di Borso dentro le mura non ha bisogno di altro. La distanza maggiore fra due tappe dell'anno 1 è di poche centinaia di metri.

**Gli anni 2 e 3 si fanno a cavallo e in galera.** Sono gli anni della penisola e dell'Europa, e sono gli anni in cui la strada delle poste è un'infrastruttura vera, già organizzata: esistono le stazioni di cambio dei cavalli, e il tempo di un viaggio si misura in **posti**, non in chilometri. La galera veneziana collega l'Adriatico al Mediterraneo, ed è il modo in cui si va da Venezia a Palermo senza passare per la Terraferma.

**L'anno 4 non è un viaggio: è un arrivo.** L'unico luogo percorribile del quarto anno è **l'archivio della corte** (`anno4-mondo.md` §3). Il duca non va a Tenochtitlán: **a Tenochtitlán arriva un documento**. Il mezzo di trasporto dell'anno 4 è la **nave** (per il materiale che viene dall'Asia e dalle Americhe), la **carovana** (per quello che viene dall'Africa e dall'Oriente via terra) e la **diligenza** (per quello europeo). Il percorso che conta, in quell'anno, è la rotta di chi porta il documento, non quella di chi lo riceve.

**L'anno 5 si fa in treno e in aereo.** Sono i mezzi del presente, e sono veloci abbastanza da coprire il mondo in un anno. Ma il tempo di attesa all'aeroporto è il costo vero, e per questo nel quinto anno il mezzo «treno» conta più dell'«aereo» anche se è quattro volte più lento: si arriva in città. **E a questi si aggiungono i mezzi che sono soltanto del testo** (§1.1): cinque, con la fonte sul verso, e la stanza del *Furioso* si attraversa con quelli.

**L'anno 4 ha due serie di mezzi, ed è il punto in cui la domanda si sdoppia** (§1.3). Chi porta il documento usa i mezzi dell'epoca della tappa — la nave per ventitré tappe su trenta, l'aereo per le cinque degli anni Trenta. Il giocatore ci arriva oggi con gli altri quattro. Il perché è didattico: **è l'unico anno in cui la stessa tabella può dire che nel 1300 per andare a Tebe ci si metteva un mese e oggi ci si mette un'ora.**

---

## 2. Il problema che i numeri mostrano: l'ordine delle tappe raddoppia il viaggio

Ecco il primo dato che il calcolo produce, e non è quello che ci si aspettava.

| Anno | Pin in percorso obbligatorio | Chilometri (ordine tappe) | Chilometri (giro che copre tutto) | Differenza | Giorni risparmiati |
|---|---|---|---|---|---|
| **2** | 9 | 3 139 | 2 153 | **−31%** | 29 |
| **3** | 22 | 18 318 | 9 308 | **−49%** | 264 |
| **4** | 13 | 58 644 | 33 177 | **−43%** | 260 |
| **5** | 15 | 79 494 | 33 511 | **−58%** | 66 |

L'ordine dei numeri di tappa **non è un ordine di viaggio**. È un ordine di argomenti: la tappa 3-28 è sul Novecento perché il livello lo richiede, non perché sia sulla strada fra Atene e Manchester. Il risultato è che il percorso che il gioco propone oggi **fa il giro del mondo due volte**.

**L'anno 3, in particolare, è il caso più chiaro.** Ventidue pin in Europa, nell'ordine delle tappe, sono **18 318 chilometri e 539 giorni**: quasi un anno e mezzo di viaggio a cavallo. Il giro che copre tutti e ventidue i luoghi, nell'ordine che un viaggiatore avrebbe scelto, è **9 308 km e 275 giorni** — poco più di nove mesi, che è ancora tanto ma è la metà.

---

## 3. Le tre ipotesi di percorso

### 3.1 Prima ipotesi — il percorso delle tappe: si tiene, e diventa una scelta narrativa

**Che cosa è.** Il duca segue l'ordine dei numeri di tappa, cioè l'ordine degli argomenti.

**Pro.** È già nei dati, non richiede di cambiare nulla, e ha una difesa narrativa forte: il duca non viaggia per luoghi, **viaggia per quello che impara**. Ogni tappa è un argomento, e l'argomento viene prima del luogo.

**Contro.** Costa il doppio del giro, e soprattutto **non copre la mappa in modo leggibile**: il giocatore vede il segnale andare avanti e indietro senza capire perché.

**Quando sceglierla.** Se il percorso del duca resta un **dettaglio** e la mappa si mostra per tappa, senza un filo che la colleghi.

### 3.2 Seconda ipotesi — il giro: la mappa ha un filo, e l'ordine delle tappe non è quello del viaggio

**Che cosa è.** Si separa **l'ordine delle tappe** (l'ordine degli argomenti, che non si tocca) dall'**ordine del viaggio** (l'ordine geografico). Il gioco ha due sequenze: quando si guarda la mappa, il percorso del duca è un giro che parte da Ferrara, tocca tutti i luoghi dell'anno e torna; quando si gioca una tappa, si gioca al numero giusto, e la mappa dice dove siamo.

**Pro.** Copre tutta la mappa con il **minimo possibile di viaggio** (il calcolo «vicino più vicino» dà il giro più corto). È un percorso che un viaggiatore avrebbe davvero scelto. E rende visibile al giocatore che **fra due tappe c'è una strada**, che è ciò che la mappa a strati degli anni 2 e 3 prometteva.

**Contro.** Richiede di cambiare il modo in cui la mappa si disegna: non più «la tappa 3-12 è qui» ma «il percorso è questo, e la tappa 3-12 è la dodicesima fermata». È un lavoro di motore, non di dati.

**Quando sceglierla.** Se si vuole che la mappa sia un percorso e non una distribuzione di punti. **È la mia raccomandazione**, perché è quella che rende il gioco un gioco di viaggio e non un questionario.

### 3.3 Terza ipotesi — il giro chiuso: tornare indietro è la regola, non l'eccezione

**Che cosa è.** Come la seconda, ma il giro **si chiude**: il duca parte da Ferrara e **torna a Ferrara**. Il ritorno non è un costo, è un atto.

**Pro.** Il ritorno è il momento in cui il gioco ha la parte migliore da offrire, e il progetto lo sa già: **è lì che fanno la comparsa i personaggi nuovi**.

**Contro.** Costa il viaggio di chiusura: **+343 km** nell'anno 2, **+1 391 km** nell'anno 3, **+9 807 km** nell'anno 4, **+11 295 km** nell'anno 5, cioè fra i 10 e i 101 giorni di viaggio. Ma il gioco non li fa pagare al giocatore: sono giorni in cui non c'è tappa, e il viaggio stesso è un esercizio.

---

## 4. Il ritorno: perché è il momento giusto per far comparire i personaggi nuovi

Il ritorno non è un dettaglio logistico. È **la struttura narrativa che il gioco usa già** nei suoi pezzi migliori, e la tabella dei mezzi lo rende possibile.

Il motivo è semplice: **andare è il viaggio dell'andare**. Il ritorno è il viaggio del ritorno, e su quel viaggio il duca non porta niente e non cerca niente: **incontra**. Le persone che incontrerebbe sul viaggio di ritorno sono esattamente quelle che il catalogo ha e che nessuna tappa usa: i mestieranti, i mercanti, gli studenti, i funzionari delle poste, i navigatori.

**Il dispositivo, in pratica.**

1. Il giocatore fa il giro e arriva all'ultimo luogo.
2. Sulla strada del ritorno, **una tappa facoltativa si apre ogni volta che il percorso passa davanti a un luogo che ha già una scheda**.
3. La tappa facoltativa è un **incontro**: non un argomento, non un esercizio di informatica, ma una persona che dice chi è e da dove viene.
4. Il giocatore che prende tutte le facoltative del ritorno vede il catalogo completo; quello che non le prende vede quello che ha scelto di vedere.

**Perché questo è lecito e non è un trucco.** Le facoltative non sbloccano niente (`lingue.md` §5.2, la regola dei facoltativi), quindi il ritorno non rende il gioco più facile né più difficile. E l'incontro è informazione vera, non ricompensa: la persona che si incontra racconta chi è, e quella scheda era già nel catalogo.

---
## 5. Coprire tutta la mappa, e andare oltre

Il secondo punto della domanda: la mappa deve essere coperta **tutta**, e si deve poter andare **oltre**. Qui c'è un equivoco da sciogliere, perché «la mappa» non è una cosa sola.

### 5.1 Che cosa copre ogni anno, davvero

| Anno | Che cosa è la mappa | Quanti pin la coprono | Che cosa manca |
|---|---|---|---|
| **1** | le mura di Ferrara | 30 tappe in 32 luoghi tutti dentro Ferrara | niente: la città è piccola e il percorso la copre intera |
| **2** | la penisola, a strati | 9 pin per tappe numerate, più porte e zone | **manca la Sardegna**, che è nella mappa e non ha tappa |
| **3** | l'Europa, a strati | 22 pin | **mancano l'Inghilterra fuori Westminster, la Scozia, il Portogallo, la Danimarca, i Balcani** |
| **4** | il mondo, a 16 strati | 13 pin con coordinate | **mancano le Americhe del Nord, il Canada, l'Australia, l'Africa occidentale** |
| **5** | il tempo, non lo spazio | 15 pin | **non è un buco**: l'anno 5 non ha una mappa da coprire, ha una linea del tempo |

**Il caso dell'anno 2 è il più netto.** Nove pin su trenta tappe, perché molte tappe dell'anno 2 non hanno un pin proprio ma passano da una **porta** (Ferrara, la città da cui parte il viaggio) o sono **zone** della carta. Il calcolo del percorso, quindi, riguarda nove luoghi, non trenta: **le altre ventuno tappe non sono spazio, sono informazione che arriva a Ferrara**. È la struttura che `luoghi.md` §4.7 ha già dichiarato, e qui emerge con le sue conseguenze: **un percorso del duca nell'anno 2 si fa fra nove luoghi**, e le altre tappe sono lettere, ambasciatori e volumi.

### 5.2 Il buco geografico è il compito del facoltativo

`luoghi.md` §4.7 ha già deciso che i buchi geografici diventano **facoltative continentali**: il Brasile, la Corea, l'Indonesia, la Nuova Zelanda, il Canada, l'Artide, l'Ungheria, la Romania, la Scandinavia, i Balcani, la Puglia. Sono **undici**, e sono già scelte.

Il calcolo del percorso dice che **quelle undici facoltative sono ciò che manca alla copertura**, e le rende preziose. Se il giro copre tutti i pin dell'anno, le facoltative continentali sono le uniche tappe che portano il duca **fuori dal continente** — e il ritorno dal continente diventa la parte più lunga del viaggio.

Questo suggerisce una cosa che il progetto non aveva considerato: **le facoltative continentali vanno aperte sul ritorno**, non sul viaggio di andata. Un punto per cui vale la pena scriverlo, e che va deciso (§8 Q4):

- Sul viaggio di andata il giocatore è sulle tracce di ciò che il duca sta cercando, e la facoltativa continentale è una deviazione che non serve.
- Sul ritorno il duca ha visto tutto quello che si poteva vedere in patria, e la facoltativa continentale diventa **l'unica cosa che manca**: il «e da fuori, invece?».

### 5.3 Andare oltre la mappa: che cosa c'è oltre

«Oltre» la mappa, nel gioco, è già definito in tre modi, e nessuno dei tre è «oltre la mappa»:

1. **Le undici facoltative continentali** (§5.2), che portano fuori dal continente.
2. **Le facoltative linguistiche dei 900 livelli** (`lingue.md` §5), che portano fuori dal percorso: un oggetto con cui si interagisce e che è in un'altra lingua.
3. **I trecento livelli informatici** che il primo anno non ha (`audit.md` B1), che sono l'unico «oltre» che non ha coordinate.

Il gioco, insomma, ha già tre maniere di andare oltre la mappa, e nessuna delle tre è un'altra mappa. Va detto, perché è il tipo di scoperta che si fa meglio adesso che dopo aver costruito il motore.

---

## 6. L'anno 1, che è il caso diverso

L'anno 1 non ha nessuno dei problemi di questo documento, e merita due righe per non sembrare dimenticato.

Borso non viaggia: **cammina dentro le mura**. La città del 1450 è percorribile a piedi in poco più di un'ora, e il gioco ha già deciso che il percorso dell'anno 1 è «unico e contiguo dentro le mura, non cronologico» (`AGENTS.md` §3, Anno 1). Non c'è mezzo di trasporto da capire e non c'è mappa da coprire.

Il percorso dell'anno 1 è quindi il **modello** degli altri: trenta tappe contigue, tutte raggiungibili a piedi, tutte dentro uno spazio che si vede tutto. Gli anni 2 e 5 possono prendersi la libertà del viaggio proprio perché l'anno 1 ha già mostrato cosa significa «un percorso che copre tutto» — e hanno il vantaggio che l'anno 1 è l'unico in cui la copertura è gratuita.

---

## 7. Che cosa è calcolato e che cosa è ipotizzato

È la distinzione che conta per non confondere i due tipi di affermazione.

**Calcolato, ripetibile, sul file:**
- le distanze in linea d'aria fra i pin, con l'haversine sulle coordinate di `dati/luoghi_gioco.json` (`percorsi_calcola.py`, `percorsi_confronto.py`);
- i giorni di viaggio, con le velocità dichiarate in `percorsi_mezzi.py`;
- il giro più corto, che è l'euristica del vicino più vicino applicata a questi insiemi.

**Ipotizzato, e da discutere:**
- che le velocità siano quelle giuste per quell'anno (un cavallo a 45 km al giorno è plausibile, ma non è una data da fonte);
- che il giro chiuso sia preferibile al giro aperto;
- che i ritorni siano il momento giusto per i personaggi nuovi;
- che le facoltative continentali si aprano sul ritorno.

**Non calcolato, perché manca il dato:**
- le **distanze stradali**, che sono il vero costo di un viaggio del Cinquecento e che nessuno dei tre script stima;
- i **tempi di attesa**, che sono il vero costo di un viaggio in nave e in aereo: una nave dipende dal vento, un aereo dall'aeroporto.

---

## 8. Le questioni aperte

### Q1 — Il percorso del duca è l'ordine delle tappe o è un giro a parte? **(la decisione più importante)**

È la prima ipotesi contro la seconda di §3. La prima non costa niente e non copre la mappa; la seconda copre la mappa e costa un lavoro di motore. La raccomandazione è la seconda, ma la decisione è di Pietro.

### Q2 — Il giro si chiude a Ferrara? **(la terza ipotesi)**

Il ritorno è il dispositivo che fa comparire i personaggi nuovi (§4), ma costa 10-101 giorni di viaggio. Il gioco non li fa pagare: li usa come esercizio di viaggio.

### Q3 — Che mezzo usa il duca, e quando lo cambia?

I mezzi sono in §1, ma la domanda aperta è se **il mezzo cambia dentro l'anno**. Sarebbe la cosa più bella: nell'anno 4 il duca non viaggia, e il mezzo è quello **di chi porta il documento**, quindi cambia a seconda della provenienza (nave per l'Asia, carovana per l'Africa, diligenza per l'Europa). Se il mezzo è dichiarato sulla scheda del documento che arriva, il giocatore impara a distinguere le rotte dal mezzo, che è esattamente il tipo di conoscenza che il gioco promette.

### Q4 — Le facoltative continentali si aprono sul ritorno?

L'ipotesi è che il ritorno le renda preziose (§5.2). Se si aprono sul ritorno, l'anno 4 diventa un anno di arrivi e di partenze, che è il suo tema.

### Q5 — Che cosa succede ai buchi geografici degli anni 3, 4 e 5?

L'anno 2 ha la Sardegna scoperta, l'anno 3 ha cinque regioni europee senza tappa, l'anno 4 ha quattro continenti senza pin. Sono buchi, e `luoghi.md` §4.7 li ha già trattati come facoltative continentali per l'anno 4. Per gli anni 2 e 3 la cosa è diversa, perché lì il buco è **incontinentale**, non solo continentale. La domanda è se si accetta che l'anno 3 copra l'Europa «di chi ci scrive», cioè quella che Alfonso I poteva conoscere, e non l'Europa geografica.

### Q6 — Il tempo di viaggio è un esercizio?

Se fra due tappe ci sono dodici giorni di strada, il gioco può (a) mostrarne uno solo, (b) farlo giocare come esercizio di percorso, (c) dichiararlo e saltarlo. Il progetto ha già deciso che i meccanismi non richiedono di scrivere testo e che tutto si fa col tocco, quindi (b) è possibile ma è un meccanismo nuovo.

---

## 9. Registro delle modifiche

| Data | Versione | Che cosa è cambiato |
|---|---|---|
| 03/10/2026 | 0.4 | **I mezzi diventano ventidue e il capitolo acquista tre sezioni.** Otto mezzi storici nuovi — treno e aereo passano anche all'anno 4, e arrivano crociera, **moto**, **sci**, **elicottero** e **monopattino**; e cinque mezzi **del testo** per il quinto anno, con il canto e l'ottava accanto: l'ippogrifo (c. IV, 18), il drago (c. XVIII, 12), la sirena (c. VI, 40), il carro di delfini (c. XI, 44) e il carro di serpenti (c. XII, 2). Ogni mezzo porta due campi nuovi, `tipo` (`storico` o `gioco`) e `dal` (l'anno di attestazione). **Il `dal` è la ragione della modifica**: senza di esso un elicottero in una tappa del 1300 passerebbe inosservato. Il controllo degli anacronismi è diventato **per tappa** (§1.2), perché l'anno 4 non è un'epoca, e il primo calcolo ha trovato un difetto vero nella propria impostazione: cercava un mezzo inesistente alla data della tappa e segnalava l'anno 5 di Alfonso II, dove non c'era né treno né aereo — ma il mezzo di cui si parla è quello **con cui il materiale arriva all'archivio**, che è del presente. Il controllo giusto confronta il mezzo di allora con quello di oggi e cerca un difetto solo: che quello di oggi non sia più lento. La ripartizione che ne esce è la tabella più informativa del capitolo (anno 4: nave 23, aereo 5, treno 1, moto 1) ed è **calcolata dalle date, non scritta a mano**. |
| 03/10/2026 | 0.3 | Solo rimandi, come alla v0.2: `luoghi.md` sale a v0.4 (la verifica F16 dei filoni) e `audit.md` a v0.6 (I19 chiusa, il conto a 28 chiuse e 86 aperte). **Nessuna cifra di questo documento cambia**: i percorsi sono calcolati sulle coordinate di `dati/luoghi_gioco.json`, che non sono state toccate. |
| 03/10/2026 | 0.2 | Solo rimandi: l'audit sale a v0.5 e `mappe.md` a v0.7 dopo le chiusure del 3 ottobre (tavolozza, sagome degli edifici, fondo di Ferrara, ambienti dei 150 livelli e file amministrativo mondiale). **Nessuna cifra di questo documento cambia**: i percorsi sono calcolati sulle coordinate di `dati/luoghi_gioco.json`, che il 3 ottobre non è stato toccato. |
| 02/10/2026 | 0.1 | Prima stesura. Calcolati i percorsi del duca per gli anni 2, 3, 4 e 5 sulle coordinate di `dati/luoghi_gioco.json`: **tre varianti** (l'ordine delle tappe, il giro che copre tutto, il giro chiuso), i **mezzi di trasporto** dell'epoca con le velocità dichiarate, e il fatto che **l'ordine dei numeri di tappa raddoppia il viaggio** (−31% fino a −58%). Le tre ipotesi di percorso, il ritorno come momento degli incontri, la copertura della mappa anno per anno con i buchi, e la proposta di aprire le facoltative continentali sul ritorno. Sei questioni aperte, di cui la prima è una decisione di progetto e non un lavoro. |