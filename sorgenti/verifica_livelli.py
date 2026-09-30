# (anno, n, titolo-argomenti, [nodi core], tipo)  tipo: N normale, P prova di corte
L = {}
L[1] = [
 ("Informazione, dato, messaggio", ["B1.1"], "N"),
 ("Analogico e digitale", ["B1.2","B1.3"], "N"),
 ("Il bit", ["B1.4","B1.5","B1.6"], "N"),
 ("Sistemi di numerazione posizionali", ["B2.1.1"], "N"),
 ("Conversioni binario ↔ decimale", ["B2.1.2","B2.1.3","B2.1.4","B2.1.5"], "N"),
 ("Ottale ed esadecimale", ["B2.2.1","B2.2.2","B2.2.3"], "N"),
 ("Unità di misura: bit, byte, prefissi SI e IEC", ["B3.1","B3.2","B3.3","B3.4"], "N"),
 ("Aritmetica binaria e overflow", ["B2.3.1","B2.3.2","B2.3.4","B2.3.5"], "N"),
 ("Codifica del testo: ASCII", ["B4.1","B4.2"], "N"),
 ("Prova di corte: codifiche e cifrario di Cesare ★", ["N2.1","N2.2"], "P"),
 ("Unicode e UTF-8", ["B4.3","B4.4","B4.5"], "N"),
 ("Colori: RGB e notazione esadecimale", ["B5.1.2","B5.2.1","B5.3.1","B5.3.3"], "N"),
 ("Immagini raster: pixel e risoluzione", ["B6.1","B6.2","B6.3"], "N"),
 ("Hardware e software", ["C11.1","D4.1","C4.1","C4.5"], "N"),
 ("La macchina di von Neumann: CPU, memoria, bus", ["D4.2","D5.1","U1.1","U1.3","U1.4","U1.7","U1.9","U1.10","U1.11","U1.13"], "N"),
 ("Il ciclo fetch-decode-execute", ["D5.2"], "N"),
 ("Memorie: RAM, dischi, SSD, gerarchia di memoria", ["C10.1","C10.4","D8.1","D8.2"], "N"),
 ("Periferiche e bus", ["C11.2","C11.3","C11.5","C11.6","D9.1"], "N"),
 ("Porte logiche e algebra di Boole ★", ["A2.1.2","A2.1.3","A2.1.4","D1.1","D1.2","D1.3"], "N"),
 ("Prova di corte: assemblare un calcolatore (scelta dei componenti, prestazioni, consumi)", ["C13.1"], "P"),
 ("Il sistema operativo: funzioni e sistemi più comuni", ["I1.1","I1.2","I7.2","I7.3","I8.1","I8.2","I8.3","I8.4","U1.12","U1.15"], "N"),
 ("Processi e scheduling", ["I2.1","I2.5"], "N"),
 ("Gestione della memoria", ["I4.1"], "N"),
 ("File system: cartelle, percorsi, permessi, backup", ["I5.1","I5.2","I5.4","I7.1","I11.3"], "N"),
 ("Il documento elettronico: struttura e stili", ["B13.1"], "N"),
 ("Foglio elettronico: celle, formule, riferimenti relativi e assoluti", ["L2.1","L2.2","L2.5"], "N"),
 ("Foglio elettronico: funzioni, grafici, statistica descrittiva; quantità d'informazione di un evento ★", ["L2.3","L2.4","A7.1.4","A8.1.1"], "N"),
 ("Internet: struttura e servizi", ["J2.1","J2.2","J8.1","K1.1","K1.2","K1.3"], "N"),
 ("Cercare e valutare le fonti; regole e sicurezza in rete; l'IA come fonte ★", ["U7.1","U7.2","U7.3","N9.1","N9.2","N9.3","N5.1","N5.2","U4.2","L11.8","O1.1","O1.6","O6.4","O6.5"], "N"),
 ("Prova finale dell'anno: inventario (foglio elettronico, codifiche, hardware)", [], "P"),
]
L[2] = [
 ("Pensiero computazionale: scomporre un problema", ["E1.1","E1.2","E1.3","E1.4"], "N"),
 ("Che cos'è un algoritmo", ["E1.5","E1.6","E1.8"], "N"),
 ("Diagrammi di flusso", ["E2.1","E2.2"], "N"),
 ("Pseudocodice", ["E2.3"], "N"),
 ("Variabili, tipi, assegnazione", ["E4.1","E4.2","E4.4","E4.6","E2.5"], "N"),
 ("Espressioni e operatori logici", ["E4.3"], "N"),
 ("Sequenza, selezione, iterazione (Böhm-Jacopini)", ["E3.1","E3.2","E3.3","E3.4","E3.5","E3.7","E3.8"], "N"),
 ("Tipologie di linguaggi: livelli, compilati e interpretati, breve storia", ["G1.1","G1.2","G7.1.1","G9.1"], "N"),
 ("Il primo linguaggio (Python): input, output, sintassi", ["G2.2.1","G2.2.2","G1.3","G1.4","G1.5","G1.6","G1.11"], "N"),
 ("Prova di corte: tracing di programmi", [], "P"),
 ("Selezione: if, elif, else", ["G1.7","G2.2.3"], "N"),
 ("Iterazione: while, contatori, accumulatori", ["E4.5"], "N"),
 ("Iterazione: for e range", ["E3.5"], "N"),
 ("Cicli annidati", ["E3.6"], "N"),
 ("Algoritmi classici: massimo, minimo, somma, media", ["E6.1.1","E6.1.2","E7.1.2"], "N"),
 ("Algoritmo di Euclide e numeri primi", ["E7.5.1"], "N"),
 ("Funzioni: definizione, parametri, valore di ritorno", ["E3.9","G1.8","G2.2.7"], "N"),
 ("Visibilità e scomposizione in funzioni", ["G1.9","G1.10","G3.1.1","G3.1.2"], "N"),
 ("Test e debugging", ["G1.12","H6.1","H6.2"], "N"),
 ("Prova di corte: problemi con funzioni", [], "P"),
 ("Liste e array", ["G2.2.5","E6.1.3","E6.1.6"], "N"),
 ("Ricerca lineare", ["E7.1.1"], "N"),
 ("Stringhe e testo", ["E6.1.5","G2.2.4"], "N"),
 ("Cifrari di Cesare e di Vigenère in codice ★", ["N2.3","N2.4","N2.6","N2.7"], "N"),
 ("Grafica con la tartaruga", ["Q1.1","Q1.2","G2.2.12"], "N"),
 ("Il caso: dadi, frequenze, probabilità simulate ★", ["A7.2.1","A7.2.2","A7.2.3","E7.5.2","S1.1","A7.1.6"], "N"),
 ("Foglio elettronico avanzato: SE, CERCA, tabelle pivot", ["L2.6","L2.7"], "N"),
 ("Come è fatta Internet: indirizzi, DNS, pacchetti", ["J2.4","J5.1","J7.1"], "N"),
 ("Collaborare in rete: cloud, posta elettronica, privacy, diritto d'autore", ["M4.8","Q13.1","U4.1","U4.3","U4.5","U7.7"], "N"),
 ("Prova finale dell'anno: generare una pianta rispettando vincoli", [], "P"),
]
L[3] = [
 ("Interi con segno e complemento a 2", ["B2.4.1","B2.4.2","B2.4.3","B2.4.4","B2.4.5"], "N"),
 ("Virgola mobile (IEEE 754) ed errori di rappresentazione", ["B2.1.6","B2.5.1","B2.5.2","B2.5.3","B2.5.5"], "N"),
 ("Array e matrici", ["E6.1.4"], "N"),
 ("Ordinamento: selection sort e bubble sort", ["E7.2.1","E7.2.2","E7.2.3"], "N"),
 ("Ordinamento: insertion sort; confronti e scambi", ["E7.2.4"], "N"),
 ("Ricerca binaria; logaritmi ★", ["E7.1.3","A1.2.5"], "N"),
 ("Contare i passi: complessità intuitiva", ["E9.2","A1.2.6","E9.8"], "N"),
 ("Ricorsione", ["E5.1","E5.2","E5.3","E5.6","E5.8"], "N"),
 ("Divide et impera: merge sort ★", ["E8.2","E7.2.5","E7.2.10","E8.5"], "N"),
 ("Prova di corte: ordinare e contare i passi", [], "P"),
 ("Stringhe avanzate e ricerca di schemi; automi ★", ["E7.4.1","E7.4.6","F1.1","F1.3","E6.5.1"], "N"),
 ("File e CSV", ["B11.1","B11.2","G1.13","G1.14","G2.2.9"], "N"),
 ("Metodologie di programmazione: top-down e modularità", ["G1.15","H4.1","H4.2"], "N"),
 ("Documentazione, stile, controllo di versione (Git) ★", ["H5.1","H5.2","H5.7","H8.2","H8.3"], "N"),
 ("Formati di immagine: bitmap e vettoriale", ["B6.4","B6.5","B6.6"], "N"),
 ("Compressione senza perdita: RLE e Huffman", ["B9.1.1","B9.1.2","B9.1.3","B9.1.4","B9.1.5"], "N"),
 ("Audio digitale: campionamento e quantizzazione", ["B7.2","B7.3","B7.4","B7.5","B7.6","B7.7"], "N"),
 ("Compressione con perdita: l'idea di JPEG e MP3", ["B9.2.1","B9.2.2","B9.2.5"], "N"),
 ("Linguaggi di markup: il concetto, Markdown", ["B13.5"], "N"),
 ("Prova di corte: formati, compressione, qualità", [], "P"),
 ("Font e tipografia digitale", ["B13.2","B13.3"], "N"),
 ("XML: elementi, attributi, buona formazione", ["B11.3","B11.4","B11.7"], "N"),
 ("HTML: struttura e semantica", ["K2.1","K2.2","K2.3","K2.4","K2.5","K2.6","K2.7","K2.8","K2.9"], "N"),
 ("SVG: la grafica vettoriale come testo", ["B6.7","K12.2"], "N"),
 ("CSS: selettori, box model, colori", ["K3.1","K3.2","K3.3","K3.4","K3.5"], "N"),
 ("Impaginazione e design responsive", ["K3.6","K3.7","K3.8"], "N"),
 ("Progettazione web: usabilità e accessibilità", ["Q8.1","Q8.2","Q8.3","K5.1","K5.2","K5.3","K5.4"], "N"),
 ("JavaScript di base: la pagina che reagisce ★", ["K4.1","K4.2","K4.3"], "N"),
 ("Pubblicare un sito; licenze e diritto d'autore", ["K8.1","K8.2","U4.4"], "N"),
 ("Prova finale dell'anno: un sito completo (testi marcati, immagini ottimizzate, stile)", [], "P"),
]
L[4] = [
 ("Astrazione: dal problema al modello", ["H3.1"], "N"),
 ("Pile e code", ["E6.3.1","E6.3.2","E6.3.3","E6.3.4","E6.3.5"], "N"),
 ("Classi e oggetti", ["G3.2.1","G2.2.11"], "N"),
 ("Attributi, metodi, costruttori", ["G3.2.2","G3.2.8"], "N"),
 ("Incapsulamento", ["G3.2.3"], "N"),
 ("Ereditarietà", ["G3.2.4","G3.2.7"], "N"),
 ("Polimorfismo e interfacce", ["G3.2.5","G3.2.6"], "N"),
 ("Diagramma UML delle classi", ["H3.2","H3.3"], "N"),
 ("Liste collegate e riferimenti ★", ["G4.1","G4.3","E6.2.1","E6.2.2","E6.2.3"], "N"),
 ("Prova di corte: modellare un sistema a oggetti", [], "P"),
 ("Implementare un linguaggio: compilatore e interprete", ["G7.1.1"], "N"),
 ("Analisi lessicale: i token", ["G7.1.2"], "N"),
 ("Grammatiche e sintassi (BNF)", ["F2.1","F2.2","F2.3"], "N"),
 ("Alberi sintattici e valutazione delle espressioni", ["E6.4.1","E6.4.2","E6.4.8","F2.5","G7.1.3","G7.1.5","E6.4.5"], "N"),
 ("Un mini-interprete: la calcolatrice ★", ["G7.3.1"], "N"),
 ("Dato, informazione, archivio: dagli archivi ai database", ["L1.1","L1.2","L1.3","L1.4"], "N"),
 ("Modello E/R: entità, attributi, relazioni", ["L3.1","L3.2"], "N"),
 ("Cardinalità e vincoli", ["L3.3","L3.4","L3.6"], "N"),
 ("Modello relazionale: tabelle e chiavi", ["L4.1","L4.2","L4.3"], "N"),
 ("Prova di corte: progettare uno schema E/R", [], "P"),
 ("Dallo schema E/R allo schema relazionale", ["L4.4"], "N"),
 ("Normalizzazione (fino alla 3FN) ★", ["L4.6","L4.7"], "N"),
 ("Algebra relazionale: selezione, proiezione, join", ["L4.5"], "N"),
 ("SQL: creare e modificare (DDL e DML)", ["L5.1","L5.2","L6.8"], "N"),
 ("SQL: SELECT, WHERE, ORDER BY", ["L5.3","L5.7"], "N"),
 ("SQL: JOIN", ["L5.4","L5.6"], "N"),
 ("SQL: aggregazioni e GROUP BY", ["L5.5","L5.8"], "N"),
 ("Database e programmi: SQL da Python ★", ["L5.12"], "N"),
 ("Privacy, GDPR, open data", ["L10.1","L10.2","L10.6"], "N"),
 ("Prova finale dell'anno: database più applicazione a oggetti", [], "P"),
]
L[5] = [
 ("Errori numerici e approssimazione", ["A10.1.1","A10.1.2"], "N"),
 ("Zeri di funzione: il metodo di bisezione", ["A10.2.1"], "N"),
 ("Il metodo di Newton ★", ["A6.2.2"], "N"),
 ("Aree sotto una curva: rettangoli e trapezi", ["A10.2.3"], "N"),
 ("Stimare π con il metodo Monte Carlo", ["S1.3"], "N"),
 ("Successioni e ricorrenze: approssimare √2", ["A4.2.1","A4.2.2","A6.1.5"], "N"),
 ("Simulazione a tempo discreto: il moto (metodo di Eulero)", ["A6.4.1","A6.4.4","S1.2","S1.4"], "N"),
 ("Oscillatori e attrito", ["A6.4.2","S5.1"], "N"),
 ("Modelli di popolazione e di epidemia", ["S14.1","S14.4","S1.5"], "N"),
 ("Prova di corte: simulazione di un fenomeno e confronto con le fonti", ["S1.6"], "P"),
 ("Confrontare un modello con i dati: minimi quadrati; apprendimento supervisionato ★", ["A7.1.5","O4.1.4"], "N"),
 ("Automi a stati finiti", ["F1.2","F1.9"], "N"),
 ("La macchina di Turing", ["F3.1","F3.2","F3.3","F3.5"], "N"),
 ("Calcolabilità: il problema della fermata", ["F4.1","F4.2","F4.7"], "N"),
 ("Complessità: P e NP in modo intuitivo", ["E9.3","E9.9","F5.5"], "N"),
 ("Reti: tipi, topologie, commutazione", ["J1.1","J1.2","J1.6","J2.3","J2.5","J2.6","E6.6.2","E7.3.1"], "N"),
 ("Modelli a strati: ISO/OSI e TCP/IP", ["J3.2","J3.3","J3.4","J3.5"], "N"),
 ("Livello fisico e di collegamento: Ethernet, Wi-Fi, errori", ["J4.1","J4.2","J4.3","J4.4","J4.5","J4.6","J4.9","B10.1.1","B10.1.2","B10.1.4"], "N"),
 ("Indirizzi IP e subnetting", ["J5.2","J5.3","J5.6","J5.7"], "N"),
 ("Prova di corte: progettare la rete di un edificio (componenti, configurazione, prestazioni)", ["J5.4","J5.9"], "P"),
 ("Instradamento e grafi: l'algoritmo di Dijkstra", ["E7.3.4","J5.5"], "N"),
 ("TCP, UDP e porte", ["J6.3","J6.4","J6.5"], "N"),
 ("Servizi di rete: DNS, HTTP, posta elettronica", ["J7.2","J7.3","J7.5"], "N"),
 ("Sicurezza in rete: crittografia asimmetrica e HTTPS", ["N3.3.1","N3.3.2","N3.3.3","N3.4.1","N3.4.2","J7.4","N4.1"], "N"),
 ("Prestazioni: banda, latenza, throughput; mantenere l'efficienza", ["I12.1","I12.2","J8.5","I11.2"], "N"),
 ("Intelligenza artificiale: imparare dai dati ★", ["O4.1.1","O4.1.2","O4.1.3","O4.3.1","O4.3.3","O4.2.1"], "N"),
 ("Reti neurali in modo intuitivo ★", ["O5.1.1","O5.1.2","O5.1.3"], "N"),
 ("IA generativa: limiti, etica, AI Act ★", ["O6.1","O10.1","O10.3","U3.2","U3.6","U4.8"], "N"),
 ("L'informatica e il metodo scientifico: la nascita di nuove scienze", ["U2.1","U2.6"], "N"),
 ("Prova finale dell'anno: un progetto di simulazione scientifica completo", ["S1.7"], "P"),
]
# nuovi nodi di approfondimento da aggiungere alla mappa: id, titolo, livello, prerequisiti, inserisci_dopo
NUOVI = [
("B1.7","Vantaggi e limiti del digitale: copie identiche, robustezza al rumore, obsolescenza dei supporti","1","B1.3","B1.6"),
("B1.8","Strumenti analogici e digitali a confronto (orologi, termometri, dischi in vinile e streaming)","1","B1.2","B1.7"),
("B1.9","Il gioco delle venti domande: dimezzare le possibilità","1","B1.5","B1.8"),
("B1.10","Segnalazioni a due simboli nella storia (fuochi, bandiere, telegrafo)","1","B1.4","B1.9"),
("B2.1.7","Sistemi di numerazione di altre culture: babilonese (base 60), maya (base 20)","1","B2.1.1","B2.1.6"),
("B2.1.8","Tracce di altre basi nella vita quotidiana: ore, minuti, dozzine","1","B2.1.1","B2.1.7"),
("B2.2.4","La codifica Base64: dati binari scritti come testo","1–2","B2.2.2","B2.2.3"),
("B2.4.7","Errori famosi dovuti all'overflow (Ariane 5, problema dell'anno 2038)","2","B2.4.4","B2.4.6"),
("B3.5","La crescita delle capacità di memoria nel tempo: dal kilobyte al petabyte","1","B3.2","B3.4"),
("B4.11","Codici storici per il testo: Morse, Baudot, EBCDIC","1","B4.1","B4.10"),
("B4.12","L'arte ASCII","1","B4.2","B4.11"),
("B6.10","Pixel art e sprite per videogiochi","1–2","B6.6","B6.9"),
("B9.1.6","Formati d'archivio: ZIP, 7z, tar","2","B9.1.4","B9.1.5"),
("B9.2.7","Esperimenti di ascolto e di visione con diversi livelli di compressione","2","B9.2.5","B9.2.6"),
("B11.10","Aprire dati pubblici in formato CSV (ISTAT, portali open data)","2","B11.2","B11.9"),
("B13.9","Revisione e collaborazione sui documenti: commenti, revisioni, versioni","1","B13.1","B13.8"),
("B13.10","Wiki e markup per la scrittura collaborativa","2","B13.5","B13.9"),
("B13.11","Storia della tipografia: da Gutenberg ai caratteri digitali","1–2","B13.2","B13.10"),
("B13.12","Caratteri e leggibilità: font ad alta leggibilità","2","B13.2","B13.11"),
("N2.9","Steganografia: nascondere l'esistenza di un messaggio","1","N2.1","N2.8"),
("N2.10","Cifrari del Rinascimento: il disco di Leon Battista Alberti","1–2","N2.4","N2.9"),
("E1.9","Rompicapi e giochi di logica come problemi computazionali (labirinti, travasi)","1","E1.2","E1.8"),
("E2.6","Strumenti per disegnare diagrammi di flusso eseguibili (Flowgorithm)","1","E2.2","E2.5"),
("E3.10","Diagrammi di Nassi-Shneiderman","2","E3.8","E3.9"),
("E3.11","Programmare un personaggio con sequenze, scelte e ripetizioni (giochi di coding)","1","E3.4","E3.10"),
("E3.12","Tabelline e schemi numerici stampati con i cicli","1","E3.5","E3.11"),
("E3.13","Cicli infiniti voluti: il ciclo principale di un gioco o di un dispositivo","1–2","E3.7","E3.12"),
("E3.14","Disegnare figure con i caratteri: triangoli, scacchiere, rombi","1","E3.6","E3.13"),
("E4.8","Nomi delle variabili e convenzioni di scrittura (camelCase, snake_case)","1","E4.1","E4.7"),
("E4.9","La congettura di Collatz (3n+1) esplorata con un programma","1–2","E3.4","E4.8"),
("E6.1.7","Media mobile sui dati di un sensore","2","E6.1.2","E6.1.6"),
("E6.3.6","Code con priorità nella vita quotidiana: il triage","2","E6.3.2","E6.3.5"),
("E7.1.5","Il secondo massimo e il valore più frequente","1–2","E7.1.2","E7.1.4"),
("E7.1.6","Cercare nel mondo reale: indici, rubriche, dizionari cartacei","1","E7.1.1","E7.1.5"),
("E7.1.7","Contare i confronti della ricerca lineare nel caso peggiore","1–2","E7.1.1","E7.1.6"),
("E7.1.8","Indovina il numero: la strategia migliore","1–2","E7.1.3","E7.1.7"),
("E7.2.11","Visualizzare gli algoritmi di ordinamento (animazioni, danze)","2","E7.2.4","E7.2.10"),
("E7.2.12","Ordinare dati composti: chiavi di ordinamento e stabilità in pratica","2","E7.2.4","E7.2.11"),
("E7.5.6","Numeri perfetti, amicabili e congettura di Goldbach","1–2","E7.5.1","E7.5.5"),
("E7.5.7","Semplificare frazioni con il massimo comune divisore","1","E7.5.1","E7.5.6"),
("E9.10","Tempi di esecuzione reali: dai microsecondi ai secoli","2","E9.2, A1.2.6","E9.9"),
("E9.11","Il commesso viaggiatore giocato a mano","2","A1.2.6","E9.10"),
("F2.10","Grammatiche per generare frasi casuali","3","F2.1","F2.9"),
("G1.16","Selezione multipla con match/case","2","G1.7","G1.15"),
("G3.2.10","Metodi speciali in Python (__str__, __eq__)","2–3","G3.2.2","G3.2.9"),
("G3.2.11","Proprietà: getter, setter e @property","3","G3.2.3","G3.2.10"),
("G3.2.12","Oggetti immutabili e dataclass","3","G3.2.3","G3.2.11"),
("G3.2.13","Ereditarietà multipla e ordine di risoluzione dei metodi","3","G3.2.4","G3.2.12"),
("G3.2.14","Gerarchie di classi nella libreria standard: le eccezioni","3","G3.2.4, G1.14","G3.2.13"),
("G3.2.15","Progettare un gioco a oggetti: personaggi, oggetti, stanze","3","G3.2.5","G3.2.14"),
("G7.1.6","Esplorare il bytecode di Python (modulo dis)","3","G7.1.1","G7.1.5"),
("G7.1.7","Come funziona l'evidenziazione della sintassi negli editor","3","G7.1.2","G7.1.6"),
("G7.1.8","Suddividere in token un testo in italiano: parole, punteggiatura, apostrofi","3","G7.1.2","G7.1.7"),
("G7.3.6","Estendere la calcolatrice con variabili e funzioni","3–4","G7.3.1","G7.3.5"),
("H3.9","Diagrammi come codice (PlantUML, Mermaid)","3","H3.3","H3.8"),
("H5.8","Storia dei sistemi di controllo di versione","2","H5.1","H5.7"),
("K3.11","Temi chiari e scuri; variabili CSS","2–3","K3.2","K3.10"),
("K3.12","CSS per la stampa","2","K3.8","K3.11"),
("K12.6","Animare la grafica SVG","2–3","K12.2","K12.5"),
("K12.7","Progettare un'icona vettoriale","2","K12.2","K12.6"),
("L3.7","Strumenti per disegnare schemi E/R","2","L3.2","L3.6"),
("L3.8","Errori tipici negli schemi E/R e come correggerli","3","L3.4","L3.7"),
("L3.9","Confrontare schemi alternativi per lo stesso problema","3","L3.4","L3.8"),
("L4.10","Codd e la nascita del modello relazionale","2","L4.1","L4.9"),
("L4.11","Generare lo schema con uno strumento di progettazione","3","L4.4","L4.10"),
("L4.12","Schemi di database reali: negozio online, social network","3","L4.4","L4.11"),
("L4.13","Anomalie di inserimento, modifica, cancellazione in un foglio di calcolo reale","3","L4.7","L4.12"),
("L4.14","Calcolatori di algebra relazionale","3","L4.5","L4.13"),
("L4.15","Tradurre domande in linguaggio naturale in algebra relazionale","3","L4.5","L4.14"),
("Q1.8","Poligoni e stelle con la tartaruga: angoli esterni","1–2","Q1.2","Q1.7"),
("E4.10","Variabili nei fogli di calcolo e nei programmi: somiglianze e differenze","1","E4.1, L2.2","E4.9"),
("L5.13","Ricerca testuale in SQL: LIKE ed espressioni regolari","2–3","L5.3","L5.12"),
("L5.14","I join rappresentati con i diagrammi di Venn, e i limiti di questa rappresentazione","2","L5.4","L5.13"),
("L5.15","Self-join: una tabella collegata a se stessa (alberi genealogici)","3","L5.4","L5.14"),
("L5.16","Mediana e percentili in SQL","3","L5.5","L5.15"),
("L5.17","Riepiloghi in SQL e tabelle pivot a confronto","3","L5.5, L2.6","L5.16"),
("L5.18","Salvare i progressi di un gioco in SQLite","3","L5.12","L5.17"),
("L7.8","Quando le tabelle non bastano: panoramica dei database NoSQL","3","L4.1","L7.7"),
("L9.10","Cruscotti costruiti sui dati di un database","3","L5.5","L9.9"),
("A4.2.5","La successione di Fibonacci e il rapporto aureo","2–3","A4.2.1","A4.2.4"),
("A7.2.6","Il problema di Monty Hall simulato","2","A7.2.3","A7.2.5"),
("A10.1.4","Incidenti causati da errori numerici (missile Patriot)","3","A10.1.2","A10.1.3"),
("A10.1.5","Aritmetica esatta: frazioni e decimali a precisione arbitraria in Python","3","A10.1.2","A10.1.4"),
("A10.2.4","Metodo delle secanti e regula falsi","3","A10.2.1","A10.2.3"),
("A10.2.5","Il metodo di Erone per la radice quadrata come caso del metodo di Newton","3","A6.2.2","A10.2.4"),
("A10.2.6","Lunghezze di curve e volumi calcolati numericamente","3","A10.2.3","A10.2.5"),
("A10.2.7","Integrare numericamente dati sperimentali (dalla velocità allo spazio)","3","A10.2.3","A10.2.6"),
("S1.9","L'ago di Buffon","3","S1.3","S1.8"),
("S1.10","Il moto del proiettile con la resistenza dell'aria","3","S1.4","S1.9"),
("S1.11","Visualizzare traiettorie e risultati di una simulazione","3","S1.4","S1.10"),
("S1.12","Adattare curve non lineari ai dati (esponenziali, potenze)","3","A7.1.5","S1.11"),
("S1.13","Pubblicare i risultati di una simulazione: notebook e dati aperti","3","S1.7","S1.12"),
("S5.5","Il pendolo: piccole e grandi oscillazioni","3","S5.1","S5.4"),
("S5.6","La risonanza: dall'altalena ai ponti","3","A6.4.2","S5.5"),
("J3.6","Protocolli di comunicazione prima di Internet: telegrafo, telefono, X.25","2–3","J3.3","J3.5"),
("J5.10","IPv6 in pratica: gli indirizzi della propria rete","2–3","J5.7","J5.9"),
("I12.8","Misurare la propria connessione e il proprio computer: strumenti di benchmark","2","I12.2","I12.7"),
("O5.6","Sperimentare con una rete neurale nel browser (TensorFlow Playground)","3","O5.1.3","O5.5"),
("U2.9","Scienze nate con il calcolatore: bioinformatica, climatologia computazionale, scienze sociali computazionali","3","U2.6","U2.8"),
]
OPZ = {
"1-1":["B11.6","L1.5"],"1-2":["B1.7","B1.8"],"1-3":["B1.9","B1.10"],"1-4":["B2.1.7","B2.1.8"],"1-5":["B2.6.1","B2.6.2"],
"1-6":["B12.5","B2.2.4"],"1-7":["B2.6.4","B3.5"],"1-8":["B2.3.3","B2.6.3"],"1-9":["B4.11","B4.12"],"1-10":["N2.5","N2.9"],
"1-11":["B4.7","B4.8"],"1-12":["B5.2.2","B5.3.2"],"1-13":["B6.9","B8.1"],"1-14":["C1.10","C8.1"],"1-15":["U1.18","D4.3"],
"1-16":["D4.5","D6.1"],"1-17":["C10.6","C10.7"],"1-18":["D9.5","D9.2"],"1-19":["D2.2","D1.4"],"1-20":["C1.6","C13.2"],
"1-21":["I10.1","I7.5"],"1-22":["I2.4","I2.2"],"1-23":["D8.3","D4.4"],"1-24":["I11.1","I5.5"],"1-25":["B13.9","U11.1"],
"1-26":["B11.9","G10.3"],"1-27":["A7.2.5","B5.2.4"],"1-28":["J8.3","J8.4"],"1-29":["N5.3","O1.3"],"1-30":["U6.1","U9.1"],
"2-1":["E1.7","E1.9"],"2-2":["U1.2","R12.1"],"2-3":["E2.4","E2.6"],"2-4":["U1.5","U11.7"],"2-5":["E4.8","E4.10"],
"2-6":["A2.1.6","A2.2.1"],"2-7":["E3.10","E3.11"],"2-8":["G9.6","G9.2"],"2-9":["G5.8.4","G10.2"],"2-10":["H6.10","G6.1"],
"2-11":["G5.1.1","G1.16"],"2-12":["E4.9","G10.4"],"2-13":["E3.12","E3.13"],"2-14":["E8.1","E3.14"],"2-15":["E7.1.5","E6.1.7"],
"2-16":["E7.5.6","E7.5.7"],"2-17":["G5.11","L2.8"],"2-18":["G3.1.3","G3.3.1"],"2-19":["H1.3","H6.3"],"2-20":["H1.4","H11.1"],
"2-21":["G2.2.6","G2.2.8"],"2-22":["E7.1.6","E7.1.7"],"2-23":["B4.9","P3.1"],"2-24":["N2.8","N2.10"],"2-25":["Q14.1","Q1.8"],
"2-26":["A7.2.4","A7.2.6"],"2-27":["L8.5","V1.1"],"2-28":["J7.9","J14.1"],"2-29":["U4.10","U7.4"],"2-30":["U7.10","Q13.2"],
"3-1":["B2.4.6","B2.4.7"],"3-2":["B2.5.4","B2.5.6"],"3-3":["S11.2","E6.6.1"],"3-4":["E7.2.8","E8.3"],"3-5":["E7.2.11","E7.2.12"],
"3-6":["E7.1.4","E7.1.8"],"3-7":["E9.10","E9.11"],"3-8":["E5.4","E8.4"],"3-9":["E7.2.6","E7.4.4"],"3-10":["E7.4.5","E6.5.4"],
"3-11":["E7.4.3","E7.4.2"],"3-12":["B11.10","G5.8.1"],"3-13":["H4.7","H4.9"],"3-14":["H5.3","H5.8"],"3-15":["B6.10","S10.1"],
"3-16":["A8.1.4","A8.2.2"],"3-17":["Q6.1","Q6.2"],"3-18":["B9.2.7","A6.5.1"],"3-19":["B13.6","B13.10"],"3-20":["B9.1.6","Q4.1"],
"3-21":["B13.11","B13.12"],"3-22":["B11.5","B13.4"],"3-23":["K10.1","K12.1"],"3-24":["K12.6","K12.7"],"3-25":["K3.9","K3.11"],
"3-26":["K3.10","K3.12"],"3-27":["K5.6","Q8.10"],"3-28":["K4.4","K4.7"],"3-29":["K8.3","H8.4"],"3-30":["K5.7","Q8.4"],
"4-1":["H3.4","H3.5"],"4-2":["I2.6","E6.3.6"],"4-3":["G3.6.2","G5.4.1"],"4-4":["G8.1","G3.2.10"],"4-5":["G3.2.11","G3.2.12"],
"4-6":["G3.2.13","G3.2.14"],"4-7":["G3.2.9","G5.6.1"],"4-8":["H3.6","H3.9"],"4-9":["E6.7.2","G4.2"],"4-10":["H4.3","G3.2.15"],
"4-11":["G7.1.6","U1.14"],"4-12":["G7.1.7","G7.1.8"],"4-13":["F8.1","F2.10"],"4-14":["E6.4.3","E6.4.6"],"4-15":["G7.3.4","G7.3.6"],
"4-16":["L13.1","L9.1"],"4-17":["L3.7","L10.3"],"4-18":["L3.5","H3.7"],"4-19":["L6.1","L4.10"],"4-20":["L3.8","L3.9"],
"4-21":["L4.11","L4.12"],"4-22":["L4.8","L4.13"],"4-23":["L4.14","L4.15"],"4-24":["L5.9","L5.11"],"4-25":["L5.13","A2.6.2"],
"4-26":["L5.14","L5.15"],"4-27":["L5.16","L5.17"],"4-28":["L15.3","L5.18"],"4-29":["L15.4","U4.9"],"4-30":["L7.8","L9.10"],
"5-1":["A10.1.4","A10.1.5"],"5-2":["A10.1.3","A10.2.4"],"5-3":["A6.2.3","A10.2.5"],"5-4":["A10.2.6","A10.2.7"],"5-5":["S8.2","S1.9"],
"5-6":["A6.2.7","A4.2.5"],"5-7":["S1.10","S1.11"],"5-8":["S5.5","S5.6"],"5-9":["S14.2","S14.5"],"5-10":["A7.4.2","A7.4.6"],
"5-11":["O4.1.6","S1.12"],"5-12":["F1.4","F2.6"],"5-13":["F3.6","F10.1"],"5-14":["F4.3","A2.3.2"],"5-15":["E9.4","F5.1"],
"5-16":["E7.3.2","S9.1"],"5-17":["J6.7","J3.6"],"5-18":["J4.10","C14.3"],"5-19":["J5.8","J5.10"],"5-20":["J4.7","J4.11"],
"5-21":["E7.3.9","J8.2"],"5-22":["J6.6","J11.5"],"5-23":["J11.6","J12.2"],"5-24":["N3.2.3","N3.2.4"],"5-25":["I12.3","I12.8"],
"5-26":["O4.2.2","O4.2.5"],"5-27":["O5.4.1","O5.6"],"5-28":["O10.5","O4.3.6"],"5-29":["U2.7","U2.9"],"5-30":["S1.13","S14.3"],
}
import json, sys
from livelli import L
G = {n['id']: n for n in json.load(open('grafo-informatica.json'))['nodi']}
pre = {k: v['prereq_espansi'] for k, v in G.items()}
BASE = set()   # v1.1: nessuna competenza in ingresso presupposta; ciò che non è informatica viene costruito nel gioco
ALTRE = lambda n: n[0] in 'AC' or n.startswith('S2.1') or n.startswith('S3.1')   # altre discipline -> richiami
def closure(n, acc):
    for p in pre[n]:
        if p not in acc: acc.add(p); closure(p, acc)
    return acc
covered = set(BASE); rows = []
for anno in range(1, 6):
    for i, (t, core, tipo) in enumerate(L[anno], 1):
        for c in core: assert c in G, c
        need = set()
        for c in core: closure(c, need)
        missing = sorted(need - covered - set(core), key=lambda x: (x[0], [int(p) for p in x[1:].split('.')]))
        rows.append((anno, i, t, core, missing))
        covered |= set(core) | set(missing)
tot = 0
for a, i, t, core, miss in rows:
    if miss:
        tot += len(miss)
        info = [m for m in miss if not ALTRE(m)]; oth = [m for m in miss if ALTRE(m)]
        print(f"{a}-{i:02d} {t[:45]:45s} INF+{len(info)} {info} | RICH+{len(oth)} {oth}")
print("totale aggiunti", tot)
import json
from livelli import L
exec(open('analizza.py').read().split('covered = set(BASE)')[0])
covered=set(BASE); lv=[]
for anno in range(1,6):
    for i,(t,core,tipo) in enumerate(L[anno],1):
        need=set()
        for c in core: closure(c,need)
        miss=need-covered-set(core); new=(set(core)|miss)-covered
        lv.append(dict(anno=anno,n=i,t=t,core=core,miss=sorted(miss),new=new,set_=set(core)|miss))
        covered|=set(core)|miss
forb=set(covered)
for n in list(covered): closure(n,forb)
maxliv={1:2,2:2,3:3,4:3,5:4}
used=set(); cov=set(BASE); out={}
# figli: mappa inversa
kids={}
for k,v in pre.items():
    for p in v: kids.setdefault(p,[]).append(k)
for d in lv:
    cov|=d['set_']
    cands=[]
    for n,node in G.items():
        if n in forb or n in used: continue
        if node['liv_min'] and node['liv_min']>maxliv[d['anno']]: continue
        cl=closure(n,set())
        if not cl<=cov: continue
        direct=len(set(pre[n])&d['set_'])
        if direct==0: continue
        cands.append((-direct, node['liv_min'] or 9, n))
    cands.sort()
    out[f"{d['anno']}-{d['n']}"]=[c[2] for c in cands[:8]]
    pick=[c[2] for c in cands[:2]]
    used|=set(pick)
    d['opt']=pick
json.dump([{k:(list(v) if isinstance(v,set) else v) for k,v in d.items()} for d in lv],open('lv.json','w'),ensure_ascii=False,indent=0)
for d in lv:
    k=f"{d['anno']}-{d['n']}"
    print(k, d['t'][:40], '|', '; '.join(f"{n} {G[n]['titolo'][:45]}" for n in d['opt']), '|| alt:', ' '.join(out[k][2:]))
import json
from nuovi import OPZ
exec(open('opzionali.py').read().split("maxliv=")[0])
maxliv={1:2,2:2,3:3,4:3,5:4}
cov=set(BASE); seen={}; probs=[]
for d in lv:
    k=f"{d['anno']}-{d['n']}"; cov|=d['set_']; op=OPZ[k]
    if len(op)!=2: probs.append((k,'num'))
    for n in op:
        if n not in G: probs.append((k,n,'inesistente')); continue
        if n in forb: probs.append((k,n,'PROPEDEUTICO a un nodo obbligatorio'))
        if n in seen: probs.append((k,n,'duplicato di',seen[n]))
        seen[n]=k
        lm=G[n]['liv_min']
        if lm and lm>maxliv[d['anno']]: probs.append((k,n,'livello',lm))
        gap=closure(n,set())-cov
        if gap: probs.append((k,n,'prerequisiti non ancora fatti',sorted(gap)))
    d['opt']=op
print(len(probs)); [print(p) for p in probs]
json.dump(lv,open('lv.json','w'),default=list,ensure_ascii=False)
import json
from nuovi import OPZ
exec(open('opzionali.py').read().split("maxliv=")[0])
NOTE={'1-27':"la quantità d'informazione si presenta in forma intuitiva: quante domande sì/no servono per individuare un caso, quante volte si dimezzano le possibilità. Logaritmo in base 2 e probabilità si costruiscono a questo livello di intuizione, senza formalismo (decisione di Pietro, 27/09/2026).",'2-28':"livello volutamente denso: gli strati di rete sono anticipati dal quinto anno per spiegare indirizzi, DNS e pacchetti (decisione di Pietro, 27/09/2026). Nella scala di difficoltà interna conviene separarli in più tappe."}
DUCHI={1:"Borso",2:"Ercole I",3:"Alfonso I",4:"Ercole II",5:"Alfonso II"}
ALTRE=lambda n: n[0] in 'AC' or n.startswith('S2.1') or n.startswith('S3.1') or n in ('B5.1.1','B7.1')
T=lambda n: G[n]['titolo']
def fmt(ns): return '; '.join(f"{T(n)} `{n}`" for n in ns)
seen=set(BASE); out=[]; data=[]
for d in lv:
    k=f"{d['anno']}-{d['n']}"
    nuovi=[c for c in d['core'] if c not in seen]; rip=[c for c in d['core'] if c in seen]
    integ=[m for m in d['miss'] if not ALTRE(m)]; rich=[m for m in d['miss'] if ALTRE(m)]
    seen|=set(d['core'])|set(d['miss'])
    tipo='Prova di corte' if d['n'] in (10,20) else ('Prova finale' if d['n']==30 else None)
    data.append(dict(id=k,anno=d['anno'],numero=d['n'],duca=DUCHI[d['anno']],titolo=d['t'],tipo='prova' if tipo else 'normale',
        nucleo=nuovi,ripresa=rip,prerequisiti_integrati=integ,prerequisiti_altre_discipline_costruiti=rich,nota_didattica=NOTE.get(k),approfondimenti=OPZ[k]))
    if d['n']==1: out.append(f"\n## Anno {d['anno']} — {DUCHI[d['anno']]}\n")
    out.append(f"### {k} · {d['t']}\n")
    if nuovi: out.append(f"- **Nucleo:** {fmt(nuovi)}")
    if rip: out.append(f"- **Ripresa in un nuovo contesto:** {fmt(rip)}")
    if not nuovi and not rip: out.append("- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi")
    if integ: out.append(f"- **Prerequisiti integrati nel livello:** {fmt(integ)}")
    if rich: out.append(f"- **Prerequisiti di altre discipline, costruiti nel gioco:** {fmt(rich)}")
    if k in NOTE: out.append(f"- **Nota didattica:** {NOTE[k]}")
    out.append(f"- **Approfondimenti facoltativi:** 1) {T(OPZ[k][0])} `{OPZ[k][0]}` · 2) {T(OPZ[k][1])} `{OPZ[k][1]}`\n")
open('corpo.md','w').write('\n'.join(out))
json.dump(data,open('/mnt/user-data/outputs/videogioco-5-duchi-livelli.json','w'),ensure_ascii=False,indent=1)
n_nuc=sum(len(x['nucleo']) for x in data); n_int=sum(len(x['prerequisiti_integrati']) for x in data); n_ric=sum(len(x['prerequisiti_altre_discipline_costruiti']) for x in data)
print(n_nuc,n_int,n_ric,len(data))
