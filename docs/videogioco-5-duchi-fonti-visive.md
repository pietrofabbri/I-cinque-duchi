---
titolo: Videogioco "I cinque duchi" — le fonti visive: che cosa il gioco non ha ancora una veste, e dove si prende
versione: 0.1
data: 2026-10-02
autore: Pietro Fabbri (con Claude)
fonte: ricerca su Wikimedia Commons del 02/10/2026, e verifica dei fondi già in dati/mappe/
documenti collegati: videogioco-5-duchi-ritratti.md (v0.2), videogioco-5-duchi-lingue-immagini.md (v0.1), videogioco-5-duchi-percorsi.md (v0.1), videogioco-5-duchi-mappe.md (v0.6), videogioco-5-duchi-luoghi-edifici.md (v0.2), videogioco-5-duchi-audit.md (v0.4), AGENTS.md
dati: dati/fonti_visive/fonti_visive.json (v1, 27 voci, 125 candidati), dati/fonti_visive/attestazione.json (v1, vuoto)
---

# Le fonti visive

## 0. Che cosa chiede questo documento

Il gioco ha delle immagini per i **personaggi** (213 schede, 169 ritratti autentici) e per gli **oggetti linguistici** (180 voci, 1120 candidati). Ha i **fondi geografici** (19 file Natural Earth). Non ha altre cose, e non le aveva mai contate.

Questo documento fa tre cose: **fa l'inventario** di che cosa ha e che cosa non ha una veste grafica; **cerca le fonti** per ciò che manca, con una ricerca vera su Wikimedia Commons; e **giudica l'accuratezza** di quelle fonti su tre cose che il progetto chiama *proporzioni, colori, forme*, perché un'immagine «giusta» che viene stirata o scurita mente quanto un'immagine sbagliata.

**Che cosa non è questo documento.** Non sceglie le fonti: i **125 candidati** che contiene sono proposte, e nessuna è stata guardata a vista. Il file `dati/fonti_visive/attestazione.json` è pronto e vuoto, con tutti i campi dichiarati.

---

## 1. L'inventario: che cosa ha una veste e che cosa no

| Cosa | Stato | Fonte | File nel progetto |
|---|---|---|---|
| **Ritratti dei personaggi** | fatto, 169 su 213 | Commons, con attestazione | `sorgenti/art/out/` (169 PNG a 48×54) |
| **Immagini degli oggetti linguistici** | proposte, 1120 candidati | Commons | `dati/lingue/immagini_oggetti.json` |
| **Fondi geografici** | fatto, 19 file | **Natural Earth**, pubblico dominio | `dati/mappe/` (1,4 MB) |
| **Terreno e rilievo** | fatto per 95 luoghi | **Terrarium/SRTM** | `dati/luoghi_gioco.json`, campo `terreno` |
| **Medi di trasporto** | **non c'è** | — | — |
| **Sagome degli edifici** | **non c'è** (si sa solo da dove verrà) | OpenStreetMap, ODbL | — |
| **Mappa di Ferrara** (anno 1) | **non c'è** (solo le mura) | da costruire | `dati/dettagli_ferrara.json` ha i dettagli, non il disegno |
| **Epigrafi e iscrizioni** | **non c'è** | — | — |
| **Tavolozza dei colori** | **non c'è** | — | — |

**Cinque buchi, e sono cinque problemi diversi.** I mezzi di trasporto servono al percorso del duca appena calcolato; le sagome degli edifici servono a disegnare le città; la mappa di Ferrara serve all'anno 1, che è l'anno in cui la copertura è gratuita e quindi non la si può trascurare; le epigrafi servono al latino; la tavolozza serve a **tutto** il resto, ed è la più urgente perché senza tavolozza ogni immagine entra con i colori propri e il gioco diventa un muro di colori non concordi.

---

## 2. I fondi geografici: che cosa hanno e che cosa manca loro

I **19 file** di `dati/mappe/` vengono da Natural Earth, **pubblico dominio**, in tre scale: 110m per il mondo, 50m per l'Europa, 10m per la penisola. Non sono GeoJSON: sono un **formato a delta con quantizzazione**, e si leggono solo con `sorgenti/gis/mappe_lettore.py`.

Il conto reale, verificato sui file:

| Scala | File | Dimensione | Che cosa contiene |
|---|---|---|---|
| **Mondo 110m** | 5 file | 111 kB | terre, paesi, regioni, fiumi, laghi |
| **Europa 50m** | 7 file | 652 kB | terre, paesi, regioni, regioni amministrative (1 687 geometrie), 186 città, fiumi, laghi |
| **Penisola 10m** | 7 file | 701 kB | coste, paesi, regioni, regioni fisiche, 622 unità, 212 città, fiumi, laghi |

**I tre limiti che il documento delle mappe dichiara già, e che qui tornano.**

1. **Le sagome degli edifici non esistono come dato.** Vengono da OpenStreetMap, che è autorizzato dal 02/10/2026 e viaggia con ODbL. Ogni edificio dovrà dichiarare da dove viene la sagoma e da dove l'altezza (`lidar`, `osm`, `stimata`).
2. **Le altezze non esistono come dato**: misurate nel 24% dei casi a Milano e nel 3% a Roma. Il progetto risponde con il **terreno** — quota, pendenza, esposizione, rilievo locale misurati su SRTM, con errore medio di 12,6 m su 14 punti noti.
3. **Non c'è un file della città di Ferrara.** C'è `dettagli_ferrara.json`, che è la scheda dei dettagli, non il disegno. L'anno 1 ha bisogno di un fondo cittadino che nessuno dei 19 file contiene.

**Il formato a delta ha una conseguenza visiva che va detta.** La quantizzazione conserva la forma ma perde la continuità della costa: a 110m il mondo è un'approssimazione onesta, ma un giocatore che guarda l'Italia e un che guarda la Spagna vedono coste con la stessa spessore di errore. La regola che ne segue è che **la scala dichiarata va sulla mappa**, così il giocatore sa che cosa sta guardando: 110m per il mondo è una mappa da navigazione, non una carta topografica.

---

## 3. Le fonti cercate per i cinque buchi

La ricerca (`sorgenti/fonti_visive_cerca.py`) ha esaminato **27 voci** in cinque categorie, con termini scelti uno per uno e non tradotti alla cieca. Ha prodotto **125 candidati con licenza libera**.

| Categoria | Voci | Candidati | Voci senza immagine |
|---|---|---|---|
| **mezzo** | 11 | 41 | nessuna |
| **edificio** | 6 | 36 | nessuna |
| **epigrafe** | 3 | 18 | nessuna |
| **incidente** | 3 | 6 | **due** (`incendio`, `carestia`) |
| **colore** | 4 | 24 | nessuna |
| **Totale** | **27** | **125** | **due** |

### 3.1 I mezzi di trasporto: la categoria più nuova

È il buco che è nato con i percorsi del duca: undici mezzi, **zero immagini**. La ricerca ne ha trovati quarantuno, e sono le fonti giuste per il Quattrocento, perché il gioco si disegna in un'epoca in cui un mezzo è un'immagine d'epoca.

| Mezzo | Anno | Proposta migliore trovata |
|---|---|---|
| A piedi | 1 | un dipinto di pellegrino |
| Mulo | 2, 3 | una stampa ottocentesca di mulo di somma |
| **Cavallo** | 2, 3 | **la Cappella dei Magi di Benozzo Gozzoli** |
| **Galera** | 2, 3 | **una galera veneziana del Provveditore d'Armata** |
| Nave | 2, 3 | Patinir, un veliero dipinto |
| Carovana | 4 | una carovana di cammelli del Marocco |
| **Diligenza** | 4 | **una stampa di Abel Hold**, pittore di strada |
| Treno | 5 | una foto di ferrovia della Val di Fiemme |
| Aereo | 5 | una foto di volo anni Cinquanta |
| Carrozza | 2, 3 | una carrozza d'epoca |
| Pipa | 2, 3 | **sbagliata**, vedi §5 |

La Cappella dei Magi e la galera del Provveditore sono fonti che il progetto può usare bene: sono italiane, sono d'epoca, e hanno un autore e una data.

### 3.2 Le sagome degli edifici: la fonte è decisa, il file non esiste

La fonte è **OpenStreetMap**, autorizzata il 02/10, con ODbL e l'attribuzione «© OpenStreetMap contributors». La ricerca ha trovato36 fotografie di edifici italiani — il Duomo di Ferrara, il Castello Estense, Palazzo Schifanoia, San Stefano — ma quelle sono **foto, non sagome**: servono al documentario, non al disegno.

**La sagoma che il motore disegna non esiste in nessun file.** Va costruita: un estratto dei building di OSM per i 95 luoghi, in formato delta come le mappe, con `forma`, `altezza` e `fonte_altezza`. È un lavoro, ed è il più grande dei cinque buchi.

### 3.3 Le epigrafi: fonti, non immagini

Le tre voci (lapide, lastra, iscrizione) hanno diciotto candidati, e sono la categoria più semplice: un'epigrafe **è** la sua immagine. Serve però la regola che vale per i testi autentici delle lingue antiche (`lingue.md` §7 Q3): l'epigrafe entra con la sua **trascrizione e la sua traduzione**, non come foto muta.

### 3.4 Il colore: la categoria più urgente e meno considerata

Quattro voci, ventiquattro candidati, e nessuna tavolozza. Il gioco adesso ha **tre sistemi di immagini che non concordano fra loro**: i 213 ritratti, i 1120 candidati degli oggetti, e i fondi geografici. Senza una tavolozza, ogni immagine porta i suoi colori e la scena diventa un muro.

Le quattro voci cercano appunto i **campionari**: le terre d'oliva del paesaggio ferrarese, le tinte dei manoscritti miniati, i motivi dei tessili, i colori degli affreschi. Una tavolozza non si sceglie a occhio: si costruisce da una fonte e si dichiara.

---

## 4. Accuratezza: proporzioni, colori, forme

È la parte che il progetto chiama *solita accuratezza*, e le tre parole hanno tre significati tecnici.

### 4.1 Proporzioni

**La regola che vale per tutte le fonti: nessuna immagine si stira.** Ogni immagine entra nella sua scheda con la sua proporzione, e se non c'entra si ritaglia — dichiarando il ritaglio (`lingue-immagini.md` §4.2).

| Che cosa | Proporzione | Perché |
|---|---|---|
| Ritratto | 8:9, verticale, 48×54 | la persona sta in piedi |
| Scheda oggetto | 4:3, orizzontale, 96×72 | l'oggetto si vede di lato |
| **Carta geografica** | **la proiezione della fonte** | una carta geografica ha un rapporto che dipende dalla latitudine: stenderla in 4:3 mente sulle distanze |
| **Sagoma di edificio** | **quella di OSM** | la facciata ha le sue proporzioni, e sono un fatto storico |

**Il caso della carta geografica è il più serio.** I file di Natural Earth sono in coordinate geografiche, e il motore li proietta. Se la proiezione non è dichiarata, le distanze appaiono sbagliate e non c'è modo di accorgersene guardando. La regola che ne segue è che **ogni carta porta la proiezione scritta**, come porta la scala.

### 4.2 Colori

**Il problema.** Un dipinto del Quattrocento ha i colori che ha adesso, che sono diversi da quelli del Quattrocento; una fotografia d'archivio è in una pellicola che sbiadisce; una stampa ottocentesca è carta, non colore. Se si mettono insieme senza dichiarare, il gioco ha **tre sistemi cromatici** e non lo sa.

**La regola che il progetto si dà, e che è quella dei ritratti**: ogni immagine porta un'**etichetta** che dice che cosa è (`fotografia`, `dipinto`, `incisione`, `miniatura`, `rilievo`, `stampa`). Un'incisione non è una fotografia e non viene trattata come una fotografia.

**La regola nuova, che riguarda la tavolozza.** Se le fonti hanno colori che non concordano, il gioco deve scegliere: o usa i colori della fonte e dichiara che sono quelli, oppure applica una **tavolozza unica** e dichiara che l'immagine è ricolorata. La seconda è più bella e meno fedele; la prima è più fedele e meno bella. **La scelta va dichiarata in un posto solo** — un file `dati/fonti_visive/tavolozza.json`, **da produrre**, che oggi non esiste — perché due persone che colorano lo stesso dipinto in due modi diversi producono due giochi.

### 4.3 Forme

La forma è il contorno, e per il gioco è la cosa più difficile, perché **la forma di un edificio non è un'immagine: è una geometria**.

| Elemento | Che cosa serve | Fonte | Stato |
|---|---|---|---|
| Costa, fiumi, confini | geometrie | Natural Earth | fatto |
| Rilievo del terreno | quota e pendenza | SRTM / Terrarium | fatto per 95 luoghi |
| **Sagoma di un edificio** | **geometria della facciata** | **OSM building** | **non fatto** |
| **Ortofoto aerea** | non serve: il gioco è 3/4 disegnato | — | — |

**La regola sulla forma, che è quella del progetto sui luoghi**: una forma che non è verificata **non si disegna**. Se di un edificio non si sa la pianta, si disegna un volume neutro e la scheda dice che è un volume neutro — che è la regola dei 41 luoghi che non hanno coordinate perché non sono luoghi (`luoghi-edifici.md` §1).

---
## 5. Il difetto della ricerca, che è il più istruttivo del lavoro

La ricerca su Commons ha sbagliato in modi diversi, e sono tre, e vanno dichiarati tutti.

**Il primo difetto: la parola con due sensi.** Alla voce **«pipa»** (che nel Cinquecento è una pianta, la *Tabernaemontana elegans*, da cui si faceva la bevanda), la ricerca ha restituito **il rospo del genere *Pipa***, che è un anfibio sudamericano del Settecento. È lo stesso errore della «correggia» che diventava il pittore Correggio (`lingue-immagini.md` §5): una parola è una parola, non un oggetto.

**Il secondo difetto: la parola giusta, il contesto sbagliato.** Alla voce **«aereo»** (il mezzo di trasporto) è arrivata una foto di un **volo turistico sugli aerei da giardinaggio** di un'azienda italiana. Alla voce **«carrozza»** è arrivata una carrozza **americana del 1922**, che è del gioco del quinto anno travestita di mezzo del Quattrocento. Alla voce **«tavolozza affreschi»** è arrivato un autoritratto di Alessandro Allori, che è un dipinto ma non una tavolozza.

**Il terzo difetto, che è il più serio: la fonte giusta usata male.** Alla voce **«cavallo»** la ricerca ha restituito **la Cappella dei Magi di Benozzo Gozzoli** — che è una delle pitture più belle del Quattrocento italiano, ed è un *corteo di cavalieri a cavallo*, non un cavallo. Usata così com'è, l'immagine del mezzo di trasporto mostra un corteo di trecento persone.

**La regola che ne nasce è la stessa di sempre, e questa volta è verificata su cinque categorie diverse**: una ricerca che restituisce un file non ha trovato l'oggetto, ha trovato una parola. Le tre regole del progetto su questo punto sono ora tutte prese, non dichiarate:

| Progetto | Regola | Dove |
|---|---|---|
| Ritratti | un nome di file non è una prova | `ritratti.md` §1 |
| Oggetti linguistici | nessun candidato nomina l'oggetto → va guardato per primo | `lingue-immagini.md` §5 |
| **Fonti visive** | **una parola che ha due sensi va cercata con due parole** | questo documento, §5 |

**E la correzione pratica, che è la più utile di tutte**: il termine di ricerca di una voce, quando la parola è ambigua, va riscritto con **due parole che non possono confondersi**. Per la pipa: *Tabernaemontana elegans botanical*, non *pipa*. Per l'aereo: *early airliner 1950s*, non *aereo*. Per la carrozza: *Renaissance court carriage*, non *carrozza*. La ricerca va rifatta su quei termini, e il risultato va nel file con i termini accanto, come è già (`fonti_visive.json`, campo `termini`).

---

## 6. I due vuoti dichiarati

**L'incendio e la carestia non hanno immagine.** Sono le due voci su ventisette che la ricerca non ha riempito, e il vuoto è reale: un incendio dell'archivio di Ferrara del 1534 e una carestia del Cinquecento **non hanno immagini d'epoca libere che le illustrino**, perché sono eventi di cui non si è disegnato niente. Le incisioni che esistono sono o di eccesso o di epoca sbagliata.

La regola è quella degli altri buchi: **si dichiara il vuoto**. Una tappa sull'incendio mostra la scheda dell'incendio con scritto perché non c'è immagine, e il testo della fonte — perché **la fonte testuale c'è ed è più affidabile di un'immagine che non c'è**.

Ma c'è una seconda possibilità, e va decisa: il progetto ha già deciso che **l'Africa del *Furioso*** entra riscritta sulla parola del testo (`furioso.md` §6), cioè **il testo al posto dell'immagine**. Lo stesso si può fare qui: l'incendio si rappresenta con **una pagina del registro che brucia**, cioè con la fonte testuale. È la soluzione più onesta e la più economica, e per la carestia forse l'unica.

---

## 7. Le questioni aperte

**Q1 — La tavolozza va prodotta o no? (bloccante per tutto il resto)**

Il gioco ha tre sistemi cromatici che non concordano. Finché la tavolozza non c'è — `dati/fonti_visive/tavolozza.json` è **da produrre** — ogni immagine entra con i suoi colori e il risultato non è un gioco, è un mosaico. La domanda ha due metà: **si ricolora tutto a una tavolozza unica** (più bello, meno fedele) **oppure si dichiara ogni fonte con i suoi colori** (più fedele, meno bello)? La seconda è quella che il progetzo ha già scelto tre volte — per i ritratti, per le etichette, per le proporzioni — ed è la coerente.

**Q2 — Le sagome degli edifici si costruiscono adesso? (bloccante per gli anni 2-5)**

È il buco più grande: OSM è autorizzata da tre giorni e il file non esiste. Serve un'estrazione dei building per i 95 luoghi, in formato delta, con `forma`, `altezza`, `fonte_altezza`. Finché non c'è, le città si disegnano con i volumi neutri che il progetto già prevede per i luoghi senza forma.

**Q3 — Il fondo di Ferrara si costruisce?**

L'anno 1 è l'anno in cui la copertura è gratuita e la mappa è piccola, e non ha un file. `dettagli_ferrara.json` ha i dettagli dei luoghi ma non la geometria. Natural Earth ha i centri abitati ma non la forma della città: **serve il perimetro ufficiale delle mura** (che `motore-e-grafica.md` dice di usare) e le sagome degli edifici, che sono Q2.

**Q4 — I colori dei fondi geografici.**

I 19 file Natural Earth hanno proprietà e categorie, ma non colori: il colore lo decide il motore. La domanda è se i colori siano **dichiarati in un file** — così ogni tappa sa che cosa sta mostrando — o se restino nel codice, dove nessuno li legge.

**Q5 — Chi guarda i 125 candidati?**

Come per gli oggetti linguistici: nessuno è stato guardato a vista, e il file di attestazione è pronto e vuoto. La differenza rispetto agli oggetti è che qui i 125 candidati sono pochi e molto diversi fra loro, e sono **le fonti che decidono l'aspetto del gioco**: scegliere male la carrozza del Quattrocento si vede in tutto il secondo anno.

---

## 8. Il riepilogo, che è la parte che serve

| | |
|---|---|
| Categorie senza veste grafica | **cinque**: mezzo, sagome, mappa di Ferrara, epigrafi, tavolozza |
| Candidati cercati su Commons | **125**, in 27 voci |
| Voci senza immagine | **due**: l'incendio e la carestia |
| Candidati scelti a vista | **zero**, e dichiarato |
| Fondi geografici già pronti | **19 file**, 1,4 MB, Natural Earth, pubblico dominio |
| Lavoro più grande che manca | **le sagome degli edifici** (OSM autorizzata, file mai costruito) |
| Lavoro più urgente che manca | **la tavolozza** (senza, i tre sistemi di immagini non concordano) |

---

## 9. Registro delle modifiche

| Data | Versione | Che cosa è cambiato |
|---|---|---|
| 02/10/2026 | 0.1 | Prima stesura. Inventario delle fonti visive: il gioco ha i ritratti (213), i fondi geografici (19 file Natural Earth, 1,4 MB) e i 1120 candidati degli oggetti linguistici; **non ha** i mezzi di trasporto, le sagome degli edifici, il fondo di Ferrara, le epigrafi e la tavolozza. Ricerca su Commons di 27 voci in cinque categorie: **125 candidati**, due vuoti dichiarati (incendio, carestia). Le tre regole sull'accuratezza — proporzioni, colori, forme — con il caso serio della proiezione delle carte, che non dichiarata mente sulle distanze. I tre difetti della ricerca, con la pipa che è diventata un rospo e la Cappella dei Magi che è un corteo, e la correzione pratica: **le parole ambigue si cercano con due parole**. Cinque questioni aperte. |