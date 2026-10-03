---
titolo: Videogioco "I cinque duchi" — audit delle questioni aperte: la lista operativa
versione: 0.9
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte: lettura di tutti i quindici documenti di progetto, verificata da sorgenti/lingue/conta_questioni.py
documenti collegati: videogioco-5-duchi-lingue.md (v0.1), videogioco-5-duchi-lingue-immagini.md (v0.1), videogioco-5-duchi-percorsi.md (v0.4), videogioco-5-duchi-fonti-visive.md (v0.3), videogioco-5-duchi-furioso.md (v0.6), videogioco-5-duchi-luoghi.md (v0.5), videogioco-5-duchi-mappe.md (v1.0), videogioco-5-duchi-anno5-mondo.md (v0.5), videogioco-5-duchi-percorsi.md (v0.4), videogioco-5-duchi-anno4-mondo.md (v0.5), videogioco-5-duchi-anno3-europa.md (v0.4), videogioco-5-duchi-anno2-penisola.md (v0.2), videogioco-5-duchi-anno1-ferrara.md (v0.3), videogioco-5-duchi-curricolo.md (v0.1), videogioco-5-duchi-gioco.md (v0.5), videogioco-5-duchi-meccaniche.md (v0.3), AGENTS.md
---

# Audit delle questioni aperte: la lista

## 0. Che cosa c'è in questo documento

La **lista operativa** di tutte le questioni aperte del progetto: che cosa si deve decidere, che cosa si può fare, e **chi decide**.

Ogni voce ha quattro cose: la **domanda** in una riga, il **pro**, il **contro**, la **valutazione** (che è la mia, e come tale si può confutare), e la **responsabilità** (chi decide: Pietro, il progetto, una comunità, un'istituzione).

Il documento è verificato da `sorgenti/lingue/conta_questioni.py`, che confronta il proprio conto con i numeri scritti qui.

## 1. Il conto

| | |
|---|---|
| Documenti con una sezione «Questioni aperte» | **15** |
| Voci enumerate | **114** |
| **Chiuse** | **29** |
| **Aperte** | **85** |
| Di cui bloccanti | quattro |
| Di cui importanti (cambiano il gioco) | quindici |
| Di cui minori (si possono rimandare) | le altre |

**Il criterio**, dichiarato perché un numero senza criterio non è un dato. Una **voce** è un punto numerato, un `### Q1` o una riga di tabella della sezione «Questioni aperte». Una voce è **chiusa** se porta la marcatura nella sua **prima riga** — «chiusa», «risolto», «ratificata», «confermata» — e non in tutto il corpo, perché una voce aperta spiega dentro il corpo quale parte è stata chiusa.

**Una voce non è sempre una domanda.** In `lingue.md` Q3 ci sono due sotto-voci dentro una sola domanda. Le **114 voci non sono 114 domande**.

**Nessuna delle ventinove chiuse è bloccante**, e due delle quattro bloccanti rimaste non sono mai state domande: erano lavori, e sono stati fatti — i novanta pin il 02/10/2026 (§2bis), la tavolozza, le sagome, il fondo di Ferrara e i colori delle carte il 03/10/2026 (§3bis). Le decisioni prese hanno tolto lavoro, non lo hanno aggiunto.

---

## 2. Le quattro bloccanti

Sono le uniche che fermano qualcosa, e sono le quattro che aspettano una **risposta**. Ognuna ha una scheda. La quinta, **B5**, era un lavoro e non una domanda: è in §2bis.

---

### B1 · I livelli linguistici e quelli informatici sono lo stesso livello o due?

`lingue.md` §7 Q1 · **pro**: due sistemi paralleli nella stessa tappa dà 32 livelli per tappa ed è l'unica forma in cui i due percorsi si incontrano. **contro**: rende ogni tappa enorme, e le trenta tappe coprirebbero 150 informatici più 900 linguistici in un'ora di lezione; l'alternativa «lingue dentro l'informatica» cancella le 900 unità di gioco. **valutazione**: è la decisione con la conseguenza più grande e la meno reversibile; va presa con la stima delle schermate per tappa, che nessuno ha fatto. **responsabilità**: Pietro. **blocca**: i dati dei livelli, la scelta delle immagini, tutte le tappe linguistiche, i testi autentici, la progressione.

#### B1 in parole semplici

*(03/10/2026 — Pietro ha chiesto di capire la B1 «meglio, con parole più semplici». Questa è la spiegazione; quella sopra è la scheda operativa. Nessuna delle due chiude la domanda: la decisione è di Pietro.)*

**Il gioco insegna due cose: l'informatica e le lingue.** Dell'informatica hai deciso **150 livelli**: cinque anni, trenta tappe all'anno. Delle lingue ne hai immaginati **900**: sei lingue, trenta livelli per lingua, cinque anni.

Le due cose non possono stare nella stessa lista. La domanda è una sola, e si può fare in italiano di tutti i giorni:

> **Quando il ragazzo è dentro la tappa 5-12, quante cose deve fare?**

- **Oppure una.** Solo il livello di informatica. E i 900 livelli di lingue spariscono come unità di gioco: diventano contenuti che compaiono dentro alcuni livelli di informatica (l'inglese che serve a una tappa, il latino che serve a un'altra). Questo è «lingue dentro l'informatica».
- **Oppure tante in fila.** Nella stessa tappa c'è il livello di informatica **e** un livello per ciascuna delle sei lingue: **32 livelli in una tappa sola**. È l'unica forma in cui i due percorsi si incontrano davvero, ed è anche quella che rende ogni tappa enorme: trenta tappe da un'ora di lezione dovrebbero contenere 150 livelli informatici più 900 linguistici, cioè **cinquantacinque livelli all'ora**. Non ci stanno.
- **Oppure a tappe alterne.** Le trenta tappe di un anno sono metà linguistiche e metà informatiche. Allora le tappe raddoppiano (diventano 300 in tutto), oppure se ne copre solo una parte e il progetto si presenta come un gioco di 150 livelli che in realtà ne copre 75.

**Che cosa è già costruito e che cosa è bloccato.** Le 150 tappe informatiche esistono già quasi tutte: mappa, pin, ambienti, mezzi, luoghi. Quelle non aspettano la B1. I **900 livelli linguistici**, invece, non esistono come dati, e non possono esistere finché la domanda non è risolta: non si sa in che stanza stanno, e senza quello non si possono scrivere i testi né scegliere le immagini. **È questa la differenza fra «blocca tutto» e «blocca metà» che l'audit dichiarava e che questa scheda non ripete.**

**Perché non la decido io, e perché è la decisione giusta che ti spetta.** Le tre scelte danno giochi diversi, non giochi uguali con dettagli diversi, e la differenza la si vede dopo: nel motore, nel tempo di lezione, nel numero di schermate. La stima delle schermate per tappa — che è ciò che servirebbe per scegliere — dipende da un prototipo che non esiste ancora. Quindi la domanda giusta non è «quale delle tre è giusta», ma:

> **quando entri in una tappa, vedi un compito solo o un compito per ciascuna lingua?**

**Quello che si può fare intanto, e che è già stato fatto.** Nessuna delle trenta tappe di informatica aspetta questa risposta: i 150 ambienti, le coordinate, i mezzi e i luoghi sono costruiti senza di lei. È la stessa regola che vale per le altre tre bloccanti: **mentre si decide, si costruisce quello che si può costruire** (`percorsi.md` §1.2 dice perché i mezzi dell'anno 4 sono stati scelti senza aspettare nessuna decisione).

---

### B2 · Le trenta voci di ogni oggetto sono confermate?

`lingue.md` §7 Q2 e `lingue-immagini.md` §6.2 Q2 · **pro**: le voci esistono e sono lavorate; confermarle sblocca 1120 candidati già cercati. **contro**: per il ferrarese non sono un elenco ma **campi da rilevare**, e la fonte non è stabilita (chi raccoglie, con che metodo, con quale consenso); un proverbo scritto a tavolino è un proverbo italiano in maschera. **valutazione**: va chiusa **prima** di scegliere le immagini, altrimenti si rifà la ricerca; per le altre cinque lingue è una revisione di trenta voci, per il ferrarese è un progetto. **responsabilità**: Pietro, e per il ferrarese **anche chi raccoglierà i proverbi**. **blocca**: B4, e le tappe facoltative degli oggetti.

### B3 · La LIS nel gioco: chi insegna, e con quali materiali?

`lingue.md` §7 Q4 · **pro**: la lingua dei segni è la scelta che rende il progetto serio; le trenta voci ci sono. **contro**: non si scrive a tavolino; servono collaborazione con la comunità sorda, video, trascrizioni, competenze che il progetto non dichiara di avere. **valutazione**: la più lenta di tutte, perché un rapporto con la comunità non si scrive in un pomeriggio; è l'unica che non si può sblocare con una decisione. **responsabilità**: Pietro **e la comunità sorda** — non è una decisione che il progetto può prendere da solo, e questa è la ragione per cui la domanda è bloccante e non importante. **blocca**: i trenta livelli LIS.

### B4 · Chi guarda le 1120 immagini degli oggetti?

`lingue-immagini.md` §6.2 Q1 · **pro**: guardarle è lavoro di ore, non di minuti; i candidati sono già tutti e hanno licenza libera. **contro**: nessuna è stata guardata; 67 su 146 sono a rischio (G7). **valutazione**: l'opzione realistica è **un campione** — i 146 migliori per voce — dichiarando che un campione non attesta il resto; le tre opzioni sono guardarle tutte, guardarle un campione, o non guardarle. **responsabilità**: io (l'IA) o Pietro; la decisione di *quanto* guardare è di Pietro. **blocca**: le tappe facoltative degli oggetti, e nient'altro.

### B5 · I novanta pin degli anni 2, 3 e 4 sono verificati? — **chiusa il 02/10/2026**

Non è più una bloccante: la scheda è in **§2bis**. Era l'unica delle cinque che non aspettava nessuna decisione, ed è l'unica che il progetto poteva chiudere da solo.

---

## 2bis. B5 chiusa: cosa è costato verificare i pin

*(02/10/2026 — `sorgenti/gis/verifica_pin.py`, otto controlli, tutti superati; `mappe.md` §8bis)*

Il numero dell'audit era giusto e la sua etichetta era sbagliata: i **novanta** non sono novanta pin distinti, sono novanta **slot di pin**, uno per tappa. Dietro ci sono 69 posti, e i posti che hanno coordinate sono 39.

| | slot | posti |
|---|---|---|
| anni 2, 3 e 4 | 90 (30 per anno) | 69 |
| con coordinate, verificati | **53** | **39** |
| senza coordinate, tutti con stato dichiarato | 37 | 37 |

**Il quinto anno è passato dagli stessi controlli lo stesso giorno**, perché il verificatore non era scritto per gli anni 2-4 ma per tutti: 30 slot, 15 posti con coordinate, **nessun difetto**. Portato a tutti e cinque gli anni, il conto è 120 slot e 71 con coordinate.

**I due difetti che sono usciti** non sono nella tabella delle tappe e non si vedrebbero mai guardando i documenti: sono nella tabella delle coordinate.

- **Baghdad**, 34 km a sud del proprio centro. La latitudine era `33.03333` invece di `33.31528`: una cifra. Il file lo dichiarava `verificata`, e lo era stato davvero — la fonte, l'articolo italiano di Wikipedia, riporta 33°02′ N. **Il dato era fedele alla fonte e la fonte era sbagliata**, e solo il confronto con un secondo file lo ha fatto vedere.
- **Karakorum**, che cadeva in **Cina**. Il nome aveva risolto sull'articolo della catena montuosa, non su quello della città. La quota lo aveva già sospettato (8 128 m), e il punto-in-poligono dà la prova che mancava: la coordinata è dentro `CHN`.

**Il caso che non è un difetto**, e che vale quanto i due difetti: **Costantinopoli** non cade in nessun Paese, a nessuna delle tre scale, perché il Corno d'Oro è stretto e la terra è a 1,4 km. Un controllo che avesse detto «in mare, errore» avrebbe fatto riscrivere una coordinata giusta. La soglia dei 3 km è dichiarata nel codice per questa ragione.

**Che cosa resta**: diciannove pin non sono verificabili sull'unità amministrativa, perché il file amministrativo non copre quei Paesi. Non è un buco del gioco, è una copertura mancante di un file che si può scaricare.

**La lezione, che è la stessa di tre volte**: questo progetto ha risolto **un titolo** invece di un luogo (Karakorum due volte, Castel del Monte una volta, Baghdad per la cifra). Il controllo automatico batte la lettura, e questa è la prima volta che lo si vede su un numero che qualcuno aveva firmato come verificato.

**E una lezione sulla lezione.** Il quinto anno non ha prodotto difetti, ma ha prodotto **due errori nella tabella di attese del verificatore** (Rotterdam non è nella provincia che il file chiama «Zelanda»), dopo il primo su Castel del Monte. Il controllo che segnala un'attesa sbagliata vale quanto quello che segnala un pin sbagliato, e una tabella scritta a mano è essa stessa un dato da verificare. **Tre volte su quattro, l'errore era di chi scriveva il controllo**: è la misura onesta di quanto sia facile sbagliare una coordinata con la fonte giusta.

---

## 3. Le quindici importanti

Quelle che, se risposte male, cambiano il gioco. In ordine di peso.

| # | Domanda | Pro | Contro | Valutazione | Chi decide |
|---|---|---|---|---|---|
| I1 | **Il percorso del duca è l'ordine delle tappe o un giro a parte?** (`percorsi.md` Q1) | Il giro copre tutta la mappa e dimezza il viaggio (−31/−49/−43/−58%) | Richiede di cambiare il modo in cui la mappa si disegna: due sequenze invece di una | Il giro: è ciò che rende la mappa un percorso e non una distribuzione di punti | Pietro |
| I2 | ~~**La tavolozza va prodotta?**~~ **chiusa il 03/10/2026** (`fonti-visive.md` Q1) | — | — | **Fatta**: 18 voci in `dati/fonti_visive/tavolozza.json`, e la scelta è quella prevista: dichiarare i colori di ogni fonte, non ricolorare tutto | Il progetto |
| I3 | ~~**Le sagome degli edifici si costruiscono?**~~ **chiusa il 03/10/2026** (`fonti-visive.md` Q2) | — | — | **Fatte**: 5209 sagome su 54 luoghi in `dati/edifici_footprint.json`, nell'ordine previsto (prima la tavolozza) | Il progetto |
| I4 | ~~**Il fondo di Ferrara si costruisce?**~~ **chiusa il 03/10/2026** (`fonti-visive.md` Q3) | — | — | **Fatto**: 14 tratti di mura, 4,20 km², in `dati/ferrara_fondo.json`; il perimetro ufficiale non esisteva in nessuna fonte e l'anello è stato ricostruito con la tolleranza che contiene tutte le tappe | Il progetto |
| I5 | **Che cosa è un «testo autentico» nelle sei lingue?** (`lingue.md` Q3) | Il progetto vieta i testi inventati; per il greco la regola è chiara | Per il ferrarese è una trascrizione di parlante, e lì si aprono consenso e varietà | Serve una regola scritta **prima** di registrare chiunque, non dopo | Pietro, e chi parla per il ferrarese |
| I6 | **Il greco moderno ha una linea propria?** (`lingue.md` Q5) | Tremila anni in tre anni di percorso rischiano di essere un elenco di argomenti | Aggiunge una settima linea a un sistema già largo | Una linea dentro i blocchi 4 e 5, come l'atlante per gli anni 3 e 4 | Pietro |
| I7 | **Che cosa succede se il giocatore non sa l'italiano?** (`lingue.md` Q7) | Il gioco è in italiano, e il percorso presuppone che si perdano punti sui livelli d'italiano | Una soglia diversa per chi l'italiano non ce l'ha è una scelta che va dichiarata, non fatta implicitamente | Una soglia minima per i livelli d'italiano, la stessa soglia alta per chi ce l'ha già; è la regola «nessuna competenza in ingresso» applicata alle lingue | Pietro |
| I8 | **Quanti esercizi fanno le trenta voci?** (`lingue.md` Q8) | Con pool da 20 per gradino sono 3 600 esercizi: è il lavoro più grande del progetto | Se le voci fossero venti, il conto calerebbe di un terzo | Il conto va detto prima di promettere; 3 600 è tanto ma il gioco è tanto | Pietro |
| I9 | **Le fonti del latino e del greco vanno cercate altrove?** (`lingue-immagini.md` Q3) | Il controllo G7 dice che 27 voci latine su 28 hanno solo proposte scoperte per caso | Commons ha le immagini degli oggetti, non le fonti filologiche: servono EDCS, EDR, biblioteche digitali | Sì: per il latino Commons è il posto sbagliato, e va detto | Pietro |
| I10 | **Le immagini servono solo per le facoltative?** (`lingue-immagini.md` Q5) | Le tappe sui testi autentici hanno bisogno di immagini diverse (la pagina di Cesare, non una coppa) | Sono almeno 900 immagini, e nessuna è stata cercata | Sì, e va detto subito: è il buco più grande dopo le sagome | Il progetto |
| I11 | **Le Nuove Indicazioni 2026 vanno acquisite?** (`curricolo.md`) | Sono il riferimento normativo del liceo scientifico | Il fascicolo non è stato acquisito e il §6 è rifatto sul vecchio | Prima di costruire il curricolo, non prima del gioco: è una settimana di lavoro | Pietro |
| I12 | **Quanto dura un livello?** (`curricolo.md`) | Ogni livello deve durare da 5 minuti a qualche ora; senza stima non si sa se 150 livelli stanno in 5 anni | La stima dipende dal prototipo, che non c'è | Stimare sul primo prototipo, non prima | Il progetto |
| I13 | **Il 1945 non è una tappa.** (`anno5-mondo.md` §13) | Il materiale ci mette Roosevelt, Cassin, Lauterpacht, e i livelli non li chiedono | Sostituirlo significa scegliere un'altra tappa che i livelli non coprono | Va deciso con il buco della biologia (I14), e sono lo stesso problema | Pietro |
| I14 | **Il buco della biologia nel quinto anno.** (`anno5-mondo.md` §13) | Il materiale dedica quindici voci a medicina, vaccini, DNA e nessun livello le copre | Levare voci dal materiale è una decisione sua, non del progetto | È il buco tematico più grosso del quinto anno | Pietro |
| I15 | **La tratta e l'imperialismo nell'anno 3.** (`anno3-europa.md` §13) | È un buco reale: nessun personaggio obbligatorio porta l'Europa fuori dall'Europa | Aggiungere una scheda di atlante che i livelli non chiedono, o dichiarare il limite | Dichiarare il limite è più onesto; una scheda di atlante sul colonialismo è giusta ma è un atlante | Pietro |
| I16 | **Leonardo in due anni.** (`anno3-europa.md` §13) | È il caso più bello del percorso: la stessa persona è «il linguaggio delle figure» e poi «la scomposizione del metodo» | Viola la regola dei ritorni che il progetto si è data | Si tiene: il ritorno forte vale più della regola, e la regola va corretta con l'eccezione | Pietro |
| I17 | **Il formato del file di consegna.** (`meccaniche.md`) | `.txt` è la proposta, ed è leggibile ovunque | Il PDF è più sicuro contro le manomissioni | `.txt` con firma, e la firma è ciò che rende la consegna verificabile | Pietro |
| I18 | **Il gioco è un modulo della piattaforma gamificata o un prodotto a sé?** (`meccaniche.md`, `curricolo.md`) | Le due scelte danno requisiti diversi su privacy, punteggio, consegna | Rimandarla non blocca niente subito | Prodotto a sé, con i requisiti della piattaforma come caso particolare | Pietro |
| I19 | ~~**I colori dei fondi geografici.**~~ **chiusa il 03/10/2026** (`fonti-visive.md` Q4) | — | — | **Fatto**: `dati/fonti_visive/colori_cartografici.json`, 17 voci (16 dichiarate con motivo e criterio, 3 prese dalla tavolozza con l'esadecimale confrontato byte per byte), la regola che **una categoria con il riempimento ha anche il bordo**, e `verifica_colori.py` (C1–C7). **Cercandoli è saltato fuori un difetto che non era di colori**: `mondo_admin1_copertura.json` stava dentro `dati/mappe/` e faceva crashare il lettore | Il progetto |

---

## 3bis. Quattro importanti chiuse il 3 ottobre

*(03/10/2026 — le quattro sono I2, I3, I4 e I19, e nessuna delle quattro aspettava una decisione)*

La sezione 3 era la più lunga del documento e le sue prime tre voci erano tre lavori che il progetto poteva fare da solo. Le tre sono fatte, in quest'ordine, e l'ordine è dichiarato perché l'ordine è una decisione. La quarta, I19, è arrivata dopo e ha portato con sé un difetto che nessuna delle altre tre aveva trovato.

**I2, la tavolozza.** `dati/fonti_visive/tavolozza.json`, **18 voci**. La domanda aveva due metà — ricolorare tutto a una tavolozza unica, oppure dichiarare i colori di ogni fonte — e la seconda era quella coerente con le tre regole già prese su etichette e proporzioni. Costruirla ha trovato tre difetti che valgono quanto la tavolozza: **un pigmento non si cerca per nome** («vermilion» è una città canadese, «red ochre» un premio televisivo), **`P462` non è l'esadecimale** ma un link a un oggetto colore, e il suo valore è un dizionario e non una stringa, e **cinque pigmenti su quindici non hanno codice in nessuna fonte**: nessuno dei cinque è stato riempito con una cifra plausibile. Il `verifica_tavolozza.py`, sei controlli, è stato eseguito **in rete**: 10 fonti ricontrollate, **0 problemi**.

**I3, le sagome degli edifici.** `dati/edifici_footprint.json`, 1,6 MB, **5209 edifici su 54 luoghi**. La valutazione che c'era in questa riga diceva «sì, ma non è la prima cosa: prima la tavolozza» — ed è l'ordine in cui sono state fatte. Il risultato che conta non è il numero di edifici ma la rinuncia dichiarata: **3336 edifici su 5209 non hanno altezza** in OSM, e diventano un volume neutro dichiarato invece di una stima. Una forma che non è verificata non si disegna, ed è la regola che il progetto si era già data sui luoghi senza coordinate.

**I4, il fondo di Ferrara.** `dati/ferrara_fondo.json`, 14 tratti di mura OSM, **8601 m di perimetro e 4,20 km²**, con la tolleranza di 60 m scelta **non a occhio ma come la più piccola in cui tutte e 28 le tappe del primo anno cadono dentro**. Una fonte è stata rifiutata e dichiarata: la relation OSM «Centro storico», che copre 1,34 km² e lascia fuori Piazza Ariostea e Palazzo dei Diamanti. Il vuoto più grosso — **1037 m** di mura che nessuna fonte disegna — resta dichiarato.

**I19, i colori dei fondi geografici.** `dati/fonti_visive/colori_cartografici.json`, **19 voci**: 16 dichiarate con motivo e criterio, 3 prese dalla tavolozza con la chiave dichiarata e l'esadecimale confrontato byte per byte. La valutazione che c'era in questa riga diceva «costa mezz'ora» ed era ottimista: il file è un'ora, i due verificatori che lo tengono fermo sono un'altra, e **cercandolo è saltato fuori un difetto che non era di colori**. `dati/mappe/mondo_admin1_copertura.json` stava **dentro `dati/mappe/`**, dove vale la regola che ci stanno solo file nel formato a delta, e faceva crashare `mappe_lettore.leggi()` con un `IndexError: list index out of range`: il peggiore dei sintomi, perché dice una lista troppo corta e non dice che il problema è un file che non aveva niente a che fare lì. Il file è stato spostato in `dati/`, il lettore ora controlla la forma del file e solleva un `ValueError` che la dice, e il controllo **C6** tiene la regola ferma. Nello stesso giorno sono entrati anche i **tre file delle cime** (`mappe.md` §2.5), con la scoperta che la fonte è **mondiale in tutte e tre le scale** e che i tre file **non sono annidati**.

**E un quarto file, che non era una domanda ma senza il quale i tre sarebbero stati tre tavole isolate.** `dati/ambienti_livelli.json` è **un ambiente per ognuno dei 150 livelli**, costruito sul modello dell'unica zona già esistita (la tappa 1-1) e con tutti i vuoti dichiarati: 99 ambienti con coordinate, 69 con sagome, e **uno solo che il motore ha davvero disegnato**. È il file che risponde alla domanda che nessuno aveva scritta: «e quindi, che cosa si disegna a ogni tappa?». Nello stesso giorno è entrato anche `mondo_admin1.json`, che chiude in `mappe.md` §2.4 la copertura amministrativa mancante: **54 pin coperti su 54**.

**Che cosa insegna, tenendo conto delle altre.** Sono sei chiusure in tre giorni, e cinque delle sei erano lavori. Le uniche decisioni che il progetto ha preso da solo in questa settimana — ODbL, la regola dei due strati — hanno tutte e due tolto lavoro. È la stessa frase che la v0.4 faceva con una chiusura, e con cinque vale ancora di più.

---

## 3ter. Altre sei chiuse il 3 ottobre, e una di loro era un difetto travestito da domanda

*(03/10/2026 — lavoro della sera, dopo la scelta dei premi. Nessuna delle sei era bloccante, e una delle sei non era una domanda)*

| voce | stato | che cosa è successo |
|---|---|---|
| **Il numero dei livelli trasversali** | **chiusa** | Sono **zero**: il trasversale è un aggancio dentro i livelli, non un livello (`quadro-trasversale.md` §1.3). Il conto dei premi è quindi **1050**, non i «circa 900» che il progetto portava da tre giorni: la cifra vecchia contava i soli livelli linguistici e dimenticava i centocinquanta informatici. Un numero che si sbaglia di un sesto è un numero che non si può usare per scrivere un catalogo |
| **La variante dei premi** | **chiusa** | Un premio per livello, 1050 record (`premi.md` §4.0) |
| **Il premio della LIS** | **chiusa** | La categoria **K**: la scheda che il giocatore produce. Non esistono 150 figure sorde documentabili (`premi.md` §2.1) |
| **`osservazione e attenzione`** | **chiusa, ed era un difetto** | Due documenti dicevano che il dominio «non esiste ancora» e lo lasciavano `da_costruire`. Esiste in quattro posti che nessuno aveva messi insieme: il nucleo `Q8.2` del livello 3-27, l'osservazione linguistica dei novecento livelli, le tappe 1-23 e 1-29, la 5-11. Una cosa che il gioco fa senza dirlo non è una lacuna: è una riga rimasta indietro |
| **La 3-28** | **chiusa** | Manchester nel registro, Torino nel documento: era una divergenza dichiarata, e l'ha chiusa la rigenerazione. Il registro ora prende il luogo dalla riga della tabella |
| **La 4-16** | **chiusa davvero** | Era un dato corretto a mano che nessuno poteva rifare. Ora la catena `estrai_luoghi.py` → `coordinate.py` → `classifica.py` lo produce, e `verifica_catena_luoghi.py` lo controlla |

**La quarta è la più instructive, e il titolo della sezione è voluto.** Un dominio dichiarato assente è la cosa più economica che si possa scrivere: non richiede di cercare niente, e la riga sembra onesta («non lo abbiamo costruito»). Ma la domanda vera era **«dove lo abbiamo costruito senza accorgercene?»**, e la risposta era in quattro posti che nessuno aveva leti insieme. Il difetto non era la lacuna: era la domanda che non era stata fatta.

**E le tre difettose che sono venute fuori mentre si chiudeva.** La catena dei luoghi non è mai stata eseguita end to end, ed eseguendola sono usciti tre difetti che nessun controllo vedeva: `estrai_luoghi.py` leggeva le colonne per numero e nell'anno 5 leggeva la stanza al posto della voce (29 tappe su 30 con il filone del *Furioso* al posto della persona); le correzioni di Baghdad e Karakorum vivevano solo in un JSON editato a mano e sparivano alla prima rigenerazione; `classifica.py` aveva due copie della regola che assegna lo stato della coordinata, e le due copie erano già divergenti. Tutte e tre sono chiuse, e `sorgenti/verifica_catena_luoghi.py` ha cinque controlli che le mordono.

---


## 3quater. La parte orale: un documento che risponde a una domanda, e un difetto nel README

*(03/10/2026 — dopo la richiesta di Pietro su speaking e listening)*

`videogioco-5-duchi-parlato.md` (v0.2) chiude il «si può fare» di ascolto e parlato, e
la risposta è articolata in **cinque livelli** invece che in un sì. I quattro fatti che
la costringono:

1. **La Web Speech API è esclusa**: su Chrome manda l'audio ai server di Google e non
   funziona offline. Un gioco senza server non può mandare la voce di un adolescente
   fuori dal dispositivo.
2. **Il materiale esiste per tre lingue e non per le altre**: su Wikimedia Commons, via
   `cerca_audio_oggetti.py`, ci sono **89 381** registrazioni in inglese, **9 179** in
   italiano, **79** in greco, **24** in latino e **zero** in ferrarese.
3. **Il riconoscimento on-device esiste ma non per il ferrarese**, e su una voce di
   minore è una decisione di privacy, non una scelta tecnica.
4. **Il gioco può comunque allenare il parlato**, perché durata, pause, ritmo e
   riascolto si misurano senza riconoscere niente.

Il numero che conta è il secondo: **la lingua di cui il progetto ha più bisogno di
ascolto è l'unica che non ha una registrazione libera al mondo**. La risposta non è
cercarla, è **produrla**: il gioco chiede a chi parla la lingua e mette la registrazione
nel quaderno del giocatore. È la stessa forma della categoria K per la LIS — **il
gioco non sa fare una cosa, e non finge: mette dentro la cosa che non sa fare il
giocatore**.

Cinque decisioni sono di Pietro e restano aperte (`parlato.md` §6): il permesso del
microfono, l'audio nel file di consegna, le opere intere, l'apertura del
riconoscimento on-device, e chi raccoglie le registrazioni dei nonni ferraresi.

**E un difetto vero, trovato per via.** Mizando la tabella dei documenti del README,
uno script ha scritto la versione nella cella del nome del file: **otto righe su
trenta avevano perso il documento che descrivevano**, e la coerenza diceva zero perché
una riga senza nome non nomina nessun documento e quindi non può contraddirlo. Le righe
sono state ricostruite e il controllo che mancava è stato scritto: ogni riga
numerata della tabella deve nominare un file che finisce in `.md` e deve finire con una
versione. Provato, e morde.

---

## 4. Le altre, in sintesi

Le **restanti**: minori, o già decise nella sostanza e che aspettano solo l'esecuzione. Chi decide è Pietro quasi sempre, e dove è il progetto è perché non è una domanda ma un lavoro.

### Sistema linguistico (restano 8)

| Domanda | Chi decide |
|---|---|
| Il confronto fra le sei lingue è obbligatorio o a rotazione? Il calcolo dà il 17% del totale | Pietro |
| I confronti filologici sono vincolanti, e come li si controlla | Pietro |
| Le trenta voci ferraresi: che tappa hanno, se non hanno immagine | Pietro |
| Chi ridimensiona le immagini scelte a 96×72, e quando | Il progetto |
| Il livello 30 di ogni lingua è un compito: che cosa produce, e con quale criterio di superamento | Pietro |

### Percorsi (restano 5)

| Domanda | Chi decide |
|---|---|
| Il giro si chiude a Ferrara? Costo 10-101 giorni di viaggio che il gioco non fa pagare | Pietro |
| Il mezzo cambia dentro l'anno? Nel quarto anno è il mezzo di chi porta il documento | Pietro |
| Le facoltative continentali si aprono sul ritorno | Pietro |
| I buchi continentali degli anni 3, 4 e 5 | Pietro |
| Il tempo di viaggio è un esercizio giocabile o una dichiarazione | Pietro |

### Fonti visive (restano 2)

| Domanda | Chi decide |
|---|---|
| Chi guarda i 125 candidati delle fonti visive | Io o Pietro |
| Le due facoltative continentali dell'anno 4 si aprono sul ritorno | Pietro |

### Anno 1 (7) e curricolo (5)

| Domanda | Chi decide |
|---|---|
| Il narratore: che ruolo hanno gli altri duchi nel percorso | Pietro |
| Renzo Ravenna e le 20 schede aggiunte: approvare o scartare | Pietro |
| La mappa digitale di Ferrara che Pietro deve fornire | Pietro |
| Le fonti primarie, scheda per scheda | Il progetto |
| La verifica storica complessiva, con un collega o con l'Archivio di Stato | Pietro **e un istituto** |
| Il secondo linguaggio tipizzato (C++ o Java) al 3º o 4º anno | Pietro |
| Il rapporto con la piattaforma gamificata (vedi I18) | Pietro |
| L'allineamento interdisciplinare con le programmazioni reali di classe | Pietro **e i colleghi** |
| Le fonti storiche del §4 | Il progetto |

### Anno 2 (8)

| Domanda | Chi decide |
|---|---|
| La carta intera alla fine dell'anno: si aprono tutti gli strati insieme | Pietro |
| Tre collettivi su trenta tappe: alternativa (a) o (b) | Pietro |
| Il bilancio degli agganci: 13 forti e 17 medi | Pietro |
| La colonna stratigrafica sempre visibile a schermo | Pietro |
| Il materiale dal 1500 in poi | Pietro |
| Le persone viventi (Cristoforetti) | Pietro |
| Le fonti del materiale | Il progetto |
| Le «visioni» dell'anno 1 nell'anno 2 | Pietro |

### Anno 3 (restano 7), anno 4 (4), anno 5 (restano 7)

| Domanda | Chi decide |
|---|---|
| Il bilancio degli agganci: 21 forti, 9 medi, e tre forse troppo forti | Pietro |
| Persone viventi (von der Leyen, Merkel, Macron): solo emblemi | Pietro |
| Le sei aggiunte (Josquin, Bellini, Dürer, Manuzio, Caxton, Levi) | Pietro |
| La corte come unico luogo percorribile: la alternativa è il visitatore-inviato | Pietro |
| La regola di AGENTS.md sul duca guida dal terzo anno (già scritta, va tenuta allineata) | Il progetto |
| I tre agganci «forti» da rivedere dell'anno 4 | Pietro |
| La tappa 4-10 e l'incendio dell'archivio | Pietro |
| Chi è il protagonista del quinto anno: dentro il *Furioso*, con la regola dei due strati (parzialmente risolta) | Pietro |
| Il quinto anno e l'anno 3: come si dividono il Novecento | Pietro |
| I facoltativi che il gioco non può mettere in tabella | Il progetto |
| I quattro agganci da rivedere del quinto anno | Pietro |
| Le previsioni con la data: si rileggono fra dieci anni, e con quale formato | Pietro |
| Il posto di F11 nel registro del gioco | Pietro |

### Luoghi (2), mappe (3), *Furioso* (2), gioco (5), meccaniche (5)

| Domanda | Chi decide |
|---|---|
| Le undici facoltative continentali: proposte e non schede | Pietro |
| Il tipo di legame dei ventisei pin del quinto anno | Pietro |
| Il vincolo di 20 000 abitanti per mostrare una città | Pietro |
| Le trenta zone percorribili: tutte, o solo dove il luogo è lo spazio del gioco | Pietro |
| Il file delle regioni amministrative: intero o ridotto | Il progetto |
| Le ventisei stanze senza coordinata: la regola che le dichiara | Pietro |
| I motti e i dialoghi delle trenta tappe | Pietro |
| Confermare la tappa 1-30 (P93, la città) | Pietro |
| Verificare che v86 e Pyodide funzionino sui computer del laboratorio e sui Chromebook | Il progetto **e il laboratorio** |
| Per 1-25 e 1-26: strumento nel gioco, file caricato, o entrambi | Pietro |
| I pesi e le soglie del meccaniche §2.3, calibrati sul prototipo | Il progetto |
| Quanti eventi di dettaglio conservare nel codice di ripresa | Il progetto |
| Lo strumento del docente: subito o dopo il prototipo | Pietro |
| Safe Exam Browser e la proposta al regolamento d'istituto sui dispositivi indossabili | Pietro **e l'istituto** |
| La specifica della modalità accessibile | Il progetto **e il progetto di accessibilità del gioco** |

---

## 5. Le domande che sono due

Tre questioni compaiono in due documenti, e una è la stessa identica:

| La domanda | Dove | Nota |
|---|---|---|
| Le trenta voci sono confermate | `lingue.md` Q2 = `lingue-immagini.md` Q2 | Una risposta sola chiude due |
| Una linea che attraversa gli anni senza essere una tappa | `lingue.md` Q5 = `anno5-mondo.md` | Stessa idea, risposta data per gli anni 3-4 e non per le lingue antiche |
| I codici `Q` dei personaggi | `anno3` Q6 = `anno4` Q5 = `anno5` Q4 | **L'unica ridondanza che funziona**: confermati in tutti e tre i documenti e concordanti. È la prova che funziona quando qualcuno la controlla |

---

## 6. La sequenza che chiude tutto

Le cinque bloccanti hanno una catena sola.

**B2** (voci confermate) viene **prima** di **B4** (chi guarda le immagini): cercare le immagini prima di aver confermato le voci è lavoro da rifare. **B1** (livelli linguistici o informatici) decide quanti tipi di tappa esistono, e quindi decide se B4 ha senso come domanda.

La catena è: **B1 → B2 → B4**. **B3** (la LIS) è indipendente e parte in parallelo, ed è la più lenta. **B5** (i novanta pin) non aspettava nessuna e **è stata fatta il 02/10/2026**: otto controlli, due difetti corretti (§2bis); **il primo anno, che non era coperto, ha cinque controlli suoi dal 03/10** (`mappe.md` §8ter, A1-A5). Il 03/10/2026 è successa la stessa cosa quattro volte di fila con I2, I3, I4 e I19, e con dei file che non erano domande: **sei chiusure in due giorni, e cinque erano lavori** (§3bis).

E la regola che ne segue, che è quella che il lavoro ha reso vera:

> **Mentre si decide, si costruisce quello che si può costruire.** Le quattro bloccanti aspettano una risposta e aspetteranno ancora: nessuna delle ventotto chiuse le toccava. Il conto di due giorni dice che la risposta non è l'unica cosa che si può fare mentre si aspetta — e non è una metafora: i controlli automatici hanno trovato due coordinate sbagliate che nessuno aveva lette, e i quattro file del 03/10 sono nati tutti da controlli che non avrebbero potuto dare torto.

---

## 7. Registro delle modifiche

| Data | Versione | Che cosa è cambiato |
| 03/10/2026 | 0.9 | **La parte orale è un documento, e il README aveva un difetto che nessun controllo vedeva.** Nasce `videogioco-5-duchi-parlato.md` (v0.2): la Web Speech API è esclusa perché manda l'audio ai server di Google, il riconoscimento on-device è dichiarato non fatto (non esiste per il ferrarese e riguarda dati di un minore), e il gioco può comunque allenare il parlato misurando **durata, pause, ritmo e riascolto**. Il dato che decide: su Commons ci sono **89 381** registrazioni inglesi, **9 179** italiane e **zero** ferraresi — la lingua di cui il progetto ha più bisogno è l'unica che non ha audio libero, e la risposta è produrlo chiedendo a chi lo parla, come si fa per la LIS con la categoria K. Cinque decisioni restano a Pietro (`parlato.md` §6).

**Il difetto.** Mizando la tabella dei documenti del README, uno script ha scritto la versione nella cella del nome del file: **otto righe su trenta avevano perso il documento che descrivevano**, e la coerenza riportava **zero** perché una riga senza nome non nomina nessun documento e quindi non può contraddirlo. Ricostruite a mano, e il controllo che mancava è scritto: ogni riga numerata nomina un file che finisce in `.md` e finisce con una versione. Provato con un difetto iniettato, e morde.

| 03/10/2026 | 0.8 | **Sei voci chiuse, e una di loro non era una domanda: era un difetto.** Aggiunta **§3ter**. Il **numero dei livelli trasversali** è chiuso — sono **zero**, perché il trasversale è un aggancio dentro i livelli e non un livello (`quadro-trasversale.md` §1.3) — e con esso il conto dei premi, che è **1050 e non i «circa 900»** che il progetto portava da tre giorni: la cifra vecchia contava i soli livelli linguistici e dimenticava i centocinquanta informatici. La **variante dei premi** e il **premio della LIS** erano già chiuse oggi e sono qui raccolte. La **`osservazione e attenzione`** era dichiarata `da_costruire` in due documenti con la frase che «il gioco non ha mai lavorato sull'attenzione come oggetto», ed è un difetto: il dominio esiste in quattro posti che nessuno aveva messi insieme (il nucleo `Q8.2` del livello 3-27, l'osservazione linguistica dei novecento livelli, le tappe 1-23 e 1-29, la 5-11). La lezione che vale è la regola: **una cosa che il gioco fa senza dirlo non è una lacuna, è una riga rimasta indietro**.

La **3-28** è chiusa: era la divergenza dichiarata fra registro e documento (Manchester e Torino) e l'ha chiusa la rigenerazione, che ha portato le divergenze da una a zero. La **4-16** è chiusa *davvero*: era un dato corretto a mano che nessuno poteva rifare, e ora la catena `estrai_luoghi.py` → `coordinate.py` → `classifica.py` lo produce. Eseguendola sono usciti **tre difetti che nessun controllo vedeva**: l'estrattore leggeva le colonne per numero e nell'anno 5 leggeva la stanza al posto della voce (29 tappe su 30 con il filone del *Furioso* al posto della persona); le correzioni di Baghdad e Karakorum vivevano solo in un JSON editato a mano e sparivano alla prima rigenerazione (ora stanno in `dati/luoghi_correzioni.json`); e `classifica.py` aveva due copie divergenti della regola che assegna lo stato della coordinata. Il nuovo `sorgenti/verifica_catena_luoghi.py` ne ha cinque. Il conto di §1 non cambia: le sei voci di oggi non erano voci dell'audit.

|---|---|---|
| 03/10/2026 | 0.7 | **La B1 è spiegata in parole semplici, e due buchi che erano dichiarati aperti sono chiusi.** Pietro ha chiesto di capire la B1 «meglio, con parole più semplici»: sotto la scheda c'è ora **B1 in parole semplici**, che dice che cosa sono i 150 livelli informatici e i 900 linguistici, quale sarà la schermata che il ragazzo vede nella tappa 5-12 (**un compito solo, 32 compiti in fila, o tappe alterne**), che cosa è già costruito e che cosa è bloccato, e che la stima delle schermate — cioè la cosa che servirebbe per decidere — dipende da un prototipo che non esiste. **La domanda è di Pietro e resta aperta.** Intanto sono chiuse tre cose: la **Q6.2** (`furioso.md` §4.12: nessuna stanza ha un disegno proprio, quattro regole, tempo di Pietro **zero**), le **51 ipotesi di coordinata** (`luoghi.md` §4.8: 28 documentate, 21 argomentate con il raggio in metri, 2 immaginate e senza punto; regole **R1-R6** e controllo **B7**) e **l'anno 1**, che non era coperto da nessun controllo dei pin e ora ha cinque controlli suoi, **A1-A5** (`mappe.md` §8ter: **30 tappe su 30 dentro le mura**, e soprattutto **0 tratti fuori sui 29** percorsi fra tappe consecutive, che è l'unico controllo che solo una città dentro le mura può avere). Le 51 ipotesi hanno anche fatto nascere i **mezzi** dell'anno 4 e 5: 22 mezzi, con l'anno di attestazione di ciascuno e un controllo di anacronismo **per tappa** che ne ha trovato uno nella stessa impostazione (`percorsi.md` §1.2). Il conto passa a **29 chiuse** e **85 aperte**; le quattro bloccanti restano quattro e sono le stesse: nessuno dei lavori di oggi le toccava, perché sono lavori che si possono fare senza la risposta. |
| 03/10/2026 | 0.6 | **Quattro importanti chiuse in un giorno, e la quarta ha portato con sé un difetto che le altre tre non avevano trovato.** I colori dei fondi geografici (I19, `fonti-visive.md` Q4) sono in `dati/fonti_visive/colori_cartografici.json`, **19 voci**, con la regola che una categoria con il riempimento ha anche il bordo e i due verificatori che la tengono ferma (`verifica_colori.py`, C1–C7). **Cercandoli è emerso che `dati/mappe/mondo_admin1_copertura.json` stava dentro `dati/mappe/`**, dove vale la regola del solo formato a delta, e faceva crashare il lettore delle mappe con un `IndexError` che non diceva niente: il file è stato spostato in `dati/` e il lettore ora solleva un `ValueError` che nomina il percorso. Nello stesso giorno sono entrati i **tre file delle cime** con la loro quota (`mappe.md` §2.5), e la scoperta che vale più dei tre file: la fonte è **mondiale in tutte e tre le scale** e i tre file **non sono annidati**, quindi un motore che li trattasse come risoluzioni diverse dello stesso elenco sbaglierebbe senza che nessun controllo lo vedesse. Chiusa anche la **Q6.1** del *Furioso*: `F11` è dichiarato filone **non assegnato** e la decisione è nei dati (`citazioni.json` v4), tenuta ferma dalla verifica **F16**. Il conto passa a **28 chiuse** e **86 aperte**, e le importanti da sedici a **quindici**. Le quattro bloccanti restano quattro e sono le stesse di prima: nessuno dei quattro lavori le toccava. |
| 03/10/2026 | 0.5 | **Tre importanti chiuse in un giorno, e le tre erano lavori, non domande.** La tavolozza (`fonti-visive.md` Q1), le sagome degli edifici (Q2) e il fondo di Ferrara (Q3) sono prodotti il 03/10/2026: `tavolozza.json` con 18 voci, `edifici_footprint.json` con 5209 sagome su 54 luoghi, `ferrara_fondo.json` con 14 tratti di mura e 4,20 km². Nello stesso giorno è entrato `mondo_admin1.json`, il file amministrativo mondiale che chiude la copertura mancante di `mappe.md` §8bis, e `ambienti_livelli.json`, un ambiente per ciascuno dei 150 livelli. Il conto passa a **26 chiuse** e **88 aperte**, e le importanti da diciannove a **sedici**. La lezione che si vede nel conto è la stessa di B5: **nessuna delle tre aspettava una decisione**, e nessuna delle ventisei chiuse è bloccante. Le quattro bloccanti restano quattro e sono le stesse di prima: nessuno dei tre lavori le toccava. |
| 02/10/2026 | 0.1 | Prima stesura. Le dodici sezioni «Questioni aperte» allora esistenti, **96 voci**, 22 chiuse e 74 aperte, cinque bloccanti, e la catena delle dipendenze. |
| 02/10/2026 | 0.4 | **Il quinto anno passa dagli stessi controlli.** `verifica_pin.py` è stato generalizzato (`--anno N`, `--tutti`) e ha coperto i 30 slot del quinto anno: **15 posti con coordinate, nessun difetto**. Il quinto anno ha però prodotto due errori nella **tabella degli attesi** del verificatore (Rotterdam), secondo caso dopo Castel del Monte. `mappe.md` sale a v0.6 e §8bis porta il conto completo di tutti e cinque gli anni: **120 slot, 71 con coordinate**. Aggiunto in §8bis che l'**anno 1 non è coperto**, perché i suoi pin prendono il confine dal WFS del Comune. Il resto del documento non cambia: il conto è 114 voci, 23 chiuse, 91 aperte, quattro bloccanti. |
| 02/10/2026 | 0.3 | **B5 chiusa.** La verifica dei pin degli anni 2, 3 e 4 è fatta (`sorgenti/gis/verifica_pin.py`, otto controlli, tutti superati): 53 slot di pin con coordinate su 90, e **due difetti reali corretti** — Baghdad a 34 km dal proprio centro, Karakorum in Cina invece che in Mongolia. Il numero 90 era esatto ma era il numero degli **slot**, non dei pin distinti: dietro ci sono 69 posti. Il conto passa a **23 chiuse** e **91 aperte**, e le bloccanti da cinque a **quattro**. Aggiunta **§2bis**, che dice cosa è costato e che cosa resta (nove pin senza unità amministrativa, per copertura del file e non per difetto). Rimando a `mappe.md` aggiornato a v0.5. |
| 02/10/2026 | 0.2 | La **lista operativa**. Il contatore è stato corretto perché vedeva tredici documenti su quindici e sbagliava il conto: ora sono **114 voci**, 22 chiuse e **92 aperte**, con i documenti nuovi (`lingue.md`, `lingue-immagini.md`, `percorsi.md`, `fonti-visive.md`) dentro. Ogni bloccante e ogni importante ha **pro, contro, valutazione e responsabilità**; le altre settantatre sono in sintesi con chi decide. Registrata una doppia domanda (`lingue.md` Q5 = `anno5-mondo.md`) e la catena B1 → B2 → B4. |