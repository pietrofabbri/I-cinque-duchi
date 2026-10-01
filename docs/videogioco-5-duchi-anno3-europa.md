---
titolo: Videogioco "I cinque duchi" — Anno III, i personaggi d'Europa: la corte di Ferrara e la carta a strati
versione: 0.2
data: 2026-10-01
autore: Pietro Fabbri (con Claude)
fonte del materiale: due documenti di progettazione storico-pedagogica di Pietro ("ANNO III — I PERSONAGGI D'EUROPA" e "ANNO III — L'EUROPA ATTRAVERSO I SECOLI"), 01/10/2026
dati: videogioco-5-duchi-anno3-europa.json e videogioco-5-duchi-anno3-personaggi.json (da generare, v0.1)
documenti collegati: videogioco-5-duchi-schema-livelli.md (v1.1, livelli 3-1…3-30), videogioco-5-duchi-curricolo.md (v0.1, §4 cornice narrativa e §5.3 elenco dei livelli dell'anno 3), videogioco-5-duchi-anno2-penisola.md (v0.1, da cui questo documento continua le convenzioni), videogioco-5-duchi-anno1-ferrara.md (v0.3), videogioco-5-duchi-anno1-mappa.md (v0.8), videogioco-5-duchi-esercizi.md (v0.1), videogioco-5-duchi-quadro-trasversale.md (v0.1), videogioco-5-duchi-gioco.md (v0.4), videogioco-5-duchi-meccaniche.md (v0.3)
---
# Anno III — I personaggi d'Europa

## 0. Che cosa contiene questo documento

Il documento **formalizza** il materiale storico-pedagogico di Pietro per il terzo anno e lo aggancia ai 30 livelli già definiti in `videogioco-5-duchi-schema-livelli.md` (v1.1, § «Anno 3 — Alfonso I»).

Come per l'Anno II:

- il **materiale** di Pietro è conservato e riordinato secondo le convenzioni del progetto;
- le **aggiunte** sono ciò che è stato introdotto per rendere il materiale giocabile, e sono segnalate voce per voce;
- le **proposte** sono da approvare e raccolte in §13;
- i **fatti storici non certi** sono indicati con `note_verifica` e raccolti in §12.

### 0.1 Le tre decisioni di Pietro (01/10/2026)

1. **La mappa è la carta d'Europa a strati.** Conferma «Carta d'Europa a strati».
2. **Le 30 tappe coprono l'intera Europa, da Omero a von der Leyen, e Alfonso I è la guida, non il protagonista giocante.** Conferma «L'intera Europa, con Alfonso come guida».
3. **Il decreto di espulsione del 1510 entra nel gioco, con la fonte.** Conferma «Sì, con il decreto e la fonte».

### 0.2 Due conseguenze delle decisioni, da mettere in conto subito

**(a) La seconda decisione cambia una regola di `AGENTS.md`.** La regola vigente è: «**Borso d'Este è il personaggio giocante**», e per l'Anno II «**Ercole è il protagonista giocante, come Borso**». Con Alfonso in veste di *guida*, il terzo anno **non** ha un personaggio giocante. È una decisione coerente con il materiale di Pietro e va rispettata, ma va resa esplicita nelle convenzioni: `AGENTS.md` §3 «Anno 1» va corretto, perché da quest'anno in poi vale «il duca è la guida; chi gioca attraversa» (v. §7).

**(b) La seconda decisione ha un costo, ed è il problema più serio di questo documento.** I livelli dell'anno 3 riguardano la **rappresentazione e la sua trasmissione**: formati, compressione, audio, font, markup, XML, HTML, CSS, JavaScript, pubblicazione. Di conseguenza gli agganci più forti stanno **dove la scrittura e l'immagine si moltiplicano**, cioè fra il XV e il XVI secolo: è lì che il percorso si addensa. Nei 30 livelli, **14 tappe stanno fra il 1400 e il 1560**, **2 sole tappe coprono il 1789–1945** (3-27, 3-28) e **nessuna copre il 1945 a oggi**. Il salto di secoli che il materiale di Pietro chiama «l'Europa divisa» e «l'Europa contemporanea» resta quindi, per ora, **fuori dal percorso giocabile**. La questione è la prima di §13 e va decisa prima di costruire le schede.

---

## 1. Il principio zero, esteso: neanche l'Europa esiste ancora

L'Anno II ha insegnato che l'Italia non esiste come Stato per gran parte del percorso. Il terzo anno estende la lezione, e la estende in una direzione che il materiale di Pietro indica con chiarezza: **anche l'Europa non esiste ancora.**

Nel 1505, quando Alfonso I succede a Ercole I, la parola «Europa» non indica nessuno spazio politico. Non c'è l'Unione Europea, non ci sono le frontiere nazionali moderne, e la stessa idea di «nazione» ha un significato quasi irriconoscibile rispetto a oggi. Esistono regni, principati, repubbliche, città-stato, territori ecclesiastici, imperi e una autorità papale che è sovrana in un senso che nessuno Stato di oggi lo è.

La conseguenza pedagogica è identica a quella dell'Anno II, ma più forte: **nessun personaggio di questo documento è «europeo»**, e non è «non europeo» per esserlo nato fuori. Un veneziano del Cinquecento non si considera membro di una futura nazione europea; un polacco del Settecento può non attraversare mai un confine che oggi è interno all'Unione; un intellettuale di Salamanca non lavora «per l'Europa».

Da qui la forma del gioco: **non si racconta la storia d'Europa, si mostra come l'Europa sia diventata ciò che è attraverso persone che appartenevano a mondi diversi e spesso in conflitto fra loro.** I personaggi sono porte d'ingresso, non il contenuto (§6).

Una conseguenza ulteriore, che vale per tutti e tre gli anni fin qui: **la parola «Europa» è essa stessa una costruzione culturale**, e il gioco non deve fingere di trovarla già pronta. È la versione più recente del principio dell'Anno II, e va detto ai ragazzi in modo esplicito.

---

## 2. I principi del terzo anno

1. **Il protagonista è la penisola, la guida è il duca, il mondo è l'Europa.** Nell'Anno I il protagonista narrativo era la città; nell'Anno II la penisola; nel terzo è il **continente**. Alfonso I non governa l'Europa: ne sta al centro, e non la vede.
2. **La corte di Ferrara è il centro del gioco, non il suo perimetro.** Tutto ciò che il giocatore incontra **arriva a Ferrara**: una lettera, un ambasciatore, un libro, un dipinto, un pezzo di artiglieria, una notizia. La corte è l'unico luogo in cui il giocatore si muove fisicamente; tutto il resto è ciò che arriva sul tavolo (§3.3).
3. **La stratificazione è il cuore del racconto**, come negli anni precedenti, ma qui la colonna ha tremila anni e il continente ha più strati di quanti ne abbia la penisola (§3.2).
4. **Non è una cronologia.** L'ordine dei 30 livelli è l'ordine degli **argomenti**. Il percorso risale e ridiscende: si parte dall'antichità greca, si arriva alla Francia del Cinquecento, si torna a Ferrara e da lì si esce verso l'Europa di Napoleone e oltre. Chi gioca incontra Atene prima di Ferrara e Ferrara prima di Versailles. È un disordine produttivo, se il gioco lo dichiara.
5. **Ogni persona è di un luogo, e ogni luogo ha strati.** Vale la regola degli anni precedenti (§3.1).
6. **La competenza finale** non è «sapere la storia d'Europa» ma chiedersi ***come facciamo a sapere che cosa è successo, e chi ha avuto interesse a raccontarlo in quel modo?***

---

## 3. La mappa: la carta d'Europa a strati

*(aggiunta, 01/10/2026 — realizza la decisione 1 del §0.1)*

### 3.1 Due assi, come nell'Anno II

- **asse orizzontale, il luogo**: l'Europa in vista dall'alto, con la geometria reale delle coste, dei fiumi e dei confini (open data, con attribuzione, come `AGENTS.md` §5);
- **asse verticale, lo strato**: accanto alla pianta, una **colonna stratigrafica** con 13 strati, dal più antico al più recente. Lo strato in cui ci si trova decide **chi parla** in quel luogo.

Lo strato dice l'epoca; il pin dice il posto. Sono due informazioni diverse, ed è la stessa architettura dell'Anno II, portata alla scala del continente.

### 3.2 Gli strati

| Strato | Denominazione | Periodo indicativo | Tappe obbligatorie |
|---|---|---|---|
| `S30` | Prima dell'Europa | età del Rame – VIII sec. a.C. | — |
| `S31` | Grecia arcaica e classica | VIII – IV sec. a.C. | 3-4, 3-5, 3-6 |
| `S32` | Ellenismo | IV – I sec. a.C. | 3-1, 3-9 |
| `S33` | Roma imperiale | I sec. a.C. – III sec. | 3-3 |
| `S34` | Tardoantico e regni su Roma | III – VIII sec. | 3-7 |
| `S35` | Carolingio | VIII – XI sec. | 3-12, 3-21 |
| `S36` | Medioevo imperiale e feudale | XI – XIII sec. | 3-8 |
| `S37` | Comuni, ordini, università | XIII – XIV sec. | 3-22, 3-23 |
| `S38` | Umanesimo, stampa, prima scienza | XIV – XVI sec. | 3-2, 3-13, 3-14, 3-16, 3-24, 3-25, 3-29 |
| `S39` | Le corti e le Riforme | 1500 – 1560 | 3-10, 3-11, 3-15, 3-17, 3-20, 3-26, 3-30 |
| `S40` | Riforma e assolutismi | 1520 – 1700 | 3-19 |
| `S41` | Barocco e nuovi mondi | 1600 – 1700 | 3-18 |
| `S42` | Rivoluzione | 1789 – 1815 | 3-27 |
| `S43` | Ottocento e Novecento | 1815 – 1945 | 3-28 |
| `S44` | Guerra fredda ed Europa unita | 1945 – oggi | — |

*(aggiunta)* Gli strati `S30` e `S44` **non hanno tappe obbligatorie**. `S30` è rappresentato da una visione facoltativa (Ötzi, che è già la tappa 2-1 dell'Anno II: v. §6.4). `S44` è il vuoto di cui parla il §0.2 e che è la prima questione aperta (§13, Q1).

**Vincoli sugli strati.** Come nell'Anno II, **nessun vincolo di monotonia**: il percorso scende e risale continuamente la colonna (3-1 è in `S32`, 3-4 in `S31`, 3-10 in `S39`, 3-27 in `S42`, 3-30 in `S39`). Le regole che valgono sono: ogni tappa dichiara il proprio strato; un luogo può comparire più volte purché cambi la voce; la nebbia dipende dal **pin visitato**, non dallo strato.

### 3.3 La corte: perché questo risolve il problema della mappa

*(aggiunta, e punto centrale dell'anno)*

Una mappa d'Europa con tremila anni non è percorribile: da Ferrara a Salamanca ci sono due mila chilometri. La soluzione non è una mappa percorribile, è una **corte**.

Il giocatore **non viaggia**. Si muove dentro il Palazzo di Alfonso I e dentro il suo castello, che sono i luoghi già costruiti per l'Anno I. Ogni tappa è **una risorsa che arriva sulla tavola della corte**, e il gioco ne annuncia l'arrivo:

| Come arriva | Che cosa è | Tappe tipiche |
|---|---|---|
| **ambasciatore** | una persona che entra e parla | 3-4, 3-5, 3-6, 3-10, 3-19, 3-27 |
| **volume** | un libro che viene aperto sulla tavola | 3-22, 3-23, 3-24 |
| **opera** | un dipinto, un disegno, un rilievo | 3-2, 3-13, 3-15, 3-20 |
| **orefice e artigiano** | un oggetto d'artiglieria, uno strumento | 3-9, 3-21 |
| **musica** | un polycoral, una messa | 3-17 |
| **carta geografica** | una mappa, un portolano | 3-3, 3-16 |
| **mestiere** | un artigiano del luogo, che lavora davanti al giocatore | 3-25, 3-29 |

Il giocatore vede la risorsa arrivare, la esamina, lavora su di essa nella bottega del livello, e poi la risorsa **va via** e resta solo la scheda. Ogni tanto una risorsa resta appesa in permanenza: le opere del Camerino d'alabastro (3-15, 3-20) sono nella stanza del duca per tutta la vita, e si vedono deteriorare.

Questa meccanica fa tre cose insieme:

1. **risolve la scala** — non serve una mappa percorribile, serve una mappa su cui arrivano cose;
2. **è storicamente esatta** — così funzionava, ed è il modo in cui una corte del Cinquecento era davvero informata: non viaggiando, ma **ricevendo**;
3. **è il livello 2-28 riscritto in forma drammatica** — la rete di trasporto (`J7.1` DNS, `J3.1` strati) era già stata anticipata nell'Anno II. Qui diventa la regola del gioco, e il giocatore la usa da subito senza accorgersene.

### 3.4 Le porte

Come nell'Anno II, i personaggi che agiscono **fuori dalla penisola** e fuori dall'Europa non possono stare sulla pianta. Valgono le stesse **porte**: la risorsa che arriva a Ferrara da un luogo non rappresentabile è annunciata da un punto della corte.

| Porta | Luogo in cui la notizia o la risorsa entra | Chi entra da lì |
|---|---|---|
| `PT-ATN` | Il salone delle ambascerie | Alessandro Magno (3-9), Belisario (3-7) |
| `PT-AXD` | La zona dei fonditori | Alboino (3-9) |
| `PT-SYN` | La cancelleria, dove si scrive | Alcuino (3-12), Dürer (3-24), Turing (3-28) |
| `PT-PAR` | Il gabinetto delle opere | Isabella d'Este (3-30), Cervantes (3-18) |
| `PT-STR` | Il magazzino dei libri | Manuzio (3-25), Caxton (3-26), i tipografi (3-29) |

*(proposta)* Le porte non sono un vezzo: sono la prova visiva che **l'informazione in questo mondo viaggia con le persone e arriva mediata**. Ogni volta che una porta si apre, il gioco mostra chi ha tradotto, chi ha tagliato, chi ha ritardato.

### 3.5 Alfonso non viaggia, e non sa

Alfonso I **non esce mai dal palazzo** nel corso dell'anno. Questo è il cuore del terzo anno, ed è la risposta alla domanda con cui si chiude il materiale di Pietro: *come può un continente diventare ciò che è attraverso decisioni prese da persone che non conoscevano il futuro?*

Il meccanico è semplice e ripetuto 30 volte. All'inizio di ogni tappa, **Alfonso commenta la risorsa che sta arrivando**, e lo fa **solo con ciò che sa**:

- se la risorsa viene da un'epoca che Alfonso conosce (dagli ambasciatori, dalla cronaca, dai domenicani che portano notizie), Alfonso parla, e dice il suo parere — che è spesso di parte, e spesso sbagliato;
- se la risorsa viene da un'epoca che Alfonso **non può conoscere** (Atene nel V secolo, Ferrara nel 1340, Mosca nel 1945), il gioco **lo dice**: «Questo non è arrivato. Non arriverà. Non lo vedrai.» E la tappa si gioca lo stesso.

Ne segue la regola che rende il gioco onesto sul lungo periodo: **il giocatore sa tutto, Alfonso non sa quasi niente, e le due colonne non si incontrano mai.** È la stessa differenza temporale che chiudeva l'Anno II, ma qui è la regola portante invece di un accorgimento, perché il protagonista non è l'unico a essere limitato nel tempo: lo è **tutto il castello**.

### 3.6 La fine dell'anno

Alla tappa 3-30 la corte si riunisce e Alfonso parla da solo, per la prima volta in tutto l'anno, di ciò che non ha capito. La **carta intera** si apre: il continente intero, con tutti i suoi strati sovrapposti, e i pin che il giocatore ha visitato.

La domanda che il gioco pone a schermo intero, e che è la conclusione del terzo anno, è quella del materiale di Pietro riformulata come domanda sul gioco:

> **questa carta mostra che gli strati esistono davvero, o mostra che noi li ordiniamo così?**

---

## 4. Le 30 tappe

*(aggiunta — costruita sui 30 livelli dello schema, non il contrario)*

**Colonna «Forza».** Come negli anni precedenti: **forte** il legame è naturale; **medio** funziona ma va costruito nel racconto; **di scena** il luogo fa solo da ambientazione.

**Colonna «Voce».** `personaggio` = nome proprio. `collettivo` = voce senza nome proprio, con attendibilità `C` (cfr. Anno II §4). In questo anno sono **1 su 30**: quasi tutte le tappe hanno un nome, perché il livelli sono tutti tecnici ma il materiale di Pietro fornisce una voce adatta a ciascuno.

| Livello | Argomento | Strato | Luogo (pin) | Voce | Domanda che apre la tappa | Forza | Rimando (abbozzo) | Facoltativi (2) |
|---|---|---|---|---|---|---|---|---|
| **3-1** | Interi con segno e complemento a 2 | `S32` | Alessandria | **Eratostene** (Q101) | Come si scrive un numero minore di zero, quando il segno non esiste? | forte | «Un altro greco arriva da Taranto, con un metodo per misurare tutto.» | Archimede; i matematici di Alessandria |
| **3-2** | Virgola mobile (IEEE 754) ed errori | `S38` | Frombork | **Copernico** (Q102) | Il numero che calcoli e il numero che scrivi sono lo stesso numero? | forte | «Un modello nuovo del cielo, e sotto i piedi un pavimento di cifre sbagliate.» | Keplero; Tycho Brahe |
| **3-3** | Array e matrici | `S33` | Roma | **Augusto** (Q103) | Come si mette un impero in ordine, riga per riga? | medio | «A nord, sulla stessa riga, un altro impero con un'altra tabella.» | Traiano; Adriano |
| **3-4** | Ordinamento: selection sort e bubble sort | `S31` | Atene | **Solone** (Q104) | Dividere un popolo in classi: in base a che cosa, e chi lo decide? | forte | «Resta la stessa città, e un altro criterio per contare chi c'è.» | Pericle; Socrate |
| **3-5** | Ordinamento: insertion sort | `S31` | Atene | **Pericle** (Q105) | Una lista che cresce di uno in uno: chi entra, e con quale criterio? | medio | «Il criterio è l'argomento. Andiamo all'Accademia, a cercare la verità.» | Solone; Tucidide |
| **3-6** | Ricerca binaria; logaritmi ★ | `S31` | Atene | **Platone** (Q106) | Si può dimezzare lo spazio di una ricerca, e trovare sempre la risposta? | medio | «Da sei mesi un esercito attraversa il Mediterraneo. Torniamo al nostro, che è più complicato.» | Aristotele; Socrate |
| **3-7** | Contare i passi: complessità | `S34` | Ravenna | **Belisario** (Q107) | Una guerra che si vince in quattro anni: quanto costa, davvero? | forte | «Sono passati secoli, e la penisola è divisa in tre. Chi si prende la parte più difficile?» | Giustiniano; Teodorico |
| **3-8** | Ricorsione | `S36` | Castel del Monte | **Federico II** (Q108) | Una forma che contiene sé stessa, otto volte: è la stessa forma o sono otto? | forte | «A nord-ovest, un imperatore pretende di governare città che non ha mai visto.» | Manfredi; Costanza d'Altavilla |
| **3-9** | Divide et impera: merge sort ★ | `S32` | Pella | **Alessandro Magno** (Q109) | Un impero diviso fra molti: i pezzi tornano a formare qualcosa? | forte | «Roma ha raccolto i pezzi. Ma la raccolta è durata tre secoli.» | Tolemeo; Pericle |
| **3-10** | Prova di corte: ordinare e contare i passi | `S39` | Ferrara, fonderia | **Alfonso I d'Este** (Q110) | I cannoni escono dalla fonderia: in che ordine li schieriamo, e con quale criterio? | forte | «Dalla fonderia si passa allo studio. Un poeta ha finito un libro di ventottomila versi.» | Tiziano; Ercole II |
| **3-11** | Stringhe avanzate e ricerca di schemi; automi ★ | `S39` | Ferrara, corte | **Ludovico Ariosto** (Q111) | Nel poema due fili si intrecciano secondo una regola: chi scrive conosce la regola? | forte | «Il libro è stampato e viaggia. A Nordmonti, in Inghilterra, qualcuno lo sta traducendo.» | Boiardo; Tasso |
| **3-12** | File e CSV | `S35` | Aquisgrana | **Alcuino** (Q112) | Una scuola che registra: che cosa si scrive, e in quale ordine? | medio | «Il registro dei beni di un impero è una tabella. Torniamo alla tabella, in un altro modo.» | Carlo Magno; Eginardo |
| **3-13** | Metodologie: top-down e modularità | `S38` | Milano | **Leonardo da Vinci** (Q113) | Un problema enorme si scompone in pezzi che si possono tenere in mano? | medio | «A Firenze, un uomo corregge lo stesso testo per anni. La correzione è la parte vera.» | Alberti; Bramante |
| **3-14** | Documentazione, stile, controllo di versione (Git) ★ | `S38` | Firenze | **Niccolò Machiavelli** (Q114) | Lo stesso libro, riveduto per anni, con un destinatario cambiato: quale versione è vera? | forte | «Il libro di cui parlavamo è stampato. Adesso la domanda è un'altra: di chi è.» | Guicciardini; Cesare |
| **3-15** | Formati di immagine: bitmap e vettoriale | `S39` | Ferrara, Camerino d'alabastro | **Dosso Dossi** (Q115) | Una parete con dentro un bassorilievo e un dipinto: sono due cose diverse? | forte | «Le opere della stanza sono state smontate e portate via nel 1598. Torneremo.» | Bellini; Tiziano |
| **3-16** | Compressione senza perdita | `S38` | Magonza | **Johannes Gutenberg** (Q116) | Come si moltiplica un testo centomila volte senza scriverlo centomila volte? | forte | «Questo uomo ha cambiato il costo di un libro. Torniamo alla sua città, che è cambiata con lui.» | Fust; Schöffer |
| **3-17** | Audio digitale: campionamento e quantizzazione | `S39` | Ferrara, cappella | **Josquin** (Q117, *aggiunta*) | Una messa costruita con le sole vocali di un nome: un suono è una cosa che si può calcolare? | forte | «A Padova, un anatomista guarda il corpo e trova che il libro ha torto.» | Alfonso I; il coro della corte |
| **3-18** | Compressione con perdita | `S41` | Alcalá de Henares | **Miguel de Cervantes** (Q118) | Un libro che descrive un mondo che non esiste: che cosa si perde, e che cosa si guadagna? | medio | «A Basilea, un altro fa un'edizione e mette le note accanto al testo.» | Shakespeare; Lope de Vega |
| **3-19** | Linguaggi di markup: il concetto, Markdown | `S40` | Basilea | **Erasmo da Rotterdam** (Q119) | Un libro in cui il testo porta dentro di sé la propria struttura e le proprie domande? | forte | «Wittenberg: un professore scrive novantacinque tesi e le affige alla porta. Sono diventate un libro.» | Lutero; Calvino |
| **3-20** | Prova di corte: il Camerino restaurato | `S39` | Ferrara, Camerino | **Giovanni Bellini** (Q120, *aggiunta*) | Un'opera spezzata in venti parti e portate in quattro città: si può ricomporre? | forte | «A Londra, un uomo prega un re di sciogliere un matrimonio. Non è un caso di coppie.» | Tiziano; Antonio Lombardo |
| **3-21** | Font e tipografia digitale | `S35` | Aquisgrana | **Carlo Magno** (Q121) | Le lettere hanno forme diverse in epoche diverse: quale giusto scrivere? | forte | «Torniamo alla stampa, che è il modo in cui quelle lettere si sono diffuse.» | Alcuino; Manuzio |
| **3-22** | XML: elementi, attributi, buona formazione | `S37` | Certaldo | **Giovanni Boccaccio** (Q122) | Cento storie ordinate in dieci giornate: che cosa tiene insieme una struttura così? | medio | «A Parigi, un frate scrive un testo che si cita per numero di articolo. È un'altra maniera di ordinare.» | Petrarca; Franco Sacchetti |
| **3-23** | HTML: struttura e semantica | `S37` | Parigi | **Tommaso d'Aquino** (Q123) | Un testo che si cita con una sigla e rimanda a un altro punto di sé stesso: si può navigare? | forte | «Un uomo di Norimberga disegna il corpo umano con i numeri invece che con le parole.» | Alberto Magno; Giovanni di San Vincenzo |
| **3-24** | SVG: la grafica vettoriale come testo | `S38` | Norimberga | **Albrecht Dürer** (Q124, *aggiunta*) | Un corpo umano si può scrivere come una serie di costruzioni geometriche? | forte | «A Venezia, un tipografo cerca un carattere che non si stanchi. È un mestiere intero.» | Leonardo (ritorno); Raffaello |
| **3-25** | CSS: selettori, box model, colori | `S38` | Venezia | **Aldo Manuzio** (Q125, *aggiunta*) | Il testo è uno, e la sua cura ne fa cento: si può cambiare l'aspetto senza cambiare le parole? | medio | «A Westminster, un altro stampatore porta la stampa in un'altra lingua.» | Francesco Griffo; i caratterai |
| **3-26** | Impaginazione e design responsive | `S39` | Westminster | **William Caxton** (Q126, *aggiunta*) | Un libro deve stare in tasca o sul pulpito: cambiano le dimensioni, non il testo? | forte | «Il Giappone. E l'America. Due risposte diverse alla stessa domanda.» | Caxton; i miniatori |
| **3-27** | Progettazione web: usabilità e accessibilità | `S42` | Parigi | **Olympe de Gouges** (Q127) | Se una società dichiara diritti universali, chi resta fuori dalla porta? | forte | «A Manchester, nel 1824, un altro scrutinio di chi conta e chi non conta.» | Wollstonecraft; Robespierre |
| **3-28** | JavaScript di base: la pagina che reagisce | `S43` | Manchester | **Alan Turing** (Q128, *aggiunta*) | Una macchina che capisce le istruzioni: come si sa che ha capito bene? | forte | «Torniamo alla corte. Tutto quello che è arrivato oggi va in un archivio.» | Ada Lovelace; i matematici di Cambridge |
| **3-29** | Pubblicare un sito; licenze e diritto d'autore | `S38` | Roma, Curia | **I tipografi e i privilegi** (Q129, collettivo `C`) | Chi può stampare, chi può leggere, e di chi è il testo? | medio | «Mantova, a pochi chilometri. Una sorella del duca ha messo ordine in un mucchio di cose.» | Manuzio; il Sant'Uffizio |
| **3-30** | Prova finale: il sito della corte | `S39` | Mantova | **Isabella d'Este** (Q130) | Un inventario di opere: le metti in ordine, e l'ordine cambia che cosa vedrai? | forte | fine anno: si apre la carta intera | Alfonso I; i musei |

**Verifica degli agganci.** Dei 30 agganci: **21 forti**, **9 medi**, **0 di scena**. Gli agganci forti sono: 3-1, 3-2, 3-4, 3-7, 3-8, 3-9, 3-10, 3-11, 3-14, 3-15, 3-16, 3-17, 3-19, 3-20, 3-21, 3-23, 3-24, 3-26, 3-27, 3-28, 3-30. Sono medi: 3-3, 3-5, 3-6, 3-12, 3-13, 3-18, 3-22, 3-25, 3-29.

*(proposta)* Questo bilancio è **migliore** di quello dell'Anno II (13 forti su 30), e la ragione è precisa: il tema dell'anno 3 è la **rappresentazione e la sua trasmissione**, e il periodo in cui la scrittura e l'immagine si moltiplicano è anche il periodo in cui la scuola ha i suoi protagonisti. Il percorso è stato costruito da qui, non per forzatura. Vedi §13, Q3.

### 4.1 Le trenta domande in forma piena

Le domande della tabella sono il cuore didattico dell'anno. In forma estesa, con i tre livelli di fonte (§6.2):

1. **Eratostene** — *Come si scrive un numero che non esiste, quando non esiste il segno?* (fonte: l'*Octad*; ricostruzione: la scuola di Alessandria; memoria: il teorema dell'ombra, che ha cancellato il resto)
2. **Copernico** — *Il numero che calcoli e il numero che scrivi sono lo stesso numero?* (fonte: il *De revolutionibus*; ricostruzione: le osservazioni; memoria: il sistema del mondo, che non accettò nessuno per cent'anni)
3. **Augusto** — *Come si mette un impero in ordine, riga per riga?* (fonte: le *Res Gestae*; ricostruzione: la riforma; memoria: la pace, che è una formula)
4. **Solone** — *Dividere un popolo in classi: in base a che cosa, e chi lo decide?* (fonte: la tradizione; ricostruzione: le quattro classi; memoria: il padre della democrazia ateniese)
5. **Pericle** — *Una lista che cresce di uno in uno: chi entra, e con quale criterio?* (fonte: Tucidide; ricostruzione: l'età d'oro; memoria: l'Atene, che escludeva quasi tutti)
6. **Platone** — *Si può dimezzare lo spazio di una ricerca e trovare sempre la risposta?* (fonte: i dialoghi; ricostruzione: l'Accademia; memoria: la linea divisa nella grotta)
7. **Belisario** — *Una guerra vinta in quattro anni: quanto è costata davvero?* (fonte: Procopio, che era al suo servizio; ricostruzione: la guerra gotica; memoria: il generale fedele, non il devastatore)
8. **Federico II** — *Una forma che contiene sé stessa, otto volte: è la stessa forma o sono otto?* (fonte: i trattati; ricostruzione: la corte; memoria: il meraviglioso, che non dice niente del costo)
9. **Alessandro Magno** — *Un impero diviso fra molti: i pezzi tornano a formare qualcosa?* (fonte: gli Arriani e i Diodori; ricostruzione: le successioni; memoria: il conquistatore, che ha perso l'impero in quarant'anni)
10. **Alfonso I d'Este** — *I cannoni escono dalla fonderia: in che ordine li schieriamo?* (fonte: l'archivio; ricostruzione: la guerra; memoria: il duca artigliere, che non ha perso niente)
11. **Ludovico Ariosto** — *Due fili che si intrecciano secondo una regola: chi scrive conosce la regola?* (fonte: il *Furioso*; ricostruzione: la corte; memoria: il poema, molto più del suo autore)
12. **Alcuino** — *Una scuola che registra: che cosa si scrive, e in quale ordine?* (fonte: le lettere; ricostruzione: la rinascita carolingia; memoria: il palagio di Carlomagno, che non è mai esistito)
13. **Leonardo** — *Un problema enorme si scompone in pezzi che si possono tenere in mano?* (fonte: i quaderni; ricostruzione: il lavoro; memoria: l'inventore geniale, che ha perso il metodo)
14. **Machiavelli** — *Lo stesso libro riveduto per anni, con un destinatario cambiato: quale versione è vera?* (fonte: gli autografi; ricostruzione: la ragione; memoria: il Cinquecento, che ha letto solo la seconda)
15. **Dosso Dossi** — *Una parete con dentro un bassorilievo e un dipinto: sono due cose diverse?* (fonte: le opere; ricostruzione: il Camerino; memoria: la sala, che non si vede più)
16. **Gutenberg** — *Come si moltiplica un testo centomila volte senza scriverlo centomila volte?* (fonte: i torchi; ricostruzione: l'officina; memoria: l'inventore singolo, che era un'impresa collettiva)
17. **Josquin** — *Una messa costruita con le sole vocali di un nome: un suono si può calcolare?* (fonte: le partiture; ricostruzione: la cappella; memoria: la musica, che è diventata «musica» e ha perso la parola)
18. **Cervantes** — *Un libro che descrive un mondo che non esiste: che cosa si perde?* (fonte: il testo; ricostruzione: la vita; memoria: il cavaliere, che non esiste più)
19. **Erasmo** — *Un libro in cui il testo porta dentro di sé la propria struttura e le proprie domande?* (fonte: l'edizione; ricostruzione: la rete di amici; memoria: l'umanista, che non ha fatto la Riforma ma l'ha resa possibile)
20. **Bellini** — *Un'opera spezzata in venti parti e portate in quattro città: si può ricomporre?* (fonte: le opere; ricostruzione: il Camerino; memoria: l'artista che non ha dipinto la sala)
21. **Carlo Magno** — *Le lettere hanno forme diverse in epoche diverse: quale giusto scrivere?* (fonte: il *De litteris*; ricostruzione: la riforma; memoria: l'imperatore, che non ha scritto il trattato)
22. **Boccaccio** — *Cento storie ordinate in dieci giornate: che cosa tiene insieme una struttura così?* (fonte: il *Decameron*; ricostruzione: la peste; memoria: le novelle, che sono un genere)
23. **Tommaso d'Aquino** — *Un testo che si cita con una sigla e rimanda a un altro punto di sé stesso?* (fonte: la *Summa*; ricostruzione: l'insegnamento; memoria: il Doctor Angelicus, che ha trasformato un commento in un sistema)
24. **Dürer** — *Un corpo umano si può scrivere come costruzioni geometriche?* (fonte: i trattati; ricostruzione: l'officina; memoria: l'incisione, che è una stampa)
25. **Manuzio** — *Il testo è uno e la sua cura ne fa cento: si cambia l'aspetto senza cambiare le parole?* (fonte: le edizioni; ricostruzione: la stamperia; memoria: l'italiana, che è un corpo piccolo e straordinario)
26. **Caxton** — *Un libro deve stare in tasca o sul pulpito: cambiano le dimensioni, non il testo?* (fonte: le edizioni; ricostruzione: l'officina; memoria: l'uomo che portò la stampa in Inghilterra)
27. **Olympe de Gouges** — *Se una società dichiara diritti universali, chi resta fuori dalla porta?* (fonte: la *Dichiarazione*; ricostruzione: la Rivoluzione; memoria: la scrittrice uccisa, che nessuno ha ricordato per due secoli)
28. **Turing** — *Una macchina che capisce le istruzioni: come si sa che ha capito bene?* (fonte: l'articolo del 1936; ricostruzione: il laboratorio; memoria: la sua sorte, che ha cancellato la sua opera)
29. **I tipografi e i privilegi** — *Chi può stampare, chi può leggere, e di chi è il testo?* (fonte: i decreti; ricostruzione: l'arte; memoria: nessuna, ed è la lezione)
30. **Isabella d'Este** — *Un inventario di opere: le metti in ordine, e l'ordine cambia che cosa vedrai?* (fonte: l'inventario; ricostruzione: il gabinetto; memoria: la «marchesa», che non dice nulla della sua mano nel catalogo)

---

## 5. Le schede dei 30 personaggi obbligatori

*(aggiunta — i codici `Q` continuano la serie dell'Anno II (Q01…Q92) da **Q101**, per non riaprire la numerazione; v. §13, Q6)*

Formato di ogni scheda, come in `anno1-ferrara.md` §10 e in `anno2-penisola.md` §5.

### Q101 · Eratostene
- **Periodo:** circa 276–194 a.C. **Luogo:** Alessandria, Cirenaica. **Pin:** Alessandria. **Strato:** `S32`. **Attendibilità:** `D+I` (l'opera è quasi interamente perduta; conosciamo l'*Octad* attraverso frammenti e citazioni).
- **Domanda:** come si scrive un numero minore di zero, quando il segno non esiste?
- **Fonte:** l'*Octad* e i frammenti; **ricostruzione:** la Biblioteca; **memoria:** la Library of Alexandria, che è una leggione romantica.
- **Aggancio 3-1:** l'*Octad* introduce il metodo delle **unità e delle non-unità**: per indicare un numero inferiore all'unità si accendeva una posizione con un contrassegno, e si accumulavano. È l'antenato diretto del **complemento a 2**, e il passaggio di mentalità che il livello chiede (da «il numero c'è / non c'è» a «il numero ha una posizione e un segno») è esattamente quello che Eratostene compie. **Forte.**
- **Motto:** «Un numero senza unità si scrive marcandolo.» **Emblema:** un papiro con una colonna di tacche e un asterisco.

### Q102 · Copernico
- **Periodo:** 1473–1543. **Luogo:** Frombork, Cracovia, Frauenburg. **Pin:** Frombork. **Strato:** `S38`. **Attendibilità:** `D`.
- **Domanda:** il numero che calcoli e il numero che scrivi sono lo stesso numero?
- **Fonte:** il *De revolutionibus* (1543); **ricostruzione:** le osservazioni e i calcoli; **memoria:** la formula, che ha sostituito il libro.
- **Aggancio 3-2:** i calcoli astronomici del XVI secolo sono **tabelle di numeri in virgola mobile** scritti a mano su tavole, con errori che si accumulano e che **nessuno poteva vedere**. Il livello mostra `0,1 + 0,2 ≠ 0,3` e l'errore di rappresentazione: il modello può essere giusto e il numero sbagliato. È il caso più onesto del livello, perché l'errore non è un difetto del calcolo ma della scrittura. **Forte.**
- **Motto:** «Il modello è esatto. I numeri no.» **Emblema:** un quadrante con le orbili segnate a matita.

### Q103 · Augusto
- **Periodo:** 63 a.C. – 14 d.C. **Luogo:** Roma. **Pin:** Roma. **Strato:** `S33`. **Attendibilità:** `D`.
- **Domanda:** come si mette un impero in ordine, riga per riga?
- **Fonte:** le *Res Gestae*; **ricostruzione:** la riforma amministrativa; **memoria:** la pax Romana, che è una formula.
- **Aggancio 3-3:** la riforma del 27 a.C. ridisegna l'impero come una **griglia di province** con funzioni fisse, in modo che ogni elemento occupi una cella e sia indirizzabile. È la matrice (`E6.1.4`) applicata allo Stato, e mostra anche il costo: una griglia che divide per funzione divide anche per giurisdizione. **Medio.**
- **Motto:** «Ho diviso per poter contare.» **Emblema:** una corona d'alloro sopra una griglia di rame.

### Q104 · Solone
- **Periodo:** circa 640–558 a.C. **Luogo:** Atene. **Pin:** Atene. **Strato:** `S31`. **Attendibilità:** `D+I` (le riforme sono note soprattutto dalla tradizione aristofanea e da Aristotele, entrambi non neutrali).
- **Domanda:** dividere un popolo in classi: in base a che cosa, e chi lo decide?
- **Fonte:** la tradizione; **ricostruzione:** la riforma delle classi per reddito; **memoria:** il padre della democrazia ateniese.
- **Aggancio 3-4:** le quattro classi sono un **ordinamento per chiave**: ogni cittadino è collocato secondo una quantità (il reddito), non secondo una qualità. È il *selection sort* in forma istituzionale, e la domanda che il livello pone è la stessa: **ordinare per chiave produce sempre una gerarchia, e la gerarchia dice chi è dentro e chi è fuori.** Il secondo esercizio del livello fa notare che un solo cittadino cambiatoReddito sposta l'intera colonna. **Forte.**
- **Motto:** «Ho ordinato Atene per numero, non per nome.» **Emblema:** quattro fasce sovrapposte, una per classe.

### Q105 · Pericle
- **Periodo:** 495–429 a.C. **Luogo:** Atene. **Pin:** Atene. **Strato:** `S31`. **Attendibilità:** `D`.
- **Domanda:** una lista che cresce di uno in uno: chi entra, e con quale criterio?
- **Fonte:** Tucidide; **ricostruzione:** l'età d'oro; **memoria:** l'Atene, che non è affatto l'Atene che si studia a scuola.
- **Aggancio 3-5 (insertion sort, `E7.2.4`):** l'elenco cresce di un elemento alla volta e ogni nuovo elemento va **inserito al posto giusto**, spostando quelli che vengono dopo. Il livello serve a far vedere il costo: inserire in fondo costa un passo, inserire in testa costa n passaggi. La domanda dell'anno — *chi entra, e con quale criterio?* — è la stessa del `insertion sort`, ed è più scomoda di quanto sembri. **Medio.**
- **Motto:** «L'elenco cresce. Ma per il rotto? Noi i cittadini siamo, gli altri no.» **Emblema:** un calatho (cesto) di grano, con l'etichetta «cittadini».

### Q106 · Platone
- **Periodo:** 427–347 a.C. **Luogo:** Atene, Siracusa. **Pin:** Atene. **Strato:** `S31`. **Attendibilità:** `D+F`.
- **Domanda:** si può dimezzare lo spazio di una ricerca e trovare sempre la risposta?
- **Fonte:** i dialoghi; **ricostruzione:** l'Accademia; **memoria:** la linea divisa e la grotta, che sono due immagini scolastiche diventate autonome.
- **Aggancio 3-6 (ricerca binaria, `E7.1.3`):** la linea divisa non è un algoritmo, ma **l'intuizione che rende possibile il dimezzare**: metà e metà, e poi ancora metà. Il livello richiede però la condizione che il ricordare abbia perso — l'array deve essere **ordinato** — e quella condizione non vale per la verità: non basta dividere lo spazio, bisogna sapere da che parte guardare. È un caso in cui un'immagine potente **suggerisce un algoritmo che funziona solo a metà**, ed è un ottimo esercizio. **Medio.**
- **Motto:** «La linea è divisa. Ma da che parte guarda colui che cerca?» **Emblema:** una linea verticale con un punto in alto, in stile incisione antica.

### Q107 · Belisario
- **Periodo:** circa 500–565. **Luogo:** Costantinopoli, Ravenna, la penisola. **Pin:** Ravenna. **Strato:** `S34`. **Attendibilità:** `D` (ma la fonte principale è Procopio, che era al suo servizio e ne scrisse sia le Storie sia i *Vandali e Goti*, che non sono la stessa cosa).
- **Domanda:** una guerra vinta in quattro anni: quanto è costata davvero?
- **Fonte:** Procopio (che va usato con cautela: è al tempo stesso testimone e dipendente); **ricostruzione:** la guerra gotica; **memoria:** il generale fedele, che non ha perso nulla e che non ha mai governato da solo.
- **Aggancio 3-7 (complessità, `E9.2`):** la guerra di riconquista è l'esempio storico più pulito del **costo che cresce più in fretta del numero di soldati**: si espande il fronte, si espande il logistico, e la città assediata costa più di un campo aperto. Il livello permette di misurare il tempo (`E9.8`) e la domanda che il gioco pone è: **quando la grandezza di un sistema diventa il suo problema, come si fa a saperlo prima che sia troppo tardi?** Adriano, alla tappa 3-3, è la versione politica della stessa domanda. **Forte.**
- **Motto:** «Vittorie in quattro anni. E poi?» **Emblema:** un falco stilizzato, tratto da una moneta.

### Q108 · Federico II
- **Periodo:** 1194–1250. **Luogo:** Palermo, Castel del Monte, Venezia. **Pin:** Castel del Monte. **Strato:** `S36`. **Attendibilità:** `D`.
- **Domanda:** una forma che contiene sé stessa, otto volte: è la stessa forma o sono otto?
- **Fonte:** l'*De arte venandi cum avibus*; **ricostruzione:** la corte; **memoria:** il meraviglioso, che non dice niente del costo.
- **Aggancio 3-8 (ricorsione, `E5.1`):** il **Castel del Monte** è un ottagono con otto torri ottagonali: la forma chiama sé stessa, e ogni torre è istanza della stessa definizione. È il caso base e passo ricorsivo resi in pietra, e il livello chiede esattamente la domanda che l'edificio pone: **quando l'istanza è identica alla definizione, il sistema è finito o si espande all'infinito?** Federico scrisse il più grande trattato di falconeria dell'Europa medioevale nello stesso periodo, su un castello che poteva guardare in otto direzioni: la stessa forma che organizza la conoscenza e organizza il territorio. **Forte.**
- **Motto:** «Otto torri, una forma sola.» **Emblema:** un ottagono con otto ottagoni più piccoli ai vertici.

### Q109 · Alessandro Magno
- **Periodo:** 356–323 a.C. **Luogo:** Pella, Persepoli, Babilonia. **Pin:** Pella. **Strato:** `S32`. **Attendibilità:** `D+M` (le fonti sono tutte successive, e tutte hanno un interesse dinastico).
- **Domanda:** un impero diviso fra molti: i pezzi tornano a formare qualcosa?
- **Fonte:** Arriana; **ricostruzione:** le successioni; **memoria:** il conquistatore, che ha perso l'impero in quarant'anni.
- **Aggancio 3-9 (divide et impera, `E8.2`):** alla morte di Alessandro l'impero viene **diviso** fra i successori, e i pezzi si combattono per tre generazioni, finché Roma non li raccoglie tutti e uno. È il ciclo completo del livello — dividi, ordina, fondi — con un esito che nessuno dei protagonisti voleva: la fusione avviene **per conquista**, non per riunione. La domanda dell'anno (che cosa resta, quando si divide?) riceve qui la sua formulazione migliore. **Forte.**
- **Motto:** «L'impero è mio. Adesso è di sette.» **Emblema:** sette punte di freccia che si incontrano.

### Q110 · Alfonso I d'Este
- **Periodo:** 1476–1534 (duca 1505–1534). **Luogo:** Ferrara. **Pin:** Ferrara. **Strato:** `S39`. **Attendibilità:** `D`.
- **Domanda:** i cannoni escono dalla fonderia: in che ordine li schieriamo, e con quale criterio?
- **Fonte:** l'archivio; **ricostruzione:** le guerre; **memoria:** il duca artigliere.
- **Aggancio 3-10 (prova di corte, ordinare e contare):** la fonderia ducale è la **metafora dell'anno** dichiarata dal curricolo («la fonderia e l'artiglieria»): un intero processo industriale che produce pezzi tutti diversi e tutti ordinabili per calibre. Il compito del livello è ordinare i pezzi e **contare i passi** (`E7`, `E9`), cioè capire che il costo di un ordine non dipende dal numero di pezzi ma da come sono disposti. **Forte.**
- **Motto:** «Il bronzo non ha idee. Io sì.» **Emblema:** un cavallo su una rotaia di cannone, in stile araldico.

#### 3.10 bis — il decreto del 1510 e la comunità ebraica di Ferrara
*(decisione 3 del §0.1 — parte della tappa 3-10, non una tappa a sé)*

Questo passaggio è il più delicato dell'intero terzo anno, e va costruito con la stessa cura di una tappa.

**Che cosa è documentato.** Alfonso I emanò nel 1510 un decreto che imponeva l'uscita agli ebrei dai suoi domini, e la comunità ebraica di Ferrara — presente in città fin dal Medioevo, e già incontrata al **MEIS** dall'Anno I (tappa 1-6) — fu fra le prime a essere coinvolte. *Verificare la data esatta, il testo del decreto, le condizioni e le mete dell'esodo* (v. §12, V1). Il decreto appartiene al periodo in cui Alfonso era in guerra contro il papa Giulio II e fu scomunicato: **non va spiegato come un atto di antisemitismo ideologico, ma come un atto di un piccolo Stato che usa l'antisemitismo come strumento di pressione politica.** È la domanda che il gioco deve porre, ed è più forte di qualunque giudizio moralistico.

**Come entra nel gioco.** Non come «fatto storico da ricordare», ma come **confronto fra due fonti dello stesso periodo**, che è il meccanismo del §6.2:

1. **la fonte dell'epoca, voce del potere:** il decreto, con la sua data e il suo testo, presentato come documento d'archivio;
2. **la ricostruzione, voce di chi era dentro:** la comunità ebraica ferrarese, che dal 1510 non c'è più in città, con l'elenco delle famiglie e degli artigiani (molti di loro medici, attrici, argentieri) e la loro destinazione;
3. **la memoria successiva, voce del duca:** la fronte del *Camerino d'alabastro*, che negli stessi anni fa commissionare a Bellini, Tiziano e Dosso Dossi le opere più belle mai riunite in una stanza. La stessa corte, nello stesso anno, fa le due cose.

**La domanda che il gioco pone** (è una delle due visioni facoltative, ed è obbligatoria in termini di presenza): *chi scrive la storia di Ferrara, e chi non la scrive?* E la risposta che il gioco **non** dà: la seconda voce è la parte che «non ha lasciato documenti» nel senso che il gioco usa altrove — qui li ha lasciati, ma sono documenti di altri, redatti da altri.

**Regole di conduzione** (proposte, da approvare):
- la scheda del decreto è **breviata, con data e fonte**, e non occupa più schermo dei tre paragrafi di confronto;
- nessun ritratto, nessuna scena di violenza, nessuna ricostruzione emotiva: solo documenti e domande;
- il nome della comunità **non** è «gli ebrei», ma **la comunità ebraica di Ferrara**;
- il collegamento con l'Anno I è esplicito: la tappa 1-6 al MEIS presenta la comunità come **presente**, e questa tappa mostra che cosa significa quando la stessa comunità scompare dalla città. Chi ha giocato l'anno 1 ha già visto la porta da cui escono;
- l'aggancio trasversale è **uno solo e non valutato**, come impone `AGENTS.md` §3: qui l'articolo 9 della Costituzione, che tutela il patrimonio e i luoghi di culto ebraici, e che nel 1950 dà a quella scomparsa una forma giuridica di esistenza.

**Perché questa tappa è la più importante dell'anno.** Perché è la prova visiva del criterio del progetto: un personaggio storico non è una figura da onorare, è **un problema a cui si accede da più fonti, che danno risposte diverse**. Alfonso I è **contemporaneamente** il fondatore della fonderia, il committente del Camerino, l'uomo scomunicato tre volte, il coniuge di Lucrezia Borgia **e l'artefice di quel decreto**. Se il gioco ne mostrasse uno solo degli cinque, violerebbe le proprie regole.

### Q111 · Ludovico Ariosto
- **Periodo:** 1474–1533. **Luogo:** Ferrara. **Pin:** Ferrara. **Strato:** `S39`. **Attendibilità:** `D`.
- **Domanda:** due fili che si intrecciano secondo una regola: chi scrive conosce la regola?
- **Fonte:** l'*Orlando furioso* (1516, e poi le edizioni del 1521 e del 1532); **ricostruzione:** la corte; **memoria:** il poema, che ha superato di gran lunga il suo autore.
- **Aggancio 3-11 (ricerca di schemi, automi, `F1.1`):** il *Furioso* è costruito su **due talismani** — Rinaldo e Angelica — che compaiono e scompaiono secondo una regola che l'Autore conosce e il lettore no, e la cui ripetizione produce la struttura dell'opera. È un **automa a stati finiti** (`F1.1`) prima di avere il nome, e le tre edizioni del 1516, 1521 e 1532 sono tre versioni dello stesso testo con regole diverse. Il livello chiede di riconoscere il pattern (`E7.4.1`) e di chiedersi se chi lo ha scritto lo sapesse davvero o lo scoprisse strada facendo. **Forte.**
- **Motto:** «Ho scritto un labirinto. Non ricordo se l'ho disegnato o se me l'hanno fatto.» **Emblema:** due fili d'oro intrecciati a formare una A.

### Q112 · Alcuino
- **Periodo:** circa 735–804. **Luogo:** York, Aquisgrana. **Pin:** Aquisgrana. **Strato:** `S35`. **Attendibilità:** `D`.
- **Domanda:** una scuola che registra: che cosa si scrive, e in quale ordine?
- **Fonte:** le lettere; **ricostruzione:** la rinascita carolingia; **memoria:** il palagio di Carlomagno, che non è mai esistito.
- **Aggancio 3-12 (file e CSV, `B11.2`):** la scuola di palazzo **produce registri**: chi è entrato, da dove viene, che cosa impara, che esito ha avuto. Sono file di testo con campi separati da un separatore, scritti e riletti più volte, con problemi di carattere (`B4.3`) che in latino non ci sono quasi e che nelle copie celtiche e anglosassoni sì. Il livello serve a far vedere che **la forma di un dato dipende dalla macchina e dall'epoca che la scrive**, e che un file senza un separatore esplicito si rompe appena un campo contiene il separatore. **Medio.**
- **Motto:** «Non ho salvato il mondo antico. Ho salvato quello che si poteva copiare.» **Emblema:** un calamo e un rotolo con una colonna di nomi.

### Q113 · Leonardo da Vinci
- **Periodo:** 1452–1519. **Luogo:** Firenze, Milano, Roma, Amboise. **Pin:** Milano. **Strato:** `S38`. **Attendibilità:** `D`.
- **Domanda:** un problema enorme si scompone in pezzi che si possono tenere in mano?
- **Fonte:** i quaderni; **ricostruzione:** il lavoro; **memoria:** l'inventore geniale, che ha perso il metodo.
- **Aggancio 3-13 (top-down e modularità, `H4.1`):** i quaderni contengono **osservazioni decomposta**: la struttura di un uccello è scomposta in parti che si possono studiare separatamente e poi ricomporre. È la modularità (`H4.1`) nel senso più letterale, e il livello serve a mostrare l'altra metà della disciplina: un modulo è utile solo se l'interfaccia è chiara, e l'interfaccia dei quaderni di Leonardo è **la carta**, che non dichiara nulla e quindi va letta male. Leonardo è già la tappa 2-8 dell'Anno II (ritorno: v. §6.4). **Medio.**
- **Motto:** «Non ho scritto un metodo. Ho scritto un modo di guardare.» **Emblema:** un compasso chiuso su una figura geometrica.

### Q114 · Niccolò Machiavelli
- **Periodo:** 1469–1527. **Luogo:** Firenze. **Pin:** Firenze. **Strato:** `S38`. **Attendibilità:** `D`.
- **Domanda:** lo stesso libro riveduto per anni, con un destinatario cambiato: quale versione è vera?
- **Fonte:** gli autografi e le edizioni; **ricostruzione:** la ragione; **memoria:** il Cinquecento, che ha letto quasi solo la seconda versione.
- **Aggancio 3-14 (documentazione e controllo di versione, `H5.1`):** il *Principe* esiste in due forme, con dedicatari diversi (Giuliano de' Medici, poi Lorenzo di Piero) e un finale rimosso. È un **controllo di versione** prima che l'idea esistesse, e il livello chiede che cosa succeda quando due versioni non coincidono: **quale si considera il testo?** La risposta del gioco è che non esiste una risposta, e che ogni risposta è una scelta che va motivata. La stessa figura, questa volta, non è l'osservatore cinico ma il primo a dover rendere conto di ciò che aveva scritto. **Forte.**
- **Motto:** «Ho scritto due libri. Dicono cose diverse. Ero io, entrambi.» **Emblema:** due fogli sovrapposti, di cui si vede solo il bordo del secondo.

### Q115 · Dosso Dossi
- **Periodo:** circa 1489–1542. **Luogo:** Ferrara. **Pin:** Ferrara (Camerino). **Strato:** `S39`. **Attendibilità:** `D`.
- **Domanda:** una parete con dentro un bassorilievo e un dipinto: sono due cose diverse?
- **Fonte:** le opere e i contratti; **ricostruzione:** il Camerino; **memoria:** la sala, che non si vede più.
- **Aggancio 3-15 (formati di immagine, `B6.4`, `B6.5`):** il **Camerino d'alabastro** contiene due tecniche incompatibili nello stesso spazio: i **bassorilievi in alabastro**, che sono figure vettoriali (curve che si scalano all'infinito senza perdersi) e i **dipinti**, che sono superfici di colore, cioè matrici di pixel (`B6.1`) che si degradano se le ingrandisci. La domanda che il gioco pone è la domanda del livello, detta in italiano: **un'immagine che si può ingrandire all'infinito è un'immagine o è un'istruzione?** È il primo incontro del percorso con l'idea di grafica vettoriale, e il fatto che il problema sia stato *posto* quattro secoli prima su una parete di uno studiolo ferrarese è il punto che il livello deve far emergere. **Forte.**
- **Motto:** «Qui un dio è scolpito. Qui è dipinto. Sembra la stessa cosa e non lo è.» **Emblema:** un rilievo e una macchia di colore sulla stessa parete.

### Q116 · Johannes Gutenberg
- **Periodo:** circa 1400–1468. **Luogo:** Magonza, Strasburgo. **Pin:** Magonza. **Strato:** `S38`. **Attendibilità:** `D+I` (l'uomo è semilegendario; la tecnica è documentata dai documenti processuali di Strasburgo).
- **Domanda:** come si moltiplica un testo centomila volte senza scriverlo centomila volte?
- **Fonte:** i documenti della causa di Strasburgo (che riguarda il sistema di fusione dei caratteri, non la stampa) e i torchi; **ricostruzione:** l'officina; **memoria:** l'inventore singolo, che fu un'impresa collettiva.
- **Aggancio 3-16 (compressione senza perdita, `B9.1.4`):** la stampa è **compressione senza perdita** nella sua forma più brillante: il testo viene scomposto in una sequenza di **sottostringhe** che si ripetono, e alla decodifica le sottostringhe vengono ricomposte nell'ordine giusto. È LZ77 (`B9.1.4`) sette secoli prima, e la differenza di qualità è la stessa che c'è fra una compressione che conserva tutto e una che butta via: **questa conserva tutto, e il costo si paga una volta sola.** La domanda del livello («nessun compressore riduce tutti i file») si applica perfettamente: il torchio riduce il costo del testo ma non riduce il costo dell'inchiostro. **Forte.**
- **Motto:** «Ho scritto il libro una volta sola. Il resto l'ha scritto il torchio.» **Emblema:** un torchio a leva, visto di profilo.

### Q117 · Josquin des Prez *(aggiunta — non era nel catalogo di Pietro)*
- **Periodo:** circa 1452–1521. **Luogo:** Ferrara, la corte estense. **Pin:** Ferrara (cappella). **Strato:** `S39`. **Attendibilità:** `D`.
- **Domanda:** una messa costruita con le sole vocali di un nome: un suono si può calcolare?
- **Fonte:** le partiture; **ricostruzione:** la cappella ducale; **memoria:** la musica, che è diventata una cosa autonoma e ha perso la parola.
- **Aggancio 3-17 (audio digitale, `B7.2`, `B7.3`):** la *Missa Hercules Dux Ferrariae* è costruita con il **soggetto cavato** dalle vocali del nome del duca: il nome diventa la melodia, e la melodia diventa l'armonia. È **codifica**: una sequenza di lettere trasformata in sequenza di note, cioè un **campionamento** (`B7.2`) e una **quantizzazione** (`B7.3`) — un simbolo discreto che prende il posto di un suono continuo. Il gioco mostra la stessa operazione in due direzioni: dal nome alla musica, e dalla musica al nome, e la domanda è se si possa tornare indietro senza perdita. **Forte.**
- **⚠ Anacronismo da correggere (v. §12, V2).** Josquin fu alla corte estense **sotto Ercole I**, non sotto Alfonso I, che successe nel 1505. La risorsa che giunge in Alfonso è dunque una musica di dieci anni prima, composta nella stessa corte da suo padre: va narrata come tale, e il gioco può usarla come occasione per mostrare che **alla corte le cose arrivano sempre da prima**. In alternativa, la tappa può essere affidata ad **Alfonso stesso** (che coltivava personalmente la passione per la musica) come voce di secondo livello.
- **Motto:** «Il nome del duca è la partitura.» **Emblema:** le cinque vocali in fila, come spartito.

### Q118 · Miguel de Cervantes
- **Periodo:** 1547–1616. **Luogo:** Alcalá de Henares, Madrid. **Pin:** Alcalá de Henares. **Strato:** `S41`. **Attendibilità:** `D`.
- **Domanda:** un libro che descrive un mondo che non esiste: che cosa si perde, e che cosa si guadagna?
- **Fonte:** il testo; **ricostruzione:** la vita, la battaglia di Lepanto, la prigionia; **memoria:** il cavaliere, che non esiste più.
- **Aggancio 3-18 (compressione con perdita, `B9.2.1`):** la compressione con perdita funziona **eliminando ciò che non si percepisce**. Il *Chisciotte* fa il contrario e il contrario è più interessante: **aggiunge** ciò che non c'è, e da quella aggiunta nasce una verità (sui soprusi, sulla giustizia, sui poveri) che non era nel testo di partenza. La domanda del livello diventa: **un'opera che non descrive il reale descrive il reale meglio di una che lo descrive?** Il gioco non risponde, e mostra che la perdita e l'aggiunta hanno lo stesso effetto. **Medio.**
- **Motto:** «Il cavaliere non esiste. La questione che pone, sì.» **Emblema:** un rotolo con una chierica e un coniglio.

### Q119 · Erasmo da Rotterdam
- **Periodo:** circa 1466–1536. **Luogo:** Rotterdam, Basilea, la rete europea. **Pin:** Basilea. **Strato:** `S40`. **Attendibilità:** `D`.
- **Domanda:** un libro in cui il testo porta dentro di sé la propria struttura e le proprie domande?
- **Fonte:** le edizioni e le lettere; **ricostruzione:** la *Respublica litteraria*, la rete di corrispondenza; **memoria:** l'umanista che non ha fatto la Riforma ma l'ha resa possibile, e che si è schierato contro Lutero.
- **Aggancio 3-19 (markup, `B13.5`):** un'edizione critica di Erasmo non è un testo continuo: è il testo **interrotto da annotazioni** che dicono «questa parola è sospetta», «questa frase è di un altro autore», «qui il manoscritto diverge». Il testo porta dentro di sé la propria **struttura** e i propri **commenti**, ed è navigabile per punti esattamente come un documento con markup (`B13.5`). È il livello che introduce l'idea di contrassegnare il testo, ed è l'antecedente più diretto del concetto stesso di markup. **Forte.**
- **Motto:** «Non ho scritto un commento al testo. Ho scritto un testo a due voci.» **Emblema:** due colonne di testo, una grande e una sottile, con trattini di richiamo.

### Q120 · Giovanni Bellini *(aggiunta — già presente in `anno1-ferrara.md` come P45-adjacent, con Dossi e Tiziano)*
- **Periodo:** circa 1430–1516. **Luogo:** Venezia, Ferrara. **Pin:** Ferrara. **Strato:** `S39`. **Attendibilità:** `D`.
- **Domanda:** un'opera spezzata in venti parti e portate in quattro città: si può ricomporre?
- **Fonte:** le opere e i documenti; **ricostruzione:** il Camerino; **memoria:** l'artista che non ha dipinto la sala, che pure gli diede il nome.
- **Aggancio 3-20 (prova di corte, formati e qualità):** la prova di corte dell'anno è **il Camerino**, e la sua difficoltà è che le opere furono **smontate e disperse nel 1598**, e oggi sono in musei diversi. Ricomporre l'ambiente significa scegliere: dove sta il rilievo, in che ordine, e che cosa si deve sostituire quando il pezzo è andato perduto. È il livello sui formati (`B6`, `B9`, `K2`) applicato a un problema che non è di computer: **la ricostruzione è sempre una decisione, e la decisione va dichiarata.** **Forte.**
- **Motto:** «La sala è smontata da sessant'anni. Ho lasciato le opere in ordine: l'ordine, quello no.» **Emblema:** un riquadro vuoto con un numero (l'inventario).

### Q121 · Carlo Magno
- **Periodo:** 742–814. **Luogo:** Aquisgrana. **Pin:** Aquisgrana. **Strato:** `S35`. **Attendibilità:** `D`.
- **Domanda:** le lettere hanno forme diverse in epoche diverse: quale giusto scrivere?
- **Fonte:** il *De litteris collationibus*; **ricostruzione:** la riforma; **memoria:** l'imperatore, che non ha scritto il trattato.
- **Aggancio 3-21 (font e tipografia, `B13.2`, `B13.3`):** il *De litteris* descrive **tre scritture** diverse (la corsiva, la cancelleresca minuscule, la maiuscola) e **le usa per tre scopi** diversi. Sono già, di fatto, **famiglie e stili** (`B13.2`), con regole di rendering diverse: una è veloce, una è elegante, una è monumentale. Il livello chiede che cosa succede a un carattere quando cambia la sua funzione — diventa un font (`B13.2`) — e la domanda storica è più pesante: **chi decide quale scrittura è quella giusta?** La risposta è una riforma amministrativa, e come tutte le risposte di potere ha un costo per chi scriveva in precedenza. **Forte.**
- **Motto:** «Ho ordinato le lettere. Non ho ordinato chi le scrive.» **Emblema:** tre lettere «a» in tre stili diversi.

### Q122 · Giovanni Boccaccio
- **Periodo:** 1313–1375. **Luogo:** Certaldo, Firenze. **Pin:** Certaldo. **Strato:** `S37`. **Attendibilità:** `D`.
- **Domanda:** cento storie ordinate in dieci giornate: che cosa tiene insieme una struttura così?
- **Fonte:** il *Decameron*; **ricostruzione:** la peste e i gruppi che si rifugiarono in campagna; **memoria:** le novelle, che sono un genere, non un libro.
- **Aggancio 3-22 (XML, `B11.3`):** il *Decameron* ha una **struttura ad albero rigorosa**: dieci giornate, dieci novelle ciascuna, dieci narratori, e ogni novella ha un tema che si collega alla cornice. È un documento **gerarchico e ben formato** (`B11.3`), con attributi (giornata, numero, narratore, tema) che senza i quali il testo non significa niente, e con una regola di buona formazione che si può violare in modi che il lettore non nota ma il computer sì. Il livello serve a far vedere che **un documento senza schema è un documento che non puoi interrogare**, e che il *Decameron* è un documento che si può interrogare in mille modi. **Medio.**
- **Motto:** «Dieci giornate, dieci voci. La cornice non è un ornamento: è l'indice.» **Emblema:** un albero con dieci rami.

### Q123 · Tommaso d'Aquino
- **Periodo:** 1225–1274. **Luogo:** Parigi, Orvieto, Napoli. **Pin:** Parigi. **Strato:** `S37`. **Attendibilità:** `D`.
- **Domanda:** un testo che si cita con una sigla e rimanda a un altro punto di sé stesso: si può navigare?
- **Fonte:** la *Summa theologiae*; **ricostruzione:** l'insegnamento; **memoria:** il Doctor Angelicus, che ha trasformato un commento in un sistema.
- **Aggancio 3-23 (HTML, struttura e semantica, `K2.1`):** la *Summa* è organizzata in **articoli numerati, con sigle fisse** (Quaestio, Articolo, Obiezione, Risposta), e ogni passaggio **cita gli altri passaggi con quelle sigle**, formando una rete di rinvii interni al testo. Chi studiava la *Summa* non leggeva un libro dall'inizio alla fine: **saltava da un articolo all'altro seguendo i rinvii**, che sono esattamente i collegamenti ipertestuali. È il livello che introduce l'idea di **rimandare a un punto preciso di un documento** (`K2.2`, `K2.3`) e, con essa, la distinzione fra testo e metadato che era già stata posta al livello 1-27. **Forte.**
- **Motto:** «Non si legge tutto. Si salta dall'articolo all'articolo, e ogni salto ha un nome.» **Emblema:** un articolo con una riga di rinvii.

### Q124 · Albrecht Dürer *(aggiunta — non era nel catalogo di Pietro)*
- **Periodo:** 1471–1528. **Luogo:** Norimberga, Venezia, Paesi Bassi. **Pin:** Norimberga. **Strato:** `S38`. **Attendibilità:** `D`.
- **Domanda:** un corpo umano si può scrivere come costruzioni geometriche?
- **Fonte:** i trattati (*Underweysung der Messung*, 1525) e le incisioni; **ricostruzione:** l'officina; **memoria:** l'incisione, che è una stampa prima ancora di essere un'arte.
- **Aggancio 3-24 (SVG, `B6.4`, `K12`):** le figure del *Vier Bücher von menschlicher Proportion* sono **costruite con linee, cerchi e rapporti**, e la sua incisione è una **stampa su metallo**: un file che si può replicare esattamente, che si può ridimensionare senza perdersi (è già vettoriale) e che si può alterare. È il livello che introduce la grafica come testo (`B6.4`), e la domanda che pone è la più affascinante del percorso: **un'immagine che descrive il corpo con i numeri è un'immagine o è una descrizione?** **Forte.**
- **Motto:** «Il corpo si misura. La misura si stampa. Il corpo no.» **Emblema:** un compasso e un reticolo geometrico.

### Q125 · Aldo Manuzio *(aggiunta — non era nel catalogo di Pietro)*
- **Periodo:** 1449/1452–1515. **Luogo:** Venezia. **Pin:** Venezia. **Strato:** `S38`. **Attendibilità:** `D`.
- **Domanda:** il testo è uno e la sua cura ne fa cento: si cambia l'aspetto senza cambiare le parole?
- **Fonte:** le edizioni e i cataloghi; **ricostruzione:** la stamperia; **memoria:** l'«italiciana», che è un corpo piccolo e straordinario.
- **Aggancio 3-25 (CSS, `K3.1`):** Manuzio non cambia le parole, cambia **tutto il resto**: il formato, il carattere, il corpo, la spaziatura, il taglio della carta, l'impaginazione, il lettore a cui il libro è destinato. Il testo è identico; **l'aspetto è un livello separato**, applicato a quel testo e non a un altro. È il concetto di CSS (`K3.1`) — stile separato dal contenuto — nella sua forma più antica, e il livello chiede che cosa succede quando lo stile diventa così potente da cambiare **significato**: un testo in caratteri grandi non dice la stessa cosa di uno in caratteri piccoli. **Medio.**
- **Motto:** «Le parole sono di Virgilio. Il taglio della carta è mio.» **Emblema:** un' «a» corsiva entro un riquadro di misure tipografiche.

### Q126 · William Caxton *(aggiunta — non era nel catalogo di Pietro)*
- **Periodo:** circa 1422–1491. **Luogo:** Westminster, Bruges, Colonia. **Pin:** Westminster. **Strato:** `S39`. **Attendibilità:** `D`.
- **Domanda:** un libro deve stare in tasca o sul pulpito: cambiano le dimensioni, non il testo?
- **Fonte:** i documenti della stamperia; **ricostruzione:** l'officina; **memoria:** l'uomo che portò la stampa in Inghilterra.
- **Aggancio 3-26 (impaginazione e design responsive, `K3.x`):** lo stesso testo esiste in **formati diversi** per destinatari diversi: il *Canterbury Tales* stampato in un formato che si porta in tasca, o in uno che si legge in chiesa. Non è responsive nel senso tecnico, ma è la **stessa domanda**: **che cosa deve adattarsi, e che cosa deve restare identico?** Il livello serve a far capire che la risposta non è ovvia: se cambiasse il testo, non sarebbe lo stesso libro; se non cambiasse niente, sarebbe scomodo. **Forte.**
- **Motto:** «Un libro per la strada e un libro per il pulpito. Le stesse storie, due gabinetti.» **Emblema:** un libro aperto in due formati diversi, affiancati.

### Q127 · Olympe de Gouges
- **Periodo:** 1748–1793. **Luogo:** Parigi. **Pin:** Parigi. **Strato:** `S42`. **Attendibilità:** `D`.
- **Domanda:** se una società dichiara diritti universali, chi resta fuori dalla porta?
- **Fonte:** la *Dichiarazione dei diritti della donna e della cittadina* (1791); **ricostruzione:** la Rivoluzione; **memoria:** la scrittrice uccisa nel 1793 e dimenticata per due secoli.
- **Aggancio 3-27 (usabilità e accessibilità, `Q8.x`):** l'accessibilità non è un extra: è **chi può davvero usare ciò che è stato costruito**. La *Dichiarazione* del 1789 dice «uomini» e con questo intende metà dell'umanità; de Gouges scrive il documento che mancava e chiede che cosa significhi «cittadino» quando la parola ha un campo di applicazione più piccolo della sua promessa. Il livello serve a far capire che **un'interfaccia perfetta per chi ha un pc, uno schermo e le mani libere non è accessibile**: è solo ben fatta. Il legame con la tappa 3-4 (Solone che ordina Atene per reddito) e con la 3-5 (Pericle e chi è cittadino) è **diretto e voluto**: la stessa domanda in tre epoche. **Forte.**
- **Motto:** «Se la donna può salire sulla scala, deve poter salire sulla piattaforma.» **Emblema:** due scale, una stretta e una larga, con la stessa scritta.

### Q128 · Alan Turing *(aggiunta — non era nel catalogo di Pietro)*
- **Periodo:** 1912–1954. **Luogo:** Manchester, Cambridge, Bletchley. **Pin:** Manchester. **Strato:** `S43`. **Attendibilità:** `D`.
- **Domanda:** una macchina che capisce le istruzioni: come si sa che ha capito bene?
- **Fonte:** *On Computable Numbers* (1936) e i lavori sulla macchina di Enigma; **ricostruzione:** il laboratorio; **memoria:** la sua sorte, che ha cancellato la sua opera, e la legge che non gli ha dato la cittadinanza, che è la stessa domanda della tappa 3-27.
- **Aggancio 3-28 (JavaScript, `K4.x`):** il livello introduce la **pagina che reagisce**: un programma che riceve un input, lo elabora e produce un output, e che **non fa niente finché non riceve l'input**. La macchina di Turing è la formalizzazione esatta di questa idea, e il suo limite (la *macchina universale*, che sa simulare qualunque altra macchina) è l'idea che rende possibile l'idea stessa di programma. La domanda del livello — *come si sa che ha capito bene?* — è la domanda della verifica (`H6`), che è il livello 2-19 visto dal lato opposto: lì si cercava l'errore in un programma, qui si cerca un criterio per dire che è giusto. **Forte.**
- **Motto:** «Ho descritto una macchina che non esiste. Funziona meglio di tante che esistono.» **Emblema:** una nastro di carta con due stati, letta da una testa.

### Q129 · I tipografi e i privilegi *(collettivo)*
- **Periodo:** dal XV al XVI secolo. **Luogo:** Venezia, Parigi, Roma, Colonia. **Pin:** Roma. **Strato:** `S38`. **Attendibilità:** `C`.
- **Domanda:** chi può stampare, chi può leggere, e di chi è il testo?
- **Fonte:** i decreti, i privilegi, l'*Imprimatur*; **ricostruzione:** l'arte tipografica come industria; **memoria:** nessuna — e questa è la lezione.
- **Aggancio 3-29 (pubblicare; licenze e diritto d'autore, `K8.x`, `U4.3`):** chi può stampare un libro, e chi può subirlo, non è una domanda tecnica: è **una domanda di potere**, e nel Cinquecento ha risposte diverse in ogni città. Il *privilegium* concede a uno stampatore il diritto esclusivo su un testo; l'*imprimatur* impone il permesso; il *diritto d'autore* moderno non esiste ancora e non è semplicemente «l'evoluzione del privilegio»: chiama in causa l'autore, che nel Cinquecento non è quasi mai l'editore. Il livello serve a far vedere che **il diritto d'autore è una costruzione sociale**, e che chi ne ha la storia più lunga non è l'autore. **Medio.**
- **Motto:** «Il testo è di chi lo scrive. La licenza è di chi possiede il torchio.» **Emblema:** un torchio con un sigillo di piombo appeso al braccio.

### Q130 · Isabella d'Este
- **Periodo:** 1474–1539. **Luogo:** Mantova, Ferrara, Milano. **Pin:** Mantova. **Strato:** `S39`. **Attendibilità:** `D`.
- **Domanda:** un inventario di opere: le metti in ordine, e l'ordine cambia che cosa vedrai?
- **Fonte:** l'inventario e la corrispondenza; **ricostruzione:** il gabinetto; **memoria:** la «marchesa», che non dice nulla della sua ruolo.
- **Aggancio 3-30 (prova finale, il sito della corte):** il gabinetto di Mantova è uno dei primi **musei** d'Europa, costruito per ordine alfabetico — un criterio che, quando fu redatto, era il modo più razionale di **non mettere in ordine**. L'inventario ha una **sede propria** (marmo, bronzo, pittura) che non è un criterio estetico ma uno strutturale, e da lì la domanda della prova finale: **un archivio con un solo criterio di ordinamento rende impossibile rispondere a certe domande.** La sorella del duca chiude l'anno con la domanda che il gioco deve lasciare aperta. È il livello sui formati (`B11`, `K2`) applicato a un problema di Stato, ed è la conclusione tecnica dell'anno. **Forte.**
- **Motto:** «Ho ordinato tutto per lettera. E ho scoperto che così non vedo niente.» **Emblema:** una mensola con tre oggetti e una chiave.

---

## 6. Il criterio: nessun personaggio è una figurina

*(materiale di Pietro, §§XXVI–XXVII, riformulato in regole operative — le regole sono quelle dell'Anno II e valgono per tutti gli anni)*

### 6.1 La catena

```
PERSONAGGIO → FONTE → AZIONE → CONSEGUENZA → INTERPRETAZIONE → DOMANDA
```

Regola operativa: **ogni tappa deve mostrare almeno un punto in cui la catena si spezza.** Una tappa in cui la catena fila liscia è una tappa sbagliata. Le sei funzioni che il materiale assegla al personaggio (testimone, contraddittore, fonte, falsa certezza, ponte geografico, ponte temporale) sono le sei modalità con cui un personaggio può **spezzare** la catena, e vanno usate tutte nel corso dell'anno.

### 6.2 I tre livelli di fonte

| Livello | Che cos'è | Come si mostra nel gioco |
|---|---|---|
| **1. La fonte dell'epoca** | una lettera, un'iscrizione, un decreto, un'opera, un processo, una cronaca, una fotografia, un discorso, un filmato | il **documento** che arriva sulla tavola della corte |
| **2. La ricostruzione dello storico** | che cosa possiamo ragionevolmente concludere dalle fonti | la **scheda**, con i gradi di attendibilità e le parti ignote |
| **3. La memoria successiva** | come è stato raccontato quel personaggio | la **terza carta**, spesso in contrasto con la seconda, e da cui si parte per la domanda |

> **una fonte non è soltanto qualcosa che conferma una risposta: è qualcosa che deve poter essere interrogato.**

### 6.3 Le funzioni del personaggio nel gioco

Le sei funzioni del materiale di Pietro diventano sei **tipi di tappa**, dichiarati nella scheda:

| Funzione | Che cosa fa nel gioco | Esempio nell'anno 3 |
|---|---|---|
| **Testimone** | il giocatore incontra chi ha visto | Belisario (3-7) |
| **Contraddittore** | due personaggi dicono la cosa opposta | Eratostene (3-1) contro la «Library of Alexandria» |
| **Fonte** | il giocatore riceve un testo e deve capire che tipo è | Alcuino (3-12), i tipografi (3-29) |
| **Falsa certezza** | una figura circondata da leggende | Boccaccio (3-22) e il Decameron come genere |
| **Ponte geografico** | la risorsa che permette di spostarsi | Tutte le tappe: la risorsa che arriva |
| **Ponte temporale** | una persona ricordata secoli dopo | Cervantes (3-18) e il suo cavaliere immaginario |

### 6.4 I ritorni: la stessa persona, un'altra voce

*(aggiunta — problema specifico di un percorso su tre epoche)*

Con tre anni di percorso, alcune persone **compaiono due volte**. Non è un difetto, è una risorsa, purché valgano tre regole:

1. **mai la stessa scheda, mai la stessa domanda, mai lo stesso livello**;
2. **la seconda volta la voce è un'altra**: l'anno 1 la persona è la voce del suo luogo, l'anno 2 è una porta su un problema, l'anno 3 è una risorsa che arriva a Ferrara e che Alfonso commenta;
3. **il ritorno deve essere annunciato**, e il gioco deve dire «questa persona l'hai già incontrata»: il gioco diventa così un archivio di sé stesso.

Elenco dei ritorni previsti (proposta, da verificare):

| Personaggio | Prima occorrenza | Seconda occorrenza | Che cosa cambia |
|---|---|---|---|
| Leonardo da Vinci | 2-8, il linguaggio delle figure | 3-13, modularità e scomposizione | da voce di un luogo a voce di un metodo |
| Copernico | 1-10 (facoltativa), lo Studio di Ferrara | 3-2, l'errore di rappresentazione | da nome su una laurea a voce sui numeri |
| Ötzi | 2-1, prima tappa dell'Anno II | visione facoltativa in 3-4 | da tappa a sguardo, dal «dato» all'«Europa» |
| Isidoro | — | 3-22, la struttura del sapere | — |
| Dante, Petrarca, Boccaccio | 2-14, 2-22 | 3-22 | — |
| Cesare, Cicerone, Augusto, Traiano, Adriano, Marco Aurelio, Costantino, Agostino, Teodorico, Giustiniano, Alboino, Matilde, Federico II, Marco Polo, Vesalio, Paracelso, Bruno, Foscolo, Galileo, Bruno | Anno II (facoltative e obbligatorie) | 3-3, 3-19, 3-22 | quasi tutte entrano come **facoltative**, per non saturare |

**Vincolo.** Nessun personaggio può essere **obbligatorio** in due anni. Chi è stato obbligatorio nell'Anno I o II può tornare solo come facoltativa o come voce di secondo livello. *(Questo vale anche per Leonardo, che va verificato: 2-8 e 3-13 sono entrambi obbligatori. Vedi §13, Q7.)*

### 6.5 Il catalogo dei personaggi

*(materiale di Pietro, §§I–XXVI, in forma di catalogo)*

Codici `Q` proposti: la serie continua da quella dell'Anno II (Q01…Q92) con **Q101…Q130** per i 30 obbligatori, e un blocco separato per il catalogo esteso. Colonne: codice · nome · periodo · luogo/pin o porta · strato · la domanda · attendibilità · destinazione.

**Destinazione**: `3-n` = obbligatorio alla tappa 3-n; `f` = facoltativo; `atl` = atlante; `a4-a5` = candidato agli anni 4-5, da verificare con la cornice narrativa (`curricolo.md` §4, che prevede Ercole II per l'anno 4 e Alfonso II per l'anno 5, entrambi nel XVI secolo).

**Il materiale di Pietro contiene 120 voci numerate** e almeno **cinque duplicati interni**, che vanno risolti nella catalogazione:

| Voce nel materiale | Problema |
|---|---|
| 14 Enrico VIII e 47 Enrico VIII d'Inghilterra | lo stesso personaggio, due numeri; la 47 è un richiamo alla 44 |
| 39 Leonardo e 63 Leonardo | idem |
| 40 Machiavelli e 118 Machiavelli (jolly) | idem |
| 41 Erasmo e 119 Erasmo (jolly) | idem |
| 53 Galileo e 56 Galileo (Sez. IX) | il materiale lo dichiara esplicitamente: **è voluto**, perché il secondo passaggio è nel Seicento e serve a un livello diverso. Va conservato come **ritorno**, non come duplicato |
| 93 Charles de Gaulle e 103 Charles de Gaulle | il materiale lo dichiara: **è voluto**, due funzioni diverse (la Francia libera / l'Europa dei federalisti). Ritorno |
| 106 Michail Gorbačëv e 111 Mikhail Gorbachev | **errore di battitura** e duplicato: una sola voce |
| 1 Ötzi e il già presente 2-1 | il materiale dell'Anno III non lo sa: è già una tappa dell'Anno II. Diventa facoltativa (§6.4) |

Criteri di scheda: identici a quelli dell'Anno II, più un campo obbligatorio in questo anno — **`funzione`** (testimone, contraddittore, fonte, falsa certezza, ponte geografico, ponte temporale: §6.3) e **`arrivo`** (come la risorsa entra a corte: §3.3).

---

## 7. Il duca è la guida, non il protagonista

*(aggiunta — realizza la decisione 2 del §0.1 e sostituisce, per l'Anno III, la regola di `AGENTS.md` §3 «Anno 1»)*

### 7.1 Che cosa cambia

| | Anno I e II | Anno III |
|---|---|---|
| Chi gioca | il duca (Borso, Ercole) | **il visitatore della corte** |
| Chi parla | i personaggi delle tappe | i personaggi delle risorsa, che parlano di sé e della propria epoca |
| Il duca | è il personaggio giocante | **è la guida**: commenta, seleziona, non viaggia |
| Il luogo percorribile | la città, tappa per tappa | il Palazzo Ducale e il Castello, sempre gli stessi |
| Che cosa porta alla tappa successiva | un rimando a piedi | **una risorsa che arriva** |

### 7.2 Il dialogo di Alfonso

*(regola fissa, valida per tutte le 30 tappe)*

1. **All'arrivo della risorsa**, Alfonso dice una frase sola, e la dice **sapendo ciò che può sapere**. Non commenta il contenuto: commenta **l'arrivo**. «Un_volume._ Arriva da Parigi.» / «Una statua. Da Norimberga, e hanno impiegato due anni a trasportarla.»
2. **Alfonso non spiega mai la tappa.** Non dice «quello che vedrai è importante», non anticipa la domanda. È un limite del personaggio, non una scelta di scrittura: lui non sa di cosa si tratta.
3. **Alfonso non viaggia mai**, in nessuna delle 30 tappe, nemmeno per un'immagine.
4. **Alla fine dell'anno**, alla tappa 3-30, Alfonso parla **da solo**, per la prima volta, e dice che cosa non ha capito. È l'unica tappa in cui parla a lungo.

### 7.3 Perché questa scelta funziona, e che cosa costa

**Funziona** perché rende l'anno 3 coerente con la sua tesi di fondo (il continente visto da un punto, non dall'alto), e perché realizza il limite temporale come **meccanica di gioco** invece che come avvertenza: il giocatore non è un osservatore esterno onnisciente, incontra un uomo che ha dei limiti, e quei limiti sono storici.

**Costa** due cose, e vanno dette.

1. **Il parallelismo con gli anni precedenti è spezzato.** Negli anni 1 e 2 il personaggio giocante attraversava la città e la penisola, e la sua posizione fisica era il segnale del progresso. Qui la posizione non cambia mai: tutto avviene nella stessa stanza. È una perdita di concretezza che va compensata con la forza dell'arrivo delle risorse.
2. **I livelli dell'anno 3 sono tecnici, e la corte è un pretesto.** La bottega del livello resta (è la stessa di `esercizi.md`), ma il contesto è meno coinvolto che negli anni precedenti. Da mettere in conto: è il prezzo di una scelta che dà molto di più sul piano storico.

*(proposta di mitigazione)* Se l'anno 3 risultasse piatto nella giocabilità, un'alternativa fedele al materiale di Pietro è che **il visitatore sia un inviato** che percorre l'Europa e porta materiale ad Alfonso, il quale continua a non viaggiare. Si recupera il movimento senza toccare la regola centrale, e si rende visibile la mediazione (che è già il meccanismo delle porte).

---

## 8. Le domande del terzo anno

*(materiale di Pietro, §XXX e §XXVII)*

| # | Domanda | Il gioco non chiede | Il gioco chiede | Dove |
|---|---|---|---|---|
| 1 | Che cosa sappiamo davvero di un'Europa che non esiste? | «Carlo V era X» | «Quali persone avevano interesse a raccontare i fatti in quel modo?» | 3-3, 3-9 |
| 2 | Un testo antichissimo ha un solo autore? | «Omero scrisse l'Iliade» | «Chi ha scritto questo, e quando?» | 3-1, 3-9 |
| 3 | L'autorità è una prova? | «Aristotele aveva ragione» | «Se lo ha detto lui, è vero?» | 3-4, 3-5 |
| 4 | Una conquista produce anche uno scambio? | «Alessandro conquistò l'Asia» | «Che cosa resta, che cosa si perde, chi ricorda?» | 3-9 |
| 5 | Quando finisce un impero? | «Nel 476 finì Roma» | «Finì l'imperatore, o le strutture?» | 3-7 |
| 6 | Un piccolo Stato può sopravvivere fra imperi? | «Alfonso I fu scomunicato» | «Come si sceglie un alleato quando gli alleati sono imperi?» | 3-10, 3-3 |
| 7 | Una controversia religiosa diventa rivoluzione politica? | «Lutero iniziò la Riforma» | «Perché una questione teologica è diventata continentale?» | 3-19, 3-26 |
| 8 | Il mondo arabo e ottomano è dentro l'Europa o fuori? | «L'Europa è un continente» | «Chi stabilisce i confini, e quando?» | 3-18, 3-27 |
| 9 | Un nuovo modello che spiega meglio l'osservazione cambia la conoscenza? | «Galileo aveva ragione» | «Chi decide fra un'autorità antica e un'osservazione?» | 3-2, 3-24 |
| 10 | Un'opera artistica è una fonte storica? | «Shakespeare scrisse Hamlet» | «Che cosa ci dice un testo finto sulla società che lo compra?» | 3-18, 3-30 |
| 11 | Una persona è una fonte su di sé? | «Machiavelli era cinico» | «Quante versioni di un testo sono vere?» | 3-14 |
| 12 | Chi è escluso quando si dichiarano diritti universali? | «La Rivoluzione francese fu liberale» | «E le donne?» | 3-27, 3-4, 3-5 |
| 13 | Il progresso e la disuguaglianza convivono? | «Il XIX secolo fu il secolo del progresso» | «Chi ne beneficiò?» | 3-28 |
| 14 | Come si passa dalla libertà alla dittatura? | «Hitler salì al potere» | «Quali istituzioni hanno smesso di funzionare?» | 3-28 |
| 15 | Si può conservare la memoria di un evento che ha cancellato le sue fonti? | «La Shoah» | «Chi racconta, e con quale documento?» | 3-28 (facoltativa), v. §13 Q1 |
| 16 | La storia è inevitabile? | «L'Europa si è unita» | «Perché Stati che si combattevano hanno iniziato a cooperare?» | 3-30 |

**Nota.** Le domande 14 e 15 riguardano il Novecento e **non hanno tappa obbligatoria**: la 3-28 (Turing, 1936) vi sfiora il periodo ma non affronta né il fascismo né la Shoah. Restano aperte, e sono la ragione principale per cui la questione §13 Q1 va decisa subito.

---

## 9. Il ritorno, e la differenza temporale

*(materiale di Pietro, §§35–37)*

Alla fine del terzo anno il giocatore ha visto arrivare sulla tavola di Alfonso trenta risorse da tutta l'Europa, e ha capito che **Ferrara non è mai stata soltanto Ferrara**: è stata dentro un impero, dentro una Lega, dentro una Riforma, dentro una tregua fra due religioni, dentro un sistema di alleanze che non esisteva quando lui è nato.

**Nel gioco:** la tappa 3-30 riporta il giocatore al gabinetto di Isabella d'Este, e da lì si apre la **carta intera** (§3.6). La domanda finale non è «che cos'è l'Europa» ma:

> **questa carta mostra che gli strati esistono davvero, o mostra che noi li ordiniamo così?**

**La differenza temporale** (materiale di Pietro, §36) è la regola portante dell'anno, ed è scritta nel motore, non nella prefazione:

- il **giocatore** sa che arriveranno Lutero, la Riforma, la rivoluzione industriale, le guerre mondiali, il Muro, l'Unione Europea;
- **Alfonso non sa quasi niente** di tutto questo, e lo dice: alla tappa 3-28, quando una risorsa arriva da Manchester e dice «1936», Alfonso non ha niente da dire, e il gioco scrive: «Alfonso I è morto da oltre quattro secoli. Questa risorsa non è per lui.»;
- i **personaggi delle risorse** non sanno niente gli uni degli altri, e questo vale anche quando sono vissuti nello stesso secolo: Tucidide non sa di Solone, Solone non sa di Pericle.

Ne segue la regola operativa che chiude l'anno, e che è la stessa dell'Anno II resa meccanica:

> **nessuno vive il passato sapendo quale sarà il futuro. Il giocatore lo sa, e questa è la ragione per cui può giocarci.**

---

## 10. La conclusione del terzo anno

L'anno deve chiudere con una domanda, non con una data. Il materiale di Pietro la formula così, e va tenuta:

> **come può un continente diventare ciò che è attraverso milioni di decisioni prese da persone che non conoscevano il futuro?**

In gioco, la domanda si pone in tre modi concreti:

1. **all'inizio**, quando il giocatore scende nella carta e vede che gli strati si somigliano: la continuità **sembra** naturale, e non lo è;
2. **alla fine di ogni tappa**, quando la risorsa va via e resta solo la scheda: di tutto quello che era arrivato, **è rimasto un documento**, e il documento è di qualcuno;
3. **alla fine dell'anno**, quando la carta intera si apre e sotto la Ferrara di oggi compaiono dodici strati: nessuno di quegli strati era previsto da chi ci viveva.

La conclusione didattica, che è la stessa dei tre anni insieme:

| Quando vedo… | mi chiedo… |
|---|---|
| un confine | chi lo ha tracciato, e per che cosa? |
| un personaggio | da quali fonti lo conosco, e chi le ha scritte? |
| una versione della storia | chi ha interesse a raccontarla così? |
| un'istituzione | chi ne beneficiava, e chi ne pagava? |
| una «grandezza» | chi c'era, e non è nominato? |
| il presente | quali decisioni lo hanno reso possibile, e quali alternative c'erano? |

E la domanda finale, che apre il quarto anno:

> **se l'Europa è nata da accordi fra Stati che si odiavano, che cosa stiamo costruendo adesso, e con quali patti?**

---

## 11. Temi sensibili e regole di contenuto

*(coerente con `anno1-ferrara.md` §8 e `anno2-penisola.md` §11)*

Il terzo anno introduce i temi più pesanti dell'intero progetto, e le regole devono essere scritte **prima** delle schede, non durante.

| Tema | Dove | Regola proposta |
|---|---|---|
| **Espulsione degli ebrei (1510)** | 3-10 | §5, «3.10 bis». Documento breve con data e fonte; confronto a tre voci; nessun ritratto, nessuna scena di violenza; collegamento esplicito con la tappa 1-6 al MEIS; aggancio trasversale uno e non valutato |
| **Persecuzioni religiose** | 3-19, 3-26 | Lutero e Caxton si presentano **senza aggettivi**: il gioco dice che cosa fecero e che cosa successe, e la domanda è sulla **meccanica** (una controversia diventa continentale perché la stampa rende la circolazione economicamente conveniente), non sul giudizio |
| **Ebraismo e antisemitismo** | 3-10, e in ogni anno | la presenza ebraica è **continua** in tutti e tre gli anni e non si introduce come caso eccezionale; l'Anno 1 la ha già incontrata al MEIS |
| **Schiavitù e colonialismo** | 3-9, 3-18, 3-30 | il gioco **non nomina** la tratta atlantica né l'imperialismo, perché nessun personaggio obbligatorio dell'anno la porta al centro. Va deciso con Pietro: o si aggiunge una scheda di atlante esplicita, o si dichiara il limite. **Vedi §13, Q2** |
| **Razzismo e «barbarie»** | 3-4, 3-5, 3-7 | ogni popolo «conquistato» ha almeno una voce propria; la demolizione di Roma (3-7) è raccontata dall'interno, non come «la barbarie dei Goti» |
| **Assolutismo** | 3-3, 3-8 | il potere è **descritto, non giudicato**; la domanda è sempre sul meccanismo |
| **Diritti, genere, cittadinanza** | 3-4, 3-5, 3-27 | la spina dorsale del percorso: tre epoche, la stessa domanda su chi è dentro e chi è fuori. È il tema più importante dell'anno e non va trattato come un'aggiunta |
| **Persone viventi** | catalogo | von der Leyen, Merkel, Macron: **solo emblemi**, e valutare se entrano nel percorso (§13, Q4) |
| **Shoah, fascismi, guerre mondiali** | fuori dal percorso obbligatorio | **fuori portata** dell'anno 3, come nell'Anno II. È il vuoto di §0.2 e la ragione della questione Q1 |

---

## 12. Anacronismi e dati da verificare

*(come in `anno1-ferrara.md` §11: si segnala, non si corregge)*

| # | Voce | Che cosa va verificato |
|---|---|---|
| **V1** | **Q110 / 3.10 — il decreto del 1510** | **verifica prioritaria.** Data esatta del decreto; testo; se e come riguarda Ferrara e Modena; nome e destino delle famiglie colpite; il rapporto con lo scomunica di Giulio II (1510). **Non usare il fatto in nessun contesto didattico finché non è verificato.** |
| **V2** | **Q117 — Josquin alla corte di Alfonso** | Josquin fu a Ferrara **sotto Ercole I**, non sotto Alfonso I: verificare le date e decidere se la tappa va riscritta (§5, Q117) |
| **V3** | Q110 — Alfonso I | date delle perdite territoriali (Modena 1510, Reggio 1512), la riconquista (1526) e la sentenza imperiale (1530); il ruolo delle artiglierie nella battaglia di Ravenna (1512); i tre scomunicati |
| **V4** | Q101 — Eratostene | il metodo delle unità e delle non-unità nell'*Octad*: che cosa dice esattamente e in quale forma |
| **V5** | Q104 — Solone | le quattro classi per reddito: quanto la tradizione è affidabile; il peso degli schiavi nel calcolo |
| **V6** | Q106 — Platone | la «linea divisa»: che cosa dice esattamente il testo, e che cosa dice la versione scolastica |
| **V7** | Q107 — Belisario | la posizione di Procopio: che cosa dice nelle *Storie* e che cosa nei *Vandali e Goti*, e perché la differenza conta |
| **V8** | Q108 — Federico II | la datazione del Castel del Monte e il suo rapporto con l'imperatore; il periodo effettivo della stesura del *De arte venandi* |
| **V9** | Q109 — Alessandro Magno | le fonti (Arriana, Diodoro, Curzio Rufo) e i loro interessi; la data della divisione effettiva |
| **V10** | Q111 — Ariosto | la struttura a talismani del *Furioso*; le tre edizioni (1516, 1521, 1532) e che cosa è cambiato fra l'una e l'altra |
| **V11** | Q112 / Q121 — Alcuino, Carlo Magno | l'attribuzione del *De litteris collationibus* a Carlo Magno (probabilmente di Alcuino o di un suo allievo): è una verifica che cambia la scheda |
| **V12** | Q113 — Leonardo | l'esempio preciso per l'aggancio 3-13: **nessuna frase generica**, va citata la pagina del quaderno |
| **V13** | Q114 — Machiavelli | le due versioni del *Principe`, i dedicatari, e che cosa è stato rimosso dal finale |
| **V14** | Q115 / Q120 — Camerino d'alabastro | data di costruzione (1520-1529?), opere attribuite, e la dispersione del 1598: dove sono oggi, e con quale provenienza |
| **V15** | Q116 — Gutenberg | la causa di Strasburgo riguarda la fusione dei caratteri, **non** la stampa: la distinzione va fatta nella scheda, perché è l'errore più comune su Gutenberg |
| **V16** | Q122 — Boccaccio | la struttura del *Decameron*: i temi, le giornate, i narratori, e la questione dell'ordine dei manoscritti |
| **V17** | Q123 — Tommaso d'Aquino | la struttura della *Summa` e le sigle: come si cita un articolo, e come si rimanda all'interno del testo |
| **V18** | Q124 — Dürer | il *Underweysung der Messung* e la data; le figure delle *Proportionen* sono costruzioni o misure? |
| **V19** | Q125 — Manuzio | l'*italiciana` e la sua datazione; il suo catalogo di edizioni (1528) come primo elenco sistematico |
| **V20** | Q126 — Caxton | le date, il soggiorno a Bruges e Colonia, e i formati della sua prima edizione inglese |
| **V21** | Q129 — i privilegi | il *privilegium` veneziano del 1469, l'*imprimatur` di Leone X (1517), e la distanza fra questi atti e il diritto d'autore moderno |
| **V22** | Q130 — Isabella d'Este | il gabinetto di Mantova, il criterio alfabetico e le sedi per materia: verificare l'ordine con cui il nucleo fu redatto |
| **V23** | In generale | ogni **porta** (§3.4) è una scelta narrativa: verificare che la risorsa potesse davvero arrivare a Ferrara in quel modo, in quegli anni, con quei tempi |
| **V24** | In generale | i **3-30, 3-13, 3-2, 3-24** mettono in scena opere che oggi sono in musei di Stati diversi: i diritti e le immagini restano quelli indicati in `FONTI-E-LICENZE.md`, e per le opere ancora in Francia (Bellini, Dosso) il gioco **non mostra l'opera**: mostra il disegno preparatorio o l'incisione antica, che sono in pubblico dominio. **Verificare voce per voce prima di realizzare le tappe** |

---

## 13. Questioni aperte

*(da decidere con Pietro; le decisioni dell'01/10/2026 sono al §0.1)*

1. **Il vuoto del Novecento.** È la prima questione, e condiziona tutto il resto. Le opzioni:
   - **(a) un sesto anno**, o gli anni 3-5 sul Novecento, con Alfonso I/Ercole II/Alfonso II come cornice e non come percorso. È la scelta che rispetta il materiale di Pietro e abbandona la cornice dei cinque duchi, che è il titolo del gioco;
   - **(b) il Novecento come «atlante»**, consultabile dal docente ma non giocabile, come proposto per l'Anno II (§13 Q6 di quel documento);
   - **(c) accettare il vuoto** e rimandare. Il gioco coprirebbe 3000 anni fino al 1936, che è già molto, ma le domande 14 e 15 di §8 resterebbero senza risposta;
   - **(d) riequilibrare i 30 livelli**, inserendo 3-4 personaggi novecentisti al posto di tre di quelli attuali (candidati: Curie, Freud, Levi, Arendt, per i livelli 3-24, 3-26, 3-28, 3-30, che sono i più adatti). È economica e ha un costo: toglie tappe al Cinquecento, che è il terreno più forte dell'anno.
   La mia proposta è **(d) insieme a (b)**: si recupera il Novecento dove è possibile senza snaturare l'anno, e il resto va in atlante. Ma **(a)** è la più fedele al tuo materiale, ed è una decisione tua.
2. **La tratta e l'imperialismo.** Nessun personaggio obbligatorio porta l'Europa fuori dall'Europa. Il catalogo di Pietro cita Colombo e Vespucci, che sono nell'Anno II e non nell'anno 3. Va deciso se aggiungere una scheda di atlante esplicita sul colonialismo (che è un buco tematico reale), o se dichiarare il limite.
3. **Il bilancio degli agganci.** 21 forti, 9 medi. Migliore dell'Anno II, e per una ragione che vale la pena verificare con te: il tema dell'anno è la trasmissione della conoscenza, e il suo terreno naturale è il XV–XVI secolo. Se qualche aggancio forte ti sembra **troppo** forte (è il rischio opposto a quello dell'Anno II), segnalo: 3-1 (Eratostene), 3-8 (Castel del Monte) e 3-24 (Dürer) sono i tre più discussi.
4. **Persone viventi.** von der Leyen, Merkel, Macron: solo emblemi, e la decisione su Q1 li rende o no giocabili.
5. **Le aggiunte.** Cinque personaggi aggiunti perché i livelli li richiedevano e il catalogo non li aveva: **Josquin** (3-17), **Bellini** (3-20), **Dürer** (3-24), **Manuzio** (3-25), **Caxton** (3-26), **Turing** (3-28). Sono tutti europei, tutti con una ragione didattica precisa e tutti verificabili. Se preferisci, tre di loro si possono sostituire con personaggi già nel tuo catalogo, al costo di indebolire l'aggancio.
6. **I codici `Q`.** Proposta: la serie continua da Q01 (Anno II) con **Q101…Q130** per l'anno 3. Alternativa: `P3-01…P3-30`, o `R01…R30`. Va confermata una volta sola, perché da qui in poi la numerazione è nel repository.
7. **I ritorni.** Leonardo è **obbligatorio in due anni** (2-8 e 3-13), contro la regola che ho proposto in §6.4. Va deciso: si tiene il ritorno forte (è il caso più bello del percorso, perché la stessa persona è «il linguaggio delle figure» e poi «la scomposizione del metodo»), oppure una delle due tappe diventa facoltativa.
8. **La corte come unico luogo percorribile.** È il prezzo della decisione 2. Se l'anno 3 risultasse piatto, l'alternativa è il **visitatore-inviato** (§7.3).
9. **La regola di `AGENTS.md`.** Va aggiornata: dal terzo anno il duca non è il personaggio giocante ma la guida. La modifica va scritta in `AGENTS.md` §3, non solo in questo documento.
10. **Le fonti del materiale.** Come per l'Anno II, il catalogo cita fonti ottime (Treccani, Britannica, ODNB, archivi) ma non le ha ancora consultate sistematicamente. Serve un abbozzo di bibliografia per i 30 obbligatori prima della stesura delle schede in `dati/`.

---

## 14. Cosa c'è da fare

1. **Decidere Q1** (il vuoto del Novecento). Tutto il resto dipende da questa scelta.
2. **Verificare V1** (il decreto del 1510) prima di qualunque uso didattico. È la verifica più importante del documento.
3. **Verifiche storiche** (§12): V2 (Josquin), V10 (Ariosto), V14 (Camerino), V15 (Gutenberg), V22 (Isabella d'Este) sono le altre cinque delicate.
4. **Revisione degli aggregati forti**: 3-1, 3-8, 3-9, 3-11, 3-20, 3-24 con Pietro.
5. **Aggiornare `AGENTS.md`** §3 con la nuova regola del duca-guida (§7).
6. **Generare i dati** in `dati/`:
   - `videogioco-5-duchi-anno3-europa.json`: 30 tappe con livello, argomento, strato, pin o porta, tipo di arrivo, funzione del personaggio, forza, rimando, facoltativi;
   - `videogioco-5-duchi-anno3-personaggi.json`: le 30 schede obbligatorie più il catalogo esteso (§6.5);
   - `videogioco-5-duchi-anno3-porte.json`: le 5 porte (§3.4);
   - `videogioco-5-duchi-anno3-ritorni.json`: la tabella dei ritorni (§6.4), che serve al motore per non ripetere le schede.
7. **Carta geografica d'Europa**: open data, con attribuzione. Servono coste, fiumi e confini storici **e** moderni (le due cose non coincidono, ed è un problema tecnico: su quale mappa si mette Atene nel V secolo? — vedi §13, e va aggiunto come Q11).
8. **Prima tappa completa** (3-1, Eratostene ad Alessandria), sul modello di `videogioco-5-duchi-tappa-1-01.md`, con l'arrivo della risorsa in corte e il commento di Alfonso.
9. **Aggiornare `README.md`**: tabella dei documenti e «da fare».

---

## 15. Registro modifiche

- **v0.2 (01/10/2026)**: correzione di un errore di calcolo. In §9 la frase di Alfonso alla tappa 3-28 diceva che era «morto da due anni»: Alfonso I muore nel 1534 e la risorsa arriva dal 1936, dunque da oltre quattro secoli. Corretto, e uniformato con lo stesso meccanismo usato nel documento dell'Anno IV («è morto da oltre tre secoli» per Ercole II, 1559).
- **v0.1 (01/10/2026)**: prima stesione. Formalizza il materiale storico-pedagogico del terzo anno di Pietro in un documento coerente con `anno1-ferrara.md`, `anno1-mappa.md` e `anno2-penisola.md`:
  - principio zero esteso (neanche l'Europa esiste ancora) e sei principi dell'anno;
  - la corte di Ferrara come unico luogo percorribile, con i sette modi di arrivo delle risorse e le cinque porte;
  - la carta d'Europa a strati, con 15 strati di cui due senza tappe obbligatorie, e il vincolo di non-monotonia esplicitato;
  - Alfonso come guida, con la regola del dialogo e il conteggio di ciò che la scelta costa;
  - le 30 tappe agganciate ai 30 livelli dello schema, con 21 agganci forti e 9 medi;
  - le trenta domande in forma piena;
  - 30 schede di personaggio obbligatorio (29 nomi proprii e 1 collettivo), con i tre livelli di fonte, la funzione e il modo di arrivo;
  - il decreto del 1510 nella tappa 3-10, con le regole di conduzione e il collegamento alla tappa 1-6;
  - il criterio, i tre livelli di fonte, le sei funzioni del personaggio e la tabella dei ritorni;
  - le sedici domande dell'anno e il modo in cui il gioco le pone;
  - temi sensibili, con regole scritte prima delle schede;
  - ventiquattro verifiche storiche, di cui una (V1) prioritaria;
  - dieci questioni aperte, di cui la prima sul vuoto del Novecento.
