# Mappa dell'informatica — Area M: Calcolo parallelo, distribuito e ad alte prestazioni (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** perché e come si calcola in parallelo; sistemi distribuiti e loro teoria; cloud, supercalcolo, edge computing, blockchain, calcolo sostenibile. È la conseguenza diretta della fine dello scaling di Dennard (C9.2).

---

## M1 Motivazioni e limiti
- **M1.1** Perché il calcolo parallelo: la frequenza dei processori ha smesso di crescere · [2–3] · ⟵ C9.1
- **M1.2** Accelerazione ed efficienza · [3] · ⟵ M1.1
- **M1.3** Legge di Amdahl · [3] · ⟵ M1.2, D10.1
- **M1.4** Legge di Gustafson; scalabilità forte e debole · [3] · ⟵ M1.3
- **M1.5** Parallelismo di dati e di compiti · [2–3] · ⟵ M1.1
- **M1.6** Granularità, bilanciamento del carico, costi di comunicazione · [3] · ⟵ M1.5

## M2 Programmazione parallela
- **M2.1** Thread e memoria condivisa in pratica · [3] · ⟵ G3.7.3, D11.1
- **M2.2** OpenMP · [3] · ⟵ M2.1
- **M2.3** Scambio di messaggi con MPI · [3–4] · ⟵ M1.6, G1.8
- **M2.4** Programmazione delle GPU: CUDA e OpenCL · [3–4] · ⟵ D11.4, M1.5
- **M2.5** Parallelismo in Python: multiprocessing, NumPy, Numba · [3] · ⟵ G3.8.1, M1.5
- **M2.6** Schemi paralleli: map, reduce, pipeline, stencil · [3] · ⟵ M1.5, E11.2
- **M2.7** Debugging e profilazione di programmi paralleli · [3–4] · ⟵ M2.1, I12.2

## M3 Sistemi distribuiti
- **M3.1** Sistemi distribuiti: definizione, obiettivi, trasparenze · [3] · ⟵ J2.5
- **M3.2** Modelli di guasto e ipotesi di sincronia · [3–4] · ⟵ M3.1
- **M3.3** Il tempo: orologi fisici, orologi logici di Lamport, orologi vettoriali · [3–4] · ⟵ M3.1, J7.9
- **M3.4** Replicazione e modelli di consistenza · [3–4] · ⟵ M3.1, L14.1
- **M3.5** Teoremi CAP e PACELC · [3–4] · ⟵ M3.4
- **M3.6** Consenso: Paxos e Raft · [4] · ⟵ M3.2, M3.3
- **M3.7** Tolleranza ai guasti bizantini · [4] · ⟵ M3.6
- **M3.8** Mutua esclusione ed elezione distribuite · [4] · ⟵ M3.3, E11.4
- **M3.9** Tabelle hash distribuite e reti sovrapposte · [4] · ⟵ M3.1, E6.5.1, J10.6
- **M3.10** Code di messaggi e sistemi publish-subscribe · [3] · ⟵ M3.1, G3.6.4

## M4 Cloud computing
- **M4.1** Il cloud: caratteristiche e modelli di servizio (IaaS, PaaS, SaaS) · [2] · ⟵ J2.5, I9.1
- **M4.2** Modelli di distribuzione: pubblico, privato, ibrido · [2] · ⟵ M4.1
- **M4.3** Servizi di base: calcolo, archiviazione a oggetti, rete · [3] · ⟵ M4.1
- **M4.4** Scalabilità elastica e bilanciamento del carico · [3] · ⟵ M4.3, M1.6
- **M4.5** Serverless e funzioni come servizio · [3] · ⟵ M4.3
- **M4.6** Costi del cloud (FinOps) · [3] · ⟵ M4.3
- **M4.7** Sovranità dei dati; il cloud per la pubblica amministrazione · [2–3] · ⟵ M4.2, U4.1
- **M4.8** Il cloud nella vita scolastica: suite collaborative, archiviazione condivisa · [1] · ⟵ —

## M5 Supercalcolo (HPC)
- **M5.1** Supercalcolatori: cluster e interconnessioni · [3] · ⟵ M2.3
- **M5.2** La classifica TOP500; FLOPS e benchmark LINPACK · [2–3] · ⟵ M1.1
- **M5.3** Code di lavoro e schedulatori (Slurm) · [3–4] · ⟵ M5.1, I2.6
- **M5.4** Il supercalcolo in Italia e in Europa (Leonardo, EuroHPC) · [2] · ⟵ M5.2
- **M5.5** Calcolo exascale e sfide energetiche · [4] · ⟵ M5.1, C13.4

## M6 Edge e fog computing
- **M6.1** Dal cloud al bordo della rete: edge e fog computing · [3] · ⟵ M4.1
- **M6.2** Elaborare vicino ai sensori: latenza e privacy · [3] · ⟵ M6.1
- **M6.3** IA sui dispositivi (edge AI, TinyML) · [3–4] · ⟵ M6.2, O5.1.7
- **M6.4** Il continuo di calcolo dal dispositivo al cloud · [4] · ⟵ M6.2, M4.4

## M7 Blockchain e registri distribuiti
- **M7.1** Registri distribuiti: idea e casi d'uso · [2] · ⟵ J2.5
- **M7.2** La catena di blocchi collegati da hash · [2–3] · ⟵ M7.1, N3.2.1
- **M7.3** Transazioni firmate e portafogli · [3] · ⟵ M7.2, N3.4.1
- **M7.4** Meccanismi di consenso: proof of work e proof of stake · [3] · ⟵ M7.2, M3.1
- **M7.5** Contratti intelligenti · [3–4] · ⟵ M7.4, G1.8
- **M7.6** Limiti: scalabilità, consumo energetico, usi impropri · [2–3] · ⟵ M7.2

## M8 Calcolo sostenibile (green computing)
- **M8.1** Consumo energetico del calcolo: misure e stime · [2–3] · ⟵ C13.1
- **M8.2** Algoritmi e software efficienti dal punto di vista energetico · [3] · ⟵ M8.1, E9.3
- **M8.3** Data center efficienti: raffreddamento, energie rinnovabili, PUE · [3] · ⟵ C13.4
- **M8.4** Impronta di carbonio dell'addestramento dei modelli di IA · [3] · ⟵ M8.1, O9.3, O9.5
- **M8.5** Pianificare il calcolo in base all'energia disponibile · [4] · ⟵ M8.3, M4.4
