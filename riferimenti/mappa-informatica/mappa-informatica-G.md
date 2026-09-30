# Mappa dell'informatica — Area G: Linguaggi e paradigmi di programmazione (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** programmare in concreto: concetti di base in un linguaggio reale, primi linguaggi (blocchi, Python), paradigmi, gestione della memoria, principali famiglie di linguaggi, sistemi di tipi, implementazione dei linguaggi (compilatori e interpreti), metaprogrammazione, storia. I concetti algoritmici indipendenti dal linguaggio sono nell'area E, i fondamenti teorici nell'area F.

---

## G1 Concetti base della programmazione
- **G1.1** Programma e linguaggio di programmazione; sintassi e semantica · [1] · ⟵ E2.3
- **G1.2** L'ambiente di sviluppo: editor, interprete o compilatore, esecuzione · [1] · ⟵ G1.1
- **G1.3** Errori di sintassi, di esecuzione e logici; leggere i messaggi di errore · [1] · ⟵ G1.2
- **G1.4** Variabili, tipi e assegnazione in un linguaggio reale · [1] · ⟵ G1.2, E4.2
- **G1.5** Operatori ed espressioni; conversioni di tipo · [1] · ⟵ G1.4, E4.3
- **G1.6** Input e output da console; formattazione · [1] · ⟵ G1.4, E4.4
- **G1.7** Selezione e iterazione nel linguaggio · [1] · ⟵ G1.5, E3.5
- **G1.8** Funzioni: definizione, parametri, valore restituito · [1–2] · ⟵ G1.7, E3.9
- **G1.9** Visibilità e durata delle variabili; locali e globali · [2] · ⟵ G1.8
- **G1.10** Passaggio dei parametri: per valore, per riferimento, per condivisione · [2] · ⟵ G1.9
- **G1.11** Commenti, nomi significativi, stile del codice · [1] · ⟵ G1.2
- **G1.12** Debugging: stampe di controllo, punti di interruzione, esecuzione passo passo · [1–2] · ⟵ G1.3, E2.5
- **G1.13** Leggere e scrivere file di testo · [2] · ⟵ G1.7, B11.2
- **G1.14** Gestione delle eccezioni · [2] · ⟵ G1.8, G1.3
- **G1.15** Moduli e librerie · [2] · ⟵ G1.8
- **G1.16** Selezione multipla con match/case · [2] · ⟵ G1.7 · (v1.1, approfondimento)

## G2 Primo linguaggio

### G2.1 Programmazione a blocchi
- **G2.1.1** L'ambiente Scratch: sprite, sfondi, script · [1] · ⟵ E2.4
- **G2.1.2** Eventi e messaggi fra sprite · [1] · ⟵ G2.1.1
- **G2.1.3** Variabili, liste e cicli a blocchi · [1] · ⟵ G2.1.1, E3.5, E4.1
- **G2.1.4** Blocchi personalizzati · [1] · ⟵ G2.1.3, E3.9
- **G2.1.5** Progetti: animazioni, storie, giochi · [1] · ⟵ G2.1.2, G2.1.3
- **G2.1.6** Il passaggio dai blocchi al testo · [1] · ⟵ G2.1.4, G1.1

### G2.2 Python
- **G2.2.1** Interprete, script, notebook · [1] · ⟵ G1.2
- **G2.2.2** Tipi di base (int, float, bool, str); tipizzazione dinamica · [1] · ⟵ G2.2.1, G1.4
- **G2.2.3** Strutture di controllo; l'indentazione come sintassi · [1] · ⟵ G2.2.2, G1.7
- **G2.2.4** Stringhe: indici, slicing, metodi · [1] · ⟵ G2.2.3, E6.1.5
- **G2.2.5** Liste e tuple · [1] · ⟵ G2.2.3, E6.1.1
- **G2.2.6** Dizionari e insiemi · [1–2] · ⟵ G2.2.5, E6.1.6
- **G2.2.7** Funzioni; parametri con valore predefinito e per nome · [1–2] · ⟵ G2.2.3, G1.8
- **G2.2.8** Comprensioni di lista · [2] · ⟵ G2.2.5, G2.2.7
- **G2.2.9** File ed eccezioni in Python · [2] · ⟵ G2.2.7, G1.13, G1.14
- **G2.2.10** Libreria standard e pacchetti (pip, ambienti virtuali) · [2] · ⟵ G2.2.7, G1.15
- **G2.2.11** Classi e oggetti in Python · [2] · ⟵ G2.2.7, G3.2.1
- **G2.2.12** Grafica e giochi: turtle, pygame · [1–2] · ⟵ G2.2.3
- **G2.2.13** Librerie scientifiche: NumPy, pandas, matplotlib · [2] · ⟵ G2.2.10, E6.1.4 · ⟶ L9
- **G2.2.14** Iteratori, generatori, decoratori · [3] · ⟵ G2.2.7, G3.3.3
- **G2.2.15** Annotazioni di tipo (type hints) · [2–3] · ⟵ G2.2.7, G6.1

## G3 Paradigmi

### G3.1 Imperativo e procedurale
- **G3.1.1** Stato, istruzioni, effetti collaterali · [2] · ⟵ G1.7
- **G3.1.2** Programmazione procedurale; scomposizione dall'alto verso il basso · [2] · ⟵ G3.1.1, G1.8
- **G3.1.3** Programmazione strutturata e istruzione goto · [2] · ⟵ G3.1.2, E3.8

### G3.2 Orientato agli oggetti
- **G3.2.1** Classi e oggetti; attributi e metodi · [2] · ⟵ G1.8, E6.3.5
- **G3.2.2** Costruttori, stato e identità di un oggetto · [2] · ⟵ G3.2.1
- **G3.2.3** Incapsulamento e visibilità · [2] · ⟵ G3.2.2
- **G3.2.4** Ereditarietà · [2] · ⟵ G3.2.3
- **G3.2.5** Polimorfismo e ridefinizione dei metodi · [2] · ⟵ G3.2.4
- **G3.2.6** Classi astratte e interfacce · [2–3] · ⟵ G3.2.5
- **G3.2.7** Composizione e aggregazione in alternativa all'ereditarietà · [2–3] · ⟵ G3.2.4
- **G3.2.8** Membri statici · [2] · ⟵ G3.2.2
- **G3.2.9** Programmazione basata su prototipi (JavaScript) · [3] · ⟵ G3.2.5
- **G3.2.10** Metodi speciali in Python (__str__, __eq__) · [2–3] · ⟵ G3.2.2 · (v1.1, approfondimento)
- **G3.2.11** Proprietà: getter, setter e @property · [3] · ⟵ G3.2.3 · (v1.1, approfondimento)
- **G3.2.12** Oggetti immutabili e dataclass · [3] · ⟵ G3.2.3 · (v1.1, approfondimento)
- **G3.2.13** Ereditarietà multipla e ordine di risoluzione dei metodi · [3] · ⟵ G3.2.4 · (v1.1, approfondimento)
- **G3.2.14** Gerarchie di classi nella libreria standard: le eccezioni · [3] · ⟵ G3.2.4, G1.14 · (v1.1, approfondimento)
- **G3.2.15** Progettare un gioco a oggetti: personaggi, oggetti, stanze · [3] · ⟵ G3.2.5 · (v1.1, approfondimento)

### G3.3 Funzionale
- **G3.3.1** Funzioni pure ed effetti collaterali · [2] · ⟵ G1.8, G3.1.1
- **G3.3.2** Immutabilità · [2] · ⟵ G3.3.1
- **G3.3.3** Funzioni come valori; funzioni di ordine superiore · [2] · ⟵ G3.3.1, A3.3.3
- **G3.3.4** Funzioni anonime (lambda) e closure · [2–3] · ⟵ G3.3.3, G1.9
- **G3.3.5** map, filter, reduce · [2] · ⟵ G3.3.3, A4.4.1
- **G3.3.6** Ricorsione al posto dell'iterazione · [2–3] · ⟵ G3.3.1, E5.4
- **G3.3.7** Tipi algebrici e pattern matching · [3] · ⟵ G3.3.6, F7.4
- **G3.3.8** Valutazione pigra e strutture infinite · [3] · ⟵ G3.3.4, F6.5
- **G3.3.9** Currying e applicazione parziale · [3] · ⟵ G3.3.4, A3.3.4
- **G3.3.10** Funtori e monadi (gestire gli effetti) · [4] · ⟵ G3.3.7, G6.4
- **G3.3.11** Linguaggi funzionali: Haskell, Lisp/Scheme/Racket, OCaml/F#, Erlang/Elixir, Clojure · [3] · ⟵ G3.3.5
- **G3.3.12** Stile funzionale nei linguaggi multiparadigma (Python, JavaScript, Rust) · [2–3] · ⟵ G3.3.5

### G3.4 Logico
- **G3.4.1** Fatti, regole, interrogazioni · [3] · ⟵ A2.2.2
- **G3.4.2** Unificazione e backtracking in Prolog · [3] · ⟵ G3.4.1, A2.2.5, E8.4
- **G3.4.3** Datalog · [3–4] · ⟵ G3.4.1, A3.2.5 · ⟶ L5
- **G3.4.4** Programmazione logica con vincoli; answer set programming · [4] · ⟵ G3.4.2, F14.4

### G3.5 Dichiarativo
- **G3.5.1** Descrivere il "che cosa" invece del "come" · [2] · ⟵ G3.1.1
- **G3.5.2** Linguaggi di markup e di stile come linguaggi dichiarativi · [2] · ⟵ G3.5.1
- **G3.5.3** Linguaggi di interrogazione (SQL) come linguaggi dichiarativi · [2] · ⟵ G3.5.1 · ⟶ L5
- **G3.5.4** Infrastruttura come codice; configurazione dichiarativa · [3] · ⟵ G3.5.1, B11.5 · ⟶ H7

### G3.6 A eventi e reattivo
- **G3.6.1** Eventi, gestori (callback) e ciclo degli eventi · [1–2] · ⟵ G1.8
- **G3.6.2** Programmare interfacce grafiche · [2] · ⟵ G3.6.1, G3.2.1
- **G3.6.3** Programmazione reattiva e flussi di eventi · [3] · ⟵ G3.6.1, G3.3.5
- **G3.6.4** Architetture guidate dagli eventi · [3] · ⟵ G3.6.1 · ⟶ H12

### G3.7 Concorrente
- **G3.7.1** Concorrenza e parallelismo: la differenza · [2] · ⟵ G1.8
- **G3.7.2** Thread e dati condivisi · [2–3] · ⟵ G3.7.1, I2.4
- **G3.7.3** Sincronizzazione nei linguaggi: lock, operazioni atomiche · [3] · ⟵ G3.7.2, I3.3
- **G3.7.4** async/await e coroutine · [2–3] · ⟵ G3.7.1, G3.6.1
- **G3.7.5** Modello ad attori e scambio di messaggi · [3] · ⟵ G3.7.1
- **G3.7.6** Canali e CSP (goroutine in Go) · [3] · ⟵ G3.7.1
- **G3.7.7** Memoria transazionale · [4] · ⟵ G3.7.3

### G3.8 Array e dataflow
- **G3.8.1** Operazioni su interi array; vettorizzazione con NumPy · [2–3] · ⟵ G2.2.13
- **G3.8.2** Linguaggi ad array (APL, J) · [3–4] · ⟵ G3.8.1
- **G3.8.3** Programmazione dataflow e visuale (Node-RED, Max/MSP, LabVIEW) · [2–3] · ⟵ G3.6.1
- **G3.8.4** Grafi computazionali (TensorFlow, JAX) · [3] · ⟵ G3.8.1, A4.3.4 · ⟶ O5

## G4 Gestione della memoria
- **G4.1** Variabili e indirizzi di memoria · [2] · ⟵ D8.1, G1.4
- **G4.2** Stack e heap; record di attivazione · [2–3] · ⟵ G4.1, E5.3
- **G4.3** Riferimenti e puntatori; aritmetica dei puntatori · [2–3] · ⟵ G4.1
- **G4.4** Allocazione e deallocazione manuale · [3] · ⟵ G4.2, G4.3
- **G4.5** Errori di memoria: perdite, puntatori pendenti, doppia deallocazione, overflow · [3] · ⟵ G4.4 · ⟶ N6
- **G4.6** Garbage collection: conteggio dei riferimenti, mark-and-sweep, generazionale · [3] · ⟵ G4.2
- **G4.7** RAII e puntatori intelligenti (C++) · [3] · ⟵ G4.4, G3.2.2
- **G4.8** Ownership, borrowing e lifetime (Rust) · [3] · ⟵ G4.4, G4.3
- **G4.9** Mutabilità, aliasing e sicurezza della memoria · [3–4] · ⟵ G4.8

## G5 Linguaggi per famiglia

### G5.1 C
- **G5.1.1** Struttura di un programma C; compilazione · [2] · ⟵ G1.7
- **G5.1.2** Tipi, dimensioni, rappresentazione · [2] · ⟵ G5.1.1, B2.4.6
- **G5.1.3** Array e stringhe terminate da zero · [2] · ⟵ G5.1.2, E6.1.1
- **G5.1.4** Puntatori in C · [2–3] · ⟵ G5.1.3, G4.3
- **G5.1.5** struct, typedef, union · [2–3] · ⟵ G5.1.2
- **G5.1.6** Memoria dinamica in C · [3] · ⟵ G5.1.4, G4.4
- **G5.1.7** Preprocessore, header, compilazione separata, make · [3] · ⟵ G5.1.1
- **G5.1.8** Libreria standard e chiamate di sistema · [3] · ⟵ G5.1.6, I1
- **G5.1.9** Comportamento indefinito · [3–4] · ⟵ G5.1.4

### G5.2 C++
- **G5.2.1** Da C a C++: riferimenti, sovraccarico, namespace · [2–3] · ⟵ G5.1.4
- **G5.2.2** Classi, costruttori, distruttori · [2–3] · ⟵ G5.2.1, G3.2.2
- **G5.2.3** Template e programmazione generica · [3] · ⟵ G5.2.2, G6.5
- **G5.2.4** Libreria standard: contenitori, iteratori, algoritmi · [3] · ⟵ G5.2.3
- **G5.2.5** Semantica di spostamento e puntatori intelligenti · [3–4] · ⟵ G5.2.2, G4.7

### G5.3 Rust
- **G5.3.1** Strumenti: cargo e crate · [3] · ⟵ G1.15
- **G5.3.2** Ownership, borrowing e lifetime in pratica · [3] · ⟵ G5.3.1, G4.8
- **G5.3.3** Enum, pattern matching, Option e Result · [3] · ⟵ G5.3.1, G3.3.7
- **G5.3.4** Trait e generici · [3] · ⟵ G5.3.3, G6.5
- **G5.3.5** Concorrenza senza data race · [3–4] · ⟵ G5.3.2, G3.7.3
- **G5.3.6** unsafe e interoperabilità con C · [4] · ⟵ G5.3.2, G5.1.4
- **G5.3.7** Rust per sistemi, web (WebAssembly) ed embedded · [3–4] · ⟵ G5.3.4

### G5.4 Java e C#
- **G5.4.1** Tipizzazione statica, classi, package · [2] · ⟵ G3.2.1
- **G5.4.2** JVM e CLR: il bytecode · [2–3] · ⟵ G5.4.1 · ⟶ G7.3
- **G5.4.3** Collezioni e generici · [3] · ⟵ G5.4.1, G6.5
- **G5.4.4** Eccezioni controllate · [2] · ⟵ G5.4.1, G1.14
- **G5.4.5** Interfacce grafiche; applicazioni Android · [2–3] · ⟵ G5.4.1, G3.6.2 · ⟶ K9
- **G5.4.6** Stream e lambda in Java · [3] · ⟵ G5.4.3, G3.3.5

### G5.5 JavaScript e TypeScript
- **G5.5.1** Sintassi, tipi, oggetti e array in JavaScript · [2] · ⟵ G1.7
- **G5.5.2** Funzioni come valori; closure · [2] · ⟵ G5.5.1, G3.3.4
- **G5.5.3** Prototipi e classi · [3] · ⟵ G5.5.1, G3.2.9
- **G5.5.4** Asincronia: callback, promise, async/await · [2–3] · ⟵ G5.5.2, G3.7.4
- **G5.5.5** Node.js e npm · [2–3] · ⟵ G5.5.1, G1.15
- **G5.5.6** TypeScript: tipi statici sopra JavaScript · [3] · ⟵ G5.5.1, G6.1

### G5.6 Go
- **G5.6.1** Sintassi, tipi, struct e interfacce · [3] · ⟵ G3.2.6
- **G5.6.2** Goroutine e canali · [3] · ⟵ G5.6.1, G3.7.6

### G5.7 Shell e scripting
- **G5.7.1** Comandi, argomenti, variabili d'ambiente · [1–2] · ⟵ I7.1
- **G5.7.2** Pipe e ridirezioni · [2] · ⟵ G5.7.1
- **G5.7.3** Script Bash: variabili, condizioni, cicli · [2] · ⟵ G5.7.2, G1.7
- **G5.7.4** Strumenti per il testo (grep, sed, awk) · [2–3] · ⟵ G5.7.2, E7.4.6
- **G5.7.5** PowerShell: pipeline di oggetti · [2–3] · ⟵ G5.7.1, G3.2.1
- **G5.7.6** Automatizzare compiti ripetitivi · [2] · ⟵ G5.7.3

### G5.8 Linguaggi per il calcolo scientifico
- **G5.8.1** R: vettori, data frame, statistica · [3] · ⟵ G1.7, A7.1
- **G5.8.2** Julia: prestazioni e dispatch multiplo · [3–4] · ⟵ G1.8
- **G5.8.3** MATLAB/Octave: calcolo matriciale · [3] · ⟵ G1.7, A5.1.6
- **G5.8.4** Notebook computazionali (Jupyter) · [2] · ⟵ G2.2.1

### G5.9 Linguaggi di descrizione dell'hardware (aspetti linguistici)
- **G5.9.1** Descrivere hardware è diverso da scrivere software · [3] · ⟵ G1.1, D2.1
- **G5.9.2** Concorrenza intrinseca e segnali · [3] · ⟵ G5.9.1, D3.3

### G5.10 Linguaggi e framework quantistici
- **G5.10.1** Framework quantistici in Python (Qiskit, Cirq, PennyLane) · [4] · ⟵ G2.2.10, T3.4
- **G5.10.2** Linguaggi quantistici dedicati (Q#, OpenQASM) · [4] · ⟵ G5.10.1

### G5.11 Altri linguaggi diffusi *(nuovo in v1.0)*
- **G5.11** Kotlin, Swift, PHP, Ruby, Lua, Dart, Zig: caratteristiche e ambiti d'uso · [2–3] · ⟵ G1.8

## G6 Sistemi di tipi
- **G6.1** Tipizzazione statica e dinamica · [2] · ⟵ G1.4, E4.2
- **G6.2** Tipizzazione forte e debole; conversioni implicite · [2] · ⟵ G6.1
- **G6.3** Tipizzazione nominale e strutturale; duck typing · [3] · ⟵ G6.1, G3.2.6
- **G6.4** Inferenza di tipo nei linguaggi · [3] · ⟵ G6.1
- **G6.5** Generici e polimorfismo parametrico · [3] · ⟵ G6.1, G3.2.5
- **G6.6** Tipi nullabili e tipi opzione · [3] · ⟵ G6.1, G3.3.7
- **G6.7** Sistemi di tipi avanzati nei linguaggi reali (dipendenti, lineari) · [4] · ⟵ G6.5, F7.6, F7.8

## G7 Implementazione dei linguaggi

### G7.1 Analisi lessicale e sintattica
- **G7.1.1** Le fasi di un compilatore: panoramica · [2–3] · ⟵ G1.2
- **G7.1.2** Analisi lessicale: token e scanner · [3] · ⟵ G7.1.1, F1.8
- **G7.1.3** Analisi sintattica discendente ricorsiva · [3] · ⟵ G7.1.2, F2.5, E5.1
- **G7.1.4** Analisi sintattica ascendente (LR, LALR); generatori di parser · [3–4] · ⟵ G7.1.3, F2.6
- **G7.1.5** Albero sintattico astratto (AST) · [3] · ⟵ G7.1.3, E6.4.8
- **G7.1.6** Esplorare il bytecode di Python (modulo dis) · [3] · ⟵ G7.1.1 · (v1.1, approfondimento)
- **G7.1.7** Come funziona l'evidenziazione della sintassi negli editor · [3] · ⟵ G7.1.2 · (v1.1, approfondimento)
- **G7.1.8** Suddividere in token un testo in italiano: parole, punteggiatura, apostrofi · [3] · ⟵ G7.1.2 · (v1.1, approfondimento)

### G7.2 Analisi semantica e generazione del codice
- **G7.2.1** Tabella dei simboli; controllo dei tipi · [3] · ⟵ G7.1.5, G6.1, E6.5.4
- **G7.2.2** Rappresentazioni intermedie (codice a tre indirizzi, SSA) · [3–4] · ⟵ G7.2.1
- **G7.2.3** Generazione del codice; allocazione dei registri · [3–4] · ⟵ G7.2.2, D7.4, A4.3.6
- **G7.2.4** Ottimizzazioni: propagazione delle costanti, eliminazione del codice morto, ottimizzazione dei cicli · [4] · ⟵ G7.2.2
- **G7.2.5** Infrastrutture di compilazione (LLVM, GCC) · [4] · ⟵ G7.2.4

### G7.3 Interpreti, macchine virtuali, JIT
- **G7.3.1** Interpreti: il ciclo di valutazione; scrivere un piccolo interprete · [3] · ⟵ G7.1.5
- **G7.3.2** Bytecode e macchine virtuali (JVM, CPython, WebAssembly) · [3] · ⟵ G7.3.1, D6.1
- **G7.3.3** Compilazione just-in-time · [4] · ⟵ G7.3.2, G7.2.4
- **G7.3.4** Transpiler e compilazione verso il web · [3] · ⟵ G7.1.5
- **G7.3.5** Il supporto a runtime: memoria, eccezioni, thread · [3–4] · ⟵ G7.3.2, G4.6
- **G7.3.6** Estendere la calcolatrice con variabili e funzioni · [3–4] · ⟵ G7.3.1 · (v1.1, approfondimento)

### G7.4 Linker e loader
- **G7.4.1** File oggetto e simboli · [3] · ⟵ D7.5
- **G7.4.2** Collegamento statico e dinamico; librerie condivise · [3] · ⟵ G7.4.1
- **G7.4.3** Caricamento in memoria e rilocazione · [3–4] · ⟵ G7.4.2, I4

## G8 Metaprogrammazione e DSL
- **G8.1** Riflessione e introspezione · [3] · ⟵ G3.2.1
- **G8.2** Macro (C, Lisp, Rust) · [3–4] · ⟵ G7.1.5
- **G8.3** Generazione automatica di codice · [3] · ⟵ G8.1
- **G8.4** Linguaggi specifici di dominio, esterni e interni · [3] · ⟵ G7.1.3
- **G8.5** Omoiconicità: il codice come dato · [4] · ⟵ G8.2, G3.3.11

## G9 Storia ed evoluzione dei linguaggi
- **G9.1** I primi linguaggi: assembly, Fortran, COBOL, Lisp, ALGOL · [1–2] · ⟵ U1.10
- **G9.2** Programmazione strutturata: Pascal, C · [2] · ⟵ G9.1, E3.8
- **G9.3** Linguaggi a oggetti: Simula, Smalltalk, C++, Java · [2] · ⟵ G9.2, G3.2.1
- **G9.4** Linguaggi di scripting e del web: Perl, Python, JavaScript, PHP · [2] · ⟵ G9.3
- **G9.5** Linguaggi recenti (Rust, Go, Swift, Kotlin) e tendenze · [2–3] · ⟵ G9.4
- **G9.6** Linguaggi educativi: Logo, BASIC, Pascal, Scratch · [1–2] · ⟵ G9.1 · ⟶ W3
- **G9.7** Linguaggi esoterici e Turing-completezza · [3] · ⟵ F3.6

## G10 Altri paradigmi e strumenti
- **G10.1** Programmazione probabilistica · [4] · ⟵ A7.4.4, G1.8
- **G10.2** Piattaforme low-code e no-code · [1–2] · ⟵ E1.5
- **G10.3** Le formule dei fogli di calcolo come programmazione funzionale · [1–2] · ⟵ L2.2
- **G10.4** Programmare in linguaggio naturale con assistenti IA · [2] · ⟵ G1.3 · ⟶ O6, H10
- **G10.5** Programmazione visuale per IoT e robotica · [1–2] · ⟵ G2.1.3 · ⟶ R12
- **G10.6** Programmazione letterata e notebook · [2–3] · ⟵ G5.8.4
