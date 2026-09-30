# Mappa dell'informatica — alberatura propedeutica

**Versione:** 0.5 (aree dettagliate + nodi di approfondimento per il videogioco) · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Stato:** alberatura di primo livello, confrontata con ACM CCS 2012, ACM/IEEE/AAAI CS2023, SWEBOK v4, categorie arXiv cs e proposta CINI (vedi §Verifica di copertura). I prerequisiti sono indicati solo per i collegamenti principali. Il grafo completo delle propedeuticità si farà in una fase successiva.

---

## 0. Scopo e convenzioni

**Scopo.** Mappare l'intero dominio dell'informatica (con le discipline confinanti: matematica, fisica/elettronica, linguistica, biologia, società) in una struttura che mostri **che cosa serve sapere prima di che cosa**. L'obiettivo finale è un grafo orientato aciclico (DAG) delle propedeuticità, da usare per:
- progettazione didattica (curricoli per indirizzo e anno);
- *skill tree* di una piattaforma gamificata;
- orientamento (mostrare dove porta ogni argomento).

**Perché un grafo e non un albero.** Molti nodi hanno più prerequisiti che provengono da rami diversi. Per esempio, la linguistica computazionale dipende da informatica teorica, probabilità e IA. L'albero qui sotto è quindi solo uno **scheletro tassonomico**: organizza i nodi per area. Le frecce `⟵` sono i "fili" che poi diventeranno gli archi del grafo.

**Struttura documentale.** Questo è il documento madre: contiene l'alberatura generale, le convenzioni e la verifica di copertura. Ogni area, una volta dettagliata, ha un proprio file `mappa-informatica-<lettera>.md`, con un nodo per riga e tutti i prerequisiti diretti. Il formato è descritto nel file dell'area A.

**Convenzioni.**
- **ID stabili**: lettera dell'area + numeri (es. `B5`, `G3.3`). Gli ID già assegnati non si rinumerano; i nuovi nodi si aggiungono in coda al ramo.
- **Ordine interno**: all'interno di un ramo, l'ordine dall'alto in basso è già indicativamente propedeutico, salvo diversa indicazione.
- `⟵ X` = "richiede X" (prerequisito, di solito da un altro ramo).
- `⟶ Y` = "sblocca / prepara Y" (è indicato solo quando il collegamento non è evidente).
- **Livello indicativo** (tra parentesi quadre):
  - `[1]` primo biennio / alfabetizzazione;
  - `[2]` triennio superiore;
  - `[3]` università (triennale);
  - `[4]` specialistico / ricerca.

---

## Panoramica delle macro-aree

| ID | Area | Prerequisiti principali di area |
|---|---|---|
| A | Fondamenti matematici e logici | — (radice) |
| B | Informazione e rappresentazione | A |
| C | Fisica, elettronica e tecnologia dell'hardware | A (+ fisica) |
| D | Architettura degli elaboratori | B, C |
| E | Algoritmi e strutture dati | A, B |
| F | Informatica teorica | A, E |
| G | Linguaggi e paradigmi di programmazione | E (+ D per i linguaggi di basso livello) |
| H | Ingegneria del software | G |
| I | Sistemi operativi e software di sistema | D, G |
| J | Reti e telecomunicazioni | B, C, I |
| K | Web e sviluppo di applicazioni | B, G, J |
| L | Dati e basi di dati | A, E, G |
| M | Calcolo parallelo, distribuito, HPC, cloud | C, D, I, J |
| N | Sicurezza informatica e crittografia | A, D, G, I, J |
| O | Intelligenza artificiale | A, E, G, L |
| P | Linguistica computazionale e NLP | F, O, A7 |
| Q | Grafica, multimedia, visione, interazione | A5, B, D, O |
| R | Robotica, automazione, embedded, IoT | C, D, G, A6 |
| S | Informatica applicata alle scienze (bioinformatica/informatica genetica…) | E, L, O + discipline |
| T | Calcolo quantistico e paradigmi non convenzionali | A5, A7, C15, D, F5 |
| U | Storia, società, etica, diritto, economia | trasversale |
| V | Sistemi informativi e informatica gestionale | H, L, J |
| W | Didattica dell'informatica (meta-ramo) | trasversale |

---

## A. Fondamenti matematici e logici

> **Dettaglio completo:** `mappa-informatica-A.md` (v1.0, 218 nodi con prerequisiti diretti).

- **A1 Aritmetica e algebra** `[1]`
  - A1.1 Insiemi numerici: naturali, interi, razionali, reali
  - A1.2 Potenze e logaritmi ⟶ B2 (basi), E9 (complessità)
  - A1.3 Divisibilità, MCD (algoritmo di Euclide), numeri primi
  - A1.4 Aritmetica modulare ⟶ E6.5 (hash), N3 (crittografia)
- **A2 Logica** `[1–3]`
  - A2.1 Proposizioni, connettivi, tavole di verità ⟶ D1
  - A2.2 Logica dei predicati, quantificatori ⟶ G3.4, L5, O2
  - A2.3 Tecniche di dimostrazione: diretta, per assurdo, per induzione ⟶ E5
  - A2.4 Sistemi formali, correttezza e completezza `[3]`
  - A2.5 Teoremi di incompletezza di Gödel `[4]`
  - A2.6 Logiche non classiche: modale, temporale (⟶ F9), fuzzy (⟶ O3), intuizionista (⟶ F7)
- **A3 Insiemi, relazioni, funzioni** `[1–2]`
  - A3.1 Insiemi, operazioni, prodotto cartesiano ⟶ L4
  - A3.2 Relazioni: di equivalenza, d'ordine
  - A3.3 Funzioni: iniettive, suriettive, composizione ⟶ F6, G3.3
  - A3.4 Cardinalità, infinito numerabile, diagonalizzazione di Cantor ⟶ F3, F4
- **A4 Matematica discreta** `[2–3]`
  - A4.1 Combinatoria (permutazioni, combinazioni, principio dei cassetti)
  - A4.2 Successioni e ricorrenze ⟶ E9
  - A4.3 Teoria dei grafi: cammini, alberi, connettività, colorazione ⟶ E6.6, E7.3
  - A4.4 Strutture algebriche: gruppi, anelli, campi finiti ⟶ B10, N3
- **A5 Algebra lineare** `[2–3]`
  - A5.1 Vettori, matrici, operazioni
  - A5.2 Trasformazioni lineari ⟶ Q1, R6
  - A5.3 Autovalori e autovettori ⟶ L11 (PageRank), O4.2 (PCA)
  - A5.4 Numeri complessi, spazi di Hilbert, prodotto tensoriale ⟶ T1
- **A6 Analisi** `[2–3]`
  - A6.1 Funzioni, limiti, continuità
  - A6.2 Derivate, gradiente ⟶ O5 (discesa del gradiente)
  - A6.3 Integrali
  - A6.4 Equazioni differenziali ⟶ R4, S1
  - A6.5 Serie e trasformata di Fourier, trasformate discrete ⟶ B7, B9, J1, Q4
- **A7 Probabilità e statistica** `[1–3]`
  - A7.1 Statistica descrittiva `[1]`
  - A7.2 Probabilità, probabilità condizionata, teorema di Bayes
  - A7.3 Variabili aleatorie e distribuzioni
  - A7.4 Inferenza statistica, stime, test
  - A7.5 Processi stocastici, catene di Markov ⟶ P5, O4.4, L11
- **A8 Teoria dell'informazione** `[2–3]` ⟵ A1.2, A7.2
  - A8.1 Entropia di Shannon
  - A8.2 Codifica di sorgente (limite di compressione) ⟶ B9
  - A8.3 Canale rumoroso e capacità ⟶ B10, J1
  - A8.4 Entropia incrociata e divergenza KL ⟶ O4, O5
- **A9 Ottimizzazione e ricerca operativa** `[3]`
  - A9.1 Programmazione lineare e intera
  - A9.2 Ottimizzazione convessa e non convessa ⟶ O5
  - A9.3 Euristiche e metaeuristiche ⟶ O8
- **A10 Analisi numerica** `[3]` ⟵ A6, B2.5
  - A10.1 Errori di arrotondamento e di troncamento, condizionamento
  - A10.2 Metodi iterativi, zeri di funzioni, integrazione numerica
  - A10.3 Algebra lineare numerica ⟶ S1
- **A11 Teoria dei numeri computazionale** `[3]`: test di primalità, fattorizzazione, logaritmo discreto ⟵ A1.3, A1.4 ⟶ N3, T4

---

## B. Informazione e rappresentazione `[1]`

> **Dettaglio completo:** `mappa-informatica-B.md` (v1.0, 132 nodi con prerequisiti diretti).

- **B1 Concetti base**: informazione, dato, segnale; analogico vs digitale; discretizzazione
- **B2 Rappresentazione dei numeri** ⟵ A1
  - B2.1 Sistemi posizionali; conversioni decimale ↔ binario
  - B2.2 Ottale ed esadecimale
  - B2.3 Aritmetica binaria, overflow
  - B2.4 Interi con segno: modulo e segno, complemento a 1, complemento a 2
  - B2.5 Virgola fissa e mobile (IEEE 754), errori di rappresentazione ⟶ A10
  - B2.6 BCD e altre codifiche numeriche
- **B3 Unità di misura**: bit, nibble, byte, word; prefissi SI (kB) e IEC (KiB)
- **B4 Codifica del testo**: ASCII, code page, Unicode, UTF-8/UTF-16, emoji, normalizzazione ⟶ K2, P3
- **B5 Codifica dei colori**
  - B5.1 Percezione del colore, sintesi additiva e sottrattiva
  - B5.2 Modelli RGB, CMYK, HSV/HSL
  - B5.3 Profondità di colore, palette, notazione esadecimale `#RRGGBB` ⟵ B2.2 ⟶ K3
  - B5.4 Spazi colore (sRGB, P3), correzione gamma `[2]`
- **B6 Immagini**: raster (pixel, risoluzione, DPI) vs vettoriale; formati BMP, PNG, JPEG, GIF, SVG
- **B7 Audio**: campionamento, teorema di Nyquist-Shannon (⟵ A6.5), quantizzazione, formati (WAV, MP3), MIDI
- **B8 Video**: fotogrammi, frame rate, codec e container
- **B9 Compressione** ⟵ A8.2
  - B9.1 Senza perdita: RLE, Huffman, LZ77/LZW
  - B9.2 Con perdita: DCT, JPEG, MP3 ⟵ A6.5
- **B10 Rilevazione e correzione degli errori** ⟵ A4.4, A8.3
  - B10.1 Bit di parità, checksum
  - B10.2 CRC
  - B10.3 Codici di Hamming, Reed-Solomon ⟶ J4, T7
- **B11 Dati strutturati**: formati testuali (CSV, JSON, XML, YAML) e binari; serializzazione; metadati ⟶ L
- **B12 Codici identificativi**: codici a barre, QR code, ISBN/IBAN (cifre di controllo) ⟵ A1.4
- **B13 Documenti digitali e tipografia digitale**: font e rendering del testo, formati (PDF, DOCX, ODF), linguaggi di markup (Markdown, LaTeX) ⟵ B4 ⟶ K2

---

## C. Fisica, elettronica e tecnologia dell'hardware

> **Dettaglio completo:** `mappa-informatica-C.md` (v1.0, 100 nodi con prerequisiti diretti).

- **C1 Elettricità di base** `[1–2]`: carica, corrente, tensione, resistenza; legge di Ohm, potenza, leggi di Kirchhoff
- **C2 Componenti passivi**: resistori, condensatori, induttori; circuiti RC (temporizzazione)
- **C3 Semiconduttori**: bande di energia, drogaggio, giunzione PN, diodo, LED
- **C4 Transistor**: BJT, MOSFET; il transistor come interruttore
- **C5 Logica CMOS**: realizzazione delle porte logiche con i transistor ⟵ D1 ⟶ D2
- **C6 Elettronica analogica**: amplificatori operazionali, filtri
- **C7 Conversione AD/DA**: ADC, DAC ⟵ B7 ⟶ R2
- **C8 Circuiti integrati e fabbricazione**: wafer di silicio, fotolitografia, nodi di processo (nm), fonderie; geopolitica dei chip (⟶ U5)
- **C9 Legge di Moore e scaling**
  - C9.1 Enunciato e storia (Moore 1965, revisione 1975)
  - C9.2 Scaling di Dennard e sua fine (~2005): *power wall*
  - C9.3 Conseguenze: multicore, acceleratori specializzati ⟶ D11, D12, M1
  - C9.4 Oltre Moore: 3D stacking, chiplet, nuovi materiali, "More than Moore" ⟶ T10
- **C10 Tecnologie di memoria**: SRAM, DRAM, flash, dischi magnetici, SSD, supporti ottici ⟶ D8
- **C11 Periferiche e interfacce**: bus, USB, display, tastiere, sensori
- **C12 Logica programmabile**: PLD, FPGA; linguaggi HDL (VHDL, Verilog) ⟵ D2, D3
- **C13 Energia e calore**: consumo, dissipazione, efficienza energetica ⟶ U6
- **C14 Mezzi di trasmissione fisica**: segnali elettrici, fibra ottica, onde radio, antenne ⟶ J1
- **C15 Fisica quantistica di base**: quantizzazione, effetto tunnel (limite alla miniaturizzazione), postulati ⟶ T1
- **C16 Progettazione di sistemi digitali ed EDA** `[3–4]`: progettazione VLSI, sintesi logica, simulazione, verifica e collaudo dell'hardware ⟵ C12, F9
- **C17 Affidabilità dell'hardware**: guasti, invecchiamento, errori transitori (soft error), ridondanza e tolleranza ai guasti ⟵ B10
- **C18 Tecnologie emergenti di dispositivo**: memristori, spintronica, calcolo in memoria (in-memory computing), elettronica flessibile ⟵ C9.4 ⟶ T10

---

## D. Architettura degli elaboratori

> **Dettaglio completo:** `mappa-informatica-D.md` (v1.0, 89 nodi con prerequisiti diretti).

- **D1 Algebra di Boole** ⟵ A2.1: operatori, proprietà, leggi di De Morgan, forme canoniche, mappe di Karnaugh
- **D2 Reti logiche combinatorie**: porte, multiplexer, decoder, sommatori, ALU ⟵ B2.3
- **D3 Reti logiche sequenziali**: latch, flip-flop, registri, contatori; macchine a stati ⟵ F1
- **D4 Modelli di macchina**: von Neumann e Harvard
- **D5 CPU**: registri, ALU, unità di controllo, clock; ciclo fetch-decode-execute
- **D6 ISA (Instruction Set Architecture)**: linguaggio macchina, formati delle istruzioni, modi di indirizzamento; CISC vs RISC; x86, ARM, RISC-V
- **D7 Assembly** ⟶ G5.1
- **D8 Gerarchia di memoria**: registri, cache (località), RAM, memoria di massa ⟵ C10 ⟶ I4, G4
- **D9 Input/Output**: polling, interrupt, DMA, bus ⟶ I1
- **D10 Prestazioni**: pipeline, hazard, esecuzione superscalare e fuori ordine, predizione dei salti, esecuzione speculativa ⟶ N8
- **D11 Parallelismo hardware**: multicore, SIMD, GPU ⟵ C9.3 ⟶ M2, Q2
- **D12 Architetture specializzate**: DSP, TPU/NPU, acceleratori per l'IA ⟶ O9
- **D13 Microcontrollori vs microprocessori, SoC** ⟶ R2

---

## E. Algoritmi e strutture dati

> **Dettaglio completo:** `mappa-informatica-E.md` (v1.0, 138 nodi con prerequisiti diretti).

- **E1 Pensiero computazionale** `[1]`: scomposizione, riconoscimento di schemi, astrazione, algoritmo; attività unplugged
- **E2 Rappresentazione degli algoritmi**: linguaggio naturale, diagrammi di flusso, pseudocodice, blocchi
- **E3 Costrutti di controllo**: sequenza, selezione, iterazione; teorema di Böhm-Jacopini
- **E4 Variabili, tipi, espressioni** ⟵ B2, B4
- **E5 Ricorsione** ⟵ A2.3
- **E6 Strutture dati**
  - E6.1 Array e matrici
  - E6.2 Liste collegate ⟵ G4 (puntatori, se implementate a basso livello)
  - E6.3 Pile, code, deque
  - E6.4 Alberi: binari, BST, bilanciati (AVL, rosso-neri), heap, trie, B-tree ⟶ L6
  - E6.5 Tabelle hash ⟵ A1.4
  - E6.6 Grafi: liste e matrici di adiacenza ⟵ A4.3
  - E6.7 Strutture probabilistiche (filtri di Bloom) ⟵ A7
- **E7 Algoritmi fondamentali**
  - E7.1 Ricerca lineare e binaria
  - E7.2 Ordinamento: selection, bubble, insertion, merge, quick, heap, counting/radix
  - E7.3 Algoritmi sui grafi: BFS, DFS, Dijkstra, Bellman-Ford, alberi ricoprenti minimi, flussi ⟶ J5, O2, R6
  - E7.4 Algoritmi su stringhe: pattern matching (KMP), distanza di edit ⟶ P3, S2.4
  - E7.5 Algoritmi numerici e geometrici
- **E8 Tecniche di progetto**: forza bruta, divide et impera, greedy, programmazione dinamica, backtracking, branch and bound
- **E9 Analisi degli algoritmi**: correttezza (invarianti), complessità temporale e spaziale, notazioni O/Ω/Θ, caso medio, analisi ammortizzata ⟵ A1.2, A4.2 ⟶ F5
- **E10 Algoritmi randomizzati, approssimati, online e di streaming** `[3–4]` ⟵ A7
- **E11 Algoritmi paralleli e distribuiti** `[3–4]` ⟶ M2, M3
- **E12 Geometria computazionale** `[3]`: inviluppo convesso, triangolazioni, diagrammi di Voronoi, intersezioni ⟵ A5 ⟶ Q2, R6.3, S6

---

## F. Informatica teorica `[3–4]`

> **Dettaglio completo:** `mappa-informatica-F.md` (v1.0, 93 nodi con prerequisiti diretti).

- **F1 Automi a stati finiti, espressioni regolari, linguaggi regolari** (`[2]` a livello intuitivo) ⟶ D3, G7, P3
- **F2 Grammatiche formali e gerarchia di Chomsky**; automi a pila, linguaggi liberi dal contesto ⟶ G7, P2, P6
- **F3 Macchina di Turing; tesi di Church-Turing** ⟵ A3.4
- **F4 Calcolabilità**: problemi indecidibili, problema della fermata, riduzioni ⟵ A3.4
- **F5 Complessità computazionale**: P, NP, NP-completezza, il problema P vs NP, PSPACE, classi probabilistiche (BPP) ⟵ E9 ⟶ N3, T5
- **F6 Lambda calcolo** ⟵ A3.3 ⟶ G3.3
- **F7 Teoria dei tipi, corrispondenza di Curry-Howard** ⟵ A2.6 ⟶ G6
- **F8 Semantica dei linguaggi**: operazionale, denotazionale, assiomatica (logica di Hoare)
- **F9 Metodi formali e verifica**: model checking (⟵ A2.6), dimostratori interattivi (Coq, Lean)
- **F10 Teoria algoritmica dell'informazione** (complessità di Kolmogorov) ⟵ A8
- **F11 Crittografia teorica e teoria dei giochi algoritmica** (equilibri, mechanism design, aste) ⟶ N3, O12, V
- **F12 Teoria dell'apprendimento computazionale** (apprendimento PAC, dimensione VC) ⟵ A7, F5 ⟶ O4
- **F13 Modelli formali della concorrenza**: reti di Petri, algebre di processi (CSP, CCS, π-calcolo) ⟵ F1 ⟶ M3
- **F14 Soddisfacibilità e vincoli**: problema SAT, solver SAT/SMT, problemi di soddisfacimento di vincoli ⟵ A2.1, F5 ⟶ F9, O2.5

---

## G. Linguaggi e paradigmi di programmazione

> **Dettaglio completo:** `mappa-informatica-G.md` (v1.0, 185 nodi con prerequisiti diretti).

- **G1 Concetti base** ⟵ E3, E4: variabili, tipi, input/output, operatori, funzioni, parametri, visibilità (scope)
- **G2 Primo linguaggio**
  - G2.1 Linguaggi visuali a blocchi (Scratch, Blockly) `[1]`
  - G2.2 Python `[1–2]`
- **G3 Paradigmi**
  - G3.1 Imperativo/procedurale
  - G3.2 Orientato agli oggetti: classi, incapsulamento, ereditarietà, polimorfismo, interfacce ⟶ H3, H4
  - G3.3 Funzionale ⟵ E5, F6: funzioni pure, immutabilità, funzioni di ordine superiore, closure, map/filter/reduce, valutazione lazy, tipi algebrici, monadi `[3]`; Haskell, Lisp/Scheme, OCaml, Elixir
  - G3.4 Logico: Prolog ⟵ A2.2
  - G3.5 Dichiarativo: SQL, HTML, linguaggi di configurazione
  - G3.6 A eventi e reattivo ⟶ K4
  - G3.7 Concorrente: thread, attori, async/await ⟵ I3
  - G3.8 Array e dataflow (NumPy, APL)
- **G4 Gestione della memoria** ⟵ D8: stack e heap, puntatori, allocazione manuale, garbage collection, ownership e borrowing
- **G5 Linguaggi (per famiglia)**
  - G5.1 C ⟵ G4, D7
  - G5.2 C++
  - G5.3 Rust ⟵ G4, G3.3 (tipi algebrici) — sistema di ownership e borrowing
  - G5.4 Java, C#
  - G5.5 JavaScript e TypeScript ⟶ K4
  - G5.6 Go
  - G5.7 Shell e scripting (Bash, PowerShell) ⟵ I7
  - G5.8 Linguaggi scientifici: R, Julia, MATLAB ⟶ S
  - G5.9 Linguaggi di descrizione hardware ⟶ C12
  - G5.10 Linguaggi e framework quantistici ⟶ T8
- **G6 Sistemi di tipi**: statici/dinamici, forti/deboli, inferenza, generici ⟵ F7
- **G7 Implementazione dei linguaggi** ⟵ F1, F2
  - G7.1 Analisi lessicale e sintattica (parsing)
  - G7.2 Analisi semantica, generazione e ottimizzazione del codice
  - G7.3 Interpreti, compilatori, JIT, bytecode e macchine virtuali
  - G7.4 Linker e loader ⟵ I
- **G8 Metaprogrammazione e DSL**
- **G10 Altri paradigmi e strumenti**: programmazione probabilistica (⟵ A7), low-code/no-code, programmazione di fogli di calcolo (⟵ L2), programmazione in linguaggio naturale (⟵ O6)
- **G9 Storia ed evoluzione dei linguaggi** (Fortran, COBOL, Lisp, ALGOL, Pascal, C, Smalltalk…) ⟶ U1

---

## H. Ingegneria del software `[2–3]`

> **Dettaglio completo:** `mappa-informatica-H.md` (v1.0, 110 nodi con prerequisiti diretti).

- **H1 Ciclo di vita del software**: requisiti, analisi, progettazione, sviluppo, test, rilascio, manutenzione
- **H2 Modelli di processo**: a cascata, iterativo, agile (Scrum, Kanban), DevOps
- **H3 Modellazione**: UML (casi d'uso, classi, sequenza, stati), diagrammi E/R ⟶ L3
- **H4 Progettazione**: modularità, coesione e accoppiamento, principi SOLID, design pattern; architetture (MVC, a strati, microservizi)
- **H5 Controllo di versione**: Git, branching, GitHub, collaborazione open source
- **H6 Qualità**: testing (di unità, integrazione, sistema; TDD), debugging, code review, analisi statica, refactoring
- **H7 Build e rilascio**: gestione delle dipendenze, CI/CD, container ⟵ I9
- **H8 Documentazione, stile, leggibilità; licenze software** ⟶ U4
- **H9 Gestione di progetto**: stime, pianificazione, gestione del rischio
- **H10 Sviluppo assistito dall'IA** ⟵ O6
- **H11 Ingegneria dei requisiti**: raccolta, analisi, specifica, validazione; requisiti funzionali e non funzionali
- **H12 Architettura del software**: stili architetturali, trade-off di qualità, documentazione architetturale ⟵ H4
- **H13 Gestione della configurazione e manutenzione**: versioni, rilasci, evoluzione e software legacy, reverse engineering ⟵ H5
- **H14 Operazioni (DevOps/SRE)**: monitoraggio, osservabilità, gestione degli incidenti ⟵ H7, I12
- **H15 Misura e qualità del software**: metriche, modelli di qualità (ISO/IEC 25010), processi di miglioramento ⟵ A7
- **H16 Economia del software**: costi, stime, valore, debito tecnico
- **H17 Sicurezza nel ciclo di vita del software** (DevSecOps) ⟵ N6
- **H18 Pratica professionale**: lavoro in team, comunicazione tecnica, standard e certificazioni ⟶ U9

---

## I. Sistemi operativi e software di sistema

> **Dettaglio completo:** `mappa-informatica-I.md` (v1.0, 80 nodi con prerequisiti diretti).

- **I1 Ruolo del sistema operativo**: kernel, modalità utente/kernel, chiamate di sistema ⟵ D9
- **I2 Processi e thread; scheduling**
- **I3 Concorrenza e sincronizzazione**: race condition, mutex, semafori, stallo (deadlock) ⟶ G3.7, L6
- **I4 Gestione della memoria**: paginazione, segmentazione, memoria virtuale ⟵ D8
- **I5 File system**: struttura, permessi, journaling
- **I6 I/O e driver**
- **I7 Interfacce utente**: shell/CLI, GUI `[1]`
- **I8 Famiglie di sistemi**: Unix/Linux, Windows, macOS, Android/iOS, sistemi operativi real-time ⟶ R3
- **I9 Virtualizzazione**: hypervisor, macchine virtuali, container (Docker), orchestrazione (Kubernetes) ⟶ M4
- **I10 Avvio e firmware**: BIOS/UEFI, bootloader
- **I11 Amministrazione di sistema**: utenti, pacchetti, backup, log
- **I12 Prestazioni e affidabilità dei sistemi**: metriche (latenza, throughput), benchmarking, teoria delle code (⟵ A7.5), disponibilità e tolleranza ai guasti ⟶ H14, M3

---

## J. Reti e telecomunicazioni

> **Dettaglio completo:** `mappa-informatica-J.md` (v1.0, 86 nodi con prerequisiti diretti).

- **J1 Fondamenti di comunicazione**: segnali, banda, modulazione, multiplexing ⟵ C14, A6.5, A8.3
- **J2 Tipi e topologie di rete**: PAN, LAN, MAN, WAN; commutazione di circuito e di pacchetto
- **J3 Modelli a strati**: ISO/OSI e TCP/IP; incapsulamento
- **J4 Livelli fisico e di collegamento**: Ethernet, indirizzi MAC, switch, Wi-Fi, Bluetooth; controllo degli errori ⟵ B10
- **J5 Livello di rete**: IPv4, IPv6, subnetting (⟵ B2), routing (⟵ E7.3), NAT, ICMP
- **J6 Livello di trasporto**: TCP (affidabilità, controllo di flusso e di congestione), UDP, porte, socket
- **J7 Livello applicativo**: DNS, HTTP/HTTPS, SMTP/IMAP, FTP, SSH, DHCP
- **J8 Internet**: struttura, ISP, BGP; storia (ARPANET) ⟶ U1
- **J9 Reti mobili e wireless**: 4G/5G/6G, reti satellitari
- **J10 Programmazione di rete**: socket, client/server, peer-to-peer ⟵ G
- **J11 Gestione e sicurezza di rete**: firewall, VPN, monitoraggio ⟶ N7
- **J12 Reti moderne**: SDN, CDN, edge ⟶ M6
- **J13 Reti quantistiche** ⟶ T9
- **J14 Standard e governance di Internet**: IETF e RFC, IEEE 802, W3C, ICANN; neutralità della rete ⟶ U4

---

## K. Web e sviluppo di applicazioni

> **Dettaglio completo:** `mappa-informatica-K.md` (v1.0, 84 nodi con prerequisiti diretti).

- **K1 Come funziona il web**: client-server, URL, browser, richieste HTTP ⟵ J7
- **K2 HTML**: struttura, semantica, form ⟵ B4
- **K3 CSS**: selettori, box model, layout (flex, grid), design responsive, colori ⟵ B5
- **K4 JavaScript nel browser**: DOM, eventi, fetch/async ⟵ G3.6, G5.5
- **K5 Accessibilità web (WCAG)** ⟶ Q8
- **K6 Framework front-end** (React, Vue, Svelte…), single page application
- **K7 Back-end**: server, API REST/GraphQL, autenticazione e sessioni ⟵ L5, N5
- **K8 Pubblicazione**: hosting, domini, generatori di siti statici (Hugo), deploy ⟵ H5
- **K9 App mobili**: native e cross-platform
- **K10 Web semantico e linked data** ⟵ L4, O2 (ontologie)
- **K11 Prestazioni, SEO, privacy (cookie, tracciamento)** ⟶ U4
- **K12 Grafica per il web**: SVG, Canvas, WebGL ⟶ Q10

---

## L. Dati e basi di dati

> **Dettaglio completo:** `mappa-informatica-L.md` (v1.0, 109 nodi con prerequisiti diretti).

- **L1 Dato, informazione, conoscenza; ciclo di vita del dato**
- **L2 Fogli di calcolo** `[1]`: formule, riferimenti, grafici ⟶ L9
- **L3 Modellazione concettuale**: modello Entità/Relazioni ⟵ H3
- **L4 Modello relazionale** ⟵ A3.1: tabelle, chiavi, vincoli di integrità, algebra relazionale, normalizzazione
- **L5 SQL**: DDL, DML, interrogazioni, join, aggregazioni, viste ⟵ A2.2
- **L6 DBMS**: transazioni ACID, controllo di concorrenza (⟵ I3), indici (⟵ E6.4), ottimizzazione delle query
- **L7 Basi di dati NoSQL**: documentali, chiave-valore, colonnari, a grafo
- **L8 Data warehouse, OLAP, big data** (Hadoop, Spark) ⟶ M
- **L9 Data science**: pulizia dei dati, analisi esplorativa, visualizzazione ⟵ A7 ⟶ O4, Q9
- **L10 Open data, governance e qualità dei dati** ⟶ U4
- **L11 Information retrieval e motori di ricerca**: indici invertiti, ranking, PageRank ⟵ A5.3, A7.5
- **L12 Sistemi di raccomandazione**: filtraggio collaborativo e basato sui contenuti ⟵ L11, O4
- **L13 Biblioteche digitali, archivi e conservazione digitale**: metadati (Dublin Core), identificatori persistenti (DOI), obsolescenza dei formati ⟵ B11
- **L14 Basi di dati distribuite e ingegneria dei dati**: replica, partizionamento, pipeline ETL, dati semi-strutturati e non strutturati ⟵ L6, M3
- **L15 Sicurezza e privacy dei dati**: controllo accessi ai dati, cifratura, provenienza dei dati ⟵ N3, N11

---

## M. Calcolo parallelo, distribuito e ad alte prestazioni `[3–4]`

> **Dettaglio completo:** `mappa-informatica-M.md` (v1.0, 51 nodi con prerequisiti diretti).

- **M1 Motivazioni e limiti**: fine dello scaling di Dennard (⟵ C9.2), legge di Amdahl, legge di Gustafson
- **M2 Programmazione parallela**: memoria condivisa (thread, OpenMP), scambio di messaggi (MPI), GPU (CUDA) ⟵ D11
- **M3 Sistemi distribuiti**: tempo e orologi logici, consenso (Paxos, Raft), teorema CAP, tolleranza ai guasti ⟵ E11
- **M4 Cloud computing**: IaaS, PaaS, SaaS, serverless ⟵ I9
- **M5 HPC e supercalcolo** (classifica TOP500) ⟶ S1
- **M6 Edge e fog computing** ⟶ R10
- **M7 Blockchain e registri distribuiti** ⟵ N3 (hash, firme), M3 (consenso)
- **M8 Calcolo sostenibile (green computing)**: efficienza energetica di data center e algoritmi ⟵ C13 ⟶ U6

---

## N. Sicurezza informatica e crittografia

> **Dettaglio completo:** `mappa-informatica-N.md` (v1.0, 101 nodi con prerequisiti diretti).

- **N1 Concetti di base**: riservatezza, integrità, disponibilità (triade CIA); minacce, vulnerabilità, rischio
- **N2 Crittografia classica** `[1]`: cifrario di Cesare, Vigenère, analisi delle frequenze ⟵ A7.1
- **N3 Crittografia moderna** ⟵ A1.4, A4.4, F5
  - N3.1 Simmetrica (AES), cifrari a blocchi e a flusso
  - N3.2 Funzioni hash crittografiche
  - N3.3 Asimmetrica (RSA, curve ellittiche), scambio di chiavi (Diffie-Hellman)
  - N3.4 Firme digitali, certificati, PKI
  - N3.5 Crittografia avanzata: prove a conoscenza zero, crittografia omomorfica, calcolo multiparte sicuro `[4]`
- **N4 Protocolli sicuri**: TLS/HTTPS, SSH ⟵ J7
- **N5 Autenticazione e controllo degli accessi**: password, autenticazione a più fattori, identità digitale (SPID/CIE)
- **N6 Sicurezza del software**: vulnerabilità tipiche (injection, buffer overflow ⟵ G4, XSS ⟵ K4), sviluppo sicuro
- **N7 Sicurezza di reti e sistemi**: firewall, IDS, malware (a livello concettuale) ⟵ J11
- **N8 Sicurezza hardware**: canali laterali, Spectre/Meltdown ⟵ D10
- **N9 Fattore umano** `[1]`: ingegneria sociale, phishing, igiene digitale ⟶ U7
- **N10 Crittografia post-quantistica** ⟵ T4 (algoritmo di Shor)
- **N11 Tecnologie per la privacy**: anonimizzazione, privacy differenziale ⟵ A7
- **N12 Informatica forense**
- **N13 Sicurezza dell'IA**: esempi avversari, avvelenamento dei dati, prompt injection ⟵ O5, O6
- **N14 Governance della sicurezza**: gestione del rischio, politiche, normative (NIS2, ISO/IEC 27001), risposta agli incidenti ⟶ U4

---

## O. Intelligenza artificiale

> **Dettaglio completo:** `mappa-informatica-O.md` (v1.0, 122 nodi con prerequisiti diretti).

- **O1 Storia, definizioni, test di Turing; IA debole e forte** ⟶ U2
- **O2 IA simbolica**
  - O2.1 Ricerca nello spazio degli stati (BFS, A*) ⟵ E7.3
  - O2.2 Giochi (minimax, potatura alfa-beta)
  - O2.3 Rappresentazione della conoscenza, logica, ontologie ⟵ A2.2
  - O2.4 Sistemi esperti, pianificazione
  - O2.5 Soddisfacimento di vincoli e ragionamento automatico ⟵ F14
- **O3 Ragionamento in condizioni di incertezza**: reti bayesiane (⟵ A7.2), logica fuzzy (⟵ A2.6)
- **O4 Machine learning** ⟵ A5, A6, A7, L9
  - O4.1 Apprendimento supervisionato: regressione, classificazione, alberi di decisione, k-NN, SVM
  - O4.2 Apprendimento non supervisionato: clustering, riduzione della dimensionalità (PCA ⟵ A5.3)
  - O4.3 Valutazione: overfitting, validazione, metriche
  - O4.4 Apprendimento per rinforzo ⟵ A7.5
- **O5 Reti neurali e deep learning** ⟵ A6.2, A9.2
  - O5.1 Percettrone, reti multistrato, backpropagation
  - O5.2 Reti convoluzionali (CNN) ⟶ Q5
  - O5.3 Reti ricorrenti (RNN, LSTM)
  - O5.4 Meccanismo di attenzione e Transformer ⟶ P7
- **O6 IA generativa**: modelli linguistici di grandi dimensioni (LLM), modelli di diffusione, prompting, RAG, agenti ⟶ H10, P7
- **O7 Sicurezza e affidabilità dell'IA**: allineamento, interpretabilità, robustezza
- **O8 Calcolo evolutivo e intelligenza di sciame** ⟵ A9.3
- **O9 Hardware, costi ed energia dell'IA** ⟵ D12 ⟶ U6
- **O10 IA, etica e diritto** (AI Act) ⟶ U3, U4
- **O11 IA nell'educazione** ⟶ W
- **O12 Sistemi multi-agente**: agenti autonomi, coordinamento, negoziazione ⟵ O2, F11
- **O13 Affective computing**: riconoscimento e modellazione delle emozioni ⟵ O4, Q8 ⟶ S13
- **O14 Valutazione dell'IA**: benchmark, metriche, valutazione umana ⟵ O4.3

---

## P. Linguistica computazionale ed elaborazione del linguaggio naturale

> **Dettaglio completo:** `mappa-informatica-P.md` (v1.0, 63 nodi con prerequisiti diretti).

- **P1 Fondamenti di linguistica**: fonologia, morfologia, sintassi, semantica, pragmatica
- **P2 Linguaggi formali e linguaggi naturali a confronto** ⟵ F2
- **P3 Elaborazione del testo**: tokenizzazione, stemming, lemmatizzazione, espressioni regolari ⟵ F1, B4
- **P4 Linguistica dei corpora**: frequenze, legge di Zipf ⟵ A7
- **P5 Modelli linguistici statistici**: n-grammi, catene di Markov ⟵ A7.5
- **P6 Analisi linguistica automatica**: POS tagging, parsing sintattico (⟵ F2), semantica distribuzionale e word embedding (⟵ A5)
- **P7 NLP neurale**: Transformer, LLM ⟵ O5.4, O6
- **P8 Applicazioni**: traduzione automatica, analisi del sentiment, chatbot, riassunto, estrazione di informazioni
- **P9 Tecnologie della voce**: riconoscimento e sintesi vocale ⟵ B7, A6.5
- **P10 Digital humanities e stilometria** ⟶ S10

---

## Q. Grafica, multimedia, visione artificiale e interazione

> **Dettaglio completo:** `mappa-informatica-Q.md` (v1.0, 95 nodi con prerequisiti diretti).

- **Q1 Grafica 2D**: primitive, rasterizzazione, trasformazioni geometriche ⟵ A5.2, B6
- **Q2 Grafica 3D**: mesh, proiezione, illuminazione, shading, rendering, ray tracing; pipeline grafica su GPU ⟵ D11
- **Q3 Animazione, simulazione fisica, sviluppo di videogiochi** (motori di gioco) ⟵ A6
- **Q4 Elaborazione delle immagini**: istogrammi, filtri, convoluzione (⟵ A6.5), segmentazione ⟵ B6
- **Q5 Visione artificiale**: estrazione di feature, riconoscimento di oggetti ⟵ O5.2 ⟶ R6
- **Q6 Audio e musica digitale**: sintesi del suono, effetti, DAW ⟵ B7
- **Q7 Realtà virtuale e aumentata**
- **Q8 Interazione uomo-macchina (HCI)**: usabilità, UX, design dell'interazione, accessibilità, basi di psicologia cognitiva
- **Q9 Visualizzazione dei dati** ⟵ L9
- **Q10 Grafica per il web** (SVG, Canvas, WebGL) ⟵ K12
- **Q11 Modellazione geometrica**: curve e superfici (Bézier, spline), CAD, stampa 3D ⟵ A5, A6, E12
- **Q12 Computing ubiquo, indossabile e interfacce tangibili** ⟵ R10
- **Q13 Lavoro cooperativo e social computing (CSCW)**: strumenti collaborativi, comunità online, crowdsourcing
- **Q14 Creatività computazionale e arte generativa**: arte algoritmica, musica generativa, creative coding (Processing, p5.js) ⟵ G2, Q1
- **Q15 Metodi di valutazione in HCI**: test con utenti, studi controllati, questionari, metodi qualitativi ⟵ A7.4

---

## R. Robotica, automazione, sistemi embedded e IoT

> **Dettaglio completo:** `mappa-informatica-R.md` (v1.0, 88 nodi con prerequisiti diretti).

- **R1 Sensori e attuatori** ⟵ C1–C4: tipi di sensori, segnali; motori DC, passo-passo, servo
- **R2 Microcontrollori**: Arduino, micro:bit, Raspberry Pi Pico; GPIO, PWM, ADC ⟵ C7, D13
- **R3 Programmazione embedded**: C/MicroPython, interrupt, vincoli di tempo e memoria, RTOS ⟵ I8
- **R4 Controlli automatici** ⟵ A6.4: sistemi dinamici, retroazione, controllore PID, stabilità, controllo digitale
- **R5 Automazione industriale**: PLC, linguaggio ladder, SCADA, Industria 4.0
- **R6 Robotica**
  - R6.1 Cinematica diretta e inversa ⟵ A5.2
  - R6.2 Dinamica
  - R6.3 Pianificazione del moto ⟵ E7.3
  - R6.4 Localizzazione e mappatura (SLAM) ⟵ A7
  - R6.5 Percezione ⟵ Q5
- **R7 Robotica autonoma e apprendimento** ⟵ O4.4
- **R8 Robot collaborativi (cobot), sociali, umanoidi**
- **R9 Veicoli autonomi e droni**
- **R10 Internet of Things**: protocolli (MQTT), reti di sensori (⟵ J), sicurezza IoT (⟵ N)
- **R11 Sistemi cyber-fisici e digital twin**
- **R12 Robotica educativa** `[1]` ⟶ W
- **R13 Cibernetica e teoria dei sistemi**: retroazione come concetto generale (Wiener), sistemi auto-organizzati ⟵ R4 ⟶ U2, S14

---

## S. Informatica applicata alle scienze

> **Dettaglio completo:** `mappa-informatica-S.md` (v1.0, 105 nodi con prerequisiti diretti).

- **S1 Calcolo scientifico e simulazione** ⟵ A10: modellizzazione, metodi Monte Carlo (⟵ A7), simulazioni ad agenti
- **S2 Bioinformatica e informatica genetica**
  - S2.1 Basi di biologia molecolare: DNA, RNA, proteine, dogma centrale
  - S2.2 Il DNA come codice: alfabeto a 4 simboli, codoni, codice genetico ⟵ B1, A8.1
  - S2.3 Sequenziamento e dati genomici; formati (FASTA, FASTQ) ⟵ B11
  - S2.4 Allineamento di sequenze (Needleman-Wunsch, Smith-Waterman, BLAST) ⟵ E7.4, E8
  - S2.5 Filogenetica ⟵ A4.3
  - S2.6 Genomica, proteomica, predizione della struttura proteica (AlphaFold) ⟵ O5
  - S2.7 Biologia dei sistemi, reti biologiche
  - S2.8 Etica e privacy dei dati genetici ⟶ U3
- **S3 Neuroscienze computazionali** ⟶ O5, T10.2
- **S4 Chimica computazionale e scienza dei materiali** ⟶ T (simulazione quantistica)
- **S5 Fisica computazionale e astroinformatica** ⟵ M5
- **S6 Ambiente, clima e sistemi informativi geografici (GIS)**
- **S7 Informatica medica**: cartella clinica elettronica, imaging, telemedicina
- **S8 Informatica per economia e finanza** (fintech)
- **S9 Scienze sociali computazionali**: analisi delle reti sociali ⟵ A4.3
- **S10 Informatica umanistica** ⟵ P10
- **S11 Vita artificiale e automi cellulari** (Gioco della vita di Conway) ⟵ F1
- **S12 Calcolo simbolico e software matematico**: sistemi di algebra computazionale, librerie numeriche, dimostrazione assistita ⟵ A, F9
- **S13 Scienze cognitive e psicologia computazionale**: modelli computazionali della mente, architetture cognitive, psicometria computazionale ⟵ O, A7 ⟶ U2
- **S14 Sistemi complessi e scienza delle reti**: reti a invarianza di scala, dinamiche emergenti, epidemiologia computazionale ⟵ A4.3, S1
- **S15 Ingegneria e manifattura computazionale**: simulazione agli elementi finiti, CAD/CAM, digital twin industriale ⟵ A10, Q11
- **S16 Informatica giuridica**: documenti normativi digitali, legal tech ⟵ P8 ⟶ U4

---

## T. Calcolo quantistico e paradigmi non convenzionali `[3–4]` (introduzione divulgativa possibile a `[2]`)

> **Dettaglio completo:** `mappa-informatica-T.md` (v1.0, 54 nodi con prerequisiti diretti).

- **T1 Prerequisiti**: numeri complessi e algebra lineare (⟵ A5.4), probabilità (⟵ A7), postulati della meccanica quantistica (⟵ C15)
- **T2 Il qubit**: sovrapposizione, sfera di Bloch, misura; entanglement
- **T3 Circuiti quantistici**: porte (X, H, CNOT…), reversibilità ⟵ D2
- **T4 Algoritmi quantistici**: Deutsch-Jozsa, Grover, trasformata di Fourier quantistica, Shor ⟶ N10
- **T5 Complessità quantistica**: classe BQP, vantaggio quantistico ⟵ F5
- **T6 Hardware quantistico**: superconduttori, ioni intrappolati, fotoni, atomi neutri; decoerenza
- **T7 Correzione degli errori quantistici** ⟵ B10
- **T8 Programmazione quantistica**: Qiskit, Cirq; simulatori ⟵ G2.2
- **T9 Comunicazione quantistica**: distribuzione quantistica delle chiavi (BB84), teletrasporto ⟵ N3
- **T10 Paradigmi non convenzionali**
  - T10.1 DNA computing (esperimento di Adleman), memorizzazione su DNA ⟵ S2
  - T10.2 Calcolo neuromorfico ⟵ S3
  - T10.3 Calcolo ottico/fotonico
  - T10.4 Calcolo analogico, reversibile, stocastico

---

## U. Storia, società, etica, diritto ed economia (trasversale)

> **Dettaglio completo:** `mappa-informatica-U.md` (v1.0, 96 nodi con prerequisiti diretti).

- **U1 Storia dell'informatica**: abaco; Pascal e Leibniz; Babbage e Ada Lovelace; Boole; Hollerith; Turing; ENIAC e von Neumann; transistor (1947); circuito integrato; microprocessore (1971); personal computer; Internet; Web (1989); smartphone; IA contemporanea
- **U2 Filosofia dell'informatica e della mente**: che cos'è calcolare, argomento della stanza cinese ⟵ F3, O1
- **U3 Etica**: bias algoritmico, responsabilità, trasparenza, etica dell'IA
- **U4 Diritto**: privacy (GDPR), diritto d'autore e licenze (open source, Creative Commons), AI Act, reati informatici, Codice dell'Amministrazione Digitale
- **U5 Economia digitale**: piattaforme, economia dei dati, filiere dei chip, lavoro e automazione
- **U6 Sostenibilità**: consumi dei data center e dell'IA, rifiuti elettronici, materie prime critiche ⟵ C13
- **U7 Cittadinanza digitale** `[1]`: identità digitale, disinformazione, benessere digitale, divari digitali
- **U8 Inclusione e questione di genere nell'informatica**
- **U9 Professioni informatiche e deontologia**
- **U10 Metodi di analisi etica**: etiche consequenzialiste, deontologiche, delle virtù applicate a casi tecnologici ⟶ U3
- **U11 Comunicazione tecnica e scientifica**: scrivere documentazione, presentare, divulgare

---

## V. Sistemi informativi e informatica gestionale `[2–3]`

> **Dettaglio completo:** `mappa-informatica-V.md` (v1.0, 40 nodi con prerequisiti diretti).

- **V1 Sistema informativo e sistema informatico**: componenti, flussi informativi, ruoli nell'organizzazione
- **V2 Processi aziendali**: modellazione (BPMN), gestione dei processi (BPM) ⟵ H3
- **V3 Sistemi gestionali**: ERP, CRM, gestione della filiera (SCM)
- **V4 Business intelligence e sistemi di supporto alle decisioni** ⟵ L8, L9
- **V5 Commercio elettronico e pagamenti digitali** ⟵ K7, N3
- **V6 E-government e servizi digitali pubblici**: identità digitale, interoperabilità, PagoPA ⟵ N5 ⟶ U7
- **V7 Enterprise architecture e governance IT** (ITIL, COBIT)
- **V8 Trasformazione digitale e gestione dell'innovazione** ⟶ U5

---

## W. Didattica dell'informatica (meta-ramo)

> **Dettaglio completo:** `mappa-informatica-W.md` (v1.0, 37 nodi con prerequisiti diretti).

- **W1 Pensiero computazionale come competenza** ⟵ E1
- **W2 Informatica unplugged**
- **W3 Linguaggi visuali e micromondi** (Logo, Scratch)
- **W4 Misconcezioni tipiche** (variabile, assegnazione, ricorsione, riferimenti)
- **W5 Curricoli e quadri di riferimento** (Indicazioni nazionali, DigComp, CSTA K-12)
- **W6 Valutazione nella programmazione**
- **W7 Gamification e piattaforme di apprendimento**

---

## Nodi-ponte principali (da cui passano molti archi)

| Nodo | Perché è un ponte |
|---|---|
| A2.1 Logica proposizionale | alimenta Boole (D1), programmazione (E3), SQL (L5), IA simbolica (O2) |
| A5 Algebra lineare | serve a grafica (Q), ML (O4–O5), robotica (R6), quantistica (T) |
| A6.5 Fourier | serve ad audio (B7), compressione (B9), telecomunicazioni (J1), immagini (Q4), voce (P9) |
| A7 Probabilità | serve a ML, NLP, crittografia, robotica (SLAM), simulazione |
| B2 Binario/esadecimale | serve ad architettura, colori (B5.3), reti (J5), sicurezza |
| C9 Legge di Moore | collega fisica ed elettronica al parallelismo (M), alle GPU e all'IA (O9), all'economia (U5), ai paradigmi post-silicio (T10) |
| E7.3 Algoritmi sui grafi | servono a routing (J5), IA (O2), robotica (R6), social network (S9) |
| F2 Grammatiche formali | servono a compilatori (G7) e linguistica computazionale (P) |
| G4 Gestione della memoria | serve a C/Rust (G5), sicurezza (N6), sistemi operativi (I4) |
| O5 Deep learning | serve a visione (Q5), NLP (P7), bioinformatica (S2.6), robotica (R7) |

---

## Verifica di copertura (v0.3, 27/09/2026)

La mappa è stata confrontata con cinque tassonomie di riferimento. Nessuna tassonomia è esaustiva: la copertura va intesa come "ogni voce delle fonti ha almeno un nodo corrispondente". Non significa che la mappa sia completa in assoluto.

### Fonti
1. **ACM Computing Classification System 2012** (CCS): la classificazione ufficiale della ricerca informatica, 13 categorie di primo livello. <https://dl.acm.org/ccs>. Le pagine ACM non erano consultabili automaticamente, per cui le categorie sono riportate dall'elenco pubblicato e noto; vanno ricontrollate sul sito.
2. **ACM/IEEE-CS/AAAI Computer Science Curricula 2023** (CS2023): 17 aree di conoscenza per i corsi di laurea. <https://csed.acm.org/knowledge-areas/>
3. **SWEBOK v4.0** (IEEE Computer Society, 2024): 18 aree di conoscenza dell'ingegneria del software. <https://www.computer.org/education/bodies-of-knowledge/software-engineering>
4. **Categorie arXiv cs.\***: circa 40 aree della ricerca corrente. <https://arxiv.org/corr/subjectclasses>
5. **Proposta CINI di Indicazioni Nazionali per l'informatica nella scuola**: 5 nuclei tematici. <https://www.consorzio-cini.it/images/Proposta-Indicazioni-Nazionali-Informatica-Scuola-numerata.pdf>

### ACM CCS 2012 → mappa
| Categoria CCS | Nodi |
|---|---|
| General and reference | U1, U11, H15 |
| Hardware | C, D, C16, C17, C18 |
| Computer systems organization | D, R (sistemi embedded e real-time), I12 |
| Networks | J |
| Software and its engineering | G, H, I |
| Theory of computation | F, E |
| Mathematics of computing | A, S12 |
| Information systems | L, V, K10, L11–L13 |
| Security and privacy | N, L15 |
| Human-centered computing | Q8, Q12–Q15, K5 |
| Computing methodologies | O, P, Q, S1, M |
| Applied computing | S, V, S15, S16, W |
| Social and professional topics | U |

### CS2023 → mappa
| Area | Nodi |
|---|---|
| AL Algorithmic Foundations | E, F1–F5 |
| AR Architecture and Organization | D, C |
| AI Artificial Intelligence | O |
| DM Data Management | L |
| FPL Foundations of Programming Languages | G, F6–F8, F13 |
| GIT Graphics and Interactive Techniques | Q |
| HCI Human-Computer Interaction | Q8, Q15, K5 |
| MSF Mathematical and Statistical Foundations | A |
| NC Networking and Communication | J |
| OS Operating Systems | I |
| PDC Parallel and Distributed Computing | M, E11, F13 |
| SEC Security | N |
| SEP Society, Ethics, and the Profession | U, U10, U11 |
| SDF Software Development Fundamentals | E1–E7, G1–G2 |
| SE Software Engineering | H |
| SPD Specialized Platform Development (web, mobile, robot, embedded, giochi, interattive) | K, K9, R, Q3, Q7 |
| SF Systems Fundamentals | D, I, I12 |

### SWEBOK v4 → mappa
| Area | Nodi |
|---|---|
| Requisiti · Architettura · Progettazione · Costruzione | H11 · H12 · H4 · G, H6 |
| Testing · Operazioni · Manutenzione | H6 · H14 · H13 |
| Gestione della configurazione · Gestione · Processo | H13, H5 · H9 · H2 |
| Modelli e metodi · Qualità | H3, F9 · H15 |
| Sicurezza · Pratica professionale · Economia | H17, N6 · H18, U9 · H16 |
| Fondamenti di computing · matematici · ingegneristici | D, E, G, I, J, L, O · A · H15, A7 |

### arXiv cs.\* → mappa (sintesi)
AI→O · AR→D · CC→F5 · CE→S1, S8, S15 · CG→E12 · CL→P · CR→N · CV→Q5 · CY→U · DB→L · DC→M · DL→L13 · DM→A4 · DS→E · ET→C18, T10 · FL→F1–F2 · GL→U11 · GR→Q1–Q2 · GT→F11 · HC→Q8 · IR→L11–L12 · IT→A8 · LG→O4–O5 · LO→A2, F9 · MA→O12 · MM→B6–B8, Q6 · MS→S12 · NA→A10 · NE→O5, O8 · NI→J · OS→I · PF→I12 · PL→G · RO→R · SC→S12 · SD→Q6, P9 · SE→H · SI→S9, S14 · SY→R4

### Proposta CINI → mappa
| Nucleo | Nodi |
|---|---|
| Algoritmi | E, F4 (problemi non risolvibili) |
| Programmazione | G1–G3 |
| Dati e informazione | B, E6, L |
| Consapevolezza digitale | N9, U7, R1 (sensori), H11 |
| Creatività digitale | Q14, Q3, Q6 |

### Lacune individuate e colmate in v0.3
| Aggiunta | Fonte che l'ha evidenziata |
|---|---|
| **V Sistemi informativi e informatica gestionale** (area nuova) | CCS *Information systems*, *Applied computing* |
| C16 EDA/VLSI, C17 affidabilità hardware, C18 tecnologie emergenti di dispositivo | CCS *Hardware*, arXiv ET |
| E12 geometria computazionale | arXiv CG |
| F12 teoria dell'apprendimento, F13 modelli della concorrenza, F14 SAT/vincoli | CCS *Theory of computation* |
| A11 teoria dei numeri computazionale | CCS *Mathematics of computing* |
| B13 documenti digitali e tipografia | CCS *Applied computing* (document management) |
| G10 altri paradigmi (probabilistico, low-code, linguaggio naturale) | CS2023 FPL |
| H11–H18 (requisiti, architettura, configurazione/manutenzione, DevOps, metriche, economia, sicurezza, pratica professionale) | SWEBOK v4 |
| I12 prestazioni e affidabilità | CS2023 SF, arXiv PF |
| J14 standard e governance di Internet | CCS *Networks* |
| L12 raccomandazione, L13 biblioteche digitali, L14 dati distribuiti, L15 sicurezza dei dati | CS2023 DM, arXiv DL/IR |
| M8 green computing | CS2023 SEP (sostenibilità) |
| N3.5 crittografia avanzata, N13 sicurezza dell'IA, N14 governance della sicurezza | CS2023 SEC |
| O2.5 vincoli, O12 multi-agente, O13 affective computing, O14 valutazione | arXiv MA, CCS *Computing methodologies* |
| Q11 modellazione geometrica, Q12 ubiquitous computing, Q13 CSCW, Q14 creatività computazionale, Q15 valutazione in HCI | CS2023 GIT/HCI, CCS HCC |
| R13 cibernetica | CCS, storia della disciplina |
| S12 calcolo simbolico, S13 scienze cognitive, S14 sistemi complessi, S15 ingegneria computazionale, S16 informatica giuridica | arXiv SC/MS/SI/CE, CCS *Applied computing* |
| U10 analisi etica, U11 comunicazione tecnica | CS2023 SEP |

### Limiti noti
- **Profondità disomogenea**: alcune aree sono al 2°–3° livello, altre solo al 1°. Si uniforma nella fase "dettaglio per ramo".
- **Frontiere mobili**: IA, calcolo quantistico e sicurezza cambiano in fretta. Conviene ripetere la verifica ogni anno (una nuova edizione di CCS e di CS2023 porterebbe nuove voci).
- **Intersezioni con altre discipline**: coprono i campi con comunità scientifiche riconosciute (bio-, neuro-, geo-, chemo-informatica, informatica giuridica, digital humanities, economia, psicologia/scienze cognitive, arte). Campi più di nicchia, come l'agricoltura di precisione o l'informatica musicale avanzata, si aggiungono come foglie di S o Q quando servono.

---

## Stato del dettaglio e del grafo (v0.4, 27/09/2026)

Tutte le 23 aree hanno un file di dettaglio. Qui sopra resta l'alberatura sintetica; la versione di riferimento di ogni nodo è quella del file di area.

**Numeri del grafo** (calcolati da `valida-mappa.py`):
- **2375 nodi** e 3748 archi di prerequisito diretto (99 nodi di approfondimento aggiunti nella v0.5).
- **40 nodi radice**: sono i punti d'ingresso, cioè i nodi senza prerequisiti.
- **Catena di prerequisiti più lunga: 23 passi.**
- **Nessun ciclo, nessun riferimento rotto, nessuna inversione di livello** (nessun nodo ha un livello più basso di un suo prerequisito). All'inizio il controllo ne aveva trovate 136: sono state corrette tutte, restringendo i riferimenti troppo generici oppure alzando il livello del nodo.

**File del sistema:**
| File | Contenuto |
|---|---|
| `mappa-informatica.md` | documento madre: scopo, convenzioni, alberatura sintetica, verifica di copertura |
| `mappa-informatica-A.md` … `-W.md` | dettaglio per area: un nodo per riga, con livello, prerequisiti diretti e collegamenti in uscita |
| `valida-mappa.py` | validatore ed esportatore: `python3 valida-mappa.py mappa-informatica-?.md --esporta` |
| `grafo-informatica.json`, `-nodi.csv`, `-archi.csv` | il grafo esportato, pronto per Graphviz, Gephi, D3 o una piattaforma |

**Nodi aggiunti durante il dettaglio** (non presenti nell'alberatura sintetica): A1.5, A3.5, A9.4, E6.8, G5.11, O5.5, R6.6, W8.

**Prossimi passi:**
1. **Revisione umana per area**: controllare nodi, formulazioni e livelli, a partire dalle aree insegnate (B, D, E, G, I, J, K, L).
2. **Mappatura sugli indirizzi**: aggiungere a ogni nodo i tag indirizzo/anno (liceo scienze applicate, ITI informatica, IPSIA).
3. **Visualizzazione interattiva del grafo**: esplorare prerequisiti e sviluppi di un nodo, filtrare per area e livello.
4. **Verifica annuale** della copertura con le nuove edizioni delle tassonomie di riferimento.

## Registro modifiche
- **v0.5 (27/09/2026)**: aggiunti 99 nodi di approfondimento, marcati "(v1.1, approfondimento)" nei file di area, per il videogioco "I cinque duchi". `S14.4` (modelli epidemici) ora richiede `A6.4.1` e `S1.4` invece di `A6.4.3`. Il grafo resta aciclico e senza inversioni di livello.
- **v0.4 (27/09/2026)**: dettaglio di tutte le aree B–W (v1.0); validatore esteso con controllo dei riferimenti in uscita e dei livelli, ed esportazione del grafo in JSON e CSV.
- **v0.3 (27/09/2026)**: verifica di copertura con 5 tassonomie; aggiunta l'area V e 60 nodi.
- **v0.2 (27/09/2026)**: alberatura estesa a 21 aree.
