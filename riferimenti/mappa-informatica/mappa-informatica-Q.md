# Mappa dell'informatica — Area Q: Grafica, multimedia, visione e interazione (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** grafica 2D e 3D, animazione e videogiochi, elaborazione delle immagini, visione artificiale, audio e musica digitale, realtà virtuale e aumentata, interazione uomo-macchina, visualizzazione dei dati, modellazione geometrica, calcolo ubiquo, collaborazione, creatività computazionale, metodi di valutazione in HCI.

---

## Q1 Grafica 2D
- **Q1.1** Coordinate dello schermo e pixel · [1] · ⟵ B6.1
- **Q1.2** Disegnare primitive: punti, linee, forme (turtle, Processing) · [1] · ⟵ Q1.1
- **Q1.3** Rasterizzazione di linee e poligoni (Bresenham, riempimento) · [3] · ⟵ Q1.2, E7.5.5
- **Q1.4** Trasformazioni 2D: traslazione, rotazione, scala · [2–3] · ⟵ Q1.2, A5.2.2
- **Q1.5** Curve di Bézier · [3] · ⟵ Q1.2, A1.5.4
- **Q1.6** Antialiasing e composizione · [3] · ⟵ Q1.3, B5.2.5
- **Q1.7** Grafica della tartaruga e frattali · [2] · ⟵ Q1.2, E5.1
- **Q1.8** Poligoni e stelle con la tartaruga: angoli esterni · [1–2] · ⟵ Q1.2 · (v1.1, approfondimento)

## Q2 Grafica 3D
- **Q2.1** Coordinate 3D, modelli poligonali, mesh · [2–3] · ⟵ A5.1.1, Q1.1
- **Q2.2** Trasformazioni 3D e coordinate omogenee · [3] · ⟵ Q2.1, A5.2.3
- **Q2.3** Telecamera e proiezione prospettica · [3] · ⟵ Q2.2
- **Q2.4** Rimozione delle superfici nascoste (z-buffer) · [3] · ⟵ Q2.3
- **Q2.5** Illuminazione e modelli di ombreggiatura (Phong) · [3] · ⟵ Q2.3, A5.1.3
- **Q2.6** Texture · [3] · ⟵ Q2.5, B6.1
- **Q2.7** Pipeline grafica e shader su GPU · [3–4] · ⟵ Q2.4, D11.4
- **Q2.8** Ray tracing e path tracing · [4] · ⟵ Q2.5, A7.3.4, A6.3.3
- **Q2.9** Strumenti: Blender, OpenGL, Vulkan · [2–3] · ⟵ Q2.1

## Q3 Animazione, simulazione, videogiochi
- **Q3.1** Animazione: fotogrammi chiave e interpolazione · [1–2] · ⟵ B8.1
- **Q3.2** Il ciclo di gioco (game loop) · [2] · ⟵ G3.6.1
- **Q3.3** Collisioni e fisica semplice · [2–3] · ⟵ Q3.2, E7.5.5
- **Q3.4** Simulazione fisica numerica · [3] · ⟵ Q3.3, A6.4.4
- **Q3.5** Motori di gioco (Godot, Unity) · [2–3] · ⟵ Q3.2, G3.2.1
- **Q3.6** IA nei videogiochi: ricerca di percorsi, macchine a stati · [3] · ⟵ Q3.2, E7.3.9, F1.1
- **Q3.7** Progettazione di videogiochi (game design) · [1–2] · ⟵ —
- **Q3.8** Generazione procedurale di contenuti · [3] · ⟵ Q3.2, E7.5.2

## Q4 Elaborazione delle immagini
- **Q4.1** L'immagine come matrice; l'istogramma · [2] · ⟵ B6.1, A7.1.2
- **Q4.2** Operazioni puntuali: luminosità, contrasto, soglia · [2] · ⟵ Q4.1
- **Q4.3** Filtri e convoluzione: sfocatura, nitidezza · [3] · ⟵ Q4.2, A6.5.5
- **Q4.4** Rilevamento dei contorni · [3] · ⟵ Q4.3, A6.2.4
- **Q4.5** Morfologia matematica · [3] · ⟵ Q4.2
- **Q4.6** Segmentazione · [3] · ⟵ Q4.4
- **Q4.7** Elaborazione nel dominio della frequenza · [3–4] · ⟵ Q4.3, A6.5.4
- **Q4.8** Strumenti: OpenCV, Pillow · [2–3] · ⟵ Q4.2, G2.2.10

## Q5 Visione artificiale
- **Q5.1** Dall'immagine alla comprensione: i compiti della visione · [2] · ⟵ Q4.1
- **Q5.2** Caratteristiche locali e corrispondenze · [3–4] · ⟵ Q4.4
- **Q5.3** Geometria della visione: calibrazione, visione stereo · [4] · ⟵ Q2.3, Q5.2
- **Q5.4** Classificare immagini con reti convoluzionali · [3] · ⟵ O5.2.2
- **Q5.5** Rilevamento e segmentazione di oggetti · [3–4] · ⟵ Q5.4
- **Q5.6** Riconoscimento facciale e questioni etiche · [3] · ⟵ Q5.4, U4.8
- **Q5.7** Riconoscimento ottico dei caratteri (OCR) · [3] · ⟵ Q5.4
- **Q5.8** Video: tracciamento e riconoscimento di azioni · [4] · ⟵ Q5.5, B8.1

## Q6 Audio e musica digitale
- **Q6.1** Registrare e modificare l'audio (Audacity) · [1] · ⟵ B7.2
- **Q6.2** Sintesi del suono: oscillatori, inviluppi, sintesi sottrattiva · [2] · ⟵ B7.1, A6.1.2
- **Q6.3** Effetti: filtri, riverbero, compressione dinamica · [2–3] · ⟵ Q6.2, A6.5.1
- **Q6.4** Workstation audio digitali e MIDI · [1–2] · ⟵ B7.7, Q6.1
- **Q6.5** Programmazione musicale (Sonic Pi, SuperCollider, Max/MSP) · [2–3] · ⟵ Q6.2, G1.7
- **Q6.6** Analisi dell'audio: spettro, altezza, ritmo · [3] · ⟵ A6.5.4, B7.4
- **Q6.7** Informatica musicale e musica generata dall'IA · [4] · ⟵ Q6.6, O6.8
- **Q6.8** Audio spaziale · [3–4] · ⟵ Q6.3

## Q7 Realtà virtuale e aumentata
- **Q7.1** Realtà virtuale, aumentata, mista: definizioni · [1–2] · ⟵ —
- **Q7.2** Visori, tracciamento, latenza, cinetosi · [3] · ⟵ Q7.1, Q2.3
- **Q7.3** Realtà aumentata: ancoraggio e riconoscimento dell'ambiente · [3–4] · ⟵ Q7.1, Q5.2
- **Q7.4** Progettare esperienze immersive · [3] · ⟵ Q7.2, Q8.3
- **Q7.5** Usi didattici, culturali, medici · [2] · ⟵ Q7.1

## Q8 Interazione uomo-macchina (HCI)
- **Q8.1** L'interazione uomo-macchina: definizione e storia delle interfacce · [2] · ⟵ I7.2
- **Q8.2** Basi di psicologia cognitiva: percezione, attenzione, memoria, modelli mentali · [2] · ⟵ —
- **Q8.3** Principi di usabilità ed euristiche di Nielsen · [2] · ⟵ Q8.1, Q8.2
- **Q8.4** Progettazione centrata sull'utente: personas e scenari · [2–3] · ⟵ Q8.3
- **Q8.5** Prototipazione: dagli schizzi ai prototipi interattivi (Figma) · [2] · ⟵ Q8.4
- **Q8.6** Principi di design visivo: gerarchia, allineamento, colore · [1–2] · ⟵ B5.2.1
- **Q8.7** Accessibilità e progettazione inclusiva · [2] · ⟵ Q8.3, U8.3
- **Q8.8** Interfacce conversazionali e vocali · [3] · ⟵ Q8.3
- **Q8.9** Leggi dell'interazione: Fitts e Hick · [3] · ⟵ Q8.2, A1.2.5
- **Q8.10** Design persuasivo e dark pattern · [2] · ⟵ Q8.3 · ⟶ U7.6

## Q9 Visualizzazione dei dati
- **Q9.1** Scegliere il grafico adatto ai dati · [1–2] · ⟵ A7.1.2
- **Q9.2** Codifiche visive: posizione, lunghezza, colore, forma · [2] · ⟵ Q9.1, Q8.2
- **Q9.3** Grafici ingannevoli e come riconoscerli · [1–2] · ⟵ Q9.1
- **Q9.4** Visualizzare dati multidimensionali, reti, mappe · [3] · ⟵ Q9.2, A4.3.1
- **Q9.5** Dashboard e visualizzazioni interattive · [3] · ⟵ Q9.2, G2.2.13

## Q10 Grafica per il web (aspetti grafici)
- **Q10.1** Grafica vettoriale e raster nel browser · [2] · ⟵ K12.2, K12.3
- **Q10.2** Rendering 3D nel browser · [3–4] · ⟵ K12.4
- **Q10.3** Animazioni e interazioni grafiche nelle pagine · [2–3] · ⟵ K3.9, K4.3

## Q11 Modellazione geometrica
- **Q11.1** Curve e superfici parametriche: spline e NURBS · [3–4] · ⟵ Q1.5, A10.2.2
- **Q11.2** Mesh e superfici di suddivisione · [4] · ⟵ Q11.1, Q2.1
- **Q11.3** CAD: modellazione solida e parametrica · [2–3] · ⟵ Q2.1
- **Q11.4** Stampa 3D: dal modello agli strati (slicing, G-code) · [1–2] · ⟵ C11.4
- **Q11.5** Scansione 3D e nuvole di punti · [4] · ⟵ Q11.2, Q5.3

## Q12 Calcolo ubiquo, indossabile e interfacce tangibili
- **Q12.1** Calcolo ubiquo e pervasivo: la visione di Weiser · [2] · ⟵ Q8.1
- **Q12.2** Dispositivi indossabili · [2–3] · ⟵ Q12.1, R1
- **Q12.3** Interfacce tangibili · [3] · ⟵ Q12.1, R2
- **Q12.4** Ambienti intelligenti e sensibili al contesto · [3] · ⟵ Q12.1, R10

## Q13 Lavoro cooperativo e social computing
- **Q13.1** Strumenti di collaborazione: documenti condivisi, videoconferenza · [1] · ⟵ M4.8
- **Q13.2** Comunità online e piattaforme sociali · [2] · ⟵ Q13.1
- **Q13.3** Crowdsourcing e scienza partecipata (Wikipedia, Zooniverse) · [2] · ⟵ Q13.2
- **Q13.4** Tecniche di modifica collaborativa in tempo reale (CRDT) · [4] · ⟵ Q13.1, M3.4
- **Q13.5** Moderazione dei contenuti · [2–3] · ⟵ Q13.2, U7.7

## Q14 Creatività computazionale e arte generativa
- **Q14.1** Creative coding: Processing, p5.js · [1–2] · ⟵ Q1.2, G1.7
- **Q14.2** Arte generativa: casualità, regole, rumore di Perlin · [2–3] · ⟵ Q14.1, E7.5.2
- **Q14.3** Arte e musica con l'IA · [3] · ⟵ Q14.2, O6.4
- **Q14.4** Una macchina può essere creativa? · [3] · ⟵ Q14.3, U2.4
- **Q14.5** Installazioni interattive e arte digitale · [2–3] · ⟵ Q14.1, R2

## Q15 Metodi di valutazione in HCI
- **Q15.1** Test di usabilità con gli utenti · [2] · ⟵ Q8.3
- **Q15.2** Questionari standardizzati (SUS) · [2] · ⟵ Q15.1
- **Q15.3** Esperimenti controllati · [3] · ⟵ Q15.1, A7.4.2
- **Q15.4** Metodi qualitativi: interviste, osservazione, analisi tematica · [3] · ⟵ Q15.1
- **Q15.5** Analisi dell'uso: registrazioni, tracciamento dello sguardo · [3–4] · ⟵ Q15.3
