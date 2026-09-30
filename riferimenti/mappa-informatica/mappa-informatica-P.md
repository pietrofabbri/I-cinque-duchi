# Mappa dell'informatica — Area P: Linguistica computazionale ed elaborazione del linguaggio naturale (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** l'incontro fra linguistica e informatica: fondamenti linguistici, linguaggi formali e naturali, elaborazione del testo, corpora, modelli statistici e neurali, analisi linguistica, applicazioni, tecnologie della voce, informatica umanistica. I modelli neurali generali sono nell'area O.

---

## P1 Fondamenti di linguistica
- **P1.1** Che cos'è la linguistica; i livelli di analisi · [1–2] · ⟵ —
- **P1.2** Fonetica e fonologia · [2] · ⟵ P1.1
- **P1.3** Morfologia: morfemi, flessione, derivazione · [2] · ⟵ P1.1
- **P1.4** Sintassi: costituenti e dipendenze · [2] · ⟵ P1.1
- **P1.5** Semantica lessicale e composizionale · [2–3] · ⟵ P1.4
- **P1.6** Pragmatica e discorso · [2–3] · ⟵ P1.5
- **P1.7** Varietà linguistiche, lingue del mondo, tipologia · [2] · ⟵ P1.1
- **P1.8** Linguistica computazionale ed elaborazione del linguaggio naturale: definizione e storia · [2] · ⟵ P1.1

## P2 Linguaggi formali e linguaggi naturali
- **P2.1** L'ambiguità delle lingue naturali: lessicale, sintattica, semantica · [2] · ⟵ P1.4
- **P2.2** Grammatiche formali applicate alle lingue · [3] · ⟵ F2.3, P1.4
- **P2.3** Le lingue naturali sono libere dal contesto? Dibattito e prove · [4] · ⟵ P2.2, F2.8
- **P2.4** Grammatiche a dipendenze e grammatiche categoriali · [3–4] · ⟵ P2.2

## P3 Elaborazione del testo
- **P3.1** Il testo come sequenza di caratteri; problemi di codifica · [2] · ⟵ B4.5
- **P3.2** Normalizzazione: maiuscole, punteggiatura, segni diacritici · [2] · ⟵ P3.1
- **P3.3** Suddivisione in parole e in frasi (tokenizzazione) · [2] · ⟵ P3.2
- **P3.4** Espressioni regolari per elaborare testi · [2] · ⟵ P3.1, E7.4.6
- **P3.5** Stemming e lemmatizzazione · [2–3] · ⟵ P3.3, P1.3
- **P3.6** Parole vuote e rappresentazione "sacco di parole" · [2] · ⟵ P3.3
- **P3.7** Tokenizzazione in sottoparole (BPE) · [3] · ⟵ P3.3, B9.1.4
- **P3.8** Strumenti: NLTK, spaCy · [2–3] · ⟵ P3.5, G2.2.10

## P4 Linguistica dei corpora
- **P4.1** Il corpus: raccolta, bilanciamento, annotazione · [2] · ⟵ P1.1
- **P4.2** Frequenze delle parole e concordanze · [2] · ⟵ P4.1, P3.3, A7.1.2
- **P4.3** Legge di Zipf · [2–3] · ⟵ P4.2, A1.2.5
- **P4.4** Collocazioni e misure di associazione · [3] · ⟵ P4.2, A7.2.3
- **P4.5** Corpora annotati e treebank · [3] · ⟵ P4.1, P1.4
- **P4.6** Accordo fra annotatori · [3] · ⟵ P4.5, A7.2.2

## P5 Modelli linguistici statistici
- **P5.1** Modelli a n-grammi · [2–3] · ⟵ P4.2, A7.2.3
- **P5.2** Stima delle probabilità e smoothing · [3] · ⟵ P5.1
- **P5.3** La perplessità come misura · [3] · ⟵ P5.1, A8.1.2
- **P5.4** Generare testo con catene di Markov · [2–3] · ⟵ P5.1
- **P5.5** Correttori ortografici e predizione delle parole · [3] · ⟵ P5.1, E7.4.4

## P6 Analisi linguistica automatica
- **P6.1** Etichettatura delle parti del discorso (POS tagging) · [3] · ⟵ P4.5, P5.1
- **P6.2** Riconoscimento delle entità nominate · [3] · ⟵ P6.1
- **P6.3** Analisi sintattica a costituenti (CYK) · [3–4] · ⟵ P2.2, F2.7
- **P6.4** Analisi sintattica a dipendenze · [3–4] · ⟵ P2.4, P6.1
- **P6.5** Semantica distribuzionale: vettori di parole (word2vec) · [3] · ⟵ P4.4, A5.1.3
- **P6.6** Disambiguazione del senso delle parole · [3–4] · ⟵ P6.5, P2.1
- **P6.7** Risorse lessicali: WordNet, dizionari computazionali · [3] · ⟵ P1.5
- **P6.8** Analisi del discorso e risoluzione delle coreferenze · [4] · ⟵ P6.2, P1.6

## P7 Elaborazione neurale del linguaggio
- **P7.1** Classificare testi con reti neurali · [3] · ⟵ P3.6, O5.1.3
- **P7.2** Modelli sequenza-a-sequenza · [4] · ⟵ O5.3.1
- **P7.3** Transformer per il linguaggio: BERT e GPT · [4] · ⟵ O5.4.3, P3.7
- **P7.4** Grandi modelli linguistici e loro competenze linguistiche · [3–4] · ⟵ O6.2
- **P7.5** Modelli multilingue e lingue con poche risorse · [4] · ⟵ P7.4, P1.7
- **P7.6** Che cosa "sanno" i modelli linguistici: sonde e interpretabilità · [4] · ⟵ P7.4, O7.3

## P8 Applicazioni
- **P8.1** Traduzione automatica: a regole, statistica, neurale · [3] · ⟵ P5.1, O6.2
- **P8.2** Analisi del sentiment · [2–3] · ⟵ P3.6, O4.1.2
- **P8.3** Classificazione di documenti e filtri antispam · [2–3] · ⟵ P3.6, O4.1.2
- **P8.4** Estrazione di informazioni · [3] · ⟵ P6.2
- **P8.5** Riassunto automatico · [3–4] · ⟵ P7.4
- **P8.6** Sistemi di domanda-risposta e chatbot · [3] · ⟵ P7.4, O6.6
- **P8.7** Semplificazione del testo e indici di leggibilità (Gulpease) · [2] · ⟵ P4.2
- **P8.8** Uso critico di traduttori automatici e strumenti di scrittura · [1–2] · ⟵ P1.1

## P9 Tecnologie della voce
- **P9.1** Il segnale vocale: fonemi e spettrogramma · [3] · ⟵ P1.2, A6.5.1, B7.2
- **P9.2** Riconoscimento automatico del parlato · [4] · ⟵ P9.1, O5.4.4
- **P9.3** Sintesi vocale · [4] · ⟵ P9.1, O6.8
- **P9.4** Architettura degli assistenti vocali · [3] · ⟵ P9.1, P8.6
- **P9.5** Riconoscimento del parlante; voci clonate e rischi · [4] · ⟵ P9.2, P9.3

## P10 Informatica umanistica e stilometria
- **P10.1** L'informatica umanistica: panoramica · [2] · ⟵ P4.1
- **P10.2** Codifica dei testi: TEI-XML · [3] · ⟵ B11.3, P10.1
- **P10.3** Stilometria e attribuzione d'autore · [3] · ⟵ P4.2, O4.1.2
- **P10.4** Lettura distante e analisi di grandi collezioni · [3] · ⟵ P10.1, P4.2
- **P10.5** Edizioni digitali; riconoscimento ottico di testi storici · [3] · ⟵ P10.2, Q5.7
