# Mappa dell'informatica — Area D: Architettura degli elaboratori (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** dalla logica booleana alla CPU completa: reti logiche, modello di von Neumann, set di istruzioni, assembly, memorie, I/O, prestazioni, parallelismo hardware. La realizzazione fisica delle porte logiche è nell'area C; la gestione software delle risorse è nell'area I.

---

## D1 Algebra di Boole
- **D1.1** Variabili e funzioni booleane; tabella di verità di una funzione · [1] · ⟵ A2.1.4
- **D1.2** Operatori e porte logiche AND, OR, NOT, NAND, NOR, XOR e i loro simboli · [1] · ⟵ D1.1, A2.1.3
- **D1.3** Proprietà e teoremi dell'algebra di Boole; De Morgan · [1–2] · ⟵ D1.2, A2.1.5
- **D1.4** Semplificazione algebrica · [2] · ⟵ D1.3
- **D1.5** Forme canoniche: mintermini e maxtermini · [2] · ⟵ D1.3, A2.1.6
- **D1.6** Mappe di Karnaugh · [2] · ⟵ D1.5
- **D1.7** Condizioni di indifferenza (don't care) · [2] · ⟵ D1.6
- **D1.8** Metodo di Quine-McCluskey · [3] · ⟵ D1.6

## D2 Reti logiche combinatorie
- **D2.1** Dal problema alla tabella di verità allo schema del circuito · [1–2] · ⟵ D1.2
- **D2.2** Simulatori di circuiti logici (Logisim, Digital) · [1] · ⟵ D1.2
- **D2.3** Multiplexer e demultiplexer · [2] · ⟵ D2.1
- **D2.4** Codificatori e decodificatori; decodificatore per display a 7 segmenti · [2] · ⟵ D2.1, B2.6.1
- **D2.5** Comparatori · [2] · ⟵ D2.1
- **D2.6** Semisommatore e sommatore completo · [1–2] · ⟵ D2.1, B2.3.1
- **D2.7** Sommatore a propagazione del riporto e con anticipo del riporto · [2–3] · ⟵ D2.6
- **D2.8** Sottrattore in complemento a 2 · [2] · ⟵ D2.7, B2.4.4
- **D2.9** ALU: operazioni aritmetiche e logiche; flag (zero, segno, riporto, overflow) · [2] · ⟵ D2.8, D2.3
- **D2.10** Moltiplicatori e circuiti di scorrimento · [3] · ⟵ D2.7, B2.3.3
- **D2.11** Ritardo di propagazione e cammino critico · [3] · ⟵ D2.7, C5.5
- **D2.12** Dalle porte ai transistor (collegamento con C5) · [2–3] · ⟵ D2.1, C5.1

## D3 Reti logiche sequenziali
- **D3.1** La memoria come retroazione: il latch SR · [2] · ⟵ D2.1
- **D3.2** Latch D; flip-flop D, JK, T · [2] · ⟵ D3.1
- **D3.3** Il segnale di clock; commutazione sul fronte · [2] · ⟵ D3.2
- **D3.4** Registri e registri a scorrimento · [2] · ⟵ D3.3
- **D3.5** Contatori sincroni e asincroni · [2] · ⟵ D3.3, B2.1.2
- **D3.6** Macchine a stati finiti di Moore e di Mealy · [2–3] · ⟵ D3.4, F1.1
- **D3.7** Progettare una macchina a stati (semaforo, distributore) · [2–3] · ⟵ D3.6, D1.6
- **D3.8** Banchi di registri; piccole RAM costruite con flip-flop · [2–3] · ⟵ D3.4, D2.4
- **D3.9** Metastabilità; sincronizzazione fra domini di clock diversi · [4] · ⟵ D3.3

## D4 Modelli di macchina
- **D4.1** Il programma memorizzato: dati e istruzioni nella stessa memoria · [1] · ⟵ B1.4
- **D4.2** L'architettura di von Neumann: CPU, memoria, I/O, bus · [1] · ⟵ D4.1
- **D4.3** Architettura Harvard e Harvard modificata · [2] · ⟵ D4.2
- **D4.4** Il collo di bottiglia di von Neumann · [2] · ⟵ D4.2
- **D4.5** Macchine didattiche (Little Man Computer, CPU simulate a 8 bit) · [1–2] · ⟵ D4.2

## D5 La CPU
- **D5.1** Registri: contatore di programma, registro istruzione, accumulatore, registri generali · [1–2] · ⟵ D4.2
- **D5.2** Il ciclo di fetch, decodifica ed esecuzione · [1] · ⟵ D5.1
- **D5.3** Unità di controllo cablata e microprogrammata · [3] · ⟵ D5.2, D3.6
- **D5.4** Il percorso dei dati (datapath) di una CPU semplice · [2–3] · ⟵ D5.2, D2.9, D3.8
- **D5.5** Clock, frequenza, cicli per istruzione (CPI) · [2] · ⟵ D5.2, D3.3
- **D5.6** Costruire una CPU completa partendo dalle porte logiche (approccio "nand2tetris") · [3] · ⟵ D5.4, D5.3

## D6 Set di istruzioni (ISA)
- **D6.1** Istruzione macchina: codice operativo e operandi · [2] · ⟵ D5.2, B2.2.2
- **D6.2** Tipi di istruzioni: trasferimento, aritmetiche, logiche, di salto · [2] · ⟵ D6.1
- **D6.3** Modi di indirizzamento: immediato, diretto, indiretto, a registro, indicizzato · [2–3] · ⟵ D6.2
- **D6.4** Formato e codifica delle istruzioni · [3] · ⟵ D6.1
- **D6.5** CISC e RISC a confronto · [2–3] · ⟵ D6.3
- **D6.6** Famiglie di processori: x86-64, ARM, RISC-V · [2–3] · ⟵ D6.5
- **D6.7** Chiamate di sottoprogramma: stack, record di attivazione, convenzioni di chiamata · [3] · ⟵ D6.3, E6.3.1
- **D6.8** Ordine dei byte e allineamento in memoria · [2–3] · ⟵ D6.1, B2.6.4

## D7 Assembly
- **D7.1** Dal linguaggio macchina all'assembly: i mnemonici · [2] · ⟵ D6.2
- **D7.2** Programmi semplici: somme, confronti, cicli · [2] · ⟵ D7.1, E3.4
- **D7.3** Accesso alla memoria e agli array · [2–3] · ⟵ D7.2, D6.3
- **D7.4** Sottoprogrammi e uso dello stack · [3] · ⟵ D7.3, D6.7
- **D7.5** Assemblatore, linker e formato dei file eseguibili · [3] · ⟵ D7.1
- **D7.6** Leggere l'assembly prodotto da un compilatore · [3] · ⟵ D7.4 · ⟶ G7

## D8 Gerarchia di memoria
- **D8.1** Indirizzi e celle di memoria; spazio di indirizzamento · [1–2] · ⟵ D4.2, A1.2.2
- **D8.2** La gerarchia: registri, cache, RAM, memoria di massa (costo, capacità, velocità) · [1–2] · ⟵ D8.1, C10.1
- **D8.3** Località spaziale e temporale · [2] · ⟵ D8.2
- **D8.4** Cache: blocchi; mappatura diretta, completamente associativa, associativa a insiemi · [3] · ⟵ D8.3, B2.3.5
- **D8.5** Politiche di sostituzione e di scrittura · [3] · ⟵ D8.4
- **D8.6** Prestazioni: tasso di successo, tempo medio di accesso · [3] · ⟵ D8.4, A7.3.2
- **D8.7** Memoria virtuale lato hardware: traduzione degli indirizzi, TLB · [3] · ⟵ D8.4 · ⟶ I4
- **D8.8** Coerenza delle cache nei multiprocessori · [3–4] · ⟵ D8.4, D11.1

## D9 Input/Output
- **D9.1** Controller e porte di I/O · [2] · ⟵ D4.2
- **D9.2** I/O a controllo di programma (polling) · [2] · ⟵ D9.1
- **D9.3** Interruzioni: richiesta, gestione, priorità · [2–3] · ⟵ D9.2
- **D9.4** Accesso diretto alla memoria (DMA) · [3] · ⟵ D9.3
- **D9.5** Bus di sistema (dati, indirizzi, controllo); arbitraggio; PCI Express · [2–3] · ⟵ D9.1, C11.5
- **D9.6** I/O mappato in memoria · [3] · ⟵ D9.1, D8.1

## D10 Prestazioni
- **D10.1** Misurare le prestazioni; legge di Amdahl nella versione di base · [2–3] · ⟵ D5.5
- **D10.2** Pipeline: stadi e throughput · [3] · ⟵ D5.4
- **D10.3** Conflitti (hazard) strutturali, sui dati, di controllo; forwarding · [3] · ⟵ D10.2
- **D10.4** Predizione dei salti · [3] · ⟵ D10.3
- **D10.5** Processori superscalari ed esecuzione fuori ordine · [3–4] · ⟵ D10.3
- **D10.6** Esecuzione speculativa · [4] · ⟵ D10.4, D10.5 · ⟶ N8
- **D10.7** Multithreading hardware (SMT) · [3–4] · ⟵ D10.5

## D11 Parallelismo hardware
- **D11.1** Multiprocessori e multicore a memoria condivisa · [3] · ⟵ D8.2, C9.3
- **D11.2** Tassonomia di Flynn (SISD, SIMD, MISD, MIMD) · [2–3] · ⟵ D4.2
- **D11.3** Istruzioni vettoriali SIMD (SSE, AVX, NEON) · [3] · ⟵ D11.2, D6.2
- **D11.4** GPU: migliaia di core semplici, modello SIMT · [3] · ⟵ D11.2, D11.1
- **D11.5** Architetture NUMA e interconnessioni · [4] · ⟵ D11.1

## D12 Architetture specializzate
- **D12.1** Processori per segnali digitali (DSP) · [3] · ⟵ D6.5, A6.5.5
- **D12.2** Acceleratori per l'IA: TPU, NPU, unità tensoriali · [3–4] · ⟵ D11.4, A5.1.6
- **D12.3** Architetture sistoliche e dataflow · [4] · ⟵ D12.2
- **D12.4** ASIC; confronto fra CPU, GPU, FPGA e ASIC · [3] · ⟵ D12.2, C12.2
- **D12.5** Architetture per il calcolo in memoria e neuromorfiche · [4] · ⟵ D12.3, C18.1

## D13 Microcontrollori e SoC
- **D13.1** Microprocessore, microcontrollore, SoC: differenze · [2] · ⟵ D4.2
- **D13.2** Periferiche integrate: timer, GPIO, ADC, UART · [2] · ⟵ D13.1, C7.1, C11.7
- **D13.3** Architetture per dispositivi mobili (core eterogenei) · [3] · ⟵ D13.1, D6.6
- **D13.4** Consumi e modalità di risparmio energetico · [2–3] · ⟵ D13.1, C13.1
