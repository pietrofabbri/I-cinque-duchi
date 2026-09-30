# Mappa dell'informatica — Area F: Informatica teorica (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** automi, linguaggi formali, calcolabilità, complessità, lambda calcolo, tipi, semantica, metodi formali, teoria dell'apprendimento, concorrenza, SAT. Quasi tutta l'area è di livello universitario; alcune porte d'ingresso (automi, macchina di Turing, P vs NP) si possono affrontare a livello `[2]` in forma intuitiva.

---

## F1 Automi a stati finiti e linguaggi regolari
- **F1.1** Automa a stati finiti deterministico (DFA): stati, transizioni, accettazione · [2] · ⟵ A3.1.5, A4.3.1
- **F1.2** Automi non deterministici (NFA) ed equivalenza con i DFA · [3] · ⟵ F1.1, A3.1.2
- **F1.3** Espressioni regolari in senso formale · [2–3] · ⟵ F1.1
- **F1.4** Teorema di Kleene: equivalenza fra espressioni regolari e automi · [3] · ⟵ F1.2, F1.3
- **F1.5** Minimizzazione degli automi · [3] · ⟵ F1.1, A3.2.3
- **F1.6** Pumping lemma e linguaggi non regolari · [3] · ⟵ F1.1, A2.3.3
- **F1.7** Proprietà di chiusura e problemi decidibili sui linguaggi regolari · [3] · ⟵ F1.4
- **F1.8** Applicazioni: analizzatori lessicali, protocolli, interfacce · [2–3] · ⟵ F1.3
- **F1.9** Trasduttori (automi con uscita) · [3] · ⟵ F1.1

## F2 Grammatiche formali e gerarchia di Chomsky
- **F2.1** Grammatiche formali: terminali, non terminali, produzioni, derivazioni · [2–3] · ⟵ A3.1.5, A3.5
- **F2.2** Notazioni BNF ed EBNF; diagrammi sintattici · [2] · ⟵ F2.1
- **F2.3** Alberi di derivazione; ambiguità · [3] · ⟵ F2.1, A4.3.3
- **F2.4** Gerarchia di Chomsky · [3] · ⟵ F2.1, F1.4
- **F2.5** Grammatiche e linguaggi liberi dal contesto · [3] · ⟵ F2.3
- **F2.6** Automi a pila ed equivalenza con le grammatiche libere · [3] · ⟵ F2.5, E6.3.1, F1.2
- **F2.7** Forma normale di Chomsky; algoritmo CYK · [3–4] · ⟵ F2.5, E8.5
- **F2.8** Pumping lemma per i linguaggi liberi dal contesto · [3–4] · ⟵ F2.5, F1.6
- **F2.9** Linguaggi dipendenti dal contesto; automi lineari limitati · [4] · ⟵ F2.4
- **F2.10** Grammatiche per generare frasi casuali · [3] · ⟵ F2.1 · (v1.1, approfondimento)

## F3 Macchina di Turing e tesi di Church-Turing
- **F3.1** Macchina di Turing: nastro, testina, stati; esempi · [2–3] · ⟵ F1.1
- **F3.2** Varianti (più nastri, non determinismo) e loro equivalenza · [3] · ⟵ F3.1
- **F3.3** La macchina di Turing universale · [3] · ⟵ F3.2
- **F3.4** Modelli equivalenti: funzioni ricorsive, macchine a registri, lambda calcolo · [3–4] · ⟵ F3.1, F6.1
- **F3.5** Tesi di Church-Turing · [3] · ⟵ F3.3
- **F3.6** Turing-completezza di linguaggi e sistemi (anche giochi e automi cellulari) · [3] · ⟵ F3.5

## F4 Calcolabilità
- **F4.1** Funzioni calcolabili e non calcolabili; argomento di cardinalità · [3] · ⟵ F3.1, A3.4.3
- **F4.2** Il problema della fermata e la sua indecidibilità · [3] · ⟵ F4.1, F3.3, A2.3.3
- **F4.3** Linguaggi decidibili, semidecidibili, non semidecidibili · [3] · ⟵ F4.2
- **F4.4** Riduzioni fra problemi · [3] · ⟵ F4.3, E8.7
- **F4.5** Teorema di Rice · [4] · ⟵ F4.4
- **F4.6** Altri problemi indecidibili: corrispondenza di Post, piastrellature, decimo problema di Hilbert · [4] · ⟵ F4.4
- **F4.7** Conseguenze pratiche: i limiti dell'analisi automatica dei programmi · [3] · ⟵ F4.2 · ⟶ H6, N6

## F5 Complessità computazionale
- **F5.1** Classi di complessità temporale; la classe P · [3] · ⟵ E9.3, F3.1
- **F5.2** La classe NP: certificati e verifica · [3] · ⟵ F5.1
- **F5.3** Riduzioni polinomiali; NP-completezza; teorema di Cook-Levin · [3] · ⟵ F5.2, F4.4, A2.1.6
- **F5.4** Problemi NP-completi classici (SAT, 3-colorazione, commesso viaggiatore, zaino) · [3] · ⟵ F5.3, A9.1.5
- **F5.5** Il problema P vs NP e le sue conseguenze · [2–3] · ⟵ E9.9
- **F5.6** Classi di spazio (L, PSPACE) ed EXPTIME; teoremi di gerarchia · [4] · ⟵ F5.3
- **F5.7** Complessità probabilistica: BPP, RP · [4] · ⟵ F5.2, E10.1
- **F5.8** Approssimabilità e inapprossimabilità · [4] · ⟵ F5.4
- **F5.9** Complessità nel caso medio e complessità "fine-grained" · [4] · ⟵ F5.3
- **F5.10** Complessità della comunicazione e dei circuiti · [4] · ⟵ F5.1, D2

## F6 Lambda calcolo
- **F6.1** Sintassi: astrazione e applicazione · [3] · ⟵ A3.3.4
- **F6.2** Beta-riduzione e forme normali · [3] · ⟵ F6.1
- **F6.3** Codificare numeri e booleani (numerali di Church) · [3] · ⟵ F6.2
- **F6.4** Ricorsione e combinatore di punto fisso · [3–4] · ⟵ F6.3, E5.1
- **F6.5** Strategie di valutazione: per valore, per nome, pigra · [3] · ⟵ F6.2
- **F6.6** Lambda calcolo tipato semplice · [3–4] · ⟵ F6.2

## F7 Teoria dei tipi
- **F7.1** Tipi come insiemi di valori e come specifiche · [3] · ⟵ A3.1.1, E4.2
- **F7.2** Regole di tipizzazione e giudizi · [3–4] · ⟵ F7.1, F6.6
- **F7.3** Polimorfismo e inferenza di Hindley-Milner · [4] · ⟵ F7.2
- **F7.4** Tipi algebrici e ricorsivi · [3–4] · ⟵ F7.1, A3.5
- **F7.5** Sottotipi · [4] · ⟵ F7.2
- **F7.6** Tipi dipendenti · [4] · ⟵ F7.2
- **F7.7** Corrispondenza di Curry-Howard: proposizioni come tipi · [4] · ⟵ F7.6, A2.6.5
- **F7.8** Tipi lineari e affini (base teorica dell'ownership) · [4] · ⟵ F7.2 · ⟶ G4

## F8 Semantica dei linguaggi
- **F8.1** Sintassi e semantica dei linguaggi di programmazione · [3] · ⟵ F2.3
- **F8.2** Semantica operazionale (a piccoli e a grandi passi) · [3–4] · ⟵ F8.1, F6.2
- **F8.3** Semantica denotazionale · [4] · ⟵ F8.1, A3.2.4
- **F8.4** Semantica assiomatica: logica di Hoare · [3–4] · ⟵ F8.1, A2.3.6, E9.1
- **F8.5** Precondizione più debole (Dijkstra) · [4] · ⟵ F8.4

## F9 Metodi formali e verifica
- **F9.1** Specifica formale (Z, TLA+, Alloy) · [3–4] · ⟵ A2.2.2, H11
- **F9.2** Model checking: sistemi a stati, proprietà temporali, esplosione degli stati · [4] · ⟵ A2.6.4, F1.1
- **F9.3** Verifica deduttiva e dimostratori interattivi (Coq/Rocq, Lean, Isabelle) · [4] · ⟵ F8.4, F7.7
- **F9.4** Solver SAT e SMT nella verifica · [4] · ⟵ F14.3, F9.1
- **F9.5** Interpretazione astratta e analisi statica · [4] · ⟵ F8.3, F4.5
- **F9.6** Casi industriali: aeronautica, ferrovie, cloud · [4] · ⟵ F9.2
- **F9.7** Verifica formale di programmi concorrenti · [4] · ⟵ F9.2, F13.3

## F10 Teoria algoritmica dell'informazione
- **F10.1** Complessità di Kolmogorov di una stringa · [4] · ⟵ F3.3, A8.1.2
- **F10.2** Incomprimibilità e casualità · [4] · ⟵ F10.1
- **F10.3** Non calcolabilità della complessità di Kolmogorov · [4] · ⟵ F10.1, F4.2
- **F10.4** Induzione di Solomonoff e principio MDL · [4] · ⟵ F10.1, A8.4.3

## F11 Crittografia teorica e teoria dei giochi algoritmica
- **F11.1** Funzioni unidirezionali e generatori pseudocasuali · [4] · ⟵ F5.2, A7.2.5
- **F11.2** Sicurezza dimostrabile e riduzioni crittografiche · [4] · ⟵ F11.1
- **F11.3** Prove interattive e prove a conoscenza zero · [4] · ⟵ F11.1, F5.7
- **F11.4** Equilibri e complessità del loro calcolo · [4] · ⟵ A9.4.2, F5.3
- **F11.5** Progettazione di meccanismi e aste · [4] · ⟵ A9.4.2
- **F11.6** Prezzo dell'anarchia; giochi di instradamento · [4] · ⟵ F11.4

## F12 Teoria dell'apprendimento computazionale
- **F12.1** Apprendimento PAC · [4] · ⟵ A7.3.6, F5.1
- **F12.2** Dimensione di Vapnik-Chervonenkis · [4] · ⟵ F12.1
- **F12.3** Apprendimento online e rimpianto · [4] · ⟵ F12.1
- **F12.4** Teoremi "no free lunch" · [4] · ⟵ F12.1

## F13 Modelli formali della concorrenza
- **F13.1** Reti di Petri: posti, transizioni, marcature · [3] · ⟵ A4.3.1
- **F13.2** Proprietà: raggiungibilità, vivezza, stallo · [3–4] · ⟵ F13.1
- **F13.3** Algebre di processi: CSP, CCS · [4] · ⟵ F1.1, F8.2
- **F13.4** π-calcolo · [4] · ⟵ F13.3
- **F13.5** Bisimulazione ed equivalenze comportamentali · [4] · ⟵ F13.3
- **F13.6** Modelli di memoria e linearizzabilità · [4] · ⟵ F13.3, I3

## F14 Soddisfacibilità e vincoli
- **F14.1** Il problema SAT; formule in CNF · [3] · ⟵ A2.1.6
- **F14.2** Algoritmi DPLL e CDCL · [3–4] · ⟵ F14.1, E8.4
- **F14.3** Solver SMT e teorie (aritmetica, array) · [4] · ⟵ F14.2, A2.2.4
- **F14.4** Problemi di soddisfacimento di vincoli: variabili, domini, propagazione · [3] · ⟵ F14.1, E8.4
- **F14.5** Programmazione a vincoli (es. MiniZinc) · [3–4] · ⟵ F14.4
- **F14.6** Transizione di fase nei problemi casuali · [4] · ⟵ F14.1, A7.3.1
