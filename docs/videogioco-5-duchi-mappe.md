---
titolo: Videogioco "I cinque duchi" — Le mappe: fondo geografico per gli anni 2, 3 e 4, e dove si prendono i dettagli delle tappe
versione: 1.1
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte del materiale: richiesta di Pietro dell'01/10/2026 («recupera e archivia tutte le mappe che possono essere utili a questo e i prossimi anni»), con l'indicazione di due usi distinti: le mappe generali per costruire un percorso sensato, e le mappe di dettaglio per rappresentare ogni livello nella forma più reale possibile
dati: dati/mappe/*.json (23 file: i 19 del 01/10/2026 da Natural Earth con `sorgenti/gis/mappe_formato.py`, piu `mondo_admin1.json` e i tre `*_altitudine.json` del 03/10/2026), dati/mondo_admin1_copertura.json (v1, il conto della copertura: sta in `dati/` e non in `dati/mappe/`, perche' li' vale la regola del solo formato a delta), dati/edifici_footprint.json (v1, 5209 sagome su 54 luoghi), dati/ferrara_fondo.json (v1, 14 tratti di mura)
documenti collegati: videogioco-5-duchi-motore-e-grafica.md (v0.1, la pipeline che questi dati alimentano), videogioco-5-duchi-luoghi.md (v0.5, la regola che decide *quali* luoghi servono e i tre gradi di ipotesi di coordinata), videogioco-5-duchi-anno2-penisola.md (v0.2), videogioco-5-duchi-anno3-europa.md (v0.4), videogioco-5-duchi-anno4-mondo.md (v0.5), videogioco-5-duchi-anno5-mondo.md (v0.6), videogioco-5-duchi-fonti-visive.md (v0.4), FONTI-E-LICENZE.md, AGENTS.md
---

# Le mappe

Questo documento raccoglie il **fondo geografico** del gioco per gli anni dal secondo in poi, e dice con chiarezza **che cosa si può prendere e che cosa no**.

La domanda di Pietro ha due parti, ed è importante non confonderle:

1. **le mappe generali**, per costruire un percorso sensato — cioè la forma della penisola, dell'Europa, del pianeta, i fiumi, i confini, le città, che servono a piazzare i pin e a far viaggiare il giocatore;
2. **le mappe di dettaglio**, per trovare le «chicche» con cui rappresentare ogni livello nella forma più reale possibile, con le proporzioni giuste.

Sono due problemi diversi, con due fonti diverse, e la parte 2 ha una brutta notizia che va detta subito (§5).

---

## 0. Che cosa è stato fatto, e che cosa è verificato

| | |
|---|---|
| **Scaricate** | 42 livelli shapefile di **Natural Earth**, in tre scale (110m, 50m, 10m) |
| **Prodotti** | **23 file di mappe** in formato proprio in `dati/mappe/` (i 19 del 01/10 più `mondo_admin1.json` e i tre `*_altitudine.json` del 03/10), per un totale di **1,6 MB** |
| **Verifiche** | **61 controlli automatici sulle mappe, tutti superati** (`sorgenti/gis/verifica_mappe_numeriche.py`), più **8 controlli sui pin degli anni dal secondo in poi, tutti superati** (`sorgenti/gis/verifica_pin.py`, §8bis: 71 slot con coordinate su 120), più **5 controlli sui trenta pin del primo anno, tutti superati** (`sorgenti/gis/verifica_anno1.py`, §8ter: 30 tappe dentro le mura) |
| **Licenza** | Natural Earth è **pubblico dominio**: nessun vincolo, nessuna attribuzione richiesta |
| **Prodotto il 03/10** | **le sagome degli edifici** (5209 su 54 luoghi), **il fondo cittadino dell'anno 1** (14 tratti di mura) e **le cime con la loro quota** (15 + 2 + 26 punti, §2.5): le tre cose che §5 e §7 dichiaravano mancanti ognuna per un motivo diverso. E i **colori delle carte**, che erano nel codice e non in un file (`fonti-visive.md` §3.7) |
| **Non è stato possibile** | l'altezza degli edifici come dato unico e affidabile: vedi §5, e la ragione è tecnica, non di volontà |

*(aggiunta — perché la verifica non è un accessorio)* Una mappa che sembra giusta guardandola può avere un anello capovolto, un punto spostato di mezzo grado o un isola ridotta a un segno, e in tutti e tre i casi il disegno resta **ben formato**. Perciò ogni file è passato per controlli numerici: le estremità dell'Italia, i sedici capoluoghi dentro la propria provincia, sette città europee dentro il proprio Paese, sei città fuori dall'Europa che non ci devono essere, e nessun vertice fuori dal mondo. I controlli hanno **trovato cinque difetti reali**, che sono descritti in §6 e che nessuno avrebbe visto a occhio.

---

## 1. Perché Natural Earth, e non un'altra fonte

Il progetto usa già i dati del Comune di Ferrara (`AGENTS.md` §3, `motore-e-grafica.md` §1), che sono ottimi ma arrivano fino al centro di Ferrara: quel WFS ha 544 livelli e nessuno dei cinque anni.

La fonte scelta per le mappe generali deve soddisfare cinque condizioni, tutte necessarie:

| Condizione | Perché è necessaria |
|---|---|
| **pubblico dominio** | il progetto non ha ancora una licenza e `FONTI-E-LICENZE.md` non è compilato: una fonte con attribuzione vincolante aggiungerebbe un obbligo legale a un repository che non l'ha ancora deciso |
| **copertura mondiale** | l'anno 4 è il pianeta, e deve funzionare anche per la Luna e per i luoghi del *Furioso* |
| **tre scale** | una sola scala non va bene: il mondo intero e la penisola sono richieste visive diverse |
| **formato vettoriale** | il gioco disegna forme, non sfondi |
| **ragionevole nel peso** | il prototipo è una sola pagina HTML: 1,4 MB di mappe è accettabile, 40 MB no |

Natural Earth le soddisfa tutte e cinque. È la scelta che non crea problemi, ed è la ragione per cui non si è cercato altro.

*(proposta — alternativa da tenere presente)* Se un giorno servisse la **forma delle coste** più fine di quanto Natural Earth dia (per esempio per la tappa su un porto o un delta), la fonte naturale è **OpenStreetMap**, che però è **ODbL**: obbliga ad attribuire «© OpenStreetMap contributors» e a distribuire eventuali database derivati con la stessa licenza. È una scelta che spetta a Pietro, e va presa prima di scaricare qualcosa, non dopo.

---

## 2. Che cosa c'è in `dati/mappe/`

### 2.1 Anno 4 — il mondo (scala 110m)

| File | Contenuto | Dimensione |
|---|---|---|
| `mondo_110_paesi` | i confini di tutti gli Stati del pianeta, con popolazione e continente | 49 kB |
| `mondo_110_terre` | le terre emerse, cioè il profilo del mondo senza i mari | 21 kB |
| `mondo_110_regioni` | le regioni fisiche: deserti, catene, pianure, tundre, foreste | 36 kB |
| `mondo_110_fiumi` | i fiumi principali del mondo | 2 kB |
| `mondo_110_laghi` | i laghi principali | 2 kB |

Questi cinque file sono la base della colonna stratigrafica degli anni 4 e 5 (`S60`–`S95`): il giocatore scende lungo una colonna che attraversa il pianeta, e le fasce sono geograficamente vere.

### 2.2 Anno 3 — l'Europa (scala 50m)

| File | Contenuto | Dimensione |
|---|---|---|
| `europa_50_paesi` | i confini degli Stati europei, con nome italiano | 61 kB |
| `europa_50_terre` | il profilo delle terre emerse europee | 47 kB |
| `europa_50_regioni` | le regioni fisiche: Alpi, Carpazi, pianure, fiordi | 38 kB |
| `europa_50_regioni_amministrative` | le unità amministrative di **1º livello** di tutta l'Europa, cioè regioni, province, Bundesländer, voivodati, e anche le unità **di secondo livello** dei Paesi che le hanno | 450 kB |
| `europa_50_citta` | 186 città europee con popolazione e posizione | 34 kB |
| `europa_50_fiumi`, `europa_50_laghi` | acque | 18 kB |

`europa_50_regioni_amministrative` è il file più grosso del pacchetto (450 kB, 1 687 geometrie). È anche quello che rende possibile la domanda giusta per l'anno 3: **non «dov'è Atene» ma «Atene è in quale parte dell'Europa»**.

### 2.3 Anno 2 — la penisola (scala 10m)

| File | Contenuto | Dimensione |
|---|---|---|
| `penisola_10_paesi` | i Paesi che toccano il riquadro italiano, con nome italiano | 157 kB |
| `penisola_10_regioni` | **622 unità** d'Italia: regioni e province | 321 kB |
| `penisola_10_coste` | le coste d'Italia e delle isole | 117 kB |
| `penisola_10_citta` | 212 città italiane e dei Paesi confinanti, con popolazione | 41 kB |
| `penisola_10_fiumi`, `penisola_10_laghi` | acque | 17 kB |
| `penisola_10_regioni_fisiche` | Alpi, Appennini, Valli Padane, tavolati, coste | 44 kB |

La scala 10m è la più fine delle tre: la quantizzazione è di **mezzo metro**, che per una mappa disegnata in stile Pokémon è più che sufficiente a far riconoscere la forma della Costiera Amalfitana o il delta del Po.

### 2.4 Il mondo, tutte le unità (scala 10m, del 03/10/2026)

Il 03/10/2026 sono entrati in `dati/mappe/` due file che chiudono il buco di copertura che §8bis dichiarava: **le unità amministrative di primo livello del mondo intero**. La fonte è Natural Earth 10m `admin_1_states_provinces`, **pubblico dominio** come tutto il resto del pacchetto.

| File | Contenuto | Dimensione |
|---|---|---|
| `mondo_admin1` | **50 unità** di primo livello, col codice del Paese | 24 kB |

Il **conto della copertura** — quante unità c'erano nella fonte, quante sono finite nel file, sette con quale tolleranza di riserva, e quali dei 54 pin ci cadono dentro — sta in **`dati/mondo_admin1_copertura.json`**, e **non** in `dati/mappe/`. Non è una scelta di collocazione: `dati/mappe/` contiene solo file nel **formato a delta** di §3, perché quella cartella si legge con `mappe_lettore.py`. Un JSON valido li dentro faceva crashare il lettore, ed è una storia che vale la pena raccontare perché il sintomo non diceva niente.

**Non sono le 4596 unità della fonte: sono 50**, e non è una scelta di comodità. Il gioco ha 54 pin che devono cadere in una unità verificabile, e si tiene **l'unità che contiene il proprio pin**, non quella che il nome del pin nomina: è punto-in-poligono sul pin, ed ogni unità scelta porta annotato il pin che l'ha fatta scegliere. Il riquadro di 0,75 gradi che circonda ciascun punto serve solo a far risparmiare spazio ai bordi del file.

**La semplificazione non è fissa, ed è il dettaglio che rende il file onesto.** Ogni anello viene semplificato finché contiene ancora il proprio pin, con tolleranze di riserva dichiarate: il default è 0,05 gradi, cioè circa 5 km, e **sette unità su 50** hanno avuto bisogno di scendere a 0,02 o 0,01 — New York, Buenos Aires, Istanbul, Venezia, Taranto, Westminster, Siena. Un file che semplifica tutto uguale sembra pulito, ed è quello che fa cadere fuori i pin.

Il conto che il file porta scritto è **54 pin coperti su 54**, ed è la risposta definitiva alla domanda che §8bis lasciava aperta.

---

### 2.5 Le cime e le loro quote (del 03/10/2026)

Il 03/10/2026 è stato convertito anche `geography_regions_elevation_points`, che dal 01/10 era scaricato e non ancora trasformato: sono i tre file `*_altitudine.json`, **15, 2 e 26 punti**. Il conto della fonte accanto al conto del file è in `dati/altitudine_manifest.json`: 19 punti in ingresso e 15 nel file da 110 m, **86 e 2**, **711 e 26**. Sono 43 punti in tutto, per 9 kB: è la fonte più economica del pacchetto e quella che ha dato il maggior numero di sorprese.

**La prima sorpresa è che la fonte è mondiale in tutte e tre le scale.** Il file si chiama `europa_50_altitudine` e contiene due cime — Elbrus e Monte Bianco — mentre gli altri 84 punti vanno da longitudine −167 a +160. Non è un errore della selezione: `geography_regions_elevation_points` è un file **globale** e la scala che ne precede il nome è il **dettaglio**, non l'estensione. Il manifest lo dichiara in `la_scala_e_l_estensione`, perché un file che si chiama «europa» e contiene il Kilimangiaro mente una volta sola, e quella volta basta.

**La seconda è più insidiosa, perché i numeri sono tutti giusti: i tre file non sono annidati.** Nessuna delle 15 cime mondiali cade nel riquadro della penisola, e nessuna delle 26 cime della penisola è fra le 15 del mondo. Sono **selezioni diverse della stessa fonte globale a dettagli diversi**, non tre risoluzioni dello stesso elenco. Un motore che li trattasse come piu' e meno risoluzioni sbaglierebbe senza che nessun controllo numerico lo venisse a dire, perché ogni vertice sarebbe legittimamente dove deve stare.

**Che cosa il file non è, e perché è scritto dentro il manifest e non solo qui.** Non è un modello del terreno — fra due cime c'è solo il vuoto della fonte, e nessuna quota di tappa si può dedurre da queste cifre. Non è la quota di una città: sono cime, e il campo `name` lo dice per ogni punto. E la quota è **quella che la fonte scrive**: l'Everest è a **8848 m**, il valore del 1954, mentre dal 2020 la quota ufficiale è 8848,86 m. Il gioco non corregge e non nasconde — è il caso di scuola del quinto anno, dove ogni numero porta con sé l'errore e la data in cui è stato misurato.

**Il lavoro tecnico è stato una funzione, non uno script.** `sorgenti/gis/shapefile_lettore.py` sapeva leggere **poligoni** (`parti()`) e non sapeva leggere un **punto**: la funzione nuova `punti()` copre le forme 1 (`Point`, con X e Y all'offset 4) e 8 (`MultiPoint`). La trappola del `MultiPoint` è che porta dentro i punti una struttura che somiglia a quella di un poligono — bounding box di 32 byte, numero dei punti all'offset 36, punti da 40 — e leggerlo con il codice dei poligoni dà coordinate che hanno l'aria di essere giuste. È il caso di scuola del **numero che sembra giusto**: va nel docstring, non solo nel codice.

---

## 3. Il formato, e perché esiste

I file non sono GeoJSON. Sono in un **formato proprio a delta**, ed è una scelta deliberata.

Il formato è:

```
{"q": <gradi per unita' intera>,
 "f": [ [{props}], ["dx,dy;dx,dy;..."], ["dx,dy;..."], ... ],
 "p": [ [{props}, lon, lat], ... ]}
```

`q` è la quantizzazione: a 20 000 unita' per grado ogni passo è mezzo metro. Ogni vertice è memorizzato come **differenza dal vertice precedente**, per cui i numeri diventano piccoli (`-62,1204`) e il file intero scende a un decimo.

Il lettore è `sorgenti/gis/mappe_lettore.py`, e restituisce coordinate in gradi decimali: **il motore non deve sapere nulla della codifica**. Il formato è lo stesso di quello già usato in `gis/citta_centro.json`, e per la stessa ragione: l'anno 1 ha già stabilito la convenzione.

*(aggiunta — la conseguenza che va detta)* Un file che non è JSON valido non si può aprire con `json.load`. È una scelta, non un errore, ma va dichiarata: chi toccherà questi dati userà il lettore, non `json.load`.

**E da questa scelta viene un invariante, che il 03/10/2026 è stato infranto per un giorno e che vale la pena scrivere.** `dati/mappe/` contiene **solo** file nel formato di sopra. Un file in un altro formato — per quanto giusto e ben documentato — non è un file che si può tenere li dentro, perché ogni lettore di quella cartella è il lettore e nient'altro.

**Il difetto che l'invariante non dichiarava, e che è il primo dei due trovati il 03/10.** `mondo_admin1_copertura.json` ci stava, ed è stato generato da `mondo_admin1.py` in un momento in cui la regola non era scritta da nessuna parte. Il lettore lo leggeva come una mappa a delta e moriva con `IndexError: list index out of range`: il peggiore dei sintomi, perché dice una lista troppo corta e non dice che il problema è un file che non aveva niente a che fare li. Il file è stato spostato in `dati/`, il generatore è stato corretto, e **il lettore ora controlla la forma del file** e solleva un `ValueError` che nomina il file e il formato atteso invece di far crashare qualcosa a caso. Il controllo **C6** di `sorgenti/verifica_colori.py` tiene l'invariante fermo: è la parte dei colori che dice la verità, ed è la parte che si accorge che in quella cartella c'è qualcosa che non dovrebbe esserci.

---

## 4. Il percorso sensato: come si usa tutto questo

La domanda di Pietro non è «disegna la mappa», ma «fai in modo che il percorso sia sensato». Le mappe servono a tre cose in concreto.

### 4.1 Il pin non è mai un punto a caso

Ogni tappa degli anni 2, 3 e 4 ha un pin. Il pin esiste già nei documenti degli anni (`pin` nella tabella delle tappe), ma finora nessuno lo aveva controllato contro una mappa: erano coordinate scritte a mano. Con questi file si può **verificare ogni pin** chiedendo «dentro quale Paese, dentro quale regione, dentro quale provincia?», e la risposta deve essere quella che il gioco dice.

`punto_in_poligono.py` esiste per questo, e la verifica ne ha già usato 23 capoluoghi come prova.

### 4.2 I posti di passaggio per i personaggi facoltativi

*(la parte della richiesta che non si può liquidare)* Pietro ha detto che dal secondo anno si potrà andare avanti e indietro e includere posti di passaggio per i personaggi facoltativi. È una conseguenza diretta del fatto che esistono più di trenta personaggi per anno: gli obbligatori sono trenta, gli altri sono decine.

I file `*_citta` sono la risposta: **212 città per l'anno 2, 186 per l'anno 3**, ciascuna con nome, posizione e popolazione. Il percorso può attraversare città che non sono pin di nessuna tappa, e il giocatore può sostare dove non era previsto. È la versione economica di «andare avanti e indietro»: non serve una mappa per tappa, serve una mappa continua con dei nomi sopra.

*(proposta)* La regola che renderebbe questa cosa elegante: **una città è raggiungibile se ha almeno 20 000 abitanti**, e le altre si mostrano come un punto senza nome. Così la mappa non si riempie di paesi che il giocatore attraversa senza vedere, e la dimensione del punto dice quanto importante è la città — che è anche un fatto, non una scelta grafica.

### 4.3 Le forme che rendono leggibile la differenza temporale

Gli anni 2-4 hanno tutti la stessa meccanica di fondo: la colonna degli strati, e l'illusione che due cose vicine nella colonna siano vicine anche nel mondo. Il giocatore deve vedere che **la distanza geometrica non è la distanza storica**, e questi file lo permettono in modo diretto: si può mostrare che Bologna e Ferrara sono a 40 km e separate da secoli, e che Atene e Roma sono vicine sulla carta e lontanissime nella storia.

---

## 5. Le «chicche» e i dettagli delle tappe: la notizia scomoda

*(questa è la parte che risponde alla seconda metà della domanda, ed è il risultato più utile del lavoro)*

Il progetto ha già la pipeline giusta per un anno: a Ferrara le sagome e le altezze vengono dal **LIDAR del Comune** (`Fabbricati_USAGE_preview`, altezza calcolata come differenza fra modello della superficie e modello del terreno). Per l'anno 1 il risultato è buono e la ricetta è nota.

Il problema è che **quel WFS esiste solo per Ferrara**, e non c'è un equivalente nazionale. Le tre fonti candidate sono state valutate davvero, con interrogazioni vere, non a memoria:

| Fonte | Che cosa dà | Esito della prova |
|---|---|---|
| **OpenStreetMap** via Overpass | sagome degli edifici ovunque, e talvolta l'altezza | **le sagome ci sono, le altezze no.** Prove fatte il 01/10/2026: Milano, rione Duomo — 50 edifici, **24 con livelli, 2 con altezza**; Roma, Colosseo — 223 edifici, **6 con altezza, nessun livello**; Ferrara, piazza — 29 edifici, **7 con altezza** |
| **Google Earth / OSM 3D** | modelli 3D di edifici reali | non sono dati apribili e licenziabili: **non usabili** |
| **Dati comunali** | sagome e altezze LIDAR | **esistono, ma comunque**: ogni Comune pubblica i propri, con formati diversi |

La conclusione è netta e va scritta perché evita di perdere settimane:

> **l'altezza degli edifici non è un dato che si scarica da una fonte unica e affidabile.** Nel punto in cui si misura, si trova nel 24% dei casi a Milano e nel 3% a Roma. Un modello che usa l'altezza OSM dove c'è e stima dove manca produce edifici sbagliati con aria di esatti, che è il peggiore dei due.

### 5.1 Che cosa si può fare, allora

La risposta che funziona è **a tre livelli**, ed è la stessa logica che il progetto usa già per la facciata della Cattedrale:

| Livello | Che cosa | Fonte | Quando |
|---|---|---|---|
| **1. Forma** | sagoma dell'edificio, dal filo di tetto | OSM Overpass, o il WFS comunale se c'è | sempre |
| **2. Altezza** | altezza reale | LIDAR comunale, dove esiste | solo dove esiste |
| **3. Altezza stimata** | livelli × altezza di piano, con la fonte dichiarata | `building:levels` OSM, altrimenti stima documentata | ovunque manchi la 2 |

La regola che rende onesto il gioco è che **la scheda di ogni edificio dice da dove viene la sua altezza**: `lidar`, `osm`, `stimata`. È la stessa trasparenza del registro dell'anno 4, che ha il campo `attendibilita` e il campo `manca`.

*(proposta — la conseguenza didattica)* Il gioco può **direglielo al giocatore**: «l'altezza di questo edificio è misurata, l'altezza di quello è stimata». È la stessa lezione del quinto anno portata dentro la grafica: **un numero è sempre accompagnato dall'errore e dalla sua provenienza**. Il documento dell'anno 5 §6.1 chiede esattamente questo, e la grafica lo rende visibile.

### 5.2 Il budget di 30 tappe

Trenta tappe all'anno, e per ognuna servirebbe una zona percorribile. Il WFS di Ferrara ha prodotto 11 185 edifici per il centro storico e la zona 1 copre 145 m di piazza. FARE lo stesso per trenta tappe in Trent'anni di storia è un progetto di mesi per anno.

*(proposta — la scala giusta)* Le zone percorribili si fanno solo dove il luogo **è** lo spazio del gioco, e le altre si fanno a pin con la forma dall'alto. Con questa regola l'anno 1 ha trenta tappe e una sola zona percorribile, e funziona già.

---

## 6. I cinque difetti che la verifica ha trovato

Sono qui perché **uno di questi li avrebbe trovati tutti a occhio**. Il primo file prodotto era ben formato, della dimensione giusta, e con la Sardegna ridotta a un segno.

| # | Difetto | Come si manifestava | Come è stato trovato | Correzione |
|---|---|---|---|---|
| **1** | **Douglas-Peucker su anello chiuso** | il segmento che chiude l'anello ha lunghezza zero, l'algoritmo lo tratta come un punto e butta via quasi tutti i vertici: la Sardegna si riduceva a un segno e **Cagliari cadeva fuori dall'Italia** | punto-in-poligono su 58 città | `dp_chiuso()`, che toglie il vertice duplicato prima di semplificare |
| **2** | **ritaglio geometrico dei poligoni** | ritagliare un poligono con il riquadro produce un anello **auto-intersecante** se il poligono esce e rientra: il controllo diceva che **Venezia era dentro la Baviera** | prova su Venezia | i poligoni non si ritagliano più: si tiene il poligono intero e lascia il ritaglio al motore |
| **3** | **delta che non riparte a ogni anello** | il lettore ripartiva da zero, lo scrittore no: tutti gli anelli interni erano spostati | confronto fra primo e secondo vertice di ogni anello | il delta riparte a ogni anello, in scrittura e in lettura |
| **4** | **città scartate** | in pyshp un punto ha `parts` vuoto, il ciclo non produceva segmenti, e tutte le città sparivano | il file città era vuoto, 0 punti | gestione esplicita del `PointShape` |
| **5** | **tropleranza di semplificazione** | 0,012 gradi sono **1,3 km**: la costa si sposta e le città costiere finiscono fuori dal proprio Paese | Cagliari, Livorno, Marsala fuori | tolleranza abbassata a 0,002 (200 m) |

*(aggiunta)* Il quinto difetto è il più importante per il progetto, e non perché fosse il più grave: **è quello che parla della differenza tra una mappa che sembra vera e una mappa che è vera alla scala giusta**. Una mappa con la Sardegna disegnata male sembra uguale a una corretta finché non ci metti dentro un punto.

### 6.1 Due cose che sembrano errori e non lo sono

Segnate qui perché sono state scambiate per difetti due volte, e perché un controllo futuro le deve riconoscere:

- **Città del Vaticano e San Marino cadono dentro il poligono dell'Italia.** Il poligono italiano di Natural Earth non ha un buco per le enclave. Non è un errore dei dati, è una scelta della fonte.
- **L'estremo ovest d'Italia è a 6,6° E (Val d'Aosta), non a Capo Spartivento.** E l'estremo sud è **Lampedusa** (35,49° N), non Portopalo. Era un errore del controllo, non dei dati.

---

## 7. Che cosa manca, e da dove si prende

| Serve | Fonte | Stato | Licenza |
|---|---|---|---|
| Fondo del mondo, Europa, penisola | Natural Earth 110/50/10m | **fatto e archiviato** | pubblico dominio |
| Altezze degli edifici a Ferrara | WFS del Comune | già nel progetto | CC BY 4.0 |
| Sagome degli edifici ovunque | OSM Overpass | **fatto il 03/10/2026**: 5209 sagome su 54 luoghi | **ODbL** |
| Altezze degli edifici fuori Ferrara | nessuna fonte unica | **irrisolto**: 24% a Milano, 3% a Roma | — |
| Altezza sul mare, rilievo | Natural Earth `elevation_points` | **fatto il 03/10/2026**: 15 + 2 + 26 cime con la quota, in `dati/mappe/*_altitudine.json`, con il conto in `dati/altitudine_manifest.json` (§2.5) | pubblico dominio |
| Linee elettriche, ferrovie | OSM Overpass | da costruire | ODbL |
| Fondo cittadino dell'anno 1 | OSM Overpass, `barrier=city_wall` | **fatto il 03/10/2026**: 14 tratti, 4,20 km² | **ODbL** |
| Ambienti dei 150 livelli | i tre file sopra piu i documenti | **fatto il 03/10/2026**: 150 su 150 | — |
| Idrografia minore per l'anno 2 | OSM o idrografia regionale | da valutare | — |

*(aggiunta — la decisione che andava presa presto, poi presa il 02/10/2026: vedi §10 Q1)* **ODbL è una scelta di Pietro, non mia.** Prima di scaricare dati da OpenStreetMap va deciso se il progetto accetta l'obbligo di attribuzione e la condivisione della stessa licenza per i database derivati. La raccomandazione è di **usare Natural Earth per tutto ciò che è possibile** e riservare OSM ai soli edifici, dichiarandone la provenienza edificio per edificio.

---

## 8. Verifiche fatte su questi dati

*(la fonte dei numeri è `sorgenti/gis/verifica_mappe_numeriche.py`, eseguito il 01/10/2026)*

| Controllo | Risultato |
|---|---|
| estremità d'Italia (ovest, est, sud, nord) con tolleranza 0,12° | **4 su 4** |
| riquadro di ingombro dell'Italia: lon 6,60–18,52, lat 35,49–47,09 | **conforme** |
| 16 capoluoghi dentro la propria provincia | **16 su 16** |
| ogni città in una sola provincia, e non in una sbagliata | **3 su 3** |
| 7 città europee dentro il proprio Paese | **7 su 7** |
| 6 città fuori dall'Europa assenti dal file europeo | **6 su 6** |
| 212 città archiviate: nessuna di un Paese lontano dentro l'Italia | **conforme** |
| nessun vertice fuori dal mondo, in tutti i 23 file | **conforme** |
| **totale** | **61 su 61** |

*(fatto il 02/10/2026)* Il controllo sui pin è in §8bis: **72 slot di pin hanno coordinate e sono stati verificati tutti**, e ne sono usciti **due difetti reali**, corretti.

*(fatto il 03/10/2026)* Il primo anno ha **cinque controlli suoi** in §8ter: `sorgenti/gis/verifica_anno1.py`, **A1-A5**, tutti superati.

*(fatto il 03/10/2026)* Sul pacchetto delle mappe sono passati altri due verificatori, che non controllano la geometria ma le cose intorno. `sorgenti/verifica_colori.py` (**C1–C7**) controlla che nessun colore delle carte viva solo nel codice, che le voci dichiarate dicano la verità sulla tavolozza, che **in `dati/mappe/` ci sia solo il formato a delta** e che ogni file di mappa abbia i colori che lo riguardano: 18 file in tabella, **0 problemi**. `sorgenti/gis/verifica_altitudine.py` (**D1–D7**) controlla che le cime cadano nel riquadro dichiarato, che abbiano nome e quota intera, che il conto del manifest torni, che l'Everest sia 8848 e che ci sia una quota negativa: **0 problemi**.

---

## 8bis. I pin degli anni dal secondo in poi, verificati uno per uno

*(fatto il 02/10/2026 — `sorgenti/gis/verifica_pin.py`, otto controlli, tutti superati; il primo anno è coperto da §8ter, dal 03/10/2026)*

È il controllo che §8 dichiarava mancante, e che l'audit chiamava **B5**: non una domanda, un lavoro.

### Che cosa è stato verificato, e che cosa non

Il numero «90» dell'audit era **esatto**, ma non era il numero dei pin: è il numero degli **slot di pin**, uno per tappa. Con il quinto anno la tabella completa è questa:

| Anno | slot | con coordinate | posti distinti |
|---|---|---|---|
| 2 | 30 | 14 | 21 |
| 3 | 30 | 26 | 26 |
| 4 | 30 | **14** | 30 |
| 5 | 30 | 18 | 27 |
| **2-5** | **120** | **72** | **95** |
| **2-4** (la B5) | 90 | **54** | 69 |

*(03/10/2026: erano 71 e 53. Il quarto anno ne ha guadagnato uno perché **Pataliputra** ha ottenuto una coordinata verificata quando il geocodificatore l'ha cercata, e l'anno 3 nessuno perché la **3-28** è diventata Torino, che aveva già coordinate dove Manchester aveva una sua. Il totale dei posti distinti non cambia: 95, e Pataliputra sostituisce Manchester.)*

I 48 slot senza coordinate hanno tutti uno stato dichiarato: 23 `non_e_un_luogo` (porte e situazioni, che per definizione non sono un luogo), 14 `da_geocodificare_a_mano` e 11 `da_geocodificare_wfs`. **Nessuno è un buco silenzioso**, ed è quello che il controllo 7 verifica: ogni pin con coordinate ha un Paese atteso dichiarato nella tabella del verificatore.

### Gli otto controlli

| # | Controllo | Soglia | Esito (anni 2-5) |
|---|---|---|---|
| 1 | nessun pin cade in mare | 3 km dalla terra | **1 su 1** (Costantinopoli, terra a 1,4 km) |
| 2 | il pin cade nel Paese che il nome dichiara | — | **54 su 54** confrontabili |
| 3 | il pin cade nell'unità amministrativa che il nome dichiara | — | **54 su 54** verificabili |
| 4 | il pin è entro 30 km dal centro omonimo archiviato | 30 km | **19 su 19** |
| 5 | nessuna coordinata duplicata fra due pin | — | **0** |
| 6 | nessuna coordinata presa da un altro pin e scambiata | — | **0** |
| 7 | ogni pin con coordinate ha un Paese atteso dichiarato | — | **0 mancanti** |
| 8 | ogni difetto trovato è dichiarato nel file di luoghi | — | **0 non dichiarati** |

### Il quinto anno: quindici pin, nessun difetto

Il quinto anno era l'unico che nessuno aveva guardato, e `verifica_pin.py` gira su di lui senza modifiche (`--anno 5`). **15 posti con coordinate, 30 slot, e nessun difetto**: tutti i Paesi giusti, tutte le unità amministrative giuste fra le cinque verificabili, tutti i centri entro 30 km dove il confronto è possibile. Il quinto anno è anche il primo in cui il confronto con i centri archiviati è quasi impossibile — Chicago, Los Alamos, Princeton e gli altri non ci sono, perché i due file delle città hanno 398 punti e sono quasi tutti capitali europee.

Il quinto anno ha però prodotto **due errori nella tabella degli attesi del verificatore**, non nei dati: Rotterdam è nel Brabante olandese del Sud e non nella provincia che il file chiama «Zelanda» (che è Frisia). È il secondo errore di questo genere dopo Castel del Monte, e la lezione è la stessa: **una tabella di attese scritta a mano è essa stessa un dato da verificare**, e il verificatore che segnala un'attesa sbagliata vale quanto quello che segnala un pin sbagliato.

### I due difetti trovati, e corretti

**Baghdad, 34 km fuori.** La coordinata era `lat 33.03333`, cioè **33°02′ N**, che è quanto riporta l'articolo in italiano di Wikipedia. Il centro che i file delle città archiviano è a 33,34° N: il pin era **34,4 km a sud**. La cifra della latitudine era sbagliata di un intero grado — `33.03` invece di `33.32`. Corretto su `en.wikipedia` (33.31528 N 44.36611 E), che è la fonte che il progetto usa quando quella italiana non torna. Il pin è ora a **3,7 km** dal centro archiviato, che per una metropoli di otto milioni di abitanti è il centro.

**Karakorum, nel Paese sbagliato.** Il nome aveva risolto sull'articolo «Karakorum», che è la **catena montuosa** fra Pakistan e Cina: la quota lo aveva già dichiarato sospetto (8 128 m, il K2) e il file lo marchiava `da_verificare`. Il controllo aggiunge la prova che mancava: la coordinata **cade dentro `CHN`** al punto-in-poligono. La capitale di Gengis Khan è in Mongolia, nella provincia dell'Övörkhangaj, a 47.1757 N 102.3338 E. Corretto sull'articolo giusto, «Karakorum (città)», e ora la verifica dice `MNG`.

### Un terzo difetto che era nella tabella, non nei dati

La prima stesura della tabella degli attesi scriveva, per **Castel del Monte**, la provincia dell'Aquila. Il controllo 3 ha detto che il pin cade in **Barletta-Andria-Trani**, che è Puglia, e la Puglia ha ragione: il castello federiciano è ad Andria, e l'omonima frazione abruzzese è un paese senza castello. **L'errore era nella mia attesa, non nel pin.** È il tipo di errore che vale la pena dichiarare, perché è la terza volta che questo progetto risolve un titolo invece di un luogo (Karakorum due volte, Castel del Monte una volta).

### Costantinopoli: un caso che non è un difetto

Il pin di Costantinopoli (41.01224, 28.97602) **non cade in nessun Paese**, a nessuna delle tre scale: è il Corno d'Oro, e il Bosforo è largo poco più di un chilometro. La terra più vicina è a 1,4 km, quindi il controllo 1 lo dichiara «sulla costa semplificata» e il controllo 2 lo esclude dal confronto sul Paese senza chiamarlo errore. **Se il pin fosse davvero in mare, il controllo 1 lo direbbe**: la soglia dei 3 km è dichiarata, e oltre i 12 km la misura non viene più fatta perché non ha senso.

### Che cosa questo controllo non copre

- ~~**19 pin** non sono verificabili sull'unità amministrativa.~~ **Chiuso il 03/10/2026.** Era un difetto di copertura, non dei pin: Agra, Buenos Aires, Bajkonur, Cambridge, Chicago, New York, Princeton, Seattle e gli altri sono fuori dall'Europa, dove il file amministrativo europeo non arriva; Costantinopoli, Uruk e Westminster sono in Paesi che il file europeo contiene solo in parte. Il file amministrativo **mondiale** di §2.4 li copre tutti: **54 pin su 54**.
- **Solo 19 pin su 54** hanno un confronto con il centro archiviato: i file delle città hanno 212 e 186 punti, che sono capitali e non un gazetteer. Per gli altri 35 la verifica è fatta sui poligoni, che è più debole ma non assente.
- ~~L'**anno 1 non è coperto**.~~ **Chiuso il 03/10/2026**: non dai controlli di qui, che per Ferrara sarebbero falsi, ma da cinque controlli suoi, **A1-A5** in `sorgenti/gis/verifica_anno1.py`, che sono in **§8ter**.
- Il punto-in-poligono lavora su geometrie semplificate: **non prova che il pin sia sulla strada o dentro il muro**, prova che è nella giusta unità amministrativa.

### Come si esegue

```bash
python3 sorgenti/gis/verifica_pin.py            # anni 2, 3 e 4 (la B5)
python3 sorgenti/gis/verifica_pin.py --anno 5   # il quinto anno
python3 sorgenti/gis/verifica_pin.py --tutti     # tutti e cinque: 120 slot, 72 con coordinate

python3 sorgenti/gis/verifica_anno1.py           # il primo anno: 30 tappe dentro le mura (A1-A5)
```

Il file ha anche `rilievo_senza_pil.py`, che misura quota e pendenza sui tasselli Terrarium **senza Pillow** (il PNG si decodifica con `zlib`, quarantacinque righe): serve perché `rilievo.py` va pure lui su questa macchina e senza `PIL` si ferma al primo tassello. I due file danno **numeri identici** su sette città già archiviate, e serve a rimisurare un punto senza reinstallare nulla.

---

## 8ter. Il primo anno: i trenta pin dentro le mura, che è l'unico modo giusto di verificarli

*(03/10/2026 — `sorgenti/gis/verifica_anno1.py`, cinque controlli **A1-A5**, 5 su 5 superati)*

**La domanda di Pietro**: «l'anno 1 non è coperto dai controlli automatici dei pin, perché i suoi confini vengono dal WFS del Comune e non dalle mappe Natural Earth: è un male?».

**La risposta breve è no, e la ragione è che i controlli di §8bis per il primo anno sarebbero stati sbagliati.** Quegli otto controlli rispondono a una domanda che ha senso per tutti gli altri anni — *«il pin cade nel Paese e nell'unità amministrativa che il nome dichiara?»* — e per Piazza Ariostea la risposta è sempre Italia, come per le altre ventinove tappe: il controllo passerebbe e non avrebbe detto niente. Il primo anno è l'unico in cui il gioco si gioca **dentro una città**, e lì la domanda che conta è un'altra:

> **il pin è dentro o fuori dal muro?** Fuori dalla linea comincia la nebbia (`tappa-1-01.md` §3). Un pin fuori dalle mure non è un pin poco accurato: è un pin che porta il giocatore dove non può andare.

**La fonte giusta è quella che il fondo stesso usa.** Il perimetro viene da `dati/ferrara_fondo.json`, **14 tratti OSM `barrier=city_wall`**, con l'anello ricostruito alla tolleranza dichiarata di 60 m: 8601 m di muro, **4,20 km²** giocabili (il dato storico è 4,8). Non è Natural Earth perché Natural Earth **non ha il muro di Ferrara**: ha il confine Italia-Croazia. Usare lì la scala sbagliata non avrebbe dato un difetto, avrebbe dato una risposta vera e inutile — che è la peggior specie di verifica.

### I cinque controlli e il loro esito

| # | Controllo | Soglia | Esito |
|---|---|---|---|
| **A1** | ogni tappa ha un punto, o dichiara di non averlo | — | **30 su 30** con punto (di cui 1-27 e 1-30 presi dall'ipotesi di grado `argomentata`, 150 m) |
| **A2** | ogni punto cade dentro le mura | margine 60 m dichiarato | **29 dentro, 1 sul margine, 0 fuori** |
| **A3** | nessuna tappa a meno di 30 m dalla linea: il muro non si attraversa in un passo | 30 m | **0** |
| **A4** | il percorso fra due tappe consecutive non esce dalle mura | 40 passi per tratto | **0 tratti fuori su 29** |
| **A5** | nessuna coordinata duplicata fra le trenta | — | **0** |

**Il percorso in linea d'aria è di 9967 m**, che è la cifra che il motore userà, e l'area giocabile è quella di cui sopra.

**A4 è il controllo che vale, ed è quello che nessuno degli anni dal secondo in poi può avere.** Fra due tappe successive si può passare fuori dalle mura e rientrare, e il punto-in-poligono sulle singole tappe non se ne accorgerebbe: è il difetto che si può avere solo in una città, ed è la ragione per cui il primo anno ha avuto bisogno di un verificatore suo invece di uno in più.

**A5 ha già corretto due tappe.** Le 1-27 (il monumento a Teodoro Bonati, nel chiostro della Certosa) e la 1-30 (la chiesa di San Cristoforo) non hanno un numero civico, e il fondo le dichiarava fuori dal controllo con una onestà che ora è superata: l'ipotesi di `dati/ipotesi_luoghi.json` dà a entrambe un punto, dichiarato `argomentata` con 150 m di raggio, e **A5 ha trovato che avevano lo stesso punto dell'ingresso della 1-29**. La risposta non è stata zittire il controllo, ma spostare i due edifici di 110 e 130 metri e dichiarare il raggio (`luoghi.md` §4.8).

**I cinque controlli sono stati provati iniettando difetti** in `anno1-mappa.md` — punto spostato fuori dalle mura, tappa sdraiata sul muro, percorso che esce, coordinata duplicata, punto mancante — e ognuno ha morso. Un controllo che non si è mai visto fallire non è un controllo.

```bash
python3 sorgenti/gis/verifica_anno1.py
```

**Che cosa resta fuori, e lo dichiaro**: il punto-in-poligono lavora su un anello ricostruito a 60 m di tolleranza, quindi «dentro le mura» significa «dentro le mura più sessanta metri», e i tratti di OSM sono ciò che un mapper ha tracciato, non un rilievo. La verifica prova che il gioco non manda il giocatore fuori dalla città; non prova che ogni metro di muro sia storicamente esatto.

---

## 9. Come si usa tutto questo in pratica

```bash
# rigenerare le mappe da capo (serve pyshp: pip install pyshp)
python3 sorgenti/gis/scarica_ne.py        # scarica i 42 shapefile
python3 sorgenti/gis/mappe_formato.py     # produce i 19 file in dati/mappe/
python3 sorgenti/gis/verifica_mappe_numeriche.py   # 61 controlli sulle mappe
python3 sorgenti/gis/verifica_pin.py               # 8 controlli sui pin degli anni 2, 3 e 4
python3 sorgenti/gis/verifica_pin.py --tutti       # gli stessi 8 controlli, tutti e cinque gli anni
python3 sorgenti/gis/mondo_admin1.py              # il file amministrativo del mondo
python3 sorgenti/gis/edifici_footprint.py         # le sagome degli edifici (Overpass)
python3 sorgenti/gis/ferrara_fondo.py             # il fondo cittadino dell'anno 1
python3 sorgenti/verifica_ambienti.py               # i 150 ambienti, otto controlli (B1-B8)
python3 sorgenti/gis/altitudine.py                    # le tre scale delle cime
python3 sorgenti/gis/verifica_altitudine.py           # le cime, sette controlli
python3 sorgenti/gis/verifica_mappe_disegno.py        # dodici pagine di verifica
python3 sorgenti/verifica_colori.py                   # i colori delle carte, C1-C7
```

Il lettore si usa così:

```python
import sys; sys.path.insert(0, "sorgenti/gis")
from mappe_lettore import leggi

geometrie, punti = leggi("dati/mappe/penisola_10_regioni.json")
for proprieta, anelli in geometrie:
    if proprieta.get("name_it") == "Ferrara":
        print(proprieta, len(anelli))
```

*(nota — quando `leggi()` sbaglia, adesso lo dice)* Il lettore controlla la forma del file prima di decodificarlo e solleva un `ValueError` che nomina il percorso e il formato atteso. Senza quel controllo un file sbagliato dentro `dati/mappe/` faceva crashare il lettore con un `IndexError` che non riportava nessuna pista (§3).

*(nota — il percorso degli script)* Gli script stanno in `sorgenti/gis/` come gli altri del progetto, e i dati in `dati/mappe/`, dove `README.md` li deve elencare. I file `.py` hanno il nome senza prefisso `videogioco-5-duchi-`, perché sono sorgenti e non dati: la convenzione dei documenti vale per `docs/`.

---

## 10. Questioni aperte

1. ~~**ODbL entra nel progetto?**~~ **Risolto il 02/10/2026: sì, entra.** L'obiezione che lo rende una scelta pesante — «ti obbliga a mettere tutto sotto licenza libera» — non è corretta: l'obbligo di condivisione scatta solo per un **database derivato**, e un gioco che disegna geometrie su schermo distribuisce un'opera, non un database. Il codice, i documenti e la grafica restano del progetto; i file di dati derivati da OSM viaggiano con ODbL e la dichiarazione «© OpenStreetMap contributors». Sblocca i sagomi degli edifici fuori Ferrara e quindi le trenta zone percorribili. Ragionamento e vincoli in `luoghi-edifici.md` §1.
2. **Il vincolo di 20 000 abitanti per mostrare una città** (§4.2) è giusto? È una proposta, non una decisione, e cambia molto la quantità di nomi sulla mappa.
3. **Le trenta zone percorribili** si fanno tutte, o solo dove il luogo è davvero lo spazio del gioco (§5.2)? La seconda ipotesi fa risparmiare mesi e il progetto funziona già così nell'anno 1.
4. **Il file `europa_50_regioni_amministrative` è grosso** (450 kB, 1 687 geometrie). Va tenuto intero, o ridotto alle unità di primo livello, visto che molte tappe dell'anno 3 sono in capitali di Stato e non serve il dettaglio dei distretti?
5. ~~**I pin degli anni 2, 3 e 4**~~ **Risolto il 02/10/2026: verificati tutti.** Sono 90 slot di pin, di cui 53 con coordinate, e i 53 sono passati per otto controlli (`verifica_pin.py`, §8bis). Ne sono usciti **due difetti reali** — Baghdad 34 km fuori, Karakorum in Cina invece che in Mongolia — entrambi corretti e annotati nel file di luoghi, e un caso che non è un difetto (Costantinopoli, nel Corno d'Oro, a 1,4 km dalla terra). ~~La domanda che restava~~ **Risolta il 03/10/2026: il file amministrativo mondiale esiste** (`dati/mappe/mondo_admin1.json`, §2.4), e **i 54 pin che hanno coordinate sono tutti coperti**. Non tutti i 120 slot, che è un'altra cosa: 54 pin distinti su 95 luoghi, e 41 luoghi non hanno coordinate perché non sono luoghi.

---

## 11. Cosa c'è da fare

1. ~~**Decidere ODbL**~~ **fatto il 02/10/2026**: entra, e i sagomi si prendono da OSM dichiarandone la provenienza edificio per edificio (`luoghi-edifici.md` §1)
2. ~~**Verificare i 90 pin**~~ **fatto il 02/10/2026**: 8 controlli in `sorgenti/gis/verifica_pin.py`, 53 pin con coordinate verificati, 2 difetti corretti (§8bis). Il quinto anno è passato dagli stessi controlli lo stesso giorno, senza difetti. La parte che il file amministrativo non copriva è chiusa dal 03/10/2026
3. ~~**Convertire l'altitudine**~~ **fatto il 03/10/2026**: `dati/mappe/mondo_110_altitudine.json`, `europa_50_altitudine.json` e `penisola_10_altitudine.json`, 15 + 2 + 26 punti, con il conto della fonte in `dati/altitudine_manifest.json` e le due scoperte dichiarate: la fonte è **mondiale in tutte e tre le scale** e **i tre file non sono annidati** (§2.5). È servita la funzione `punti()` in `sorgenti/gis/shapefile_lettore.py`, che legge `Point` e `MultiPoint`
4. ~~**Costruire `dati/mappe/anno1_pin.json`**: i pin dell'anno 1 verificati con lo stesso metodo, così il metodo è provato su dati già noti~~ **Risolto il 03/10/2026, ma non con il metodo di qui, e la ragione è la risposta alla domanda di Pietro**: per una città dentro le mure il «metodo di qui» sarebbe stato sbagliato. I controlli giusti per il primo anno sono **A1-A5** in `sorgenti/gis/verifica_anno1.py`, che confrontano le trenta tappe con il perimetro delle mura e non con Natural Earth (§8ter). Il file `anno1_pin.json` **non serve**: i trenta punti vivono già in `docs/videogioco-5-duchi-anno1-mappa.md` e i due che non avevano un punto lo hanno ora grazie alle ipotesi di `dati/ipotesi_luoghi.json` (`luoghi.md` §4.8)
5. ~~**Decidere il formato degli edifici**~~ **fatto il 03/10/2026**: `dati/edifici_footprint.json` con i campi `forma`, `altezza_m` e `fonte_altezza` (`osm_height`/`osm_levels`/`assente`), che è la regola di §5.1 scritta nei dati e non solo nel documento
6. ~~**Costruire il file amministrativo mondiale**~~ **fatto il 03/10/2026**: `dati/mappe/mondo_admin1.json`, 50 unità, 54 pin coperti su 54, con il conto della copertura in `dati/mondo_admin1_copertura.json` — che sta in `dati/` e non in `dati/mappe/`, e il perché è scritto (§2.4 e §3)
7. ~~**Costruire il fondo cittadino dell'anno 1**~~ **fatto il 03/10/2026**: `dati/ferrara_fondo.json`, 14 tratti di mura OSM, 4,20 km² (§3.5 di `fonti-visive.md`)
8. ~~**Costruire gli ambienti dei 150 livelli**~~ **fatto il 03/10/2026**: `dati/ambienti_livelli.json`, **150 su 150** (§3.6 di `fonti-visive.md`, `sorgenti/ambienti_livelli.py` e `sorgenti/verifica_ambienti.py` con otto controlli A1-A8/B1-B8). Restava scritto aperto mentre il file era gia' pronto da due giorni: una riga di «cosa c'e' da fare» che non corrisponde a nessun lavoro mancante e' una riga che mente, e questa ne aveva scoperto un'altra

---

## 12. Registro modifiche

- **v1.1 (03/10/2026)**: **l'ultimo punto di «cosa c'è da fare» era chiuso da due giorni e lo dichiarava aperto.** Il punto 8 chiedeva gli ambienti dei centocinquanta livelli: il file c'era, completo al 150 su 150, con il suo generatore e i suoi otto controlli. Quello che mancava era la scrittura, e una riga di «cosa c'è da fare» che non corrisponde a nessun lavoro mancante è una riga che mente — perché costringe a rileggerla ogni volta, e a chiedersi se il lavoro sia ancora da fare. Chiudendola sono tornato alla sezione che l'aveva prodotto e **i suoi numeri non erano più quelli del file**: sette cifre sbagliate in `fonti-visive.md` §3.6. La chiusura di un punto scoperto un difetto in un altro documento, ed è la seconda volta che accade (§11 punto 4 aveva fatto trovare il conto dei pin). Il punto 8 è chiuso e la catena degli ambienti è `ambienti_livelli.py` → `verifica_ambienti.py` (B1–B8), tutti superati.

- **v0.9 (03/10/2026)**: **il primo anno non è più scoperto, e la ragione per cui era scoperto era la giusta: i suoi confini non vengono da Natural Earth.** La domanda di Pietro — «è un male?» — ha una risposta che è «no»: per una città dentro le mure, gli otto controlli di §8bis sarebbero stati *falsi*. «Il pin cade nel Paese che il nome dichiara» per Piazza Ariostea è sempre Italia, come per le altre ventinove tappe: il controllo sarebbe passato senza aver detto niente. La domanda che conta per l'anno 1 è **«è dentro o fuori dal muro?»**, perché fuori comincia la nebbia: un pin fuori dalle mura non è un pin poco accurato, è un pin che porta il giocatore dove non può andare.
  - **`sorgenti/gis/verifica_anno1.py`, cinque controlli A1-A5, 5 su 5 superati**: 30 tappe su 30 con un punto, **29 dentro le mura e 1 sul margine e 0 fuori**, 0 tappe entro 30 m dalla linea, **0 tratti fuori sui 29** e 0 coordinate duplicate. La fonte è `dati/ferrara_fondo.json` (14 tratti OSM `barrier=city_wall`), non il confine Italia-Croazia di Natural Earth: usare lì la scala sbagliata non avrebbe dato un difetto, avrebbe dato una risposta vera e inutile;
  - **A4 è il controllo che vale**, ed è l'unico che nessun altro anno può avere: fra due tappe successive si può passare fuori dalle mura e rientrare, e il punto-in-poligono sulle singole tappe non se ne accorgerebbe;
  - **A5 ha corretto due tappe**: 1-27 e 1-30 avevano il punto dell'ingresso della 1-29, e la risposta è stata spostarle di 110 e 130 metri con raggio dichiarato, non zittire il controllo. È la conseguenza diretta delle ipotesi di coordinata (`luoghi.md` §4.8): due tappe che non si potevano controllare ora si controllano;
  - **il §11 punto 4 è chiuso e non si farà**: `dati/mappe/anno1_pin.json` non serve, perché i trenta punti vivono già in `anno1-mappa.md` e i due che mancavano hanno ora un punto ipotizzato e dichiarato. Il §11 punto 8 era un elenco di ambienti e non un pacchetto di mappe: era **chiuso** e lo dichiarava aperto, ed è stato chiuso davvero (§11 punto 8).

- **v0.8 (03/10/2026)**: **le cime sono state convertite, e convertendole è saltato fuori un difetto che non era di geometria.** `dati/mappe/mondo_110_altitudine.json`, `europa_50_altitudine.json` e `penisola_10_altitudine.json` portano **15, 2 e 26 punti** di `geography_regions_elevation_points`, con il conto della fonte in `dati/altitudine_manifest.json` (19→15, 86→2, 711→26). Le due scoperte che i numeri non nascondono: la fonte è **mondiale in tutte e tre le scale** — il file chiamato «europa» elenca 86 cime da longitudine −167 a +160 e solo due in Europa — e **i tre file non sono annidati**, nessuna delle 15 cime mondiali cadendo nel riquadro della penisola: sono selezioni diverse della stessa fonte globale, e un motore che li trattasse come risoluzioni diverse dello stesso elenco sbaglierebbe invisibilmente. Dichiarato anche che il file **non è un modello del terreno** e che l'Everest è a 8848 m, il valore del 1954, che il gioco non corregge. Per leggerli è servita la funzione `punti()` in `sorgenti/gis/shapefile_lettore.py`, che copre `Point` e `MultiPoint`: la trappola del `MultiPoint` è che porta dentro i punti una struttura che somiglia a quella di un poligono, e leggerlo con il codice dei poligoni dà coordinate che sembrano giuste.

  **Il difetto vero è un altro, ed è il primo dei due chiusi in questo documento.** `dati/mappe/mondo_admin1_copertura.json` stava **dentro `dati/mappe/`**, dove vale la regola del solo formato a delta, e faceva crashare `mappe_lettore.leggi()` con un `IndexError: list index out of range`: un sintomo che dice una lista troppo corta e non dice che il problema è un file che non aveva niente a che fare li. Il file è stato spostato in `dati/`, il generatore corretto, **il lettore ora controlla la forma del file** e solleva un `ValueError` che nomina il percorso, e il controllo **C6** tiene l'invariante fermo. Il pacchetto passa da 21 a **23 file** e i controlli numerici da 57 a **61 su 61**. I **colori delle carte**, che erano scritti nel codice del disegnatore, sono ora in `dati/fonti_visive/colori_cartografici.json` (19 voci, `fonti-visive.md` §3.7) e `sorgenti/gis/verifica_mappe_disegno.py` li **legge** invece di scriverli: il suo difetto di prima era `fill="F6FAFC"` senza il cancelletto, cioè dodici pagine di verifica senza un colore. Due verificatori nuovi: `verifica_colori.py` (C1–C7, 18 file in tabella di copertura) e `verifica_altitudine.py` (D1–D7), entrambi a zero, entrambi provati anche sufficiendo difetti.

- **v1.0 (03/10/2026)**: **i pin sono 72 e non 71, ed è il rigeneramento del registro a dirlo.** La catena dei luoghi (`estrai_luoghi.py` → `coordinate.py` → `classifica.py` → `aggiorna_registro.py`) è stata eseguita end to end per la prima volta, e due luoghi hanno cambiato stato: **Pataliputra** ha ottenuto una coordinata verificata (25.6125 N 85.12833 E, l'odierna Patna) quando il geocodificatore l'ha cercata, e **Manchester** è uscita dal registro perché la tappa 3-28 ora dice Torino. Il quarto anno passa da 13 a **14** slot con coordinate, il totale da 71 a **72**, e i due Paesi attesi che mancavano — IND per Pataliputra, ITA per Torino — sono dichiarati in `ATTESI_GIA`, perché il controllo 7 ha ragione: un pin verificato senza Paese atteso è un pin che nessuno può confrontare con nessun altro. Otto controlli, 8/8. Il dettaglio della catena è in `sequenza.md` §1 e le regole in `AGENTS.md`.

- **v0.7 (03/10/2026)**: **la copertura amministrativa è chiusa, e con lei i tre file che chiudevano i buchi di grafica.** Il file amministrativo mondiale (`dati/mappe/mondo_admin1.json`, 50 unità di primo livello da Natural Earth 10m, pubblico dominio) copre **54 pin su 54**: è la risposta alla domanda che §8bis lasciava aperta sui diciannove pin non verificabili, che era un difetto di copertura e non dei pin. La selezione non è per nome ma punto-in-poligono sul pin, e la semplificazione scende da sola finché l'anello contiene ancora il proprio pin: **sette unità su 50** hanno avuto bisogno di una tolleranza più fine, ed è dichiarato quali. Nello stesso giorno sono entrati `dati/edifici_footprint.json` (5209 sagome su 54 luoghi) e `dati/ferrara_fondo.json` (14 tratti di mura, 4,20 km², 28 tappe su 28 dentro), e i tre file hanno il loro capitolo in `fonti-visive.md` (v0.2, §3.2, §3.5 e §3.6). §7, §9, §10 e §11 sono aggiornati di conseguenza: le sagome non sono più «da costruire» e il fondo cittadino dell'anno 1 non è più un buco.

- **v0.1 (01/10/2026)**: prima stesione. Fondo geografico per gli anni 2, 3 e 4:
  - **19 file di mappe** in `dati/mappe/`, estratti da Natural Earth (pubblico dominio) in tre scale: 110m per il mondo, 50m per l'Europa, 10m per la penisola, per 1,4 MB complessivi;
  - il **formato a delta** con il suo lettore, che riprende la convenzione già stabilita da `gis/citta_centro.json`;
  - il **punto-in-poligono** col winding number, che distingue i buchi dalle isole e senza il quale nessun controllo è affidabile;
  - i **cinque difetti reali** trovati dalla verifica, con il metodo per ognuno: la Sardegna ridotta a un segno, Venezia dentro la Baviera, gli anelli interni spostati, le città scartate, e la costa spostata di 1,3 km;
  - **57 controlli automatici, tutti superati**;
  - la risposta alla domanda sulle «chicche»: le sagome si prendono da OpenStreetMap, **le altezze non esistono come dato** (24% a Milano, 3% a Roma), e la regola dei tre livelli con la dichiarazione della provenienza di ogni altezza;
  - la proposta del **vincolo dei 20 000 abitanti** per decidere che cosa si può attraversare senza fermarsi;
  - **cinque questioni aperte**, la prima delle quali è la licenza ODbL, che è una decisione di Pietro e non può essere presa da una fonte.

- **v0.4 (02/10/2026)**: rimandi di versione aggiornati agli anni 3, 4 e 5 e a `luoghi.md`, che sono saliti a v0.4, v0.5, v0.4 e v0.3 con le decisioni del 02/10/2026.
- **v0.6 (02/10/2026)**: **la verifica dei pin copre adesso tutti e cinque gli anni.** `verifica_pin.py` prende `--anno N` e `--tutti`, e il quinto anno è passato dagli stessi otto controlli lo stesso giorno: **30 slot, 15 posti con coordinate, nessun difetto**. Il quinto anno ha pero' prodotto **due errori nella tabella degli attesi** (Rotterdam non è nella provincia che il file chiama «Zelanda»), cioè il secondo caso in cui l'errore era nella mia attesa e non nei dati: la tabella degli attesi è essa stessa un dato da verificare. §8bis ora porta la tabella completa (120 slot, 71 con coordinate) e dichiara anche che **l'anno 1 non è coperto**, perché i suoi pin prendono il confine dal WFS del Comune e non dalle mappe.

- **v0.5 (02/10/2026)**: **la verifica dei pin degli anni 2, 3 e 4 è fatta**, ed è la sezione **§8bis**, nuova. Otto controlli in `sorgenti/gis/verifica_pin.py`, tutti superati, su **53 slot di pin con coordinate** dei 90 slot totali. Il numero 90 dell'audit è esatto ma è il numero degli **slot** (uno per tappa), non dei pin distinti: i posti sono 69 e i pin con coordinate sono 39. Risultato: **due difetti reali corretti** (Baghdad, 34 km a sud del centro per una cifra di latitudine sbagliata; Karakorum, che cadeva in Cina invece che in Mongolia, risolto sull'articolo giusto), **un errore nella tabella degli attesi** (Castel del Monte non è in Abruzzo) e **un caso che non è un difetto** (Costantinopoli cade nel Corno d'Oro, a 1,4 km dalla terra). Aggiunto `sorgenti/gis/rilievo_senza_pil.py`, che rimisura quota e pendenza senza Pillow e dà gli stessi numeri di `rilievo.py` su sette città archiviate. Corretti in `dati/luoghi_gioco.json` i record di Baghdad e Karakorum (coordinate, articolo, fonte, terreno rimisurato).

- **v0.3 (02/10/2026)**: controllo di coerenza. Il rimando a `anno5-mondo.md` era fermo alla v0.1 (è alla v0.2) e quello a `luoghi.md` alla v0.1 (è alla v0.2). I due file citati che il documento non promette esistere — `dati/mappe/anno1_pin.json` e `dati/mappe/edifici.json` — restano quelli che sono, cioè roba **da costruire**: il controllo automatico li legge ora come «dichiarati come futuri» e non come smarriti.

- **v0.2 (02/10/2026)**: la Q1 è risolta e il §5 è sbloccato.
  - **ODbL entra nel progetto.** La ragione per cui sembrava una scelta pesante — l'obbligo di mettere tutto sotto licenza libera — non si applica: scatta solo per un **database derivato**, e un gioco che disegna geometrie su schermo distribuisce un'opera. Codice, documenti e grafica restano del progetto; i file di dati derivati viaggiano con ODbL e l'attribuzione «© OpenStreetMap contributors». Vedi `luoghi-edifici.md` §1.
  - Aggiunto il rimando a `videogioco-5-duchi-luoghi-edifici.md`, che tiene lo **schema del dettaglio per luogo** (impianto, materiali, edifici, cronologia, terreno, vuoto), i **95 luoghi** del gioco classificati in sette tipi, e il **rilievo del terreno** come risposta alle altezze mancanti.
