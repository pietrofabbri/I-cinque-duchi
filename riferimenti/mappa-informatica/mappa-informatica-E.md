# Mappa dell'informatica — Area E: Algoritmi e strutture dati (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** dal pensiero computazionale del primo biennio fino agli algoritmi avanzati. I concetti di programmazione sono trattati qui in forma indipendente dal linguaggio; la loro realizzazione in un linguaggio specifico è nell'area G.

---

## E1 Pensiero computazionale
- **E1.1** Problema, istanza, soluzione · [1] · ⟵ —
- **E1.2** Scomporre un problema in sottoproblemi · [1] · ⟵ E1.1
- **E1.3** Riconoscere schemi ricorrenti · [1] · ⟵ E1.1
- **E1.4** Astrazione: che cosa tenere e che cosa trascurare; il modello · [1] · ⟵ E1.1
- **E1.5** Algoritmo: definizione e proprietà (finitezza, non ambiguità, eseguibilità) · [1] · ⟵ E1.2
- **E1.6** Esecutore e istruzioni elementari; esecutore umano e macchina · [1] · ⟵ E1.5
- **E1.7** Attività unplugged (percorsi su griglia, ordinare carte) · [1] · ⟵ E1.5 · ⟶ W2
- **E1.8** Algoritmi nella vita quotidiana e loro limiti · [1] · ⟵ E1.5
- **E1.9** Rompicapi e giochi di logica come problemi computazionali (labirinti, travasi) · [1] · ⟵ E1.2 · (v1.1, approfondimento)

## E2 Rappresentazione degli algoritmi
- **E2.1** Descrizione in linguaggio naturale; il problema dell'ambiguità · [1] · ⟵ E1.5
- **E2.2** Diagrammi di flusso: simboli standard · [1] · ⟵ E2.1
- **E2.3** Pseudocodice · [1] · ⟵ E2.1
- **E2.4** Programmazione a blocchi come rappresentazione eseguibile · [1] · ⟵ E2.2 · ⟶ G2.1
- **E2.5** Simulare l'esecuzione a mano (tabella di traccia) · [1] · ⟵ E2.2, E4.1
- **E2.6** Strumenti per disegnare diagrammi di flusso eseguibili (Flowgorithm) · [1] · ⟵ E2.2 · (v1.1, approfondimento)

## E3 Costrutti di controllo
- **E3.1** Sequenza · [1] · ⟵ E1.6
- **E3.2** Selezione semplice e doppia · [1] · ⟵ E3.1, A2.1.2
- **E3.3** Selezione multipla; condizioni composte · [1] · ⟵ E3.2, A2.1.4
- **E3.4** Iterazione con condizione (ciclo con controllo in testa e in coda) · [1] · ⟵ E3.2
- **E3.5** Iterazione a conteggio (ciclo for) · [1] · ⟵ E3.4, E4.1
- **E3.6** Cicli annidati · [1–2] · ⟵ E3.5
- **E3.7** Terminazione dei cicli; cicli infiniti · [1–2] · ⟵ E3.4
- **E3.8** Teorema di Böhm-Jacopini; programmazione strutturata · [2] · ⟵ E3.4, E2.2
- **E3.9** Sottoprogrammi: funzioni, parametri, valore restituito · [1–2] · ⟵ E3.1, E1.2 · ⟶ G1
- **E3.10** Diagrammi di Nassi-Shneiderman · [2] · ⟵ E3.8 · (v1.1, approfondimento)
- **E3.11** Programmare un personaggio con sequenze, scelte e ripetizioni (giochi di coding) · [1] · ⟵ E3.4 · (v1.1, approfondimento)
- **E3.12** Tabelline e schemi numerici stampati con i cicli · [1] · ⟵ E3.5 · (v1.1, approfondimento)
- **E3.13** Cicli infiniti voluti: il ciclo principale di un gioco o di un dispositivo · [1–2] · ⟵ E3.7 · (v1.1, approfondimento)
- **E3.14** Disegnare figure con i caratteri: triangoli, scacchiere, rombi · [1] · ⟵ E3.6 · (v1.1, approfondimento)

## E4 Variabili, tipi, espressioni
- **E4.1** La variabile come contenitore con nome; assegnazione · [1] · ⟵ E1.6
- **E4.2** Tipi elementari: intero, reale, booleano, carattere, stringa · [1] · ⟵ E4.1, B2.1.2, B4.2
- **E4.3** Espressioni aritmetiche, relazionali e logiche; precedenza degli operatori · [1] · ⟵ E4.2, A2.1.4
- **E4.4** Input e output · [1] · ⟵ E4.1
- **E4.5** Costanti; contatori e accumulatori · [1] · ⟵ E4.1, E3.4
- **E4.6** Scambio di due variabili; misconcezioni sull'assegnazione · [1] · ⟵ E4.1 · ⟶ W4
- **E4.7** Tipi composti: array e record · [1–2] · ⟵ E4.2
- **E4.8** Nomi delle variabili e convenzioni di scrittura (camelCase, snake_case) · [1] · ⟵ E4.1 · (v1.1, approfondimento)
- **E4.9** La congettura di Collatz (3n+1) esplorata con un programma · [1–2] · ⟵ E3.4 · (v1.1, approfondimento)
- **E4.10** Variabili nei fogli di calcolo e nei programmi: somiglianze e differenze · [1] · ⟵ E4.1, L2.2 · (v1.1, approfondimento)

## E5 Ricorsione
- **E5.1** Definizioni ricorsive: caso base e passo ricorsivo · [2] · ⟵ E3.9, A3.5
- **E5.2** Ricorsione sui numeri: fattoriale, Fibonacci, potenza · [2] · ⟵ E5.1, A4.2.1
- **E5.3** La pila delle chiamate e la traccia di esecuzione · [2] · ⟵ E5.2
- **E5.4** Ricorsione e iterazione: equivalenza, ricorsione di coda · [2–3] · ⟵ E5.3, E3.4
- **E5.5** Ricorsione su strutture: liste e alberi · [2] · ⟵ E5.2, E6.4.1
- **E5.6** Classici: torre di Hanoi, permutazioni, flood fill · [2] · ⟵ E5.2
- **E5.7** Dimostrare la correttezza per induzione · [3] · ⟵ E5.2, A2.3.4
- **E5.8** Memoizzazione · [2–3] · ⟵ E5.2, E6.5.1

## E6 Strutture dati

### E6.1 Array e matrici
- **E6.1.1** Array: accesso per indice, lunghezza · [1] · ⟵ E4.7
- **E6.1.2** Scorrere un array: somma, massimo, conteggio · [1] · ⟵ E6.1.1, E3.5, E4.5
- **E6.1.3** Array dinamici (le liste di Python); crescita ammortizzata · [2] · ⟵ E6.1.1
- **E6.1.4** Matrici e array multidimensionali · [1–2] · ⟵ E6.1.2, E3.6
- **E6.1.5** Stringhe come sequenze di caratteri · [1] · ⟵ E6.1.1, B4.2
- **E6.1.6** Dizionari (array associativi): uso · [1–2] · ⟵ E6.1.1
- **E6.1.7** Media mobile sui dati di un sensore · [2] · ⟵ E6.1.2 · (v1.1, approfondimento)

### E6.2 Liste collegate
- **E6.2.1** Nodi e riferimenti; lista semplice · [2] · ⟵ E4.7
- **E6.2.2** Inserimento e cancellazione; confronto con l'array · [2] · ⟵ E6.2.1, E6.1.3
- **E6.2.3** Liste doppie e circolari · [2] · ⟵ E6.2.2

### E6.3 Pile e code
- **E6.3.1** Pila (LIFO): push e pop · [2] · ⟵ E6.1.1
- **E6.3.2** Coda (FIFO); buffer circolare · [2] · ⟵ E6.1.1, A1.4.1
- **E6.3.3** Coda a doppio ingresso (deque) · [2] · ⟵ E6.3.1, E6.3.2
- **E6.3.4** Applicazioni: parentesi bilanciate, notazione polacca inversa, annulla/ripeti · [2] · ⟵ E6.3.1
- **E6.3.5** Tipo di dato astratto: interfaccia e implementazione · [2] · ⟵ E6.3.1, E6.3.2 · ⟶ G3.2
- **E6.3.6** Code con priorità nella vita quotidiana: il triage · [2] · ⟵ E6.3.2 · (v1.1, approfondimento)

### E6.4 Alberi
- **E6.4.1** Alberi: terminologia e rappresentazione · [2] · ⟵ A4.3.3, E6.2.1
- **E6.4.2** Alberi binari; visite in preordine, simmetrica, in postordine e per livelli · [2] · ⟵ E6.4.1, E5.1
- **E6.4.3** Alberi binari di ricerca: ricerca, inserimento, cancellazione · [2–3] · ⟵ E6.4.2, E7.1.3
- **E6.4.4** Alberi bilanciati: AVL, rosso-neri · [3] · ⟵ E6.4.3, E9.3
- **E6.4.5** Heap e code con priorità · [2–3] · ⟵ E6.4.2
- **E6.4.6** Trie · [3] · ⟵ E6.4.1, E6.1.5
- **E6.4.7** B-tree e B+tree · [3] · ⟵ E6.4.4 · ⟶ L6
- **E6.4.8** Alberi di espressioni e alberi sintattici · [2–3] · ⟵ E6.4.2 · ⟶ G7
- **E6.4.9** Insiemi disgiunti (union-find) · [3] · ⟵ E6.4.1

### E6.5 Tabelle hash
- **E6.5.1** Funzione hash: dal valore all'indice · [2] · ⟵ E6.1.1, A1.4.1
- **E6.5.2** Collisioni: liste di trabocco, indirizzamento aperto · [2–3] · ⟵ E6.5.1, A4.1.4
- **E6.5.3** Fattore di carico e rehashing · [3] · ⟵ E6.5.2
- **E6.5.4** Insiemi e dizionari implementati con hash · [2] · ⟵ E6.5.1

### E6.6 Rappresentazione dei grafi
- **E6.6.1** Matrice di adiacenza · [2] · ⟵ A4.3.1, E6.1.4
- **E6.6.2** Liste di adiacenza · [2] · ⟵ A4.3.1, E6.1.6
- **E6.6.3** Quale rappresentazione per grafi densi e sparsi · [3] · ⟵ E6.6.1, E6.6.2, E9.2

### E6.7 Strutture probabilistiche
- **E6.7.1** Filtri di Bloom · [3] · ⟵ E6.5.1, A7.2.3
- **E6.7.2** Skip list · [3] · ⟵ E6.2.2, A7.2.2
- **E6.7.3** Sketch per flussi di dati (Count-Min, HyperLogLog) · [4] · ⟵ E6.7.1

### E6.8 Strutture persistenti e immutabili *(nuovo in v1.0)*
- **E6.8** Strutture dati persistenti (condivisione strutturale) · [3–4] · ⟵ E6.4.2 · ⟶ G3.3

## E7 Algoritmi fondamentali

### E7.1 Ricerca
- **E7.1.1** Ricerca lineare · [1] · ⟵ E6.1.2
- **E7.1.2** Ricerca del massimo e del minimo; ricerca con sentinella · [1] · ⟵ E7.1.1
- **E7.1.3** Ricerca binaria su un array ordinato · [1–2] · ⟵ E7.1.1
- **E7.1.4** Ricerca binaria sulla risposta (bisezione) · [3] · ⟵ E7.1.3
- **E7.1.5** Il secondo massimo e il valore più frequente · [1–2] · ⟵ E7.1.2 · (v1.1, approfondimento)
- **E7.1.6** Cercare nel mondo reale: indici, rubriche, dizionari cartacei · [1] · ⟵ E7.1.1 · (v1.1, approfondimento)
- **E7.1.7** Contare i confronti della ricerca lineare nel caso peggiore · [1–2] · ⟵ E7.1.1 · (v1.1, approfondimento)
- **E7.1.8** Indovina il numero: la strategia migliore · [1–2] · ⟵ E7.1.3 · (v1.1, approfondimento)

### E7.2 Ordinamento
- **E7.2.1** Il problema dell'ordinamento; stabilità e ordinamento in loco · [1] · ⟵ E6.1.2
- **E7.2.2** Ordinamento per selezione (selection sort) · [1] · ⟵ E7.2.1, E7.1.2
- **E7.2.3** Bubble sort · [1] · ⟵ E7.2.1
- **E7.2.4** Ordinamento per inserimento (insertion sort) · [1–2] · ⟵ E7.2.1
- **E7.2.5** Merge sort · [2] · ⟵ E7.2.1, E5.2, E8.2
- **E7.2.6** Quick sort; scelta del pivot · [2–3] · ⟵ E7.2.1, E5.2, E8.2
- **E7.2.7** Heap sort · [3] · ⟵ E6.4.5
- **E7.2.8** Ordinamenti non basati su confronti: counting, radix, bucket · [3] · ⟵ E7.2.1, E6.1.1
- **E7.2.9** Limite inferiore Ω(n log n) per l'ordinamento per confronti · [3] · ⟵ E7.2.5, E9.3
- **E7.2.10** Fusione di sequenze ordinate · [2] · ⟵ E7.2.1
- **E7.2.11** Visualizzare gli algoritmi di ordinamento (animazioni, danze) · [2] · ⟵ E7.2.4 · (v1.1, approfondimento)
- **E7.2.12** Ordinare dati composti: chiavi di ordinamento e stabilità in pratica · [2] · ⟵ E7.2.4 · (v1.1, approfondimento)

### E7.3 Algoritmi sui grafi
- **E7.3.1** Visita in ampiezza (BFS); cammini minimi non pesati · [2] · ⟵ E6.6.2, E6.3.2
- **E7.3.2** Visita in profondità (DFS); componenti connesse · [2] · ⟵ E6.6.2, E6.3.1, E5.1
- **E7.3.3** Ordinamento topologico · [2–3] · ⟵ E7.3.2, A4.3.4
- **E7.3.4** Algoritmo di Dijkstra · [3] · ⟵ E7.3.1, E6.4.5
- **E7.3.5** Bellman-Ford e Floyd-Warshall · [3] · ⟵ E7.3.4, E8.5
- **E7.3.6** Alberi ricoprenti minimi: Kruskal e Prim · [3] · ⟵ E6.4.9, E8.3
- **E7.3.7** Flusso massimo (Ford-Fulkerson) · [3–4] · ⟵ E7.3.1
- **E7.3.8** Componenti fortemente connesse · [3] · ⟵ E7.3.2
- **E7.3.9** Ricerca informata A* ed euristiche ammissibili · [3] · ⟵ E7.3.4

### E7.4 Algoritmi su stringhe
- **E7.4.1** Ricerca ingenua di una sottostringa · [1–2] · ⟵ E6.1.5, E3.6
- **E7.4.2** Knuth-Morris-Pratt e Boyer-Moore · [3] · ⟵ E7.4.1, E9.2
- **E7.4.3** Rabin-Karp e hash di stringhe · [3] · ⟵ E7.4.1, E6.5.1
- **E7.4.4** Distanza di edit (Levenshtein) · [3] · ⟵ E8.5
- **E7.4.5** Più lunga sottosequenza comune · [3] · ⟵ E8.5
- **E7.4.6** Espressioni regolari come strumento pratico di ricerca · [2] · ⟵ E6.1.5 · ⟶ F1
- **E7.4.7** Array e alberi dei suffissi · [4] · ⟵ E7.2.6, E6.4.6

### E7.5 Algoritmi numerici e geometrici elementari
- **E7.5.1** Algoritmi aritmetici: Euclide, potenza veloce, crivello · [1–2] · ⟵ A1.3.4, E3.4
- **E7.5.2** Numeri casuali nei programmi; simulazioni semplici · [1–2] · ⟵ E3.5
- **E7.5.3** Moltiplicazione di interi grandi (Karatsuba) · [3] · ⟵ E8.2, B2.6.3
- **E7.5.4** Moltiplicazione di matrici; algoritmo di Strassen · [3–4] · ⟵ A5.1.6, E8.2
- **E7.5.5** Geometria elementare: intersezione di segmenti, punto in un poligono · [2–3] · ⟵ A5.1.4
- **E7.5.6** Numeri perfetti, amicabili e congettura di Goldbach · [1–2] · ⟵ E7.5.1 · (v1.1, approfondimento)
- **E7.5.7** Semplificare frazioni con il massimo comune divisore · [1] · ⟵ E7.5.1 · (v1.1, approfondimento)

## E8 Tecniche di progetto
- **E8.1** Forza bruta ed enumerazione · [1–2] · ⟵ E3.6
- **E8.2** Divide et impera · [2] · ⟵ E5.2
- **E8.3** Algoritmi greedy e quando funzionano · [2–3] · ⟵ E7.2.1
- **E8.4** Backtracking (N regine, sudoku) · [2–3] · ⟵ E5.6
- **E8.5** Programmazione dinamica: sottostruttura ottima, tabelle · [3] · ⟵ E5.8, E8.2
- **E8.6** Branch and bound · [3] · ⟵ E8.4
- **E8.7** Ridurre un problema a un altro già risolto · [3] · ⟵ E8.1 · ⟶ F4, F5

## E9 Analisi degli algoritmi
- **E9.1** Correttezza: pre- e post-condizioni, invarianti di ciclo · [2–3] · ⟵ E3.4, A2.3.6
- **E9.2** Costo di un algoritmo: contare le operazioni · [1–2] · ⟵ E3.6
- **E9.3** Notazioni asintotiche O, Ω, Θ · [2–3] · ⟵ E9.2, A1.2.6, A6.1.3
- **E9.4** Caso migliore, peggiore e medio · [2–3] · ⟵ E9.3, A7.3.2
- **E9.5** Costo degli algoritmi ricorsivi ed equazioni di ricorrenza · [3] · ⟵ E9.3, A4.2.4, E5.2
- **E9.6** Complessità spaziale · [2–3] · ⟵ E9.3
- **E9.7** Analisi ammortizzata · [3] · ⟵ E9.3, E6.1.3
- **E9.8** Misurare sperimentalmente i tempi · [2] · ⟵ E9.2 · ⟶ I12
- **E9.9** Problemi trattabili e intrattabili (panoramica intuitiva) · [2] · ⟵ E9.3 · ⟶ F5
- **E9.10** Tempi di esecuzione reali: dai microsecondi ai secoli · [2] · ⟵ E9.2, A1.2.6 · (v1.1, approfondimento)
- **E9.11** Il commesso viaggiatore giocato a mano · [2] · ⟵ A1.2.6 · (v1.1, approfondimento)

## E10 Algoritmi randomizzati, approssimati, online e di streaming
- **E10.1** Algoritmi randomizzati: Las Vegas e Monte Carlo · [3–4] · ⟵ E9.4, A7.3.2
- **E10.2** Algoritmi di approssimazione; rapporto di approssimazione · [4] · ⟵ E8.3, F5.4
- **E10.3** Algoritmi online; analisi competitiva · [4] · ⟵ E9.3
- **E10.4** Algoritmi per flussi di dati · [4] · ⟵ E6.7.3
- **E10.5** Algoritmi parametrizzati ed esatti esponenziali · [4] · ⟵ F5.4
- **E10.6** Algoritmi per memoria esterna e cache-oblivious · [4] · ⟵ E9.3, D8

## E11 Algoritmi paralleli e distribuiti
- **E11.1** Modelli di calcolo parallelo (PRAM; lavoro e profondità) · [3–4] · ⟵ E9.3
- **E11.2** Riduzione e scan paralleli · [3–4] · ⟵ E11.1, A4.4.1
- **E11.3** Ordinamento parallelo · [4] · ⟵ E11.1, E7.2.5
- **E11.4** Algoritmi distribuiti: elezione del leader, diffusione · [4] · ⟵ E7.3.1, E11.1
- **E11.5** MapReduce come schema algoritmico · [3] · ⟵ E11.2 · ⟶ L8

## E12 Geometria computazionale
- **E12.1** Primitive: orientamento di tre punti, intersezioni · [3] · ⟵ E7.5.5
- **E12.2** Inviluppo convesso (Graham, Jarvis) · [3] · ⟵ E12.1, E7.2.5
- **E12.3** Tecnica della linea di scansione (sweep line) · [3–4] · ⟵ E12.1, E6.4.4
- **E12.4** Triangolazione di Delaunay e diagrammi di Voronoi · [4] · ⟵ E12.2
- **E12.5** Strutture per ricerche spaziali (k-d tree, quadtree) · [3–4] · ⟵ E6.4.3, A5.1.3 · ⟶ Q2, S6
