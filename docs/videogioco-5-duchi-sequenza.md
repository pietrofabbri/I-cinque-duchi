---
titolo: Videogioco "I cinque duchi" — la sequenza degli anni 2, 3 e 4: le trenta voci obbligatorie in fila, con i luoghi e le distanze
versione: 0.2
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte del materiale: richiesta di Pietro del 03/10/2026 («hai la sequenza dei livelli per i 4 anni, con relativi luoghi, quindi puoi mettere in sequenza i vari personaggi (almeno quelli non facoltativi)»), con le regole già prese sui percorsi, sui tipi di legame e sulle ipotesi di coordinata
dati: dati/sequenza_tappe.json (v1, generato da sorgenti/sequenza_tappe.py: le novanta tappe degli anni 2, 3 e 4 con luogo, voce, mezzo, distanza e giorni); dati/luoghi_gioco.json (il registro, da cui vengono le coordinate); dati/ipotesi_luoghi.json (le quarantanove coordinate che il registro non puo' verificare)
controllo: python3 sorgenti/sequenza_tappe.py (rigenera il JSON e le tre tabelle di questo documento); python3 sorgenti/verifica_sequenza.py (S1-S6: trenta tappe per anno in ordine, una voce obbligatoria per tappa e nessuna ripetuta, le facoltative fuori dalla sequenza, nessun punto mancante senza dichiarazione, e le distanze che combaciano con i km al giorno dichiarati nei percorsi)
documenti collegati: videogioco-5-duchi-anno2-penisola.md (v0.2), videogioco-5-duchi-anno3-europa.md (v0.4), videogioco-5-duchi-anno4-mondo.md (v0.5), videogioco-5-duchi-percorsi.md (v0.4, il percorso del duca, che qui non e' lo stesso), videogioco-5-duchi-luoghi.md (v0.5, i tipi di legame e le ipotesi), videogioco-5-duchi-ritratti.md (v0.2), AGENTS.md
---

# La sequenza degli anni 2, 3 e 4

## 0. Che cosa c'è qui, e che cosa non c'è

Qui c'è **una fila**: per ogni anno, le trenta tappe nell'ordine in cui il giocatore le incontra, con il luogo, la voce che incontra e la distanza dalla tappa precedente. Le voci sono le **trenta obbligatorie** di ogni anno: quelle che il giocatore incontra per forza, e le facoltative stanno nella loro colonna, fuori dalla sequenza, perché una sequenza che le include mente sul percorso che fa.

**Che cosa non c'è, e perché.** Non c'è l'anno 1 (le trenta tappe sono tutte dentro Ferrara, a pochi metri l'una dall'altra: la fila sarebbe `Borso, San Maurelio, via Manzoni…` e non insegnerebbe niente) e non c'è l'anno 5 (che ha già la sua tabella a colonna stanza in `anno5-mondo.md` §4).

**Le tabelle qui sotto non sono scritte a mano.** Le genera `sorgenti/sequenza_tappe.py` leggendo le tabelle delle trenta tappe dei tre documenti d'anno, e se il generatore non le aggiorna la tabella mente senza che nessuno se ne accorga. Il comando è in §5.

## 1. Il difetto che questa sequenza ha trovato

Costruire la fila ha fatto emergere una cosa che nessuno dei controlli precedenti vedeva, e che vale più della fila: **la tappa 4-16 ha due luoghi diversi in due file diversi, e quello che aveva nel registro era il posto sbagliato**.

Il 2 ottobre 2026 Pietro sostituì Ibn Khaldun con Ashoka alla 4-16 e Ibn Khaldun divenne la facoltativa forte della stessa tappa. Il documento dell'anno 4 fu aggiornato — 4-16 = **Pataliputra**, che è il luogo di Ashoka — ma **il registro dei luoghi non fu rigenerato** e continuava a portare «Tunisi e Il Cairo», che era il luogo di Ibn Khaldun: Tunisiano, e al Cairo dove visse.

Le **ipotesi di coordinata** del 3 ottobre costruirono sopra quel posto sbagliato una strada Tunisino-Cairo, con la fonte che diceva «partenza Tunisi, arrivo Il Cairo» e la frase che il gioco avrebbe mostrato al ragazzo attribuita ad **Ashoka**. Il record era internamente coerente, aveva due punti, aveva il tratto, aveva la fonte: e i sei controlli R1-R6 gli avevano dato il via libera. **Un controllo che verifica la forma non verifica la premessa**: io ho controllato che la strada fosse ben costruita e non che la strada fosse quella giusta.

La 4-16 è ora **Pataliputra** e la strada Tunisino-Cairo sparisce con lei: i nomi doppi con il tratto passano da otto a sette, e la distanza dell'anno 3 è cambiata di 1108 km perché la 3-28 è passata da Manchester a Torino. Il punto viene dalla tabella del documento, non dalla mano.

**La causa, e come è stata chiusa.** Il 3 ottobre la correzione era stata scritta **a mano** in `dati/luoghi_gioco.json`, perché il generatore del registro (`sorgenti/luoghi/classifica.py`, con `estrai_luoghi.py` e `coordinate.py`) riscrivendo il file avrebbe cancellato quattro cose che nessun comando rifa: il terreno misurato su SRTM, il campo `controllo`, i `dettagli` compilati a mano e il blocco `tappe` con i trenta binomi pin/stanza del quinto anno. Una correzione che non si può rigenerare è una correzione che nessuno può rifare: il 3 ottobre, infatti, il generatore **rifacendo il registro avrebbe rimesso il valore vecchio**, perché il file degli estratti era rimasto indietro rispetto ai documenti.

Il 3 ottobre la catena è stata sistemata per bene, in quattro mosse, e ognuna ha un controllo suo (`sorgenti/verifica_catena_luoghi.py`, cinque):

1. **`estrai_luoghi.py` legge le colonne per intestazione, non per numero.** Nell'anno 5 la tabella ha una colonna in più — la `Stanza`, fra il pin e la voce — e il numero fisso prendeva la stanza come se fosse la voce: in ventinove tappe su trenta il campo `voce` conteneva il filone del *Furioso* invece della persona. Il sintomo era che il nome sembrava già un titolo: «la strada della fuga di Rinaldo `F2` 1,32». Non se n'era accorto nessuno, perché nessuno leggeva centoventi nomi di persona in un colpo.
2. **`aggiorna_registro.py` unisce invece di sovrascrivere**, e porta dietro i campi compilati a mano.
3. **`dati/luoghi_correzioni.json` dichiara le correzioni che i controlli hanno trovato** — Baghdad e Karakorum — che prima vivevano solo nel JSON editato a mano e sparivano alla prima rigenerazione.
4. **Il registro è stato rigenerato davvero**: la 4-16 prende Pataliputra dalla tabella, la 3-28 prende Torino, e **le divergenze fra registro e documento sono passate da una a zero**. La lista `DICHIARATE` di `sequenza_tappe.py` resta nel codice, vuota e dichiarata.

La lezione che resta è quella che l'aveva fatto nascere: **un controllo che verifica la forma non verifica la premessa**, e un dato corretto a mano è un dato che nessuno può ricostruire.

## 2. Le tre sequenze, e che cosa dicono

<!-- SEQUENZA:INIZIO -->
### Anno 2 — la penisola

*cavallo, 45 km al giorno. Percorso in linea d'aria: **8404 km in 194 giorni**. Voci obbligatorie distinte: **30**. Facoltative dichiarate in tabella: **59**. Tappe senza punto: nessuna.*

| # | Tappa | Luogo (pin) | Voce obbligatoria | Forza | Facoltative (2) | | km dalla precedente | giorni | km cumulati |
|---|---|---|---|---|---|---|---|---|
| 1 | **2-1** | Bolzano, Museo archeologico altoatesino | Ötzi `Q01` | forte | La Dama di Verrucchio; i popoli della penisola |  |  | 0 |
| 2 | **2-2** | Crotone | Pitagora `Q11` | forte | Archita; Al-Khwārizmī | 948 | 21 | 948 |
| 3 | **2-3** | Roma, area del Campidoglio | Romolo `Q05` | medio | Tarquinio il Superbo; Lucrezia | 501 | 11 | 1450 |
| 4 | **2-4** | Squillace, monastero di Vivarium | Cassiodoro `Q34` | medio | I copisti | 503 | 11 | 1952 |
| 5 | **2-5** | Roma | Appio Claudio Cieco `Q19` | forte | Camillo; Cincinnato | 503 | 11 | 2455 |
| 6 | **2-6** | Elea (Velia) | Parmenide `Q12` | medio | Zenone di Elea; i fisici di Crotone | 295 | 7 | 2750 |
| 7 | **2-7** | Roma, Tuscolo | Cincinnato `Q17` | medio | Camillo; Catone il Censore | 274 | 6 | 3024 |
| 8 | **2-8** | Milano | Leonardo da Vinci `Q63` | forte | Isabella d'Este; Leonello d'Este | 497 | 11 | 3521 |
| 9 | **2-9** | Roma, Curia | Cicerone `Q21` | forte | Cornelia; gli ambasciatori | 478 | 11 | 3998 |
| 10 | **2-10** | Roma, villa dei Gracchi | Cornelia, madre dei Gracchi `Q27` | medio | Tiberio Gracco; Gaio Gracco | 4 | 1 | 4003 |
| 11 | **2-11** | Elea (Velia) | Zenone di Elea `Q13` | forte | Parmenide; Appio Claudio | 295 | 7 | 4298 |
| 12 | **2-12** | Porta `PT-CAR` (Ferrara) | Annibale `Q22` | medio | Scipione l'Africano; Catone il Censore | 595 | 13 | 4893 |
| 13 | **2-13** | Roma | Catone il Censore `Q26` | medio | Tiberio Gracco; Scipione l'Africano | 335 | 7 | 5228 |
| 14 | **2-14** | Firenze | Dante Alighieri `Q47` | medio | Petrarca; Boccaccio | 232 | 5 | 5459 |
| 15 | **2-15** | Palermo | Federico II di Svevia `Q44` | medio | Costanza d'Altavilla; Manfredi | 653 | 15 | 6113 |
| 16 | **2-16** | Taranto | Archita di Taranto `Q14` | medio | Pitagora; Euclide | 424 | 9 | 6537 |
| 17 | **2-17** | Roma | Tiberio Gracco `Q28` | forte | Cesare; Catone Uticense | 428 | 10 | 6965 |
| 18 | **2-18** | Roma | Giulio Cesare `Q20` | medio | Cicerone; Cleopatra | 0 | 1 | 6965 |
| 19 | **2-19** | Chiusi | Lars Porsenna `Q10` | medio | Teodolinda; i coloni | 132 | 3 | 7098 |
| 20 | **2-20** | Roma | Augusto `Q29` | forte | Ottaviano giovane; Agrippa | 132 | 3 | 7230 |
| 21 | **2-21** | Porta `PT-AQU` (Ferrara) | Carlo Magno `Q37` | medio | Matilde di Canossa; le città del Nord | 335 | 7 | 7565 |
| 22 | **2-22** | Venezia | Marco Polo `Q46` | medio | Francesco Sforza; i mercanti | 87 | 2 | 7652 |
| 23 | **2-23** | Roma, Curia | I copisti e gli amanuensi (Q91, collettivo `C`) | medio | Il tipografo; Lucrezia | 395 | 9 | 8047 |
| 24 | **2-24** | Firenze | Leon Battista Alberti (Q62, *aggiunta*) | forte | Enigma; i cifrari di Stato | 232 | 5 | 8279 |
| 25 | **2-25** | Ferrara, zona dell'Addizione Erculea | Biagio Rossetti (Q64, *aggiunta*) | forte | Ercole I; i muratori | 123 | 3 | 8402 |
| 26 | **2-26** | Ferrara, corte | Lucrezia Borgia `Q41` | forte | Isabella d'Este; Tasso | 2 | 1 | 8404 |
| 27 | **2-27** | Porta `PT-CON` (Ferrara) | Giustiniano `Q35` | medio | Alboino; Teodolinda | 0 | 1 | 8404 |
| 28 | **2-28** | Ferrara, corte | I corrieri e i messaggeri (Q90, collettivo `C`) | medio | Cristoforo Colombo; Amerigo Vespucci | 0 | 1 | 8404 |
| 29 | **2-29** | Porta `PT-COL` (Ferrara) | Amerigo Vespucci `Q45` | forte | Colombo; i copisti | 0 | 1 | 8404 |
| 30 | **2-30** | Ferrara, corte | Il consiglio di corte: i progettisti, i muratori, i proprietari, i contadini (Q92, collettivo `C`) | forte | Ercole I; le donne della corte | 0 | 1 | 8404 |

### Anno 3 — l'Europa

*cavallo, 45 km al giorno. Percorso in linea d'aria: **20098 km in 450 giorni**. Voci obbligatorie distinte: **30**. Facoltative dichiarate in tabella: **61**. Tappe senza punto: nessuna.*

| # | Tappa | Luogo (pin) | Voce obbligatoria | Forza | Facoltative (2) | | km dalla precedente | giorni | km cumulati |
|---|---|---|---|---|---|---|---|---|
| 1 | **3-1** | Alessandria | Eratostene `Q101` | forte | Archimede; i matematici di Alessandria |  |  | 0 |
| 2 | **3-2** | Frombork | Copernico `Q102` | forte | Keplero; Tycho Brahe | 1315 | 29 | 1315 |
| 3 | **3-3** | Roma | Augusto `Q103` | medio | Traiano; Adriano | 1484 | 33 | 2798 |
| 4 | **3-4** | Atene | Solone `Q104` | forte | Pericle; Socrate | 1052 | 23 | 3850 |
| 5 | **3-5** | Atene | Pericle `Q105` | medio | Solone; Tucidide | 0 | 1 | 3850 |
| 6 | **3-6** | Atene | Platone `Q106` | medio | Aristotele; Socrate | 0 | 1 | 3850 |
| 7 | **3-7** | Ravenna | Belisario `Q107` | forte | Giustiniano; Teodorico | 1199 | 27 | 5049 |
| 8 | **3-8** | Castel del Monte | Federico II `Q108` | forte | Manfredi; Costanza d'Altavilla | 498 | 11 | 5547 |
| 9 | **3-9** | Pella | Alessandro Magno `Q109` | forte | Tolemeo; Pericle | 526 | 12 | 6073 |
| 10 | **3-10** | Ferrara, fonderia | Alfonso I d'Este `Q110` | forte | Tiziano; Ercole II | 998 | 22 | 7071 |
| 11 | **3-11** | Ferrara, corte | Ludovico Ariosto `Q111` | forte | Boiardo; Tasso | 0 | 1 | 7071 |
| 12 | **3-12** | Aquisgrana | Alcuino `Q112` | medio | Carlo Magno; Eginardo | 778 | 17 | 7849 |
| 13 | **3-13** | Milano | Leonardo da Vinci `Q113` | medio | Alberti; Bramante | 634 | 14 | 8483 |
| 14 | **3-14** | Firenze | Niccolò Machiavelli `Q114` | forte | Guicciardini; Cesare | 250 | 6 | 8732 |
| 15 | **3-15** | Ferrara, Camerino d'alabastro | Dosso Dossi `Q115` | forte | Bellini; Tiziano | 122 | 3 | 8854 |
| 16 | **3-16** | Magonza | Johannes Gutenberg `Q116` | forte | Fust; Schöffer | 627 | 14 | 9481 |
| 17 | **3-17** | Ferrara, cappella | Josquin (Q117, *aggiunta*) | forte | Alfonso I; il coro della corte | 626 | 14 | 10107 |
| 18 | **3-18** | Alcalá de Henares | Miguel de Cervantes `Q118` | medio | Shakespeare; Lope de Vega | 1315 | 29 | 11422 |
| 19 | **3-19** | Basilea | Erasmo da Rotterdam `Q119` | forte | Lutero; Calvino | 1177 | 26 | 12599 |
| 20 | **3-20** | Ferrara, Camerino | Giovanni Bellini (Q120, *aggiunta*) | forte | Tiziano; Antonio Lombardo | 652 | 14 | 13251 |
| 21 | **3-21** | Aquisgrana | Carlo Magno `Q121` | forte | Alcuino; Manuzio | 1000 | 22 | 14251 |
| 22 | **3-22** | Certaldo | Giovanni Boccaccio `Q122` | medio | Petrarca; Franco Sacchetti | 886 | 20 | 15137 |
| 23 | **3-23** | Parigi | Tommaso d'Aquino `Q123` | forte | Alberto Magno; Giovanni di San Vincenzo | 891 | 20 | 16028 |
| 24 | **3-24** | Norimberga | Albrecht Dürer (Q124, *aggiunta*) | forte | Leonardo; Raffaello | 638 | 14 | 16666 |
| 25 | **3-25** | Venezia | Aldo Manuzio (Q125, *aggiunta*) | medio | Francesco Griffo; i caratterai | 456 | 10 | 17122 |
| 26 | **3-26** | Westminster | William Caxton (Q126, *aggiunta*) | forte | Caxton; i miniatori | 1137 | 25 | 18259 |
| 27 | **3-27** | Parigi | Olympe de Gouges `Q127` | forte | Wollstonecraft; Robespierre | 343 | 8 | 18602 |
| 28 | **3-28** | Torino | Primo Levi (Q128, *aggiunta*, 02/10/2026) | forte | Alan Turing  forte, era la voce obbligatoria); Ada Lovelace; i matematici di Cambridge | 582 | 13 | 19184 |
| 29 | **3-29** | Roma, Curia | I tipografi e i privilegi (Q129, collettivo `C`) | medio | Manuzio; il Sant'Uffizio | 525 | 12 | 19710 |
| 30 | **3-30** | Mantova | Isabella d'Este `Q130` | forte | Alfonso I; i musei | 388 | 9 | 20098 |

### Anno 4 — il mondo

*barca, 60 km al giorno. Percorso in linea d'aria: **136516 km in 2273 giorni**. Voci obbligatorie distinte: **30**. Facoltative dichiarate in tabella: **63**. Tappe senza punto: nessuna.*

| # | Tappa | Luogo (pin) | Voce obbligatoria | Forza | Facoltative (2) | | km dalla precedente | giorni | km cumulati |
|---|---|---|---|---|---|---|---|---|
| 1 | **4-1** | Uruk | Gilgamesh `Q201` | forte | L'Eneuma Elish; il re assiro |  |  | 0 |
| 2 | **4-2** | Il Cairo e le carovane | Ibn Battuta `Q202` | forte | Ibn Jubayr; i portatori d'acqua | 1384 | 23 | 1384 |
| 3 | **4-3** | Xianyang | Qin Shi Huang `Q203` | forte | Il figlio di Shi Huangdi; gli scribi | 7123 | 119 | 8507 |
| 4 | **4-4** | Tebe | Hatshepsut `Q204` | forte | Nefertari; i sacerdoti di Amun | 7218 | 120 | 15724 |
| 5 | **4-5** | Agra | Akbar `Q205` | medio | Abul Fazl; le città nuove | 4494 | 75 | 20219 |
| 6 | **4-6** | Karakorum | Gengis Khan `Q206` | forte | I quattro khanati; i cronachi cinesi | 3071 | 51 | 23289 |
| 7 | **4-7** | Hannover | Leibniz (Q207, *aggiunta*) | medio | Newton; Hooke | 6204 | 103 | 29494 |
| 8 | **4-8** | Uppsala | Carl Linneo `Q208` | forte | I lini; le critiche alla classificazione | 963 | 16 | 30457 |
| 9 | **4-9** | Il Cairo `A`, con Timbuctù `S` | Mansa Musa `Q209` | forte | I mercanti di Songhai; Ibn Battuta | 3467 | 58 | 33924 |
| 10 | **4-10** | Ferrara, corte | Ercole II d'Este `Q210` | forte | I magazzinieri; Lucrezia Borgia | 2377 | 40 | 36301 |
| 11 | **4-11** | Baghdad | Al-Khwarizmi `Q211` | forte | Tim Berners-Lee  forte dal 02/10/2026); Robert of Chester; il libro dell'algebra | 3076 | 51 | 39377 |
| 12 | **4-12** | Qufu | Confucio `Q212` | forte | Il dizionario di Mengxi; i calligrafi | 6503 | 108 | 45880 |
| 13 | **4-13** | Alessandria | Ipazia `Q213` | medio | I sacerdoti di Soknopaiou Nesos; le tre scritture | 8532 | 142 | 54412 |
| 14 | **4-14** | Tenochtitlán | Moctezuma II `Q214` | medio | Tlacaelel; i calendari | 9808 | 163 | 64220 |
| 15 | **4-15** | Chio e la Ionia | Omero `Q215` | forte | I rapsodi; Pisistrato | 11416 | 190 | 75636 |
| 16 | **4-16** | Pataliputra | Ashoka (Q216, *sostituisce Ibn Khaldun dal 02/10/2026, v. §0.4*) | forte | Ibn Khaldun  forte, era la voce obbligatoria); Cesare; i monaci buddisti | 5654 | 94 | 81289 |
| 17 | **4-17** | Bombay e Delhi | B. R. Ambedkar `Q217` | forte | Il tempio di Kalaram; il poeta | 852 | 14 | 82141 |
| 18 | **4-18** | Costantinopoli | Solimano il Magnifico `Q218` | forte | I millet; Ibrahim, fratello del sultano | 4551 | 76 | 86692 |
| 19 | **4-19** | Il Cairo | Ibn al-Haytham `Q219` | medio | Il Libro degli specchi; il muḥtasib | 1235 | 21 | 87927 |
| 20 | **4-20** | Ferrara e il regno | I censori (Q220, collettivo `C`) | forte | Gli ufficiali del catasto; il censitore cinese | 2375 | 40 | 90302 |
| 21 | **4-21** | Toledo | Isabella di Castiglia `Q221` | forte | I censitori; i funzionari dell'archivio | 1397 | 23 | 91699 |
| 22 | **4-22** | Babilonia | Hammurabi `Q222` | forte | Il codice; la stele di Nippur | 4369 | 73 | 96068 |
| 23 | **4-23** | Lisbona e Calicut | Vasco da Gama `Q223` | forte | I piloti di Malindi; Ahmad ibn Majid | 3981 | 66 | 100050 |
| 24 | **4-24** | Nanchang e il mare | Zheng He `Q224` | forte | Ma Huan; i cantieri | 4584 | 76 | 104634 |
| 25 | **4-25** | Annapolis e Baltimora | Frederick Douglass `Q225` | forte | Sojourner Truth; i censitori | 12347 | 206 | 116981 |
| 26 | **4-26** | Spagna e Tenochtitlán | Hernán Cortés `Q226` | forte | Las Casas; i signori di Tlaxcala | 3087 | 51 | 120068 |
| 27 | **4-27** | Scutari e Costantinopoli | Florence Nightingale `Q227` | forte | Gorgas; i soldati | 11426 | 190 | 131494 |
| 28 | **4-28** | Motihari e Londra | George Orwell `Q228` | forte | Il lavoro alla BBC; la revisione spagnola | 2501 | 42 | 133995 |
| 29 | **4-29** | Parigi e Varsavia | Marie Curie `Q229` | forte | Malala Yousafzai  forte dal 02/10/2026); il libro di Irène; l'Accademia | 1448 | 24 | 135443 |
| 30 | **4-30** | Ferrara, archivio | Le persone che non hanno firmato (Q230, collettivo `C`) | forte | Le voci senza nome; Ercole II | 1072 | 18 | 136516 |

<!-- SEQUENZA:FINE -->

## 3. La differenza con `percorsi.md`, che non è un errore ma è la cosa più importante di questa pagina

`percorsi.md` dichiara il percorso del duca: **3139 km in 95 giorni** nell'anno 2, **18 318 km in 539 giorni** nel 3, **61 482 km in 630 giorni** nel 4. Queste pagine dichiarano numeri quasi il doppio o il doppio e mezzo. Le due cose non si contraddicono, e la ragione è che sono due domande diverse:

| | `percorsi.md` | questa pagina |
|---|---|---|
| che cosa segue | i **pin che avevano coordinate**: 9, 22 e 13 | tutte e **trenta** le tappe |
| che cosa domanda | «un uomo del Quattrocento attraverserebbe davvero questi luoghi?» | «in che ordine il giocatore incontra le trenta persone?» |
| che cosa non sa | le altre 21, 8 e 17 tappe, perché non avevano un punto | niente: i punti mancanti sono arrivati con le ipotesi del 3 ottobre |

Il percorso del duca era una domanda di **fattibilità**: quei pin si possono visitare in un ordine che un uomo di allora farebbe? La sequenza è una domanda di **ordine di lettura**: il giocatore incontra la 4-16 prima della 4-17 e non può farne un giro, perché i numeri di tappa seguono gli argomenti e gli argomenti vanno e vengono. **Sono due ordini diversi e vanno tenuti separati**, che è la regola che `percorsi.md` §3 già scriveva.

La conseguenza più dura sta nell'anno 4: **130 011 km in 2165 giorni**, quasi sei anni. Non è un errore di calcolo: è la risposta. Nell'anno 4 il duca non viaggia (`anno4-mondo.md` §3), il mezzo è quello di chi porta i documenti, e se metti le trenta tappe in fila sulla carta il percorso è una rotta che nessuno ha mai fatto. Per questo l'anno 4 non ha una sequenza di viaggio: ha una sequenza di **arrivi**.

## 4. Una cosa che i numeri non dicono e che va detta

Le **facoltative** sono 59, 61 e 63 secondo l'anno, cioè quasi il doppio delle obbligatorie, e stanno tutte in una colonna che i documenti dichiarano «Facoltativi (2)». Due cose ne seguono, e nessuna delle due è comfortevole:

- **il numero due non torna sempre**: l'anno 2 dichiara 59 facoltative su 30 tappe, cioè una tappa ne ha tre o una delle due caselle è stata tagliata. Il generatore mette quello che c'è e **dichiara** quello che manca (`facoltativi_troncate`), invece di riempirlo;
- **sono il doppio delle persone che il giocatore incontra davvero**: il gioco promette trenta incontri e il catalogo ne ha sessanta che si aprono solo se il giocatore li cerca. È una scelta, ed è dichiarata, ma è il numero più grande che c'è nel progetto dopo i centocinquanta livelli.

### 4.1 Tredici persone sono obbligatorie in una tappa e facoltative in un'altra

Il controllo S3 lo ha trovato e il numero è **tredici**: sono persone che il giocatore incontra **per forza** a una tappa e che ritroverebbe **se le cerca** in un'altra. Non è un errore, ed è probabilmente una buona scelta — una persona che torna è un ritorno, e il progetto ha già la regola dei ritorni forti (`anno3-europa.md` §13, I16). Ma è un numero che nessuno sapeva e che cambia il conto delle facoltative: **non sono 183 facoltative, sono 170 e tredici di quelle sono già nel percorso**.

| anno | quante | chi |
|---|---|---|
| 2 | **8** | Amerigo Vespucci (fac. alla 2-28), Catone il Censore (2-7, 2-12), Cicerone (2-18), Cincinnato (2-5), Parmenide (2-11), Pitagora (2-16), Tiberio Gracco (2-10, 2-13), Zenone di Elea (2-6) |
| 3 | **4** | Alcuino (3-21), Carlo Magno (3-12), Pericle (3-4, 3-9), Solone (3-5) |
| 4 | **1** | Ibn Battuta (4-9) |

**Ibn Battuta è il caso più interessante**, e la ragione è che lui è diventato una facoltativa per una decisione esplicita: è la «facoltativa forte» della 4-9, che è la tappa del manoscritto, e la sua voce si incrocia con la 4-2, dove il Cairo e le carovane sono la sua rotta. Non è un doppione: sono due tappe diverse che parlano dello stesso uomo da due lati.

**Il numero due della colonna facoltative non torna, e va detto con le sue parole**: l'anno 2 dichiara 59 facoltative su trenta tappe. O una tappa ne ha tre, o una delle due caselle è stata tagliata quando la tabella si è accorciata. Il generatore mette quello che c'è e **dichiara** quello che manca (`facoltativi_troncate`), invece di riempirlo con un nome inventato.


## 5. Come si rigenera

```bash
python3 sorgenti/sequenza_tappe.py            # il JSON e le tre tabelle qui sotto
python3 sorgenti/sequenza_tappe.py --anno 3   # un anno solo, in chiaro, senza scrivere
python3 sorgenti/verifica_sequenza.py         # i sei controlli
```

Le tabelle stanno fra i due marcatori `<!-- SEQUENZA:INIZIO -->` e `<!-- SEQUENZA:FINE -->`: il generatore sostituisce quello che c'è fra, e tutto il resto del documento lo tocca solo se lo cambi a mano.

## 6. Cosa c'è da fare

1. **Il numero due della colonna facoltative**, che nell'anno 2 non torna: o la tabella si completa, o il titolo della colonna smette di dire «(2)».
2. ~~**Il generatore del registro**~~ **chiusa il 03/10/2026**: esiste, ed è stato eseguito davvero. Il confronto che mancava è quello che §1 racconta, e l'ha vinto. La catena ha quattro controlli suoi in `sorgenti/verifica_catena_luoghi.py`.
3. **Le trenta voci in sequenza**: questa pagina mette i nomi in fila, ma non mette in fila gli **argomenti** che ogni voce porta con sé. È il capitolo che manca, ed è il capitolo che rende la sequenza un percorso e non un elenco.

## 7. Registro delle modifiche

- **v0.2 (03/10/2026)**: **la divergenza dichiarata è chiusa, e chiusa come si deve: rigenerando.** Il registro dei luoghi è stato rifatto dalla catena `estrai_luoghi.py` → `coordinate.py` → `classifica.py`, e lungo la strada sono usciti quattro difetti veri. Il primo: **`estrai_luoghi.py` leggeva le colonne per numero**, e nell'anno 5 la colonna della stanza sta fra il pin e la voce — in ventinove tappe su trenta il campo `voce` aveva il filone del *Furioso* invece della persona. Ora la tabella si legge per **intestazione**. Il secondo: **le correzioni di Baghdad e Karakorum vivevano solo in un JSON editato a mano** e sparivano alla prima rigenerazione; ora stanno in `dati/luoghi_correzioni.json` e vengono riapplicate ogni volta. Il terzo: **`classifica.py` aveva due copie della regola che assegna lo stato della coordinata**, e le due copie erano già divergenti sulle sette ferraresi; ora c'è una definizione sola. Il quarto, che è la conseguenza: **`ambienti_livelli.json` era rimasto indietro** e la 4-16 aveva ancora il punto dall'ipotesi benché il registro avesse la coordinata. La correzione della 4-16 è così passata da **dato scritto a mano** a **dato che la catena produce**, che è la differenza fra una correzione e una riparazione. Le divergenze fra registro e documento sono **zero**, e `DICHIARATE` in `sequenza_tappe.py` resta vuota e dichiarata. Il percorso dell'anno 3 è passato da 18990 a 20098 km perché la 3-28 è diventata Torino.
- **v0.1 (03/10/2026)**: prima stesione. Novanta tappe in sequenza, le trenta voci obbligatorie di ciascun anno in fila con i luoghi e le distanze, le facoltative tenute fuori e dichiarate. Il ritorno vero del lavoro è **un difetto di dati**: la 4-16 aveva nel registro il luogo di Ibn Khaldun dopo che il documento l'aveva cambiato in quello di Ashoka, e le ipotesi del giorno prima avevano costruito sopra quel posto sbagliato una strada interamente inventata che i sei controlli avevano approvato. La lezione è scritta in §1 e vale per tutto il progetto: **un controllo di forma non verifica una premessa**.