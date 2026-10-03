---
titolo: Videogioco "I cinque duchi" — i premi: dieci categorie di oggetti, undisciplina ciascuna, e le quattro prove che un premio deve superare
versione: 0.3
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte del materiale: richiesta di Pietro del 03/10/2026 («per ogni livello, per ogni disciplina, tranne informatica, occorre stabilire dei premi... per il ferrarese potrebbero essere figurine di ferraresi illustri che non vengono citati nella storia, per la lingua italiana poeti e autori italiani, poi i premi potrebbero essere dipinti, sculture, opere architettoniche... pensa a cosa potrebbe essere associato come ricompensa al compimento di ciascun livello»), con le regole gia prese su etichette, oggetti di interazione, luoghi e licenze
dati: dati/lingue/associazioni.json (v1, le 180 voci: trenta per lingua, sei lingue); dati/fonti_visive/fonti_visive.json e dati/lingue/immagini_oggetti.json (le schede con etichetta e licenza, da cui i premi prendono la provenienza); dati/premi.json (v1, il catalogo dei premi: da generare, e la sua cardinalita' dipende dalla decisione di §5)
controllo: python3 sorgenti/verifica_premi.py (P1-P5: le categorie sono chiuse e senza buchi, ogni disciplina ha almeno una categoria primaria, i sei ambiti della sfida a mani nude hanno ciascuno un premio possibile, nessuna categoria e' assegnata a una disciplina che il progetto non ha, e nessun premio puo' essere un'opera generata o un'immagine senza licenza)
documenti collegati: videogioco-5-duchi-inventario.md (v0.1, gli elementi interattivi e i quattro registri personali), videogioco-5-duchi-lingue.md (v0.1, le sei lingue e i 900 livelli), videogioco-5-duchi-lingue-immagini.md (v0.1, le 180 voci, le quattro immagini e le nove etichette), videogioco-5-duchi-quadro-trasversale.md (v0.1, i quattro ambiti e le arti per anno), videogioco-5-duchi-ritratti.md (v0.2, la regola del ritratto autentico e dell'emblema), videogioco-5-duchi-pedagogia.md (v0.1, il vantaggio tangibile e la lacuna «osservazione e attenzione»), videogioco-5-duchi-ripassi.md (v0.1), videogioco-5-duchi-luoghi.md (v0.6), FONTI-E-LICENZE.md, AGENTS.md
---

# I premi

## 0. Che cosa è un premio, in una frase

È **un oggetto vero che il ragazzo guarda e che gli dice che cosa sa adesso**. Non una medaglia, non un punto, non una promessa: un'opera che esiste, che ha un autore o una data, e che si può aprire e guardare.

La definizione è stretta di proposito, e segue il principio del progetto: **un premio che non ha a che fare con il contenuto del livello è un premio decorativo**. Il vantaggio deve essere tangibile e non promesso (`pedagogia.md` §1.2): il vantaggio qui non è il premio, è **la cosa che il premio fa vedere**.

## 1. Le undici categorie

L'elenco è **chiuso**, e l'undicesima è nata oggi per una ragione che è in §2.1. Una dodicesima non si aggiunge quando manca un premio: si usa una delle undici o si dichiara il vuoto.

| # | categoria | che cosa è | che cosa serve per ottenerlo |
|---|---|---|---|
| **A** | Figure e ritratti | una persona raffigurata, con nome e date | la regola di `ritratti.md`: autentico o emblema, e tre etichette dichiarate |
| **B** | Pittura | dipinto, affresco, mosaico, miniatura | fonte libera, autore, data quando esiste, museo e numero d'inventario |
| **C** | Scultura | statua, bassorilievo, erma, busto | foto libera, autore, data, luogo |
| **D** | Architettura | edificio, piazza, giardino, ponte, strada | foto, data, e **la ragione per cui quell'edificio** |
| **E** | Opere scritte | manoscritto, prima edizione, pagina stampata, partitura | digitalizzazione o immagine del frontespizio, con l'istituzione che la espone |
| **F** | Epigrafi e iscrizioni | lastra, cippo, tabella, bassorilievo con testo | foto della pietra e **trascrizione del testo**, che è metà del premio |
| **G** | Musica | spartito, strumento, disco | partitura in pubblico dominio o registrazione con licenza |
| **H** | Teatro e cinema | locandina, fotogramma, scenografia, manifesto | **diritti**: molte opere moderne sono ancora protette e non si possono usare |
| **I** | Documenti e leggi | la pagina che ha cambiato una regola | immagine del documento, data, e il luogo in cui è stato scritto |
| **J** | Emblemi e stemmi | il simbolo che dichiara un valore | origine, significato, e chi lo ha adottato |
| **K** | Scheda prodotta dal giocatore | **la voce propria**: per la lingua dei segni, la scheda che il giocatore ha scritto, con il segno del livello e la sua frase | nessuna fonte esterna: è il giocatore, ed è l'unico premio che non si può copiare |

Le categorie **E** e **F** esistono perché sono le uniche due che si possono **leggere**. Un premio che si può leggere vale doppio in un percorso di lingue: il ragazzo non la guarda, la **usa**.

## 2. Le associazioni

Una tabella sola, undici righe. La colonna «da escludere» è la parte che vale: dice che cosa **non** si abbina, e il perché.

| disciplina | primaria | secondaria | da escludere, e perché |
|---|---|---|---|
| **Italiano** | **E** — manoscritti e prime edizioni; **A** — poeti e scrittori | **B** per i testi che hanno un'immagine | un dizionario o una grammatica: un oggetto che si compra e non si guarda non premia nessuno |
| **Ferrarese** | **A** — figure di ferraresi illustri **non citati nella storia**; **D** — architettura ferrarese | **B** (Ortolano, Dosso Dossi, Garofalo), **C** (monumenti cittadini) | **le trenta figure delle 30 tappe dell'anno 1**: il premio deve essere la scoperta, non il ripasso |
| **Latino** | **F** — epigrafi latine; **E** — edizioni | **A** — scrittori romani; **D** — architettura romana | qualsiasi premio **da guardare e non da leggere**: il percorso latino è *leggere senza tradurre*, e un'immagine lo contraddice |
| **Inglese** | **E** — prime edizioni in inglese; **H** — cinema (è l'arte principale dell'anno 4, `quadro-trasversale.md` §1) | **A** — autori di lingua inglese | quiz, ricette, giochi da tavolo: un premio che è un esercizio travestito |
| **Lingua dei segni** | **K** — la scheda che il giocatore produce | **A** — le poche figure sorde documentate, quando sono verificabili | **tutto ciò che è scelto per essere famoso invece che per essere della comunità**. Il catalogo non può essere scritto: `lingue.md` Q4 dichiara che una lingua dei segni non si scrive a tavolino, e un premio sì |
| **Greco** | **B** — mosaici e pittura vasare; **C** — statue; **F** — epigrafi greche | **E** — manoscritti bizantini; **D** — acropoli e Partenone | per l'ultimo terzo del percorzo (il greco moderno) servono opere **contemporanee**: solo antichità significa che tremila anni di percorso finiscono in un museo del passato |
| **Diritto** | **I** — Costituzione, codici, trattati | **D** — architettura delle istituzioni | il concetto di legge in astratto: il premio è **una pagina con una data** |
| **Etica** | **I** — la Dichiarazione universale dei diritti umani; **J** — stemmi | **B** — dipinti allegorici | niente senza oggetto: un premio etico che non si può indicare con il dito non è un premio |
| **Filosofia** | **A** — i filosofi; **B** — le allegorie (le lezioni di filosofia di Rembrandt, Goya, Magnasco) | **E** — prime edizioni | l'opera filosofica in astratto: non ha un'immagine, e si premia **il dipinto che la illustra** |
| **Psicologia** | **A** — chi ha descritto il fenomeno (Freud, Kahneman, Tversky); **B** — l'immagine dell'esperimento | — | un esercizio di rilassamento: sarebbe un premio che il gioco stesso dovrebbe fare per primo |
| **Osservazione e attenzione** | **D** — la pianta e la sua soglia, l'unica cosa che si guarda con attenzione | **B** — i dipinti che obbligano a guardare davvero | era **da_costruire** fino al 03/10/2026, quando è risultato che il dominio non mancava: il gioco ci lavorava già in quattro posti (`quadro-trasversale.md` §1.3). Niente che si possa guardare di fretta |

L'ultima riga era `da_costruire`, ed era un difetto: il dominio `osservazione e attenzione` **esiste già** in quattro posti del progetto (`quadro-trasversale.md` §1.3, che porta le prove). La riga è chiusa dal 03/10/2026 e il dominio ha il suo premio: la pianta di una città vista dalla torre, cioè la categoria `D`.

### 2.1 Il premio della lingua dei segni: perché non può essere una persona

*(decisione di Pietro del 03/10/2026: «esistono 150 figure di sordi importanti? a prescindere, cambiamo premio».)*

**La risposta è no, e il numero la dice: non esistono centocinquanta figure sorde storiche documentabili.** Le fonti enciclopediche che il progetto usa nominano i pionieri — l'Abbé de l'Épée, Laurent Cler, e in Italia Lorenzo Mordini e chi ha scritto i primi manuali — cioè **poche decine**, non centocinquanta, e molte non hanno una fonte che regga la prova 1. La ragione non è la memoria delle persone: è che una lingua dei segni è stata per secoli **invisibile**, e le sue figure non sono state registrate dai documenti che il progetto può usare.

Con un premio per livello, la lingua dei segni dovrebbe avere **centocinquanta premi** (centocinquanta livelli, sei lingue per anno). Con poche decine di figure documentate, la prova 4 — **nessun duplicato** — sarebbe violata cinque volte per nome.

**Il premio cambia, e cambia in meglio.** È la **categoria K**: la scheda che il giocatore ha prodotto lui. Per ogni livello superato della lingua dei segni il giocatore riceve **una pagina del proprio quaderno**: il segno che quel livello ha insegnato, con la **frase che ha scritto lui**, e la data. Nessun premio del progetto è più suo di questo.

Tre ragioni, e la terza è quella che tiene:

1. **è l'unico premio che non si può copiare** — tutto il resto si trova su Wikimedia Commons, questo no;
2. **è il premio giusto per una lingua**: imparare la LIS non è guardare, è produrre. Un premio che ti fa produrre la lingua è l'unico che non sia un premio decorativo;
3. **non ha il problema della fonte**: le altre dieci categorie hanno tutte una fonte da dichiarare e una licenza da verificare, e questa ha solo il giocatore.

**Quello che resta aperto, e non è un premio**: la **forma del segno** nel quaderno. Il gioco non può disegnare la LIS — la `lingue.md` Q4 dichiara che una lingua dei segni non si scrive a tavolino, e un disegno fatto dal progetto sarebbe esattamente l'errore che quella domanda vieta. Quindi la scheda del quaderno porta **lo spazio** (un riquadro, una riga, la data) e **la riga di descrizione** che il livello fornisce, e **il segno lo mette il giocatore** — in un'altra parte del file, o a mano sulla pagina stampata. Va dichiarato che il gioco non sa disegnare la propria lingua dei segni: è il più grande limite che ha, ed è giusto che sia scritto.


### 2.2 I sei domini della sfida a mani nude, e che cosa possono avere come premio

| dominio | premio possibile | stato |
|---|---|---|
| `informatica` | **nessuno**: i premi sono per le altre discipline, per tua scelta | dichiarato |
| `logica` | **nessuno**: non ha un oggetto proprio, e non è un premio che si possa guardare | dichiarato |
| `calcolo mentale e stime` | **nessuno**, per la stessa ragione | dichiarato |
| `linguistica e testo` | **E** e **F**: le due categorie che si leggono | possibile |
| `Costituzione e cittadinanza` | **I**, lo stesso premio di Diritto | possibile |
| `osservazione e attenzione` | **D** — la pianta e la sua soglia | chiuso |

Quattro dei sei domini **non possono avere un premio**. Non è un difetto: è la differenza fra un gioco che premia e un gioco che premia **qualcosa**. Nella tappa a mani nude un dominio senza premio si dichiara come tale, e la tappa vale per la prestazione, non per il premio.


## 3. Le quattro prove che un premio deve superare

Un premio entra nel catalogo solo se le passa tutte e quattro. Le prove sono corto, e ognuna ha una ragione.

| # | prova | perché serve |
|---|---|---|
| **1. Esiste, e si può vedere** | l'opera esiste, l'immagine è libera di diritti, e porta etichetta, autore e data | il progetto vieta le immagini generate e i volti inventati (`lingue-immagini.md` §1): un premio inventato insegna che esistono opere che non esistono |
| **2. Insegna il livello** | chi ha superato quel livello, guardando il premio, deve **riconoscere** in esso qualcosa di ciò che ha imparato | senza questa prova il premio è una decorazione, e la verifica non potrebbe mai dire che sia giusto |
| **3. Non è già nella storia** | l'opera non compare già nella storia della tappa, e non è già il pin o la stanza | se è già nella storia il premio non aggiunge niente: il ragazzo l'ha già visto e il premio diventa un ricordo |
| **4. Non è un duplicato** | due livelli diversi non hanno lo stesso premio | due premi uguali sono uno solo, e il secondo livello è stato trattato come se avesse qualcosa in più |

La prova 3 è quella che Pietro ha scritto lui, per il ferrarese, e vale per tutte le discipline: **il premio è la scoperta**. Per l'anno 1 la cosa è facile e per gli anni dopo è impossibile: le trenta figure di Ferrara sono già tutte nella storia, e i premi dell'anno 1 sono quindi architettura (`D`) e pittura (`B`), non persone.

## 4. La cardinalità, decisa: un premio per livello, e una salvadanaio

*(decisione di Pietro, 03/10/2026: «un livello compiuto per ogni premio: il giocatore lo mette in una sorta di salvadanaio».)*

La scelta è fra le tre di questa tabella, ed è la più pesante:

| variante | quanti premi | esito |
|---|---|---|
| **un premio per livello** | **1050** (vedi §4.0) | **scelta**: il livello ha la sua ricompensa, e la ricompensa ha un posto dove stare |
| un premio per voce | 180 | scartata: le stesse trenta voci attraversano cinque anni e non distinguono i livelli |
| un premio per anno e disciplina | circa 50 | scartata: il ragazzo riceve quarantacinque cose in cinque anni |

### 4.0 Il numero è esatto: 1050, non «circa 900»

Il «circa» era una dichiarazione di buco, non una cifra: `quadro-trasversale.md` non dichiarava quanti livelli aggiungessero i suoi quattro ambiti, e senza quel dato le tre varianti di cardinalità non erano confrontabili. Il dato è **zero**, e la ragione è nel testo dello stesso quadro: il trasversale **non aggiunge materie** (§0) e «compare solo dove si collega in modo naturale alla tappa e non è mai contenuto valutato». Un aggancio dentro un livello non è un livello.

Quindi il catalogo ha un numero solo:

| | quanti |
|---|---|
| livelli informatici | 150 (`schema-livelli.md`, uno per tappa) |
| livelli linguistici | 900 (sei lingue × trenta × cinque anni) |
| livelli dei quattro ambiti trasversali | **0**: sono agganci, e `quadro-trasversale.md` §1.3 lo dichiara per il quinto (osservazione e attenzione) che non ha neanche un programma |
| **totale dei livelli** | **1050** |
| **premi, con la variante scelta** | **1050**, meno quelli di discipline che non hanno un oggetto proprio (§2.2) |

Il numero dei premi è dunque **1050 e non 900**: la cifra che girava nel progetto contava i soli livelli linguistici e dimenticava i centocinquanta informatici, che hanno un premio anche loro. La correzione cambia la dimensione del catalogo di circa un sesto, ed è il motivo per cui il conto andava chiuso prima di scrivere `dati/premi.json`, che è **da produrre** e che senza questo numero sarebbe stato scritto corto di centocinquanta record.

### 4.1 La salvadanaio, e perché non è un'immagine

Il premio non viene mostrato e basta: **va in un registro che il giocatore possiede**, la salvadanaio, ed è uno dei quattro registri personali dell'inventario (`inventario.md` §3). Tre ragioni, e la terza è quella che conta:

1. **è il catalogo personale**: non «hai vinto 340 premi», ma «ecco i 340 oggetti che hai imparato», ognuno con le sue tre righe;
2. **è consultabile**: si apre quando si vuole, serve per il ripasso e serve per la consegna;
3. **non è un'immagine**: una salvadanaio con dentro le foto dei premi sarebbe un inventario di icone. **La salvadanaio contiene i premi, non le loro immagini**, e le immagini sono in `lingue-immagini.md`, ciascuna con la sua etichetta e la sua licenza.

### 4.2 Le tre righe che ogni premio porta

Ogni premio porta una scheda di **tre righe brevi**, nella lingua del gioco, e la terza è quella che rende il premio un premio:

| riga | che cosa contiene | esempio |
|---|---|---|
| **`chi`** | chi è, in una riga: nome, date, e perché è qui | «Ambedkar, 1891–1956, giurista: ha scritto la Costituzione dell'India» |
| **`cosa`** | che cosa ha fatto, e **quale fatto**, non generico | «ha scritto il rapporto sui diritti dei Dalit, che nel suo Paese erano legge» |
| **`riflessione`** | che cosa sarebbe diverso oggi, e perché è vero | «senza quel testo, la Costituzione indiana non avrebbe i diritti che ha» |

**La terza riga non è una formula, è una prova.** Il modello «se non ci fosse stato lui oggi non potremmo…» è la **forma**, e vale solo per i premi che sono persone. Per un oggetto — una pizza, un'epigrafe, un documento — la riflessione è della stessa sostanza e non della stessa frase: «senza questa lapide non sapremmo che quel nome esisteva». **Se la riflessione si può scrivere senza pensarci, il premio è decorativo** e non entra (`pedagogia.md` §1.2).

## 5. Cosa c'è da fare

1. ~~**Il numero dei livelli trasversali**~~ **chiusa il 03/10/2026**: sono **zero**, dichiarato in `quadro-trasversale.md` §1.3, e il conto dei livelli è **1050** (§4.0).
2. ~~**La variante scelta**~~ **chiusa il 03/10/2026**: un premio per livello, Pietro.
3. **Il catalogo `dati/premi.json`**, **da produrre**: i due blocchi di §5 sono chiusi, quindi il catalogo si può scrivere. Con i campi `premio`, `categoria`, `disciplina`, `etichetta`, `fonte`, `licenza`, `perche_prova_2`, e compilato solo dopo che le prove 1, 3 e 4 sono soddisfatte una per una. Sono **1050 record**, e il lavoro più grosso è la prova 3.
4. ~~**La LIS**~~ **chiusa il 03/10/2026** (§2.1): il premio non è una persona ma la scheda che il giocatore produce, la categoria **K**. Quello che resta aperto non è il premio, è `lingue.md` Q4 — **la forma del segno nel quaderno**, che il gioco non può disegnare.
5. ~~**Il quinto dominio**~~ **chiusa il 03/10/2026**: `pedagogia.md` §3 e `premi.md` §2.2 lo davano per assente e non lo era — esisteva in quattro posti (`quadro-trasversale.md` §1.3) e ha preso il suo premio, la categoria `D`.

## 6. Registro delle modifiche

- **v0.1 (03/10/2026)**: prima stesione. Dieci categorie chiuse, undici discipline con la loro associazione e la colonna «da escludere», quattro prove di ammissione, tre varianti di cardinalità con i numeri accanto. Le tre cose che il documento dichiara e non risolve: **la cardinalità** (che è di Pietro), **il numero dei livelli trasversali** (che il progetto non ha) e **la LIS** (che non si scrive a tavolino). Una riga della tabella — `osservazione e attenzione` — è la stessa lacuna che `pedagogia.md` §3 aveva trovata nelle sei categorie della sfida a mani nude, e le due vanno chiuse insieme o non si chiudono.
- **v0.3 (03/10/2026)**: **il numero dei premi è chiuso, ed era sbagliato di un sesto.** Aggiunto §4.0: i livelli dei quattro ambiti trasversali sono **zero** — il trasversale è un aggancio dentro i livelli, non un livello — quindi i livelli sono 150 informatici più 900 linguistici, cioè **1050**, e non i «circa 900» che il progetto portava da tre giorni. La cifra vecchia contava i soli livelli linguistici e dimenticava i centocinquanta informatici, che hanno un premio anche loro: è la ragione per cui il conto andava chiuso prima di scrivere `dati/premi.json`. Nello stesso giorno è chiusa la riga `osservazione e attenzione`: **non era un dominio da costruire, era un dominio che il progetto aveva già** in quattro posti (`quadro-trasversale.md` §1.3), e ha preso il suo premio — la categoria `D`, la pianta e la sua soglia. Le quattro cose da fare scendono a una: scrivere il catalogo.
