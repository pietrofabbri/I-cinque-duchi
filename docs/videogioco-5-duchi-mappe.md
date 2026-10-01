---
titolo: Videogioco "I cinque duchi" — Le mappe: fondo geografico per gli anni 2, 3 e 4, e dove si prendono i dettagli delle tappe
versione: 0.1
data: 2026-10-01
autore: Pietro Fabbri (con Claude)
fonte del materiale: richiesta di Pietro dell'01/10/2026 («recupera e archivia tutte le mappe che possono essere utili a questo e i prossimi anni»), con l'indicazione di due usi distinti: le mappe generali per costruire un percorso sensato, e le mappe di dettaglio per rappresentare ogni livello nella forma più reale possibile
dati: dati/mappe/*.json (19 file, prodotti il 01/10/2026 da Natural Earth con `sorgenti/gis/mappe_formato.py`)
documenti collegati: videogioco-5-duchi-motore-e-grafica.md (v0.1, la pipeline che questi dati alimentano), videogioco-5-duchi-luoghi.md (v0.1, la regola che decide *quali* luoghi servono), videogioco-5-duchi-anno2-penisola.md (v0.1), videogioco-5-duchi-anno3-europa.md (v0.2), videogioco-5-duchi-anno4-mondo.md (v0.3), videogioco-5-duchi-anno5-mondo.md (v0.1), FONTI-E-LICENZE.md, AGENTS.md
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
| **Prodotti** | 19 file di mappe in formato proprio, in `dati/mappe/`, per un totale di **1,4 MB** |
| **Verifiche** | **57 controlli automatici, tutti superati** (`sorgenti/gis/verifica_mappe_numeriche.py`) |
| **Licenza** | Natural Earth è **pubblico dominio**: nessun vincolo, nessuna attribuzione richiesta |
| **Non è stato possibile** | il fondo delle tappe di dettaglio: vedi §5, e la ragione è tecnica, non di volontà |

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
| Sagome degli edifici ovunque | OSM Overpass | **da costruire**, interfaccia verificata | **ODbL: va deciso** |
| Altezze degli edifici fuori Ferrara | nessuna fonte unica | **irrisolto**: 24% a Milano, 3% a Roma | — |
| Altezza sul mare, rilievo | Natural Earth `elevation_points` | scaricato, non ancora convertito | pubblico dominio |
| Linee elettriche, ferrovie | OSM Overpass | da costruire | ODbL |
| Idrografia minore per l'anno 2 | OSM o idrografia regionale | da valutare | — |

*(aggiunta — la decisione che va presa presto)* **ODbL è una scelta di Pietro, non mia.** Prima di scaricare dati da OpenStreetMap va deciso se il progetto accetta l'obbligo di attribuzione e la condivisione della stessa licenza per i database derivati. La raccomandazione è di **usare Natural Earth per tutto ciò che è possibile** e riservare OSM ai soli edifici, dichiarandone la provenienza edificio per edificio.

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
| nessun vertice fuori dal mondo, in tutti i 19 file | **conforme** |
| **totale** | **57 su 57** |

*(da fare)* Non è ancora verificato che **ogni pin delle 90 tappe degli anni 2, 3 e 4** cada nel Paese e nella regione che il documento dichiara. È il controllo più importante che resta, ed è possibile adesso che prima non lo era.

---

## 9. Come si usa tutto questo in pratica

```bash
# rigenerare le mappe da capo (serve pyshp: pip install pyshp)
python3 sorgenti/gis/scarica_ne.py        # scarica i 42 shapefile
python3 sorgenti/gis/mappe_formato.py     # produce i 19 file in dati/mappe/
python3 sorgenti/gis/verifica_mappe_numeriche.py   # 57 controlli
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

*(nota — il percorso degli script)* Gli script stanno in `sorgenti/gis/` come gli altri del progetto, e i dati in `dati/mappe/`, dove `README.md` li deve elencare. I file `.py` hanno il nome senza prefisso `videogioco-5-duchi-`, perché sono sorgenti e non dati: la convenzione dei documenti vale per `docs/`.

---

## 10. Questioni aperte

1. **ODbL entra nel progeto?** È la decisione che sblocca i sagomi degli edifici fuori Ferrara, e quindi le trenta zone percorribili. Senza, gli edifici vengono dal WFS comunale, che esiste solo dove esiste (§5).
2. **Il vincolo di 20 000 abitanti per mostrare una città** (§4.2) è giusto? È una proposta, non una decisione, e cambia molto la quantità di nomi sulla mappa.
3. **Le trenta zone percorribili** si fanno tutte, o solo dove il luogo è davvero lo spazio del gioco (§5.2)? La seconda ipotesi fa risparmiare mesi e il progetto funziona già così nell'anno 1.
4. **Il file `europa_50_regioni_amministrative` è grosso** (450 kB, 1 687 geometrie). Va tenuto intero, o ridotto alle unità di primo livello, visto che molte tappe dell'anno 3 sono in capitali di Stato e non serve il dettaglio dei distretti?
5. **I pin degli anni 2, 3 e 4** vanno verificati tutti? Sono 90 coordinate scritte a mano, e questa è la prima volta che si può farlo.

---

## 11. Cosa c'è da fare

1. **Decidere ODbL** (§10 Q1): blocca tutto il §5
2. **Verificare i 90 pin** degli anni 2, 3 e 4 contro i file archiviati: è il controllo che manca e che vale più di qualunque altro
3. **Convertire l'altitudine** (`geography_regions_elevation_points`): serve al quinto anno, dove la colonna degli strati è il tempo e la montagna è un dato
4. **Costruire `dati/mappe/anno1_pin.json`**: i pin dell'anno 1 verificati con lo stesso metodo, così il metodo è provato su dati già noti
5. **Decidere il formato degli edifici**: se si sceglie OSM, definire `dati/mappe/edifici.json` con i campi `forma`, `altezza`, `fonte_altezza` (`lidar`/`osm`/`stimata`), `livelli` — la regola di §5.1 scritta nei dati, non solo nel documento

---

## 12. Registro modifiche

- **v0.1 (01/10/2026)**: prima stesione. Fondo geografico per gli anni 2, 3 e 4:
  - **19 file di mappe** in `dati/mappe/`, estratti da Natural Earth (pubblico dominio) in tre scale: 110m per il mondo, 50m per l'Europa, 10m per la penisola, per 1,4 MB complessivi;
  - il **formato a delta** con il suo lettore, che riprende la convenzione già stabilita da `gis/citta_centro.json`;
  - il **punto-in-poligono** col winding number, che distingue i buchi dalle isole e senza il quale nessun controllo è affidabile;
  - i **cinque difetti reali** trovati dalla verifica, con il metodo per ognuno: la Sardegna ridotta a un segno, Venezia dentro la Baviera, gli anelli interni spostati, le città scartate, e la costa spostata di 1,3 km;
  - **57 controlli automatici, tutti superati**;
  - la risposta alla domanda sulle «chicche»: le sagome si prendono da OpenStreetMap, **le altezze non esistono come dato** (24% a Milano, 3% a Roma), e la regola dei tre livelli con la dichiarazione della provenienza di ogni altezza;
  - la proposta del **vincolo dei 20 000 abitanti** per decidere che cosa si può attraversare senza fermarsi;
  - **cinque questioni aperte**, la prima delle quali è la licenza ODbL, che è una decisione di Pietro e non può essere presa da una fonte.