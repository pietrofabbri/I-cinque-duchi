# Mappa dell'informatica — Area L: Dati e basi di dati (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** dal foglio di calcolo al DBMS relazionale, SQL, NoSQL, data warehouse e big data, data science, open data, motori di ricerca, sistemi di raccomandazione, conservazione digitale, dati distribuiti, sicurezza dei dati. L'apprendimento automatico sui dati è nell'area O.

---

## L1 Dato, informazione, conoscenza
- **L1.1** Dati strutturati, semi-strutturati, non strutturati · [1] · ⟵ B11.1
- **L1.2** Ciclo di vita del dato: raccolta, archiviazione, elaborazione, conservazione, cancellazione · [1–2] · ⟵ L1.1
- **L1.3** Qualità dei dati: accuratezza, completezza, coerenza, attualità · [2] · ⟵ L1.1
- **L1.4** Archivi tradizionali e basi di dati; i problemi di ridondanza e incoerenza · [2] · ⟵ L1.1, I5.2
- **L1.5** La piramide dati-informazione-conoscenza-saggezza (DIKW) · [1–2] · ⟵ B1.1

## L2 Fogli di calcolo
- **L2.1** Celle, righe, colonne; tipi di dato nelle celle · [1] · ⟵ B11.1
- **L2.2** Formule; riferimenti relativi e assoluti · [1] · ⟵ L2.1, A1.5.1
- **L2.3** Funzioni: somma, media, conteggio, SE, CERCA · [1] · ⟵ L2.2, E3.2
- **L2.4** Grafici · [1] · ⟵ L2.1, A7.1.2
- **L2.5** Ordinare, filtrare, formattazione condizionale · [1] · ⟵ L2.1
- **L2.6** Tabelle pivot · [2] · ⟵ L2.5
- **L2.7** Il foglio di calcolo usato come base di dati, e i suoi limiti · [2] · ⟵ L2.5, L1.4
- **L2.8** Macro e automazione (VBA, Apps Script) · [2–3] · ⟵ L2.3, G1.8

## L3 Modellazione concettuale
- **L3.1** Livelli di astrazione: concettuale, logico, fisico · [2] · ⟵ L1.4
- **L3.2** Entità e attributi; identificatori · [2] · ⟵ L3.1
- **L3.3** Associazioni e cardinalità (1:1, 1:N, N:M) · [2] · ⟵ L3.2, A3.2.1
- **L3.4** Diagrammi Entità/Relazioni e loro notazioni · [2] · ⟵ L3.3
- **L3.5** Generalizzazioni e gerarchie · [2–3] · ⟵ L3.4
- **L3.6** Dai requisiti al modello concettuale · [2–3] · ⟵ L3.4
- **L3.7** Strumenti per disegnare schemi E/R · [2] · ⟵ L3.2 · (v1.1, approfondimento)
- **L3.8** Errori tipici negli schemi E/R e come correggerli · [3] · ⟵ L3.4 · (v1.1, approfondimento)
- **L3.9** Confrontare schemi alternativi per lo stesso problema · [3] · ⟵ L3.4 · (v1.1, approfondimento)

## L4 Modello relazionale
- **L4.1** La relazione come tabella: attributi, tuple, domini · [2] · ⟵ A3.1.4, L3.1
- **L4.2** Chiavi: superchiave, chiave candidata, primaria, esterna · [2] · ⟵ L4.1
- **L4.3** Vincoli di integrità: di dominio, di entità, referenziale · [2] · ⟵ L4.2
- **L4.4** Traduzione dal modello E/R al modello relazionale · [2] · ⟵ L4.3, L3.4
- **L4.5** Algebra relazionale: selezione, proiezione, join, unione, differenza · [2–3] · ⟵ L4.1, A3.1.3
- **L4.6** Dipendenze funzionali · [2–3] · ⟵ L4.2
- **L4.7** Normalizzazione: 1NF, 2NF, 3NF, BCNF · [2–3] · ⟵ L4.6, L4.3
- **L4.8** Denormalizzazione consapevole · [3] · ⟵ L4.7
- **L4.9** Calcolo relazionale · [3–4] · ⟵ L4.5, A2.2.2
- **L4.10** Codd e la nascita del modello relazionale · [2] · ⟵ L4.1 · (v1.1, approfondimento)
- **L4.11** Generare lo schema con uno strumento di progettazione · [3] · ⟵ L4.4 · (v1.1, approfondimento)
- **L4.12** Schemi di database reali: negozio online, social network · [3] · ⟵ L4.4 · (v1.1, approfondimento)
- **L4.13** Anomalie di inserimento, modifica, cancellazione in un foglio di calcolo reale · [3] · ⟵ L4.7 · (v1.1, approfondimento)
- **L4.14** Calcolatori di algebra relazionale · [3] · ⟵ L4.5 · (v1.1, approfondimento)
- **L4.15** Tradurre domande in linguaggio naturale in algebra relazionale · [3] · ⟵ L4.5 · (v1.1, approfondimento)

## L5 SQL
- **L5.1** DDL: CREATE, ALTER, DROP; tipi di dato · [2] · ⟵ L4.3
- **L5.2** DML: INSERT, UPDATE, DELETE · [2] · ⟵ L5.1
- **L5.3** SELECT con condizioni e ordinamento · [2] · ⟵ L5.1, A2.1.4
- **L5.4** Join interni ed esterni · [2] · ⟵ L5.3, L4.5
- **L5.5** Funzioni di aggregazione, GROUP BY, HAVING · [2] · ⟵ L5.3
- **L5.6** Interrogazioni annidate · [2–3] · ⟵ L5.4
- **L5.7** Valori NULL e logica a tre valori · [2–3] · ⟵ L5.3, A2.6.1
- **L5.8** Viste · [2] · ⟵ L5.4
- **L5.9** Controllo degli accessi: GRANT e REVOKE · [2–3] · ⟵ L5.1
- **L5.10** Funzioni finestra, espressioni di tabella comuni, interrogazioni ricorsive · [3] · ⟵ L5.6, A3.2.5
- **L5.11** Trigger e procedure memorizzate · [3] · ⟵ L5.2, G1.8
- **L5.12** SQL dentro i programmi: connettori, query parametriche, ORM · [2–3] · ⟵ L5.3, G1.15 · ⟶ K7
- **L5.13** Ricerca testuale in SQL: LIKE ed espressioni regolari · [2–3] · ⟵ L5.3 · (v1.1, approfondimento)
- **L5.14** I join rappresentati con i diagrammi di Venn, e i limiti di questa rappresentazione · [2] · ⟵ L5.4 · (v1.1, approfondimento)
- **L5.15** Self-join: una tabella collegata a se stessa (alberi genealogici) · [3] · ⟵ L5.4 · (v1.1, approfondimento)
- **L5.16** Mediana e percentili in SQL · [3] · ⟵ L5.5 · (v1.1, approfondimento)
- **L5.17** Riepiloghi in SQL e tabelle pivot a confronto · [3] · ⟵ L5.5, L2.6 · (v1.1, approfondimento)
- **L5.18** Salvare i progressi di un gioco in SQLite · [3] · ⟵ L5.12 · (v1.1, approfondimento)

## L6 Sistemi di gestione di basi di dati (DBMS)
- **L6.1** Architettura di un DBMS · [2–3] · ⟵ L4.1
- **L6.2** Transazioni e proprietà ACID · [3] · ⟵ L6.1
- **L6.3** Controllo di concorrenza: lock a due fasi, livelli di isolamento, MVCC · [3] · ⟵ L6.2, I3.3
- **L6.4** Ripristino dopo i guasti: log e checkpoint · [3] · ⟵ L6.2
- **L6.5** Organizzazione fisica: file, pagine, record · [3] · ⟵ L6.1, I5.3
- **L6.6** Indici (B+tree, hash) e loro scelta · [3] · ⟵ L6.5, E6.4.7, E6.5.1
- **L6.7** Elaborazione e ottimizzazione delle interrogazioni; piani di esecuzione · [3–4] · ⟵ L6.6, L4.5
- **L6.8** DBMS diffusi: SQLite, PostgreSQL, MySQL/MariaDB · [2] · ⟵ L5.1

## L7 Basi di dati NoSQL
- **L7.1** Perché il NoSQL; cenni al teorema CAP · [3] · ⟵ L6.2
- **L7.2** Basi di dati chiave-valore · [3] · ⟵ L7.1, E6.5.4
- **L7.3** Basi di dati a documenti (es. MongoDB) · [3] · ⟵ L7.1, B11.4
- **L7.4** Basi di dati a colonne · [3–4] · ⟵ L7.1
- **L7.5** Basi di dati a grafo e loro linguaggi di interrogazione (Cypher) · [3] · ⟵ L7.1, A4.3.1
- **L7.6** Basi di dati per serie temporali e vettoriali · [3–4] · ⟵ L7.1, A5.1.3 · ⟶ O6
- **L7.7** Consistenza eventuale · [3–4] · ⟵ L7.1
- **L7.8** Quando le tabelle non bastano: panoramica dei database NoSQL · [3] · ⟵ L4.1 · (v1.1, approfondimento)

## L8 Data warehouse, OLAP, big data
- **L8.1** Sistemi operazionali e analitici (OLTP e OLAP) · [3] · ⟵ L6.2
- **L8.2** Data warehouse: schema a stella, fatti e dimensioni · [3] · ⟵ L8.1, L4.4
- **L8.3** Cubi OLAP: roll-up, drill-down, slice and dice · [3] · ⟵ L8.2
- **L8.4** Processi ETL ed ELT · [3] · ⟵ L8.2
- **L8.5** Big data: volume, velocità, varietà, veridicità · [2–3] · ⟵ L1.1
- **L8.6** Elaborazione distribuita: MapReduce, Hadoop, Spark · [3–4] · ⟵ L8.5, E11.5
- **L8.7** Data lake e lakehouse · [3–4] · ⟵ L8.4, L8.6
- **L8.8** Elaborazione di flussi di dati (Kafka, Flink) · [4] · ⟵ L8.6

## L9 Data science
- **L9.1** Il ciclo di un progetto di analisi dei dati · [2] · ⟵ L1.2
- **L9.2** Raccolta: fonti, API, web scraping · [2] · ⟵ L9.1, B11.4
- **L9.3** Pulizia e preparazione: valori mancanti, duplicati, formati · [2] · ⟵ L9.1, L1.3
- **L9.4** Analisi esplorativa · [2] · ⟵ L9.3, A7.1.4
- **L9.5** Visualizzare i dati per analizzarli · [2] · ⟵ L9.4, A7.1.2
- **L9.6** Strumenti: pandas, R, notebook · [2] · ⟵ L9.3, G2.2.13
- **L9.7** Raccontare con i dati · [2] · ⟵ L9.5, U11.4
- **L9.8** Riproducibilità dell'analisi · [3] · ⟵ L9.6, H5.1
- **L9.9** Inferenza e modelli statistici nell'analisi · [3] · ⟵ L9.4, A7.4.2
- **L9.10** Cruscotti costruiti sui dati di un database · [3] · ⟵ L5.5 · (v1.1, approfondimento)

## L10 Open data, governance e qualità dei dati
- **L10.1** Open data: definizione, licenze, portali nazionali · [1–2] · ⟵ L1.1, U4.5
- **L10.2** Scala a cinque stelle degli open data · [2] · ⟵ L10.1
- **L10.3** Governance dei dati: ruoli, responsabilità, politiche · [3] · ⟵ L1.3
- **L10.4** Metadati e cataloghi di dati · [2–3] · ⟵ L10.1, B11.6
- **L10.5** Principi FAIR · [3] · ⟵ L10.4
- **L10.6** Protezione dei dati personali nel trattamento dei dati · [2] · ⟵ U4.1

## L11 Information retrieval e motori di ricerca
- **L11.1** Il problema della ricerca in documenti non strutturati · [2] · ⟵ L1.1
- **L11.2** L'indice invertito · [2–3] · ⟵ L11.1, E6.5.4
- **L11.3** Modello booleano e modello vettoriale; TF-IDF · [3] · ⟵ L11.2, A5.1.3, A1.2.5
- **L11.4** Valutazione: precisione e richiamo · [3] · ⟵ L11.1
- **L11.5** Crawler e architettura di un motore di ricerca · [3] · ⟵ L11.2, J7.3
- **L11.6** PageRank e analisi dei collegamenti · [3] · ⟵ L11.5, A5.3.3, A7.5.3
- **L11.7** Ricerca semantica con embedding · [4] · ⟵ L11.3, L7.6
- **L11.8** Usare bene un motore di ricerca: operatori, valutazione dei risultati · [1] · ⟵ — · ⟶ U7.3

## L12 Sistemi di raccomandazione
- **L12.1** Tipi di sistemi di raccomandazione · [2–3] · ⟵ L1.1
- **L12.2** Raccomandazione basata sui contenuti · [3] · ⟵ L12.1, L11.3
- **L12.3** Filtraggio collaborativo · [3] · ⟵ L12.1, A5.1.3
- **L12.4** Fattorizzazione di matrici · [4] · ⟵ L12.3, A5.3.2
- **L12.5** Valutazione, problema dell'avvio a freddo, bolle di filtro · [3] · ⟵ L12.3 · ⟶ U7.4

## L13 Biblioteche digitali, archivi e conservazione digitale
- **L13.1** Biblioteche e archivi digitali · [2] · ⟵ L1.2
- **L13.2** Metadati descrittivi: Dublin Core · [2–3] · ⟵ L13.1, B11.6
- **L13.3** Identificatori persistenti: DOI, ORCID, handle · [2–3] · ⟵ L13.1
- **L13.4** Conservazione a lungo termine: obsolescenza dei formati, migrazione, emulazione · [3] · ⟵ L13.1, B11.9
- **L13.5** Archivi del web · [2] · ⟵ L13.1
- **L13.6** Conservazione digitale a norma dei documenti amministrativi · [3] · ⟵ L13.4, B13.8

## L14 Basi di dati distribuite e ingegneria dei dati
- **L14.1** Replicazione dei dati · [3] · ⟵ L6.2
- **L14.2** Partizionamento (sharding) · [3] · ⟵ L14.1
- **L14.3** Transazioni distribuite; commit a due fasi · [4] · ⟵ L14.1, L6.3
- **L14.4** Pipeline di dati e loro orchestrazione · [3] · ⟵ L8.4
- **L14.5** Archiviazione e interrogazione di dati semi-strutturati e non strutturati · [3] · ⟵ L7.3
- **L14.6** Basi di dati nel cloud (servizi gestiti) · [3] · ⟵ L14.2 · ⟶ M4

## L15 Sicurezza e privacy dei dati
- **L15.1** Controllo degli accessi ai dati: ruoli e privilegi · [2–3] · ⟵ L5.9
- **L15.2** Cifratura dei dati a riposo e in transito · [3] · ⟵ L6.1, N3.1
- **L15.3** SQL injection e difese · [2–3] · ⟵ L5.12 · ⟶ N6
- **L15.4** Anonimizzazione e pseudonimizzazione · [3] · ⟵ L10.6 · ⟶ N11
- **L15.5** Provenienza e tracciabilità dei dati · [3–4] · ⟵ L10.3
- **L15.6** Backup e ripristino delle basi di dati · [3] · ⟵ L6.4, I11.3
