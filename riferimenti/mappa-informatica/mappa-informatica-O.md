# Mappa dell'informatica — Area O: Intelligenza artificiale (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** IA simbolica, ragionamento in condizioni di incertezza, apprendimento automatico, reti neurali, IA generativa, sicurezza e interpretabilità, calcolo evolutivo, hardware, etica, IA nell'educazione, sistemi multi-agente, affective computing, valutazione. L'elaborazione del linguaggio è nell'area P, la visione artificiale in Q, la robotica in R. Alcuni nodi d'uso consapevole (O1.6, O6.4, O6.5, O11.1) sono di livello `[1]`.

---

## O1 Definizioni, storia, agenti
- **O1.1** Che cos'è l'intelligenza artificiale: definizioni e approcci · [1] · ⟵ —
- **O1.2** Storia dell'IA e principali svolte · [1–2] · ⟵ O1.1, U1.17
- **O1.3** Il test di Turing · [1–2] · ⟵ O1.1
- **O1.4** IA ristretta e generale; IA debole e forte · [2] · ⟵ O1.1
- **O1.5** Agenti intelligenti: percezione, azione, ambiente · [2] · ⟵ O1.1
- **O1.6** L'IA nella vita quotidiana: riconoscerla e usarla con consapevolezza · [1] · ⟵ O1.1 · ⟶ U7

## O2 IA simbolica

### O2.1 Ricerca nello spazio degli stati
- **O2.1.1** Problemi come spazi di stati · [2] · ⟵ O1.5, A4.3.1
- **O2.1.2** Ricerca non informata: in ampiezza, in profondità, a costo uniforme · [2–3] · ⟵ O2.1.1, E7.3.1, E7.3.2
- **O2.1.3** Ricerca informata: euristiche e A* · [3] · ⟵ O2.1.2, E7.3.9
- **O2.1.4** Ricerca locale · [3] · ⟵ O2.1.1, A9.3.1

### O2.2 Giochi
- **O2.2.1** Giochi a due giocatori e albero di gioco · [2] · ⟵ O2.1.1, A4.3.3
- **O2.2.2** Algoritmo minimax · [2–3] · ⟵ O2.2.1, A9.4.3
- **O2.2.3** Potatura alfa-beta · [3] · ⟵ O2.2.2
- **O2.2.4** Ricerca ad albero Monte Carlo · [3–4] · ⟵ O2.2.2, A7.3.4

### O2.3 Rappresentazione della conoscenza
- **O2.3.1** Regole, frame, reti semantiche · [2–3] · ⟵ A2.2.2
- **O2.3.2** Inferenza in avanti e all'indietro · [3] · ⟵ O2.3.1, A2.1.7
- **O2.3.3** Ontologie e grafi di conoscenza · [3–4] · ⟵ O2.3.1
- **O2.3.4** Ragionamento di senso comune e suoi limiti · [3] · ⟵ O2.3.1

### O2.4 Sistemi esperti e pianificazione
- **O2.4.1** Sistemi esperti: base di conoscenza e motore inferenziale · [2–3] · ⟵ O2.3.1
- **O2.4.2** Pianificazione automatica (STRIPS, PDDL) · [3–4] · ⟵ O2.1.3, O2.3.1

### O2.5 Vincoli e ragionamento automatico
- **O2.5** Soddisfacimento di vincoli e ragionamento automatico nell'IA · [3] · ⟵ F14.4, O2.1.1

## O3 Ragionamento in condizioni di incertezza
- **O3.1** Rappresentare l'incertezza con la probabilità · [3] · ⟵ A7.2.4
- **O3.2** Reti bayesiane · [3–4] · ⟵ O3.1, A4.3.4
- **O3.3** Inferenza esatta e approssimata · [4] · ⟵ O3.2
- **O3.4** Modelli temporali: HMM, filtro di Kalman, filtri a particelle · [4] · ⟵ O3.2, A7.5.6
- **O3.5** Logica fuzzy e controllo fuzzy · [3] · ⟵ A2.6.2
- **O3.6** Teoria delle decisioni per agenti · [3–4] · ⟵ O3.1, A9.4.1

## O4 Apprendimento automatico

### O4.1 Apprendimento supervisionato
- **O4.1.1** Imparare dai dati: esempi, caratteristiche, etichette · [1–2] · ⟵ O1.1, B11.1
- **O4.1.2** Classificazione e regressione · [2] · ⟵ O4.1.1
- **O4.1.3** k vicini più prossimi · [2] · ⟵ O4.1.2, A5.1.3
- **O4.1.4** Regressione lineare · [2–3] · ⟵ O4.1.2, A7.1.5
- **O4.1.5** Regressione logistica · [3] · ⟵ O4.1.4, A8.4.1
- **O4.1.6** Alberi di decisione · [2–3] · ⟵ O4.1.2, A8.1.2
- **O4.1.7** Metodi d'insieme: foreste casuali, boosting · [3] · ⟵ O4.1.6
- **O4.1.8** Macchine a vettori di supporto · [3–4] · ⟵ O4.1.5, A9.2.4
- **O4.1.9** Classificatore bayesiano ingenuo · [3] · ⟵ O4.1.2, A7.2.4
- **O4.1.10** Preparare le caratteristiche: normalizzazione e codifica · [2–3] · ⟵ O4.1.1, L9.3

### O4.2 Apprendimento non supervisionato
- **O4.2.1** Clustering: k-means · [2–3] · ⟵ O4.1.1, A5.1.3
- **O4.2.2** Clustering gerarchico e basato sulla densità · [3] · ⟵ O4.2.1
- **O4.2.3** Riduzione della dimensionalità: PCA · [3] · ⟵ O4.2.1, A5.3.2
- **O4.2.4** Visualizzare dati ad alta dimensione (t-SNE, UMAP) · [4] · ⟵ O4.2.3
- **O4.2.5** Rilevamento di anomalie · [3] · ⟵ O4.2.1, A7.3.3
- **O4.2.6** Apprendimento autosupervisionato · [4] · ⟵ O4.2.3, O5.1.5

### O4.3 Valutazione dei modelli
- **O4.3.1** Insiemi di addestramento, di validazione e di test · [2] · ⟵ O4.1.2
- **O4.3.2** Sovradattamento e sottoadattamento; compromesso fra distorsione e varianza · [2–3] · ⟵ O4.3.1
- **O4.3.3** Metriche: accuratezza, precisione, richiamo, F1, matrice di confusione · [2] · ⟵ O4.3.1
- **O4.3.4** Validazione incrociata · [3] · ⟵ O4.3.1, A7.4.6
- **O4.3.5** Regolarizzazione · [3] · ⟵ O4.3.2, O4.1.4
- **O4.3.6** Bias nei dati ed equità dei modelli · [2–3] · ⟵ O4.3.3, U3.2
- **O4.3.7** Strumenti: scikit-learn · [2–3] · ⟵ O4.3.1, G2.2.13

### O4.4 Apprendimento per rinforzo
- **O4.4.1** Agente, ambiente, ricompensa · [2–3] · ⟵ O1.5
- **O4.4.2** Processi decisionali di Markov e funzioni di valore · [3] · ⟵ O4.4.1, A7.5.5
- **O4.4.3** Q-learning · [3–4] · ⟵ O4.4.2
- **O4.4.4** Esplorazione e sfruttamento; banditi multibraccio · [3] · ⟵ O4.4.1, A7.3.2
- **O4.4.5** Apprendimento per rinforzo profondo · [4] · ⟵ O4.4.3, O5.1.5
- **O4.4.6** Apprendimento per rinforzo da feedback umano (RLHF) · [4] · ⟵ O4.4.5, O6.1

## O5 Reti neurali e deep learning

### O5.1 Fondamenti
- **O5.1.1** Neurone artificiale e percettrone · [2] · ⟵ O4.1.2, A5.1.3
- **O5.1.2** Funzioni di attivazione · [2–3] · ⟵ O5.1.1, A6.1.1
- **O5.1.3** Reti multistrato; approssimazione universale · [3] · ⟵ O5.1.2, A5.1.6
- **O5.1.4** Funzione di perdita e discesa del gradiente · [3] · ⟵ O5.1.3, A6.2.5, A8.4.1
- **O5.1.5** Retropropagazione dell'errore · [3] · ⟵ O5.1.4, A6.2.6
- **O5.1.6** Ottimizzatori, inizializzazione, normalizzazione, dropout · [3–4] · ⟵ O5.1.5, A9.2.3
- **O5.1.7** Framework: PyTorch, TensorFlow, Keras · [3] · ⟵ O5.1.3, G3.8.4
- **O5.1.8** Addestramento su GPU · [3–4] · ⟵ O5.1.7, D11.4

### O5.2 Reti convoluzionali
- **O5.2.1** La convoluzione sulle immagini · [3] · ⟵ O5.1.3, A6.5.5, B6.1
- **O5.2.2** Pooling e architetture classiche (LeNet, ResNet) · [3] · ⟵ O5.2.1
- **O5.2.3** Apprendimento per trasferimento · [3] · ⟵ O5.2.2

### O5.3 Reti ricorrenti
- **O5.3.1** Reti ricorrenti per le sequenze · [3–4] · ⟵ O5.1.5
- **O5.3.2** LSTM e GRU · [4] · ⟵ O5.3.1

### O5.4 Attenzione e Transformer
- **O5.4.1** Embedding: parole e oggetti come vettori · [3] · ⟵ O5.1.3, A5.1.3
- **O5.4.2** Il meccanismo di attenzione · [3–4] · ⟵ O5.4.1, A5.1.6
- **O5.4.3** L'architettura Transformer · [4] · ⟵ O5.4.2
- **O5.4.4** Transformer per immagini, audio e dati multimodali · [4] · ⟵ O5.4.3, O5.2.1

### O5.5 Reti neurali su grafi *(nuovo in v1.0)*
- **O5.5** Reti neurali su grafi · [4] · ⟵ O5.1.5, A4.3.1
- **O5.6** Sperimentare con una rete neurale nel browser (TensorFlow Playground) · [3] · ⟵ O5.1.3 · (v1.1, approfondimento)

## O6 IA generativa
- **O6.1** Modello linguistico: prevedere il token successivo · [2–3] · ⟵ A7.2.3, O4.1.1
- **O6.2** Grandi modelli linguistici: pre-addestramento, scala, capacità emergenti · [3–4] · ⟵ O6.1, O5.4.2
- **O6.3** Messa a punto e allineamento (istruzioni, RLHF) · [4] · ⟵ O6.2, O4.4.1
- **O6.4** Usare i modelli: prompt, contesto, esempi · [1–2] · ⟵ O1.6
- **O6.5** Allucinazioni, limiti, verifica delle risposte · [1–2] · ⟵ O6.4, U7.3
- **O6.6** Generazione aumentata dal recupero (RAG) · [3] · ⟵ O6.2, L11.3
- **O6.7** Agenti e uso di strumenti · [3] · ⟵ O6.2, O1.5
- **O6.8** Modelli di diffusione per immagini, audio, video · [4] · ⟵ O5.2.1, A7.3.3
- **O6.9** Autoencoder variazionali e reti generative avversarie · [4] · ⟵ O5.1.5, A8.4.2
- **O6.10** Modelli aperti e chiusi; esecuzione in locale · [2–3] · ⟵ O6.4
- **O6.11** Valutare i contenuti generati; filigrane e provenienza · [3] · ⟵ O6.5

## O7 Sicurezza e affidabilità dell'IA
- **O7.1** Robustezza e generalizzazione fuori distribuzione · [3–4] · ⟵ O4.3.2
- **O7.2** Spiegabilità: importanza delle caratteristiche, SHAP · [3–4] · ⟵ O4.1.7
- **O7.3** Interpretabilità meccanicistica · [4] · ⟵ O7.2, O5.4.3
- **O7.4** Allineamento ai valori umani · [4] · ⟵ O6.3
- **O7.5** Valutazione dei rischi dei modelli più avanzati · [4] · ⟵ O7.4, O14.1

## O8 Calcolo evolutivo e intelligenza di sciame
- **O8.1** Algoritmi genetici: popolazione, selezione, incrocio, mutazione · [2–3] · ⟵ A9.3.1
- **O8.2** Programmazione genetica ed evoluzione di strategie · [3–4] · ⟵ O8.1
- **O8.3** Intelligenza di sciame: colonie di formiche, sciami di particelle · [3] · ⟵ A9.3.1
- **O8.4** Neuroevoluzione · [4] · ⟵ O8.1, O5.1.3

## O9 Hardware, costi ed energia dell'IA
- **O9.1** Perché servono le GPU per l'IA · [3] · ⟵ D11.4, O5.1.6
- **O9.2** Acceleratori dedicati · [3–4] · ⟵ D12.2
- **O9.3** Costi di addestramento e di inferenza; leggi di scala · [3–4] · ⟵ O6.2
- **O9.4** Compressione dei modelli: quantizzazione, distillazione, potatura · [4] · ⟵ O5.1.6, B2.5.6
- **O9.5** Energia e impronta ambientale dell'IA · [2–3] · ⟵ U6.2

## O10 Etica e diritto dell'IA
- **O10.1** Rischi e benefici dell'IA per la società · [1–2] · ⟵ O1.6
- **O10.2** Equità, bias e discriminazione algoritmica · [2–3] · ⟵ O4.3.6
- **O10.3** Trasparenza e responsabilità dei sistemi di IA · [2–3] · ⟵ O10.1, U3.3
- **O10.4** L'AI Act in pratica: classificare un sistema · [3] · ⟵ U4.8
- **O10.5** IA, lavoro, creatività, diritto d'autore · [2–3] · ⟵ O10.1, U4.3

## O11 IA nell'educazione
- **O11.1** Usare l'IA per studiare: tutor, spiegazioni, esercizi · [1–2] · ⟵ O6.4
- **O11.2** Integrità accademica e uso trasparente · [1–2] · ⟵ O11.1
- **O11.3** Sistemi di tutoraggio intelligenti e apprendimento adattivo · [3] · ⟵ O11.1, O4.1.2
- **O11.4** Analisi dei dati di apprendimento (learning analytics) · [3] · ⟵ L9.4
- **O11.5** Politiche scolastiche sull'uso dell'IA · [2–3] · ⟵ O11.2, O10.1, U4.8

## O12 Sistemi multi-agente
- **O12.1** Agenti autonomi e loro interazione · [3] · ⟵ O1.5
- **O12.2** Coordinamento e cooperazione · [3–4] · ⟵ O12.1
- **O12.3** Negoziazione e aste fra agenti · [4] · ⟵ O12.1, F11.5
- **O12.4** Simulazioni ad agenti · [3] · ⟵ O12.1 · ⟶ S1
- **O12.5** Più modelli linguistici che collaborano · [4] · ⟵ O12.2, O6.7

## O13 Affective computing
- **O13.1** Modelli psicologici delle emozioni (categoriali e dimensionali) · [2–3] · ⟵ —
- **O13.2** Riconoscere le emozioni da volto, voce, testo · [3–4] · ⟵ O13.1, O5.2.1
- **O13.3** Agenti conversazionali empatici · [4] · ⟵ O13.2, O6.2
- **O13.4** Questioni etiche e giuridiche del riconoscimento delle emozioni · [3] · ⟵ O13.2, U4.8

## O14 Valutazione dell'IA
- **O14.1** Benchmark e loro limiti · [3] · ⟵ O4.3.3
- **O14.2** Valutazione umana e preferenze · [3] · ⟵ O14.1
- **O14.3** Valutare i modelli linguistici; contaminazione dei dati di test · [3–4] · ⟵ O14.1, O6.2
- **O14.4** Red teaming · [4] · ⟵ O14.3
