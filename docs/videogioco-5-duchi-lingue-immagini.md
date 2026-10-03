---
titolo: Videogioco "I cinque duchi" — le immagini degli oggetti di interazione: dove vengono e perché si dichiarano
versione: 0.1
data: 2026-10-02
autore: Pietro Fabbri (con Claude)
fonte: ricerca su Wikimedia Commons del 02/10/2026
documenti collegati: videogioco-5-duchi-lingue.md (v0.1), videogioco-5-duchi-ritratti.md (v0.2), videogioco-5-duchi-luoghi-edifici.md (v0.3), videogioco-5-duchi-esercizi.md (v0.1), AGENTS.md, FONTI-E-LICENZE.md
dati: dati/lingue/associazioni.json (v1), dati/lingue/immagini_oggetti.json (v1, 180 voci, 1120 candidati)
---

# Le immagini degli oggetti di interazione

## 0. A che cosa serve, e che cosa non è ancora fatto

Il gioco ha seicentottanta voci di oggetto: **trenta per ciascuna delle sei lingue** (`videogioco-5-duchi-lingue.md` §5.4). Ogni voce è la cosa con cui il giocatore interagisce nella tappa facoltativa dell'oggetto: la pizza, un numero romano, un clarinetto, una coppa greca, un campo di raccolta dei proverbi ferraresi.

Questo documento dice **quali immagini esistono per quelle voci, con quale licenza, e quali non esistono**. È un documento di controllo, non un catalogo da sfogliare, ed è gemello di `videogioco-5-duchi-ritratti.md`.

**Che cosa è fatto.** Una ricerca su Wikimedia Commons ha esaminato tutte e 180 le voci con termini scelti uno per uno, non tradotti alla cieca. Ha prodotto **1120 candidati con licenza libera**, di cui il progetto ne ha **respinti 12** per difetto automatico. I dati sono in `dati/lingue/immagini_oggetti.json`.

**Che cosa non è fatto, e conta più del resto.** **Nessuna immagine è stata ancora scelta, e nessuna è stata guardata a vista.** I 1120 candidati sono *proposte*, non scelte. Il controllo automatico verifica licenza, misura e copertura, ma non può sapere se la fotografia del «kykeon» mostra il kykeon o un vaso qualsiasi: se lo chiede, risponde che non lo sa. La scelta la fa una persona, e si registra in `dati/lingue/attestazione_oggetti.json` con etichetta e motivo, come per i ritratti.

**Il difetto più importante del lavoro è in §5**, ed è la ripetizione esatta di un difetto già trovato nei ritratti. Vale la pena leggerlo prima di fidarsi di qualunque numero di questo documento.

---

## 1. La regola: quattro immagini, non una

La regola dei ritratti (`ritratti.md` §1: due immagini, non una) vale per le persone. Per gli oggetti ne servono quattro, perché un oggetto può essere fotografato, dipinto, stampato — o non essere visibile affatto.

| | `foto` | `dipinto` | `stampa` | `nessuna` |
|---|---|---|---|---|
| **quando** | esiste una fotografia libera che mostra l'oggetto | l'oggetto esiste solo in un'opera d'arte | l'oggetto esiste in una fonte a stampa, un manoscritto, una partitura, un'epigrafe | non esiste immagine libera, e l'oggetto va disegnato |
| **esempio** | *la pizza*, *il vino* | *il simposio*, *le coppe dipinte* | *i numeri romani*, *gli auspici* | *i proverbi ferraresi*, *la trasmissione della tecnica* |
| **chi decide** | una ricerca automatica **propone**, poi un attestato a vista | idem | idem | idem |
| **dichiarazione** | l'**etichetta** (§3) e la **licenza** | idem | idem | il **motivo** per cui non c'è immagine |

La quarta categoria non è una sconfitta. È la parte del gioco in cui si vede che la conoscenza ha un bordo, ed è la stessa lezione dei 44 emblemi dei ritratti: una voce con scritto «non esiste immagine libera» insegna più di un'immagine inventata.

**Regola che vale per tutte e quattro.** Nel gioco **non entra un'immagine generata**, per nessun oggetto. Una fotografia di una pizza vera sì; una pizza disegnata dall'IA no. Un dipinto di un simposio sì; un simposio ricostruito no. Il progetto vieta i volti inventati per le persone reali e vieta, per la ragione stessa, gli oggetti inventati: un piatto inventato insegna che le regioni d'Italia hanno piatti che non esistono, il che è una bugia con una bella cornice.

---

## 2. I numeri della ricerca

La ricerca ha girato il 02/10/2026 su Wikimedia Commons, con `sorgenti/lingue/cerca_immagini_oggetti.py`, che chiede a Commons i nomi dei file (`filetype:bitmap`) e ne legge la licenza dalla pagina del file.

| | Italiano | Ferrarese | Latino | Inglese | LIS | Greco | **Totale** |
|---|---|---|---|---|---|---|---|
| voci | 30 | 30 | 30 | 30 | 30 | 30 | **180** |
| con immagini libere | 30 | 0 | 28 | 30 | 30 | 28 | **146** |
| senza immagini libere | 0 | 30 | 2 | 0 | 0 | 2 | **34** |

**I candidati.** 1120 in tutto, 17 licenze diverse, tutte libere:

| Licenza | Candidati |
|---|---|
| CC BY-SA 4.0 | 476 |
| Public domain | 202 |
| CC BY-SA 3.0 | 126 |
| CC0 | 92 |
| CC BY 2.0 | 53 |
| CC BY 4.0 | 53 |
| CC BY-SA 2.0 | 45 |
| CC BY 3.0 | 38 |
| altre nove | 35 |

**I 34 senza immagini** non sono tutti la stessa cosa, e la distinzione conta:

| Lingua | Voci | Perché |
|---|---|---|
| **Ferrarese** | 30 | Le trenta voci **non sono oggetti**: sono campi da rilevare (`lingue.md` §5.4). Non esiste immagine che rappresenti «i proverbi dei mestieri». Non è una ricerca saltata: è una categoria, dichiarata nei dati con il suo motivo. |
| **Latino** | 2 | *L'ispezione delle interiora* e *le formule di protezione*: i termini cercati non danno nulla di libero. Vanno cercati in altre fonti, o dichiarati `nessuna`. |
| **Greco** | 2 | *Il vino di Maronea* e *i vini dirottati*: il primo non ha un'immagine propria (è un vino locale, non un oggetto riconoscibile), il secondo è una pratica di cui non resta documento visivo. |

---

## 3. Le etichette, che sono la parte importante

Ogni immagine che entra nel gioco porta un'etichetta, come i ritratti. Le etichette sono nove, e sono la garanzia che chi guarda un'immagine sappia che cosa sta guardando:

| Etichetta | Quando |
|---|---|
| `fotografia` | scatto fotografico, moderno o d'archivio |
| `immagine_d_archivio` | scatto storico, con data e luogo se disponibili |
| `dipinto` | dipinto su tela, tavola o muro |
| `incisione` | incisione, xilografia, litografia, acquaforte |
| `miniatura` | miniatura di manoscritto |
| `rilievo` | bassorilievo, alto rilievo, scolpito |
| `partitura` | spartito, tablatura, notazione musicale |
| `frammento_antico` | parte di un'opera antica, con il museo e l'inventario |
| `immagine_tratteggiata` | disegno, schizzo, incisione d'epoca |

**Tre regole che le etichette devono rispettare.**

1. **L'etichetta descrive l'immagine, non l'oggetto.** Un'anfora greca fotografata in un museo è `frammento_antico`, non `anfora`: l'anfora è l'oggetto, l'immagine è quello che le hanno fatto.
2. **La data va dichiarata quando c'è.** Un'immagine senza data non è un'immagine storica: è un'immagine che *potrebbe* essere del 1900 o del 2020, e il gioco non può fingere di sapere quale delle due sia.
3. **Il museo e l'inventario, quando ci sono.** Le collezioni museali sono le fonti più serie di questo progetto, e citare il numero d'inventario è ciò che rende un'immagine verificabile da chiunque.

Le stesse regole valgono per l'autore e per la licenza, che ogni scheda mostra (§4).

---
## 4. Misura e proporzione: la parte che riguarda la fedeltà

Una rappresentazione è fedele solo se **non cambia le proporzioni di ciò che rappresenta**. È la regola che vale per i luoghi (`luoghi-edifici.md` §5, il rilievo come risposta alle altezze mancanti) e vale qui con una conseguenza pratica: **le immagini non si stirano mai**.

### 4.1 Le misure

| | Ritratto | Scheda oggetto | Perché |
|---|---|---|---|
| Misura | 48×54 px | **96×72 px** | L'oggetto ha bisogno di poco più di spazio del ritratto, perché si riconosca; il doppio sarebbe una foto a parte |
| Proporzione | 8:9, verticale | **4:3, orizzontale** | La scheda è accanto al testo del livello, non sopra |
| Peso atteso | 1 258 byte in media | **da misurare** | Non ancora misurato: le immagini non sono state scelte |
| Minimo per entrare | — | **160×120 px** | Sotto questa misura il gioco dovrebbe ingrandire, e il gioco non ingrandisce |

### 4.2 La regola del ritaglio, che è la parte difficile

I 1120 candidati hanno rapporti d'aspetto che vanno da **0,14 a 7,00**. Non si possono usare tutti: molti sono strisce, quadrati, o panorami.

La regola che il progetto adotta è di **ritagliare, non stirare**, con due condizioni che rendono la cosa onesta:

1. **Il ritaglio non può togliere l'oggetto.** Se ritagliare in 4:3 toglie il soggetto dalla foto, la foto non entra: si cerca un'altra immagine. Per questo il controllo **G4** verifica, per ciascuna voce, che **esista almeno un candidato usabile con la forma giusta**, e non accetta che tutte le opzioni siano da ritagliare a forza.
2. **Il ritaglio si dichiara.** Ogni scheda che ha subìto un ritaglio lo dice, come si dichiara la cronologia di una piazza (`luoghi-edifici.md` §4: una tappa del 1450 non può mostrare la piazza di oggi). Il giocatore che vede un'immagine ritagliata deve poter sapere che lo è.

**Il risultato del controllo.** Tutte e 146 le voci coperte — cioè tutte, salvo le trenta ferraresi e le quattro senza immagine — hanno **almeno un candidato con la misura e la proporzione giusta**. Non ce n'è nessuna che si può sistemare solo ritagliando a forza.

### 4.3 Quello che la proporzione non risolve

La proporzione corretta rende l'immagine **fedele nelle misure** e non dice niente sulla **sua verità**. Un'immagine stirata mente; un'immagine ritagliata può mentire anche di più, perché toglie il contesto. Perciò il ritaglio è ammesso solo se l'oggetto resta intero e riconoscibile, e la decisione finale resta di chi guarda l'immagine (Q1, §6).

---

## 5. Il difetto più importante: la ricerca ha trovato oggetti sbagliati

Questa sezione è il cuore del documento, e vale più dei numeri di §2.

Una ricerca automatica che «funziona» restituisce un file per ogni voce, e sembra risolto il problema. Non lo risolve. Nel progetto è già successo con i ritratti: la ricerca ha restituito **un gatto per Renata Viganò**, una ceramica iraniana per i mercanti di Ferrara e una parata di soldati di oggi per i Bersaglieri del 1848. Qui è successo di nuovo, in modo più sistematico, e i casi sono due.

**Il primo caso: la parola che significa due cose.** Alla voce **«la correggia»** il file migliore è stato `Antonio Allegri da Correggio.jpg`, cioè il ritratto di un pittore il cui cognome suona come la voce. Alla voce **«gli occhiali»** sono arrivate le foto di una moschea di Istanbul. Non è un errore della ricerca: è la differenza fra cercare una parola e cercare un oggetto.

**Il secondo caso, più grave: la parola giusta nel contesto sbagliato.** Alla voce **«il tè»** (greco, le bevande) il risultato è un mulino olandese e una fattoria, per la confusione fra «tea» e «the» in inglese. Alla voce **«la sete»** (greco) è arrivato un canale nella città di **Sète**, in Francia. Alla voce **«la conservazione»** sono arrivati articoli di **biologia della conservazione**, non la conservazione del vino in una cantina. Alla voce **«i proverbi»** (latino) è arrivata una **Biblia in latino**, che è un testo bellissimo e non è un proverbio. Alla voce **«sabaion»** (dolce piemontese) è arrivata la crema inglese *sabayon*, che è un'altra cosa.

Il controllo **G7** esiste per rendere questi casi visibili senza guardare le immagini: segnala le voci in cui **nessun** candidato contiene né la parola dell'oggetto né quella del termine cercato. Sono **67 voci su 146**, e la distribuzione dice già qualcosa:

| Lingua | Voci a rischio G7 | Su quante coperte |
|---|---|---|
| Italiano | 2 | 30 |
| Latino | **27** | 28 |
| Inglese | 12 | 30 |
| LIS | 9 | 30 |
| Greco | 17 | 28 |

**Il latino è il caso peggiore, e per una ragione che il progetto riconosce già.** Ventisette voci su ventotto sono a rischio, perché i termini latini che ho cercato sono termini **inglesi transliterati** (*haruspex*, *exta hepatum*), e Commons li contiene quasi solo in descrizioni, non nei nomi dei file. Non è un errore della ricerca: è che la ricerca è andata nel posto sbagliato per quella lingua.

**La regola che ne nasce, e che vale per tutto il progetto.**

> **Una ricerca che restituisce un file non ha trovato l'oggetto: ha trovato una parola.** La scelta la fa una persona che guarda l'immagine, e il risultato si registra in `dati/lingue/attestazione_oggetti.json` con etichetta, autore, licenza e **motivo del giudizio**.

È la stessa regola dei ritratti (`AGENTS.md` §3, «una ricerca automatica propone, non decide»), e il progetto l'ha già imparata una volta: quando un `HTTP 429` di Wikipedia venne letto come «nessun ritratto esiste», quindici personaggi con un ritratto celebre furono dichiarati senza. Una risposta che non arriva non è una risposta negativa, e un file che arriva non è la risposta giusta.

---

## 6. I controlli automatici e le questioni aperte

### 6.1 I sette controlli

`sorgenti/lingue/verifica_immagini_oggetti.py` esegue sette controlli su `dati/lingue/immagini_oggetti.json`:

| # | Controllo | Che cosa cerca | Esito |
|---|---|---|---|
| **G1** | Copertura | ogni voce ha candidati, e le trenta ferraresi dichiarano il motivo per cui non ne possono avere | 180 voci, tutte coperte o motivate |
| **G2** | Licenze | ogni candidato ha una licenza libera riconosciuta, e nessuna non commerciale | tutte libere |
| **G3** | Misura | nessun candidato sotto 160×120, che nel gioco verrebbe ingrandito | **4 respinti** |
| **G4** | Proporzione | ogni voce coperta ha almeno un candidato con la forma giusta per la scheda, senza ritaglio forzato | **146 su 146** |
| **G5** | Completezza | autore e indirizzo ci sono in ogni candidato | **8 respinti** |
| **G6** | Pertinenza | quante voci restano da guardare a vista: **146**, perché il controllo automatico non può sapere se l'immagine è dell'oggetto giusto | dichiarato |
| **G7** | Scivolamento | quante voci in cui nessun candidato nomina l'oggetto: **67**, da guardare per prime | avviso, non errore |

Il conto dei dodici problemi è **12 candidati respinti** su 1120, non dodici voci scoperte: tutte e dodici le voci hanno alternative. G7 non è un errore ed è per questo che non fa fallire lo script.

### 6.2 Le questioni aperte

**Q1 — Chi guarda le immagini, e con quale impegno? (bloccante per le tappe dell'oggetto)**
Guardare 1120 candidati a vista è un lavoro di ore, non di minuti, e finora non è stato fatto **nessuno**. Le opzioni sono tre: le guardo io e registro l'attestazione, le guarda Pietro, oppure si guarda **un campione** — i 146 migliori per voce — e il resto si considera sufficiente. La terza è la più realistica, ma va detto che **non è la stessa cosa**: un campione non attesta il resto.

**Q2 — Le trenta voci di ogni lingua sono confermate? (bloccante)**
Riprende `lingue.md` §7 Q2. Un'immagine cerca la voce giusta, non quella confermata: se le trenta voci cambiano, tutta la ricerca va rifatta. Conviene quindi chiudere Q2 prima di scegliere le immagini, non dopo.

**Q3 — Le fonti del latino e del greco vanno cercate altrove? (bloccante per il latino)**
Il G7 dice che **27 voci latine su 28** hanno solo proposte scoperte per caso. Le fonti giuste non sono Commons: sono i **corpus epigrafici** (EDCS, EDR) e le **biblioteche digitali** (Gallica, BEIC). Commons ha le immagini degli oggetti, non le fonti filologiche. Va deciso se aggiungere questi due corpi alle ricerche, il che è un lavoro diverso e va detto.

**Q4 — Che cosa si fa delle trenta voci ferraresi? (non bloccante)**
Le trenta voci ferraresi non hanno immagine e non ne possono avere: sono campi di raccolta. Ma allora la tappa dell'oggetto ferrarese **non ha immagine**, mentre tutte le altre ne hanno. Va deciso se le tappe ferraresi mostrano qualcos'altro — un'immagine della persona che parla, una trascrizione, il paesaggio — o se dichiarano il vuoto con la stessa regola dei 44 emblemi. La seconda è più onesta, ed è quella che il progetto sceglie di solito.

**Q5 — Le immagini servono solo per le facoltative? (non bloccante)**
Le voci degli oggetti servono alle tappe facoltative, ma gli stessi oggetti compaiono anche nei **testi autentici** dei 900 livelli (`lingue.md` §2: ogni livello ha un testo vero). Una tappa su Cesare ha bisogno di un'immagine della pagina di Cesare, non di una coppa. Le due cose sono diverse, e solo la prima è stata fatta: **le immagini dei testi autentici non sono state cercate**, e sono almeno 900.

**Q6 — Chi ridimensiona, e quando? (non bloccante, tecnica)**
Ridurre a 96×72 gli spinelli di Commons richiede un'immagine minima (§4.1), un taglio che non alteri la proporzione, e una decisione sul formato. Il metodo (`ritratto_reale.py` per i ritratti) esiste già e va ripreso, ma nessuna immagine degli oggetti è ancora stata ridotta, perché nessuna è stata scelta.

---

## 7. Registro delle modifiche

| Data | Versione | Che cosa è cambiato |
|---|---|---|
| 02/10/2026 | 0.1 | Prima stesura. Ricerca su Wikimedia Commons delle **180 voci** degli oggetti di interazione, con termini scelti voce per voce: **1120 candidati** con licenza libera, di cui **12 respinti** per difetto automatico. La regola delle quattro categorie, le etichette, la misura 96×72 e la regola del ritaglio dichiarato. Il difetto della ricerca — 67 voci in cui nessun candidato nomina l'oggetto, fra cui il latino a 27 su 28 — dichiarato per esteso, con i sette controlli che lo rendono visibile. **Nessuna immagine scelta, nessuna guardata a vista**: è dichiarato, ed è la prima questione aperta. |