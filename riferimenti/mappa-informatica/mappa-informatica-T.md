# Mappa dell'informatica — Area T: Calcolo quantistico e paradigmi non convenzionali (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** calcolo quantistico (qubit, circuiti, algoritmi, complessità, hardware, correzione degli errori, programmazione, comunicazione) e altri paradigmi di calcolo non convenzionali (DNA, neuromorfico, ottico, analogico, reversibile). L'area è quasi tutta di livello `[3–4]`, ma ha alcune porte d'ingresso divulgative a livello `[2]`: T1.1, T2.1, T5.3, T6.6, T8.1.

---

## T1 Prerequisiti e motivazioni
- **T1.1** Perché un computer quantistico: i limiti del calcolo classico e l'idea di Feynman · [2] · ⟵ C9.1
- **T1.2** Richiamo: numeri e vettori complessi · [4] · ⟵ A5.4.1, A5.4.2
- **T1.3** Richiamo: probabilità e misura · [3] · ⟵ A7.2.2, C15.3
- **T1.4** I postulati della meccanica quantistica visti dall'informatica · [4] · ⟵ C15.5, T1.2

## T2 Il qubit
- **T2.1** Dal bit al qubit: la sovrapposizione (visione intuitiva) · [2] · ⟵ B1.5, T1.1
- **T2.2** Il qubit come vettore; notazione di Dirac · [4] · ⟵ T2.1, T1.2
- **T2.3** La sfera di Bloch · [4] · ⟵ T2.2
- **T2.4** La misura e la regola di Born · [4] · ⟵ T2.2, T1.3
- **T2.5** Più qubit e prodotto tensoriale · [4] · ⟵ T2.2, A5.4.4
- **T2.6** Entanglement e stati di Bell · [4] · ⟵ T2.5
- **T2.7** Teorema di non clonazione · [4] · ⟵ T2.2, A5.4.3

## T3 Circuiti quantistici
- **T3.1** Calcolo reversibile; porte classiche reversibili (Toffoli) · [3] · ⟵ D2.1, A3.3.2
- **T3.2** Porte a un qubit: X, Z, H, di fase · [4] · ⟵ T2.3, A5.4.3
- **T3.3** Porte a due qubit: CNOT · [4] · ⟵ T3.2, T2.5
- **T3.4** Circuiti quantistici e loro simulazione · [4] · ⟵ T3.3
- **T3.5** Universalità degli insiemi di porte quantistiche · [4] · ⟵ T3.3
- **T3.6** Teletrasporto quantistico e codifica superdensa · [4] · ⟵ T3.3, T2.6

## T4 Algoritmi quantistici
- **T4.1** Parallelismo quantistico e interferenza · [4] · ⟵ T3.4
- **T4.2** Algoritmi di Deutsch e Deutsch-Jozsa · [4] · ⟵ T4.1
- **T4.3** Algoritmi di Bernstein-Vazirani e di Simon · [4] · ⟵ T4.2
- **T4.4** Algoritmo di Grover · [4] · ⟵ T4.1
- **T4.5** Trasformata di Fourier quantistica e stima di fase · [4] · ⟵ T4.1, A6.5.4
- **T4.6** Algoritmo di Shor · [4] · ⟵ T4.5, A11.2
- **T4.7** Algoritmi variazionali (VQE, QAOA) · [4] · ⟵ T4.1, A9.2.1
- **T4.8** Simulazione di sistemi quantistici · [4] · ⟵ T4.5 · ⟶ S4.3
- **T4.9** Apprendimento automatico quantistico · [4] · ⟵ T4.7, O4.1.2

## T5 Complessità quantistica
- **T5.1** La classe BQP · [4] · ⟵ T4.2, F5.2
- **T5.2** Vantaggio quantistico: esperimenti e controversie · [4] · ⟵ T5.1
- **T5.3** Che cosa i computer quantistici sanno (e non sanno) fare: miti e realtà · [2–3] · ⟵ T2.1

## T6 Hardware quantistico
- **T6.1** I requisiti di DiVincenzo · [4] · ⟵ T3.4
- **T6.2** Qubit superconduttori · [4] · ⟵ T6.1
- **T6.3** Ioni intrappolati e atomi neutri · [4] · ⟵ T6.1
- **T6.4** Qubit fotonici · [4] · ⟵ T6.1, C14.3
- **T6.5** Decoerenza e rumore; l'era NISQ · [4] · ⟵ T2.4
- **T6.6** Stato dell'arte e piani dei produttori · [2–3] · ⟵ T5.3

## T7 Correzione degli errori quantistici
- **T7.1** Errori quantistici: bit flip e phase flip · [4] · ⟵ T6.5, T3.2
- **T7.2** Codici a ripetizione quantistici e codice di Shor · [4] · ⟵ T7.1, B10.3.2
- **T7.3** Codici di superficie e qubit logici · [4] · ⟵ T7.2
- **T7.4** Calcolo tollerante ai guasti e teorema della soglia · [4] · ⟵ T7.3

## T8 Programmazione quantistica
- **T8.1** Editor visuali e simulatori di circuiti (Quirk, IBM Quantum Composer) · [2–3] · ⟵ T2.1, D1.2
- **T8.2** Programmare con Qiskit o Cirq · [4] · ⟵ T3.4, G2.2.10
- **T8.3** Eseguire su hardware reale nel cloud · [4] · ⟵ T8.2, T6.5

## T9 Comunicazione quantistica
- **T9.1** Distribuzione quantistica delle chiavi: protocollo BB84 · [4] · ⟵ T2.4, T2.7, N3.3.1
- **T9.2** Protocolli basati sull'entanglement (E91) · [4] · ⟵ T9.1, T2.6
- **T9.3** Reti quantistiche e ripetitori · [4] · ⟵ T9.2, T3.6

## T10 Paradigmi di calcolo non convenzionali

### T10.1 Calcolo con il DNA
- **T10.1.1** L'esperimento di Adleman (1994) · [3] · ⟵ S2.2.1, A4.3.7
- **T10.1.2** Memorizzare dati nel DNA · [3] · ⟵ S2.2.1, B10.3.2

### T10.2 Calcolo neuromorfico
- **T10.2.1** Reti neurali a impulsi · [4] · ⟵ S3.2, O5.1.1
- **T10.2.2** Chip neuromorfici · [4] · ⟵ T10.2.1, D12.5

### T10.3 Calcolo ottico
- **T10.3.1** Calcolo ottico e fotonico · [4] · ⟵ C18.5

### T10.4 Altri paradigmi
- **T10.4.1** Calcolo analogico, storico e moderno · [3] · ⟵ C6.1
- **T10.4.2** Calcolo reversibile e limite di Landauer · [4] · ⟵ T3.1, A8.1.2
- **T10.4.3** Calcolo stocastico e probabilistico in hardware · [4] · ⟵ C5.1, A7.3.1
- **T10.4.4** Calcolo con materiali e sistemi biologici (reservoir computing, organoidi) · [4] · ⟵ T10.2.1
