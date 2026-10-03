---
titolo: Videogioco "I cinque duchi" — le fonti visive: che cosa il gioco non ha ancora una veste, e dove si prende
versione: 0.3
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte: ricerca su Wikimedia Commons del 02/10/2026; tavolozza da Wikidata e Wikipedia del 03/10/2026; sagome e mura da OpenStreetMap via Overpass API del 03/10/2026; cime e quote da Natural Earth `geography_regions_elevation_points` del 03/10/2026; verifica dei fondi già in dati/mappe/
documenti collegati: videogioco-5-duchi-ritratti.md (v0.2), videogioco-5-duchi-lingue-immagini.md (v0.1), videogioco-5-duchi-percorsi.md (v0.4), videogioco-5-duchi-mappe.md (v0.9), videogioco-5-duchi-luoghi-edifici.md (v0.2), videogioco-5-duchi-audit.md (v0.7), videogioco-5-duchi-tappa-1-01.md (v0.3), AGENTS.md
dati: dati/fonti_visive/fonti_visive.json (v1, 27 voci, 125 candidati), dati/fonti_visive/attestazione.json (v1, vuoto), dati/fonti_visive/tavolozza.json (v1, 18 voci), dati/edifici_footprint.json (v1, 5209 edifici su 54 luoghi), dati/ferrara_fondo.json (v1, 14 tratti di mura), dati/ambienti_livelli.json (v1, 150 ambienti), dati/fonti_visive/colori_cartografici.json (v1, 19 voci), dati/altitudine_manifest.json (v1, tre file di cime: 15, 2 e 26 punti)
---

# Le fonti visive

## 0. Che cosa chiede questo documento

Il gioco ha delle immagini per i **personaggi** (213 schede, 169 ritratti autentici) e per gli **oggetti linguistici** (180 voci, 1120 candidati). Ha i **fondi geografici** (19 file Natural Earth). Il 2 ottobre non aveva altro, e non le aveva mai contate.

Questo documento fa quattro cose: **fa l'inventario** di che cosa ha e che cosa non ha una veste grafica; **cerca le fonti** per ciò che manca, con una ricerca vera su Wikimedia Commons; **costruisce** le sei derivazioni che erano solo un buco dichiarato — la tavolozza, i colori delle carte, le sagome degli edifici, il fondo di Ferrara, gli ambienti dei centocinquanta livelli e le cime con la loro quota; e **giudica l'accuratezza** di tutto questo su tre cose che il progetto chiama *proporzioni, colori, forme*, perché un'immagine «giusta» che viene stirata o scurita mente quanto un'immagine sbagliata.

**Che cosa non è questo documento.** Non sceglie le fonti dei **125 candidati**: sono proposte, e nessuna è stata guardata a vista. Il file `dati/fonti_visive/attestazione.json` è pronto e vuoto, con tutti i campi dichiarati. E non disegna niente: i sei file che ha prodotto sono **dati**, non grafica, e ognuno dichiara la propria fonte e i propri vuoti.

---

## 1. L'inventario: che cosa ha una veste e che cosa no

| Cosa | Stato | Fonte | File nel progetto |
|---|---|---|---|
| **Ritratti dei personaggi** | fatto, 169 su 213 | Commons, con attestazione | `sorgenti/art/out/` (169 PNG a 48×54) |
| **Immagini degli oggetti linguistici** | proposte, 1120 candidati | Commons | `dati/lingue/immagini_oggetti.json` |
| **Fondi geografici** | fatto, 19 file | **Natural Earth**, pubblico dominio | `dati/mappe/` (1,4 MB) |
| **Unità amministrative del mondo** | fatto, 50 unità | **Natural Earth 10m**, pubblico dominio | `dati/mappe/mondo_admin1.json` |
| **Terreno e rilievo** | fatto per 95 luoghi | **Terrarium/SRTM** | `dati/luoghi_gioco.json`, campo `terreno` |
| **Tavolozza dei colori** | **fatto il 03/10/2026**, 18 voci | Wikidata e Wikipedia | `dati/fonti_visive/tavolozza.json` |
| **Sagome degli edifici** | **fatto il 03/10/2026**, 5209 edifici su 54 luoghi | OpenStreetMap, **ODbL** | `dati/edifici_footprint.json` |
| **Fondo di Ferrara** (anno 1) | **fatto il 03/10/2026**, 14 tratti di mura | OpenStreetMap, **ODbL** | `dati/ferrara_fondo.json` |
| **Ambienti dei 150 livelli** | **fatto il 03/10/2026**, 150 su 150 | i documenti del progetto più i tre file sopra | `dati/ambienti_livelli.json` |
| **Colori dei fondi geografici** | **fatto il 03/10/2026**, 19 voci | una scelta dichiarata, non un colore a occhio nel codice | `dati/fonti_visive/colori_cartografici.json` |
| **Cime e quote** | **fatto il 03/10/2026**, 15 + 2 + 26 punti | **Natural Earth**, pubblico dominio | `dati/mappe/mondo_110_altitudine.json` e gli altri due |
| **Medi di trasporto** | **non c'è** | — | — |
| **Epigrafi e iscrizioni** | **non c'è** | — | — |

**Cinque buchi il 2 ottobre, due il 3.** Erano cinque, ed erano cinque problemi diversi. Quattro sono chiusi: la **tavolozza**, le **sagome degli edifici**, il **fondo di Ferrara** e gli **ambienti dei centocinquanta livelli**. Restano due, ed è giusto che restino: i **mezzi di trasporto** servono al percorso del duca e sono un problema di *immagini*, non di geometrie; le **epigrafi** servono al latino e sono un problema di *testo*, non di grafica. Nessuna delle due era un buco che si potesse chiudere con uno script, e sono dichiarate in §7.

**Un sesto buco è stato chiuso lo stesso giorno, e non era un buco di immagini mancanti: era un colore che c'era già e stava nel posto sbagliato.** I colori delle carte geografici stavano scritti nel codice del disegnatore, dove nessuno li leggeva (§3.7); mentre li si cercavano è saltato fuori che un file che non aveva niente a che fare stava dentro `dati/mappe/` e faceva crashare il lettore delle mappe (§7, Q4).

**L'ordine in cui sono stati chiusi è quello giusto, ed è dichiarato perché l'ordine è una decisione.** Prima la tavolozza, che è più piccola e serve a tutto il resto; poi le sagome, che sono il buco più grosso; poi il fondo di Ferrara, che dipende dalle sagome; e infine gli ambienti, che non sono una fonte nuova ma l'assemblaggio dei tre precedenti sui centocinquanta livelli. Il quarto non era un quarto buco: era la domanda «e quindi, che cosa si disegna a ogni tappa?», e senza risponderla i primi tre restano tre tavole isolate.

---

## 2. I fondi geografici: che cosa hanno e che cosa manca loro

I **19 file** di `dati/mappe/` vengono da Natural Earth, **pubblico dominio**, in tre scale: 110m per il mondo, 50m per l'Europa, 10m per la penisola. Non sono GeoJSON: sono un **formato a delta con quantizzazione**, e si leggono solo con `sorgenti/gis/mappe_lettore.py`.

Il conto reale, verificato sui file:

| Scala | File | Dimensione | Che cosa contiene |
|---|---|---|---|
| **Mondo 110m** | 5 file | 111 kB | terre, paesi, regioni, fiumi, laghi |
| **Europa 50m** | 7 file | 652 kB | terre, paesi, regioni, regioni amministrative (1 687 geometrie), 186 città, fiumi, laghi |
| **Penisola 10m** | 7 file | 701 kB | coste, paesi, regioni, regioni fisiche, 622 unità, 212 città, fiumi, laghi |

**I tre limiti che il documento delle mappe dichiara già, e che qui tornano — due risolti, uno ancora vero.**

1. ~~**Le sagome degli edifici non esistono come dato.**~~ **Risolto il 03/10/2026**: `dati/edifici_footprint.json`, 5209 sagome su 54 luoghi, ognuna con `forma`, `altezza_m` e `fonte_altezza` (`osm_height`, `osm_levels`, `assente`). Vengono da OpenStreetMap, autorizzata il 02/10/2026, e viaggiano con **ODbL**. §3.2.
2. **Le altezze non esistono come dato**: misurate nel 24% dei casi a Milano e nel 3% a Roma. Il progetto risponde con il **terreno** — quota, pendenza, esposizione, rilievo locale misurati su SRTM, con errore medio di 12,6 m su 14 punti noti. Sui 5209 edifici effettivamente presi, l'altezza c'è in 588 casi (`osm_height`) e si ricava dai piani in altri 1285 (`osm_levels`): **3336 non hanno niente** e diventano un volume neutro dichiarato. §3.2.
3. ~~**Non c'è un file della città di Ferrara.**~~ **Risolto il 03/10/2026**: `dati/ferrara_fondo.json` ha il perimetro delle mura ricostuito da 14 tratti OSM, 8601 m di perimetro e 4,20 km² di area interna, con tutte le 28 tappe 3. ~~**Non c'è un file della città di Ferrara.**~~ **Risolto il 03/10/2026**: `dati/ferrara_fondo.json` ha il perimetro delle mura ricostruito da 14 tratti OSM, 8601 m di perimetro e 4,20 km² di area interna, con tutte le 28 tappe dell'anno 1 che ci cadono dentro. §3.5.

**Il punto 2 resta il punto aperto, ma il 03/10/2026 è stato costruito un file che va nella stessa direzione e va detto con le sue parole.** `dati/mappe/mondo_110_altitudine.json`, `europa_50_altitudine.json` e `penisola_10_altitudine.json` portano le **cime** di Natural Earth con la loro quota: 15, 2 e 26 punti. Sono cime, non luoghi di gioco, e il file lo dichiara: nessun motore può dedurre la quota di una tappa da un elenco di cime. Ma il punto 2 chiedeva se il gioco ha un dato di quota, e adesso l'ha per il primo volta — per il sottosuolo, non per i luoghi.

**Il formato a delta ha una conseguenza visiva che va detta.** La quantizzazione conserva la forma ma perde la continuità della costa: a 110m il mondo è un'approssimazione onesta, ma un giocatore che guarda l'Italia e un che guarda la Spagna vedono coste con la stessa spessore di errore. La regola che ne segue è che **la scala dichiarata va sulla mappa**, così il giocatore sa che cosa sta guardando: 110m per il mondo è una mappa da navigazione, non una carta topografica.

---

## 3. Le fonti cercate, e i sei file costruiti

La ricerca (`sorgenti/fonti_visive_cerca.py`) ha esaminato **27 voci** in cinque categorie, con termini scelti uno per uno e non tradotti alla cieca. Ha prodotto **125 candidati con licenza libera**. Le categorie che hanno prodotto un **file di dati** sono quelle degli edifici, dei colori e dei fondi (sagome §3.2, colore §3.4, mura di Ferrara §3.5, ambienti §3.6); quelle che non lo hanno prodotto sono i mezzi e le epigrafi, e il perché è dichiarato.

A quei quattro file il 03/10/2026 se ne sono aggiunti **due che non vengono dalla ricerca su Commons** ma da un buco emerso documentando: i **colori delle carte** (§3.7) e le **cime con la loro quota** (§3.8). Sono sei, e sei è il numero che dice §8.

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

### 3.2 Le sagome degli edifici: costruite il 03/10/2026

La fonte è **OpenStreetMap**, autorizzata il 02/10, con ODbL e l'attribuzione «© OpenStreetMap contributors». La ricerca del 02/10 aveva trovato 36 fotografie di edifici italiani — il Duomo di Ferrara, il Castello Estense, Palazzo Schifanoia, San Stefano — ma quelle sono **foto, non sagome**: servono al documentario, non al disegno. La sagoma che il motore disegna è un'altra cosa, ed è **un estratto dei building di OSM per i 54 luoghi che hanno coordinate**, in formato delta come le mappe.

`dati/edifici_footprint.json` è di **1,6 MB** e contiene **5209 edifici su 54 luoghi**, tutti i 54 con almeno un edificio (`luoghi_senza_edifici` è vuoto).

| | |
|---|---|
| Luoghi interrogati | **54**, tutti con coordinate |
| Edifici tenuti | **5209** |
| Edifici scartati | **6470**, e ogni scarto ha un motivo dichiarato: 3372 oltre il tetto del luogo, 3072 anonimi e piccoli, 13 ad anello troppo corto, 13 semplificati troppo |
| Altezza misurata (`osm_height`) | **588** |
| Altezza dai piani (`osm_levels` × 3,2 m/piano) | **1285** |
| Senza altezza: **volume neutro dichiarato** | **3336** |

**Le quattro regole, tutte dichiarate nel file, perché un buco travestito da geometria è il peggiore dei difetti.**

1. **Raggio 250 m attorno al pin.** È una scelta, non un limite della fonte: dichiarata come `raggio_m`.
2. **Cosa è «significativo»**: ha un nome, ha un wikidata, ha un'altezza o dei piani, è di una categoria che il gioco sa nomincare, è patrimonio, oppure ha più di 120 m² di area. Un capannone senza nome e senza misure non viene disegnato come se fosse un palazzo.
3. **Tetto di 140 edifici per luogo.** Oltre, il file tiene i più grandi e dichiara il tetto: altrimenti il centro di Londra mangia il file per un solo tappa.
4. **Altezza assente non si stima.** L'edificio esce con `altezza_m: null` e `fonte_altezza: "assente"`, e il motore ne fa un **volume neutro**. È la stessa regola di §4.3 e la stessa dei 41 luoghi che non hanno coordinate perché non sono luoghi: *un volume che non sa niente si dichiara, non si indovina*.

**I due difetti che sono costati di più, entrambi dichiarati nel codice.**

- **L'interrogazione a Overpass va spezzata.** Con aree concatenate sulla stessa riga l'API risponde `HTTP 400: ';' expected - '(' found`; separate da `;` e su righe nuove funziona. Con aree raggruppate a 6 alla volta c'è stato un `504`: `overpass_spezzato()` dimezza il gruppo e riprova, fino a tre volte, e la scala finale (`GRUPPO=3`) ha fatto passare tutti i 54 luoghi.
- **La prima versione del file aveva il conto sbagliato in un modo invisibile.** Interrogare 54 luoghi in un colpo solo è più semplice e non finisce: alla prima interruzione si perde tutto. Da qui il flag `--riprendi`, che legge il file già scritto e salta i luoghi che ci sono.

### 3.3 Le epigrafi: fonti, non immagini

Le tre voci (lapide, lastra, iscrizione) hanno diciotto candidati, e sono la categoria più semplice: un'epigrafe **è** la sua immagine. Serve però la regola che vale per i testi autentici delle lingue antiche (`lingue.md` §7 Q3): l'epigrafe entra con la sua **trascrizione e la sua traduzione**, non come foto muta.

### 3.4 Il colore: la tavolozza, costruita il 03/10/2026

Quattro voci, ventiquattro candidati, e nessuna tavolozza. Il gioco aveva **tre sistemi di immagini che non concordavano fra loro**: i 213 ritratti, i 1120 candidati degli oggetti, e i fondi geografici. Senza una tavolozza, ogni immagine porta i suoi colori e la scena diventa un muro.

Le quattro voci cercano appunto i **campionari**: le terre d'oliva del paesaggio ferrarese, le tinte dei manoscritti miniati, i motivi dei tessili, i colori degli affreschi. Una tavolozza non si sceglie a occhio: si costruisce da una fonte e si dichiara.

`dati/fonti_visive/tavolozza.json` è **18 voci** e nasce da una scelta di principio, che è quella delle tre regole già prese su etichette e proporzioni: **non si ricolora tutto a una tavolozza unica, si dichiara il colore di ogni fonte**. Le 18 voci si dividono in tre gruppi, e il file dichiara quale dei tre sia:

| Provenienza | Voci | Che cosa è |
|---|---|---|
| `wikidata_p465` | **5** | l'esadecimale dichiarato da Wikidata per un pigmento storico |
| `wikipedia_infobox` | **5** | il campo «color» dell'infobox di un artista, cioè il colore che *quell'artista* usava |
| dichiarata a mano | **3** | terre, bianco calce e fondo di scena: non hanno un codice in nessuna fonte, e il gioco dichiara che sono una scelta |
| stato del gioco | **5** | verde rame, giallo, oro, inchiostro, e i tre colori di stato (ok, attenzione, errore): non sono pigmenti, sono **la grammatica del gioco** |

**I tre difetti che la costruzione ha trovato, e che sono la parte instructive del lavoro.**

1. **Il colore di un pigmento non si cerca per nome.** La ricerca su Wikidata per «vermilion» restituisce una **città della provincia di Alberta**; «red ochre» restituisce un **premio televisivo**; «minium» restituisce **un'alga**. I pigmenti hanno nomi che il motore di ricerca non distingue dagli omonimi. La correzione è che gli **identificatori Wikidata sono espliciti** nella fonte: `tavolozza_campioni.py` non cerca, dichiara.
2. **`P462` non è l'esadecimale: è un link a un oggetto «colore».** Il percorso giusto è a due tappe: pigmento → `P462` → oggetto colore → `P465` → esadecimale. E il valore di `P462` è un **dizionario** (`{"entity-type": "item", ...}`), non una stringa: senza controllarne il tipo finisce nel file come colore, e un dizionario non è un colore.
3. **Cinque pigmenti su quindici non hanno esadecimale da nessuna parte**: il bianco di piombo, l'azzurrite, la malachite, l'orpimento e il giallo di piombo e stagno. Non si è tirata fuori una terna di cifre plausibili: sono in `pigmenti_senza_colore_macchina` con la prova, e le voci ricostruite su altri pigmenti.

**Le due dichiarazioni che rendono il file onesto.** `senza_colore_dichiarato` è **vuoto**: nessuna voce ha un colore inventato. E `campioni_guardati` è **zero**, come i 125 candidati: i campionari non sono stati aperti, e il file non finge di averli guardati.

`dati/fonti_visive/tavolozza_candidati.json` porta, accanto alle 18 voci, le **altre dichiarazioni** trovate (per esempio il vermiglio è `E34234` su Wikidata e `FF4000` sull'infobox: due fonti che dicono cose diverse, entrambe vere, e la scelta va motivata) e le **famiglie di colori senza voce** (i tessili e gli affreschi): dichiarare che manca una voce è diverso dal non averci pensato.

`sorgenti/verifica_tavolozza.py` è il controllo: sei verifiche (A1–A6), con `--offline` per quando la rete non c'è. Eseguito **in rete il 03/10/2026**: 10 fonti ricontrollate, **0 problemi**.

### 3.5 Il fondo di Ferrara: costruito il 03/10/2026

`dati/ferrara_fondo.json` è il fondo cittadino dell'anno 1, e nasce da una domanda che sembrava di disegno e si è rivelata di misura: **che cosa è «dentro le mura»?**

La fonte sono i **14 tratti** che OpenStreetMap ha per `barrier=city_wall` intorno a Ferrara (ODbL, `(c) OpenStreetMap contributors`). OSM non ha l'anello delle mura: ha tratti, con dei vuoti. Il vuoto più grosco è di **1037 m** fra gli ultimi due estremi, e nessuna fonte lo disegna.

**La scelta non è stata fatta a occhio, e questo è il punto.** I tratti sono stati uniti a catena entro una tolleranza, e la tolleranza è stata scelta così: **si tiene la più piccola in cui tutte le tappe del primo anno cadono dentro**. La scala completa è nel file, e i cinque passi sono tutti dichiarati:

| Tolleranza | Vertici | Area interna | Tappe fuori |
|---|---|---|---|
| 5 m | 93 | 0,13 km² | 27 su 28 |
| 15 m | 51 | 0,24 km² | 28 su 28 |
| 25 m | 51 | 0,74 km² | 26 su 28 |
| 40 m | 51 | 1,44 km² | 19 su 28 |
| **60 m** | **54** | **4,20 km²** | **0** |

Il risultato: perimetro **8601 m**, area interna **4,20 km²** contro i 4,8 km² storici, e **28 tappe su 28 dentro**, zero sul bordo, zero fuori. Le due tappe che non hanno coordinate (1-27 e 1-30) sono dichiarate fuori dal controllo: non si possono verificare, e il file non finge che siano dentro.

**Una fonte è stata rifiutata, ed è la più interessante.** OSM ha una relation che si chiama `3875619 «Centro storico»`, sembra fatta apposta e copre 1,34 km². Ma **13 tappe su 28 stanno fuori**, fra cui Piazza Ariostea, Palazzo dei Diamanti e Porta degli Angeli: un perimetro che esclude la piazza dei Diamanti non è il perimetro delle mura, per quanto sia chiamato centro storico. Il nome giusto è la fonte sbagliata, ed è registrata in `fonti_rifiutate` con la prova.

**Un difetto che la scala delle tolleranze ha nascosto, e che va dichiarato.** La prima versione del controllo di «dentro» lavorava in gradi con un raggio di 0,5 — cioè **55 km**: ogni tappa risultava «sul bordo», e la scala delle tolleranze non discriminava niente. Il calcolo di distanza su sferoide è stato corretto, e la tabella qui sopra è quella vera.

Il file dichiara anche i suoi tre limiti: nessun tratto porta `start_date`, quindi **il file non sa quando ogni tratto di mura è stato costruito e non lo deduce**; le mura di origine e quelle dell'Addizione Erculea non sono distinguibili, e il quinto anno lavora sulla stessa area; e la zona percorribile è l'interno delle mura più un margine di 60 m oltre la linea, oltre il quale c'è la nebbia.

### 3.6 Gli ambienti dei centocinquanta livelli: costruiti il 03/10/2026

Il quarto file non è una fonte nuova: è la risposta alla domanda che i primi tre lasciavano senza risposta. **`dati/ambienti_livelli.json` è un ambiente per ognuno dei 150 livelli, 150 su 150**, nell'ordine 1-1, 1-2, … 5-30, ed è costruito sul modello dell'unica zona già esistita: la piazza della Cattedrale di `videogioco-5-duchi-tappa-1-01.md` §3.

Un ambiente porta: il livello, l'argomento, la voce (il personaggio), il luogo, le coordinate, il **tipo** di ambiente con la sua griglia, le sagome che ci sono, il fondo (solo per l'anno 1), la paletta, l'orientamento e — se non si sa — i suoi **vuoti dichiarati**.

**Come sono costruiti, e perché da tre fonti diverse.** L'anno 1 prende le coordinate da `anno1-mappa.md` §3, che le ha già verificate sui numeri civici del Comune; gli anni 2-5 prendono il luogo da `dati/luoghi_gioco.json`, campo `tappe`, che collega livello e luogo **per relazione esplicita e non per confronto di nomi**: confrontare nomi è la tecnica che ha fatto cadere Karakorum sulla catena montuosa, e qui non si rifà.

| | |
|---|---|
| Ambienti | **150** su 150 attesi, nessuno mancante |
| Con coordinate | **99** |
| Con sagome OSM | **69** |
| Già costruiti (quelli che il motore ha disegnato) | **1**, la tappa 1-1 |

I **nove tipi** di ambiente e quante volte compare ciascuno: `citta` 65, `edificio` 32, `citta_antica` 11, `percorso` 11, `situazione` 11, `paesaggio` 7, `porta` 5, `area` 5, `piazza` 3.

**Il tipo non è indovinato in silenzio.** Ogni ambiente dichiara in `tipo_da` da dove viene il suo tipo: dal campo `tipo` del registro dei luoghi quando c'è, e da una **parola chiave** quando non c'è (`cattedrale` → edificio, `piazza` → piazza). Le griglie — colonne, righe, metri per tessera, nove tabelle diverse — sono una **scelta di progetto, non un dato di una fonte**, e stanno tutte nel file perché il motore le legga e nessuno le riscriva nel codice.

**I vuoti sono tutti dichiarati, uno per uno**, e sono la parte più utile del file: `orientamento_non_dichiarato` **150** (solo la 1-1 ha un orientamento, gli altri 149 no, e dichiararlo vuol dire che il motore non deve sceglierlo da solo), `senza_sagome_osm` 81, `coordinate_non_e_un_luogo` 24, `coordinate_da_geocodificare_a_mano` 14, `coordinate_da_geocodificare_wfs` 11, `sole_sagome_senza_altezza` 13, `senza_coordinate` 2.

`sorgenti/verifica_ambienti.py` è il controllo: sei verifiche (B1–B6), **tutte superate il 03/10/2026**.

---

### 3.7 I colori delle carte: costruiti il 03/10/2026

I fondi di Natural Earth non hanno colori: sono geometrie, e il colore glielo decide il motore. La Q4 chiedeva se quei colori dovessero stare **in un file** o **nel codice**, e la risposta è stata un file: `dati/fonti_visive/colori_cartografici.json`, **19 voci**.

**Un colore entra in questo file in due modi, e solo due**, ed è la stessa regola della tavolozza applicata un passo oltre:

| Da dove | Voci | Che cosa dichiara la voce |
|---|---|---|
| dalla **tavolozza** | **3** (`lago`, `etichetta_mappa`, `fondo_gioco`) | la `chiave_tavolozza`, e il controllo ne confronta l'esadecimale **byte per byte** con `tavolozza.json` |
| **dichiarata qui** | **16** | il `motivo` (che cosa è) e il `criterio` (perché proprio questo colore) |

Non esiste un terzo modo, ed è il punto: **nessun colore entra perché stava già nel codice**, e nessuno entra per assomiglianza a un altro.

**La regola che le carte hanno e le immagini non hanno.** Ogni categoria che ha un riempimento ha anche un bordo, e i due si dichiarano insieme: una categoria con il riempimento e senza il bordo è un file che non sa come si disegna, e una con il bordo e senza il riempimento è una linea senza forma.

**Le tre categorie che non hanno un riempimento, e perché è una scelta.** Le **terre emerse** e le **regioni fisiche** si disegnano col solo bordo e lasciano trasparente il fondo della carta: riempirle nasconderebbe i Paesi che ci stanno sopra, e i deserti si distinguono dal Paese che li contiene non riempiendoli. Le **50 unità amministrative del mondo** non hanno un colore proprio e usano quelli di Stato, perché un'unità amministrativa è un Paese come un altro.

**I due colori che il file dichiara ma nessuno disegna, e perché sono dichiarati lo stesso.** `fondo_gioco` è il fondo della scena e non della pagina di verifica: la carta del gioco ci sta sopra e i due bianchi sporchi devono essere lo stesso, ma nessuna delle dodici pagine di verifica lo disegna. Il **colore della nebbia** invece **non è dichiarabile** e sta in `non_dichiarati`: sta nel prototipo generato, che in questo checkout non c'è, e dichiararlo sarebbe dichiarare un colore che nessuno ha potuto misurare.

**Il difetto vero che è saltato fuori cercandoli, e che non era di colori.** `dati/mappe/mondo_admin1_copertura.json` — il file che dichiara come le 50 unità amministrative sono state scelte fra le 4596 della fonte, con quale tolleranza e quali sette che hanno avuto bisogno di una riserva, e quali dei 54 pin ci cadono dentro — stava **dentro `dati/mappe/`**, dove vale la regola che ci stanno solo file nel formato a delta, perché `dati/mappe/` si legge solo con `mappe_lettore.py`. Un JSON valido in quella cartella faceva **crashare il lettore** con un `IndexError: list index out of range`, che è il peggiore dei sintomi: dice una lista troppo corta e non dice che il problema è un file che non aveva niente a che stare lì. Il file è stato spostato in `dati/` — dove è un dato e non una mappa — il lettore ora controlla la forma del file e solleva un `ValueError` che lo dice, e il controllo **C6** tiene la regola ferma.

### 3.8 Le cime e le loro quote: costruite il 03/10/2026

`dati/mappe/mondo_110_altitudine.json`, `europa_50_altitudine.json` e `penisola_10_altitudine.json` portano le **cime** di Natural Earth con la quota sul livello del mare. Sono **15, 2 e 26 punti**, in formato a delta come tutte le altre mappe, e `dati/altitudine_manifest.json` dichiara il conto della fonte accanto al conto del file: 19 punti in entrata e 15 nel file da 110 m, 86 e 2, 711 e 26.

**La scoperta che vale più dei tre file, e che nessuno dei numeri nasconde.** La fonte si chiama `geography_regions_elevation_points` ed è **mondiale in tutte e tre le scale**: la scala è il dettaglio, non l'estensione. Il file da 50 m elenca 86 cime su tutto il globo e solo due in Europa, da longitudine −167 a +160; quello da 10 m ne elenca 711 di cui 26 nel riquadro della penisola. Il manifest lo dichiara in `la_scala_e_l_estensione`, perché un file chiamato «europa» che contiene il Kilimangiaro è un file che mente una volta sola, e quella volta basta.

**E da qui segue la seconda scoperta, che è quella pericolosa: i tre file non sono annidati.** Nessuna delle 15 cime mondiali cade nel riquadro della penisola, e nessuna delle 26 cime della penisola è fra le 15 del mondo: sono **selezioni diverse della stessa fonte globale a dettagli diversi**, non tre risoluzioni dello stesso elenco. Un gioco che li trattasse come piu' e meno risoluzioni sbaglierebbe, e sbaglierebbe invisibilmente, perché tutti i numeri sono giusti.

**Quello che il file non è, dichiarato perché è la parte che si legge.** Non è un modello del terreno: fra due cime c'è solo il vuoto di questa fonte, e nessun motore può dedurre la quota di una tappa da queste cifre. Non è la quota di una città, e il campo `name` lo dice per ogni punto. E la quota è **quella che la fonte scrive**: l'Everest è a **8848 m**, che è il valore del 1954, mentre dal 2020 la quota ufficiale è 8848,86 m. Il file non corregge e non nasconde — è il caso di scuola del quinto anno, dove ogni numero porta con sé l'errore e la data in cui è stato misurato.

**Il lavoro tecnico che ha reso possibile tutto questo è una funzione.** `sorgenti/gis/shapefile_lettore.py` sapeva leggere **poligoni** (`parti()`) e non sapeva leggere un **punto**. La funzione nuova `punti()` legge le forme 1 (`Point`, con X e Y a offset 4) e 8 (`MultiPoint`, che ha un bounding box di 32 byte e il numero dei punti all'offset 36, coi punti che cominciano a 40): la trappola è che il MultiPoint ha *dentro* i punti una struttura che sembrava quella di un poligono, e leggerla con il codice dei poligoni dà coordinate che hanno l'aria di essere giuste.

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

**La regola nuova, che riguarda la tavolozza.** Se le fonti hanno colori che non concordano, il gioco deve scegliere: o usa i colori della fonte e dichiara che sono quelli, oppure applica una **tavolozza unica** e dichiara che l'immagine è ricolorata. La seconda è più bella e meno fedele; la prima è più fedele e meno bella.

**La scelta è la prima, ed è dichiarata in un posto solo**: `dati/fonti_visive/tavolozza.json`. È la stessa scelta che il progetto aveva già fatto tre volte — per i ritratti, per le etichette, per le proporzioni — e che resta la coerente: **ogni fonte porta i suoi colori e li dichiara**, e il gioco non ricolora il dipinto di Cavallini per farlo quadrare con la miniatura. Un posto solo perché due persone che colorano lo stesso dipinto in due modi diversi producono due giochi.

**La stessa regola, un passo oltre, per le carte geografici.** La scelta della tavolozza riguarda le immagini; i fondi di Natural Earth non hanno colori propri e il gioco deve dargliene. La domanda del 2 ottobre era se quei colori stessero **in un file** o **nel codice**, e la risposta è che dal 3 ottobre stanno in un file: `dati/fonti_visive/colori_cartografici.json`, 17 voci (§3.7). La regola è la stessa — ogni colore dice da dove viene — e in più ne vale una che le carte hanno e le immagini non hanno: **una categoria che ha un riempimento ha anche un bordo, e i due si dichiarano insieme**.

### 4.3 Forme

La forma è il contorno, e per il gioco è la cosa più difficile, perché **la forma di un edificio non è un'immagine: è una geometria**.

| Elemento | Che cosa serve | Fonte | Stato |
|---|---|---|---|
| Costa, fiumi, confini | geometrie | Natural Earth | fatto |
| Unità amministrative del mondo | geometrie del primo livello | Natural Earth 10m | fatto, 50 unità |
| Rilievo del terreno | quota e pendenza | SRTM / Terrarium | fatto per 95 luoghi |
| **Sagoma di un edificio** | **geometria della facciata** | **OSM building** | **fatto: 5209 su 54 luoghi** |
| **Perimetro delle mura di Ferrara** | **poligono di chiusura** | **OSM `city_wall`** | **fatto: 14 tratti, 4,20 km²** |
| **Ortofoto aerea** | non serve: il gioco è 3/4 disegnato | — | — |

**La regola sulla forma, che è quella del progetto sui luoghi**: una forma che non è verificata **non si disegna**. Se di un edificio non si sa la pianta, si disegna un volume neutro e la scheda dice che è un volume neutro — che è la regola dei 41 luoghi che non hanno coordinate perché non sono luoghi (`luoghi-edifici.md` §1) e che ora vale anche per i **3336 edifici su 5209** che escono da OSM senza altezza.

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

**Q1 — ~~La tavolozza va prodotta o no?~~ CHIUSA il 03/10/2026**

Il gioco aveva tre sistemi cromatici che non concordano, e finché la tavolozza non c'era
ogni immagine entrava con i suoi colori: il risultato non era un gioco, era un mosaico. La
domanda aveva due metà: **si ricolora tutto a una tavolozza unica** (più bello, meno
fedele) **oppure si dichiara ogni fonte con i suoi colori** (più fedele, meno bello)?
**La seconda**, che è quella che il progetto aveva già scelto tre volte: per i ritratti,
per le etichette, per le proporzioni.

La tavolozza è `dati/fonti_visive/tavolozza.json`, **18 voci**, costruita da fonti e non a occhio: §3.4 e §4.2. La verifica `sorgenti/verifica_tavolozza.py` (sei controlli, A1–A6) è stata eseguita **in rete** il 03/10/2026: dieci fonti ricontrollate, **0 problemi**.

**Q2 — ~~Le sagome degli edifici si costruiscono adesso?~~ CHIUSA il 03/10/2026**

Era il buco più grande, ed era bloccante per gli anni 2-5. Il file c'è: `dati/edifici_footprint.json`, **5209 edifici su 54 luoghi**, in formato delta, con `forma`, `altezza_m` e `fonte_altezza` — §3.2.

**La metà della domanda che riguardava i 95 luoghi è stata corretta, e il motivo va scritto**: non sono 95. Sono **54**, i luoghi che hanno coordinate. Gli altri 41 non sono luoghi (porte di gioco, percorsi fra due città, situazioni) e non hanno niente da sagomare; costruire sagome per loro avrebbe significato inventare il posto in cui si disegna un non luogo. E i 3336 edifici senza altezza diventano un **volume neutro dichiarato**, non una stima.

**Q3 — ~~Il fondo di Ferrara si costruisce?~~ CHIUSA il 03/10/2026**

L'anno 1 è l'anno in cui la copertura è gratuita e la mappa è piccola, e non aveva un file. Il perimetro delle mura è in `dati/ferrara_fondo.json`: 14 tratti OSM, 8601 m di perimetro, 4,20 km² di area interna, con la tolleranza di 60 m scelta perché è la più piccola in cui **tutte e 28 le tappe** ci cadono dentro — §3.5.

**Il perimetro che `motore-e-grafica.md` dice di usare non è un file che si poteva scaricare**, ed è il fatto più utile di questa chiusura: nessuna fonte pubblica ha il perimetro ufficiale delle mura di Ferrara. Quello che c'è è un anello di tratti con dei vuoti, e il vuoto più grosso — **1037 m** — resta senza disegno ed è dichiarato nel file.

**Q4 — ~~I colori dei fondi geografici.~~ CHIUSA il 03/10/2026**

I 19 file Natural Earth hanno proprietà e categorie, ma non colori: il colore lo decideva il motore. La domanda era se quei colori dovessero essere **dichiarati in un file** — così ogni tappa sa che cosa sta mostrando — o restare nel codice, dove nessuno li legge. **La tavolozza copriva metà della domanda**: i colori di stato e di scena c'erano già (`ok`, `attenzione`, `errore`, `sfondo`, `inchiostro`), ma quelli per **categoria cartografica** — terra, mare, confine, città — stavano nel codice. Ora stanno in `dati/fonti_visive/colori_cartografici.json`, **19 voci**: 16 dichiarate con motivo e criterio, 3 prese dalla tavolozza con la chiave dichiarata e l'esadecimale confrontato byte per byte. §3.7.

**Il punto interessante della chiusura è che cercando i colori è saltato fuori un difetto che non era di colori**, ed è la parte che resta da questa domanda: un file che non aveva niente a che fare stava nella cartella sbagliata e faceva crashare il lettore delle mappe. La storia è in §3.7.

**I due controlli che tengono la cosa ferma.** `sorgenti/verifica_colori.py` fa **sette verifiche, C1–C7**: gli esadecimali sono ben formati e le chiavi univoche (C1); le tre voci prese dalla tavolozza **dicono il vero**, confronto byte per byte (C2); le 16 dichiarate portano motivo e criterio (C3); **nessun colore vive solo nel codice** (C4); ogni voce è usata o dichiarata fra le non disegnate (C5); `dati/mappe/` contiene **solo file a delta** (C6); e ogni file di mappa ha colori che lo riguardano, su una tabella di copertura di 18 file (C7). **0 problemi**, e la prova negativa c'è: cinque difetti iniettati danno cinque problemi segnalati.

E `sorgenti/gis/verifica_mappe_disegno.py`, che **non scrive più i colori nel proprio codice ma li legge dal file**, ha reso dodici pagine di verifica. Il suo difetto di prima è instructive: scriveva `fill="F6FAFC"` invece di `fill="#F6FAFC"`, cioè dodici pagine bellissime e senza un colore, perché l'esadecimale senza il cancelletto in SVG non è un colore. È dichiarato nel suo docstring, perché un difetto che si corregge e si dimentica torna.

**Q5 — Chi guarda i 125 candidati?**

Come per gli oggetti linguistici: nessuno è stato guardato a vista, e il file di attestazione è pronto e vuoto. La differenza rispetto agli oggetti è che qui i 125 candidati sono pochi e molto diversi fra loro, e sono **le fonti che decidono l'aspetto del gioco**: scegliere male la carrozza del Quattrocento si vede in tutto il secondo anno.

---

## 8. Il riepilogo, che è la parte che serve

| | |
|---|---|
| Categorie senza veste grafica | il 02/10 erano **cinque**: mezzo, sagome, mappa di Ferrara, epigrafi, tavolozza. Il 03/10 sono **due**: mezzo ed epigrafi |
| Candidati cercati su Commons | **125**, in 27 voci |
| Voci senza immagine | **due**: l'incendio e la carestia |
| Candidati scelti a vista | **zero**, e dichiarato |
| Fondi geografici già pronti | **19 file**, 1,4 MB, Natural Earth, pubblico dominio |
| Tavolozza | **fatto**: 18 voci, 10 da fonti automatiche, 3 dichiarate, 5 di stato |
| Sagome degli edifici | **fatto**: 5209 edifici su 54 luoghi, **3336 senza altezza** e a volume neutro |
| Fondo di Ferrara | **fatto**: 14 tratti, 8601 m di perimetro, 4,20 km², 28 tappe su 28 dentro |
| Ambienti dei livelli | **fatti**: 150 su 150, di cui 99 con coordinate e 69 con sagome |
| Colori delle carte | **fatti**: 19 voci dichiarate, di cui 3 prese dalla tavolozza; nessun colore vive solo nel codice |
| Cime e quote | **fatte**: 15 + 2 + 26 punti su tre scale, con la scoperta che la fonte è **mondiale in tutte e tre** e i tre file non sono annidati |
| Quanti ambienti il motore ha disegnato | **uno**, la tappa 1-1 |
| Lavoro più grande che resta | i **125 candidati** da guardare a vista, e i **cinquantuno** ambienti senza coordinate |
| Lavoro più grande che manca *fra i dati* | nessuno: i sei file ci sono e sono verificati |

---

## 9. Registro delle modifiche

| Data | Versione | Che cosa è cambiato |
|---|---|---|
| 03/10/2026 | 0.3 | **La Q4 è chiusa, e cercando i colori delle carte è saltato fuori un difetto che non era di colori.** I colori per categoria cartografica stavano scritti nel codice del disegnatore: ora sono `dati/fonti_visive/colori_cartografici.json`, **19 voci**, 16 dichiarate con motivo e criterio e 3 prese dalla tavolozza con l'esadecimale confrontato byte per byte, con la regola che **una categoria con il riempimento ha anche il bordo** e le tre che il riempimento non ce l'hanno, dichiarate una per una (§3.7). **Il difetto vero**: `dati/mappe/mondo_admin1_copertura.json stava dentro `dati/mappe/`, dove vale la regola che ci stanno solo file a delta, e faceva crashare il lettore con un `IndexError` che non diceva niente; il file è stato spostato in `dati/`, il lettore ora controlla la forma del file e solleva un `ValueError` che la dice, e il controllo **C6** tiene la regola ferma. **Le cime con la quota** (`mondo_110_altitudine`, `europa_50_altitudine`, `penisola_10_altitudine`: 15, 2 e 26 punti, più `dati/altitudine_manifest.json`), con le due scoperte che i numeri non nascondono: la fonte è **mondiale in tutte e tre le scale** — il file da 50 m elenca 86 cime da longitudine −167 a +160 e solo due in Europa — e **i tre file non sono annidati**, perché sono selezioni diverse della stessa fonte globale (§3.8). Per costruirli è servita la funzione `punti()` in `sorgenti/gis/shapefile_lettore.py`, che legge `Point` e `MultiPoint`, e il difetto che porta con sé è che il `MultiPoint` ha dentro i punti una struttura che sembrava quella di un poligono. Due verificatori nuovi: `verifica_colori.py` (**C1–C7**, con cinque difetti iniettati che danno cinque problemi) e `verifica_altitudine.py` (**D1–D7**, con sei difetti che ne danno sette); `verifica_mappe_disegno.py` è stato riscritto perché **legga** i colori dal file invece di scriverli nel proprio codice, e il suo difetto di prima (`fill="F6FAFC"` senza il cancelletto: dodici pagine senza un colore) è dichiarato nel docstring. Delle cinque questioni resta **solo la Q5**. |
| 03/10/2026 | 0.2 | **Quattro dei cinque buchi sono chiusi, e sono chiusi con quattro file di dati.** **La tavolozza** (`dati/fonti_visive/tavolozza.json`, 18 voci: 5 da Wikidata, 5 dall'infobox di un artista, 3 dichiarate, 5 di stato), costruita da fonti e non a occhio, con tre difetti dichiarati: **un pigmento non si cerca per nome** («vermilion» è una città canadese), **`P462` non è l'esadecimale** ma un link a un oggetto colore — e il suo valore è un dizionario, non una stringa — e **cinque pigmenti su quindici non hanno codice da nessuna parte**, nessuno dei quali è stato riempito con una cifra plausibile. **Le sagome degli edifici** (`dati/edifici_footprint.json`, 1,6 MB, **5209 edifici su 54 luoghi**, 588 con altezza misurata, 1285 ricavata dai piani, **3336 a volume neutro dichiarato**), con le quattro regole dichiarate e i due difetti dell'interrogazione a Overpass. **Il fondo di Ferrara** (`dati/ferrara_fondo.json`, 14 tratti, 8601 m, **4,20 km²**, 28 tappe su 28 dentro) con la tolleranza di 60 m scelta **non a occhio ma come più piccola in cui tutte le tappe cadono dentro**, la scala completa dei cinque passi nel file, e **una fonte rifiutata e dichiarata**: la relation OSM «Centro storico», che lascia fuori Piazza Ariostea e Palazzo dei Diamanti. **Gli ambienti dei centocinquanta livelli** (`dati/ambienti_livelli.json`, **150 su 150**, nove tipi, nove griglie dichiarate come scelta di progetto, tutti i vuoti dichiarati uno per uno), costruiti sul modello della tappa 1-1 e per relazione esplicita fra livello e luogo, non per confronto di nomi. Sei controlli nuovi, due verificatori: `verifica_tavolozza.py` (A1–A6, eseguito **in rete**, 0 problemi) e `verifica_ambienti.py` (B1–B6, 0 problemi). Le Q1, Q2 e Q3 sono chiuse; restano Q4 e Q5. |
| 02/10/2026 | 0.1 | Prima stesura. Inventario delle fonti visive: il gioco ha i ritratti (213), i fondi geografici (19 file Natural Earth, 1,4 MB) e i 1120 candidati degli oggetti linguistici; **non ha** i mezzi di trasporto, le sagome degli edifici, il fondo di Ferrara, le epigrafi e la tavolozza. Ricerca su Commons di 27 voci in cinque categorie: **125 candidati**, due vuoti dichiarati (incendio, carestia). Le tre regole sull'accuratezza — proporzioni, colori, forme — con il caso serio della proiezione delle carte, che non dichiarata mente sulle distanze. I tre difetti della ricerca, con la pipa che è diventata un rospo e la Cappella dei Magi che è un corteo, e la correzione pratica: **le parole ambigue si cercano con due parole**. Cinque questioni aperte. |