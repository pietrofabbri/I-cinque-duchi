---
titolo: Videogioco "I cinque duchi" — curricolo dei 150 livelli (bozza)
versione: 0.1
data: 2026-09-27
autore: Pietro Fabbri (con Claude)
stato: bozza di lavoro, da integrare con il materiale di Pietro sui duchi e con le nuove Indicazioni nazionali 2026 (sezione Informatica non ancora acquisita)
documenti collegati: mappa-informatica.md (ID dei nodi usati qui), mappa-informatica-A.md
---

# Videogioco "I cinque duchi": curricolo dei 150 livelli

## 0. Come leggere questo documento

Il documento è pensato per essere usato anche senza il contesto della conversazione in cui è nato, da persone o da altre AI. Contiene:

1. i **requisiti** fissati da Pietro;
2. il **quadro normativo** da ricalcare (Indicazioni nazionali, liceo scientifico opzione scienze applicate) e le avvertenze sul suo aggiornamento;
3. il **modello di livello**, cioè lo schema dati di ogni livello;
4. la **cornice narrativa** proposta (un duca per anno);
5. l'**elenco dei 150 livelli** (30 per anno);
6. la **verifica di copertura** rispetto alle Indicazioni;
7. le **questioni aperte**.

**Convenzioni**

- `B2.1`, `E7.3`… sono gli ID dei nodi di `mappa-informatica.md`. Servono a generare prerequisiti e contenuti procedurali.
- `AC SO AL DE RC IS CS BD` sono le aree tematiche delle Indicazioni 2010 (vedi §2).
- ★ indica un contenuto **oltre le Indicazioni**, cioè il "fare di più". Nel livello è comunque obbligatorio, ma si può spostare negli approfondimenti se serve alleggerire.
- **Prova di corte** indica un livello-traguardo, presente ogni 10 livelli. È integrativo: riprende e combina i 9 livelli precedenti.
- I collegamenti interdisciplinari sono **proposte da verificare** con le programmazioni dei colleghi del consiglio di classe.

---

## 1. Requisiti (fissati da Pietro)

| # | Requisito |
|---|---|
| R1 | Il gioco ricalca **almeno** il programma di Informatica del liceo scientifico opzione scienze applicate, **anno per anno**. Dove possibile va oltre. |
| R2 | La materia è Informatica. Vengono toccate anche le **propedeuticità in altre materie** e sono favoriti i **collegamenti interdisciplinari**. |
| R3 | **30 livelli per anno** in sequenza, quindi 150 livelli in 5 anni. |
| R4 | Ogni livello ha un **livello minimo di approfondimento** (soglia) che sblocca il livello successivo, più **approfondimenti facoltativi** a piacere. |
| R5 | Ambientazione: i **cinque duchi d'Este di Ferrara**. |

Requisiti ereditati dal progetto collegato "piattaforma gamificata" (**da confermare**: non è ancora deciso se il gioco sia un modulo di quella piattaforma):

- nessun account, per motivi di privacy;
- consegna dei progressi tramite Google Classroom, in un formato leggibile dal docente;
- punteggio che valuta il **processo** (tempi, tentativi, coerenza dei passaggi), non solo la risposta;
- gioco autoesplicativo;
- istanze generate proceduralmente, con difficoltà crescente;
- scala di gradualità interna per ogni argomento.

---

## 2. Quadro normativo

### 2.1 Indicazioni nazionali 2010 (in vigore)

Fonte: Schema di regolamento delle Indicazioni nazionali per i licei (DPR 89/2010), sezione "Liceo scientifico, opzione scienze applicate — Informatica" (file caricato da Pietro, pp. 368–370).

**Aree tematiche:**

- architettura dei computer (AC);
- sistemi operativi (SO);
- algoritmi e linguaggi di programmazione (AL);
- elaborazione digitale dei documenti (DE);
- reti di computer (RC);
- struttura di Internet e servizi (IS);
- computazione, calcolo numerico e simulazione (CS);
- basi di dati (BD; nel testo, per refuso, compare anche la sigla "BS").

**Primo biennio**

- **AC**: hardware e software; introduzione alla codifica binaria (ASCII, Unicode); macchina di von Neumann (CPU, memoria, dischi, bus, periferiche).
- **SO**: concetto e funzioni di base del sistema operativo; sistemi più comuni; processo come programma in esecuzione; gestione della memoria di base; file system.
- **DE**: elementi di un documento elettronico e strumenti di produzione, con particolare attenzione al foglio elettronico.
- **IS**: struttura e servizi di Internet; comunicazione e ricerca di informazioni efficaci; problematiche e regole d'uso.
- **AL**: principi dei linguaggi di programmazione; tipologie di linguaggi; concetto di algoritmo; implementazione in pseudocodice o in un linguaggio di cui si introduce la sintassi.

**Secondo biennio.** I temi si scelgono secondo il contesto e i rapporti con le altre discipline:

- **DE**: strumenti avanzati per i documenti, linguaggi di markup (XML), formati non testuali (bitmap, vettoriale, compressione), font tipografici, progettazione web;
- **BD**: introduzione al modello relazionale; linguaggi di interrogazione e manipolazione dei dati;
- **AL**: implementazione di un linguaggio di programmazione; metodologie di programmazione; sintassi di un linguaggio orientato agli oggetti.

**Quinto anno**

- **CS**: principali algoritmi del calcolo numerico; principi teorici della computazione; semplici simulazioni a supporto della ricerca scientifica (studio quantitativo di una teoria, confronto di un modello con i dati), possibilmente legate a fisica o scienze;
- **RC/IS**: reti, protocolli, struttura di Internet e servizi di rete.

**Linee generali da rispettare trasversalmente**

- Teoria e pratica su un piano paritario e integrate.
- Collegamento sistematico tra strumenti e concetti sottostanti.
- Collegamenti con le discipline scientifiche, con la filosofia e con l'italiano (fondamenti logici, influenza sul metodo scientifico, nascita di nuove scienze).
- Scelta dei componenti hardware, loro configurazione, valutazione delle prestazioni, mantenimento dell'efficienza.
- Approfondimenti mirati all'università negli ultimi due anni.

**Nota.** Le Indicazioni 2010 sono scritte **per biennio**, non per anno. La ripartizione anno per anno del §5 è quindi una **scelta progettuale** coerente con il testo e con la prassi diffusa (primo anno: codifica, hardware, sistema operativo, documenti; secondo anno: algoritmi e programmazione; terzo anno: formati, markup e web; quarto anno: programmazione a oggetti e basi di dati). Non è un obbligo normativo.

### 2.2 Nuove Indicazioni nazionali per i licei (2026): avvertenza

- Il 22 aprile 2026 il Ministero ha pubblicato la **bozza** delle nuove Indicazioni per i licei, con un fascicolo dedicato al liceo scientifico opzione scienze applicate. La consultazione delle scuole è durata fino al 31 maggio 2026.
- Secondo le fonti di stampa, l'entrata in vigore è prevista da **settembre 2027 per le classi prime** (a.s. 2027/28), poi progressivamente per le classi successive.
- **La sezione Informatica della bozza non è stata ancora acquisita.** I siti che ospitano il PDF non sono raggiungibili da questo ambiente, oppure ne restituiscono solo le prime sezioni.
- **Conseguenza progettuale.** Il curricolo qui sotto è costruito sulle Indicazioni 2010. Ogni livello è però etichettato con l'area delle Indicazioni e con i nodi della mappa. Quando si acquisisce il testo 2026 basta rifare la verifica del §6 e spostare o aggiungere livelli, senza riprogettare tutto. Dalle sintesi di stampa è probabile un peso maggiore dell'**intelligenza artificiale** in senso critico e trasversale; i livelli ★ del quinto anno (e alcuni del primo) già la anticipano.

---

## 3. Modello di livello

### 3.1 Struttura di un livello

Ogni livello ha tre strati:

1. **Nucleo**, obbligatorio. Contiene i concetti e le abilità del livello, presentati in modo autoesplicativo e con una scala di difficoltà interna. Le istanze (numeri, testi, mappe, dati) sono generate proceduralmente.
2. **Soglia minima**, per sbloccare il livello successivo. Criterio proposto: *k* istanze consecutive risolte correttamente al grado di difficoltà "base", con un indice di processo accettabile (nessun salto incoerente dei passaggi, tempi plausibili). Valori indicativi: *k* = 3 per i livelli normali, *k* = 5 per le prove di corte.
3. **Approfondimenti**, facoltativi (le "stanze segrete del castello"). Sono gradi di difficoltà superiori, varianti, collegamenti interdisciplinari ed estensioni oltre programma. Danno ricompense (collezionabili, titoli di corte) ma **non bloccano** il percorso.

Si può sempre tornare a un livello già superato, per ripasso o per completare gli approfondimenti.

### 3.2 Schema dati (proposta, un record per livello)

```yaml
id: "2-17"                 # anno-numero
anno: 2
numero: 17
duca: "Ercole I"
titolo: "Funzioni: definizione, parametri, ritorno"
tipo: normale              # normale | prova_di_corte
aree_IN: [AL]              # aree Indicazioni 2010 (poi anche codici IN 2026)
nodi_mappa: [G1]           # ID di mappa-informatica.md
prerequisiti: ["2-16", "2-9"]
oltre_IN: false            # true = ★
interdisciplinare:
  - materia: matematica
    aggancio: "funzione come corrispondenza input→output"
    tipo: propedeutico     # propedeutico | collegamento | applicazione
ambientazione: "Il fattore ducale delega i conti a un 'ufficiale' che riceve dati e restituisce un risultato"
soglia: {k: 3, difficolta: base}
approfondimenti: ["funzioni con più valori di ritorno", "funzioni come parametri ★"]
generatore: "funzioni_aritmetiche_v1"   # nome del generatore procedurale
```

---

## 4. Cornice narrativa: un duca per anno

Proposta, da armonizzare con il materiale storico di Pietro. **Date e fatti vanno ricontrollati su fonti storiche prima dell'uso.**

| Anno | Duca | Periodo (duca di Ferrara) | Filo conduttore | Metafora informatica dominante |
|---|---|---|---|---|
| 1° | **Borso** | 1471 (duca di Modena e Reggio dal 1452) | Palazzo Schifanoia e il Salone dei Mesi, la Bibbia di Borso, l'amministrazione del ducato | **Registrare e codificare**: l'informazione, la sua rappresentazione e la macchina che la tratta |
| 2° | **Ercole I** | 1471–1505 | L'Addizione Erculea (Biagio Rossetti), il teatro, la *Missa Hercules Dux Ferrariae* di Josquin | **Progettare**: dall'idea al piano eseguibile, cioè algoritmi e programmi |
| 3° | **Alfonso I** | 1505–1534 | La fonderia e l'artiglieria, il Camerino d'alabastro (Bellini, Tiziano), l'*Orlando furioso* (1516) | **Forgiare e rappresentare**: formati, immagini, testo marcato, web |
| 4° | **Ercole II** | 1534–1559 | La corte di Renata di Francia, gli archivi, le Delizie | **Ordinare e modellare**: oggetti, linguaggi, basi di dati |
| 5° | **Alfonso II** | 1559–1597 | Il terremoto del 1570 (Pirro Ligorio), Tasso, i corrieri verso Roma, la devoluzione del 1598 | **Simulare, comunicare, conoscere i limiti**: calcolo numerico, simulazione, reti, teoria della computazione |

Agganci ricorrenti:

- la *Missa Hercules Dux Ferrariae* usa un "soggetto cavato" dalle vocali del nome del duca: è un esempio storico di **codifica** (livello 1-9);
- la fonderia di Alfonso I rende intuitiva la coppia **stampo/pezzo = classe/oggetto**, ripresa al 4° anno;
- la genealogia estense è l'esempio naturale per l'**ereditarietà** (livello 4-5) e per gli **alberi**.

---

## 5. Elenco dei livelli

Colonne: n · titolo · area IN · nodi mappa · aggancio interdisciplinare (M = matematica, F = fisica, S = scienze naturali, I = italiano, St = storia, Fil = filosofia, A = disegno e storia dell'arte, EC = educazione civica, Mu = musica).

### 5.1 Primo anno — Borso: "Il duca che registra tutto"

| n | Titolo | IN | Mappa | Interdisciplinare |
|---|---|---|---|---|
| 1 | Informazione, dato, messaggio: le lettere del duca | AC | B1 | I (comunicazione) |
| 2 | Analogico e digitale: meridiana e clessidra | AC | B1 | F (misura) |
| 3 | Il bit: il duca risponde sì o no ★ (quantità d'informazione) | AC | B1, B3, A8.1★ | M |
| 4 | Sistemi posizionali: numeri romani e cifre arabe nei registri | AC | B2.1 | St (Fibonacci, abaco), M |
| 5 | Conversioni binario ↔ decimale | AC | B2.1 | M (potenze) |
| 6 | Ottale ed esadecimale | AC | B2.2 | M |
| 7 | Unità di misura: bit, byte, prefissi SI e IEC | AC | B3 | F (prefissi SI) |
| 8 | Aritmetica binaria e overflow | AC | B2.3 | M |
| 9 | Codificare il testo: ASCII e il "soggetto cavato" di Josquin | AC | B4 | Mu, I |
| 10 | **Prova di corte**: il messaggio cifrato del duca (codifiche + cifrario di Cesare ★) | AC | B2, B4, N2★ | St |
| 11 | Unicode e UTF-8: le lingue della corte | AC | B4 | lingue straniere |
| 12 | Colori: RGB e notazione esadecimale (i colori del Salone dei Mesi) | AC | B5.2, B5.3 | A, F (luce) |
| 13 | Immagini raster: pixel e risoluzione (le miniature della Bibbia di Borso) | AC | B6 | A |
| 14 | Hardware e software | AC | D4 | — |
| 15 | La macchina di von Neumann: CPU, memoria, bus | AC | D4, D5 | St (von Neumann) |
| 16 | Il ciclo fetch-decode-execute: il segretario del duca | AC | D5 | — |
| 17 | Memorie: RAM, dischi, SSD, gerarchia | AC | C10, D8 | F |
| 18 | Periferiche e bus | AC | C11, D9 | — |
| 19 | Porte logiche e algebra di Boole ★ | AC | A2.1, D1 | M (logica) |
| 20 | **Prova di corte**: assemblare il calcolatore del ducato (scelta dei componenti e prestazioni) | AC | C, D | F |
| 21 | Il sistema operativo: a che cosa serve, i sistemi più comuni | SO | I1, I7, I8 | — |
| 22 | Processi e scheduling: le udienze del duca | SO | I2 | — |
| 23 | Gestione della memoria | SO | I4 | — |
| 24 | File system: cartelle, percorsi, permessi, backup | SO | I5, I11 | — |
| 25 | Il documento elettronico: struttura e stili | DE | B13 | I |
| 26 | Foglio elettronico: celle, formule, riferimenti relativi e assoluti | DE | L2 | M |
| 27 | Foglio elettronico: funzioni, grafici, statistica descrittiva (il Salone dei Mesi come tabella 12×3) | DE | L2, A7.1 | M (statistica), S (dati di laboratorio) |
| 28 | Internet: struttura e servizi | IS | J8, K1 | St (ARPANET) |
| 29 | Cercare e valutare le fonti; regole e sicurezza in rete; IA come fonte ★ | IS | U7, N9, O6★ | I, St, EC |
| 30 | **Prova finale di Borso**: l'inventario del ducato (foglio elettronico + codifiche + hardware) | AC, DE, SO | — | M |

### 5.2 Secondo anno — Ercole I: "Progettare la città"

| n | Titolo | IN | Mappa | Interdisciplinare |
|---|---|---|---|---|
| 1 | Pensiero computazionale: scomporre il progetto dell'Addizione | AL | E1 | St (urbanistica) |
| 2 | Che cos'è un algoritmo: le istruzioni per Biagio Rossetti | AL | E1 | I (testo regolativo) |
| 3 | Diagrammi di flusso | AL | E2 | — |
| 4 | Pseudocodice | AL | E2 | — |
| 5 | Sequenza, selezione, iterazione (Böhm-Jacopini) | AL | E3 | M (logica) |
| 6 | Variabili, tipi, assegnazione | AL | E4, G1 | M (variabile algebrica ≠ variabile informatica) |
| 7 | Espressioni e operatori logici | AL | E4, A2.1 | M |
| 8 | Tipologie di linguaggi: livelli, compilati e interpretati, breve storia | AL | G7.3, G9 | St |
| 9 | Il primo linguaggio (Python): input, output, sintassi | AL | G2.2 | — |
| 10 | **Prova di corte**: seguire le strade (tracing di programmi) | AL | E3, G1 | — |
| 11 | Selezione: if, elif, else | AL | G1 | — |
| 12 | Iterazione: while, contatori, accumulatori | AL | G1 | M |
| 13 | Iterazione: for e range | AL | G1 | — |
| 14 | Cicli annidati: la griglia dell'Addizione | AL | G1 | M (piano cartesiano) |
| 15 | Algoritmi classici: massimo, minimo, somma, media | AL | E7 | M |
| 16 | Euclide e i numeri primi | AL | A1.3 | M |
| 17 | Funzioni: definizione, parametri, valore di ritorno | AL | G1 | M (funzione) |
| 18 | Visibilità e scomposizione in funzioni | AL | G1 | — |
| 19 | Test e debugging | AL | H6 | — |
| 20 | **Prova di corte**: le gabelle del ducato (problemi con funzioni) | AL | G1, E7 | M |
| 21 | Liste e array | AL | E6.1 | — |
| 22 | Ricerca lineare | AL | E7.1 | — |
| 23 | Stringhe e testo | AL | B4, E6.1 | I |
| 24 | Cifrari di Cesare e di Vigenère in codice ★ | AL | N2 | St, lingue |
| 25 | Grafica con la tartaruga: geometria del piano di Rossetti | AL | Q1★ | M (geometria), A |
| 26 | Il caso: dadi, frequenze, probabilità simulate ★ | AL | A7.2, S1 | M (probabilità) |
| 27 | Foglio elettronico avanzato: SE, CERCA, tabelle pivot | DE | L2 | S, F (laboratorio) |
| 28 | Come è fatta Internet: indirizzi, DNS, pacchetti | IS | J2, J5, J7 | — |
| 29 | Collaborare in rete: cloud, posta elettronica, privacy, diritto d'autore | IS | U4, U7 | EC |
| 30 | **Prova finale di Ercole I**: generare la pianta dell'Addizione rispettando i vincoli | AL | E, G1 | St, A, M |

### 5.3 Terzo anno — Alfonso I: "La fonderia e il Camerino"

| n | Titolo | IN | Mappa | Interdisciplinare |
|---|---|---|---|---|
| 1 | Interi con segno e complemento a 2 | AL | B2.4 | M |
| 2 | Virgola mobile (IEEE 754) ed errori di rappresentazione | AL | B2.5 | F (cifre significative) |
| 3 | Array e matrici | AL | E6.1 | M |
| 4 | Ordinamento: selection sort e bubble sort | AL | E7.2 | — |
| 5 | Ordinamento: insertion sort; confronti e scambi | AL | E7.2 | — |
| 6 | Ricerca binaria | AL | E7.1 | M (logaritmi) ★ |
| 7 | Contare i passi: complessità intuitiva | AL | E9 | M (crescita delle funzioni) |
| 8 | Ricorsione | AL | E5 | M (induzione), A (frattali) |
| 9 | Divide et impera: merge sort ★ | AL | E8, E7.2 | — |
| 10 | **Prova di corte**: la fonderia ordina i cannoni | AL | E7, E9 | — |
| 11 | Stringhe avanzate e ricerca di schemi (il lessico del *Furioso*) | AL | E7.4, F1★ | I |
| 12 | File e CSV | AL | B11 | S, F (dati di laboratorio) |
| 13 | Metodologie di programmazione: top-down e modularità | AL | H4 | — |
| 14 | Documentazione, stile, controllo di versione (Git) ★ | AL | H5, H8 | — |
| 15 | Formati di immagine: bitmap e vettoriale (il Camerino d'alabastro) | DE | B6 | A |
| 16 | SVG: la grafica vettoriale come testo | DE | B6, K12 | M (geometria analitica) |
| 17 | Compressione senza perdita: RLE e Huffman | DE | B9.1, A8.2 | M |
| 18 | Compressione con perdita: l'idea di JPEG e MP3 | DE | B9.2 | F (onde) |
| 19 | Audio digitale: campionamento e quantizzazione | DE | B7 | F (suono), Mu |
| 20 | **Prova di corte**: il Camerino restaurato (formati, compressione, qualità) | DE | B6–B9 | A |
| 21 | Font e tipografia digitale (dalle edizioni del *Furioso* ai caratteri digitali) | DE | B13 | St (stampa), I |
| 22 | Linguaggi di markup: il concetto, Markdown | DE | B13 | — |
| 23 | XML: elementi, attributi, buona formazione; codificare un canto del *Furioso* | DE | B11 | I |
| 24 | HTML: struttura e semantica | DE | K2 | — |
| 25 | CSS: selettori, box model, colori | DE | K3 | A |
| 26 | Impaginazione e design responsive | DE | K3 | A |
| 27 | Progettazione web: usabilità e accessibilità | DE | K5, Q8 | EC (inclusione) |
| 28 | JavaScript di base: la pagina che reagisce ★ | DE | K4 | — |
| 29 | Pubblicare un sito; licenze e diritto d'autore | DE | K8, U4 | EC |
| 30 | **Prova finale di Alfonso I**: il sito della corte (testi marcati, immagini ottimizzate, stile) | DE, AL | K, B | I, A, St |

### 5.4 Quarto anno — Ercole II: "Gli archivi e la corte"

| n | Titolo | IN | Mappa | Interdisciplinare |
|---|---|---|---|---|
| 1 | Astrazione: dal problema al modello | AL | E1, H3 | Fil |
| 2 | Classi e oggetti: lo stampo e il pezzo | AL | G3.2 | — |
| 3 | Attributi, metodi, costruttori | AL | G3.2 | — |
| 4 | Incapsulamento | AL | G3.2 | — |
| 5 | Ereditarietà: la genealogia estense | AL | G3.2 | St |
| 6 | Polimorfismo e interfacce | AL | G3.2 | — |
| 7 | Diagramma UML delle classi | AL | H3 | — |
| 8 | Pile e code: l'anticamera delle udienze | AL | E6.3 | — |
| 9 | Liste collegate e riferimenti ★ | AL | E6.2, G4 | — |
| 10 | **Prova di corte**: modellare la corte come sistema a oggetti | AL | G3.2, H3 | St |
| 11 | Implementare un linguaggio: compilatore e interprete | AL | G7.3 | — |
| 12 | Analisi lessicale: i token | AL | G7.1, F1 | I (lessico) |
| 13 | Grammatiche e sintassi (BNF) | AL | F2, G7.1 | I (analisi logica), lingue |
| 14 | Alberi sintattici e valutazione delle espressioni | AL | E6.4, G7 | M |
| 15 | Un mini-interprete: la calcolatrice del duca ★ | AL | G7 | — |
| 16 | Dato, informazione, archivio: dall'Archivio estense ai database | BD | L1 | St |
| 17 | Modello E/R: entità, attributi, relazioni | BD | L3 | — |
| 18 | Cardinalità e vincoli | BD | L3 | M |
| 19 | Modello relazionale: tabelle e chiavi | BD | L4 | M (insiemi, relazioni) |
| 20 | **Prova di corte**: progettare l'archivio di Renata (schema E/R) | BD | L3 | St |
| 21 | Dallo schema E/R allo schema relazionale | BD | L4 | — |
| 22 | Normalizzazione (fino alla 3FN) ★ | BD | L4 | — |
| 23 | Algebra relazionale: selezione, proiezione, join | BD | L4 | M (insiemi, logica) |
| 24 | SQL: SELECT, WHERE, ORDER BY | BD | L5 | — |
| 25 | SQL: JOIN | BD | L5 | — |
| 26 | SQL: aggregazioni e GROUP BY | BD | L5 | M (statistica) |
| 27 | SQL: creare e modificare (DDL e DML) | BD | L5 | — |
| 28 | Database e programmi: SQL da Python ★ | BD, AL | L5, G | — |
| 29 | Privacy, GDPR, open data | BD | U4, L10 | EC |
| 30 | **Prova finale di Ercole II**: il catasto delle Delizie (database + applicazione a oggetti) | BD, AL | L, G3.2 | St, S (territorio) |

### 5.5 Quinto anno — Alfonso II: "Il terremoto, i corrieri, i limiti"

| n | Titolo | IN | Mappa | Interdisciplinare |
|---|---|---|---|---|
| 1 | Errori numerici e approssimazione | CS | A10.1, B2.5 | F (misura), M |
| 2 | Zeri di funzione: il metodo di bisezione | CS | A10.2 | M (analisi) |
| 3 | Il metodo di Newton ★ | CS | A10.2 | M (derivate) |
| 4 | Aree sotto una curva: rettangoli e trapezi | CS | A10.2 | M (integrali) |
| 5 | Stimare π con il metodo Monte Carlo | CS | S1, A7 | M (probabilità) |
| 6 | Successioni e ricorrenze: approssimare √2 | CS | A4.2 | M |
| 7 | Simulazione a tempo discreto: il moto (metodo di Eulero) | CS | S1, A6.4 | F (cinematica e dinamica) |
| 8 | Oscillatori e attrito | CS | S1 | F |
| 9 | Modelli di popolazione e di epidemia | CS | S1, S14 | S (biologia) |
| 10 | **Prova di corte**: il terremoto del 1570 (simulazione e confronto con le fonti) | CS | S1 | S (scienze della Terra), F (onde), St |
| 11 | Confrontare un modello con i dati: minimi quadrati | CS | A7.4, O4.1★ | F (laboratorio), M |
| 12 | Automi a stati finiti: la porta del castello | CS | F1 | — |
| 13 | La macchina di Turing | CS | F3 | Fil, St |
| 14 | Calcolabilità: il problema della fermata | CS | F4 | Fil, M (Gödel ★) |
| 15 | Complessità: P e NP spiegati in modo intuitivo | CS | F5 | M |
| 16 | Reti: tipi, topologie, commutazione (i corrieri Ferrara–Roma) | RC | J2 | St |
| 17 | Modelli a strati: ISO/OSI e TCP/IP | RC | J3 | — |
| 18 | Livello fisico e di collegamento: Ethernet, Wi-Fi, errori | RC | J4, B10 | F (elettromagnetismo) |
| 19 | Indirizzi IP e subnetting | RC | J5 | M (binario) |
| 20 | **Prova di corte**: progettare la rete del palazzo (componenti, configurazione, prestazioni) | RC | J2–J5 | — |
| 21 | Instradamento e grafi: l'algoritmo di Dijkstra | RC | J5, E7.3 | M (grafi) |
| 22 | TCP, UDP e porte | RC | J6 | — |
| 23 | Servizi di rete: DNS, HTTP, posta elettronica | IS | J7 | — |
| 24 | Sicurezza in rete: crittografia asimmetrica e HTTPS | IS | N3, N4 | M (aritmetica modulare) |
| 25 | Prestazioni: banda, latenza, throughput; mantenere l'efficienza | RC | I12 | F |
| 26 | Intelligenza artificiale: imparare dai dati ★ | CS | O4 | Fil, M |
| 27 | Reti neurali spiegate in modo intuitivo ★ | CS | O5 | S (neuroni) |
| 28 | IA generativa: limiti, etica, AI Act ★ | CS | O6, O10, U3 | Fil, EC, I |
| 29 | L'informatica e il metodo scientifico: la nascita di nuove scienze | CS | S, U2 | Fil, St della scienza, I |
| 30 | **Prova finale di Alfonso II**: la devoluzione, cioè un progetto di simulazione scientifica completo legato a fisica o scienze | CS | S1 | F, S |

---

## 6. Verifica di copertura (Indicazioni 2010 → livelli)

| Voce delle Indicazioni | Livelli |
|---|---|
| Hardware e software | 1-14 |
| Codifica binaria, ASCII, Unicode | 1-4…1-11 |
| Von Neumann: CPU, memoria, dischi, bus, periferiche | 1-15…1-18, 1-20 |
| Sistema operativo, sistemi comuni, processi, memoria, file system | 1-21…1-24 |
| Documento elettronico, foglio elettronico | 1-25…1-27, 2-27 |
| Struttura e servizi di Internet, ricerca, regole d'uso | 1-28, 1-29, 2-28, 2-29 |
| Principi e tipologie di linguaggi, algoritmo, pseudocodice, sintassi di un linguaggio | 2-1…2-23 |
| Documenti avanzati, markup (XML), formati non testuali, compressione, font, progettazione web | 3-15…3-29 |
| Modello relazionale, linguaggi di interrogazione e manipolazione | 4-16…4-29 |
| Implementazione di un linguaggio | 4-11…4-15 |
| Metodologie di programmazione | 3-13, 3-14, 4-1, 4-7 |
| Linguaggio orientato agli oggetti | 4-2…4-10 |
| Algoritmi del calcolo numerico | 5-1…5-6 |
| Principi teorici della computazione | 5-12…5-15 |
| Reti, protocolli, struttura di Internet e servizi | 5-16…5-25 |
| Simulazioni a supporto della ricerca scientifica (modello contro dati) | 5-7…5-11, 5-30 |
| Linee generali: scelta dei componenti, prestazioni, efficienza | 1-20, 5-20, 5-25 |
| Linee generali: collegamenti con filosofia e italiano, nascita di nuove scienze | 4-13, 5-13, 5-14, 5-28, 5-29 |

Ogni voce delle Indicazioni 2010 ha almeno un livello. Livelli oltre le Indicazioni (★): 1-3, 1-10, 1-19, 1-29, 2-24…2-26, 3-6, 3-9, 3-11, 3-14, 3-28, 4-9, 4-15, 4-22, 4-28, 5-3, 5-11, 5-14, 5-26…5-28.

---

## 7. Questioni aperte

1. **Materiale sui duchi.** È da integrare il materiale di Pietro (chat "2B" e "informatica knowledge tree"). La cornice del §4 è una proposta sostituibile.
2. **Nuove Indicazioni 2026.** Serve acquisire il fascicolo `LS-SCIENZE-APPLICATE` (sezione Informatica) e rifare il §6. Serve anche decidere se il gioco segue le Indicazioni 2010, quelle 2026 o entrambe (per esempio le prime fino alle coorti che iniziano nel 2026/27, poi le nuove).
3. **Linguaggio di programmazione.** Python è previsto per tutti gli anni. Va deciso se introdurre un secondo linguaggio tipizzato (C++ o Java) al 3° o 4° anno, per la programmazione a oggetti e i tipi.
4. **Rapporto con la piattaforma gamificata.** Il gioco può essere un modulo della piattaforma, con gli stessi requisiti (privacy, Classroom, punteggio sul processo), oppure un prodotto a sé.
5. **Allineamento interdisciplinare.** I collegamenti con matematica, fisica e scienze vanno verificati sulle programmazioni reali di classe. In particolare vanno controllati la tempistica di analisi, probabilità e onde nel quarto e quinto anno e lo sfasamento tra i livelli che richiedono un prerequisito matematico e il momento in cui quel prerequisito viene insegnato.
6. **Granularità.** Ogni livello deve durare da 5 minuti a qualche ora. Va stimata la durata media per anno e confrontata con le ore curricolari (2 ore settimanali, circa 66 ore annue).
7. **Fonti storiche.** Date e fatti del §4 vanno verificati su fonti storiche prima dell'uso nel gioco.

---

## 8. Fonti

- Indicazioni nazionali per i licei, DPR 89/2010, sezione "Liceo scientifico opzione scienze applicate — Informatica" (PDF caricato da Pietro).
- Ministero dell'Istruzione e del Merito, pubblicazione della bozza delle nuove Indicazioni nazionali per i licei, 22/04/2026: <https://www.mim.gov.it/-/pubblicato-il-testo-delle-nuove-indicazioni-nazionali-per-i-licei->
- Fascicolo della bozza per le scienze applicate (non ancora letto integralmente): <https://www.orizzontescuola.it/wp-content/uploads/2026/04/LS-SCIENZE-APPLICATE.pdf>
- Calendario di entrata in vigore (fonte di stampa): <https://edunews24.it/scuola/scuola-e-attualit-come-cambieranno-i-programmi-dei-licei-dal-2027>
- `mappa-informatica.md` v0.3 (progetto Scuola).
