# Mappa dell'informatica — Area A: Fondamenti matematici e logici (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md` (alberatura generale, convenzioni, verifica di copertura).
**Perché si parte da qui:** A è la radice del grafo. Quasi tutti i suoi nodi hanno prerequisiti soltanto interni all'area. Le poche eccezioni sono tre dipendenze esterne, elencate in fondo.

---

## Convenzioni di questo file (valgono per tutti i file di dettaglio per area)

Ogni nodo è una riga con questo formato, pensato per essere estratto automaticamente e trasformato in grafo:

```
- **ID** Titolo · [livello] · ⟵ prerequisiti diretti · ⟶ nodi che sblocca in altre aree
```

- **ID**: estende quello del documento madre (A5.3 → A5.3.1, A5.3.2…). Gli ID esistenti non cambiano mai; i nuovi nodi si aggiungono in coda al proprio ramo.
- **Livello**:
  - `[1]` primo biennio;
  - `[2]` triennio;
  - `[3]` università;
  - `[4]` specialistico.
  Un intervallo come `[1–2]` indica un nodo che si può affrontare a due livelli di profondità.
- **⟵ prerequisiti diretti**: solo quelli *immediati*, sia interni sia esterni all'area. Quelli ereditati per transitività si omettono: se X richiede Y e Y richiede Z, in X si scrive solo Y. `⟵ —` indica un nodo radice, senza prerequisiti.
- **⟶ sblocca**: i collegamenti verso altre aree, cioè gli archi uscenti più significativi. È facoltativo.
- **Un nodo intermedio (es. A5.3) richiede tutti i suoi figli**: padroneggiare A5.3 significa padroneggiare A5.3.1…A5.3.n. I prerequisiti si scrivono solo sui nodi foglia.

**Ambito.** L'area A comprende la matematica *nella misura in cui serve all'informatica*. Non è un curricolo completo di matematica: per esempio la geometria euclidea classica compare solo dove serve (vettori, grafica).

---

## A1 Aritmetica e algebra

### A1.1 Insiemi numerici
- **A1.1.1** Numeri naturali: successore, operazioni, ordinamento · [1] · ⟵ —
- **A1.1.2** Interi relativi, valore assoluto · [1] · ⟵ A1.1.1
- **A1.1.3** Razionali: frazioni, rappresentazione decimale limitata e periodica · [1] · ⟵ A1.1.2 · ⟶ B2.5
- **A1.1.4** Reali e irrazionali; approssimazione, cifre significative · [1] · ⟵ A1.1.3 · ⟶ B2.5
- **A1.1.5** Notazione scientifica e ordini di grandezza · [1] · ⟵ A1.1.4, A1.2.1 · ⟶ B3, B2.5

### A1.2 Potenze e logaritmi
- **A1.2.1** Potenze a esponente intero e loro proprietà · [1] · ⟵ A1.1.2
- **A1.2.2** Potenze di 2 e di 10 (tabella da 2⁰ a 2²⁰; 2¹⁰ ≈ 10³) · [1] · ⟵ A1.2.1 · ⟶ B2.1, B3
- **A1.2.3** Radici ed esponenti razionali · [1] · ⟵ A1.2.1, A1.1.4
- **A1.2.4** Funzione esponenziale; crescita esponenziale · [2] · ⟵ A1.2.3, A3.3.1 · ⟶ C9.1
- **A1.2.5** Logaritmi (in particolare log₂), proprietà, cambiamento di base · [2] · ⟵ A1.2.4 · ⟶ E7.1, E9
- **A1.2.6** Confronto di crescite: costante, logaritmica, lineare, n log n, polinomiale, esponenziale, fattoriale · [2] · ⟵ A1.2.5, A3.3.5 · ⟶ E9

### A1.3 Divisibilità
- **A1.3.1** Divisione euclidea: quoziente e resto · [1] · ⟵ A1.1.1 · ⟶ B2.1
- **A1.3.2** Multipli, divisori, criteri di divisibilità · [1] · ⟵ A1.3.1
- **A1.3.3** Numeri primi, crivello di Eratostene, fattorizzazione unica · [1] · ⟵ A1.3.2 · ⟶ E7
- **A1.3.4** MCD e mcm; algoritmo di Euclide · [1] · ⟵ A1.3.3 · ⟶ E2, E7
- **A1.3.5** Identità di Bézout, algoritmo di Euclide esteso · [3] · ⟵ A1.3.4, A1.1.2

### A1.4 Aritmetica modulare
- **A1.4.1** Congruenze, "aritmetica dell'orologio" · [1–2] · ⟵ A1.3.1 · ⟶ B2.4, B12, E6.5
- **A1.4.2** Operazioni modulo n, inverso moltiplicativo · [3] · ⟵ A1.4.1, A1.3.5
- **A1.4.3** Esponenziazione modulare veloce (square-and-multiply) · [3] · ⟵ A1.4.2, A1.2.1 · ⟶ N3.3
- **A1.4.4** Piccolo teorema di Fermat; funzione φ e teorema di Eulero · [3] · ⟵ A1.4.2, A1.3.3 · ⟶ N3.3
- **A1.4.5** Teorema cinese del resto · [3] · ⟵ A1.4.2

### A1.5 Algebra elementare *(nuovo in v1.0)*
- **A1.5.1** Espressioni letterali; la lettera come incognita, parametro, variabile · [1] · ⟵ A1.1.2 · ⟶ E4 (la "variabile" informatica è un concetto diverso: vedi W4)
- **A1.5.2** Equazioni e disequazioni lineari · [1] · ⟵ A1.5.1
- **A1.5.3** Sistemi lineari · [1–2] · ⟵ A1.5.2 · ⟶ A5.1.8
- **A1.5.4** Polinomi; equazioni di secondo grado · [1–2] · ⟵ A1.5.2 · ⟶ A4.4.4
- **A1.5.5** Sommatorie e produttorie (notazione Σ, Π); somme notevoli aritmetiche e geometriche · [2] · ⟵ A1.5.1, A1.2.1 · ⟶ E9

---

## A2 Logica

### A2.1 Logica proposizionale
- **A2.1.1** Enunciati e valori di verità · [1] · ⟵ —
- **A2.1.2** Connettivi NOT, AND, OR · [1] · ⟵ A2.1.1 · ⟶ E3, D1
- **A2.1.3** XOR, implicazione, bicondizionale; NAND e NOR · [1] · ⟵ A2.1.2
- **A2.1.4** Tavole di verità; tautologie e contraddizioni · [1] · ⟵ A2.1.3
- **A2.1.5** Equivalenze logiche; leggi di De Morgan · [1] · ⟵ A2.1.4 · ⟶ D1
- **A2.1.6** Forme normali congiuntiva e disgiuntiva (CNF, DNF) · [2] · ⟵ A2.1.5 · ⟶ D1, F14
- **A2.1.7** Conseguenza logica; regole di inferenza (modus ponens, modus tollens); deduzione naturale · [2–3] · ⟵ A2.1.4
- **A2.1.8** Completezza funzionale (ogni funzione booleana si esprime con i soli NAND) · [2] · ⟵ A2.1.6 · ⟶ C5, D2

### A2.2 Logica dei predicati
- **A2.2.1** Predicati, dominio, variabili libere e vincolate · [2] · ⟵ A2.1.4, A3.1.1
- **A2.2.2** Quantificatori ∀ ed ∃; negazione dei quantificatori · [2] · ⟵ A2.2.1 · ⟶ L5
- **A2.2.3** Formalizzare enunciati del linguaggio naturale · [2] · ⟵ A2.2.2 · ⟶ H11, P2
- **A2.2.4** Interpretazioni e modelli (semantica di Tarski) · [3] · ⟵ A2.2.2, A3.3.1
- **A2.2.5** Forma a clausole, unificazione, risoluzione · [3] · ⟵ A2.2.4, A2.1.6 · ⟶ G3.4, O2.3

### A2.3 Tecniche di dimostrazione
- **A2.3.1** Che cos'è una dimostrazione: ipotesi, tesi, controesempio · [2] · ⟵ A2.1.7
- **A2.3.2** Dimostrazione diretta e per contrapposizione · [2] · ⟵ A2.3.1
- **A2.3.3** Dimostrazione per assurdo · [2] · ⟵ A2.3.1 · ⟶ A3.4.3, F4
- **A2.3.4** Induzione matematica (semplice e forte) · [2] · ⟵ A2.3.2, A1.5.5 · ⟶ E5, E9
- **A2.3.5** Induzione strutturale (su liste, alberi, formule) · [3] · ⟵ A2.3.4, A3.5 · ⟶ F2, G3.3
- **A2.3.6** Invarianti: dimostrare che una proprietà si conserva a ogni passo · [2–3] · ⟵ A2.3.4 · ⟶ E9, F8

### A2.4 Sistemi formali · [3]
- **A2.4.1** Sintassi e semantica di un linguaggio logico · [3] · ⟵ A2.2.4
- **A2.4.2** Assiomi e regole di inferenza; derivazioni · [3] · ⟵ A2.4.1, A2.1.7
- **A2.4.3** Correttezza e completezza (teorema di completezza di Gödel) · [3] · ⟵ A2.4.2
- **A2.4.4** Decidibilità della logica proposizionale; semi-decidibilità della logica del primo ordine · [3–4] · ⟵ A2.4.3, F4.2 · ⟶ F9

### A2.5 Incompletezza · [4]
- **A2.5.1** Aritmetica di Peano · [4] · ⟵ A2.4.2, A2.3.4
- **A2.5.2** Teoremi di incompletezza di Gödel e loro legame con il problema della fermata · [4] · ⟵ A2.5.1, F4.2 · ⟶ U2

### A2.6 Logiche non classiche
- **A2.6.1** Logiche a più valori (a tre valori: il NULL di SQL) · [2–3] · ⟵ A2.1.4 · ⟶ L5
- **A2.6.2** Logica fuzzy: gradi di verità · [3] · ⟵ A2.1.4, A3.3.1 · ⟶ O3, R4
- **A2.6.3** Logica modale: necessità e possibilità · [4] · ⟵ A2.2.4
- **A2.6.4** Logiche temporali (LTL, CTL) · [4] · ⟵ A2.6.3 · ⟶ F9
- **A2.6.5** Logica intuizionista · [4] · ⟵ A2.4.2 · ⟶ F7

---

## A3 Insiemi, relazioni, funzioni

### A3.1 Insiemi
- **A3.1.1** Insieme e appartenenza; rappresentazioni per elencazione, per proprietà, con diagrammi di Venn · [1] · ⟵ —
- **A3.1.2** Sottoinsiemi, insieme vuoto, insieme delle parti · [1] · ⟵ A3.1.1 · ⟶ A4.1.1
- **A3.1.3** Unione, intersezione, differenza, complemento; corrispondenza con i connettivi logici · [1] · ⟵ A3.1.1, A2.1.2 · ⟶ L4
- **A3.1.4** Prodotto cartesiano; coppie e n-uple · [1–2] · ⟵ A3.1.3 · ⟶ L4
- **A3.1.5** Alfabeti, stringhe, sequenze; multiinsiemi · [2] · ⟵ A3.1.4 · ⟶ B1, F1

### A3.2 Relazioni
- **A3.2.1** Relazione binaria; rappresentazioni con matrice e con grafo · [1–2] · ⟵ A3.1.4 · ⟶ L4
- **A3.2.2** Proprietà: riflessiva, simmetrica, antisimmetrica, transitiva · [2] · ⟵ A3.2.1
- **A3.2.3** Relazioni di equivalenza, classi, partizioni · [2] · ⟵ A3.2.2
- **A3.2.4** Ordini parziali e totali; diagrammi di Hasse · [2–3] · ⟵ A3.2.2 · ⟶ E7.2
- **A3.2.5** Chiusura transitiva · [3] · ⟵ A3.2.2 · ⟶ E7.3, L5 (interrogazioni ricorsive)

### A3.3 Funzioni
- **A3.3.1** Funzione come relazione; dominio, codominio, immagine · [1–2] · ⟵ A3.2.1 · ⟶ G1
- **A3.3.2** Funzioni iniettive, suriettive, biiettive; funzione inversa · [2] · ⟵ A3.3.1 · ⟶ B1 (una codifica è una funzione iniettiva), N3
- **A3.3.3** Composizione di funzioni · [2] · ⟵ A3.3.1 · ⟶ G3.3
- **A3.3.4** Funzioni parziali, funzioni di più argomenti, currying · [3] · ⟵ A3.3.3, A3.1.4 · ⟶ F6
- **A3.3.5** Funzioni notevoli per l'informatica: parte intera inferiore e superiore, mod, fattoriale · [2] · ⟵ A3.3.1, A1.3.1 · ⟶ E9

### A3.4 Cardinalità
- **A3.4.1** Cardinalità finita; corrispondenza biunivoca · [1] · ⟵ A3.1.1
- **A3.4.2** Insiemi infiniti numerabili · [3] · ⟵ A3.4.1, A3.3.2
- **A3.4.3** Diagonalizzazione di Cantor; insiemi non numerabili · [3] · ⟵ A3.4.2, A2.3.3 · ⟶ F4

### A3.5 Definizioni ricorsive di insiemi e funzioni *(nuovo in v1.0)* · [2–3]
- **A3.5** Definire per casi base e casi induttivi (numeri naturali, liste, alberi, espressioni) · [2–3] · ⟵ A3.3.1 · ⟶ E5, F2

---

## A4 Matematica discreta

### A4.1 Combinatoria
- **A4.1.1** Principi della somma e del prodotto; configurazioni possibili con n bit (2ⁿ) · [1] · ⟵ A1.2.1, A3.1.2 · ⟶ B2.1, B3
- **A4.1.2** Permutazioni, disposizioni, combinazioni · [2] · ⟵ A4.1.1, A3.3.5
- **A4.1.3** Coefficienti binomiali, triangolo di Tartaglia · [2] · ⟵ A4.1.2
- **A4.1.4** Principio dei cassetti · [2] · ⟵ A4.1.1 · ⟶ E6.5 (collisioni), B9 (limiti della compressione)
- **A4.1.5** Principio di inclusione-esclusione · [3] · ⟵ A4.1.2, A3.1.3
- **A4.1.6** Funzioni generatrici · [4] · ⟵ A4.1.3, A6.1.5

### A4.2 Successioni e ricorrenze
- **A4.2.1** Successioni definite per ricorrenza (Fibonacci) · [2] · ⟵ A3.5 · ⟶ E5
- **A4.2.2** Progressioni aritmetiche e geometriche · [2] · ⟵ A1.5.5
- **A4.2.3** Soluzione di ricorrenze lineari · [3] · ⟵ A4.2.1, A1.5.4
- **A4.2.4** Ricorrenze "divide et impera" e teorema master · [3] · ⟵ A4.2.1, A1.2.5 · ⟶ E9
- **A4.2.5** La successione di Fibonacci e il rapporto aureo · [2–3] · ⟵ A4.2.1 · (v1.1, approfondimento)

### A4.3 Teoria dei grafi
- **A4.3.1** Grafo: nodi, archi; orientato e non orientato; pesato · [1–2] · ⟵ A3.2.1 · ⟶ E6.6
- **A4.3.2** Grado, cammini, cicli, connessione (i ponti di Königsberg) · [2] · ⟵ A4.3.1
- **A4.3.3** Alberi: radice, foglie, altezza; alberi ricoprenti · [2] · ⟵ A4.3.2 · ⟶ E6.4
- **A4.3.4** Grafi orientati aciclici (DAG) e ordinamento topologico · [2–3] · ⟵ A4.3.2, A3.2.4 · ⟶ H7, E7.3 (è anche la struttura di questa mappa)
- **A4.3.5** Grafi bipartiti e abbinamenti (matching) · [3] · ⟵ A4.3.2
- **A4.3.6** Grafi planari e colorazione · [3] · ⟵ A4.3.2 · ⟶ G7.2 (allocazione dei registri)
- **A4.3.7** Cammini euleriani e hamiltoniani · [2–3] · ⟵ A4.3.2 · ⟶ F5
- **A4.3.8** Grafi casuali, reti small-world e a invarianza di scala · [4] · ⟵ A4.3.2, A7.3.1 · ⟶ S14

### A4.4 Strutture algebriche
- **A4.4.1** Operazioni e proprietà: associativa, commutativa, elemento neutro, inverso · [2] · ⟵ A3.3.1 · ⟶ G3.3 (fold/reduce su monoidi), M2
- **A4.4.2** Gruppi, gruppi ciclici · [3] · ⟵ A4.4.1, A1.4.2 · ⟶ N3.3
- **A4.4.3** Anelli e campi; ℤₚ · [3] · ⟵ A4.4.2
- **A4.4.4** Polinomi su campi finiti; campi di Galois GF(2ⁿ) · [4] · ⟵ A4.4.3, A1.5.4 · ⟶ B10.2, B10.3, N3.1
- **A4.4.5** Reticoli d'ordine e algebre di Boole come struttura · [3] · ⟵ A3.2.4, A4.4.1 · ⟶ D1
- **A4.4.6** Curve ellittiche su campi finiti · [4] · ⟵ A4.4.3 · ⟶ N3.3

---

## A5 Algebra lineare

### A5.1 Vettori e matrici
- **A5.1.1** Vettori nel piano e nello spazio; componenti · [1–2] · ⟵ A1.1.4 · ⟶ Q1
- **A5.1.2** Somma di vettori e prodotto per uno scalare · [2] · ⟵ A5.1.1
- **A5.1.3** Prodotto scalare, norma, distanza, similarità del coseno · [2] · ⟵ A5.1.2, A6.1.2 · ⟶ O4.1 (k-NN), P6
- **A5.1.4** Prodotto vettoriale · [2] · ⟵ A5.1.2 · ⟶ Q2
- **A5.1.5** Matrici e operazioni elementari; un'immagine come matrice · [2] · ⟵ A5.1.2 · ⟶ E6.1, B6
- **A5.1.6** Prodotto matriciale · [2] · ⟵ A5.1.5, A5.1.3 · ⟶ O5.1
- **A5.1.7** Determinante e matrice inversa · [2–3] · ⟵ A5.1.6
- **A5.1.8** Risoluzione di sistemi lineari: eliminazione di Gauss · [2–3] · ⟵ A5.1.5, A1.5.3 · ⟶ A10.3

### A5.2 Spazi vettoriali e trasformazioni lineari
- **A5.2.1** Spazio vettoriale, indipendenza lineare, base, dimensione · [3] · ⟵ A5.1.2
- **A5.2.2** Trasformazioni lineari come matrici (rotazione, scala, riflessione) · [2–3] · ⟵ A5.1.6, A6.1.2 · ⟶ Q1, R6.1
- **A5.2.3** Coordinate omogenee e trasformazioni affini · [3] · ⟵ A5.2.2 · ⟶ Q2
- **A5.2.4** Ortogonalità, proiezioni, minimi quadrati · [3] · ⟵ A5.2.1, A5.1.3 · ⟶ O4.1 (regressione)

### A5.3 Autovalori e decomposizioni
- **A5.3.1** Autovalori e autovettori · [3] · ⟵ A5.2.2, A5.1.7
- **A5.3.2** Diagonalizzazione; decomposizione ai valori singolari (SVD) · [3–4] · ⟵ A5.3.1, A5.2.4 · ⟶ O4.2 (PCA), L12
- **A5.3.3** Matrici stocastiche e vettore stazionario · [3] · ⟵ A5.3.1, A7.2.2 · ⟶ L11 (PageRank), A7.5.2

### A5.4 Numeri complessi e algebra lineare per il calcolo quantistico
- **A5.4.1** Numeri complessi: forma algebrica, trigonometrica, esponenziale · [2–3] · ⟵ A1.5.4, A6.1.2 · ⟶ A6.5.2
- **A5.4.2** Spazi vettoriali complessi, prodotto hermitiano, notazione di Dirac (bra-ket) · [4] · ⟵ A5.4.1, A5.2.1 · ⟶ T1
- **A5.4.3** Matrici unitarie ed hermitiane · [4] · ⟵ A5.4.2, A5.3.1 · ⟶ T3
- **A5.4.4** Prodotto tensoriale · [4] · ⟵ A5.4.2 · ⟶ T2 (entanglement)

---

## A6 Analisi

### A6.1 Funzioni reali
- **A6.1.1** Funzioni elementari e loro grafici: lineari, quadratiche, esponenziali, logaritmiche · [2] · ⟵ A3.3.1, A1.2.5
- **A6.1.2** Funzioni trigonometriche; oscillazioni: periodo, frequenza, fase · [2] · ⟵ A6.1.1 · ⟶ B7, J1
- **A6.1.3** Limiti e comportamento asintotico · [2] · ⟵ A6.1.1 · ⟶ E9 (le notazioni O/Ω/Θ sono definite tramite limiti)
- **A6.1.4** Continuità · [2] · ⟵ A6.1.3
- **A6.1.5** Successioni e serie numeriche; convergenza · [2–3] · ⟵ A6.1.3, A4.2.2

### A6.2 Calcolo differenziale
- **A6.2.1** Derivata come tasso di variazione · [2] · ⟵ A6.1.4
- **A6.2.2** Regole di derivazione; regola della catena · [2] · ⟵ A6.2.1 · ⟶ O5.1 (backpropagation)
- **A6.2.3** Massimi e minimi · [2] · ⟵ A6.2.2 · ⟶ A9
- **A6.2.4** Funzioni di più variabili, derivate parziali, gradiente · [3] · ⟵ A6.2.2, A5.1.2
- **A6.2.5** Discesa del gradiente · [3] · ⟵ A6.2.4, A6.2.3 · ⟶ A9.2.1, O4.1, O5.1
- **A6.2.6** Differenziazione automatica sul grafo computazionale · [3–4] · ⟵ A6.2.2, A4.3.4 · ⟶ O5.1
- **A6.2.7** Serie di Taylor e approssimazione polinomiale · [3] · ⟵ A6.2.2, A6.1.5 · ⟶ A10.1

### A6.3 Calcolo integrale
- **A6.3.1** Integrale come area e come accumulo · [2] · ⟵ A6.1.4
- **A6.3.2** Teorema fondamentale del calcolo; tecniche di integrazione · [2–3] · ⟵ A6.3.1, A6.2.2
- **A6.3.3** Integrali multipli · [3] · ⟵ A6.3.2, A6.2.4 · ⟶ A7.3.5, Q2 (rendering)

### A6.4 Equazioni differenziali
- **A6.4.1** Modelli dinamici elementari: crescita e decadimento · [2–3] · ⟵ A6.2.1, A1.2.4 · ⟶ S1
- **A6.4.2** Equazioni differenziali ordinarie lineari di 1° e 2° ordine; oscillatori · [3] · ⟵ A6.4.1, A6.3.2 · ⟶ C2 (circuiti RC), R4
- **A6.4.3** Sistemi di equazioni differenziali; stabilità degli equilibri · [3] · ⟵ A6.4.2, A5.3.1 · ⟶ R4
- **A6.4.4** Soluzione numerica (metodi di Eulero e di Runge-Kutta) · [3] · ⟵ A6.4.1, A10.1.1 · ⟶ S1, Q3
- **A6.4.5** Equazioni alle derivate parziali (calore, onde) · [4] · ⟵ A6.4.2, A6.2.4 · ⟶ S15
- **A6.4.6** Trasformata di Laplace e funzione di trasferimento · [3] · ⟵ A6.4.2, A5.4.1 · ⟶ R4

### A6.5 Analisi di Fourier e segnali
- **A6.5.1** Idea di spettro: un segnale come somma di sinusoidi · [2] · ⟵ A6.1.2 · ⟶ B7, Q6
- **A6.5.2** Serie di Fourier · [3] · ⟵ A6.5.1, A6.3.2, A5.4.1
- **A6.5.3** Trasformata di Fourier continua · [3] · ⟵ A6.5.2
- **A6.5.4** Trasformata discreta (DFT) e algoritmo FFT · [3] · ⟵ A6.5.3, E8 · ⟶ B9.2, P9, Q4
- **A6.5.5** Convoluzione e filtri · [3] · ⟵ A6.5.3 · ⟶ Q4, O5.2
- **A6.5.6** Trasformata coseno discreta (DCT) e wavelet · [3–4] · ⟵ A6.5.4 · ⟶ B9.2 (JPEG, MP3)
- **A6.5.7** Campionamento e aliasing (fondamento del teorema di Nyquist-Shannon) · [3] · ⟵ A6.5.3 · ⟶ B7, C7

---

## A7 Probabilità e statistica

### A7.1 Statistica descrittiva
- **A7.1.1** Popolazione e campione; variabili qualitative e quantitative · [1] · ⟵ —
- **A7.1.2** Distribuzioni di frequenza; tabelle e grafici · [1] · ⟵ A7.1.1 · ⟶ L2, Q9
- **A7.1.3** Media, mediana, moda · [1] · ⟵ A7.1.2
- **A7.1.4** Varianza, deviazione standard, quartili · [1–2] · ⟵ A7.1.3, A1.2.3
- **A7.1.5** Correlazione e regressione lineare semplice · [2] · ⟵ A7.1.4 · ⟶ O4.1
- **A7.1.6** Correlazione e causalità; paradosso di Simpson · [2] · ⟵ A7.1.5 · ⟶ U3, L9

### A7.2 Probabilità
- **A7.2.1** Esperimento aleatorio, spazio campionario, eventi · [1–2] · ⟵ A3.1.3
- **A7.2.2** Definizioni di probabilità (classica, frequentista, soggettiva); assiomi · [2] · ⟵ A7.2.1, A4.1.2
- **A7.2.3** Probabilità condizionata e indipendenza · [2] · ⟵ A7.2.2
- **A7.2.4** Teorema di Bayes · [2] · ⟵ A7.2.3 · ⟶ O3 (es. filtri antispam)
- **A7.2.5** Numeri pseudocasuali e generatori · [2] · ⟵ A7.2.2, A1.4.1 · ⟶ S1, N3
- **A7.2.6** Il problema di Monty Hall simulato · [2] · ⟵ A7.2.3 · (v1.1, approfondimento)

### A7.3 Variabili aleatorie
- **A7.3.1** Variabili discrete: Bernoulli, binomiale, geometrica, Poisson · [2] · ⟵ A7.2.3, A4.1.3
- **A7.3.2** Valore atteso e varianza · [2] · ⟵ A7.3.1, A7.1.4 · ⟶ E9 (caso medio), E10
- **A7.3.3** Variabili continue: uniforme, esponenziale, normale · [2–3] · ⟵ A7.3.2, A6.3.1
- **A7.3.4** Legge dei grandi numeri e teorema del limite centrale · [3] · ⟵ A7.3.3 · ⟶ S1 (Monte Carlo)
- **A7.3.5** Distribuzioni congiunte, covarianza · [3] · ⟵ A7.3.3, A6.3.3 · ⟶ O4
- **A7.3.6** Disuguaglianze di concentrazione (Markov, Čebyšëv, Chernoff) · [4] · ⟵ A7.3.4 · ⟶ E10, F12

### A7.4 Statistica inferenziale
- **A7.4.1** Stimatori e intervalli di confidenza · [3] · ⟵ A7.3.4
- **A7.4.2** Test di ipotesi e p-value · [3] · ⟵ A7.4.1 · ⟶ Q15, H15
- **A7.4.3** Stima di massima verosimiglianza · [3] · ⟵ A7.4.1, A6.2.3 · ⟶ O4
- **A7.4.4** Inferenza bayesiana · [3–4] · ⟵ A7.4.3, A7.2.4 · ⟶ O3
- **A7.4.5** Esperimenti controllati e A/B test · [3] · ⟵ A7.4.2 · ⟶ K11
- **A7.4.6** Ricampionamento: bootstrap e validazione incrociata · [3] · ⟵ A7.4.1 · ⟶ O4.3

### A7.5 Processi stocastici
- **A7.5.1** Catene di Markov: stati e matrice di transizione · [3] · ⟵ A7.2.3, A5.1.6 · ⟶ P5
- **A7.5.2** Distribuzione stazionaria · [3] · ⟵ A7.5.1, A5.3.3
- **A7.5.3** Passeggiate aleatorie · [3] · ⟵ A7.5.1 · ⟶ L11
- **A7.5.4** Processi di Poisson e teoria delle code (M/M/1) · [3] · ⟵ A7.5.1, A7.3.3 · ⟶ I12, J6
- **A7.5.5** Processi decisionali di Markov (MDP) · [3–4] · ⟵ A7.5.1, A7.3.2 · ⟶ O4.4
- **A7.5.6** Modelli di Markov nascosti (HMM) · [4] · ⟵ A7.5.1, A7.4.3 · ⟶ P6, P9, S2.4

---

## A8 Teoria dell'informazione

### A8.1 Informazione ed entropia
- **A8.1.1** Quantità di informazione di un evento (−log₂ p); il bit come unità di misura · [2] · ⟵ A1.2.5, A7.2.2 · ⟶ B1
- **A8.1.2** Entropia di una sorgente · [2–3] · ⟵ A8.1.1, A7.3.2
- **A8.1.3** Entropia congiunta e condizionata; informazione mutua · [3] · ⟵ A8.1.2, A7.2.3 · ⟶ O4.1 (alberi di decisione)
- **A8.1.4** Ridondanza del linguaggio naturale (esperimento di Shannon) · [2–3] · ⟵ A8.1.2 · ⟶ P4, N2

### A8.2 Codifica di sorgente
- **A8.2.1** Codici a lunghezza fissa e variabile; codici prefissi · [2] · ⟵ A3.1.5, A4.3.3 · ⟶ B4 (UTF-8)
- **A8.2.2** Disuguaglianza di Kraft · [3] · ⟵ A8.2.1
- **A8.2.3** Primo teorema di Shannon (limite alla compressione) · [3] · ⟵ A8.2.2, A8.1.2
- **A8.2.4** Codifica di Huffman e codifica aritmetica · [2–3] · ⟵ A8.2.1, A8.1.2 · ⟶ B9.1

### A8.3 Canale e rumore
- **A8.3.1** Modelli di canale (canale binario simmetrico); il rumore · [3] · ⟵ A8.1.2, A7.3.1 · ⟶ J1
- **A8.3.2** Capacità di canale; secondo teorema di Shannon · [3] · ⟵ A8.3.1, A8.1.3
- **A8.3.3** Distanza di Hamming; ridondanza per rilevare e correggere errori · [2] · ⟵ A3.1.5, A4.1.1 · ⟶ B10

### A8.4 Informazione e apprendimento
- **A8.4.1** Entropia incrociata · [3] · ⟵ A8.1.2 · ⟶ O5.1
- **A8.4.2** Divergenza di Kullback-Leibler · [3–4] · ⟵ A8.4.1 · ⟶ O6
- **A8.4.3** Principio di minima lunghezza di descrizione (MDL) · [4] · ⟵ A8.2.3 · ⟶ F10

---

## A9 Ottimizzazione e ricerca operativa

### A9.1 Programmazione lineare e intera
- **A9.1.1** Modellare un problema di ottimizzazione: variabili decisionali, vincoli, funzione obiettivo · [2] · ⟵ A1.5.2
- **A9.1.2** Programmazione lineare in due variabili: metodo grafico · [2] · ⟵ A9.1.1, A1.5.3
- **A9.1.3** Metodo del simplesso; dualità · [3] · ⟵ A9.1.2, A5.1.8
- **A9.1.4** Programmazione intera; branch and bound · [3] · ⟵ A9.1.3, E8
- **A9.1.5** Problemi classici: zaino, commesso viaggiatore, scheduling, flussi su reti · [3] · ⟵ A9.1.1, A4.3.2 · ⟶ F5

### A9.2 Ottimizzazione continua
- **A9.2.1** Ottimizzazione non vincolata · [3] · ⟵ A6.2.5
- **A9.2.2** Funzioni e insiemi convessi · [3] · ⟵ A9.2.1
- **A9.2.3** Metodi stocastici (SGD, Adam) · [3–4] · ⟵ A9.2.1, A7.3.2 · ⟶ O5.1
- **A9.2.4** Ottimizzazione vincolata; moltiplicatori di Lagrange · [3] · ⟵ A9.2.2 · ⟶ O4.1 (SVM)

### A9.3 Euristiche e metaeuristiche
- **A9.3.1** Ricerca locale, hill climbing · [2–3] · ⟵ A9.1.1
- **A9.3.2** Simulated annealing, tabu search · [3] · ⟵ A9.3.1, A7.2.2
- **A9.3.3** Algoritmi genetici · [3] · ⟵ A9.3.1, A7.2.5 · ⟶ O8
- **A9.3.4** Ottimizzazione multi-obiettivo; frontiera di Pareto · [3–4] · ⟵ A9.1.1, A3.2.4

### A9.4 Decisioni e giochi (base) *(nuovo in v1.0)*
- **A9.4.1** Decisioni in condizioni di incertezza; utilità attesa · [2–3] · ⟵ A7.3.2
- **A9.4.2** Giochi in forma normale; dilemma del prigioniero; equilibrio di Nash · [2–3] · ⟵ A9.4.1 · ⟶ F11, O12
- **A9.4.3** Giochi a somma zero e strategia minimax · [2–3] · ⟵ A9.4.2 · ⟶ O2.2

---

## A10 Analisi numerica

### A10.1 Errori
- **A10.1.1** Errore assoluto e relativo · [2] · ⟵ A1.1.4
- **A10.1.2** Aritmetica in virgola mobile: epsilon di macchina, cancellazione numerica · [2–3] · ⟵ A10.1.1, B2.5.5
- **A10.1.3** Condizionamento di un problema e stabilità di un algoritmo · [3] · ⟵ A10.1.2, A6.2.1
- **A10.1.4** Incidenti causati da errori numerici (missile Patriot) · [3] · ⟵ A10.1.2 · (v1.1, approfondimento)
- **A10.1.5** Aritmetica esatta: frazioni e decimali a precisione arbitraria in Python · [3] · ⟵ A10.1.2 · (v1.1, approfondimento)

### A10.2 Metodi numerici di base
- **A10.2.1** Zeri di funzioni: bisezione e metodo di Newton · [2–3] · ⟵ A6.1.4, A6.2.1
- **A10.2.2** Interpolazione polinomiale e spline · [3] · ⟵ A1.5.4, A5.1.8 · ⟶ Q11
- **A10.2.3** Integrazione numerica (trapezi, Simpson) · [3] · ⟵ A6.3.1, A10.1.1
- **A10.2.4** Metodo delle secanti e regula falsi · [3] · ⟵ A10.2.1 · (v1.1, approfondimento)
- **A10.2.5** Il metodo di Erone per la radice quadrata come caso del metodo di Newton · [3] · ⟵ A6.2.2 · (v1.1, approfondimento)
- **A10.2.6** Lunghezze di curve e volumi calcolati numericamente · [3] · ⟵ A10.2.3 · (v1.1, approfondimento)
- **A10.2.7** Integrare numericamente dati sperimentali (dalla velocità allo spazio) · [3] · ⟵ A10.2.3 · (v1.1, approfondimento)
- *(L'integrazione numerica delle equazioni differenziali è A6.4.4.)*

### A10.3 Algebra lineare numerica
- **A10.3.1** Fattorizzazione LU; metodi iterativi (Jacobi, Gauss-Seidel) · [3] · ⟵ A5.1.8, A10.1.3
- **A10.3.2** Matrici sparse · [3–4] · ⟵ A10.3.1, E6.1 · ⟶ S15, L11
- **A10.3.3** Calcolo numerico degli autovalori (metodo delle potenze) · [3] · ⟵ A5.3.1, A10.3.1 · ⟶ L11

---

## A11 Teoria dei numeri computazionale · [3–4]
- **A11.1** Test di primalità probabilistici (Miller-Rabin) · [3–4] · ⟵ A1.4.4, A7.2.3 · ⟶ N3.3
- **A11.2** Fattorizzazione di interi e sua difficoltà computazionale · [4] · ⟵ A1.3.3, A1.4.3 · ⟶ N3.3, T4
- **A11.3** Logaritmo discreto · [4] · ⟵ A4.4.2, A1.4.3 · ⟶ N3.3
- **A11.4** Reticoli (lattice) e problemi difficili su reticolo · [4] · ⟵ A5.2.1, A11.2 · ⟶ N10

---

## Riepiloghi per il grafo

**Nodi radice (nessun prerequisito):** A1.1.1 (naturali), A2.1.1 (enunciati), A3.1.1 (insiemi), A7.1.1 (popolazione e campione). Sono i punti d'ingresso da cui può partire qualsiasi percorso.

**Dipendenze esterne all'area A (archi entranti da altre aree, verificate automaticamente):**
| Nodo | Prerequisito esterno | Motivo |
|---|---|---|
| A2.4.4, A2.5.2 | F4.2 (problema della fermata) | decidibilità e incompletezza si capiscono insieme alla fermata |
| A6.5.4, A9.1.4 | E8 (tecniche di progetto) | FFT e branch and bound sono algoritmi |
| A10.1.2 | B2.5.5 (errori di rappresentazione) | l'errore di macchina dipende dalla rappresentazione |
| A10.3.2 | E6.1 (array e matrici) | le matrici sparse sono una struttura dati |

Nota: con F4.2 non si forma un ciclo, perché F4 dipende da A3.4 e non da A2.4 o A2.5.

**Percorso minimo verso la programmazione** (per il primo biennio):
A1.1.1 → A1.2.1 → A1.2.2 → A4.1.1 (2ⁿ configurazioni) · A2.1.1 → A2.1.4 → A2.1.5 · A3.1.1 → A3.1.3 · A1.3.1 (quoziente e resto). Bastano questi nodi per affrontare B2 (binario) ed E3 (strutture di controllo).

**Statistiche v1.0:** 11 rami, 45 sotto-rami, 218 nodi foglia. Il controllo automatico ha dato questi esiti: tutti i prerequisiti interni esistono, il grafo interno è aciclico, 4 radici, 6 archi entranti da altre aree.

## Registro modifiche
- **v1.0 (27/09/2026)**: primo dettaglio dell'area. Nodi nuovi rispetto al documento madre: A1.5 (algebra elementare), A3.5 (definizioni ricorsive), A9.4 (decisioni e giochi). Tutti gli ID del documento madre sono stati conservati.
