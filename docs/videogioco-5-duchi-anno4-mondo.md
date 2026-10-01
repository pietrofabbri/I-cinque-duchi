---
titolo: Videogioco "I cinque duchi" — Anno IV, il mondo oltre l'Europa: l'archivio di Ferrara e il pianeta a strati
versione: 0.4
data: 2026-10-01
autore: Pietro Fabbri (con Claude)
fonte del materiale: due documenti di progettazione storico-pedagogica di Pietro ("ANNO IV — IL MONDO OLTRE L'EUROPA" e "ANNO IV — LE CIVILTÀ DEL MONDO"), 01/10/2026
dati: videogioco-5-duchi-anno4-mondo.json e videogioco-5-duchi-anno4-personaggi.json (da generare, v0.1)
documenti collegati: videogioco-5-duchi-schema-livelli.md (v1.1, livelli 4-1…4-30), videogioco-5-duchi-curricolo.md (v0.1, §4 cornice narrativa e §5.4 elenco dei livelli dell'anno 4), videogioco-5-duchi-luoghi.md (v0.1, la regola dei luoghi, applicata ai pin di questo documento), videogioco-5-duchi-anno3-europa.md (v0.2, da cui questo documento continua le convenzioni), videogioco-5-duchi-anno2-penisola.md (v0.2), videogioco-5-duchi-anno1-ferrara.md (v0.3), videogioco-5-duchi-anno1-mappa.md (v0.9), videogioco-5-duchi-esercizi.md (v0.1), videogioco-5-duchi-quadro-trasversale.md (v0.1), videogioco-5-duchi-gioco.md (v0.5), videogioco-5-duchi-meccaniche.md (v0.3)
---
# Anno IV — Il mondo oltre l'Europa

## 0. Che cosa contiene questo documento

Il documento **formalizza** il materiale storico-pedagogico di Pietro per il quarto anno e lo aggancia ai 30 livelli già definiti in `videogioco-5-duchi-schema-livelli.md` (v1.1, § «Anno 4 — Ercole II»).

Come per gli anni II e III:

- il **materiale** di Pietro è conservato e riordinato secondo le convenzioni del progetto;
- le **aggiunte** sono ciò che è stato introdotto per rendere il materiale giocabile, e sono segnalate voce per voce;
- le **proposte** sono da approvare e raccolte in §13;
- i **fatti storici non certi** sono indicati con `note_verifica` e raccolti in §12.

### 0.1 Il materiale è in due pezzi, e i due pezzi hanno funzioni diverse

Il quarto anno arriva in **due documenti separati**, e non è un caso:

- **«Il mondo oltre l'Europa»** (75 voci numerate) è il **percorso delle persone**: un viaggio nel tempo, da Ötzi ai protagonisti del presente, con l'Europa al centro per molto meno di quanto ci si aspetti. È una successione di incontri.
- **«Le civiltà del mondo»** (78 voci numerate) è il **percorso delle domande**: non cronologico, comparativo, costruito attorno a problemi (*vivere insieme, chi ha il diritto di comandare, cittadino o suddito, donne e potere, religione e società, le città, il commercio, il denaro, le migrazioni, le caste, la conoscenza, le epidemie, la propaganda, la libertà, le nazioni, gli imperi, le lingue, l'arte, il cinema, il progresso…*). Non è una successione di persone: è un **insieme di problemi**.

La formalizzazione li tiene separati perché sono due cose diverse, e li unisce perché il gioco ha bisogno di entrambe:

| | Percorso I («il mondo oltre l'Europa») | Percorso II («le civiltà del mondo») |
|---|---|---|
| Che cosa dà al gioco | **la voce**: chi arriva nell'archivio e parla | **l'asse di confronto**: la domanda che quella voce mette a confronto con un'altra civiltà |
| Ordine | cronologico e disperso (dal 3300 a.C. a oggi) | non cronologico, per problemi |
| Che cosa diventa | i **30 personaggi obbligatori** e le schede (§5) | il **confronto** di ogni tappa (§4, colonna «Confronto») |

*(aggiunta — questa è la decisione di impianto che rende il quarto anno costruibile)* Le due liste di materiale sono lunghe (75 + 78 voci, con duplicati interni: §6.5) e i livelli sono trenta. Non si possono usare tutte. Si usano **trenta persone del percorso I**, una per livello, e **trenta temi del percorso II**, uno per livello: ogni tappa è quindi un incontro fra una persona e un problema, ed è già la domanda che il gioco pone.

### 0.2 Le decisioni che il materiale implica

1. **Il protagonista è il mondo, la guida è il duca.** Il materiale dice: «Il protagonista è Ercole II d'Este». È vero nel senso narrativo — il suo mondo è il percorso — ma non nel senso meccanico: dal terzo anno vige la regola che **il duca non è il personaggio giocante** (Anno III §7, `AGENTS.md` §3). Ercole II è dunque il **personaggio giocante dell'anno 4 solo nella sua forma di guida-commentatore**, ed è la **soglia narrativa**: il suo mondo è quello che il giocatore attraversa (§3.5).
2. **Il quarto anno è l'anno dell'archivio.** I livelli 4-16…4-30 sono ciclo di vita del dato, modello E/R, tabelle, normalizzazione, algebra relazionale, SQL, privacy. Il tema non è «il mondo»: è **come una società registra se stessa e chi viene registrato**. È il terreno perfetto per il materiale di Pietro, che chiede esattamente questo (§10, «le fonti non parlano da sole»).
3. **Il presente resta aperto.** Il materiale chiude con «le persone del presente» e con la domanda finale. Nel gioco questo significa che **l'ultima tappa non è un personaggio ma una riga vuota** (§4, 4-30): il percorso non si chiude su una conclusione, si chiude su una domanda che il giocatore deve portare fuori dal gioco.
4. **Nessuna civiltà è il centro.** È il principio zero dell'anno (§1) e coincide con quanto il materiale dichiara al §72 («la storia non ha un centro»).

### 0.3 Tre conseguenze da mettere in conto subito

**(a) Gli agganci sono fortissimi, e questo è un rischio.** Dei 30 agganci: **24 forti, 6 medi, 0 di scena**. È il bilancio migliore dei quattro anni, e la ragione è precisa e verificabile: i livelli dell'anno 4 sono **astrazione, modelli, archivi, tabelle, query**, e il materiale di Pietro è una storia di **popoli che si raccontano e che finiscono negli archivi degli altri**. Il rischio è il rovescio di quello dell'Anno II: non un aggancio debole, ma un aggancio **troppo ovvio**, dove il livello sembra inventato per la persona. I tre da rivedere con Pietro sono **4-8 (Linneo)**, **4-9 (Mansa Musa)** e **4-24 (Zheng He)**.

**(b) Due strati restano senza tappe, ed è un buco vero.** Dei sedici strati (§3.2), due sono vuoti:

- **`S60`, prima delle città**: non è una scelta, è una constatazione. Prima del 3300 a.C. **non esistono documenti scritti**, e un archivio di quei tempi è vuoto. Il gioco può mostrarlo con una tappa facoltativa (Ötzi, che è già la tappa 2-1 dell'Anno II: v. §6.4);
- **`S66`, India e Asia meridionale dal 300 a.C. al 1200**: qui è una scelta, ed è un buco. Buddha e Ashoka sono due delle voci più forti del materiale e **non hanno tappa obbligatoria** (§13, Q2).

**(c) L'età digitale resta sottorappresentata, e per una ragione buona.** Quattro tappe arrivano all'Ottocento e al primo Novecento (4-17 Ambedkar, 4-25 Douglass, 4-27 Nightingale, 4-29 Curie) e **una sola** arriva al Novecento pieno (4-28, Orwell, 1903–1950). Berners-Lee, Gagarin, Armstrong, Mandela, Malala sono nel catalogo come **facoltativi e di atlante**. La ragione è che i livelli 4-29 e 4-30 (privacy, open data, database) sono i livelli in cui il presente sarebbe più naturale, e sono anche gli ultimi due, dove il percorso deve chiudersi con la domanda e non con un personaggio. È una decisione, non una dimenticanza: §13, Q3.

---

## 1. Il principio zero, esteso: il mondo non esiste ancora

L'Anno II ha insegnato che l'Italia non esiste come Stato. L'Anno III che non esiste l'Europa. Il quarto anno estende la lezione **al mondo intero**, ed è il passaggio più difficile dei quattro, perché qui non si tratta di una parola politica: si tratta dell'idea stessa che tiene insieme il racconto.

Nel 1534, quando Ercole II succede ad Alfonso I, **nessuno al mondo sa che esiste un mondo**. Non nel senso che non esiste, obviously: nel senso che **non esiste l'oggetto**. Non c'è un pianeta osservato dall'esterno, non c'è una fotografia della Terra, non c'è un nome collettivo per l'umanità, non c'è un modo di pensare che «l'Africa», «l'Asia» e «l'America» siano tre parti di una stessa figura. C'è il mondo conosciuto — l'oikouménos degli antichi, la «terra abitata» — e poi c'è il resto, che non ha nome e non è percepito come un luogo.

Ne segue la conseguenza didattica, che è la più forte del progetto:

> **nessun personaggio di questo documento è «del mondo», e nessuno è «di un altro mondo».** Un mercante di Timbuctù e un amanuense di Ferrara non appartengono a due metà della Terra: appartengono a due reti di scambio che si incontreranno, o non si incontreranno mai, e che potrebbero anche non sapere l'una dell'altra.

E ne segue la seconda, che è quella che il materiale mette al centro e che è il principio zero vero e proprio dell'anno:

> **la storia non ha un centro.** Non perché sia politicamente corretto dirlo, ma perché è un fatto documentabile: mentre Ferrara vive il suo Rinascimento, la Cina ha una tradizione politica millenaria, l'India ha imperi, l'Impero ottomano governa tre continenti, l'Africa occidentale ha regni e banche, e nessuno di questi mondi sa che gli altri esistono. La storia mondiale **nasce** nel momento in cui queste storie vengono messe in relazione — e quel momento, per la maggior parte di esse, è **violento**.

---

## 2. I principi del quarto anno

1. **Il protagonista è il mondo, il luogo è l'archivio, la guida è il duca.** Nell'Anno I il protagonista narrativo era la città, nell'Anno II la penisola, nell'Anno III il continente, nel quarto è **il pianeta**. Il luogo percorribile è una stanza sola: l'archivio della corte (§3.3).
2. **Ogni tappa è un documento che entra e viene catalogato.** Il giocatore non incontra persone: incontra **carte**, e ogni carta ha un autore, una data, un viaggio e una traduzione. Questa è la differenza rispetto all'Anno III e va dichiarata ai ragazzi: «nell'anno scorso le persone entravano nella stanza; quest'anno entra ciò che hanno scritto.»
3. **La colonna del tempo non è lineare.** La scala va da 300.000 anni fa a oggi: servono dodici ordini di grandezza. Il gioco **dichiara** la scala logaritmica invece di nasconderla (§3.1).
4. **Non è una cronologia.** L'ordine dei 30 livelli è l'ordine degli **argomenti**: si parte da Gilgamesh, si finisce con una riga vuota. Il percorso torna indietro di venti secoli più di due volte. È un disordine produttivo, e come negli anni precedenti va dichiarato, non nascosto.
5. **Ogni documento è di qualcuno.** La competenza finale non è «sapere la storia del mondo», ma **pesare le prospettive**: non tutte le fonti valgono lo stesso, e saperlo spiegare è il compito (§8, domande 14–16).
6. **La persona non è un modello.** Le categorie moderne servono a organizzare, non a contenere. Ogni scheda deve dire che cosa della persona **non** ci sta nel suo attributo (§6.3).

---

## 3. La mappa: il pianeta a strati

*(aggiunta, 01/10/2026)*

### 3.1 Due assi, e una scala che non è lineare

- **asse orizzontale, il luogo**: il pianeta in vista dall'alto, con la geografia reale di coste, fiumi, deserti, catene e oceani (open data, con attribuzione, come `AGENTS.md` §5). È la stessa architettura degli anni II e III, portata alla scala del globo;
- **asse verticale, lo strato**: accanto alla pianta, una **colonna stratigrafica** con sedici strati.

La differenza rispetto agli anni precedenti è nella scala, e va risolta esplicitamente perché il giocatore la vede: fra il più antico strato e il più recente ci sono **cinque o sei mila anni**, e la distanza fra il 3300 a.C. e il 1500 d.C. è grande quanto quella fra il 1500 e oggi. Una colonna lineale renderebbe il Cinquecento una striscia invisibile.

*(aggiunta — proposta)* La colonna usa quindi una **scala logaritmica del tempo**, dichiarata a schermo, e il gioco la usa come occasione didattica: il livello 4-1 chiede l'astrazione, e **la prima astrazione del gioco è la colonna stessa**. Chi guarda la colonna vede subito che la vicinanza di due epoche sulla colonna non significa parentela: `S71` (1450–1521) e `S72` (1520–1560) sono adiacenti e non hanno nulla a che fare l'una con l'altra. È la stessa lezione del terzo anno (la continuità **sembra** naturale e non lo è), ma su scala maggiore.

### 3.2 Gli strati

| Strato | Denominazione | Periodo indicativo | Tappe obbligatorie |
|---|---|---|---|
| `S60` | Prima delle città | 300.000 – 10.000 anni fa | — |
| `S61` | Le prime città e la prima scrittura | 3000 – 1900 a.C. | 4-1, 4-22 |
| `S62` | Egitto e Africa settentrionale | 2000 – 500 a.C. | 4-4 |
| `S63` | Cina: le procedure e la scrittura | 600 a.C. – 500 d.C. | 4-3, 4-12 |
| `S64` | I mondi greci | 800 – 100 a.C. | 4-15 |
| `S65` | Roma, l'Impero, il tardoantico | 100 a.C. – 600 d.C. | 4-13 |
| `S66` | India e Asia meridionale | 300 a.C. – 1200 d.C. | — |
| `S67` | I mondi islamici | 700 – 1500 | 4-2, 4-11, 4-19 |
| `S68` | Gli imperi eurasiatici | 1100 – 1300 | 4-6 |
| `S69` | Africa occidentale, deserti e rotte | 1200 – 1450 | 4-9, 4-16 |
| `S70` | Asia e oceano | 1300 – 1500 | 4-24 |
| `S71` | La prima metà del XVI secolo | 1450 – 1521 | 4-14, 4-21, 4-23, 4-26 |
| `S72` | La corte | 1520 – 1560 | 4-10, 4-18 |
| `S73` | La ragione misurata | 1560 – 1750 | 4-5, 4-7, 4-8 |
| `S74` | Cifre, diritti, misure | 1750 – 1900 | 4-17, 4-20, 4-25, 4-27, 4-29 |
| `S75` | Il secolo breve e il presente aperto | 1900 – oggi | 4-28, 4-30 |

**I due strati vuoti.** `S60` non è un errore: prima del 3300 a.C. **non ci sono documenti scritti**, e il vuoto dell'archivio è il primo insegnamento dell'anno. `S66` è una scelta, e una scelta discussa: Buddha e Ashoka ci sono, ma come facoltativi (§13, Q2).

**Vincoli sugli strati.** Come negli anni precedenti, **nessun vincolo di monotonia**: il percorso scende e risale continuamente (4-1 è in `S61`, 4-4 in `S62`, 4-10 in `S72`, 4-13 in `S65`, 4-22 in `S61`, 4-30 in `S75`). Le regole: ogni tappa dichiara il proprio strato; un luogo può comparire più volte purché cambi la voce; la nebbia dipende dal **pin visitato**, non dallo strato.

### 3.3 L'archivio: perché questo risolve il problema della scala

*(aggiunta, e punto centrale dell'anno)*

Una mappa del pianeta con cinquemila anni non è percorribile: da Ferrara a Tenochtitlán ci sono dodici mila chilometri e nessuna strada. La soluzione non è una mappa percorribile: è **un archivio**.

Il giocatore **non viaggia**. Si muove dentro la **sala dell'archivio** della corte di Ferrara, costruita sul luogo dove materialmente si trovava l'archivio ducale e dove ancora oggi si conserva l'archivio storico comunale. Ogni tappa è **un documento che entra nella sala**, e il gioco ne annuncia l'arrivo. Le prime dieci tappe costruiscono le **classi** (che cosa è un documento, che cosa è una persona, che cosa è un luogo); le altre venti costruiscono le **tabelle**, e alla fine il giocatore ha un archivio con dentro tutto quello che è arrivato.

La meccanica fa quattro cose insieme:

1. **risolve la scala** — non serve una mappa percorribile, serve una mappa su cui arrivano cose;
2. **è storicamente esatta** — è così che un archivio del Cinquecento funzionava davvero: non si esplorava il mondo, si **riordinava ciò che era arrivato**;
3. **è il livello 4-16 riscritto in forma drammatica** — il gioco *è* il ciclo di vita del dato: raccolta, archiviazione, elaborazione, conservazione, cancellazione;
4. **è la risposta al buco tematico degli anni precedenti** — dopo il vuoto su colonialismo e tratta dichiarato nell'Anno III (§13 Q2 di quel documento), il quarto anno mette quei fatti **dentro l'archivio**, dove sono registri, elenchi, contratti, e dove la domanda «chi ha scritto questa riga?» è la domanda del gioco.

*(proposta)* Ogni documento che entra **resta** nella sala. All'inizio l'archivio ha tre scaffali vuoti; alla fine della tappa 4-30 ne ha uno pieno, e il giocatore lo sfoglia. È il primo momento del gioco in cui ciò che ha costruito è **visibile tutto insieme**.

### 3.4 I sette modi di arrivo e le sette porte

Come negli anni precedenti, ciò che arriva da un luogo non rappresentabile sulla pianta è annunciato da una **porta**: un punto della sala da cui la risorsa entra, e che dice **come** è arrivata.

| Porta | Dove | Che cosa arriva | Tappe |
|---|---|---|---|
| `PT-SCR` | lo scaffale dei testi | un testo antico: una tavoletta, un rotolo, un papiro, un'edizione a stampa | 4-1, 4-11, 4-12, 4-15, 4-16, 4-22, 4-28 |
| `PT-ORR` | l'aula delle deposizioni | una testimonianza detta a voce e messa per iscritto | 4-6, 4-13, 4-26 |
| `PT-CRR` | il corridoio dei corrieri | una lettera, un rapporto, un trattato, un registro di corte | 4-5, 4-7, 4-8, 4-10, 4-17, 4-18, 4-21, 4-23 |
| `PT-MAR` | l'armadio delle carte di mare | una carta nautica, un registro di viaggio, un giornale di bordo | 4-2, 4-9, 4-24 |
| `PT-REG` | l'archivio delle persone censite | un censimento, un libro di leggi, un elenco di tribute | 4-3, 4-4, 4-14, 4-20, 4-25 |
| `PT-LAB` | il banco dei laboratori | un quaderno di misure, una tabella di esperimenti | 4-19, 4-27, 4-29 |
| `PT-VOC` | la stanza senza finestre | ciò che resta di chi non scrisse | 4-30 |

*(proposta)* Le sette porte sono la prova visiva che **l'informazione in questo mondo viaggia con le persone e arriva mediata**. Ogni volta che una porta si apre, il gioco mostra **chi ha tradotto, chi ha tagliato, chi ha ritardato**. La settima porta è l'unica che non si apre mai prima della fine, ed è deliberato: il giocatore passa ventinove tappe a registrare la voce di qualcuno, e alla trentunesima scopre che la porta accanto non l'aveva mai notata.

### 3.5 Ercole II: la soglia, e il suo limite

Ercole II **non esce mai dall'archivio** nel corso dell'anno. Il meccanico è semplice e ripetuto trenta volte. All'inizio di ogni tappa **Ercole commenta il documento che sta arrivando**, e lo fa **solo con ciò che sa**:

- se il documento viene da un'epoca che Ercole conosce (i corrieri, i vescovi, i mercanti, i libri che arrivano in città), Ercole parla, e dice il suo parere — che è spesso di parte, e spesso sbagliato;
- se il documento viene da un'epoca che Ercole **non può conoscere** (Uruk nel 2700 a.C., Atene nel V secolo, Alessandria nel IV, Tenochtitlán nel 1519), il gioco **lo dice**: «Questo non è arrivato. Non arriverà. Non lo vedrai.» E la tappa si gioca lo stesso.

Ne segue la regola che rende il gioco onesto sul lungo periodo, ed è la stessa dell'Anno III resa meccanica:

> **il giocatore sa tutto, Ercole non sa quasi niente, e le due colonne non si incontrano mai.**

Ma c'è una differenza rispetto al terzo anno, e va detta. Nell'Anno III Ercole commentava **l'arrivo** di una risorsa. Nel quarto anno l'archivio è **il suo ufficio**: non può non sapere che un documento è arrivato, perché lui stesso (o chiunque gli stia accanto) ha dovuto registrarlo. Perciò il commento di Ercole cambia natura: **non giudica il contenuto, ma l'operazione**. «Questo l'hanno scritto loro. Perché l'hanno scritto in questo modo? A me serve per sapere chi devo pagare.» È la posizione di un archivista, e storicamente è la posizione giusta: la domanda di Ercole è *a chi serve questo documento?*, che è la domanda con cui si apre la stampa moderna.

*(aggiunta)* Il 1534 è anche l'anno in cui a Ferrara brucia una parte della città, e in cui l'archivio ducale è esposto. Va verificato (V1) che cosa si perse e che cosa rimase: se è vero che dell'archivio di centinaia di anni si sono conservati registri sparsi, **è la prova storica più forte della tesi dell'anno**, e va nella tappa 4-10 come fatto, non come metafora.

### 3.6 La fine dell'anno

Alla tappa 4-30 l'archivio è completo. Il gioco non chiude con una domanda di Ercole, ma con un'operazione: il giocatore **stampa il registro**. Trenta righe, con i suoi campi. E vede che una riga è vuota.

La domanda a schermo intero, che è la conclusione del quarto anno, è quella del materiale di Pietro riformulata come domanda sul gioco:

> **questo registro è la storia del mondo, o è la storia di chi ha scritto?**

---

## 4. Le 30 tappe

*(aggiunta — costruita sui 30 livelli dello schema, non il contrario)*

**Colonna «Forza».** Come negli anni precedenti: **forte** il legame è naturale; **medio** funziona ma va costruito nel racconto; **di scena** il luogo fa solo da ambientazione.

**Colonna «Confronto».** Il tema del percorso II che quella tappa mette a confronto con la persona del percorso I (§0.1). È la seconda voce dell'anno, ed è quella che rende il gioco comparativo invece che enciclopedico.

**Colonna «Voce».** `personaggio` = nome proprio. `collettivo` = voce senza nome proprio, con attendibilità `C`. In questo anno sono **2 su 30**: sono i due registri senza firma (i censori, e le persone che non hanno potuto scrivere), e sono la risposta del gioco alla domanda finale del materiale.

| Livello | Argomento | Strato | Pin | Voce | Porta | Domanda che apre la tappa | Forza | Confronto (percorso II) | Facoltativi (2) |
|---|---|---|---|---|---|---|---|---|---|
| **4-1** | Astrazione: dal problema al modello | `S61` | Uruk | **Gilgamesh** (Q201) | `PT-SCR` | Una tavoletta d'argilla non è il mondo: che cosa ci metti dentro, e che cosa perdi? | forte | §68 Le fonti non parlano da sole | L'Eneuma Elish (collettivo); il re assiro (facoltativa) |
| **4-2** | Pile e code | `S67` | Il Cairo e le carovane | **Ibn Battuta** (Q202) | `PT-MAR` | Un viaggio è una coda: si arriva nell'ordine in cui si è partiti. E se qualcuno si perde? | forte | §11 Le persone che si spostano | Ibn Jubayr (facoltativa); i portatori d'acqua |
| **4-3** | Classi e oggetti | `S63` | Xianyang | **Qin Shi Huang** (Q203) | `PT-REG` | Un impero che rende ogni misura uguale a ogni altra: che cos'è, un oggetto? | forte | §2 Chi ha il diritto di comandare | Il figlio di Shi Huangdi (facoltativa); gli scribi |
| **4-4** | Attributi, metodi, costruttori | `S62` | Tebe | **Hatshepsut** (Q204) | `PT-REG` | Il giorno in cui prendi il nome e la corona un oggetto cambia: che cosa succede ai suoi attributi? | forte | §54 L'arte come memoria | Nefertari (facoltativa); i sacerdoti di Amun |
| **4-5** | Incapsulamento | `S73` | Agra | **Akbar** (Q205) | `PT-CRR` | Un impero con mille lingue e mille divinità: fuori c'è una porta sola. Chi decide che cosa si vede? | medio | §6 Quando la religione diventa identità politica | Abul Fazl (facoltativa); le città nuove |
| **4-6** | Ereditarietà | `S68` | Karakorum | **Gengis Khan** (Q206) | `PT-ORR` | Un impero che si eredita a voce, non su carta: che cosa passa, e che cosa si rompe? | forte | §44 Gli imperi | I quattro khanati (collettivo); i cronachi cinesi |
| **4-7** | Polimorfismo e interfacce | `S73` | Hannover | **Leibniz** (Q207, *aggiunta*) | `PT-CRR` | Due persone che non si sono mai incontrate costruiscono la stessa cosa: com'è possibile? | medio | §22 La conoscenza | Newton (ritorno, v. §6.4); Hooke (facoltativa) |
| **4-8** | Diagramma UML delle classi | `S73` | Uppsala | **Carl Linneo** (Q208) | `PT-CRR` | Il mondo diventa un disegno di caselle e linee. È una descrizione, o è un verdetto? | forte | §20 Il razzismo moderno | I lini (collettivo); le critiche alla classificazione (facoltativa) |
| **4-9** | Liste collegate e riferimenti | `S69` | Il Cairo `A`, con Timbuctù `S` | **Mansa Musa** (Q209) | `PT-MAR` | Una catena di pozzi, e ogni pozzo indica il successivo: che cosa succede se ne salta uno? | forte | §9 Il commercio | I mercanti di Songhai; Ibn Battuta (ritorno, facoltativa) |
| **4-10** | Prova di corte: modellare un sistema a oggetti | `S72` | Ferrara, corte | **Ercole II d'Este** (Q210) | `PT-CRR` | Di settantacinque anni di duchi, quasi niente è rimasto. Che cosa manca, e chi l'ha perso? | forte | §71 Ercole II guarda il mondo | I magazzinieri; Lucrezia Borgia (ritorno) |
| **4-11** | Implementare un linguaggio | `S67` | Baghdad | **Al-Khwarizmi** (Q211) | `PT-SCR` | Una procedura scritta perché la esegua qualcun altro: il primo programma è una regola in arabo. | forte | §50 Le lingue | Robert of Chester (facoltativa); il libro dell'algebra |
| **4-12** | Analisi lessicale: i token | `S63` | Qufu | **Confucio** (Q212) | `PT-SCR` | Un testo di cinquemila anni senza un punto e senza una virgola: come trovi le parole? | forte | §1 Vivere insieme | Il dizionario di Mengxi (facoltativa); i calligrafi |
| **4-13** | Grammatiche e sintassi (BNF) | `S65` | Alessandria | **Ipazia** (Q213) | `PT-ORR` | Tre scritture sulla stessa pietra e una sola frase: come si riconosce la stessa frase in tre lingue? | medio | §23 Ma la conoscenza può anche essere perduta | I sacerdoti di Soknopaiou Nesos (facoltativa); le tre scritture |
| **4-14** | Alberi sintattici e valutazione | `S71` | Tenochtitlán | **Moctezuma II** (Q214) | `PT-REG` | Il trono si eredita dalla parte della madre: l'albero si percorre al contrario. Come ci si cerca dentro? | medio | §13 Le Americhe prima e dopo l'arrivo europeo | Tlacaelel (facoltativa); i calendari (collettivo) |
| **4-15** | Un mini-interprete | `S64` | Chio e la Ionia | **Omero** (Q215) | `PT-ORR` | Nessuno scrisse i poemi: li cantavano. Un testo senza pagina, che si esegue a voce? | forte | §25 Esplorare non significa scoprire | I rapsodi (collettivo); Pisistrato (facoltativa) |
| **4-16** | Dato, informazione, archivio | `S69` | Tunisi e Il Cairo | **Ibn Khaldun** (Q216) | `PT-SCR` | Davanti a sette generazioni dico che cambieranno. È una previsione, o ha letto i registri? | medio | §72 Il concetto di progresso | Cesare (ritorno, facoltativa); le tribù del deserto |
| **4-17** | Modello E/R: entità, attributi, relazioni | `S74` | Bombay e Delhi | **B. R. Ambedkar** (Q217) | `PT-CRR` | Nati in una certa famiglia si eredita anche un mestiere e un posto dove sedersi. È una tabella? | forte | §19 Le caste e la gerarchia | Il tempio di Kalaram (facoltativa); il poeta |
| **4-18** | Cardinalità e vincoli | `S72` | Costantinopoli | **Solimano il Magnifico** (Q218) | `PT-CRR` | Un impero in cui ognuno appartiene a più di una cosa: quante relazioni servono? | forte | §8 Le città raccontano il potere | I millet (collettivo); Ibrahim, fratello del sultano (facoltativa) |
| **4-19** | Modello relazionale: tabelle e chiavi | `S67` | Il Cairo | **Ibn al-Haytham** (Q219) | `PT-LAB` | Sei righe di misure per ogni luce: la tabella c'è, ma la chiave è una domanda. | medio | §24 Chi può produrre conoscenza | Il Libro degli specchi (facoltativa); il muḥtasib |
| **4-20** | Prova di corte: progettare uno schema E/R | `S74` | Ferrara e il regno | **I censori** (Q220, collettivo `C`) | `PT-REG` | Contare tutti: persone, case, botti. Qualcuno però si conta in un campo diverso dagli altri. Chi? | forte | §42 La dichiarazione dei diritti | Gli ufficiali del catasto; il censitore cinese (facoltativa) |
| **4-21** | Dall'E/R allo schema relazionale | `S71` | Toledo | **Isabella di Castiglia** (Q221) | `PT-CRR` | Per tassare un regno si fa un elenco di tutte le case. Qualcuno fa l'elenco di tutte le case. | forte | §43 Le nazioni | I censitori (collettivo); i funzionari dell'archivio |
| **4-22** | Normalizzazione (fino alla 3FN) | `S61` | Babilonia | **Hammurabi** (Q222) | `PT-SCR` | Duecentottantadue frasi, e in ognuna un nome, un numero, un metallo. Si può dividere senza perdere niente? | forte | §10 Il denaro | Il codice (collettivo); la stele di Nippur (facoltativa) |
| **4-23** | Algebra relazionale: selezione, proiezione, join | `S71` | Lisbona e Calicut | **Vasco da Gama** (Q223) | `PT-MAR` | Una rotta che arriva in un porto che fa commercio da sempre: stai cercando il mondo, o il tavolo? | forte | §25 Esplorare non significa scoprire | I piloti di Malindi (collettivo); Ahmad ibn Majid (facoltativa) |
| **4-24** | SQL: creare e modificare | `S70` | Nanchang e il mare | **Zheng He** (Q224) | `PT-MAR` | Quattrocento navi, ventisettemila persone, tre anni. Nessuno scrive una riga: come si fa? | forte | §64 Il pianeta interconnesso | Ma Huan (facoltativa); i cantieri |
| **4-25** | SQL: SELECT, WHERE, ORDER BY | `S74` | Annapolis e Baltimora | **Frederick Douglass** (Q225) | `PT-REG` | Un elenco di persone in cui gli schiavi non ci sono. Come si fa a contarli senza contarli? | forte | §12 La diaspora africana | Sojourner Truth (facoltativa); i censitori (ritorno) |
| **4-26** | SQL: JOIN | `S71` | Spagna e Tenochtitlán | **Hernán Cortés** (Q226) | `PT-ORR` | Un impero di milioni non crolla per un esercito: crolla quando si unisce a un'altra tabella. | forte | §48 Il colonialismo visto da più lati | Las Casas (facoltativa); i signori di Tlaxcala (collettivo) |
| **4-27** | SQL: aggregazioni e GROUP BY | `S74` | Scutari e Costantinopoli | **Florence Nightingale** (Q227) | `PT-LAB` | Non basta sapere quante persone sono morte: bisogna sapere di che cosa, e in che mese. | forte | §29 Le epidemie | Gorgas (facoltativa); i soldati (collettivo) |
| **4-28** | SQL da Python ★ | `S75` | Motihari e Londra | **George Orwell** (Q228) | `PT-SCR` | Un programma è un testo che si legge: ogni testo che arriva dall'esterno va letto come un ordine. Come? | forte | §67 Il problema dell'informazione | Il lavoro alla BBC; la revisione spagnola (facoltativa) |
| **4-29** | Privacy, GDPR, open data | `S74` | Parigi e Varsavia | **Marie Curie** (Q229) | `PT-LAB` | I suoi quaderni sono ancora radioattivi: di chi sono i dati di una persona, e chi decide? | forte | §4 Donne e potere | Il libro di Irène; l'Accademia (facoltativa) |
| **4-30** | Prova finale: database e applicazione a oggetti | `S75` | Ferrara, archivio | **Le persone che non hanno firmato** (Q230, collettivo `C`) | `PT-VOC` | Trenta documenti, trenta righe. Chi non ha potuto scrivere la sua? | forte | §69 La storia dei vincitori | Le voci senza nome (facoltativa); Ercole II |

**Verifica degli agganci.** Dei 30 agganci: **24 forti, 6 medi, 0 di scena**. I **sei medi** sono 4-5 (Akbar/incapsulamento), 4-7 (Leibniz/polimorfismo), 4-13 (Ipazia/BNF), 4-14 (Moctezuma/alberi), 4-16 (Ibn Khaldun/ciclo di vita), 4-19 (Ibn al-Haytham/chiavi). I tre **da rivedere con Pietro** perché l'aggancio è forse troppo ovvio: 4-8, 4-9, 4-24.

*(proposta)* Questo bilancio è migliore di quello degli anni precedenti (13 forti nell'Anno II, 21 nell'Anno III) e la ragione è verificabile: i livelli dell'anno 4 sono **la rappresentazione del dato e i suoi strumenti**, e il materiale di Pietro è, senza volerlo, la storia di **come l'umanità si è registrata e di chi non è riuscito a registrarsi**. Il percorso è stato costruito da qui, non per forzatura. Vedi §13, Q4.

### 4.1 Le trenta domande in forma piena

Le domande della tabella sono il cuore didattico dell'anno. In forma estesa, con i tre livelli di fonte (§6.2):

1. **Gilgamesh** — *Una tavoletta d'argilla non è il mondo: che cosa ci metti, e che cosa perdi?* (fonte: le tavolette di Nippur; ricostruzione: la scrittura come mezzo; memoria: il diluvio, che ha cancellato il resto)
2. **Ibn Battuta** — *Un viaggio è una coda: e se qualcuno si perde?* (fonte: la *Rihla*, dettata a Ibn Juzayy; ricostruzione: venticinque anni di viaggi; memoria: il viaggiatio infallibile)
3. **Qin Shi Huang** — *Un impero che rende ogni misura uguale a ogni altra: che cos'è, un oggetto?* (fonte: le iscrizioni in piccola scrittura; ricostruzione: la standardizzazione; memoria: il primo imperatore, che è anche l'uomo che bruciò i libri)
4. **Hatshepsut** — *Che cosa succede agli attributi di una persona quando qualcun altro li cambia?* (fonte: le statue cancellate; ricostruzione: le raffigurazioni maschili; memoria: la maledizione di Hatshepsut, che è una leggerie ottocentesca)
5. **Akbar** — *Fuori c'è una porta sola: chi decide che cosa si vede?* (fonte: l'*A'in-i Akbari* di Abul Fazl; ricostruzione: l'amministrazione; memoria: il sovrano tollerante, che è una semplificazione)
6. **Gengis Khan** — *Che cosa passa, e che cosa si rompe, in un impero che si eredita a voce?* (fonte: la *Secret History*, di molto posteriore; ricostruzione: la divisione del 1229; memoria: il conquistatore, che non nomina mai i popoli che si ribellano)
7. **Leibniz** — *Due persone che non si sono mai incontrate costruiscono la stessa cosa: com'è possibile?* (fonte: i *Cartegi* del 1676 e i *Principia*; ricostruzione: il calcolo; memoria: la disputa di priorità, che è durata più di un secolo)
8. **Linneo** — *Il mondo diventa un disegno di caselle: descrizione o verdetto?* (fonte: il *Systema Naturae*; ricostruzione: l'osservazione sul campo; memoria: il naturalista innocente, che non è esistito)
9. **Mansa Musa** — *Ogni pozzo indica il successivo: che cosa succede se ne salta uno?* (pin: Il Cairo, non Timbuctù — v. §3.3, 3 e `luoghi.md`) (fonte: le relazioni dei mercanti; ricostruzione: il viaggio del 1324; memoria: l'uomo che porta più oro di tutti)
10. **Ercole II d'Este** — *Di settantacinque anni di duchi, quasi niente è rimasto: che cosa manca?* (fonte: l'archivio; ricostruzione: l'incendio e le perdite; memoria: il duca che amava la musica, che è tutto ciò che si dice di lui)
11. **Al-Khwarizmi** — *Una procedura scritta perché la esegua qualcun altro.* (fonte: il trattato di algebra; ricostruzione: i manuali di aritmetica; memoria: l'uomo il cui nome è diventato una parola)
12. **Confucio** — *Come trovi le parole in un testo che non ha né punti né virgole?* (fonte: gli *Analects*, compilati dopo; ricostruzione: il lessico cinese; memoria: il vecchio saggio, che non scrisse nulla)
13. **Ipazia** — *Tre scritture, una frase: come si riconosce la stessa frase in tre lingue?* (fonte: la stele; ricostruzione: la tradizione di Ipazia è quasi tutta tardiva; memoria: la donna bruciata, che è un racconto di secoli dopo)
14. **Moctezuma II** — *L'albero si percorre al contrario: come si cerca la corona dentro un albero?* (fonte: i registri tlaxcalteca e spagnoli; ricostruzione: la successione; memoria: l'imperatore che non vide niente)
15. **Omero** — *Un testo senza pagina, che si esegue a voce: come si cataloga?* (fonte: l'oralità, ricostruita dai filologi; ricostruzione: la fissazione per iscritto; memoria: il cieco, che non è mai stato cieco)
16. **Ibn Khaldun** — *È una previsione, o ha letto i registri?* (fonte: la *Muqaddimah*; ricostruzione: il metodo; memoria: il filosofo isolato, che ha insegnato a un giovane spagnolo)
17. **Ambedkar** — *Nati in una certa famiglia si eredita anche un mestiere: è una tabella?* (fonte: *L'annullamento delle caste*; ricostruzione: le lotte per i templi; memoria: il riformatore che ha salvato l'India, che è metà della verità)
18. **Solimano** — *Quante relazioni servono per un impero in cui ognuno appartiene a più di una cosa?* (fonte: il *Kanunname*; ricostruzione: l'amministrazione; memoria: il sultano, che è un titolo)
19. **Ibn al-Haytham** — *La tabella c'è, ma la chiave è una domanda.* (fonte: il *Kitab al-Manazir*; ricostruzione: le misure sull'ombra; memoria: l'uomo che ha capito la luce, che è un anacronismo)
20. **I censori** — *Qualcuno si conta in un campo diverso dagli altri: chi decide quale?* (fonte: i moduli; ricostruzione: la burocrazia; memoria: nessuna, ed è la lezione)
21. **Isabella di Castiglia** — *Qualcuno fa l'elenco di tutte le case.* (fonte: i *padrones*; ricostruzione: la riconquista e la tassazione; memoria: la regina che non governò, che è falso)
22. **Hammurabi** — *Si può dividere senza perdere niente?* (fonte: la stele; ricostruzione: l'uso del diritto; memoria: il primo codice civile, che non è un codice)
23. **Vasco da Gama** — *Stai cercando il mondo, o stai cercando il tavolo?* (fonte: il *Sumi da India* di Alvise; ricostruzione: la rotta; memoria: il navigatore che aprì le rotte, che erano già aperte)
24. **Zheng He** — *Nessuno scrive una riga: come si fa?* (fonte: il *Xingcha Shenglan*; ricostruzione: le sette spedizioni; memoria: le navi enormi, di cui nessuna traccia)
25. **Douglass** — *Come si fa a contarli senza contarli?* (fonte: le clausole di fuga; ricostruzione: il censimento americano; memoria: l'oratore, che è vero e non basta)
26. **Cortés** — *Un impero crolla quando si unisce a un'altra tabella.* (fonte: le lettere di Cortés; ricostruzione: le alleanze indigene; memoria: il traditore, che è una versione spagnola del 1519 e non ha le sue ragioni)
27. **Nightingale** — *Non basta il numero: serve la causa e il mese.* (fonte: le *Note* del 1858; ricostruzione: l'ospedale di Scutari; memoria: la donna con la lampada, che è un'immagine di giornale del 1855)
28. **Orwell** — *Ogni testo che arriva dall'esterno va letto come un ordine: come?* (fonte: il romanzo; ricostruzione: la guerra di Spagna e la BBC; memoria: il futuro, che è diventato il presente)
29. **Curie** — *Di chi sono i dati di una persona?* (fonte: i quaderni di laboratorio; ricostruzione: la gestione dei rifiuti radioattivi; memoria: la coppia, che era un lui e una lei)
30. **Le persone che non hanno firmato** — *Chi non ha potuto scrivere la sua riga?* (fonte: l'assenza stessa della fonte; ricostruzione: i nomi recuperati; memoria: nessuna, ed è la lezione)

---

## 5. Le schede dei 30 personaggi obbligatori

*(aggiunta — i codici `Q` continuano la serie degli anni II e III da **Q201**, per non riaprire la numerazione; v. §13, Q5)*

Formato di ogni scheda, come in `anno1-ferrara.md` §10, `anno2-penisola.md` §5 e `anno3-europa.md` §5.

### Q201 · Gilgamesh
- **Periodo:** circa 2700 a.C. (personaggio mitico, terzo millenario a.C. nella tradione). **Luogo:** Uruk. **Pin:** Uruk. **Strato:** `S61`. **Attendibilità:** `M` (il personaggio è letterario; le tavolette che lo raccontano sono reali e parziali).
- **Domanda:** una tavoletta d'argilla non è il mondo: che cosa ci metti dentro, e che cosa perdi?
- **Fonte:** le tavolette di Nippur; **ricostruzione:** la scrittura cuneiforme come tecnologia; **memoria:** il diluvio, che ha cancellato quasi tutto e ha reso Gilgamesh il primo eroe che sembri universale.
- **Aggancio 4-1:** l'*Epopea di Gilgamesh* è la prima opera in cui **un racconto viene fissato**: prima la parola cantata, poi la parola scritta. Il livello chiede che cosa si perde quando si passa dal mondo al modello: la prima riga di codice del gioco è una descrizione, e una descrizione lascia fuori quasi tutto. **Forte.**
- **Motto:** «Nessuno scrive la vita di un uomo: scrive quello che di lui si può dire in duecento righe.» **Emblema:** una tavoletta d'argilla con quattro righe di cunei.

### Q202 · Ibn Battuta
- **Periodo:** 1304–1368 circa. **Luogo:** Ceuta, Il Cairo, Mecca, Delhi, Malindi, Zanzibar. **Pin:** Il Cairo. **Strato:** `S67`. **Attendibilità:** `D+I` (il viaggio è documentato, il racconto è dettato a uno scriba al servizio del sultano del Marocco e ha una finalità politica).
- **Domanda:** un viaggio è una coda: si arriva nell'ordine in cui si è partiti. E se qualcuno si perde?
- **Fonte:** la *Rihla*, dettata a Ibn Juzayy; **ricostruzione:** venticinque anni, dalla penisola iberica all'India e all'Africa orientale; **memoria:** il viaggiatio infallibile.
- **Aggancio 4-2:** la struttura del livello è una **coda FIFO**: si parte, si accodano gli incontri, si escono nell'ordine. Ibn Battuta è l'esempio più pulito di una sequenza di arrivi in cui **ogni tappa è il risultato della precedente**, e in cui l'errore di una tappa (una nave che non parte) sposta tutte le altre. **Forte.**
- **Motto:** «Sono passati venticinque anni e non ho ancora visto il fondo della coda.» **Emblema:** un tappeto arrotolato con una fila di nodi.

### Q203 · Qin Shi Huang
- **Periodo:** 259–210 a.C. **Luogo:** Xianyang. **Pin:** Xianyang. **Strato:** `S63`. **Attendibilità:** `D`.
- **Domanda:** un impero che rende ogni misura uguale a ogni altra: che cos'è, un oggetto?
- **Fonte:** le iscrizioni in *piccola scrittura*; **ricostruzione:** la standardizzazione di caratteri, pesi, misure e larghezze di carro; **memoria:** il primo imperatore, che è anche l'uomo che bruciò i libri.
- **Aggancio 4-3:** per poter avere una tabella occorre che gli oggetti siano **intercambiabili**: una clessidra diversa da un'altra, misurata con lo stesso criterio, diventa confrontabile con tutte le altre. La standardizzazione di Qin Shi Huang è esattamente il passaggio da «un mucchio di oggetti» a «una classe di oggetti con gli stessi attributi». Il livello può mostrarlo in modo immediato: lo stesso tipo di oggetto, con lo stesso attributo, in province che non si sono mai viste. **Forte.**
- **Motto:** «Se due pesi non danno lo stesso risultato, uno dei due è falso.» **Emblema:** un peso di bronzo con tre stampigliature uguali.

### Q204 · Hatshepsut
- **Periodo:** circa 1473–1458 a.C. **Luogo:** Tebe. **Pin:** Tebe. **Strato:** `S62`. **Attendibilità:** `D`.
- **Domanda:** il giorno in cui prendi il nome e la corona un oggetto cambia: che cosa succede ai suoi attributi?
- **Fonte:** le statue e i rilievi della sua cappella funeraria; **ricostruzione:** le raffigurazioni che la mostrano maschio, con la regalia di un faraone; **memoria:** la «maledizione di Hatshepsut», che è una legggeria ottocentesca.
- **Aggancio 4-4:** è il caso didattico più pulito di **attributi modificati dopo la costruzione**. Le sue immagini sono state cambiate due volte: dagli antichi, che la resero uomo, e dai moderni, che cancellarono il nome dalla lista dei faraoni. Il livello permette di chiedere che cosa succede a un oggetto quando qualcuno con accesso ne cambia gli attributi, e che cosa rimane dell'originale. **Forte.**
- **Motto:** «Un attributo non è la persona: ma chi lo modifica decide di chi è.» **Emblema:** due profili sovrapposti, uno con la corona piatta e uno con quella alta.

### Q205 · Akbar
- **Periodo:** 1542–1605. **Luogo:** Agra, Fatehpur Sikri. **Pin:** Agra. **Strato:** `S73`. **Attendibilità:** `D+I` (le sue scelte sono note soprattutto dalla descrizione favolosa di Abul Fazl).
- **Domanda:** un impero con mille lingue e mille divinità: fuori c'è una porta sola. Chi decide che cosa si vede?
- **Fonte:** l'*A'in-i Akbari*; **ricostruzione:** l'amministrazione e le sperimentazioni religiose; **memoria:** il sovrano tollerante, che è una semplificazione.
- **Aggancio 4-5:** l'incapsulamento è **un'interfaccia sola verso l'esterno e una complessità nascosta all'interno**. Akbar governa un impero in cui ognuno è più cose insieme; l'amministrazione espone pochi concetti comprensibili a tutti e tiene il resto dentro. **Medio**: il parallelo è suggestivo ma non documentato, e va raccontato come un'idea del gioco, non come una proprietà del personaggio. **Medio.**
- **Motto:** «Governare un impero è parlare una sola lingua e capirne mille.» **Emblema:** un cancello con una sola porta aperta su una città enorme.

### Q206 · Gengis Khan
- **Periodo:** 1162–1227. **Luogo:** Karakorum. **Pin:** Karakorum. **Strato:** `S68`. **Attendibilità:** `D+L` (il profilo è ricostruito da fonti cinesi, persiane e arabe; molte sue frasi sono leggende).
- **Domanda:** un impero che si eredita a voce, non su carta: che cosa passa, e che cosa si rompe?
- **Fonte:** le fonti esterne e la *Secret History*, di molto più tarda; **ricostruzione:** la divisione fra i figli del 1229; **memoria:** il conquistatore, che nel racconto popolare non nomina mai i popoli che si ribellano.
- **Aggancio 4-6:** l'**ereditarietà** non è qui un programma ma una promessa orale (*yassa*, attribuzione incerta: V7). Il livello permette un esperimento chiaro: un oggetto passa a un figlio, l'oggetto è lo stesso tipo, ma con campi diversi; e quando l'eredità è orale, **i campi non sono obbligatori**, quindi gli interpreti divergono. È il caso in cui l'ereditarietà **rompe** la promessa di trasmettere tutti gli attributi. **Forte.**
- **Motto:** «Il regno è come il cavallo: se lo spezzi, non lo hai più.» **Emblema:** quattro cavalli che tirano una sola carrozza.

### Q207 · Leibniz *(aggiunta — sostituisce Isaac Newton, spostato all'anno 5)*
- **Periodo:** 1646–1716. **Luogo:** Hannover, Londra, Parigi. **Pin:** Hannover. **Strato:** `S73`. **Attendibilità:** `D`.
- **Domanda:** due persone che non si sono mai incontrate costruiscono la stessa cosa: com'è possibile?
- **Fonte:** i *Cartegi* del 1676 e i *Principia*; **ricostruzione:** il calcolo; **memoria:** la disputa di priorità, che è durata più di un secolo e che nessuno dei due voleva.
- **Aggancio 4-7:** il **polimorfismo** e l'**interfaccia**: Leibniz voleva un linguaggio universale (*characteristica universalis*) in cui ogni idea fosse un simbolo calcolabile, e scoprì il calcolo indipendentemente da Newton. Due implementazioni diverse della stessa operazione, che convergevano perché descrivevano la stessa cosa. **Medio**, e il livello può mostrarlo in modo immediato: la stessa funzione scritta in due formalismi diversi dà lo stesso risultato.
- **Motto:** «Calcoliamo la stessa curva per strade diverse: il risultato è uguale.» **Emblema:** due fogli con lo stesso grafico e due grafemi diversi.

### Q208 · Carl Linneo
- **Periodo:** 1707–1778. **Luogo:** Uppsala, Stoccolma. **Pin:** Uppsala. **Strato:** `S73`. **Attendibilità:** `D+L` (le classificazioni sono documentatissime; il loro uso razzista è documentato, ma la sua responsabilità personale è molto discussa: V9).
- **Domanda:** il mondo diventa un disegno di caselle e linee. È una descrizione, o un verdetto?
- **Fonte:** il *Systema Naturae* e le edizioni successive; **ricostruzione:** il lavoro sul campo; **memoria:** il naturalista innocente, che non è mai esistito.
- **Aggancio 4-8:** il **diagramma delle classi** è nato per classificare il vivente: caselle (specie, generi), attributi, relazioni, tutto in un disegno che si può guardare e correggere. Linneo è il primo a produrre questo oggetto a scala del mondo. Il livello permette al giocatore di **modificare** il diagramma e di vedere che cosa succede quando chi classifica sceglie le caselle. **Forte.**
- **Motto:** «Ho ordinato il mondo in dodici regni. Nessuno mi aveva chiesto se volevo.» **Emblema:** una foglia con la sua nomenclatura binaria.

### Q209 · Mansa Musa
- **Periodo:** circa 1280–1337. **Luogo:** Niani, Timbuctù, Il Cairo, Mecca. **Pin:** Il Cairo. **Legame:** `A` (il fatto documentato del 1324 è la delegazione ricevuta al Cairo, dove l'oro fu distribuito; la capitale del Mali era Niani; Timbuctù è `S`, la grande città del Sahara, non attestata come tappa). V. `luoghi.md` §3.3, 3. **Strato:** `S69`. **Attendibilità:** `D+I` (il viaggio del 1324 è attestato; le cifre sull'oro sono molto gonfiate nelle fonti successive).
- **Domanda:** una catena di pozzi, e ogni pozzo indica il successivo: che cosa succede se ne salta uno?
- **Fonte:** le relazioni dei mercanti e del sultano del Marocco; **ricostruzione:** le rotte del sale e dell'oro; **memoria:** l'uomo che porta più oro di tutti.
- **Aggancio 4-9:** la **strada del sale** è una catena di punti in cui ogni punto vale solo se il successivo c'è, e vale in entrambe le direzioni: una **lista collegata**, con riferimenti che puntano oltre sé stessi. Il livello può far perdere un pozzo e vedere che cosa succede alla rotta. **Forte.**
- **Motto:** «Un pozzo vale quanto il pozzo dopo: se c'è, il primo vale il doppio.» **Emblema:** una catena di oche d'acqua legate da una corda.

### Q210 · Ercole II d'Este
- **Periodo:** 1508–1559. **Luogo:** Ferrara. **Pin:** Ferrara. **Strato:** `S72`. **Attendibilità:** `D`.
- **Domanda:** di settantacinque anni di duchi, quasi niente è rimasto. Che cosa manca, e chi l'ha perso?
- **Fonte:** l'archivio; **ricostruzione:** l'incendio del 1534, le riforme amministrative, l'interesse per la musica e per l'agricoltura; **memoria:** il duca che amava la musica, che è tutto ciò che in genere si dice di lui.
- **Aggancio 4-10:** la prova di corte dell'anno è **modellare l'archivio stesso**: che cosa si conserva, che cosa si butta, che cosa non si è mai pensato di conservare. Ercole II è il primo caso del gioco in cui **chi si trova dentro l'archivio non è il protagonista**: il duca è la guida, e la prova consiste nel mettere ordine in ciò che lui non ha scritto. **Forte.**
- **Motto:** «Io non ordino: registro. E quello che non registro domani non esiste.» **Emblema:** uno scaffale vuoto con un cartellino scritto a metà.

### Q211 · Al-Khwarizmi
- **Periodo:** circa 780–850. **Luogo:** Baghdad. **Pin:** Baghdad. **Strato:** `S67`. **Attendibilità:** `D`.
- **Domanda:** una procedura scritta perché la esegua qualcun altro: il primo programma è una regola in arabo.
- **Fonte:** il trattato di algebra e i manuali di calcolo; **ricostruzione:** l'ambiente di calcolo scientifico; **memoria:** l'uomo il cui nome è diventato una parola.
- **Aggancio 4-11:** un algoritmo è, alla sua origine, **una procedura scritta per essere eseguita da una persona diversa**, con esempi numerici. Il nome «algoritmo» viene dalla latinizzazione del suo nome: **il primo programma è anche un pacchetto di codice che ha fatto una volta il giro del mondo**. Il livello chiede di scrivere un linguaggio e un interprete, ed è qui che la parola ha già cent'anni. **Forte.**
- **Motto:** «Scrivo perché lo eseguano altri, e perché non debbano chiedermi il permesso.» **Emblema:** un foglio di calcolo con una colonna di numeri arabi.

### Q212 · Confucio
- **Periodo:** 551–479 a.C. **Luogo:** Qufu, Luoyang. **Pin:** Qufu. **Strato:** `S63`. **Attendibilità:** `D+I` (gli *Analects* sono una compilazione di generi successivi).
- **Domanda:** come trovi le parole in un testo che non ha né punti né virgole?
- **Fonte:** gli *Analects*; **ricostruzione:** il lessico cinese e i dizionari; **memoria:** il vecchio saggio che non scrisse nulla.
- **Aggancio 4-12:** la scrittura cinese classica **non aveva punteggiatura**, e i testi più antichi arrivano a noi con le frasi che il lettore deve ricomporre. Separare un testo in parole è un problema reale prima di poterlo cercare o tradurre: il livello 4-12 non è un esercizio inventato, è una difficoltà che si è davvero dovuta risolvere, e in un caso con centinaia di migliaia di simboli. **Forte.**
- **Motto:** «La mia frase più lunga è una conversazione, e non l'ho scritta.» **Emblema:** tre ideogrammi senza alcun segno di punteggiatura.

### Q213 · Ipazia
- **Periodo:** circa 350–415. **Luogo:** Alessandria. **Pin:** Alessandria. **Strato:** `S65`. **Attendibilità:** `D+L` (la sua opera di docente è documentata dai tardivi; la sua morte è nota da una fonte tarda e sola: V3).
- **Domanda:** tre scritture sulla stessa pietra e una sola frase: come si riconosce la stessa frase in tre lingue?
- **Fonte:** la stele di Rosetta; **ricostruzione:** la tradizione scolastica su Ipazia; **memoria:** la donna bruciata, che è un racconto di secoli dopo.
- **Aggancio 4-13:** la **stele di Rosetta** è il problema della grammatica nella forma più concreta: lo stesso testo in egiziano geroglifico, demotico e greco, e chi non leggeva i primi due poteva solo indovinare le regole. Chi sa il greco può **ricostruire** la grammatica di una lingua perduta. Ipazia è la voce della scuola che ha tenuto insieme quei tre mondi. **Medio**, e soprattutto: il livello 4-13 è anche un caso di fonti malissime, e va usato come esercizio di critica, non come biografia. **Medio.**
- **Motto:** «Non mi hanno ricordata per quello che ho insegnato, ma per quello che è successo dopo.» **Emblema:** un frammento di stele con tre righe di tre scritture diverse.

### Q214 · Moctezuma II
- **Periodo:** 1466–1520. **Luogo:** Tenochtitlán. **Pin:** Tenochtitlán. **Strato:** `S71`. **Attendibilità:** `D` (le fonti sono soprattutto spagnole, e quindi interessate: V18).
- **Domanda:** il trono si eredita dalla parte della madre: l'albero si percorre al contrario. Come ci si cerca dentro?
- **Fonte:** i registri tlaxcalteca e quelli spagnoli; **ricostruzione:** la successione e i tributi; **memoria:** l'imperatore che non vide niente.
- **Aggancio 4-14:** nei mondi mesoamericani la successione passa **per la linea materna**: l'albero dinastico non si percorre dal fiume alla chioma, ma dalla chioma verso il fiume. Il livello 4-14 chiede appunto alberi, visite ed evaluation: il giocatore può cercare una posizione in un albero e scoprire che **la direzione in cui si cammina cambia il risultato**. **Medio.**
- **Motto:** «L'albero si guarda dalla fronda: è lì che si comincia.» **Emblema:** un albero con le radici in alto e i rami verso il basso.

### Q215 · Omero
- **Periodo:** VIII secolo a.C. circa (personaggio composito, forse mai esistito). **Luogo:** Chio e la Ionia. **Pin:** Chio. **Strato:** `S64`. **Attendibilità:** `M` (la figura è letteraria; la tradizione è orale e la fissazione scritta è più tarda).
- **Domanda:** nessuno scrisse i poemi: li cantavano. Un testo senza pagina, che si esegue a voce?
- **Fonte:** l'oralità, ricostruita dai filologi; **ricostruzione:** la prima fissazione per iscritto, in un periodo di transizione; **memoria:** il cieco, che non è mai stato cieco.
- **Aggancio 4-15:** il livello chiede di **scrivere un interprete**, cioè un programma che esegue una descrizione. Il caso di Omero è l'esempio più anteno e più onesto di questo: un testo la cui esecuzione non è la lettura ma **il canto, con la variazione del rapsodo**. Un interprete che «esegue» un testo non ne esce mai identico. **Forte.**
- **Motto:** «Il testo non è quello che ho scritto: è quello che ho detto ieri sera.» **Emblema:** un rotolo senza parole, con una bocca e un ritmo.

### Q216 · Ibn Khaldun
- **Periodo:** 1332–1406. **Luogo:** Tunisi, Il Cairo, Fes. **Pin:** Tunisi. **Strato:** `S69`. **Attendibilità:** `D`.
- **Domanda:** davanti a sette generazioni dico che cambieranno. È una previsione, o ha letto i registri?
- **Fonte:** la *Muqaddimah* (1377); **ricostruzione:** il metodo: distinguere ciò che è proprio delle società da ciò che è proprio degli uomini; **memoria:** il filosofo isolato, a cui il destino fa incontrare un giovane spagnolo che lo copierà.
- **Aggancio 4-16:** il livello chiede che cosa si fa di un dato **dopo** averlo raccolto: lo si conserva, lo si elabora, lo si distrugge? Ibn Khaldun è il primo a dire che certe informazioni sono **delle informazioni** e che si possono raccogliere e ordinare come si ordina il resto: i dati su chi sia una popolazione e su come viva valgono più di un aneddoto. **Medio:** l'aggancio è concettuale e non ha un documento che lo sostenga; va costruito nel racconto, e va detto ai ragazzi che lo stiamo usando come esempio, non come documentazione.
- **Motto:** «La civiltà è un ciclo, e io ne ho visto quattro.» **Emblema:** una clessidra con dentro un nome.

### Q217 · B. R. Ambedkar
- **Periodo:** 1891–1956. **Luogo:** Bombay, Delhi. **Pin:** Bombay. **Strato:** `S74`. **Attendibilità:** `D`.
- **Domanda:** nati in una certa famiglia si eredita anche un mestiere e un posto dove sedersi. È una tabella?
- **Fonte:** *L'annullamento delle caste* (1936) e i testi costituzionali; **ricostruzione:** il movimento per l'apertura dei templi e la costituzione del 1950; **memoria:** il riformatore che ha salvato l'India, che è metà della verità.
- **Aggancio 4-17:** il livello chiede di costruire un modello E/R, cioè **entità, attributi e relazioni**. La caste è un modello E/R senza nessuna tabella: l'entità è la persona, gli attributi sono nati in una famiglia che ne eredita altri, e le relazioni sono regole che valgono per tutti e non si possono modificare da un utente. Il punto più forte è che Ambedkar **descrive** il sistema dall'esterno e lo scrive in un documento che si può leggere, discutere e cambiare. **Forte.**
- **Motto:** «La casta non è un attributo: è una tabella, e le tabelle si aprono.» **Emblema:** una griglia di caselle con una sola riga aperta.

### Q218 · Solimano il Magnifico
- **Periodo:** 1494–1566. **Luogo:** Costantinopoli. **Pin:** Costantinopoli. **Strato:** `S72`. **Attendibilità:** `D` (il concetto di *millet* è molto discusso fra gli storici: V21).
- **Domanda:** un impero in cui ognuno appartiene a più di una cosa: quante relazioni servono?
- **Fonte:** il *Kanunname* e gli archivi ottomani; **ricostruzione:** l'amministrazione, le moschee, le città; **memoria:** il sultano, che è un titolo.
- **Aggancio 4-18:** il livello chiede **cardinalità e vincoli**, cioè quante relazioni fra quante entità e quali regole che le tengono insieme. L'impero ottomano è il caso più grande e meglio documentato di una società in cui una persona è contemporaneamente cittadina, soggetta a un'autorità religiosa, membro di una professione e membro di una famiglia: la relazione non è «uno a molti», è **molti a molti**, e le regole sono tutte da costruire. **Forte.**
- **Motto:** «Il suddito non appartiene a una sola parte: appartiene a quattro, e le quattro non vanno d'accordo.» **Emblema:** quattro chiavi sulla stessa persona.

### Q219 · Ibn al-Haytham
- **Periodo:** circa 965–1040. **Luogo:** Bassora, Il Cairo. **Pin:** Il Cairo. **Strato:** `S67`. **Attendibilità:** `D`.
- **Domanda:** sei righe di misure per ogni luce: la tabella c'è, ma la chiave è una domanda.
- **Fonte:** il *Kitab al-Manazir* e il Libro degli specchi; **ricostruzione:** le tabelle di esperimenti sull'ombra e sulla rifrazione; **memoria:** l'uomo che ha capito la luce, che è un anacronismo.
- **Aggancio 4-19:** il livello chiede la relazione come tabella e le chiavi. Ibn al-Haytham costruisce **tabelle di valori misurati** con una colonna di condizioni (distanza, altezza) e una di risultati, e il suo problema è esattamente quello della chiave: **che cosa identifica una riga?** Una riga di misura non si identifica con l'oggetto, si identifica con la condizione in cui è stata presa. **Medio**, perché il salto è intellettuale ma non documentato a livello di tappa.
- **Motto:** «Non guardo il cielo: guardo l'ombra di una lancia e misuro quello che c'è.» **Emblema:** una lancia, una sombra e una griglia di numeri.

### Q220 · I censori
- **Periodo:** dal III secolo a.C. a oggi. **Luogo:** ovunque. **Pin:** Ferrara (ufficio del catasto). **Strato:** `S74`. **Attendibilità:** `C` (collettivo).
- **Domanda:** contare tutti: persone, case, botti. Qualcuno però si conta in un campo diverso dagli altri. Chi?
- **Fonte:** i moduli, i registri, le istruzioni; **ricostruzione:** la burocrazia fiscale; **memoria:** nessuna, ed è la lezione.
- **Aggancio 4-20:** la prova di corte dell'anno è **progettare uno schema E/R** e il compito è esattamente quello del censimento: decidere **che cosa è una persona**. Lo schiavo è una voce in una casa, il servo è una voce, il proprietario è una voce: lo stesso modulo, campi diversi, e la decisione è politica, non tecnica. **Forte.**
- **Motto:** «Il censimento non descrive il paese: lo decide.» **Emblema:** un modulo con due colonne e un nome che non c'è.

### Q221 · Isabella di Castiglia
- **Periodo:** 1451–1504. **Luogo:** Toledo. **Pin:** Toledo. **Strato:** `S71`. **Attendibilità:** `D` (le cifre del *padronamiento* sono discusse: V17).
- **Domanda:** per tassare un regno si fa un elenco di tutte le case. Qualcuno fa l'elenco di tutte le case.
- **Fonte:** i *padrones* generali (1494–1514); **ricostruzione:** la riconquista, la tassazione, la nascita dell'amministrazione regia; **memoria:** la regina che non governò, che è falso.
- **Aggancio 4-21:** il livello chiede di **passare da un modello concettuale a uno schema relazionale**, cioè di trasformare «una persona che sta in una casa che è in un paese» in tabelle con chiavi. Il *padronamiento* spagnolo è la versione più grande e più antica di questa operazione mai tentata in Europa: milioni di famiglie, con le case come unità, per poter riscuotere. E le carte finiscono in **un archivio che è ancora aperto** (Simancas). **Forte.**
- **Motto:** «Prima si conta la casa, poi la persona: era più comodo, e funzionava.» **Emblema:** una pianta di città con una casa cerchiata.

### Q222 · Hammurabi
- **Periodo:** circa 1792–1750 a.C. **Luogo:** Babilonia. **Pin:** Babilonia. **Strato:** `S61`. **Attendibilità:** `D`.
- **Domanda:** duecentottantadue frasi, e in ognuna un nome, un numero, un metallo. Si può dividere senza perdere niente?
- **Fonte:** la stele; **ricostruzione:** l'uso del diritto; **memoria:** il primo codice civile, che non è un codice.
- **Aggancio 4-22:** la **normalizzazione** chiede di eliminare la ripetizione: se «dieci shekel d'argento» compare in cento frasi, la si mette in una tabella sola e si rimanda. Ma il testo di Hammurabi **ripete di proposito**, perché ogni frase deve essere completa per chi la legge da solo. Il livello può mostrare la perdita: si guadagna struttura, si perde la frase autonoma. E c'è un episodio che riguarda la traduzione: nel 1952 la stele è stata riscritta in un'altra lingua, e ogni traduzione è una normalizzazione. **Forte.**
- **Motto:** «Se la legge è completa da sola, non ha bisogno di un articolo che la rimandi.» **Emblema:** una stele spezzata con righe di numeri.

### Q223 · Vasco da Gama
- **Periodo:** circa 1469–1524. **Luogo:** Lisbona, Malindi, Calicut. **Pin:** Lisbona. **Strato:** `S71`. **Attendibilità:** `D` (il racconto degli incontri in India è mediato da relazioni portoghesi).
- **Domanda:** una rotta che arriva in un porto che fa commercio da sempre: stai cercando il mondo, o stai cercando il tavolo?
- **Fonte:** le lettere di Alvise; **ricostruzione:** la rotta del 1497–1499; **memoria:** il navigatore che aprì le rotte, che erano già aperte.
- **Aggancio 4-23:** l'**algebra relazionale** finisce con il **join**: unire due tavole su una condizione, e il risultato dipende tutto da quella condizione. Vasco da Gama arriva a Calicut e scopre che il porto è pieno di navi, di merci e di credito, e che la flotta «scoprì» una cosa che esisteva da secoli: **la condizione del join era già scritta, la si era solo scritta in un'altra lingua.** Il materiale di Pietro lo dice esplicitamente (§32): per chi viveva in quelle reti gli europei erano nuovi arrivati. **Forte.**
- **Motto:** «Abbiamo navigato due anni per trovare un tavolo, e il tavolo era già apparecchiato.» **Emblema:** due reti che si toccano in un punto.

### Q224 · Zheng He
- **Periodo:** 1371–1433. **Luogo:** Nanchang, Nanjing, il mare. **Pin:** Nanchang. **Strato:** `S70`. **Attendibilità:** `D` (le cifre delle flotte sono discusse: V15).
- **Domanda:** quattrocento navi, ventisettemila persone, tre anni. Nessuno scrive una riga: come si fa?
- **Fonte:** il *Xingcha Shenglan* di Ma Huan; **ricostruzione:** le sette spedizioni; **memoria:** le navi enormi, di cui non si è trovata traccia.
- **Aggancio 4-24:** il livello chiede di **creare e modificare strutture**: il DDL. Zheng He comanda una struttura così grande che non può funzionare senza un registro: navi, equipaggi, carichi, rotte, e le **modifiche** a ogni tappa. E il livello può chiudere con il divieto di navigare del 1433: **la stessa struttura, chiusa** — come un archivio di cui si ordina la distruzione. **Forte.**
- **Motto:** «La flotta è grande abbastanza perché nessuno possa ricordarsela: meglio così.» **Emblema:** un registro con un pennello e l'onda su cui non c'è una riga.

### Q225 · Frederick Douglass
- **Periodo:** 1818–1895. **Luogo:** Maryland, Baltimora, Annapolis. **Pin:** Annapolis. **Strato:** `S74`. **Attendibilità:** `D`.
- **Domanda:** un elenco di persone in cui gli schiavi non ci sono. Come si fa a contarli senza contarli?
- **Fonte:** le clausole di fuga dei moduli federali e le *Narrative*; **ricostruzione:** il censimento degli Stati Uniti e che cosa vi compariva; **memoria:** l'oratore, che è vero e non basta.
- **Aggancio 4-25:** il livello chiede una **query**: selezionare, filtrare, ordinare. Douglass permette di vedere che **il filtro più potente è quello che esclude**: fino al 1850 il censimento americano non contava gli schiavi singolarmente, li registrava come numero, e li registrava in una colonna diversa. Un `WHERE` sbagliato produce un risultato falso senza nessun errore. **Forte.**
- **Motto:** «Il mio nome era in una colonna diversa, e la colonna si chiamava 'schiavi'.» **Emblema:** un foglio con una colonna senza nomi.

### Q226 · Hernán Cortés
- **Periodo:** 1485–1547. **Luogo:** Spagna, Tenochtitlán. **Pin:** Spagna. **Strato:** `S71`. **Attendibilità:** `D+I` (le lettere di Cortés sono propaganda, e lo sono dichiaratamente).
- **Domanda:** un impero di milioni non crolla per un esercito: crolla quando si unisce a un'altra tabella.
- **Fonte:** le lettere di Cortés; **ricostruzione:** le alleanze con Tlaccala e altri popoli; **memoria:** il traditore, che è una versione spagnola del 1519 e non ha le sue ragioni.
- **Aggancio 4-26:** il **join** è la cosa che decide il risultato. Nessuna Potenza militare del 1519 abbatte da sola l'Impero azteco; ciò che lo abbatte è **una condizione di unione** fra due tavelle: un piccolo esercito e una rete di popoli che avevano le loro ragioni per allearsi con lui. Il livello può far vedere al giocatore che **la stessa tabella, con una condizione di join diversa, dà un risultato completamente diverso**. **Forte.**
- **Motto:** «Non ho vinto la battaglia: ho trovato qualcuno che odiava chi stavo attaccando.» **Emblema:** due liste di nomi che si incrociano su un nome solo.

### Q227 · Florence Nightingale
- **Periodo:** 1820–1910. **Luogo:** Scutari, Costantinopoli, Londra. **Pin:** Scutari. **Strato:** `S74`. **Attendibilità:** `D`.
- **Domanda:** non basta sapere quante persone sono morte: bisogna sapere di che cosa, e in che mese.
- **Fonte:** le *Note* del 1858; **ricostruzione:** l'ospedale militare di Scutari e le condizioni igieniche; **memoria:** la donna con la lampada, che è un'immagine di giornale del 1855 e non un fatto.
- **Aggancio 4-27:** il livello chiede **aggregazioni e raggruppamenti**: raggruppare per causa e per mese. Il diagramma a ragnatela che Nightingale pubblicò nel 1858 fa esattamente questo, e mostra che la mortalità Byind era **molto più bassa** per le malattie prevenibili di quanto sembrasse guardando il totale dei morti. È la prima infografica che cambia una decisione politica. **Forte.**
- **Motto:** «Il numero dei morti era sbagliato; non sbagliato di molto, ma sbagliato nel modo che uccide.» **Emblema:** un diagramma a ragnatela con due rientranze.

### Q228 · George Orwell
- **Periodo:** 1903–1950. **Luogo:** Motihari, Londra, Barcellona. **Pin:** Londra. **Strato:** `S75`. **Attendibilità:** `D`.
- **Domanda:** un programma è un testo che si legge: ogni testo che arriva dall'esterno va letto come un ordine. Come?
- **Fonte:** il romanzo del 1949; **ricostruzione:** il lavoro alla BBC e la guerra di Spagna; **memoria:** il futuro, che è diventato il presente.
- **Aggancio 4-28:** il livello introduce l'**SQL injection** e la query costruita concatenando ciò che viene da fuori. Il caso è la versione più seria della stessa cosa: **il linguaggio che descrive è anche linguaggio che comanda**, e se non si distingue, chi scrive il testo decide che cosa farà chi lo esegue. Il gioco mostra le due cose insieme: il romanzo che inventa il meccanismo e il livello che lo implementa. **Forte.**
- **Motto:** «Il fatto, in bocca al potente, si trasforma in ordine.» **Emblema:** una riga di testo che letta come codice fa un'altra cosa.

### Q229 · Marie Curie
- **Periodo:** 1867–1934. **Luogo:** Varsavia, Parigi. **Pin:** Parigi. **Strato:** `S74`. **Attendibilità:** `D`.
- **Domanda:** i suoi quaderni sono ancora radioattivi: di chi sono i dati di una persona, e chi decide?
- **Fonte:** i quaderni di laboratorio e gli archivi; **ricostruzione:** le istituzioni scientifiche dell'epoca e la gestione dei rifiuti; **memoria:** la coppia, che era un lui e una lei.
- **Aggancio 4-29:** il livello chiede **privacy, GDPR e open data**. Curie è il caso limite: i suoi dati più preziosi sono nei quaderni, che sono materiale privato, e sono anche un bene pubblico che fa risalire le origini della fisica nucleare. Chi decide che cosa si apre, a chi, e con quali condizioni? **Forte.**
- **Motto:** «Ho passato la vita a misurare. Nessuno mi aveva detto che i miei appunti sarebbero rimasti radioattivi.» **Emblema:** un quaderno con una coperta di piombo.

### Q230 · Le persone che non hanno firmato
- **Periodo:** tutta la storia. **Luogo:** ovunque. **Pin:** Ferrara, la stanza senza finestre. **Strato:** `S75`. **Attendibilità:** `C` (collettivo).
- **Domanda:** trenta documenti, trenta righe. Chi non ha potuto scrivere la sua?
- **Fonte:** l'assenza stessa della fonte; **ricostruzione:** i nomi recuperati a posteriori; **memoria:** nessuna, ed è la lezione.
- **Aggancio 4-30:** la prova finale è **un database con trenta righe e un campo che resta vuoto**. Il gioco stampa il registro e chiede al giocatore di riempiere l'ultima riga: non c'è un nome, e non può esserci, perché quella persona non ha mai scritto. La tappa **non si risolve**: il gioco accetta che ci siano nomi inventati solo se il giocatore li marca come ipotesi, e chiede in cambio di sapere **quanti nomi servirebbero**. **Forte.**
- **Motto:** «Il registro è completo. Manca quasi tutto.» **Emblema:** una riga di registro vuota, con una matita accanto.

---

## 6. Il criterio: nessun personaggio è una figurina

*(materiale di Pietro, §§71–75 e §67–71 del secondo percorso, riformulato in regole operative — le regole sono quelle degli anni precedenti e valgono per tutti gli anni)*

### 6.1 La catena

```
PERSONAGGIO → FONTE → AZIONE → CONSEGUENZA → INTERPRETAZIONE → DOMANDA
```

Regola operativa: **ogni tappa deve mostrare almeno un punto in cui la catena si spezza.** Una tappa in cui la catena fila liscia è una tappa sbagliata. Nell'Anno IV la rottura ha un nome preciso e ricorrente, ed è **il documento**: quasi tutte le tappe si rompono nel passaggio fra la persona e la sua fonte, perché la fonte è di qualcun altro.

### 6.2 I tre livelli di fonte

| Livello | Che cos'è | Come si mostra nel gioco |
|---|---|---|
| **1. La fonte dell'epoca** | una tavoletta, un papiro, un'iscrizione, un registro, una lettera, un diagramma, una fotografia, un discorso | il **documento** che entra dalla porta e che va catalogato |
| **2. La ricostruzione dello storico** | che cosa possiamo ragionevolmente concludere dalle fonti | la **scheda**, con i gradi di attendibilità e le parti ignote |
| **3. La memoria successiva** | come è stato raccontato quel personaggio | la **terza carta**, spesso in contrasto con la seconda, e da cui si parte per la domanda |

> **una fonte non è soltanto qualcosa che conferma una risposta: è qualcosa che deve poter essere interrogato.**

### 6.3 Le funzioni del personaggio nel gioco

Le sei funzioni del materiale diventano sei **tipi di tappa**, dichiarati nella scheda:

| Funzione | Che cosa fa nel gioco | Esempio nell'anno 4 |
|---|---|---|
| **Testimone** | il giocatore incontra chi ha visto o saputo | Vasco da Gama (4-23), Ibn Battuta (4-2) |
| **Contraddittore** | due documenti dicono la cosa opposta | Ipazia (4-13) e la tradizione della sua morte; Douglass (4-25) e il censimento |
| **Fonte** | il giocatore riceve un testo e deve capire che tipo è | Al-Khwarizmi (4-11), Ibn al-Haytham (4-19), i censori (4-20) |
| **Falsa certezza** | una figura circondata da leggende | Omero (4-15), Mansa Musa (4-9), Zheng He (4-24), le «navi enormi» |
| **Ponte geografico** | la risorsa che permette di spostarsi | tutte le tappe: la porta da cui entra |
| **Ponte temporale** | una persona ricordata secoli dopo | Moctezuma II (4-14), Gengis Khan (4-6) |

### 6.4 I ritorni: la stessa persona, un'altra voce

*(aggiunta — problema più grave che negli anni precedenti, perché il materiale del quarto anno contiene molti nomi già obbligatori nei primi tre anni)*

Con quattro anni di percorso, alcune persone **compaiono due volte**. Non è un difetto, è una risorsa, purché valgano tre regole:

1. **mai la stessa scheda, mai la stessa domanda, mai lo stesso livello**;
2. **la seconda volta la voce è un'altra**: nell'Anno I la persona è la voce del suo luogo, nell'Anno II una porta su un problema, nell'Anno III una risorsa che arriva in corte, nell'Anno IV **un documento da catalogare**;
3. **il ritorno deve essere annunciato**, e il gioco deve dire «questa persona l'hai già incontrata».

**Il problema specifico di quest'anno.** Il materiale del percorso I contiene nomi già obbligatori in passato, e sono molti. La regola degli anni precedenti dice che **nessun personaggio può essere obbligatorio in due anni**. Questi nomi, quindi, **non possono diventare le 30 voci dell'anno 4**, e vanno o in facoltativa o in atlante:

| Personaggio nel materiale | Già obbligatorio in | Destinazione nel quarto anno |
|---|---|---|
| Omero, Pericle, Platone, Alessandro Magno, Cesare, Augusto, Marco Aurelio, Costantino, Agostino, Giustiniano | Anno II e III | facoltative o «confronto» (le tappe di Pericle e Alessandro sono citate nei confronti) |
| Maometto, Carlo Magno, Marco Polo, Vesalio, Galileo, Copernico, Leonardo, Gutenberg, Colombo | Anno II e III | facoltative; **Leonardo** compare come voce al §34 del materiale: va tenuto come richiamo, non come tappa |
| Ötzi | Anno II (2-1) | facoltativa della 4-1, come voce dello strato `S60` vuoto |
| Ercole I | Anno II (protagonista) | citato nella 4-10 come padre; **Ercole II è il figlio e l'ingresso dell'anno** |
| Guglielmo di Ferrara, Leon Battista Alberti, Biagio Rossetti | Anno II | richiami |

**Vincolo.** Nessuno di questi può essere obbligatorio nel quarto anno. È il rispetto più importante della regola, e va verificato voce per voce quando i dati verranno generati in `dati/`.

*(proposta)* Il lato positivo è che il quarto anno può **citarli senza spese**: il confronto fra Confucio e Socrate, o fra Gandhi e Martin Luther King, è materiale del primo percorso e funziona come richiamo a schede già viste. Il gioco può anche **direglielo**: «questa persona l'hai incontrata al livello 2-18: adesso la vedi da un'altra parte».

### 6.5 Il catalogo dei personaggi

*(materiale di Pietro: 75 + 78 voci, in forma di catalogo)*

Codici `Q` proposti: la serie continua da quella dell'Anno III (Q101…Q130) con **Q201…Q230** per i 30 obbligatori, e un blocco separato per il catalogo esteso. Colonne: codice · nome · periodo · luogo/pin o porta · strato · la domanda · attendibilità · destinazione.

**Destinazione**: `4-n` = obbligatorio alla tappa 4-n; `f` = facoltativo; `atl` = atlante; `a5` = candidato all'anno 5 (Alfonso II, v. `curricolo.md` §4).

**Problemi interni del materiale**, che vanno risolti in catalogazione:

| Voce nel materiale | Problema |
|---|---|
| §36 e §44 Akbar | lo stesso personaggio due volte; il materiale lo dichiara **voluto** (la seconda ripresa è sul pluralismo). Diventa una scheda sola e un confronto |
| §45 e §48 Galileo | lo dichiara **voluto**: il secondo passaggio è sulle tradizioni della conoscenza. Scheda sola + confronto |
| §22 Avicenna, §51 Al-Khwarizmi, §49 Ibn al-Haytham e le rispettive voci del percorso II | gli stessi compaiono nel percorso II dentro gli elenchi tematici: non sono duplicati, sono **usi diversi**. Catalogati una volta sola |
| §66 Gagarin, §67 Armstrong, §68 Berners-Lee, §69 Malala, §63 Mandela, §64 King, §65 Maathai, §70 «le persone del presente» | tutti nel primo Novecento e oltre: **diventano il blocco `atl`**, perché i livelli dell'anno non arrivano al presente (§0.3 c) |
| «Confucio» nel percorso I e nel percorso II | coerente: una sola voce, due funzioni |
| «Elisabetta I» (§46) e «Queen Victoria» (§47) | **incoerenza di lingua nel materiale**: la seconda va resa «**Vittoria**», coeremente con «Elisabetta I» |

Criteri di scheda: identici a quelli degli anni precedenti, più i due campi obbligatori di quest'anno — **`funzione`** (testimone, contraddittore, fonte, falsa certezza, ponte geografico, ponte temporale: §6.3) e **`porta`** (come il documento entra: §3.4).

---

## 7. L'archivio che il giocatore costruisce

*(aggiunta — il deliverable dell'anno, e la cosa che rende il percorso diverso dai tre precedenti)*

### 7.1 Che cosa cambia rispetto all'Anno III

| | Anno III | Anno IV |
|---|---|---|
| Che cosa entra in sala | una risorsa (un libro, un dipinto, una nave) | **un documento** (una tavoletta, un registro, una lettera) |
| Che cosa fa il giocatore | la guarda e la esamina | **la cataloga** |
| Che cosa resta | la scheda del personaggio | **la riga del registro** |
| La guida | commenta l'arrivo | **registra**: chiede «a chi serve?» |
| Che cosa produce il giocatore | schede | **un archivio con dentro trenta documenti** |

### 7.2 Il registro: i campi, e perché sono quelli

Ogni tappa deposita **una riga** in un registro che il giocatore costruisce. I campi sono dichiarati dal gioco, non dal giocatore, perché sono la parte didattica:

| Campo | Che cosa ci mette | Perché esiste |
|---|---|---|
| `id` | l'ordine di arrivo in archivio | il gioco non è cronologico: l'id è l'ordine dei livelli, e il giocatore lo vede |
| `titolo` | il nome del documento | l'oggetto che si cerca |
| `autore` | chi lo ha scritto, **quando lo si sa** | quasi sempre la casella più difficile da riempire |
| `data` | la data del documento | una data che non si conosce resta `null` |
| `luogo` | dove è stato prodotto | il luogo è una delle due dimensioni della mappa |
| `strato` | lo strato della colonna | l'altra dimensione |
| `porta` | da dove è entrato | **la mediazione è visibile** |
| `tradotto_da` | chi l'ha tradotto o copiato, se lo si sa | il livello 4-17 chiede esattamente questo campo |
| `manca` | che cosa non c'è nel documento | il campo che rende il gioco onesto |
| `attendibilita` | `D`, `I`, `M`, `L`, `F`, `C` | le codifiche dell'Anno I |

I campi `tradotto_da` e `manca` sono **l'innovazione del quarto anno**, e sono anche la risposta alla domanda con cui il materiale chiude (§75): *chi ha scritto la fonte, quando, per chi, con quale scopo, che cosa racconta e che cosa omette.*

### 7.3 Perché funziona, e che cosa costa

**Funziona** perché rende visibile il filo del percorso: dopo trenta tappe il giocatore ha in mano **un oggetto costruito con le proprie mani** in cui ogni riga ha una fonte, e il motivo per cui l'ha costruito è la domanda dell'anno. E funziona perché i livelli 4-16…4-29 sono esattamente la costruzione di quel registro: E/R, tabelle, normalizzazione, algebra relazionale, SQL, query parametriche, privacy. Il gioco non **illustra** il percorso di un anno: lo **usa**.

**Costa** due cose, e vanno dette.

1. **Il giocatore non vede il mondo, vede i documenti del mondo.** È la scelta giusta per quest'anno, ma è una perdita di concretezza: negli anni II e III il paesaggio cambiava. Qui l'unica mappa che cambia è la colonna degli strati. La compensazione è la pianta del pianeta, che resta visibile alle spalle dell'archivio e su cui il gioco marca il punto da cui arriva ogni documento.
2. **Le prime dieci tappe non hanno ancora un registro.** Fino alla 4-10 si costruiscono le classi e non le tabelle: il registro esiste a partire dalla 4-16. Va detto ai ragazzi, altrimenti la prima metà sembra un'altra cosa. *(proposta di mitigazione)* Si può stampare un **registro provvisorio** di carta alla fine della 4-10, con le prime dieci voci in forma di schede sciolte, e incollarlo alla parete dell'archivio: da lì in poi il registro ha due parti, e alla 4-30 si uniscono.

---

## 8. Le domande del quarto anno

*(materiale di Pietro: §§40–75 del primo percorso e §§40–78 del secondo)*

| # | Domanda | Il gioco non chiede | Il gioco chiede | Dove |
|---|---|---|---|---|
| 1 | Che cosa sappiamo davvero di un mondo che non esiste ancora? | «Gutenberg ha stampato nel 1450» | «Che cosa c'era in quella stampa, e chi l'ha scritta?» | 4-1, 4-11, 4-16 |
| 2 | Una legge è giusta perché è legge? | «Hammurabi ha fatto il primo codice» | «A chi serve, e chi ci guadagna?» | 4-22 |
| 3 | La filosofia è nata in Grecia? | «Confucio ha fondato il confucianesimo» | «Chi si è posto la stessa domanda, e in che anno?» | 4-12, 4-11, 4-19 |
| 4 | Un impero si può governare dall'esterno? | «Alessandro ha conquistato l'Asia» | «Chi ha accettato, e con quale scambio?» | 4-5, 4-6, 4-18 |
| 5 | La memoria storica si può manipolare? | «Hatshepsut è stata cancellata» | «Chi ha cancellato, quando, e con quale diritto?» | 4-4 |
| 6 | Un nome è una persona? | «Omero ha scritto l'Iliade» | «Quante persone hanno contribuito a un solo nome?» | 4-15 |
| 7 | «Democrazia» significa la stessa cosa in ogni epoca? | «Pericle ha inventato la democrazia» | «Chi era dentro e chi era fuori?» | 4-20, 4-21 |
| 8 | La religione è un fatto privato? | «Akbar ha costruito un impero tollerante» | «Chi decide il confine fra le religioni?» | 4-5, 4-18 |
| 9 | Un impianto può fondare una dinastia? | «I moghul governavano l'India» | «Come si tiene insieme una società con mille lingue?» | 4-5, 4-12 |
| 10 | Chi ha avuto accesso alla conoscenza? | «Marie Curie ha vinto il Nobel» | «Chi non ha potuto nemmeno provare?» | 4-19, 4-29 |
| 11 | Esplorare significa scoprire? | «Colombo ha scoperto l'America» | «Chi ci stava già, e che cosa aveva costruito?» | 4-23, 4-24 |
| 12 | Una conquista è una caduta? | «Gli spagnoli hanno conquistato il Messico» | «Perché un impero di milioni è crollato in pochi anni?» | 4-26, 4-14 |
| 13 | Che cosa succede quando le popolazioni si spostano? | «L'Europa si è popolata» | «Chi si è spostato, e chi è rimasto?» | 4-2, 4-25 |
| 14 | Una classificazione scientifica resta neutra? | «Linneo ha classificato gli esseri umani» | «Chi ha usato quelle caselle, e per che cosa?» | 4-8, 4-17 |
| 15 | Più comunicazione significa più conoscenza? | «Oggi siamo tutti collegati» | «Come si verifica ciò che arriva?» | 4-28, 4-27 |
| 16 | La storia ha un centro? | «L'Europa ha fatto la modernità» | «Che cosa c'era fuori, e chi non lo scriveva?» | 4-9, 4-10, 4-30 |

**Nota.** Le domande 12, 14 e 16 sono le più difficili, e sono quelle che il materiale di Pietro mette al centro (§48, §69, §72). Le tre tappe che le sostengono sono **4-26, 4-8 e 4-30**, e la 4-30 è anche la prova finale. Sono le tre da costruire per prime, anche se sono le ultime.

---

## 9. Il ritorno, e la differenza temporale

Alla fine del quarto anno il giocatore ha stampato trenta righe e ha visto che il mondo è molto più grande di quanto il suo archivio riuscisse a contenere: perché il suo archivio è fatto di **trenta voci**, e il mondo no.

**Nel gioco:** la tappa 4-30 riporta il giocatore alla sala dell'archivio, e da lì si apre **il registro completo**. La domanda finale non è «che cos'è il mondo» ma:

> **questo registro è la storia del mondo, o è la storia di chi ha scritto?**

**La differenza temporale** è la regola portante dell'anno, ed è scritta nel motore, non nella prefazione:

- il **giocatore** sa che arriveranno l'Impero britannico, la schiavitù, il$Novecento, Internet;
- **Ercole II non sa quasi niente** di tutto questo, e lo dice: alla 4-28, quando un documento arriva e dice «1936», Ercole non ha niente da dire, e il gioco scrive: «Ercole è morto da oltre tre secoli. Questo documento non è per lui»;
- i **personaggi dei documenti** non sanno niente gli uni degli altri, e questo vale anche quando sono vissuti nello stesso secolo: Qin Shi Huang non sa di Confucio, Confucio non sa di Qin Shi Huang.

Ne segue la regola operativa che chiude l'anno:

> **nessuno vive il passato sapendo quale sarà il futuro. Il giocatore lo sa, e questa è la ragione per cui può giocarci.**

La differenza rispetto all'Anno III è che qui la regola ha un **corpo materiale**: il futuro di cui Ercole non sa è finito dentro il suo archivio, e ci è finito **per mano di chi l'ha scritto**. Ercole non ignora il Novecento: l'ha in casa, in un cassetto, e non lo aprirà.

---

## 10. La conclusione del quarto anno

L'anno deve chiudere con una domanda, non con una data. Il materiale di Pietro la formula così, e va tenuta:

> **quando due persone appartenenti a mondi diversi si incontrano, chi decide quale delle due storie è quella «vera»?**

In gioco, la domanda si pone in tre modi concreti:

1. **all'inizio**, quando il giocatore scende nella colonna e vede che gli strati si somigliano: la continuità **sembra** naturale, e non lo è;
2. **alla fine di ogni tappa**, quando il documento viene archiviato e resta una riga: di tutto quello che era arrivato, **è rimasto un riassunto di qualcuno**;
3. **alla fine dell'anno**, quando il registro si stampa e una riga è vuota: nessuno di quei trenta documenti era previsto da chi ci viveva.

La lezione conclusiva del materiale (§77) è che **il mondo non era inevitabile**, e va tradotta in una meccanica: la tabella che il giocatore ha costruito **potrebbe essere stata diversa**. Le colonne scelte, i campi scelti, i nomi esclusi sono tutte decisioni, e tutte hanno conseguenze. Un giocatore che ha scritto il registro in modo diverso ha scritto una storia diversa del mondo, e il gioco glielo dice.

---

## 11. Temi sensibili e regole di contenuto

*(coerente con `anno1-ferrara.md` §8, `anno2-penisola.md` §11 e `anno3-europa.md` §11)*

Il quarto anno è l'anno più difficile del progetto: porta **schiavitù, conquista, colonialismo, razzismo, sessismo, religione e propaganda**. Le regole vanno scritte **prima** delle schede, e sono le seguenti.

| Tema | Dove | Regola proposta |
|---|---|---|
| **Schiavitù** | 4-25, 4-26, 4-30 | Douglass è la voce principale e la sua voce è **dentro** il sistema che descrive; nessuna scena di violenza; la schiavitù non si riduce a un numero di trasportati, ma a **quali righe mancano** (4-30) |
| **Conquista e colonizzazione** | 4-14, 4-21, 4-23, 4-26 | **non esiste un solo punto di vista**: ogni tappa di conquista ha almeno una voce che è stata conquistata (Tlaxcala, i piloti di Malindi, i tributi di Moctezuma). Cortés è introdotto **con le sue stesse lettere**, che sono propaganda dichiarata |
| **Razzismo** | 4-8, 4-17 | Linneo è presentato **con il suo schema e con i suoi limiti**; la scheda deve dire che la classificazione non prova niente e che il suo uso successivo è stato politico. Ambedkar è la risposta: un sistema di relazioni descritto da chi lo subiva, e poi cambiato |
| **Genere** | 4-4, 4-29, 4-30 | le donne dell'anno sono tre (Hatshepsut, Ipazia, Marie Curie) e sono tutte presenti **per il loro lavoro**, mai come eccezione da sante da museo; la domanda 10 di §8 è dedicata a chi non ha potuto nemmeno provare |
| **Religione** | 4-5, 4-12, 4-18 | le religioni sono **sistemi sociali**, non verità; il gioco non prende posizione su nessuna e le desc tutte con lo stesso trattamento |
| **Propaganda** | 4-26, 4-27, 4-28 | la propaganda è mostrata come **tecnica**, non come cattiveria: le lettere di Cortés, il ritratto di Nightingale del 1855, il romanzo di Orwell sono tre casi in cui l'immagine pubblica è costruita. Il gioco non usa nessuna di queste immagini come se fosse un fatto |
| **Persone senza nome** | 4-30, e tutte | è **il tema dell'anno**. Ogni tappa che registra una voce deve chiedersi chi non è stato registrato; e la 4-30 esiste per questo |
| **Persone viventi** | catalogo | nessuna persona vivente entra nel percorso giocabile: solo emblemi, e solo in atlante (§13, Q6) |

---

## 12. Anacronismi e dati da verificare

*(come in `anno1-ferrara.md` §11: si segnala, non si corregge)*

| # | Voce | Che cosa va verificato |
|---|---|---|
| **V1** | **Q210 — Ercole II d'Este** | **verifica prioritaria.** Date (1508–1559); l'incendio di Ferrara del gennaio 1534 e che cosa dell'archivio perdette; il matrimonio con Renée di Francia (1548) e la sorte dei figli; l'introduzione del mais, del riso e della canna da zucchero; il patronato musicale (Cipriano de Rore, Giaches de Wert) e il rapporto con il caso del «bambino mostruoso» del 1537; la spedizione ferrarese del 1556 a Szigetvár |
| **V2** | Q213 — Ipazia | Le fonti sulla sua morte sono poche e tarde (Damascio, via Fozio): **non usare il racconto della folla come fatto**. Verificare che cosa dice la tradizione scolastica e che cosa le fonti antiche |
| **V3** | Q204 — Hatshepsut | La cancellazione delle immagini è **doppia**: parte antica, parte novecentesca (i nomi rimossi dalla lista dei faraoni). Verificare le due date, perché la domanda della tappa dipende da questo |
| **V4** | Q203 — Qin Shi Huang | La *piccola scrittura*; l'unità di misure e larghezze; l'incendio dei libri del 213 a.C. e che cosa dice davvero la fonte (memoriale di Li Si) |
| **V5** | Q212 — Confucio | Gli *Analects* sono una compilazione di epoche diverse; verificare che cosa è attribuito a Confucio e che cosa no. La scrittura cinese classica **senza punteggiatura**: verificare che cosa c'era nei manoscritti e quando entrò la punteggiatura |
| **V6** | Q206 — Gengis Khan | L'attribuzione della *yassa* è discussa: **non presentarla come un testo scritto**. La divisione del 1229 e le quattro parti; la *Secret History* è di molto più tarda |
| **V7** | Q208 — Linneo | L'edizione esatta in cui compaiono le varietà di *Homo sapiens* (la 10ª del 1758?): **verificare**, perché è l'errore più diffuso. E verificare con cura la vicenda del viaggio con le navi degli schiavi, che è essa stessa contestata |
| **V8** | Q209 — Mansa Musa | Le cifre sull'oro sono gonfiatissime nelle fonti successive: verificare che cosa è attestato nel 1324 e che cosa è leggenda |
| **V9** | Q211 — Al-Khwarizmi | La latinizzazione del nome che dà «algoritmo» (al-Khwarizmi → Algoritmi); la traduzione latina di Robert of Chester (1145) |
| **V10** | Q202 — Ibn Battuta | La *Rihla* è dettata a Ibn Juzayy per il sultano: il testo ha una finalità politica. Verificare che cosa è dubbio (l'India, il Mali) e che cosa è attestato |
| **V11** | Q216 — Ibn Khaldun | La *Muqaddimah* (1377) e la struttura dei cicli (*ʿasr*); verificare che cosa dice davvero, perché l'aggancio 4-16 è concettuale e non può poggiare su una frase generica |
| **V12** | Q215 — Omero | La questione omerica e la teoria della formula orale (Parry-Lord); verificare che cosa è una ricostruzione filologica e che cosa tradizione |
| **V13** | Q218 — Solimano | Il concetto di **millet**: è discusso fra gli storici, non usarlo come dato acquisito. Il *Kanunname*, le moschee, la datazione |
| **V14** | Q217 — Ambedkar | *L'annullamento delle caste* (1936); il movimento per l'apertura dei templi (1935, Nashik); i diritti fundamentali della Costituzione del 1950; verificare la frase che si vuole citare |
| **V15** | Q214 — Moctezuma II | La **successione matrilineare**: verificare la regola e le sue eccezioni. I registri dei tributi, l'arrivo di Cortés (1519), il vaiolo a Tenochtitlán (1520) e le cifre, che sono tutte stime |
| **V16** | Q221 — Isabella di Castiglia | Il *padronamiento* 1494–1514: le cifre delle famiglie sono discusse. E l'archivio di Simancas: che cosa si conserva e come è accessibile |
| **V17** | Q222 — Hammurabi | La stele (ritrovata a Susa, 1901), il numero di disposizioni, il prologo e l'epilogo, e **la ritraslazione in accadico del 1952**: ogni traduzione è una normalizzazione, e va detto |
| **V18** | Q224 — Zheng He | Il numero e le dimensioni delle navi sono discusse; il *Xingcha Shenglan* di Ma Huan come fonte primaria; il divieto di navigare del 1433 e il suo effettivo grado |
| **V19** | Q223 — Vasco da Gama | Il ruolo dei piloti di Malindi e la loro dipendenza dalla corona di Vasco: è il punto del §32 del materiale e va verificato con precisione, perché è la differenza fra «scoperta» e arrivo |
| **V20** | Q225 — Douglass | Che cosa contava davvero il censimento degli Stati Uniti e **da quale anno** gli schiavi comparivano singolarmente (1850?): è la prova dell'aggancio |
| **V21** | Q226 — Cortés | Le alleanze con Tlaccala e altri; le lettere come propaganda; la vicenda delle navi (varata, incagliata o bruciate, e quando) |
| **V22** | Q227 — Nightingale | Le *Note* (1858), il diagramma del 1858 (la pubblicazione è del 1859?); il ritratto del 1855 e come nacque come immagine pubblica; i numeri di mortalità all'ospedale di Scutari |
| **V23** | Q229 — Marie Curie | I quaderni e il loro stato (perché sono radioattivi); le date dei due premi (1903, 1911); il rifiuto dell'Accademia; la legge sul radioattivo |
| **V24** | Q228 — Orwell | Il romanzo (1949), la sua attività alla BBC, la guerra di Spagna, la sua morte (1950). Verificare **quale** meccanismo del romanzo si vuole citare, e che cosa è invenzione letteraria |
| **V25** | Q230 — le persone che non hanno firmato | La tappa non ha una fonte: verificare che gli **esempi** che si useranno siano documentati (un nome di schiavo noto solo da un documento del 1850, ecc.) |
| **V26** | In generale | ogni **porta** (§3.4) è una scelta narrativa: verificare che il documento potesse davvero arrivare a Ferrara in quel modo, in quegli anni, con quei tempi |
| **V27** | In generale | diritti e immagini: `FONTI-E-LICENZE.md` è vincolante. Verificare voce per voce, soprattutto per 4-8 (illustrazioni del *Systema Naturae*), 4-27 (il diagramma del 1855–58, pubblico dominio ma con prove successive) e 4-14 (immagini dei siti mesoamericani) |
| **V28** | In generale | il materiale contiene **superlativi** («il più grande impero territoriale contiguo») che vanno verificati o addolciti: regola del progetto, nessun superlativo senza fonte |

---

## 13. Questioni aperte

*(da decidere con Pietro)*

1. **Il buco di `S66`.** India e Asia meridionale dal 300 a.C. al 1200 non hanno tappa obbligatoria, e nel materiale sono due voci forti: Buddha e Ashoka. Le opzioni: **(a)** sostituire una delle 30 tappe con Ashoka (candidati: i sei «medi»); **(b)** tenere i 30 e portare Buddha e Ashoka in facoltativa forte e atlante; **(c)** aggiungere un **dialogo di confronto** in 4-12 (Confucio) e in 4-3 (Qin Shi Huang), dove la tappa è la cinese e il confronto è l'India. La mia proposta è **(a)**: un anno che si chiama «il mondo oltre l'Europa» e lascia fuori l'Asia meridionale antica è un anno che ripete l'errore che dice di combattere.
2. **Il presente.** Le tappe arrivano al 1900-1950 e si fermano (4-28). Berners-Lee, Mandela, Malala, Gagarin sono in facoltativa e in atlante. Va deciso se l'anno 4 accetta questo limite (la risposta del **principio zero**: il presente non è ancora conosciuto) o se almeno due di questi entrano come facoltative forti nei livelli 4-11 e 4-29, che sono i più adatti (Internet e dati personali).
3. **La regola dei due collettivi.** Il quarto anno ha due voci senza nome (i censori e le persone che non hanno firmato). Sono la parte più forte del percorso e anche la più difficile da scrivere bene. Va deciso se sono **due tappe** o se la 4-30 le unisce in una sola con dentro entrambe le voci.
4. **I tre agganci «forti» da rivedere.** 4-8 (Linneo), 4-9 (Mansa Musa) e 4-24 (Zheng He) sono forse **troppo** ovvii: il livello sembra fatto per la persona. Segnalo questi tre in particolare; 4-22 (Hammurabi) e 4-27 (Nightingale) mi sembrano i due più solidi.
5. **I codici `Q`.** Proposta: la serie continua con **Q101…Q130** → **Q201…Q230**. Alternativa: `R01…R30`. Va confermata una volta sola, perché da qui in poi la numerazione è nel repository.
6. **Le persone viventi.** Nessuna entra nel percorso. Resta il problema, già segnalato nell'Anno III, di che cosa fare del presente.
7. **La tappa 4-10 e l'incendio.** Se V1 conferma che dell'archivio ducale si è perso molto nel 1534, quella è la prova più forte della tesi dell'anno e va nella tappa 4-10 come fatto. Se non si conferma, la tappa resta, ma il materiale è solo un'inferenza e va detto.
8. **Le fonti del materiale.** Come per gli anni II e III, il materiale è ricco e non è stato ancora consultato sistematicamente. Serve un abbozzo di bibliografia per i 30 obbligatori prima della stesura delle schede in `dati/`.

---

## 14. Cosa c'è da fare

1. **Decidere Q1** (il buco dell'Asia meridionale antica) e **Q2** (il presente). Le altre scelte dipendono da queste.
2. **Verifiche storiche** (§12): V1 (Ercole II), V2 (Ipazia), V3 (Hatshepsut), V7 (Linneo), V8 (Mansa Musa), V15 (Moctezuma), V20 (il censimento) sono le sette che cambiano una scheda se sbagliate.
3. **Revisione degli agganci forti**: 4-8, 4-9, 4-24 con Pietro (§13, Q4).
4. **Aggiornare `AGENTS.md`** §3 con la sezione «Anno 4» (il luogo è l'archivio; il documento è l'unità di gioco; la guida registra).
5. **Generare i dati** in `dati/`:
   - `videogioco-5-duchi-anno4-mondo.json`: 30 tappe con livello, argomento, strato, pin, porta, tipo di documento, funzione del personaggio, forza, confronto (voce del percorso II), rimando, facoltativi;
   - `videogioco-5-duchi-anno4-personaggi.json`: le 30 schede obbligatorie più il catalogo esteso (§6.5);
   - `videogioco-5-duchi-anno4-porte.json`: le sette porte (§3.4);
   - `videogioco-5-duchi-anno4-registro.json`: **i campi del registro** (§7.2), che è il deliverable dell'anno e va progettato per primo, perché tutto il resto dipende da lui.
6. **Carta del pianeta**: open data, con attribuzione. Servono coste, deserti, fiumi, catene e oceani; e va deciso **su quale proiezione** si mette «l'India antica» o «l'Africa occidentale», che sono le stesse difficoltà del documento Anno III.
7. **Prima tappa completa** (4-1, Gilgamesh a Uruk), sul modello di `videogioco-5-duchi-tappa-1-01.md`, con l'ingresso del documento dalla `PT-SCR` e il commento di Ercole.
8. **Aggiornare `README.md`**: tabella dei documenti e «da fare».

---

## 15. Registro modifiche

- **v0.4 (02/10/2026)**: controllo di coerenza su tutto il progetto. Il testo non cambia: due rimandi di versione erano fermi (`anno1-mappa.md` v0.8, `gioco.md` v0.4).

- **v0.3 (01/10/2026)**: applicazione della **regola dei luoghi** (`luoghi.md` §3.3, 3). Il pin della tappa 4-9 passa da **Timbuctù** a **Il Cairo**, dichiarato di tipo `A`: il fatto documentato del 1324 è la delegazione ricevuta al Cairo, dove l'oro fu distribuito, e la capitale del Mali era Niani. Timbuctù non è attestata come tappa del viaggio e resta come **luogo simbolico `S`**. Cambia la riga della tabella delle tappe, il pin e il tipo di legame nella scheda Q209 e la nota accanto alla nona domanda. Nessun aggancio cambia forza (4-9 resta **forte**) e i conteggi del documento non cambiano. Era la verifica **V13** di `luoghi.md`.

- **v0.2 (01/10/2026)**: la scheda **4-7 passa da Isaac Newton a Leibniz**, che entra come *aggiunta*. Motivo: il livello 5-3 dello schema dei livelli si chiama «il metodo di Newton», e l'anno 4 non può tenere lo stesso personaggio come obbligatorio in due anni (regola §6.4). Newton non scompare: diventa il **rimando** di 4-7 ed è il personaggio obbligatorio della tappa 5-3 dell'anno 5. Cambia di conseguenza la domanda della tappa («due persone che non si sono mai incontrate costruiscono la stessa cosa»), mentre l'aggancio resta di forza **medio** e i conteggi del documento non cambiano (24 forti, 6 medi). Decisione di Pietro del 01/10/2026.
- **v0.1 (01/10/2026)**: prima stesione. Formalizza il materiale storico-pedagogico del quarto anno di Pietro in un documento coerente con `anno1-ferrara.md`, `anno1-mappa.md`, `anno2-penisola.md` e `anno3-europa.md`:
  - i due percorsi del materiale distinti per funzione (le persone / le domande) e uniti nei 30 agganci;
  - principio zero esteso (il mondo non esiste ancora) e sei principi dell'anno;
  - il pianeta a strati con sedici strati `S60`–`S75`, due dei quali vuoti, e la scala logaritmica dichiarata;
  - l'archivio come unico luogo percorribile, con i sette modi di arrivo e le sette porte;
  - le 30 tappe agganciate ai 30 livelli dello schema, con 24 agganci forti e 6 medi, e i tre da rivedere segnalati;
  - le trenta domande in forma piena;
  - 30 schede di personaggio obbligatorio (28 nomi proprii e 2 collettivi) con i tre livelli di fonte, la funzione e la porta;
  - il registro che il giocatore costruisce, con i suoi campi, come deliverable dell'anno;
  - la regola dei ritorni, che in questo anno è un problema serio perché il materiale contiene molti nomi già obbligatori nei primi tre anni;
  - le sedici domande dell'anno e il modo in cui il gioco le pone;
  - temi sensibili, con regole scritte prima delle schede;
  - ventotto verifiche storiche, di cui una (V1) prioritaria;
  - otto questioni aperte, di cui la prima sul buco dell'Asia meridionale antica.

---