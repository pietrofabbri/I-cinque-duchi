---
titolo: Videogioco "I cinque duchi" — Anno V, il mondo contemporaneo: il cantiere dell'Addizione Erculea e la carta della stima
versione: 0.1
data: 2026-10-01
autore: Pietro Fabbri (con Claude)
fonte del materiale: due documenti di progettazione storico-pedagogica di Pietro ("ANNO V — IL MONDO CONTEMPORANEO, primo percorso" e "ANNO V — IL MONDO CONTEMPORANEO, secondo percorso"), 01/10/2026
dati: videogioco-5-duchi-anno5-mondo.json e videogioco-5-duchi-anno5-personaggi.json e videogioco-5-duchi-anno5-stime.json (da generare, v0.1)
documenti collegati: videogioco-5-duchi-schema-livelli.md (v1.1, livelli 5-1…5-30), videogioco-5-duchi-curricolo.md (v0.1, §4 cornice narrativa e §5.5 elenco dei livelli dell'anno 5), videogioco-5-duchi-luoghi.md (v0.1, la regola dei luoghi, che questo documento applica ai propri pin), videogioco-5-duchi-anno4-mondo.md (v0.2, da cui questo documento continua le convenzioni), videogioco-5-duchi-anno3-europa.md (v0.2), videogioco-5-duchi-anno2-penisola.md (v0.1), videogioco-5-duchi-anno1-ferrara.md (v0.3), videogioco-5-duchi-anno1-mappa.md (v0.8), videogioco-5-duchi-esercizi.md (v0.1), videogioco-5-duchi-quadro-trasversale.md (v0.1), videogioco-5-duchi-gioco.md (v0.4), videogioco-5-duchi-meccaniche.md (v0.3)
---
# Anno V — Il mondo contemporaneo

## 0. Che cosa contiene questo documento

Il documento **formalizza** il materiale storico-pedagogico di Pietro per il quinto anno e lo aggancia ai 30 livelli già definiti in `videogioco-5-duchi-schema-livelli.md` (v1.1, § «Anno 5 — Alfonso II»).

Come per gli anni II, III e IV:

- il **materiale** di Pietro è conservato e riordinato secondo le convenzioni del progetto;
- le **aggiunte** sono ciò che è stato introdotto per rendere il materiale giocabile, e sono segnalate voce per voce;
- le **proposte** sono da approvare e raccolte in §13;
- i **fatti storici non certi** sono indicati con `note_verifica` e raccolti in §12.

### 0.1 I due percorsi, ancora con due funzioni diverse

Come nell'anno precedente, il materiale arriva in **due documenti separati**:

- **«Il mondo contemporaneo — Primo percorso»** (119 voci) è il **percorso delle persone**: dalla nuova idea di umanità del 1945 fino al presente e a ciò che viene dopo, con l'attenzione alla **scienza** e alle trasformazioni tecniche;
- **«Il mondo contemporaneo — Secondo percorso»** (64 voci) è il **percorso dei temi**: non cronologico nel senso delle persone, ma **progressivo nel tempo** (dal dopoguerra alla pandemia, all'intelligenza artificiale, al futuro).

| | Primo percorso | Secondo percorso |
|---|---|---|
| Che cosa dà al gioco | **la voce**: chi arriva sulla tavola di progetto e parla | **l'asse di confronto**: il problema su cui quella voce si appoggia |
| Che cosa diventa | i **30 personaggi obbligatori** e le schede (§5) | il **confronto** di ogni tappa (§4) |

*(aggiunta — differenza rispetto all'anno 4)* Nell'Anno IV i due percorsi erano complementari ma **di uguale natura**: il primo era cronologio, il secondo comparativo per problemi, e bastava incrociarli. Nell'Anno V i due percorsi sono invece **due metà dello stesso viaggio**: il primo racconta le persone, il secondo i temi, e sono entrambi **in ordine di tempo**. Questo cambia una cosa importante e utile: **l'anno 5 è il primo anno in cui i 30 livelli possono essere letti quasi in ordine cronologico senza che il gioco perda niente**, e vale la pena sfruttarlo (§0.3 b).

### 0.2 Le decisioni che il materiale implica

1. **Il protagonista è il tempo che deve ancora venire.** Il materiale è netto: «il quinto anno non deve insegnare il futuro», e chiude su «nessuno conosceva il futuro». Questo diventa il principio zero dell'anno (§1) e il suo tono.
2. **Il quinto duca è Alfonso II d'Este, e il luogo è un cantiere.** Alfonso II è duca dal 1559 al 1597 e nel 1592 fa iniziare l'**Addizione Erculea**, l'ampliamento della città. Il livello 5-20 chiede di **progettare la rete di un edificio**, e il livello 5-10 di **validare un modello**: un duca che progetta una città con dei numeri è, senza cercarlo, la figura giusta per un anno che finisce con l'intelligenza artificiale. Il luogo percorribile è dunque **la tavola di progetto dell'ingegnere ducale** (§3.3).
3. **La città non fu finita.** L'Addizione Erculea fu interrotta e completata solo in parte. È il simbolo dell'anno, e il gioco deve dirlo: **il percorso si chiude con un progetto incompiuto**, non con una conclusione.
4. **Chi garantisce la verità?** È la domanda con cui il materiale chiude (§116), ed è la domanda del gioco: i livelli 5-26…5-28 sono imparare dai dati, reti neurali, IA generativa, bias e AI Act.

### 0.3 Quattro conseguenze da mettere in conto subito

**(a) Una collisione di persona, risolta.** Il livello 5-3 si chiama «il metodo di Newton» e il livello 5-21 «Dijkstra». Newton era il personaggio obbligatorio della tappa 4-7: la regola dei ritorni che ho proposto nell'Anno III lo vieta in due anni. **Decisione di Pietro (01/10/2026): Newton è obbligatorio solo al 5-3, e al 4-7 entra Leibniz come aggiunta.** `anno4-mondo.md` è stato aggiornato a v0.2 di conseguenza, con la scheda, la domanda e la voce nella tabella delle tappe.

**(b) L'anno è «solo» degli ultimi ottant'anni, e questo è un problema e una risorsa.** Fra il 1945 e oggi ci sono ottant'anni e trenta tappe: quasi tre anni per tappa. Negli anni precedenti la colonna copriva cinquemila anni e il gioco poteva prendersi la libertà di non essere cronologico; qui **non può**, perché non c'è abbastanza tempo da spostare. Due conseguenze:

- i livelli 5-1…5-11 (metodi numerici e simulazione) **non hanno personaggi del dopoguerra** se non Fermi, e per uno di essi si è dovuto usare un personaggio dell'Ottocento (John Snow, 5-9). È una scelta, non una disattenzione, e va dichiarata ai ragazzi: «i metodi che il Novecento usa sono più vecchi delle persone che li usano»;
- la **svolta dei livelli** (5-12 automi, 5-13 macchina di Turing, 5-14 fermata, 5-15 P e NP, 5-16…5-25 reti, 5-26…5-29 IA) segue l'ordine **storico reale** dello sviluppo dell'informatica, che è quasi cronologico. È un vantaggio raro: il percorso può essere seguito anche senza conoscere la programmazione.

**(c) Sei strati vuoti in fondo, ed è la cosa più importante del documento.** Dei sedici strati, **sei non hanno tappe** (§3.2): sono quelli dal 2026 in poi. Il gioco li mostra **vuoti sulla colonna**, e alla tappa 5-30 apre la settima porta, `PT-FUT`, che è una stanza vuota. La lezione del materiale diventa una cosa che si vede: *l'ultimo sesto del gioco è uno spazio bianco, e nessuno lo riempirà per noi*.

**(d) Le persone viventi entrano, ma solo come emblema.** Decisione di Pietro (01/10/2026): **sì, le persone viventi possono essere personaggi obbligatori**, purché senza ritratto e con una scheda dichiarata «in formazione». Nel quinto anno sono sei (5-11 Fei-Fei Li, 5-15 Yann LeCun, 5-26 Joy Buolamwini, 5-27 Geoffrey Hinton, 5-28 Timnit Gebru, 5-29 Demis Hassabis) e vengono marcate con il campo **`stato: in formazione`** e con la regola che nessuna di loro può essere data per corretta (§5, §11). Le altre ventiquattro sono defunte, e molte sono defunte da poco.

---

## 1. Il principio zero, esteso: non è il mondo a non esistere, è il tempo

Per quattro anni il gioco ha tolto un nome alla volta. Nel secondo anno: **l'Italia non esiste ancora**. Nel terzo: **non esiste l'Europa**. Nel quarto: **non esiste il mondo**. Sono tre lezioni diverse, ma la loro meccanica è la stessa: quando il giocatore arriva, il nome non c'è, e deve imparare a vivere senza.

Il quinto anno toglie qualcos'altro, e la differenza è importante: **non toglie un nome, toglie un tempo**.

Nel 1559, quando Alfonso II succede a Ercole II, il futuro non è una incognita: **il futuro non è un oggetto che esiste e che non si vede**. Non c'è un «domani» che qualcuno potrebbe, in teoria, leggere. Non ci sono previsioni affidabili, non c'è nessun che sappia. Anche il presente è in parte ignoto: nessuno intuisce la rivoluzione industriale, nessuno prevede le guerre mondiali, nessuno immagina il calcolatore.

Ne segue la conseguenza didattica, che è la più difficile di tutti e cinque gli anni perché toglie al gioco la sua risorsa preferita, il «te lo spiego perché è già successo»:

> **nessuna delle trenta persone di questo documento sapeva che cosa sarebbe successo dopo.** Non Einstein, non Turing, non Berners-Lee, non Margaret Hamilton. E il gioco, che sa, non può dirlo: può soltanto mostrare che avevano le stesse informazioni di noi e ne hanno fatto un uso migliore o peggiore.

E ne segue la seconda, che è la regola operativa dell'anno:

> **le idee viaggiano, ma arrivano trasformate.** Una scoperta di oggi è un metodo di ieri; un metodo di ieri è un'idea di trecent'anni prima. Il gioco lo mostra nei rimandi: quando arriva il transistor, l'ha inventato un gruppo; quando arriva il Web, l'hanno costruito trenta persone poco conosciute; quando arriva l'intelligenza artificiale, l'ha costruita usando idee di Church, Shannon, Turing e von Neumann, tutti morti prima che il termine esistesse.

---

## 2. I principi del quinto anno

1. **Il protagonista non è un luogo, è un tempo.** La città, la penisola, il continente, il pianeta: il quinto anno non allarga lo sguardo, lo **proietta in avanti**. Il luogo percorribile è una stanza sola (§3.3).
2. **Ogni tappa è un numero, e il numero è sbagliato.** I livelli dell'anno sono metodi di approssimazione: bisezione, Newton, Monte Carlo, integrazione, simulazione, minimi quadrati. Il gioco **non nasconde l'errore e non premia la precisione**: mostra sempre l'errore accanto al valore, e la domanda non è «quanto hai indovinato» ma **«da quanto ti sei sbagliato, e da che cosa dipende»**.
3. **Sei strati vuoti in fondo.** L'ultimo sesto del gioco non è un livello in più: è uno spazio bianco che il giocatore vede e in cui nessuno scrive (§0.3 c).
4. **Non è una cronologia, ma quasi.** Per la prima volta l'ordine dei livelli segue da vicino l'ordine storico (§0.3 b). Va detto ai ragazzi, perché in questo anno la vicinenza di due tappe **significa qualcosa**: 5-24 (crittografia a chiave pubblica) viene prima di 5-25 (capacità del canale) e di 5-26 (imparare dai dati), e quel «prima» è vero.
5. **Le persone non sono eroi, e alcune sono ancora vive.** Il materiale stesso avverte (§11): non tutte le persone influenti vanno presentate come autorità (§11).
6. **La competenza finale** non è «sapere che cosa succederà», ma **sapere che cosa non si sa e come ci si ragiona sopra**: distinguere il fatto dallinterpretazione, la previsione dalla certezza, il dato dal modello (§8, domande 13–16).

---

## 3. La mappa: il cantiere dell'Addizione Erculea

*(aggiunta, 01/10/2026)*

### 3.1 Due assi

- **asse orizzontale, il luogo**: la **pianta della città**. Nell'anno 1 era la città entro le mura; qui è la città **come progetto**: la Ferrara di allora e i nuovi quartieri disegnati a tavolino. Due geometrie sovrapposte, una esistente e una che non esiste ancora;
- **asse verticale, lo strato**: accanto alla pianta, la **colonna stratigrafica** con sedici strati.

*(aggiunta — cosa cambia rispetto agli anni precedenti)* La colonna di quest'anno **non è una colonna geologica**. Negli anni II–IV la colonna copriva migliaia di anni e il gioco la usava per mostrare che la vicinanza è illusoria; qui la colonna copre ottant'anni e la vicinanza **è reale**, ma è reale in un altro modo: due strati adiacenti sono due cose che sono successe una dopo l'altra, e nessuna delle due sapeva dell'altra.

### 3.2 Gli strati

| Strato | Denominazione | Periodo indicativo | Tappe obbligatorie |
|---|---|---|---|
| `S80` | Il terreno: le idee che arrivano da lontano | fino al 1700 | 5-3, 5-6, 5-20 |
| `S81` | Il terreno: gli strumenti e le prime misure | 1700 – 1899 | 5-9 |
| `S82` | La svolta: cambia il metodo della conoscenza | 1900 – 1939 | 5-2, 5-13, 5-14 |
| `S83` | Guerra, dopoguerra, il transistor, i primi calcolatori | 1940 – 1959 | 5-1, 5-5, 5-8, 5-12, 5-21, 5-25 |
| `S84` | Reti, sistemi, il calcolatore che diventa personale | 1960 – 1974 | 5-17, 5-19, 5-24 |
| `S85` | L'informatica personale e la rivelazione dell'Universo | 1975 – 1984 | 5-4 |
| `S86` | Il Web, i dati, il pianeta come sistema | 1985 – 1994 | 5-7, 5-16, 5-18, 5-23 |
| `S87` | Il primo decennio del secolo | 1995 – 2004 | 5-10 |
| `S88` | Dati, piattaforme, moneta | 2005 – 2014 | 5-11, 5-22 |
| `S89` | Intelligenza artificiale e responsabilità | 2015 – 2025 | 5-15, 5-26, 5-27, 5-28, 5-29, 5-30 |
| `S90` | 2026 – 2030 | — | — |
| `S91` | 2031 – 2035 | — | — |
| `S92` | 2036 – 2040 | — | — |
| `S93` | 2041 – 2045 | — | — |
| `S94` | 2046 – 2050 | — | — |
| `S95` | 2051 e oltre | — | — |

**I sei strati vuoti** sono la parte più importante della mappa. Non sono un ritardo: sono il progetto. Il materiale chiede che il quinto anno **non insegni il futuro** e che termini con una domanda; i sei strati vuoti sono la versione meccanica della stessa idea. Il gioco li disegna sulla colonna come sei fasce bianche, e alla tappa 5-30 il giocatore ci va e li guarda.

*(proposta)* Il gioco può anche **scrivere** in quelle fasce, e ogni volta che lo fa registra **la data e la firma**: alla fine della partita lo schermo mostra tutte le previsioni fatte dal giocatore, con l'anno in cui le ha fatte. È il modo più onesto di chiudere un gioco che parla di previsioni.

**Vincoli sugli strati.** Come negli anni precedenti, **nessun vincolo di monotonia**: 5-3 è in `S80`, 5-9 in `S81`, 5-2 in `S82`, 5-20 in `S80`, 5-30 in `S89`. Le regole sono le stesse: ogni tappa dichiara il proprio strato; la nebbia dipende dal **pin visitato**, non dallo strato.

### 3.3 Il cantiere: perché questo risolve il problema della scala

*(aggiunta, e punto centrale dell'anno)*

Il materiale del quinto anno non si può giocare: passa dagli accordi sui diritti umani del 1948 all'algoritmo di bisezione, dal vaccino all'HTTPS. Nessuna mappa è percorribile, e nessuna stanza contiene tutto.

La soluzione è **un cantiere**. Il giocatore **non viaggia e non esce dalla città**: sta nella sala da progetto degli ingegneri ducali, davanti alla pianta dell'ampliamento che Alfonso II fa iniziare nel 1592. Ogni tappa è **un calcolo che arriva sulla tavola**, e il gioco ne annuncia l'origine. Le prime undici tappe sono calcoli (quanto è grande, quanto costa, quanto cresce, quanto sbaglio); le successive sono cose che si costruiscono (una macchina, una rete, un modello che impara da dati).

La meccanica fa quattro cose insieme:

1. **risolve la scala** — non serve una mappa percorribile, serve un tavolo su cui arrivano cose;
2. **è storicamente esatta** — nel Cinquecento una città si progetta con numeri, rilievi e calcoli, e la città che ne nacque **fu finita solo in parte**;
3. **è il livello 5-30 riscritto in forma drammatica** — la prova finale è «un progetto di simulazione scientifica completo», e il progetto del ducale è un progetto di simulazione che nessuno finì;
4. **chiude il gioco nel modo giusto** — il giocatore passa l'anno a fare stime e a costruire cose, e alla fine gli resta **una città incompiuta e sei anni senza nome**, che è esattamente ciò che il materiale chiede di lasciare.

*(proposta)* Alfonso II commenta i calcoli con la sola esperienza di un uomo del Cinquecento: sa contare, sa stimare un raccolto, non sa che cosa sia un errore standard. Quando arriva un numero che non può nemmeno leggere («una probabilità», «un intervallo di confidenza»), il gioco **glielo fa dire male**, e lo dice.

### 3.4 I sette modi di arrivo e le sette porte

| Porta | Dove | Che cosa arriva | Tappe |
|---|---|---|---|
| `PT-LAB` | il banco del laboratorio | una misura ripetibile, una tabella di misure | 5-1, 5-4, 5-6, 5-25, 5-26, 5-27 |
| `PT-PAP` | l'archivio delle pubblicazioni | un articolo, un rapporto, una tesi | 5-2, 5-3, 5-5, 5-11, 5-14, 5-15, 5-28, 5-29, 5-30 |
| `PT-MAT` | l'officina delle macchine | una macchina, uno schema, una procedura | 5-13, 5-18, 5-21, 5-22 |
| `PT-CAB` | il tavolo dei cavi e delle chiavi | un cavo, un indirizzo, un certificato | 5-16, 5-17, 5-19, 5-23, 5-24 |
| `PT-CIT` | il rilievo del quartiere | una pianta, una mappa di una malattia, una statistica cittadina | 5-9, 5-10, 5-20 |
| `PT-URB` | il cannocchiale e il territorio | un'osservazione del cielo, un rilievo, un calcolo di rotta | 5-7, 5-8, 5-12 |
| `PT-FUT` | la stanza del futuro | niente. è vuota, e si apre solo alla fine | 5-30 |

*(proposta)* Le sette porte hanno una proprietà che le altre non avevano: **`PT-FUT` non porta niente**. Tutte le altre porte del gioco sono state, fino ad ora, una metafora della mediazione; questa è l'assenza. Il gioco deve aprire la porta e non mostrarci niente, e dire la frase che chiude l'anno.

### 3.5 Alfonso II e il progetto

Alfonso II **non esce dalla sala da progetto** in tutto l'anno. Il meccanico è semplice e ripetuto trenta volte. All'inizio di ogni tappa **Alfonso commenta il calcolo che è arrivato**, e lo fa **solo con ciò che sa fare**:

- se il calcolo è del suo tempo (un raccolto, un costo, un raggio, un numero di abitanti), Alfonso lo commenta, e spesso ha torto;
- se il calcolo arriva da un'epoca che non ha vissuto, il gioco **lo dice**: «Questo non è arrivato. Non arriverà. Non lo vedrai.» E la tappa si gioca lo stesso.

La differenza rispetto agli anni precedenti è che qui Alfonso **non è solo un uomo con un limite**: è **il committente**. È lui che ordina il ampliamento della città, e il giocatore non costruisce per lui, costruisce **davanti a lui**, e può sbagliare. Alla tappa 5-30 Alfonso guarda la pianta dei quartieri nuovi e constata che **non saranno finiti**: non perché il progetto sia sbagliato, ma perché lui morirà nel 1597 e nel 1598 il ducato passa al Papato. È la prima volta nel gioco che la guida **non vede la fine della propria storia**, ed è la più importante.

*(aggiunta)* Vanno verificate (V1) la datazione dell'Addizione Erculea, la sua attribuzione agli ingegneri ducali, l'estensione realmente costruita e le ragioni dell'interruzione. Ma anche senza quei dettagli, la tappa 5-20 regge: **un progetto di ampliamento urbano interrotto** è un fatto documentato e il suo insegliamento è esatto.

### 3.6 La fine dell'anno

Alla tappa 5-30 il gioco apre `PT-FUT`. La stanza è vuota. Il giocatore vede le sei fasce bianche sulla colonna e può scrivervi sopra, e ogni scrittura viene registrata con la data.

La domanda a schermo intero, che è la conclusione del quinto anno, è quella del materiale riformulata come domanda sul gioco:

> **queste sei fasce bianche sono vuote perché non succederà niente, o perché nessuno lo sa ancora?**

---

## 4. Le 30 tappe

*(aggiunta — costruita sui 30 livelli dello schema, non il contrario)*

**Colonna «Forza».** Come negli anni precedenti: **forte** il legame è naturale; **medio** funziona ma va costruito nel racconto; **di scena** il luogo fa solo da ambientazione.

**Colonna «Confronto».** Il tema del secondo percorso su cui quella tappa si appoggia (§0.1).

**Colonna «Voce».** `personaggio` = nome proprio. `collettivo` = voce senza nome proprio, con attendibilità `C`. In questo anno sono **2 su 30**, ed è una novità: la prima è **una macchina** (una tappa la cui protagonista non è una persona), la seconda sono **gli ingegneri delle reti**. Entrambe servono alla stessa cosa: togliere la centralità dell'individuo, che è la lezione del materiale.

**Colonna «Stato».** `def` = persona defunta, `in formazione` = persona vivente, scheda con `stato: in formazione`, **solo emblema e nessuna affermazione di correttezza** (decisione di Pietro, 01/10/2026: §0.3 d).

| Livello | Argomento | Strato | Pin | Voce | Porta | Domanda che apre la tappa | Forza | Confronto (percorso II) | Facoltativi (2) |
|---|---|---|---|---|---|---|---|---|---|
| **5-1** | Errori numerici e approssimazione | `S83` | Chicago | **Enrico Fermi** (Q301) | `PT-LAB` | Non sai la risposta: come fai a dare un numero che sia comunque giusto? | forte | §5 La scienza nella competizione mondiale | il problema di Fermi; il fisico teorico (facoltativa) |
| **5-2** | Zeri di funzione: il metodo di bisezione | `S82` | Vienna | **Karl Popper** (Q302) | `PT-PAP` | Come si fa a trovare il punto esatto in cui un'idea si rompe? | forte | §35 La conoscenza non è neutra | Thomas Kuhn (facoltativa); Duhem e Quine (facoltativa) |
| **5-3** | Il metodo di Newton ★ | `S80` | Londra | **Isaac Newton** (Q303) | `PT-PAP` | Partendo da un numero sbagliato, quante volte ci arrivo a quello giusto? | forte | §35 La conoscenza non è neutra | Eulero; Ostrowski (facoltativa) |
| **5-4** | Aree sotto una curva: rettangoli e trapezi | `S85` | Bethesda | **Vera Rubin** (Q306) | `PT-LAB` | Non vedo metà dell'Universo: la calcolo dall'area sotto la curva? | forte | §5 La scienza nella competizione mondiale | Ford e Thonnard; de Sitter (facoltativa) |
| **5-5** | Stimare π con il metodo Monte Carlo | `S83` | Los Alamos | **John von Neumann** (Q304) | `PT-PAP` | Come fa a darmi la costante dell'Universo un tiro casuale? | forte | §5 La scienza nella competizione mondiale | Stanislaw Ulam; Nicholas Metropolis (facoltative) |
| **5-6** | Successioni e ricorrenze: approssimare √2 | `S80` | Babilonia | **Le mani che hanno approssimato √2** (Q305, collettivo `C`) | `PT-LAB` | Un numero con cui non si può fare niente di esatto e con cui si costruiva tutto: che cosa se ne fa? | medio | §61 Il quinto anno non deve insegnare il futuro | il regolo babilonese; i matematici arabi (facoltative) |
| **5-7** | Simulazione a tempo discreto: il moto (Eulero) | `S86` | Londra | **James Lovelock** (Q307) | `PT-URB` | Tutto l'insieme cambia ogni volta e nessuno lo controlla: come lo si tiene in piedi? | forte | §22 La Terra come sistema | Margret Turner; i modelli climatici (collettivo) |
| **5-8** | Oscillatori e attrito | `S83` | Bajkonur | **Sergej Korolëv** (Q308) | `PT-URB` | Un pezzo in orbita si calcola ogni secondo: che cosa succede se sbaglio due volte? | medio | §6 La corsa allo spazio | il programma spaziale (collettivo); Oktyabrskij (facoltativa) |
| **5-9** | Modelli di popolazione e di ecosistema: SIR | `S81` | Londra, Broad Street | **John Snow** (Q309, *aggiunta*) | `PT-CIT` | Un numero di morti in una città: che cosa devo guardare per capire come si diffonde? | forte | §45 La pandemia | William Farr; le statistiche cittadine (facoltative) |
| **5-10** | Prova di corte: validare un modello e confrontarlo con le fonti | `S87` | Stoccolma | **Hans Rosling** (Q310, *aggiunta*) | `PT-CIT` | Gli stessi dati raccontano due storie opposte: ho sbagliato i dati o l'asse? | forte | §42 L'informazione diventa sovrabbondante | Gapminder (collettivo); i revisori dei modelli (facoltativa) |
| **5-11** | Confrontare un modello con i dati: minimi quadrati | `S88` | Princeton | **Fei-Fei Li** (Q311, *in formazione*) | `PT-PAP` | Un computer non ha visto niente: come gli dico che cosa deve guardare? | forte | §36 Chi può produrre conoscenza? | chi ha etichettato ImageNet (collettivo); Jia Deng (facoltativa) |
| **5-12** | Automi a stati finiti | `S83` | Buenos Aires | **Jorge Luis Borges** (Q312) | `PT-URB` | Una biblioteca che contiene tutti i libri possibili, con un numero sbagliato ogni quattro righe | forte | §42 L'informazione diventa sovrabbondante | «Tlön, Uqbar, Orbis Tertius»; i bibliotecari (collettivo) |
| **5-13** | La macchina di Turing | `S82` | Cambridge | **La macchina** (Q313, collettivo `C`) | `PT-MAT` | Un nastro, una testina, due stati: che cosa basta davvero a dire «sto pensando»? | forte | §8 Turing e la domanda sulle macchine | Alan Turing (ritorno dal 3-28); Alonzo Church (ritorno, 5-14) |
| **5-14** | Calcolabilità: il problema della fermata | `S82` | Princeton | **Alonzo Church** (Q314, *aggiunta*) | `PT-PAP` | Esiste un programma che non si ferma mai: come fa uno a saperlo? | forte | §8 Turing e la domanda sulle macchine | Turing; il lambda calculus (facoltativa) |
| **5-15** | Complessità: P e NP in modo intuitivo | `S89` | New York | **Yann LeCun** (Q315, *in formazione*) | `PT-PAP` | Funziona benissimo e non sappiamo spiegare perché: che cosa vuol dire «non sappiamo»? | forte | §35 La conoscenza non è neutra | Stephen Cook; Leslie Valiant (facoltative) |
| **5-16** | Reti: tipi, topologie, commutazione | `S86` | Seattle | **Radia Perlman** (Q316) | `PT-CAB` | Due reti collegate da un cavo: che cosa succede se i messaggi girano in tondo? | forte | §27 Dalla macchina personale alla rete | Bob Kahn; i ponti (collettivo, facoltativa) |
| **5-17** | Modelli a strati: ISO/OSI e TCP/IP | `S84` | Los Angeles | **Vint Cerf** (Q317) | `PT-CAB` | Due reti che parlano lingue diverse: come si fa senza obbligare nessuno a cambiare lingua? | forte | §27 Dalla macchina personale alla rete | Bob Kahn; Louis Pouzin (facoltative) |
| **5-18** | Livello fisico e di collegamento: Ethernet, CRC | `S86` | una sala di riunione, 1983 | **Gli ingegneri delle reti** (Q318, collettivo `C`) | `PT-MAT` | Uno standard di collegamento scritto da ingegneri di sei paesi: chi decide che cosa è corretto? | medio | §27 Dalla macchina personale alla rete | Donald Davies (facoltativa, è al 5-19); Bob Kahn (facoltativa) |
| **5-19** | Indirizzi IP e subnetting | `S84` | Londra | **Donald Davies** (Q319, *aggiunta*) | `PT-CAB` | Un numero che identifica un computer: che cosa succede quando i computer sono miliardi? | forte | §27 Dalla macchina personale alla rete | Peter Kirstein; la Cambridge Ring (facoltative) |
| **5-20** | Prova di corte: progettare la rete di un edificio | `S80` | Ferrara | **Alfonso II d'Este** (Q320) | `PT-CIT` | Voglio un quartiere nuovo: quanti rubano, da dove arriva l'acqua, chi ci passa? | forte | §64 Il futuro non è scritto | Aleotti; i geometri ducali (facoltativa) |
| **5-21** | Instradamento e grafi: Dijkstra | `S83` | Rotterdam | **Edsger Dijkstra** (Q321, *aggiunta*) | `PT-MAT` | Qual è il cammino più corto, se «corto» non è la stessa cosa per tutti? | forte | §58 Il futuro della politica | Bellman; Floyd (facoltative) |
| **5-22** | TCP, UDP e porte | `S88` | un documento del 2008 | **Satoshi Nakamoto** (Q322) | `PT-MAT` | Come si ha ordine e affidabilità senza un'autorità che garantisca niente? | forte | §33 La finanza digitale | Vitalik Buterin; chi ha perso (facoltativa) |
| **5-23** | Servizi di rete: DNS, HTTP, posta | `S86` | Ginevra | **Tim Berners-Lee** (Q323) | `PT-CAB` | Un indirizzo che non appartiene a nessuna persona: che cosa c'è, in fondo, a un numero? | forte | §28 Il problema dell'informazione | il CERN nel 1990; i primi browser (collettivo) |
| **5-24** | Sicurezza in rete: crittografia asimmetrica | `S84` | un ufficio riservato, 1970 | **James Ellis** (Q324, *aggiunta*) | `PT-CAB` | Se lo so solo io e non lo dico a nessuno: la conoscenza esiste? | forte | §35 La conoscenza non è neutra | Diffie e Hellman; Rivest, Shamir, Adleman (facoltative) |
| **5-25** | Prestazioni: banda, latenza, throughput | `S83` | Murray Hill, 1948 | **Claude Shannon** (Q325) | `PT-LAB` | Più banda non basta mai: che cosa la blocca? | forte | §9 Shannon e l'era dell'informazione | Norbert Wiener; von Neumann (ritorno, 5-5) |
| **5-26** | Intelligenza artificiale: imparare dai dati | `S89` | Boston, 2018 | **Joy Buolamwini** (Q326, *in formazione*) | `PT-LAB` | Il riconoscimento funziona: solo che funziona peggio su certe facce. Che cosa correggo? | forte | §50 Ma l'algoritmo non è neutrale | Timnit Gebru (facoltativa, è al 5-28); chi ha costruito i dataset (collettivo) |
| **5-27** | Reti neurali in modo intuitivo ★ | `S89` | Toronto, 2012 | **Geoffrey Hinton** (Q327, *in formazione*) | `PT-LAB` | Una riga di unità collegate a caso produce frasi: com'è che «funziona» vuol dire qualcosa? | forte | §48 L'intelligenza artificiale | Yann LeCun (ritorno, 5-15); Yoshua Bengio (facoltativa) |
| **5-28** | IA generativa: limiti, etica, AI Act ★ | `S89` | Seattle, 2020 | **Timnit Gebru** (Q328, *in formazione*) | `PT-PAP` | Un sistema che funziona e che sbaglia certe persone: di chi è il documento che lo dice? | forte | §51 La macchina che decide | Margaret Mitchell; le schede dei dataset (facoltative) |
| **5-29** | Informatica e metodo scientifico | `S89` | Londra, 2020 | **Demis Hassabis** (Q329, *in formazione*) | `PT-PAP` | Se la macchina propone e noi non capiamo il ragionamento: la scoperta è di chi? | forte | §49 L'AI entra nella scienza | Bruno Latour; AlphaFold (facoltativa) |
| **5-30** | Prova finale: un progetto di simulazione completo | `S89` | Ferrara, sala di progetto | **Daniel Kahneman** (Q330) | `PT-FUT` | Il progetto è pronto e non so se è giusto: lo apro, e a chi affido i dati? | forte | §62 Il quinto anno non deve insegnare il futuro | Amos Tversky; chi scriverà nelle fasce bianche (facoltative) |

**Verifica degli agganci.** Dei 30 agganci: **27 forti, 3 medi, 0 di scena**. I **tre medi** sono 5-6 (la coda delle mani, le ricorrenze), 5-8 (Korolëv, gli oscillatori) e 5-18 (gli ingegneri delle reti, il livello fisico). I quattro **da rivedere con Pietro** perché l'aggancio è forse troppo ovvio: **5-5** (Monte Carlo e von Neumann), **5-12** (Borges e gli automi), **5-25** (Shannon e la capacità del canale) e **5-30** (Kahneman e la prova finale).

*(proposta)* Il bilancio è di nuovo il più alto dei cinque anni, e per la stessa ragione degli anni precedenti: i livelli dell'anno 5 sono **i metodi con cui si produce un numero**, e il materiale di Pietro è la storia di **chi ha prodotto numeri che hanno cambiato il mondo e di chi non ha potuto produrli**. Il percorso è stato costruato da qui, non per forzatura.

### 4.1 Le trenta domande in forma piena

1. **Fermi** — *Non sai la risposta: come fai a dare un numero che sia comunque giusto?* (fonte: le conferenze di fisica nucleare; ricostruzione: gli ordini di grandezza; memoria: l'uomo che ha costruito la bomba)
2. **Popper** — *Come si fa a trovare il punto esatto in cui un'idea si rompe?* (fonte: la *Logik der Forschung*; ricostruzione: il metodo; memoria: l'uomo che ha deciso che la scienza è un metodo e non un corpo di verità)
3. **Newton** — *Partendo da un numero sbagliato, quante volte ci arrivo a quello giusto?* (fonte: i *Principia* e i trattati giovanili; ricostruzione: l'iterazione; memoria: il genio solo, che è l'errore più diffuso)
4. **Rubin** — *Non vedo metà dell'Universo: la calcolo dall'area sotto la curva?* (fonte: gli articoli sulla rotazione delle galassie; ricostruzione: la materia oscura; memoria: la donna che ha visto l'oscurità, che è un titolo e non una spiegazione)
5. **von Neumann** — *Come fa a darmi la costante dell'Universo un tiro casuale?* (fonte: i lavori di Los Alamos; ricostruzione: il metodo; memoria: il cervello della macchina, che ha un'altra storia)
6. **Le mani che hanno approssimato √2** — *Un numero con cui non si può fare niente di esatto: che cosa se ne fa?* (fonte: le tavolette babilonesi; ricostruzione: l'iterazione; memoria: nessuna, ed è la lezione)
7. **Lovelock** — *Tutto l'insieme cambia ogni volta e nessuno lo controlla: come lo si tiene in piede?* (fonte: gli articoli su Gaia; ricostruzione: le simulazioni; memoria: l'ipotesi che è ancora un'ipotesi)
8. **Korolëv** — *Se sbaglio due volte di fila, il razzo cade?* (fonte: i rapporti dei voli; ricostruzione: il calcolo delle orbite; memoria: l'ingegnere che non volò mai)
9. **Snow** — *Un numero di morti in una città: che cosa devo guardare?* (fonte: la distribuzione dei casi; ricostruzione: l'acqua; memoria: l'uomo che chiuse la pompa, che è una parte sola della storia)
10. **Rosling** — *Ho sbagliato i dati o l'asse?* (fonte: le serie storiche; ricostruzione: gli assi ingannevoli; memoria: l'uomo che mostrava che il mondo stava andando meglio)
11. **Fei-Fei Li** — *Un computer non ha visto niente: come gli dico che cosa deve guardare?* (fonte: l'insieme di dati e le sue schede; ricostruzione: la tassonomia; memoria: la fotografia che ha cambiato la computer vision)
12. **Borges** — *Tutti i libri possibili, con un numero sbagliato ogni quattro righe.* (fonte: «La biblioteca di Babel»; ricostruzione: le combinazioni; memoria: il labirinto, che è un'altra cosa)
13. **La macchina** — *Che cosa basta davvero a dire «sto pensando»?* (fonte: la descrizione del 1936; ricostruzione: la simulazione; memoria: nessuna, perché le macchine non hanno memoria)
14. **Church** — *Come fa uno a saperlo?* (fonte: l'articolo sul problema della decisione; ricostruzione: la non calcolabilità; memoria: il tecnico che ha fermato la teoria)
15. **LeCun** — *Funziona e non sappiamo perché: che cosa vuol dire «non sappiamo»?* (fonte: le ricerche sulle reti; ricostruzione: l'assenza di una teoria; memoria: l'uomo che ha detto «non capiamo perché funziona», che è la frase più onesta di tutta l'informatica)
16. **Perlman** — *Che cosa succede se i messaggi girano in tondo?* (fonte: l'algoritmo che spegne i cicli; ricostruzione: il protocollo; memoria: l'inventore che non ha un medaglia con il suo nome)
17. **Cerf** — *Come si fa senza obbligare nessuno a cambiare lingua?* (fonte: le specifiche di TCP; ricostruzione: i livelli; memoria: Internet come mercato, che è un racconto politico)
18. **Gli ingegneri delle reti** — *Chi decide che cosa è corretto?* (fonte: i documenti dello standard; ricostruzione: il comitato; memoria: nessuna, ed è la lezione)
19. **Davies** — *Un numero che identifica un computer: che cosa succede quando sono miliardi?* (fonte: i lavori sui pacchetti; ricostruzione: l'indirizzamento; memoria: il termine giusto, che nessuno conosce)
20. **Alfonso II d'Este** — *Voglio un quartiere nuovo: e se non lo finirò mai?* (fonte: le piante ducali; ricostruzione: l'ampliamento; memoria: il duca elegante, che è tutto ciò che si dice di lui)
21. **Dijkstra** — *Se «corto» non è la stessa cosa per tutti, quale cammino vale?* (fonte: l'articolo del 1959; ricostruzione: i grafi; memoria: l'uomo che ha litigato con l'istruzione)
22. **Nakamoto** — *Come si ha ordine senza un'autorità che garantisca niente?* (fonte: il testo del 2008; ricostruzione: i registri distribuiti; memoria: l'identità ignota, che è il fatto più conosciuto di questa storia)
23. **Berners-Lee** — *Un indirizzo che non è di nessuno: che cosa c'è in fondo?* (fonte: la proposta del 1989; ricostruzione: la rete; memoria: l'inventore che non ha voluto il brevetto)
24. **Ellis** — *Se lo so solo io, la conoscenza esiste?* (fonte: il documento del 1970, declassificato nel 1997; ricostruzione: la chiave pubblica; memoria: nessuna per trent'anni, ed è la lezione)
25. **Shannon** — *Più banda non basta mai: che cosa la blocca?* (fonte: l'articolo del 1948; ricostruzione: il canale rumoroso; memoria: il padre della teoria dell'informazione)
26. **Buolamwini** — *Funziona: solo che funziona peggio su certe facce.* (fonte: lo studio sui riconoscitori facciali; ricostruzione: i dataset sbilanciati; memoria: nessuna, ed è la lezione)
27. **Hinton** — *Com'è che «funziona» vuol dire qualcosa?* (fonte: gli articoli sulle reti profonde; ricostruzione: l'apprendimento; memoria: l'uomo che ha detto che le reti sono come il cervello, che è una metafora e non un fatto)
28. **Gebru** — *Di chi è il documento che dice che il sistema sbaglia?* (fonte: le schede dei dataset; ricostruzione: la documentazione; memoria: nessuna, ed è la lezione)
29. **Hassabis** — *Se la macchina propone, la scoperta è di chi?* (fonte: le pubblicazioni; ricostruzione: la ricerca assistita; memoria: nessuna: la sua storia è ancora in corso)
30. **Kahneman** — *Il progetto è pronto e non so se è giusto: lo apro?* (fonte: le ricerche con Tversky; ricostruzione: i bias sistematici; memoria: l'uomo che ha vinto il premio Nobel e poi ha scritto un libro per dire che non dobbiamo fidarci del nostro cervello)

---

## 5. Le schede dei 30 personaggi obbligatori

*(aggiunta — i codici `Q` continuano la serie degli anni precedenti da **Q301**; v. §13, Q4)*

**Due campi nuovi in quest'anno**, che riguardano l'anno e non la persona:

- **`stato`**: `def` (defunta) o **`in formazione`** (vivente). Per chi è `in formazione` valgono tre regole fisse: **solo emblema, mai ritratto**; **nessuna scheda può dire che ha ragione**; **la sua storia può cambiare** e il gioco lo dichiara al giocatore;
- **`aggiunta`**: la persona non è nel catalogo di Pietro ed è stata introdotta perché il livello la richiede. Le aggiunte di quest'anno sono sei: John Snow, Hans Rosling, Alonzo Church, Donald Davies, Edsger Dijkstra, James Ellis.

Formato di ogni scheda, come negli anni precedenti.

### Q301 · Enrico Fermi
- **Periodo:** 1901–1954. **Luogo:** Roma, Chicago, Los Alamos. **Pin:** Chicago. **Strato:** `S83`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** non sai la risposta: come fai a dare un numero che sia comunque giusto?
- **Fonte:** le lezioni e i problemi di fisica nucleare; **ricostruzione:** il metodo degli ordini di grandezza; **memoria:** l'uomo che ha costruito la bomba.
- **Aggancio 5-1:** il livello chiede l'**errore assoluto e relativo** e l'aritmetica in virgola mobile. Il «problema di Fermi» è il caso in cui **non si sa la risposta e va data comunque**: conta gli ordini di grandezza con quello che hai. Il gioco può chiedere al giocatore la stima *prima* di mostrargli la misura vera, e mostrare che una stima con l'ordine di grandezza gi vale più di una risposta esatta tirata a caso. **Forte.**
- **Motto:** «Non so la risposta, ma so di che grandezza è.» **Emblema:** un foglio con una domanda e una potenza di dieci scritta a mano.

### Q302 · Karl Popper
- **Periodo:** 1902–1994. **Luogo:** Vienna, Londra, Nuova Zelanda. **Pin:** Vienna. **Strato:** `S82`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** come si fa a trovare il punto esatto in cui un'idea si rompe?
- **Fonte:** la *Logik der Forschung* (1934); **ricostruzione:** il criterio di falsificabilità; **memoria:** l'uomo che ha deciso che la scienza è un metodo e non un corpo di verità.
- **Aggancio 5-2:** la **bisezione** cerca lo zero di una funzione dividendo l'intervallo: a metà, di qua o di là? È letteralmente la procedura con cui si cerca il punto in cui un'idea cessa di reggere, e Popper è il primo a chiedere che quella ricerca sia **metodo**, non talento. **Forte.**
- **Motto:** «Un'idea si valida provando a falsificarla: se non si può, è un oggetto di fede.» **Emblema:** un intervallo diviso a metà, con un punto interrogativo a metà.

### Q303 · Isaac Newton
- **Periodo:** 1643–1727. **Luogo:** Londra, Cambridge, Woolsthorpe. **Pin:** Londra. **Strato:** `S80`. **Attendibilità:** `D`. **Stato:** `def`. *(ritorno: era la voce di 4-7, poi spostato a v0.2 di `anno4-mondo.md`)*
- **Domanda:** partendo da un numero sbagliato, quante volte ci arrivo a quello giusto?
- **Fonte:** i *Principia* e i trattati giovanili; **ricostruzione:** l'iterazione; **memoria:** il genio solo, che è l'errore più diffuso.
- **Aggancio 5-3:** il livello è **il suo metodo**, e l'errore che il gioco deve insegnare è proprio quello che l'iterazione non ha: **partendo da una stima sbagliata si può divergere invece di convergere**. Il livello permette al giocatore di scegliere il punto di partenza e di vedere che cosa succede: è il primo caso in cui «la risposta» dipende da una decisione presa prima. **Forte.**
- **Motto:** «Ogni tanto la matematica mi prende per mano.» **Emblema:** una tangente a una curva che taglia un'altra.

### Q304 · John von Neumann
- **Periodo:** 1903–1957. **Luogo:** Budapest, Princeton, Los Alamos. **Pin:** Los Alamos. **Strato:** `S83`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** come fa a darmi la costante dell'Universo un tiro casuale?
- **Fonte:** i lavori di Los Alamos; **ricostruzione:** il metodo di Monte Carlo; **memoria:** il cervello della macchina, che è un'altra storia e molto romanzata.
- **Aggancio 5-5:** il metodo Monte Carlo **stima una quantità esatta usando numeri casuali**, e la sua prima applicazione è stata una mano invisibile che si muove a caso e calcola al tempo stesso l'energia di una bomba. Il livello chiede di stimare π con un lancio di frecce in un quadrato: il giocatore vede che l'errore scende con il numero di lanci, e che **nessun lancio dà la risposta esatta**. **Forte.**
- **Motto:** «Meglio una risposta che si può simulare che una verità che si può solo intuire.» **Emblema:** un quadrato pieno di frecce casuali e un numero che si avvicina.

### Q305 · Le mani che hanno approssimato √2 *(collettivo)*
- **Periodo:** circa 1800 a.C. **Luogo:** Babilonia. **Pin:** Babilonia. **Strato:** `S80`. **Attendibilità:** `C`. **Stato:** anonimo.
- **Domanda:** un numero con cui non si può fare niente di esatto e con cui si costruiva tutto: che cosa se ne fa?
- **Fonte:** le tavolette babilonesi, conservate in musei; **ricostruzione:** il metodo di approssimazione; **memoria:** nessuna, ed è la lezione.
- **Aggancio 5-6:** il livello chiede la **convergenza di una successione per ricorrenza**: si parte da 1, si moltiplica per 1,4, si arrotonda, si ripete, e dopo quattro passi si ottiene 1,414. Le tavolette babilonesi contengono proprio questo, con l'approssimazione scritta in cifre sessaggesimali. **Medio**, perché la connessione con le successioni moderne è analogica, ma il livello può mostrarlo in modo diretto: la stessa iterazione, e il numero arriva a **più cifre esatte** di quante oggi si sappiano scrivere in forma esatta. E sono mani senza nome, che è il tema dell'Anno IV che torna.
- **Motto:** «Non sappiamo chi eravamo. Sappiamo che sapevamo il numero.» **Emblema:** una tavoletta con due colonne di cifre.

### Q306 · Vera Rubin
- **Periodo:** 1928–2016. **Luogo:** Bethesda, Washington. **Pin:** Bethesda. **Strato:** `S85`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** non vedo metà dell'Universo: la calcolo dall'area sotto la curva?
- **Fonte:** gli articoli sulla rotazione delle galassie; **ricostruzione:** la questione della materia oscura; **memoria:** «la donna che ha visto l'oscurità», che è un titolo e non una spiegazione.
- **Aggancio 5-4:** il livello chiede l'**area sotto una curva** con rettangoli e trapezi. La curva che Rubin misura è quella della velocità di rotazione delle stelle in funzione dalla distanza dal centro: sotto quella curva c'è la massa. E la curva è piatta dove non dovrebbe esserlo. Il gioco può mostrare che **integrando la curva si ottiene la massa, e che la massa ottenuta non basta a spiegare il moto**: il numero è giusto e il modello è sbagliato. **Forte.**
- **Motto:** «La curva è piatta. Nessuno me l'aveva detto che non poteva esserlo.» **Emblema:** una galassia vista di lato, con una curva che non scende.

### Q307 · James Lovelock
- **Periodo:** 1911–2022. **Luogo:** Londra, Marlow. **Pin:** Londra. **Strato:** `S86`. **Attendibilità:** `D+I`. **Stato:** `def`.
- **Domanda:** tutto l'insieme cambia ogni volta e nessuno lo controlla: come lo si tiene in piede?
- **Fonte:** gli articoli su Gaia; **ricostruzione:** le simulazioni; **memoria:** l'ipotesi che è ancora un'ipotesi, e va detto.
- **Aggancio 5-7:** il livello chiede la **simulazione a tempo discreto**: lo stato del sistema si calcola passo dopo passo. È il modo in cui si studia oggi l'atmosfera, e la versione più famosa è il «mondo margherita» di Lovelock, in cui il temperatura di una pianeta è governata da un'algebra di organismi. Il gioco mostra che **il passo piccolo non garantisce niente**: la simulazione è buona finché è calibrata, e va calibrata con dati. **Forte.**
- **Motto:** «Il pianeta è un sistema di feedback, e io l'ho potuto solo simulare.» **Emblema:** una margherita stilizzata con le sue "petale" numeriche.

### Q308 · Sergej Korolëv
- **Periodo:** 1907–1966. **Luogo:** Zhytomyr, Mosca, Bajkonur. **Pin:** Bajkonur. **Strato:** `S83`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** se sbaglio due volte di fila, il razzo cade?
- **Fonte:** i rapporti dei voli; **ricostruzione:** il calcolo delle orbite; **memoria:** l'ingegnere che non volò mai e che passò anni in prigionia.
- **Aggancio 5-8:** il livello chiede gli **equilibri oscillatori con attrito** e il problema degli N corpi. Un veicolo in orbita è un sistema che si calcola a passo di secondo, e ogni errore di rotta si somma. Il parallelo con gli oscillatori è che **l'orbita è un moto che si ripete**: se il sistema è smorzato, cade; se è stabile, resta. **Medio**, perché il legame con l'attrito è un'analogia e non una proprietà del programma spaziale, ma il caso è autentico e documentato.
- **Motto:** «L'orbita non è un punto: è un numero che ogni secondo va ricalcolato.» **Emblema:** due orbite quasi sovrapposte e una freccia che indica la deriva.

### Q309 · John Snow *(aggiunta)*
- **Periodo:** 1813–1858. **Luogo:** Londra. **Pin:** Londra, Broad Street. **Strato:** `S81`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** un numero di morti in una città: che cosa devo guardare?
- **Fonte:** la distribuzione dei casi; **ricostruzione:** l'acqua; **memoria:** l'uomo che chiuse la pompa, che è **una parte sola** della storia e non tutta.
- **Aggancio 5-9:** il livello introduce i **modelli epidemici** e dice che un'epidemia è un sistema con tre fasi. Il caso di Snow è il primo caso in cui una mappa di punti cambia la decisione, e mostra che **il dato non è il numeroaggregato ma la sua distribuzione**. Il gioco deve anche dire la parte scomoda: chiudere la pompa aiutò, ma le condizioni igieniche erano il motivo per cui il colera era lì, e la fonte era l'acqua, non la cattiva aria. **Forte.**
- **Motto:** «Non guardo la media: guardo la mappa.» **Emblema:** una mappa di strade con una pompa cerchiata due volte.

### Q310 · Hans Rosling *(aggiunta)*
- **Periodo:** 1948–2017. **Luogo:** Uppsala, Stoccolma. **Pin:** Stoccolma. **Strato:** `S87`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** ho sbagliato i dati o l'asse?
- **Fonte:** le serie storiche; **ricostruzione:** gli assi ingannevoli; **memoria:** l'uomo che mostrava che il mondo stava andando meglio, e che a questo punto quasi nessuno crede.
- **Aggancio 5-10:** il livello è la **validazione dei modelli** e l'**analisi di sensibilità**: che cosa succede al risultato se cambio un parametro? Rosling ha costruito un intero racconto su una cosa che il gioco può far vedere in trenta secondi: **gli stessi dati, due assi diversi, due storie opposte**. E aggiunge la parte difficile: i dati li ha raccolti lui, e il confronto con le fontiequindi una verifica, non un'opinione. **Forte.**
- **Motto:** «Il mondo non è andato peggio. Lo abbiamo guardato peggio.» **Emblema:** due grafici identici con assi verticali diversi.

### Q311 · Fei-Fei Li *(in formazione)*
- **Periodo:** 1976–. **Luogo:** Pechino, Princeton, Stanford. **Pin:** Princeton. **Strato:** `S88`. **Attendibilità:** `D`. **Stato:** **`in formazione`**.
- **Domanda:** un computer non ha visto niente: come gli dico che cosa deve guardare?
- **Fonte:** l'insieme di dati e le sue schede; **ricostruzione:** la tassonomia e l'etichettatura; **memoria:** nessuna: la sua storia è ancora in corso.
- **Aggancio 5-11:** il livello è **imparare dai dati** ed è anche la prima tappa che parla di chi *sceglie* i dati. Un immagine non è un dato finché qualcuno non l'ha chiamata «gatto». La scelta delle etichette, la quantità di esempi per classe e la divisione fra dati di addestramento, di validazione e di test sono **scelte politiche prima che tecniche**, ed è esattamente ciò che il livello chiede. **Forte.** La scheda dichiara `stato: in formazione` e non afferma che la sua visione sia corretta.
- **Motto:** «Un computer non ha mai visto niente: ha solo quello che noi gli abbiamo dato.» **Emblema:** una griglia di immagini con una etichetta scritta a mano.

### Q312 · Jorge Luis Borges
- **Periodo:** 1899–1986. **Luogo:** Buenos Aires, Ginevra. **Pin:** Buenos Aires. **Strato:** `S83`. **Attendibilità:** `D+F`. **Stato:** `def`.
- **Domanda:** tutti i libri possibili, con un numero sbagliato ogni quattro righe.
- **Fonte:** «La biblioteca di Babel» (1941); **ricostruzione:** le combinazioni; **memoria:** il labirinto, che è un'altra cosa.
- **Aggancio 5-12:** il livello chiede gli **automi a stati finiti**, cioè i sistemi che possono essere in un numero finito di stati e che hanno un insieme finito di regole di passaggio. La biblioteca di Babel è esattamente questo: venticinque simboli, tutte le combinazioni possibili, un insieme finito di regole che generano tutto. E i suoi libri **contengono errori aritmetici**: perché il generatore non capiva la matematica che produceva. Il gioco può mostrarlo con un automa a tre stati che genera l'alfabeto, e poi chiedere che cosa significhi che un sistema finito produca un testo infinito. **Forte.**
- **Motto:** «Il libro è scritto, ma nessuno capirà la matematica che lo ha scritto.» **Emblema:** una biblioteca con scaffali identici all'infinito.

### Q313 · La macchina *(collettivo)*
- **Periodo:** dal 1936 a oggi. **Luogo:** ovunque. **Pin:** Cambridge. **Strato:** `S82`. **Attendibilità:** `C`. **Stato:** meccanismo.
- **Domanda:** che cosa basta davvero a dire «sto pensando»?
- **Fonte:** la descrizione del 1936; **ricostruzione:** le simulazioni; **memoria:** nessuna, perché le macchine non hanno memoria e gli esseri umani sì.
- **Aggancio 5-13:** è la prima tappa dell'anno **la cui protagonista non è una persona**, ed è una scelta deliberata. Il livello descrive una macchina con quattro pezzi (nastro, testina, stato, regola) e dimostra che bastano a calcolare tutto ciò che è calcolabile. Il gioco può far costruire al giocatore la macchina a mano e poi mostrare che **quella macchina è capace di simulare qualunque altra macchina**: la cosa più importante del Novecento detta da una figura senza volto. **Forte.**
- **Motto:** «Quattro pezzi. Eppure, con questi quattro pezzi, ci si arriva a tutto.» **Emblema:** un nastro, una testina e una freccia che si sposta.

### Q314 · Alonzo Church *(aggiunta)*
- **Periodo:** 1903–1964. **Luogo:** Princeton. **Pin:** Princeton. **Strato:** `S82`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** esiste un programma che non si ferma mai: come fa uno a saperlo?
- **Fonte:** l'articolo sul problema della decisione (1936); **ricostruzione:** la non calcolabilità; **memoria:** il tecnico che ha fermato una teoria.
- **Aggancio 5-14:** il livello è **il problema della fermata**: esiste un programma che va in loop? La risposta di Church (e, in un altro formalismo, di Turing) è **no: non è possibile saperlo**. È il primo caso nella storia dell'informatica in cui una domanda ben posta ha una risposta che è «non si può rispondere», ed è la ragione per cui oggi esistono gli analizzatori statici e perché non possono essere completi. **Forte.**
- **Motto:** «Ci sono programmi di cui non posso dirvi se finiscono. È un teorema, non una distrazione.» **Emblema:** un nastro che gira e una scritta «non decidibile».

### Q315 · Yann LeCun *(in formazione)*
- **Periodo:** 1960–. **Luogo:** Parigi, New York. **Pin:** New York. **Strato:** `S89`. **Attendibilità:** `D`. **Stato:** **`in formazione`**.
- **Domanda:** funziona benissimo e non sappiamo spiegare perché: che cosa vuol dire «non sappiamo»?
- **Fonte:** le ricerche sulle reti; **ricostruzione:** l'assenza di una teoria; **memoria:** nessuna: la sua storia è ancora in corso.
- **Aggancio 5-15:** il livello distingue i **problemi trattabili** da quelli che non lo sono, e il caso dell'intelligenza artificiale è la versione seria di quella domanda: l'apprendimento funziona su problemi che nessuno sa risolvere in modo controllato, e **non sappiamo perché**. Il gioco deve dire che «non sappiamo ancora» è una frase che va sulla targa, non un fallimento. **Forte.**
- **Motto:** «Funziona. Non sappiamo perché. È importante dirlo, non nasconderlo.» **Emblema:** una rete di nodi con un punto interrogativo al centro.

### Q316 · Radia Perlman
- **Periodo:** 1951–. **Luogo:** Seattle, Digital Equipment Corporation. **Pin:** Seattle. **Strato:** `S86`. **Attendibilità:** `D`. **Stato:** **`in formazione`**.
- **Domanda:** che cosa succede se i messaggi girano in tondo?
- **Fonte:** l'algoritmo che spegne i cicli; **ricostruzione:** il protocollo di instradamento fra ponti; **memoria:** l'inventore che non ha una medaglia con il suo nome.
- **Aggancio 5-16:** il livello chiede **topologie e commutazione**, cioè come i pacchetti attraversano una rete di apparati. Il problema di Perlman è il più classico dell'informatica distribuita: se due ponti si inoltrano l'uno all'altro il messaggio senza fine, la rete si blocca. La soluzione è calcolare **la topologia** e spegnere i cicli, e il gioco può far girare letteralmente i pacchetti e mostrarne il blocc. **Forte.**
- **Motto:** «Due apparati che si parlano si mandano messaggi all'infinito. Bisogna spegnere il ciclo.» **Emblema:** due scatole collegate da un filo che si duplica all'infinito.

### Q317 · Vint Cerf
- **Periodo:** 1943–. **Luogo:** Los Angeles, Londra. **Pin:** Los Angeles. **Strato:** `S84`. **Attendibilità:** `D`. **Stato:** **`in formazione`**.
- **Domanda:** come si fa senza obbligare nessuno a cambiare lingua?
- **Fonte:** le specifiche di TCP; **ricostruzione:** i livelli; **memoria:** Internet come mercato, che è un racconto politico e non una spiegazione.
- **Aggancio 5-17:** il livello è il **modello a strati**: ogni livello fa un lavoro e non sa nulla di quelli sotto. TCP/IP ha funzionato perché non ha obbligato nessuno a sostituire la propria rete: ha definito **un'interfaccia**, e l'interfaccia è ciò che rende compatibili cose diverse. È la stessa lezione del programma cinese del terzo anno e della tassa 4-17, applicata alla rete. **Forte.**
- **Motto:** «Il segreto non è la strada: è che ognuno può parlare la sua lingua e ci si incontra a metà.» **Emblema:** due reti con un incrocio di strati numerati.

### Q318 · Gli ingegneri delle reti *(collettivo)*
- **Periodo:** dagli anni Settanta a oggi. **Luogo:** ovunque. **Pin:** una sala di riunione, 1983. **Strato:** `S86`. **Attendibilità:** `C`. **Stato:** senza nome.
- **Domanda:** uno standard di collegamento scritto da ingegneri di sei paesi: chi decide che cosa è corretto?
- **Fonte:** i documenti dello standard; **ricostruzione:** il comitato; **memoria:** nessuna, ed è la lezione.
- **Aggancio 5-18:** il livello è **Ethernet, CRC, la tabella dello switch**: roba che ha fatto funzionare mezzo mondo e che nessuno conosce, perché è scritta in documenti tecnici e non in storie. È la seconda tappa dell'anno **senza un nome proprio**, ed è la risposta diretta al rischio dell'Anno V, che è l'**elogio dei fondatori**: Internet è stato costruito da centinaia di persone che hanno passato le giornate a discutere di bit di parità. **Medio**, perché il legame con il livello è tecnico e non narrativo, ma la tappa è necessaria.
- **Motto:** «Non c'è un nome sulla porta. Ci sono ottocento pagine di standard.» **Emblema:** una pila di documenti tecnici e un timbro di approvazione.

### Q319 · Donald Davies *(aggiunta)*
- **Periodo:** 1924–2000. **Luogo:** Londra, Slough. **Pin:** Londra. **Strato:** `S84`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** un numero che identifica un computer: che cosa succede quando i computer sono miliardi?
- **Fonte:** i lavori sui pacchetti; **ricostruzione:** l'indirizzamento; **memoria:** il termine giusto, che nessuno conosce.
- **Aggancio 5-19:** il livello chiede **indirizzi, maschere, sottoreti, NAT**. Davies propose di spezzare i messaggi in pezzi («pacchetti») e di instradarli in modo indipendente, e il nome stesso viene da un suo schizzo. Il gioco può mostrare che il pacchetto è **un numero con dentro un altro numero**, cioè la subnetting è la stessa idea portata a un livello dentro. **Forte.**
- **Motto:** «Ho chiamato i pezzi pacchetti, e per trent'anni nessuno ha saputo che ero io.» **Emblema:** un messaggio spezzato in tre buste con l'indirizzo scritto fuori.

### Q320 · Alfonso II d'Este
- **Periodo:** 1533–1597. **Luogo:** Ferrara. **Pin:** Ferrara. **Strato:** `S80`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** voglio un quartiere nuovo: e se non lo finirò mai?
- **Fonte:** le piante ducali; **ricostruzione:** l'ampliamento della città; **memoria:** il duca elegante, che è quasi tutto ciò che in genere si dice di lui.
- **Aggancio 5-20:** il livello chiede di **progettare la rete di un edificio**: componenti, collegamenti, prestazioni. Alfonso II fa iniziare nel 1592 l'ampliamento della città, e il progetto è **incompleto**, perché fu interrotto e fu costruito solo in parte. È la prima e unica volta nel gioco che **il committente vede finire l'anno senza vedere la fine del suo progetto**, ed è il modo in cui il gioco chiude il ciclo dei cinque duchi. **Forte.**
- **Motto:** «Ho ordinato una città. Se non sarà finita, l'avrò almeno ordinata.» **Emblema:** una pianta di quartieri con una parte lasciata in bianco.

### Q321 · Edsger Dijkstra *(aggiunta)*
- **Periodo:** 1930–2002. **Luogo:** Rotterdam, Nuenen, Austin. **Pin:** Rotterdam. **Strato:** `S83`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** qual è il cammino più corto, se «corto» non è la stessa cosa per tutti?
- **Fonte:** l'articolo del 1959; **ricostruzione:** l'algoritmo sui grafi; **memoria:** l'uomo che ha litigato con l'istruzione, che è un'altra battaglia.
- **Aggancio 5-21:** il livello è **il suo algoritmo**, e il caso che il gioco deve insegnare è che «più corto» dipende dal **criterio**: il cammino più corto in numero di salti non è quello più veloce, se i collegamenti hanno latenze diverse. Il livello successivo (5-22) è esattamente questo passaggio, e l'anno intero lo prepara. **Forte.**
- **Motto:** «Se vuoi che ti dicano solo le strade buone, devi accettare che ci dicano anche le cattive.» **Emblema:** un grafo con un solo percorso evidenziato e altri in grigio.

### Q322 · Satoshi Nakamoto
- **Periodo:** attivo dal 2008; identità ignota. **Luogo:** ignoto. **Pin:** un documento del 2008. **Strato:** `S88`. **Attendibilità:** `M` (il nome è uno pseudonimo: non sappiamo chi c'è, e non è una leggenda, è un fatto). **Stato:** senza volto.
- **Domanda:** come si ha ordine e affidabilità senza un'autorità che garantisca niente?
- **Fonte:** il testo del 2008; **ricostruzione:** i registri distribuiti; **memoria:** l'identità ignota, che è il fatto più conosciuto di tutta questa storia.
- **Aggancio 5-22:** il livello chiede **affidabilità, riscontro, ritrasmissione, numeri di sequenza**: come fa un protocollo a fidarsi di un canale che perde e duplica messaggi? La risposta di quel testo è: ogni partecipante tiene una copia del registro e la confronta, e il registro più lungo fa fede. È la costruzione di un protocollo affidabile **senza un'autorità centrale**, ed è un caso da tappa piena, anche se non si sa chi lo ha scritto. **Forte.**
- **Motto:** «Nessuno garantisce niente. Ognuno controlla, e il registro più lungo ha ragione.» **Emblema:** due copie di un registro con una riga che non coincide.

### Q323 · Tim Berners-Lee
- **Periodo:** 1955–. **Luogo:** Londra, Svizzera, Massachusetts. **Pin:** Ginevra. **Strato:** `S86`. **Attendibilità:** `D`. **Stato:** **`in formazione`**.
- **Domanda:** un indirizzo che non appartiene a nessuna persona: che cosa c'è, in fondo, a un numero?
- **Fonte:** la proposta del 1989; **ricostruzione:** la rete; **memoria:** l'inventore che non ha voluto il brevetto.
- **Aggancio 5-23:** il livello chiede **DNS, HTTP, posta**: un nome che diventa un numero, un testo con regole di richiesta e risposta, una casella che esiste solo se qualcuno la controlla. Il Web ha funzionato perché **ogni cosa è un indirizzo**: la stessa domanda («che cos'è un nome?») che il gioco pone al livello 5-19 la pone qui, e la risposta è un'altra. **Forte.**
- **Motto:** «Il Web non è stato progettato per la ricerca: è stato progettato perché si potesse parlare.» **Emblema:** un indirizzo che si risolve in un indirizzo.

### Q324 · James Ellis *(aggiunta)*
- **Periodo:** 1910–1995. **Luogo:** Londra, GCHQ. **Pin:** un ufficio riservato, 1970. **Strato:** `S84`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** se lo so solo io e non lo dico a nessuno, la conoscenza esiste?
- **Fonte:** il documento del 1970, declassificato nel 1997; **ricostruzione:** la chiave pubblica; **memoria:** nessuna per trent'anni, ed è la lezione.
- **Aggancio 5-24:** il livello chiede **crittografia asimmetrica**, firma digitale, certificati. Un servizio segreto britannico aveva già inventato la chiave pubblica nel 1970 e non ne poteva parlare: la scoperta venne pubblicata ventisette anni dopo, e altri la rifecero per strada propria. È il caso in cui **la conoscenza esisteva e non esisteva insieme**, ed è l'antitesi perfetta dell'anno 4 (che finiva con «chi non ha potuto scrivere la sua riga»). **Forte.**
- **Motto:** «L'ho scritto e non l'ho detto. La scoperta era lì, senza che nessuno potesse arrivarci.» **Emblema:** un documento sigillato, aperto ventisette anni dopo.

### Q325 · Claude Shannon
- **Periodo:** 1916–2001. **Luogo:** Michigan, Bell Labs. **Pin:** Murray Hill, 1948. **Strato:** `S83`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** più banda non basta mai: che cosa la blocca?
- **Fonte:** l'articolo del 1948; **ricostruzione:** il canale rumoroso; **memoria:** il padre della teoria dell'informazione.
- **Aggancio 5-25:** il livello chiede **banda, latenza, throughput, jitter, benchmarking**. Shannon ha dimostrato che esiste un **limite massimo** alla quantità di informazione che si può far passare da un canale, e che quel limite dipende dalla banda e dal rumore. Il gioco può far vedere che **raddoppiare la banda non raddoppia il throughput** se il rumore resta, e che il limite non è un difetto della rete: è una legge. **Forte.**
- **Motto:** «Si può solo fare entrare tanto: il resto si perde, e la legge dice quanto.» **Emblema:** un canale con la larghezza indicata e una freccia che si ferma.

### Q326 · Joy Buolamwini *(in formazione)*
- **Periodo:** 1989–. **Luogo:** Boston, Atlanta. **Pin:** Boston, 2018. **Strato:** `S89`. **Attendibilità:** `D`. **Stato:** **`in formazione`**.
- **Domanda:** il riconoscimento funziona: solo che funziona peggio su certe facce. Che cosa correggo?
- **Fonte:** lo studio sui riconoscitori facciali; **ricostruzione:** i dati sbilanciati; **memoria:** nessuna: la sua storia è ancora in corso.
- **Aggancio 5-26:** il livello chiede **accuratezza, precisione, richiamo, matrice di confusione, k vicini, clustering**. Il suo studio è la matrice di confusione diventata una questione di giustizia: gli stessi algoritmi che in un test azzardano riconoscono il viso di un certo gruppo di persone sbagliano **più volte** su un altro, e la ragione è nei dati di addestramento, non nel codice. Il gioco può far costruire al giocatore la matrice e mostrare che **una sola metrica non basta** e che cambiare i dati sposta l'errore. **Forte.**
- **Motto:** «Il sistema funziona. Funziona peggio per alcune persone, e il motivo è dentro i dati.» **Emblema:** due matrici di confusione con numeri diversi nelle stesse caselle.

### Q327 · Geoffrey Hinton *(in formazione)*
- **Periodo:** 1947–. **Luogo:** Scozia, Toronto. **Pin:** Toronto, 2012. **Strato:** `S89`. **Attendibilità:** `D`. **Stato:** **`in formazione`**.
- **Domanda:** una riga di unità collegate a caso produce frasi: com'è che «funziona» vuol dire qualcosa?
- **Fonte:** gli articoli sulle reti profonde; **ricostruzione:** l'apprendimento; **memoria:** l'uomo che ha detto che le reti sono come il cervello, che è una metafora e non un fatto.
- **Aggancio 5-27:** il livello costruisce **un neurone artificiale, le funzioni di attivazione, le reti multistrato**. Il caso di Hinton è quello in cui l'addestramento di una rete profonda ha cambiato l'informatica in quattro anni, e in cui **la cosa più importante da dire ai ragazzi è che nessuno sa perché funziona**. Il gioco può mostrare che la rete non è un programma scritto da qualcuno: è **una struttura di parametri** che il calcolo ha aggiustato a forza, e capire come funziona è un problema aperto. **Forte.**
- **Motto:** «Nessuno ha scritto le regole del riconoscimento. I numeri le hanno trovate.» **Emblema:** una rete di strati con i pesi scritti dentro le linee.

### Q328 · Timnit Gebru *(in formazione)*
- **Periodo:** 1983–. **Luogo:** Etiopia, Stati Uniti. **Pin:** Seattle, 2020. **Strato:** `S89`. **Attendibilità:** `D`. **Stato:** **`in formazione`**.
- **Domanda:** un sistema che funziona e che sbaglia certe persone: di chi è il documento che lo dice?
- **Fonte:** le schede dei dataset; **ricostruzione:** la documentazione; **memoria:** nessuna: la sua storia è ancora in corso.
- **Aggancio 5-28:** il livello è **IA generativa, rischi e benefici, bias algoritmico, responsabilità, AI Act**: è il livello che chiude il ciclo con l'anno 4 (dati, privacy, «chi è escluso?»). Il suo contributo è l'idea che **un insieme di dati dovrebbe avere una scheda, come un farmaco**, che dica da dove viene, chi ha pagato, che cosa contiene e che cosa non contiene. E che l'AI Act, di cui il livello parla, esiste in parte perché quella scheda mancava. **Forte.**
- **Motto:** «Un dato senza documentazione è un materiale che nessuno è obbligato a controllare.» **Emblema:** una scheda tecnica con il riquadro «dati raccolti da» vuoto.

### Q329 · Demis Hassabis *(in formazione)*
- **Periodo:** 1976–. **Luogo:** Londra. **Pin:** Londra, 2020. **Strato:** `S89`. **Attendibilità:** `D`. **Stato:** **`in formazione`**.
- **Domanda:** se la macchina propone e noi non capiamo il ragionamento, la scoperta è di chi?
- **Fonte:** le pubblicazioni; **ricostruzione:** la ricerca assistita; **memoria:** nessuna: la sua storia è ancora in corso.
- **Aggancio 5-29:** il livello chiede che cosa sia, oggi, **il metodo scientifico** quando la macchina è dentro. La domanda che il gioco pone è la più difficile dell'anno e non ha risposta: **se il sistema suggerisce la struttura e noi non sappiamo ricostruire il ragionamento, la comprensione non è completa**. Il gioco non deve scegliere fra le due risposte possibili (è uno strumento, oppure è un investigatore): deve mostrare che il problema è aperto. **Forte.**
- **Motto:** «Ha trovato la struttura. Noi abbiamo capito che cos'è. Sono due cose diverse.» **Emblema:** una struttura tridimensionale e un foglio di calcoli con dentro un puntino interrogativo.

### Q330 · Daniel Kahneman
- **Periodo:** 1934–2024. **Luogo:** Tel Aviv, Princeton, Strasburgo. **Pin:** Ferrara, sala di progetto. **Strato:** `S89`. **Attendibilità:** `D`. **Stato:** `def`.
- **Domanda:** il progetto è pronto e non so se è giusto: lo apro, e a chi affido i dati?
- **Fonte:** le ricerche con Tversky; **ricostruzione:** i bias sistematici; **memoria:** l'uomo che ha vinto il premio Nobel e poi ha scritto un libro per dire che non dobbiamo fidarci del nostro cervello.
- **Aggancio 5-30:** la prova finale è **un progetto di simulazione completo**, e Kahneman è la persona che ha dimostrato che **noi non sappiamo giudicare il nostro stesso progetto**: l'ancoraggio, la disponibilità, la conferma, e soprattutto la tendenza a essere più sicuri di quanto non si sia. Il gioco gli fa l'ultima domanda pratica che gli resta: **se il progetto è finito e tu non sei in grado di sapere se è giusto, che cosa fai?** Non c'è una risposta automatica, ed è il punto. **Forte.**
- **Motto:** «Il progetto è pronto. Io non so se è giusto. È esattamente il momento in cui non devi fidarti del tuo giudizio.» **Emblema:** una planimetria con sopra una riga di numeri e una domanda.

---

## 6. Il criterio: nessun numero senza errore

*(materiale di Pietro, §62 e §64 e §§5–61 del primo percorso, riformulato in regole operative — le regole sono quelle degli anni precedenti e valgono per tutti gli anni)*

### 6.1 La catena

```
PERSONAGGIO → METODO → NUMERO → ERRORE → CONFRONTO → DOMANDA
```

È la catena dell'Anno IV con un anello in più. Nell'Anno IV l'anello che si rompeva era **il documento**: quasi tutte le tappe si rompevano fra la persona e la sua fonte, perché la fonte è di qualcun altro. Nel quinto anno l'anello che si rompe è **il numero**: ogni tappa produce un valore, e il valore è sbagliato.

Regola operativa, nuova e non negoziabile:

> **nessuna tappa del quinto anno può mostrare un numero senza mostrare l'errore accanto.** Non l'errore relativo in un riquadro, non il valore «giusto» a video: **i due numeri insieme, sempre**, e la domanda non è quanto hai indovinato ma **da quanto ti sei sbagliato e da che cosa dipende**.

L'anno 4 ha prodotto un registro di trenta righe in cui una riga restava vuota. L'anno 5 produce una **carta delle stime** in cui ogni riga ha **due** numeri e nessuno dei due è «il» numero (§7).

### 6.2 I tre livelli di fonte, adattati all'anno

I tre livelli dell'Anno IV sono la regola del progetto e valgono anche qui, ma il primo livello cambia natura: in questo anno **non esiste quasi più la fonte d'epoca**, perché il giocatore stesso produce il numero.

| Livello | Che cos'è | Nel quinto anno |
|---|---|---|
| **1. Il calcolo** | il procedimento, il codice, il metodo: ciò che il giocatore può ripetere | **diventa il primo livello**, ed è la cosa buona del quinto anno: il giocatore non riceve un documento da catalogare, **esegue il metodo e può rifarlo** |
| **2. Il risultato e la sua incertezza** | il valore ottenuto, l'errore, l'intervallo | è il cuore della tappa: due numeri e la domanda «da quanto mi sono sbagliato?» |
| **3. La memoria successiva** | come è stato raccontato quel risultato, e chi ci ha guadagnato | **il livello più importante del quinto anno**, perché il dopoguerra è il periodo in cui la fama tecnologica si separa dai fatti: il transistor è di tre persone, Internet di trenta, la «rivoluzione dell'IA» di nessuno in particolare |

> **una fonte non è soltanto qualcosa che conferma una risposta: è qualcosa che deve poter essere interrogato.**

### 6.3 Le funzioni del personaggio nel gioco

Le funzioni del materiale sono diverse da quelle dell'anno 4 (lì erano testimone, contraddittore, fonte, falsa certezza, ponte geografico, ponte temporale). Qui sono **ruoli rispetto al numero**, e sono cinque:

| Funzione | Che cosa fa nel gioco | Esempio nell'anno 5 |
|---|---|---|
| **Chi ha prodotto il numero** | il giocatore impara il suo metodo e ne ripete la logica | Fermi (5-1), von Neumann (5-5), Newton (5-3), Dijkstra (5-21) |
| **Chi ha prodotto il metodo senza produrre il numero** | il caso più importante dell'anno: la persona che ha costruito lo strumento ma non ha fatto il calcolo | Katherine Johnson non è nel percorso; **Perlman** (5-16) scrive il protocollo, **Cerf** (5-17) scrive lo standard, **Davies** (5-19) batte il nome, **Berners-Lee** (5-23) propone il nome |
| **Chi ha mostrato che il numero non basta** | il caso in cui il metodo funziona e la comprensione manca | LeCun (5-15), Buolamwini (5-26), Gebru (5-28) |
| **Il collettivo** | la voce senza nome, con attendibilità `C` | **La macchina** (5-13) e **Gli ingegneri delle reti** (5-18): due tappe su trenta senza nome proprio |
| **Il committente** | colui per cui il progetto esiste, e che non ne vedrà la fine | Alfonso II (5-20), che è anche l'unico personaggio del gioco che **non attraversa** i cinque anni |

*(aggiunta — la quarta funzione è la più nuova e la più importante)* La seconda funzione risolve un problema che il gioco porta dal primo anno e non aveva mai affrontato: **l'informatica è fatta di persone che non compaiono nei libri di storia**. Nell'anno 5 questa cosa è diventata visibile perché i protocolli informatici hanno una data di pubblicazione e un nome, e quello che hanno non è una persona. Il gioco lo dice: «il protocollo di instradamento ha un nome. Chi gli ha dato il nome?».

### 6.4 I ritorni: la stessa persona, un'altra voce

Valgono le tre regole dell'Anno IV (mai la stessa scheda, mai la stessa domanda, mai lo stesso livello; la seconda volta la voce è un'altra; il ritorno va annunciato). Ma **il quinto anno ha un problema opposto al quarto**: il suo materiale non contiene nomi già obbligatori, perché il dopoguerra è troppo recente. Il problema è un altro, ed è più sottile.

**Il problema: la generazione, non le persone.** Fra il 1945 e il 2025 molte figure sono vissute nei paesi che hanno costruito l'informatica. Trenta tappe su trenta, se si prende il materiale così com'è, sono **del Nord globale**: Chicago, Vienna, Los Alamos, Bethesda, New York, Princeton, Cambridge, Seattle, Los Angeles, Londra, Rotterdam, Ginevra, Murray Hill, Toronto, Boston. Ferrara è al centro ma non ha quasi nessuna tappa.

Le regole che propongo:

1. **il principio zero copre anche questo** — nel 1592 il giocatore non sa che il mondo si sposterà, e soprattutto non sa *dove* si sposterà. Un progetto di ampliamento urbano a Ferrara nel 1592 è un progetto perfettamente sensato, e il gioco deve lasciarlo essere tale;
2. **il bilancio geografico va dichiarato al giocatore**, non nascosto: alla 5-20 il gioco mostra la pianta dei quartieri nuovi e dice «quello che state costruendo è una città come tante. Fra quattrocento anni, metà delle cose che contano in informatica saranno state fatte in tre continenti di cui nessuno è questo»;
3. **nessun nome dell'anno 5 può essere un toponimo nazionale italiano**, se non con una ragione storica esplicita. È una conseguenza diretta di Q1 in `luoghi.md` §4.5: se la mappa del quinto anno fosse la geografia del *Furioso*, venticinque dei trenta personaggi perderebbero il loro luogo verificato. Il progetto sceglie la mappa reale, e la geografia reale di questo anno è quella che è.

*(proposta)* Questo vuoto è anche **l'occasione più grande per gli anni futuri** del gioco: se un sesto anno dovesse mai esistere, il suo materiale naturale è la storia dell'informatica fuori dal Nord globale, e l'anno 5 avrà insegnato ai ragazzi a riconoscerne l'assenza. Vale la pena dirlo loro.

### 6.5 Il catalogo dei personaggi

Codici `Q` proposti: la serie continua da quella dell'Anno IV (Q201…Q230) con **Q301…Q330** per i trenta obbligatori.

**Destinazione**: `5-n` = obbligatorio alla tappa 5-n; `f` = facoltativo; `atl` = atlante.

| Codice | Nome | Destinazione | Note |
|---|---|---|---|
| Q301 | Enrico Fermi | 5-1 | |
| Q302 | Karl Popper | 5-2 | nel catalogo di Pietro |
| Q303 | Isaac Newton | 5-3 | **ritorno dal 4-7**, spostato per decisione di Pietro (§0.3 a) |
| Q304 | John von Neumann | 5-5 | |
| Q305 | Le mani che hanno approssimato √2 | 5-6 | **collettivo** `C` |
| Q306 | Vera Rubin | 5-4 | |
| Q307 | James Lovelock | 5-7 | |
| Q308 | Sergej Korolëv | 5-8 | |
| Q309 | John Snow | 5-9 | **aggiunta** |
| Q310 | Hans Rosling | 5-10 | **aggiunta** |
| Q311 | Fei-Fei Li | 5-11 | vivente, `in formazione` |
| Q312 | Jorge Luis Borges | 5-12 | |
| Q313 | La macchina | 5-13 | **collettivo** `C` |
| Q314 | Alonzo Church | 5-14 | **aggiunta** |
| Q315 | Yann LeCun | 5-15 | vivente, `in formazione` |
| Q316 | Radia Perlman | 5-16 | |
| Q317 | Vint Cerf | 5-17 | |
| Q318 | Gli ingegneri delle reti | 5-18 | **collettivo** `C` |
| Q319 | Donald Davies | 5-19 | **aggiunta** |
| Q320 | Alfonso II d'Este | 5-20 | |
| Q321 | Edsger Dijkstra | 5-21 | **aggiunta** |
| Q322 | Satoshi Nakamoto | 5-22 | |
| Q323 | Tim Berners-Lee | 5-23 | **ritorno dall'Atlante dell'Anno IV**, dove era in `atl` |
| Q324 | James Ellis | 5-24 | **aggiunta** |
| Q325 | Claude Shannon | 5-25 | |
| Q326 | Joy Buolamwini | 5-26 | vivente, `in formazione` |
| Q327 | Geoffrey Hinton | 5-27 | vivente, `in formazione` |
| Q328 | Timnit Gebru | 5-28 | vivente, `in formazione` |
| Q329 | Demis Hassabis | 5-29 | vivente, `in formazione` |
| Q330 | Daniel Kahneman | 5-30 | |

**Problemi interni del materiale**, che vanno risolti in catalogazione:

| Voce nel materiale | Problema |
|---|---|
| §1 Eleanor Roosevelt, §2 René Cassin, §3 Hersch Lauterpacht | le tre prime voci del percorso I sono **giuristi e politici**, e i livelli dell'anno 5 sono metodi numerici. Non possono essere tappe obbligatorie: vanno in facoltativa forte e atlante. **Il problema è che il 1945 è l'ingresso del «mondo contemporaneo» e i nostri livelli cominciano dai numeri**: va detto (§13, Q1) |
| §7 Turing, §13 Shannon, §11 Bardeen/Brattain/Shockley, §14 Feynman, §15 Oppenheimer | **tutti nel materiale, nessuno nei livelli.** Sono i nomi che i ragazzi si aspettano. Diventano **facoltative forti** e **atlante**, e il gioco deve dire perché non sono obbligatori: il gioco non è un corso di storia, è un corso di metodi |
| §9 Wiener, §10 Shannon | Shannon è **anche** nel percorso II all'interno di un elenco tematico: due usi, non due voci |
| §16–24 medicine and biology, §25–32 computing | il blocco della biologia (vaccini, antibiotici, DNA, genetica) **non ha livelli corrispondenti**. È il buco più grosso del materiale rispetto allo schema, ed è il primo candidato per i facoltativi (§13, Q2) |
| §33–41 economy and finance | ha un solo livello (5-22, moneta e registri). Il resto è facoltativa |
| §50–52 intelligenza artificiale | quattro voci forti per quattro livelli: è la parte meglio agganciata di tutto il materiale |
| §56–60 futuro, previsioni, globalizzazione | il **secondo percorso** li tratta come temi a sé, ma **nessun livello li copre**: sono i sei strati vuoti, e il gioco li usa come tali (§3.6). Non è una perdita: è il punto |

*(proposta)* Il confronto più utile fra primo e secondo percorso è uno solo, ed è nella tabella delle tappe: la voce «percorso I» dice **chi ha prodotto il numero**, il «percorso II» dice **su quale problema il numero si appoggia**. Le due colonne non coincidono mai e non devono coincidere.

---

## 7. La carta delle stime: il deliverable del quinto anno

*(aggiunta — è la parte che rende il quinto anno diverso dai quattro precedenti)*

### 7.1 Che cosa cambia rispetto al registro dell'Anno IV

Nell'Anno IV il giocatore costruiva un **registro di trenta documenti**, con dieci campi, e alla fine una riga restava vuota. Nel quinto anno l'unità non è il documento, è **la stima**.

| | Anno IV | Anno V |
|---|---|---|
| L'unità di gioco | il **documento** che entra dalla porta | il **calcolo** che il giocatore esegue |
| Che cosa il giocatore raccoglie | trenta schede bibliografiche | trenta righe con **due numeri** ciascuna |
| Il vuoto finale | una riga **vuota** nel registro | sei **fasce bianche** in fondo alla colonna |
| La domanda finale | «questo registro è la storia del mondo, o di chi ha scritto?» | «quelle fasce sono vuote perché non succederà niente, o perché nessuno lo sa ancora?» |

La differenza è che nell'anno 4 il giocatore **non sapeva** che una riga sarebbe restata vuota: la riga vuota è l'assenza di una fonte. Nel quinto anno il giocatore **sa** che le fasce saranno vuote, perché gliele ha mostrate all'inizio. E può scegliere di scriverci.

### 7.2 La carta: i campi, e perché sono quelli

`videogioco-5-duchi-anno5-stime.json`, un record per tappa:

| Campo | Che cosa contiene | Perché c'è |
|---|---|---|
| `livello` | `5-1`…`5-30` | il collegamento con lo schema dei livelli |
| `metodo` | il nome del metodo usato | obbligatorio: una stima senza metodo non è ripetibile |
| `valore` | il numero ottenuto | il primo numero |
| `errore` | l'errore, assoluto o relativo, **esposto** | **il secondo numero**: senza questo il primo numero mente |
| `distanza` | di quanto il risultato si discosta da quello che il giocatore credeva | terzo numero: distingue «ho sbagliato il calcolo» da «avevo l'idea sbagliata» |
| `ipotesi` | le assunzioni del metodo, in una riga | è qui che vive la parte più onesta dell'anno: ogni metodo ha premesse, e nessun metodo le dichiara da solo |
| `incertezza` | da che cosa dipende l'errore: aritmetica, modello, misura, ipotesi | **il campo nuovo dell'anno**: distingue «il computer ha sbagliato» da «il modello è sbagliato» |
| `porta` | da dove è arrivato il calcolo (§3.4) | come nell'anno 4 |
| `attendibilita` | `D`, `I`, `M`, `L`, `F`, `C` | la scala del progetto, invariata |
| `firma` | la data e il nome dello studente che ha scritto la riga | **rende il registro non falsificabile a posteriori** |

*(proposta — il campo `distanza` è il più importante)* Un giocatore che azzecca il valore e sbaglia la previsione ha imparato qualcosa di diverso da uno che sbaglia entrambi. Il campo `distanza` rende visibile la differenza fra **chi sa fare il conto** e **chi sa che cosa il conto significherà**, che è la competenza finale dell'anno (§2, principio 6).

### 7.3 Le sei fasce bianche

I sei strati `S90`–`S95` non sono tappe e non hanno pin. Alla 5-30 il gioco apre `PT-FUT`, che è una stanza vuota, e sulla colonna ci sono le sei fasce.

**Il gioco chiede al giocatore di scrivere una previsione per decade**, dal 2026 al 2050 e oltre, e per ciascuna chiede tre cose:

1. **che cosa succederà** — una frase;
2. **da quale numero dipende** — un numero che oggi si può già misurare o calcolare, che rende quella previsione controllabile;
3. **la data e la firma**.

*(proposta — la parte che rende il finale onesto)* Alla fine della partita il gioco mostra **tutte le previsioni fatte durante l'anno**, non solo quelle delle fasce: quelle del primo giorno e quelle dell'ultimo. Il giocatore vede che la previsione fatta alla 5-1 e quella fatta alla 5-30 sulla stessa questione non coincidono, e il gioco non dice quale delle due è giusta. **Dice solo che ne ha scritte due in un giorno, in due anni di scuola.**

E la consegna finale non è la carta delle stime: è **la carta delle stime più le sei previsioni con la data**. Un file che, fra dieci anni, potrà essere riletto e confrontato. È l'unico modo che il gioco ha di chiudere con una verifica che non può barare.

### 7.4 Perché funziona, e che cosa costa

Funziona perché rende visibile la cosa che il materiale chiede e che nessun libro di testo rende visibile: **un numero è sempre accompagnato da un errore, e l'errore ha una causa che si può nominare**.

Costa tre cose, e vanno dichiarate prima di costruirla:

1. **il giocatore deve accettare di sbagliare davanti**. È la richiesta più alta di tutti e cinque gli anni, e la ragione per cui il progetto sceglie di costruirla;
2. **il file di consegna cresce**: trenta righe con dieci campi più sei previsioni è più di quanto l'anno 1 chiedesse. La meccanica di consegna (`meccaniche.md` v0.3) va verificata con questo formato;
3. **le fasce bianche possono essere riempite male**, cioè con previsioni che sono semplicemente ciò che il giocatore si aspetta che gli altri abbiano detto. Il gioco non può impedirlo e non deve provarci: può solo chiedere il numero da cui dipende, che è la domanda che rende una previsione verificabile invece che una scommessa.

---

## 8. Le sedici domande del quinto anno

*(materiale di Pietro: le domande sono ricavate dal testo, la forma è quella degli anni precedenti — una domanda sola, senza risposta, che il gioco pone e a cui non risponde)*

1. **L'errore che non si vede** — Fermi, 5-1: quando un numero è sbagliato di molto e lo sbaglio è grande, come fa a sembrare affidabile?
2. **Il punto in cui un'idea si rompe** — Popper, 5-2: che cosa cerca davvero il metodo che cerca uno zero?
3. **La velocità dell'errore** — Newton, 5-3: perché partendo da un numero sbagliato l'errore si dimezza, e che cosa lo fa dimezzare?
4. **L'invisibile** — Rubin, 5-4: come si calcola la metà di una cosa che non si vede?
5. **Il caso che produce un numero esatto** — von Neumann, 5-5: come fa a darmi la costante dell'Universo un tiro casuale?
6. **Il numero che non si può scrivere** — le mani di √2, 5-6: un numero che non ha forma esatta con cui si costruiva tutto: che cosa gliene facevano?
7. **L'insieme che non è guidato** — Lovelock, 5-7: se nessuno controlla il sistema, chi decide che sia vivo?
8. **Il calcolo che non torna** — Korolëv, 5-8: un errore di due secondi in un'orbita: che cosa succede davvero?
9. **La correlazione che sembra il contatto** — Snow, 5-9: gli stessi dati raccontano due storie opposte: ho sbagliato i dati o l'asse?
10. **Il grafico che mente** — Rosling, 5-10: gli stessi dati raccontano due storie opposte: ho sbagliato i dati o l'asse?
11. **La macchina che ha bisogno di parole** — Fei-Fei Li, 5-11: un computer non ha visto niente: come gli dico che cosa deve guardare?
12. **La biblioteca sbagliata** — Borges, 5-12: tutti i libri possibili, con un numero sbagliato ogni quattro righe: che cosa manca?
13. **Il dubbio giusto** — Church, 5-14 / LeCun, 5-15: che cosa vuol dire «non sappiamo perché funziona»?
14. **La parte che non ha nome** — gli ingegneri delle reti, 5-18: uno standard scritto da persone di sei paesi: chi decide che cosa è corretto?
15. **Il metodo che funziona e la comprensione che manca** — Gebru, 5-28 / Hassabis, 5-29: se la macchina propone e noi non capiamo il ragionamento, la scoperta è di chi?
16. **La responsabilità** — Kahneman, 5-30: il progetto è pronto e non so se è giusto: a chi affido i dati?

*(nota)* Le domande 9 e 10 sono volutamente identiche nella prima parte: sono la stessa domanda posta a **Snow**, che l'ha risolta, e a **Rosling**, che l'ha resa visibile. È la prima volta che il gioco ripete una domanda, e la ripetizione è il punto.

*(nota)* Le domande 13, 14, 15 e 16 sono **le quattro finali**: sono quelle che il §2, principio 6, indica come la competenza dell'anno, e sono le uniche che il gioco **non può** chiudere. Ogni altra domanda dell'anno ha una risposta che si trova; queste no, ed è per questo che stanno alla fine.

---

## 9. Il ritorno, e la differenza temporale

Alla fine del quinto anno il giocatore ha trenta righe con due numeri ciascuna e sei fasce vuote in fondo alla colonna. Ha visto che **nessuno dei trenta ha saputo che cosa sarebbe successo dopo**, e che il metodo è l'unica cosa che sopravvive al contesto.

**Nel gioco:** la tappa 5-30 riporta il giocatore nella sala di progetto, dove la pianta dei quartieri nuovi è ancora sulla tavola. Alfonso II guarda la pianta e constata che **non sarà finita** (§3.5). La domanda finale non è «che cosa succederà» ma:

> **questo progetto è sbagliato, o è un progetto che non ha avuto tempo?**

**La differenza temporale** è la regola portante dell'anno ed è scritta nel motore:

- il **giocatore** sa che arriveranno le guerre mondiali, il transistor, Internet, la pandemia, l'intelligenza artificiale;
- **Alfonso II non sa niente** di tutto questo, e non solo perché è vissuto prima: è un uomo del Cinquecento che non ha i concetti per pensarlo. Quando arriva un numero che non può nemmeno leggere («una probabilità», «un intervallo di confidenza»), il gioco **glielo fa dire male, e lo dichiara** (§3.5);
- i **personaggi delle trenta tappe** non sanno niente gli uni degli altri, anche quando sono vissuti nello stesso decennio: Shannon non sa di Davies, Davies non sa di Perlman, LeCun non sa di Hinton. Su questo punto l'anno 5 è più severo degli altri perché i protagonisti sono **contemporanei**: due persone che hanno fatto insieme la rivoluzione dell'informatica possono non essersi mai incontrate.

Ne segue la regola operativa che chiude l'anno:

> **nessuno vive il passato sapendo quale sarà il futuro. Il giocatore lo sa, e questa è la ragione per cui può giocarci.**

La differenza rispetto all'Anno IV è che lì la differenza temporale aveva **un corpo materiale** (il futuro era finite in un cassetto dell'archivio, scritto da qualcun altro) e qui ha **una forma geometrica**: le fasce bianche. Nell'anno 4 il vuoto era una riga che manca; nell'anno 5 è uno spazio che il giocatore può riempire e che il gioco registra con la data.

---

## 10. La conclusione del quinto anno

L'anno chiude con una domanda, non con una data. Il materiale di Pietro la formula così, e va tenuta:

> **dato che nessuno conosce il futuro, quali strumenti servono per costruirne uno di cui poter essere responsabili?**

In gioco la domanda si pone in quattro modi concreti:

1. **all'inizio**, quando il giocatore scende nella colonna e vede i sei strati vuoti in fondo: lo spazio bianco **non è un livello in più**, e il gioco non finge che lo sia;
2. **alla fine di ogni tappa**, quando la riga della carta delle stime si scrive con due numeri e non uno: di tutto quello che era arrivato **resta un valore e un errore**;
3. **alla fine dell'anno**, quando le sei previsioni vengono mostrate tutte insieme con le date in cui sono state scritte: il giocatore vede che la sua idea del futuro è cambiata, e non sa se è diventata più giusta o solo più informata;
4. **alla consegna**, quando il file che esce dal gioco porta la data accanto a ogni previsione: dieci anni dopo qualcuno potrà rileggerlo e misurare quanto era sbagliato. È l'unico controllo possibile, ed è sufficiente.

La lezione conclusiva del materiale (§62) è che **il quinto anno non deve insegnare il futuro**, e la sua traduzione meccanica è la parte più seria di tutto il documento: **il gioco non ha l'autorità di dire come sarà**, e questa è la prima volta in cui una cosa che il gioco potrebbe fare facilmente è vietata.

*(proposta)* Ne segue una regola di scrittura per tutte le trenta schede e per le trenta facoltative: **nessuna frase che contenga il futuro come dato.** Non «Internet ha trasformato la società» ma «la rete ha cambiato il modo in cui si cercano le informazioni»; non «l'intelligenza artificiale sostituirà molti lavori» ma «dal 2015 esistono sistemi che scrivono testi, e sanno farlo male in modi che nessuno aveva previsto». La regola è verificabile e si può applicare meccanicamente a una revisione del testo.

---

## 11. Temi sensibili e regole di contenuto

*(coerente con `anno1-ferrara.md` §8, `anno2-penisola.md` §11, `anno3-europa.md` §11 e `anno4-mondo.md` §11)*

Il quinto anno è l'anno del **metodo**: apparentemente è il meno politico dei cinque, ed è invece quello in cui le scelte politiche sono più difficili da vedere, perché sono dentro i numeri. Le regole vanno scritte **prima** delle schede.

| Tema | Dove | Regola proposta |
|---|---|---|
| **Le armi nucleari** | 5-1 (Fermi), 5-5 (von Neumann), 5-8 (Korolëv) | i tre personaggi hanno tutti lavorato per programmi militari. **La scheda deve dirlo nella prima riga**, non in una nota: il metodo numerico del gioco nasce dentro la guerra. Nessuna scena di esplosione; il nucleare entra come **decisione**, non come spettacolo |
| **Chi gode del metodo** | 5-10, 5-20, 5-30 | Rosling mostra che il mondo è andato meglio **perché molti paesi sono cresciuti**, e che i dati senza asse mentono due volte. Il gioco deve dire che una stima ben fatta può essere usata per convincere qualcuno di una cosa falsa. **Nessun gioco numerico che produca una buona impressione dei numeri senza mostrare da dove vengono** |
| **Le persone viventi** | 5-11, 5-15, 5-26, 5-27, 5-28, 5-29 | regole decise il 01/10/2026: **solo emblema, mai ritratto; scheda con `stato: in formazione`; nessuna scheda può affermare che la persona ha ragione; il gioco dichiara al giocatore che la loro storia può cambiare**. Sono sei su trenta: è la proporzione più alta di persone viventi in tutto il progetto, ed è una conseguenza diretta del fatto che l'anno è il presente |
| **La disuguaglianza nell'accesso** | 5-26, 5-27, 5-28 | i tre livelli sull'intelligenza artificiale sono anche i tre livelli in cui il risultato **dipende da chi ha raccolto i dati**. La scheda di Gebru (5-28) è la più importante del capitolo: un insieme di dati dovrebbe avere una scheda come un farmaco. **Nessuna di queste tre tappe può mostrare un risultato senza mostrare chi è stata esclusa dai dati** |
| **Il potere e la sorveglianza** | 5-22 (Nakamoto), 5-24 (Ellis), 5-16 (Perlman) | Ellis è il caso più difficile: il suo lavoro sulla chiave pubblica è stato tenuto segreto per trent'anni e il gioco deve dirlo. Il denaro senza intermediario è presentato come **libertà**, ed è anche un problema di riciclaggio e di controllo: la scheda deve tenere le due cose insieme, senza prediche |
| **La propaganda e la percezione** | 5-10 (Rosling), 5-12 (Borges), 5-30 (Kahneman) | il materiale del primo percorso dedica voci a Zewail, Sontag, McLuhan, Eco, Orwell: sono **facoltative**, non tappe. La regola è che la capacità di manipolare una percezione è un **problema tecnico**, non un difetto morale, e va trattata come tale |
| **La privacy** | 5-22, 5-24 | l'anno 4 ha trattato la protezione dei dati come argomento; qui è un problema di **chiavi**. Nessuna tappa deve suggerire che la crittografia risolva la privacy: la scheda di Ellis deve dire che una chiave pubblica protegge il messaggio **e non chi lo manda** |
| **Il sesso e il genere** | tutto | il materiale cita Amnesty, il genere e le discriminazioni. La regola del progetto: nessun personaggio è presentato come eroe solo perché è riuscito. La scheda di Shockley, che il materiale propone per separare il contributo scientifico dalle idee, è il modello esatto |
| **Le previsioni** | 5-30, e tutto | **la regola più dura del capitolo**: nessuna previsione scritta dal gioco può essere vera. Se il gioco ne scrive una, è una **scommessa con la data**, e il gioco la conserva |

*(nota)* Due temi che il materiale solleva e che **non** entrano nel percorso giocabile, ma vanno nel capitolo di discussione con il docente: il cambiamento climatico (il quarto anno lo ha trattato come buono geografico, il quinto anno lo incontra come **modello numerico**, ed è la cosa giusta da dire) e la questione della memoria e del testimone (che il gioco risolve in modo trasversale, con la carta delle stime firmata e datata).

---

## 12. Anacronismi e dati da verificare

*(come in `anno4-mondo.md` §12: si segnala, non si corregge)*

| # | Voce | Che cosa va verificato |
|---|---|---|
| **V1** | **Q320 — Alfonso II d'Este e l'Addizione Erculea** | **verifica prioritaria.** Le date (1559–1597), l'inizio dei lavori (1592), l'attribuzione agli ingegneri ducali, l'estensione realmente costruita e le ragioni dell'interruzione. **L'aggancio della tappa 5-20 regge anche senza i dettagli** (un ampliamento urbano interrotto è un fatto documentato) ma i numeri che il gioco farà vedere devono essere giusti |
| **V2** | **V1 come premise** | la tesi di V1 regge su un fatto semplice e documentato: **un progetto di ampliamento non fu finito**. Se anche questo risultasse falso, la tappa 5-20 va rifatta |
| **V3** | Q301 — Fermi | il ruolo di Fermi nel programma nucleare e la datazione; la sua attività di «problema di Fermi» come metodo di stima |
| **V4** | Q304 — von Neumann | il ruolo nel calcolo automatico (architettura, EDVAC) e la nascita effettiva del metodo Monte Carlo (con Ulam e Metropolis): **non attribuirgli il metodo da solo** |
| **V5** | Q306 — Vera Rubin | la scoperta della rotazione delle galassie e le altre tappe del suo lavoro (le supernovae, la materia oscura): verificare che cosa si attribuisce a lei e che cosa al gruppo |
| **V6** | Q307 — Lovelock | l'ipotesi Gaia è **un'ipotesi discussa**: la scheda non deve presentarla come teoria accettata, e la sua validità empirica è ancora dibattuta |
| **V7** | Q308 — Korolëv | il progetto del razzo, le date, il fatto che l'ingegnere **non volò mai**: verificare perché (detenzione, prigionia) e che cosa è documentato |
| **V8** | Q309 — John Snow | **la vicenda del Broad Street è la più sovracitata della epidemiologia**: verificare che cosa dice il testo del 1855 e che cosa è leggenda (la «pompa» come unico intervento efficace è una semplificazione). È una verifica che conta, perché il gioco la usa come modello di metodo |
| **V9** | Q310 — Rosling | i dati Gapminder e la loro attendibilità; la forma dei grafici a bolle e il ruolo degli assi |
| **V10** | Q311 — Fei-Fei Li | la costruzione di ImageNet, la quantità e la provenienza delle etichette, e il fatto che **chi le ha fatte era anonimo**: è la scheda che regge l'aggancio e va verificata voce per voce |
| **V11** | Q312 — Borges | «Tlön, Uqbar, Orbis Tertius» è un racconto e non un modello: **la scheda non deve presentarlo come una previsione** |
| **V12** | Q313 — La macchina | la descrizione del 1936 è di Turing, che **non è il personaggio della tappa**: verificare che la tappa non attribuisca la macchina a un collettivo che non esiste |
| **V13** | Q314 — Church | l'articolo del 1936 e la distinzione fra lambda-calcolo e funzioni ricorsive; il problema della fermata è di Turing: **non attribuirlo a Church** |
| **V14** | Q315 — LeCun | le sue posizioni sull'assenza di una teoria delle reti profonde sono citate e cambiano: **verificare la data della fonte** prima di usarle come motto |
| **V15** | Q316 — Perlman | l'algoritmo di instradamento fra ponti (STP, 1985) e il suo ruolo: verificare anche il fatto che **non ha ricevuto premi importanti**, che è la parte che la scheda usa |
| **V16** | Q317 — Cerf | il ruolo di Cerf e Kahn nel TCP, e il fatto che il Web di Berners-Lee si appoggia su Internet e non lo è: la distinzione è importante e va detta |
| **V17** | Q318 — Gli ingegneri delle reti | lo standard Ethernet del 1983 è di **Xerox PARC** e riguarda una sola tecnologia: la scheda non deve farlo sembrare il protocollo di collegamento di oggi |
| **V18** | Q319 — Davies | l'espressione «pacchetto» è di Davies; verificare la datazione del documento e il ruolo di Peter Kirstein nella Cambridge Ring |
| **V19** | Q322 — Nakamoto | l'identità è sconosciuta: **il gioco non deve costruire una biografia**. Verificare anche la data del testo (2008) e che cosa il testo dice e non dice |
| **V20** | Q323 — Berners-Lee | la proposta del 1989 e la decisione sul brevetto; verificare la formulazione esatta, perché «non ha voluto il brevetto» è una frase che si usa spesso e in modo impreciso |
| **V21** | Q324 — James Ellis | **verifica delicata**: il documento del 1970, la sua scoperta «non scoperta» e la declassificazione del 1997. Verificare che cosa è documentato e che cosa è ricostruito; la scheda non deve presentarlo come il primo a inventare la chiave pubblica |
| **V22** | Q325 — Shannon | l'articolo del 1948, il modello del canale rumoroso, e la distinzione fra informazione e significato: **il secondo punto è quello che il materiale usa e va verificato** |
| **V23** | Q326 — Buolamwini | le date della ricerca sul riconoscimento facciale e i dati di Gender Shades: verificare che cosa è stato misurato e come, perché l'aggancio è forte e deve essere esatto |
| **V24** | Q327 — Hinton | il 2012 come data del paper su ImageNet e il ruolo del gruppo di Toronto |
| **V25** | Q328 — Gebru | il caso del modello di linguaggio e la vicenda dei ricercatori di Google: **verificare che cosa è documentato prima e cosa è ricostruzione giornalistica**, e non usare una ricostruzione come fatto |
| **V26** | Q329 — Hassabis | AlphaFold e il premio Nobel del 2024: verificare le date, l'attribuzione del premio (tre persone) e che cosa il sistema fa e non fa |
| **V27** | Q330 — Kahneman | le ricerche con Tversky, il premio Nobel del 2002 e la data della morte (2024). La scheda è di una persona **morta di recente**, e va trattata con la cura che il progetto riserva alle persone morte di recente |
| **V28** | Q305 — le tavolette di √2 | i numeri delle tavolette e le cifre iniziali e finali: verificare perché il gioco **non deve mostrare una sequenza di cifre senza dire quale tavoletta** |
| **V29** | In generale | **le fasce bianche**: le decadi `S90`–`S95` sono scelte di progetto e non dati storici. Il gioco non deve scrivere niente che faccia pensare che il 2030 sia una previsione dello schema dei livelli |
| **V30** | In generale | la **forma dei grafici** del gioco: nessun grafico può essere più suggestivo dei dati che contiene. Verificare la libreria di riferimento prima di generare le schermate |
| **V31** | In generale | **le porte**: come nell'anno 4, ogni porta è una scelta narrativa. Ma qui la cosa è più delicata, perché i calcoli del dopoguerra **non potevano arrivare a Ferrara**: verificare che cosa il gioco dichiara e che cosa lascia intendere |
| **V32** | In generale | **le persone viventi**: nessuna scheda `in formazione` può contenere un'affermazione di correttezza. Verifica meccanica, non storica, ma va fatta prima della consegna |
| **V33** | In generale | i **superlativi**: il materiale contiene espressioni da verificare o da addolcire. Regola del progetto: nessun superlativo senza fonte |

---

## 13. Questioni aperte

*(da decidere con Pietro)*

1. **Il 1945 non è una tappa.** Le prime tre voci del percorso I sono Eleanor Roosevelt, René Cassin e Hersch Lauterpacht, e i livelli dell'anno cominciano dai numeri. Le opzioni: **(a)** tenere i trenta come sono e dichiarare il 1945 come **contesto** del primo percorso, non come tappa (è la mia proposta); **(b)** sostituire una tappa con una voce giuridica; **(c)** aprire il capitolo dell'anno con una **tappa zero** non numerata, che non conta nei trenta e presenta il dopoguerra come cornice. La (c) è la più bella e la più costosa
2. **Il buco della biologia.** Il materiale dedica quindici voci a medicina, vaccini, antibiotici, DNA e genetica, e **nessun livello dell'anno 5 le copre**. È il buco più grosso fra materiale e schema. Le opzioni: tenere il buco e dirlo, o aggiungere facoltative forti che si aprano dai livelli vicini (5-4 e 5-26 sono i più adatti)
3. **I facoltativi «che il gioco non può mettere in tabella».** Turing, Shannon, Wiener, Bardeen, Brattain, Shockley, Feynman, Oppenheimer sono nel materiale e non sono tappe. La mia proposta è che il gioco **dica loro esplicitamente perché** non sono obbligatori, altrimenti sembra un gioco che ha dimenticato i nomi importanti. Va deciso se questo diventa una schermata fissa o una voce di atlante
4. **I codici `Q`.** Proposta: la serie continua con **Q201…Q230** → **Q301…Q330**. Alternativa: `R01…R30`. Va confermata una volta sola, perché da qui in poi la numerazione è nel repository
5. **I quattro agganci da rivedere.** 5-5 (Monte Carlo e von Neumann), 5-12 (Borges e gli automi), 5-25 (Shannon e la capacità del canale) e 5-30 (Kahneman e la prova finale) sono forse **troppo** ovvii: il livello sembra fatto per la persona. Segnalo questi quattro; 5-1 (Fermi) e 5-23 (Berners-Lee) mi sembrano i più solidi
6. **Il bilancio geografico.** Trenta tappe su trenta fuori dal Sud globale (§6.4). Va deciso se il capitolo lo dichiara al giocatore con una schermata o se resta una nota di progetto
7. **La sesta tappa del `PT-FUT`.** La porta che non porta niente è la chiusa dell'anno. Va deciso se il giocatore può **scrivere** nelle fasce o solo guardarle: la prima opzione rende la consegna più forte, la seconda è più facile da valutare
8. **Le previsioni con la data.** Il gioco conserva le previsioni del giocatore e le rilette fra dieci anni? Se sì, serve un formato che sopravviva a un cambio di piattaforma e a una consegna su Classroom. Se no, la previsione resta un esercizio di scrivere, che è comunque utile ma molto meno
9. **Il quinto anno e l'anno 3.** Il terzo anno ha il vuoto del Novecento (§13 Q1 di `anno3-europa.md`). Il quinto anno, di fatto, **riempie** quel vuoto. Va deciso se l'anno 3 debba accennare al fatto che il Novecento arriva, o se resta una domanda aperta fino alla fine del percorso
10. **Le fonti del materiale.** Come per gli anni II, III e IV, il materiale è ricco e non è stato consultato sistematicamente. Serve un abbozzo di bibliografia per i trenta obbligatori prima della stesura delle schede in `dati/`

---

## 14. Cosa c'è da fare

1. **Decidere Q1** (il 1945 non è una tappa) e **Q2** (il buco della biologia). Le altre scelte dipendono da queste
2. **Verifiche storiche** (§12): **V1 e V2** (l'Addizione Erculea e la sua interruzione), **V8** (Broad Street, che è la verifica più sovracitata), **V21** (James Ellis, la più delicata) e **V25** (il caso Gebru, dove la distinzione fra documentato e ricostruito è decisiva) sono le cinque che cambiano una scheda se sbagliate
3. **Revisione degli agganci forti** con Pietro (§13, Q5): 5-5, 5-12, 5-25, 5-30
4. **Applicare la regola dei luoghi** (`luoghi.md` §1 e §5.3) a tutti i pin di questo documento: ogni pin dichiara il suo tipo di legame, e i **luoghi fantastici** — se e quando Q1 di `luoghi.md` verrà decisa nella direzione «atlante e finale» — sono gli unici senza coordinate
5. **Aggiornare `AGENTS.md`** §3 con la sezione «Anno 5» (il luogo è una sala di progetto; l'unità di gioco è il calcolo; il numero è sempre accompagnato dall'errore) e con la sezione trasversale «La regola dei luoghi»
6. **Generare i dati** in `dati/`:
   - `videogioco-5-duchi-anno5-mondo.json`: 30 tappe con livello, argomento, strato, pin, porta, funzione del personaggio, forza, confronto (voce del percorso II), rimando, facoltativi;
   - `videogioco-5-duchi-anno5-personaggi.json`: le trenta schede obbligatorie più il catalogo esteso (§6.5), con i campi `stato` e `aggiunta`;
   - `videogioco-5-duchi-anno5-porte.json`: le sette porte, con `PT-FUT` dichiarata **vuota**;
   - `videogioco-5-duchi-anno5-stime.json`: **i campi della carta delle stime** (§7.2) e le sei fasce bianche, che è il deliverable dell'anno e va progettato per primo
7. **Prima tappa completa** (5-1, Fermi a Chicago), sul modello di `videogioco-5-duchi-tappa-1-01.md`, con l'ingresso della misura da `PT-LAB`, il commento di Alfonso II e la prima riga della carta delle stime con **due numeri**
8. **Aggiornare `README.md`**: tabella dei documenti e «da fare» — fatto in v0.1 di questo documento, da rifare quando il capitolo sarà completo

---

## 15. Registro modifiche

- **v0.1 (01/10/2026)**: prima stesione. Formalizza il materiale storico-pedagogico del quinto anno di Pietro («Il mondo contemporaneo», primo e secondo percorso) in un documento coerente con gli anni precedenti:
  - i due percorsi distinti per funzione (le persone / i temi), con la constatazione che nell'Anno V sono **due metà dello stesso viaggio** e che i trenta livelli possono essere letti quasi in ordine cronologico;
  - il principio zero esteso: **non è il mondo a non esistere, è il tempo**, con la conseguenza didattica più difficile del progetto (il gioco non può dire come sarà);
  - sei principi dell'anno;
  - la mappa a **tempo**: il cantiere dell'Addizione Erculea come unico luogo percorribile, la pianta della città come geometria sovrapposta e sedici strati `S80`–`S95`, **sei dei quali vuoti** e mostrati come fasce bianche;
  - le sette porte `PT-LAB`, `PT-PAP`, `PT-MAT`, `PT-CAB`, `PT-CIT`, `PT-URB`, `PT-FUT`, con `PT-FUT` che **non porta niente** e si apre solo alla fine;
  - le trenta tappe agganciate ai trenta livelli dello schema, con **27 agganci forti e 3 medi** e i quattro da rivedere segnalati;
  - le trenta domande in forma piena;
  - trenta schede (ventotto nomi proprii, **due collettivi**), con i campi nuovi `stato` e `aggiunta`, sei persone viventi e sei aggiunte;
  - il criterio dell'anno, con la catena `PERSONAGGIO → METODO → NUMERO → ERRORE → CONFRONTO → DOMANDA` e la regola che **nessun numero può essere mostrato senza il suo errore**;
  - la **carta delle stime**, deliverable dell'anno, con i suoi campi e con le sei fasce bianche scrivibili;
  - le sedici domande dell'anno, con le quattro finali che il gioco non può chiudere;
  - il ritorno e la differenza temporale, la conclusione e la **regola di scrittura sulle frasi che contengono il futuro come dato**;
  - temi sensibili, con regole scritte prima delle schede;
  - **trentatré verifiche**, di cui due (V1 e V2 sull'Addizione Erculea) prioritarie;
  - **dieci questioni aperte**, la prima sul 1945 che non è una tappa e la seconda sul buco della biologia;
  - la regola di Newton al 5-3 e Leibniz al 4-7, già applicata all'Anno IV (v0.2 di `anno4-mondo.md`).
