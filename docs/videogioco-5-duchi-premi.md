---
titolo: Videogioco "I cinque duchi" — i premi: dieci categorie di oggetti, undisciplina ciascuna, e le quattro prove che un premio deve superare
versione: 0.1
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte del materiale: richiesta di Pietro del 03/10/2026 («per ogni livello, per ogni disciplina, tranne informatica, occorre stabilire dei premi... per il ferrarese potrebbero essere figurine di ferraresi illustri che non vengono citati nella storia, per la lingua italiana poeti e autori italiani, poi i premi potrebbero essere dipinti, sculture, opere architettoniche... pensa a cosa potrebbe essere associato come ricompensa al compimento di ciascun livello»), con le regole gia prese su etichette, oggetti di interazione, luoghi e licenze
dati: dati/lingue/associazioni.json (v1, le 180 voci: trenta per lingua, sei lingue); dati/fonti_visive/fonti_visive.json e dati/lingue/immagini_oggetti.json (le schede con etichetta e licenza, da cui i premi prendono la provenienza); dati/premi.json (v1, il catalogo dei premi: da generare, e la sua cardinalita' dipende dalla decisione di §5)
controllo: python3 sorgenti/verifica_premi.py (P1-P5: le dieci categorie sono chiuse e senza buchi, ogni disciplina ha almeno una categoria primaria, i sei ambiti della sfida a mani nude hanno ciascuno un premio possibile, nessuna categoria e' assegnata a una disciplina che il progetto non ha, e nessun premio puo' essere un'opera generata o un'immagine senza licenza)
documenti collegati: videogioco-5-duchi-lingue.md (v0.1, le sei lingue e i 900 livelli), videogioco-5-duchi-lingue-immagini.md (v0.1, le 180 voci, le quattro immagini e le nove etichette), videogioco-5-duchi-quadro-trasversale.md (v0.1, i quattro ambiti e le arti per anno), videogioco-5-duchi-ritratti.md (v0.2, la regola del ritratto autentico e dell'emblema), videogioco-5-duchi-pedagogia.md (v0.1, il vantaggio tangibile e la lacuna «osservazione e attenzione»), videogioco-5-duchi-ripassi.md (v0.1), videogioco-5-duchi-luoghi.md (v0.5), FONTI-E-LICENZE.md, AGENTS.md
---

# I premi

## 0. Che cosa è un premio, in una frase

È **un oggetto vero che il ragazzo guarda e che gli dice che cosa sa adesso**. Non una medaglia, non un punto, non una promessa: un'opera che esiste, che ha un autore o una data, e che si può aprire e guardare.

La definizione è stretta di proposito, e segue il principio del progetto: **un premio che non ha a che fare con il contenuto del livello è un premio decorativo**. Il vantaggio deve essere tangibile e non promesso (`pedagogia.md` §1.2): il vantaggio qui non è il premio, è **la cosa che il premio fa vedere**.

## 1. Le dieci categorie

L'elenco è **chiuso**. UnaUndicesima categoria non si aggiunge quando manca un premio: si usa una delle dieci o si dichiara il vuoto.

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

Le categorie **E** e **F** esistono perché sono le uniche due che si possono **leggere**. Un premio che si può leggere vale doppio in un percorso di lingue: il ragazzo non la guarda, la **usa**.

## 2. Le associazioni

Una tabella sola, undici righe. La colonna «da escludere» è la parte che vale: dice che cosa **non** si abbina, e il perché.

| disciplina | primaria | secondaria | da escludere, e perché |
|---|---|---|---|
| **Italiano** | **E** — manoscritti e prime edizioni; **A** — poeti e scrittori | **B** per i testi che hanno un'immagine | un dizionario o una grammatica: un oggetto che si compra e non si guarda non premia nessuno |
| **Ferrarese** | **A** — figure di ferraresi illustri **non citati nella storia**; **D** — architettura ferrarese | **B** (Ortolano, Dosso Dossi, Garofalo), **C** (monumenti cittadini) | **le trenta figure delle 30 tappe dell'anno 1**: il premio deve essere la scoperta, non il ripasso |
| **Latino** | **F** — epigrafi latine; **E** — edizioni | **A** — scrittori romani; **D** — architettura romana | qualsiasi premio **da guardare e non da leggere**: il percorso latino è *leggere senza tradurre*, e un'immagine lo contraddice |
| **Inglese** | **E** — prime edizioni in inglese; **H** — cinema (è l'arte principale dell'anno 4, `quadro-trasversale.md` §1) | **A** — autori di lingua inglese | quiz, ricette, giochi da tavolo: un premio che è un esercizio travestito |
| **Lingua dei segni** | **nessuna delle dieci** — è l'eccezione dichiarata, §2.1 | — | **tutto ciò che è scelto per essere famoso invece che per essere della comunità**. Il catalogo non può essere scritto: `lingue.md` Q4 dichiara che una lingua dei segni non si scrive a tavolino, e un premio sì |
| **Greco** | **B** — mosaici e pittura vasare; **C** — statue; **F** — epigrafi greche | **E** — manoscritti bizantini; **D** — acropoli e Partenone | per l'ultimo terzo del percorzo (il greco moderno) servono opere **contemporanee**: solo antichità significa che tremila anni di percorso finiscono in un museo del passato |
| **Diritto** | **I** — Costituzione, codici, trattati | **D** — architettura delle istituzioni | il concetto di legge in astratto: il premio è **una pagina con una data** |
| **Etica** | **I** — la Dichiarazione universale dei diritti umani; **J** — stemmi | **B** — dipinti allegorici | niente senza oggetto: un premio etico che non si può indicare con il dito non è un premio |
| **Filosofia** | **A** — i filosofi; **B** — le allegorie (le lezioni di filosofia di Rembrandt, Goya, Magnasco) | **E** — prime edizioni | l'opera filosofica in astratto: non ha un'immagine, e si premia **il dipinto che la illustra** |
| **Psicologia** | **A** — chi ha descritto il fenomeno (Freud, Kahneman, Tversky); **B** — l'immagine dell'esperimento | — | un esercizio di rilassamento: sarebbe un premio che il gioco stesso dovrebbe fare per primo |
| **Osservazione e attenzione** | **D** — la pianta e la sua soglia; **B** — i dipinti che obbligano a guardare davvero | **F** — le iscrizioni, che si leggono a distanza | niente: il dominio **non esiste ancora** nel progetto, e la riga resta **da_costruire** |

L'ultima riga è la stessa lacuna che `pedagogia.md` §3 aveva trovata nelle sei categorie della sfida a mani nude: **`osservazione e attenzione` è un dominio che il progetto non ha ancora**. Qui ha almeno una categoria possibile, che è la pianta di una città vista dalla torre: ma resta **da costruire**, e le due righe vanno lette insieme.

### 2.1 L'eccezione dichiarata, e i sei domini della sfida a mani nude

**L'eccezione: la lingua dei segni non ha una categoria.** Le dieci di §1 sono un elenco chiuso, e nessuna di loro è «una produzione della comunità sorda», che è un oggetto la cui provenienza è la condizione perché valga. Aggiungere una undicesima categoria per una sola disciplina sarebbe una categoria che esiste per una riga: peggio. La riga resta quindi **dichiarata vuota**, ed è l'unica.

**I sei domini della sfida a mani nude** (`pedagogia.md` §3) hanno invece una tabella, e la tabella dice una cosa che nessuno dei due documenti diceva:

| dominio | premio possibile | stato |
|---|---|---|
| `informatica` | **nessuno**: i premi sono per le altre discipline, per tua scelta | dichiarato |
| `logica` | **nessuno**: non ha un oggetto proprio, e non è un premio che si possa guardare | dichiarato |
| `calcolo mentale e stime` | **nessuno**, per la stessa ragione | dichiarato |
| `linguistica e testo` | **E** e **F**: le due categorie che si leggono | possibile |
| `Costituzione e cittadinanza` | **I**, lo stesso premio di Diritto | possibile |
| `osservazione e attenzione` | **D** e **B**, e sono le uniche due righe che poggiano su un dominio che il progetto non ha ancora | da_costruire |

Quattro dei sei domini della sfida **non possono avere un premio**. Non è un difetto: è la differenza fra un gioco che premia e un gioco che premia **qualcosa**. La regola che ne segue è che nella tappa a mani nude un dominio senza premio si dichiara come tale, e la tappa vale per la prestazione, non per il premio.


## 3. Le quattro prove che un premio deve superare

Un premio entra nel catalogo solo se le passa tutte e quattro. Le prove sono corto, e ognuna ha una ragione.

| # | prova | perché serve |
|---|---|---|
| **1. Esiste, e si può vedere** | l'opera esiste, l'immagine è libera di diritti, e porta etichetta, autore e data | il progetto vieta le immagini generate e i volti inventati (`lingue-immagini.md` §1): un premio inventato insegna che esistono opere che non esistono |
| **2. Insegna il livello** | chi ha superato quel livello, guardando il premio, deve **riconoscere** in esso qualcosa di ciò che ha imparato | senza questa prova il premio è una decorazione, e la verifica non potrebbe mai dire che sia giusto |
| **3. Non è già nella storia** | l'opera non compare già nella storia della tappa, e non è già il pin o la stanza | se è già nella storia il premio non aggiunge niente: il ragazzo l'ha già visto e il premio diventa un ricordo |
| **4. Non è un duplicato** | due livelli diversi non hanno lo stesso premio | due premi uguali sono uno solo, e il secondo livello è stato trattato come se avesse qualcosa in più |

La prova 3 è quella che Pietro ha scritto lui, per il ferrarese, e vale per tutte le discipline: **il premio è la scoperta**. Per l'anno 1 la cosa è facile e per gli anni dopo è impossibile: le trenta figure di Ferrara sono già tutte nella storia, e i premi dell'anno 1 sono quindi architettura (`D`) e pittura (`B`), non persone.

## 4. I tre numeri possibili, e che cosa cambia

Il catalogo non si può scrivere senza scegliere **quanti premi ci sono**, e i tre numeri possibili sono lontanissimi l'uno dall'altro.

| variante | quanti premi | che cosa si ottiene | che cosa costa |
|---|---|---|---|
| **un premio per livello** | **circa 900**, più i trasversali | ogni livello ha il suo, e la prova 2 è sempre esatta | un catalogo grande quasi quanto il gioco, e 900 oggetti da verificare uno per uno |
| **un premio per voce** | **180**, più i trasversali | l'oggetto di interazione è il premio: si lo incontra e lo si riceve | la prova 2 si indebolisce, perché gli stessi trenta oggetti attraversano cinque anni e non distinguono i livelli |
| **un premio per anno e disciplina** | **circa 50** (sei lingue più quattro ambiti, per cinque anni) | un catalogo piccolo e verificabile, e un ritmo di arrivo che si vede | la prova 2 diventa vera solo all'anno, e il ragazzo riceve meno cose |

**Il numero di cui il progetto non sa ancora niente è quello dei trasversali**: `quadro-trasversale.md` dà i quattro ambiti e i loro cinque passaggi, ma **non dichiara quanti livelli trasversali ci siano per anno**. Senza quel numero le tre varianti non si confrontano, ed è il primo dato che manca.

## 5. Cosa c'è da fare

1. **Il numero dei livelli trasversali**, che è il dato che rende confrontabili le tre varianti di §4.
2. **La variante scelta**: per livello, per voce o per anno. È la decisione di Pietro e cambia il catalogo più di qualunque altra.
3. **Il catalogo**, da generare in `dati/premi.json` dopo la decisione di §4, con i campi `premio`, `categoria`, `disciplina`, `etichetta`, `fonte`, `licenza`, `perche_prova_2`, e compilato solo dopo che le prove 1, 3 e 4 sono soddisfatte una per una.
4. **La LIS**: finché `lingue.md` Q4 è aperta, la riga della tabella dei premi resta **dichiarata vuota** e non viene riempita con un'immagine presa per caso.

## 6. Registro delle modifiche

- **v0.1 (03/10/2026)**: prima stesione. Dieci categorie chiuse, undici discipline con la loro associazione e la colonna «da escludere», quattro prove di ammissione, tre varianti di cardinalità con i numeri accanto. Le tre cose che il documento dichiara e non risolve: **la cardinalità** (che è di Pietro), **il numero dei livelli trasversali** (che il progetto non ha) e **la LIS** (che non si scrive a tavolino). Una riga della tabella — `osservazione e attenzione` — è la stessa lacuna che `pedagogia.md` §3 aveva trovata nelle sei categorie della sfida a mani nude, e le due vanno chiuse insieme o non si chiudono.