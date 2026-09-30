# Mappa dell'informatica — Area S: Informatica applicata alle scienze (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** le intersezioni fra informatica e altre discipline: calcolo scientifico, bioinformatica e informatica genetica, neuroscienze, chimica, fisica, scienze della Terra, medicina, economia, scienze sociali, discipline umanistiche, vita artificiale, calcolo simbolico, scienze cognitive, sistemi complessi, ingegneria, diritto. Ogni ramo contiene anche i minimi prerequisiti disciplinari non informatici (per esempio la biologia molecolare in S2.1).

---

## S1 Calcolo scientifico e simulazione
- **S1.1** Modello e simulazione: perché simulare · [1–2] · ⟵ E1.4
- **S1.2** Simulazioni a tempo discreto e a eventi discreti · [2] · ⟵ S1.1, E3.4
- **S1.3** Metodi Monte Carlo · [2–3] · ⟵ S1.1, A7.2.2, E7.5.2
- **S1.4** Simulare sistemi dinamici con equazioni differenziali · [3] · ⟵ S1.1, A6.4.4
- **S1.5** Modelli ad agenti · [2–3] · ⟵ S1.2 · ⟶ O12.4
- **S1.6** Validazione dei modelli, incertezza, analisi di sensibilità · [3] · ⟵ S1.3, A7.4.1
- **S1.7** Software scientifico riproducibile · [3] · ⟵ S1.1, H5.2
- **S1.8** Apprendimento automatico per le scienze (modelli surrogati, reti informate dalla fisica) · [4] · ⟵ S1.4, O5.1.5
- **S1.9** L'ago di Buffon · [3] · ⟵ S1.3 · (v1.1, approfondimento)
- **S1.10** Il moto del proiettile con la resistenza dell'aria · [3] · ⟵ S1.4 · (v1.1, approfondimento)
- **S1.11** Visualizzare traiettorie e risultati di una simulazione · [3] · ⟵ S1.4 · (v1.1, approfondimento)
- **S1.12** Adattare curve non lineari ai dati (esponenziali, potenze) · [3] · ⟵ A7.1.5 · (v1.1, approfondimento)
- **S1.13** Pubblicare i risultati di una simulazione: notebook e dati aperti · [3] · ⟵ S1.7 · (v1.1, approfondimento)

## S2 Bioinformatica e informatica genetica

### S2.1 Basi di biologia molecolare
- **S2.1.1** Cellula, DNA, RNA, proteine · [1–2] · ⟵ —
- **S2.1.2** Il dogma centrale: trascrizione e traduzione · [2] · ⟵ S2.1.1
- **S2.1.3** Geni, genoma, mutazioni · [2] · ⟵ S2.1.2

### S2.2 Il DNA come codice
- **S2.2.1** Il DNA come stringa sull'alfabeto {A, C, G, T} · [1–2] · ⟵ S2.1.1, B1.4
- **S2.2.2** Il codice genetico: codoni e ridondanza · [2] · ⟵ S2.2.1, S2.1.2, A4.1.1
- **S2.2.3** Il contenuto informativo del genoma · [2–3] · ⟵ S2.2.1, A8.1.2
- **S2.2.4** Operazioni su sequenze: complemento inverso, traduzione, ricerca di motivi · [2] · ⟵ S2.2.2, E6.1.5

### S2.3 Sequenziamento e dati genomici
- **S2.3.1** Tecnologie di sequenziamento; le letture · [2–3] · ⟵ S2.1.3
- **S2.3.2** Formati FASTA e FASTQ; banche dati biologiche (GenBank, UniProt) · [2–3] · ⟵ S2.3.1, B11.1
- **S2.3.3** Assemblaggio dei genomi con grafi di de Bruijn · [4] · ⟵ S2.3.1, A4.3.7

### S2.4 Allineamento di sequenze
- **S2.4.1** Allineamento globale (Needleman-Wunsch) · [3] · ⟵ S2.2.4, E7.4.4
- **S2.4.2** Allineamento locale (Smith-Waterman) · [3] · ⟵ S2.4.1
- **S2.4.3** Matrici di sostituzione e punteggi · [3] · ⟵ S2.4.1, A7.2.3
- **S2.4.4** Ricerca euristica nelle banche dati: BLAST · [3] · ⟵ S2.4.2, E6.5.4
- **S2.4.5** Allineamento multiplo · [4] · ⟵ S2.4.2
- **S2.4.6** Modelli di Markov nascosti per sequenze biologiche · [4] · ⟵ S2.4.3, A7.5.6

### S2.5 Filogenetica
- **S2.5.1** Alberi filogenetici · [3] · ⟵ S2.4.1, A4.3.3
- **S2.5.2** Metodi basati sulle distanze (UPGMA, neighbor joining) · [3–4] · ⟵ S2.5.1, O4.2.2
- **S2.5.3** Metodi a massima verosimiglianza e bayesiani · [4] · ⟵ S2.5.1, A7.4.3

### S2.6 Genomica e proteomica
- **S2.6.1** Espressione genica e analisi dei dati omici · [4] · ⟵ S2.3.2, L9.4
- **S2.6.2** Struttura delle proteine e sua predizione (AlphaFold) · [4] · ⟵ S2.1.1, O5.4.3
- **S2.6.3** Genomica personale e medicina di precisione · [3–4] · ⟵ S2.1.3

### S2.7 Biologia dei sistemi
- **S2.7.1** Reti di regolazione genica e reti metaboliche · [4] · ⟵ S2.6.1, A4.3.1
- **S2.7.2** Modelli dinamici dei sistemi biologici · [4] · ⟵ S2.7.1, A6.4.3

### S2.8 Etica dei dati genetici
- **S2.8.1** Privacy dei dati genetici; test genetici venduti al pubblico · [2–3] · ⟵ S2.1.3, U4.1
- **S2.8.2** Editing genetico (CRISPR) e questioni etiche · [3] · ⟵ S2.1.3, U3.1

## S3 Neuroscienze computazionali
- **S3.1** Il neurone biologico e il potenziale d'azione · [2–3] · ⟵ —
- **S3.2** Modelli di neurone (integrate-and-fire, Hodgkin-Huxley) · [4] · ⟵ S3.1, A6.4.2
- **S3.3** Reti neurali biologiche e plasticità sinaptica · [4] · ⟵ S3.2
- **S3.4** La codifica neurale dell'informazione · [4] · ⟵ S3.3, A8.1.3
- **S3.5** Interfacce cervello-computer · [3–4] · ⟵ S3.1, O4.1.2
- **S3.6** Reti neurali artificiali e cervello: analogie e differenze · [3] · ⟵ S3.1, O5.1.1

## S4 Chimica computazionale e scienza dei materiali
- **S4.1** Rappresentare le molecole (grafi, notazione SMILES) · [3] · ⟵ A4.3.1
- **S4.2** Dinamica molecolare · [4] · ⟵ S4.1, A6.4.4
- **S4.3** Chimica quantistica computazionale · [4] · ⟵ S4.1, C15.5
- **S4.4** Scoperta di farmaci e materiali con l'IA · [4] · ⟵ S4.1, O5.5

## S5 Fisica computazionale e astroinformatica
- **S5.1** Simulare sistemi fisici: moto, gravitazione, problema degli N corpi · [2–3] · ⟵ S1.2
- **S5.2** Analisi dei dati sperimentali in fisica · [3] · ⟵ A7.4.1, L9.4
- **S5.3** Astroinformatica: le grandi campagne di osservazione del cielo · [3–4] · ⟵ S5.2, L8.5
- **S5.4** Il calcolo per la fisica delle particelle (CERN, griglia di calcolo) · [4] · ⟵ S5.2, M5.1
- **S5.5** Il pendolo: piccole e grandi oscillazioni · [3] · ⟵ S5.1 · (v1.1, approfondimento)
- **S5.6** La risonanza: dall'altalena ai ponti · [3] · ⟵ A6.4.2 · (v1.1, approfondimento)

## S6 Ambiente, clima e sistemi informativi geografici
- **S6.1** Dati geografici: coordinate e proiezioni cartografiche · [2] · ⟵ A5.1.1
- **S6.2** Modelli vettoriale e raster nei GIS · [2] · ⟵ S6.1, B6.5
- **S6.3** Strumenti GIS (QGIS) e mappe web (OpenStreetMap) · [2] · ⟵ S6.2
- **S6.4** Analisi spaziale · [3] · ⟵ S6.3, E12.5
- **S6.5** Telerilevamento e immagini satellitari · [3] · ⟵ S6.2, Q4.1
- **S6.6** Modelli climatici · [4] · ⟵ S1.4, M5.1
- **S6.7** Monitoraggio ambientale con reti di sensori · [2–3] · ⟵ R10.1

## S7 Informatica medica
- **S7.1** Fascicolo sanitario elettronico e standard (HL7 FHIR) · [2–3] · ⟵ B11.4
- **S7.2** Immagini mediche: formato DICOM ed elaborazione · [3] · ⟵ Q4.1
- **S7.3** Diagnosi assistita dall'IA · [3–4] · ⟵ S7.2, O5.2.3
- **S7.4** Telemedicina e dispositivi indossabili per la salute · [2] · ⟵ S7.1
- **S7.5** Privacy e sicurezza dei dati sanitari · [2–3] · ⟵ S7.1, U4.1
- **S7.6** Epidemiologia computazionale · [3–4] · ⟵ S14.4

## S8 Economia e finanza
- **S8.1** Fogli di calcolo per l'economia e la finanza · [1–2] · ⟵ L2.3
- **S8.2** Modelli finanziari e simulazione del rischio · [3] · ⟵ S1.3
- **S8.3** Trading algoritmico · [4] · ⟵ S8.2, O4.1.2
- **S8.4** Fintech e servizi bancari digitali · [2] · ⟵ V5.3
- **S8.5** Economia computazionale e simulazione dei mercati · [4] · ⟵ S1.5, A9.4.2

## S9 Scienze sociali computazionali
- **S9.1** Analisi delle reti sociali: centralità e comunità · [3] · ⟵ A4.3.2, E7.3.1
- **S9.2** Analisi di social media e testi su larga scala · [3] · ⟵ S9.1, P8.2
- **S9.3** Diffusione delle informazioni e della disinformazione · [3–4] · ⟵ S9.1, S14.3
- **S9.4** Esperimenti online e questioni etiche · [3] · ⟵ A7.4.5, U3.8

## S10 Informatica per le discipline umanistiche
- **S10.1** Patrimonio culturale digitale: digitalizzazione, musei, archivi · [1–2] · ⟵ B6.2
- **S10.2** Analisi computazionale di testi letterari e storici · [3] · ⟵ P10.4
- **S10.3** Ricostruzioni 3D e archeologia digitale · [3] · ⟵ Q11.3
- **S10.4** Musica, arte e storia dell'arte computazionali · [3] · ⟵ Q6.6, Q5.4

## S11 Vita artificiale e automi cellulari
- **S11.1** Automi cellulari elementari · [2] · ⟵ E6.1.4, F1.1
- **S11.2** Il Gioco della vita di Conway · [1–2] · ⟵ E6.1.4
- **S11.3** Emergenza e auto-organizzazione · [2–3] · ⟵ S11.2
- **S11.4** Evoluzione artificiale e creature virtuali · [3–4] · ⟵ S11.3, O8.1

## S12 Calcolo simbolico e software matematico
- **S12.1** Sistemi di algebra computazionale (SymPy, Maxima) · [2–3] · ⟵ A1.5.4, G1.15
- **S12.2** Algoritmi simbolici: semplificazione, derivazione, integrazione · [3–4] · ⟵ S12.1, E6.4.8
- **S12.3** Geometria dinamica (GeoGebra) · [1] · ⟵ —
- **S12.4** Librerie numeriche (BLAS, LAPACK, SciPy) · [3] · ⟵ A10.3.1
- **S12.5** Dimostrazioni matematiche assistite dal calcolatore · [4] · ⟵ F9.3

## S13 Scienze cognitive e psicologia computazionale
- **S13.1** Le scienze cognitive: la mente come elaborazione di informazione · [2–3] · ⟵ Q8.2
- **S13.2** Architetture cognitive (ACT-R, SOAR) · [4] · ⟵ S13.1, O2.3.1
- **S13.3** Modelli computazionali di percezione, memoria, apprendimento · [4] · ⟵ S13.1, O5.1.3
- **S13.4** Psicometria computazionale e test adattivi · [3–4] · ⟵ A7.4.3
- **S13.5** Modelli bayesiani della cognizione · [4] · ⟵ S13.1, A7.4.4
- **S13.6** Mente e tecnologia: effetti su memoria, attenzione, apprendimento · [2–3] · ⟵ S13.1 · ⟶ U7.6

## S14 Sistemi complessi e scienza delle reti
- **S14.1** Sistemi complessi: emergenza e non linearità · [2–3] · ⟵ —
- **S14.2** Caos deterministico (mappa logistica) · [3] · ⟵ S14.1, A4.2.1
- **S14.3** Reti complesse: piccolo mondo, invarianza di scala, dinamiche sulle reti · [3–4] · ⟵ S14.1, A4.3.2
- **S14.4** Modelli epidemici (SIR) · [3] · ⟵ S14.1, A6.4.1, S1.4
- **S14.5** Frattali e dimensione frattale · [2–3] · ⟵ S14.1, A1.2.5

## S15 Ingegneria e manifattura computazionale
- **S15.1** Metodo degli elementi finiti · [4] · ⟵ A6.4.5, A10.3.2
- **S15.2** Fluidodinamica computazionale · [4] · ⟵ S15.1
- **S15.3** CAD/CAM e macchine a controllo numerico · [3] · ⟵ Q11.3
- **S15.4** Gemelli digitali industriali · [4] · ⟵ S15.1, R11.2
- **S15.5** Ottimizzazione del progetto · [4] · ⟵ S15.1, A9.2.2

## S16 Informatica giuridica
- **S16.1** Informatica giuridica e diritto dell'informatica: la distinzione · [2–3] · ⟵ U4.1
- **S16.2** Banche dati giuridiche e norme in formato digitale (Normattiva, Akoma Ntoso) · [3] · ⟵ S16.1, B11.3
- **S16.3** Processo telematico e firma digitale degli atti · [3] · ⟵ S16.1, N3.4.4
- **S16.4** Analisi automatica dei testi giuridici · [4] · ⟵ S16.2, P8.4
- **S16.5** Contratti intelligenti e diritto · [4] · ⟵ M7.5, S16.1
- **S16.6** Decisioni automatizzate e giustizia predittiva · [3–4] · ⟵ S16.1, O10.3
