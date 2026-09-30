# Mappa dell'informatica — Area B: Informazione e rappresentazione (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** come si rappresentano con i bit numeri, testo, colori, immagini, suoni, video e dati strutturati; compressione e correzione degli errori. È l'area d'ingresso tipica del primo biennio.

---

## B1 Concetti base
- **B1.1** Dato, informazione, conoscenza: differenze · [1] · ⟵ —
- **B1.2** Segnale; grandezze analogiche e digitali · [1] · ⟵ B1.1
- **B1.3** Discretizzazione: campionare nel tempo e quantizzare i valori (idea intuitiva) · [1] · ⟵ B1.2, A1.1.3
- **B1.4** Codifica: associare simboli a configurazioni; un codice come corrispondenza · [1] · ⟵ B1.1, A3.1.1
- **B1.5** Il bit come unità minima; quante informazioni distinguono n bit · [1] · ⟵ B1.4, A4.1.1 · ⟶ A8.1.1
- **B1.6** Perché il binario: due stati fisici stabili e distinguibili · [1] · ⟵ B1.5 · ⟶ C4
- **B1.7** Vantaggi e limiti del digitale: copie identiche, robustezza al rumore, obsolescenza dei supporti · [1] · ⟵ B1.3 · (v1.1, approfondimento)
- **B1.8** Strumenti analogici e digitali a confronto (orologi, termometri, dischi in vinile e streaming) · [1] · ⟵ B1.2 · (v1.1, approfondimento)
- **B1.9** Il gioco delle venti domande: dimezzare le possibilità · [1] · ⟵ B1.5 · (v1.1, approfondimento)
- **B1.10** Segnalazioni a due simboli nella storia (fuochi, bandiere, telegrafo) · [1] · ⟵ B1.4 · (v1.1, approfondimento)

## B2 Rappresentazione dei numeri

### B2.1 Sistemi posizionali e conversioni
- **B2.1.1** Sistemi additivi (numeri romani) e posizionali; la base · [1] · ⟵ A1.1.1, A1.2.1
- **B2.1.2** Numerazione binaria: contare in binario · [1] · ⟵ B2.1.1, A1.2.2
- **B2.1.3** Conversione binario → decimale (somma di potenze) · [1] · ⟵ B2.1.2
- **B2.1.4** Conversione decimale → binario (divisioni successive) · [1] · ⟵ B2.1.2, A1.3.1
- **B2.1.5** Conversione fra basi qualsiasi · [1] · ⟵ B2.1.3, B2.1.4
- **B2.1.6** Numeri frazionari in binario (moltiplicazioni successive); frazioni non rappresentabili esattamente · [1–2] · ⟵ B2.1.5, A1.1.3
- **B2.1.7** Sistemi di numerazione di altre culture: babilonese (base 60), maya (base 20) · [1] · ⟵ B2.1.1 · (v1.1, approfondimento)
- **B2.1.8** Tracce di altre basi nella vita quotidiana: ore, minuti, dozzine · [1] · ⟵ B2.1.1 · (v1.1, approfondimento)

### B2.2 Ottale ed esadecimale
- **B2.2.1** Basi 8 e 16 · [1] · ⟵ B2.1.5
- **B2.2.2** Conversione rapida binario ↔ esadecimale per gruppi di 4 bit · [1] · ⟵ B2.2.1
- **B2.2.3** Usi dell'esadecimale: colori, indirizzi di memoria, indirizzi MAC, dump · [1] · ⟵ B2.2.2 · ⟶ D8, J4
- **B2.2.4** La codifica Base64: dati binari scritti come testo · [1–2] · ⟵ B2.2.2 · (v1.1, approfondimento)

### B2.3 Aritmetica binaria
- **B2.3.1** Addizione binaria e riporto · [1] · ⟵ B2.1.2
- **B2.3.2** Sottrazione binaria e prestito · [1] · ⟵ B2.3.1
- **B2.3.3** Moltiplicazione e divisione binaria; lo scorrimento (shift) come ×2 e ÷2 · [1–2] · ⟵ B2.3.1
- **B2.3.4** Parole di lunghezza fissa; overflow · [1] · ⟵ B2.3.1, B3.1
- **B2.3.5** Operazioni bit a bit (AND, OR, XOR, NOT) e maschere · [2] · ⟵ B2.1.2, A2.1.3 · ⟶ J5, G1

### B2.4 Interi con segno
- **B2.4.1** Modulo e segno · [1] · ⟵ B2.3.4
- **B2.4.2** Complemento a 1 · [1–2] · ⟵ B2.4.1
- **B2.4.3** Complemento a 2: rappresentazione e intervallo rappresentabile · [1–2] · ⟵ B2.4.2, A1.4.1
- **B2.4.4** Sottrazione come somma in complemento a 2; overflow con segno · [2] · ⟵ B2.4.3, B2.3.2 · ⟶ D2
- **B2.4.5** Rappresentazione in eccesso (con bias) · [2] · ⟵ B2.4.3
- **B2.4.6** Tipi interi con e senza segno nei linguaggi (int, unsigned, long) · [2] · ⟵ B2.4.3 · ⟶ G1
- **B2.4.7** Errori famosi dovuti all'overflow (Ariane 5, problema dell'anno 2038) · [2] · ⟵ B2.4.4 · (v1.1, approfondimento)

### B2.5 Numeri reali: virgola fissa e mobile
- **B2.5.1** Virgola fissa · [2] · ⟵ B2.1.6
- **B2.5.2** Notazione scientifica in base 2: segno, mantissa, esponente · [2] · ⟵ B2.5.1, A1.1.5, B2.4.5
- **B2.5.3** Standard IEEE 754 a precisione singola e doppia · [2] · ⟵ B2.5.2
- **B2.5.4** Valori speciali: zero con segno, infiniti, NaN, numeri denormalizzati · [2–3] · ⟵ B2.5.3
- **B2.5.5** Errori di rappresentazione (0,1 + 0,2 ≠ 0,3) e arrotondamento · [2] · ⟵ B2.5.3 · ⟶ A10.1.2
- **B2.5.6** Formati ridotti per l'IA (half, bfloat16, int8) · [3] · ⟵ B2.5.3 · ⟶ O9

### B2.6 Altre codifiche numeriche
- **B2.6.1** BCD (decimale codificato in binario) · [2] · ⟵ B2.1.5
- **B2.6.2** Codice Gray · [2] · ⟵ B2.1.2 · ⟶ C11
- **B2.6.3** Interi a precisione arbitraria (bignum) · [2–3] · ⟵ B2.3.4 · ⟶ N3.3
- **B2.6.4** Ordine dei byte: big-endian e little-endian · [2] · ⟵ B3.1 · ⟶ D6, J3

## B3 Unità di misura
- **B3.1** Bit, nibble, byte, word · [1] · ⟵ B1.5
- **B3.2** Multipli SI (kB, MB, GB) e IEC (KiB, MiB, GiB); l'ambiguità nell'uso comune · [1] · ⟵ B3.1, A1.2.2, A1.1.5
- **B3.3** Stimare dimensioni: una pagina di testo, una foto, una canzone, un film · [1] · ⟵ B3.2
- **B3.4** Velocità di trasmissione: bit/s e byte/s · [1] · ⟵ B3.2 · ⟶ J1
- **B3.5** La crescita delle capacità di memoria nel tempo: dal kilobyte al petabyte · [1] · ⟵ B3.2 · (v1.1, approfondimento)

## B4 Codifica del testo
- **B4.1** Caratteri, glifi, codici: l'idea di tabella di codifica · [1] · ⟵ B1.4
- **B4.2** ASCII a 7 bit; caratteri di controllo; fine riga (LF, CR LF) · [1] · ⟵ B4.1, B2.1.4
- **B4.3** ASCII esteso e code page (Latin-1, Windows-1252); il problema delle lettere accentate · [1] · ⟵ B4.2
- **B4.4** Unicode: punti di codice, piani, repertorio universale · [1–2] · ⟵ B4.3, B2.2.1
- **B4.5** UTF-8: codifica a lunghezza variabile, compatibilità con ASCII · [2] · ⟵ B4.4, B2.3.5
- **B4.6** UTF-16 e UTF-32; il BOM · [2] · ⟵ B4.5, B2.6.4
- **B4.7** Mojibake: errori di decodifica e come diagnosticarli · [2] · ⟵ B4.5
- **B4.8** Emoji, sequenze combinate, normalizzazione (NFC, NFD) · [2–3] · ⟵ B4.5
- **B4.9** Confronto e ordinamento di stringhe; collazione e maiuscole/minuscole secondo la lingua · [2–3] · ⟵ B4.4 · ⟶ L5
- **B4.10** Scritture da destra a sinistra e non latine · [3] · ⟵ B4.4 · ⟶ K5
- **B4.11** Codici storici per il testo: Morse, Baudot, EBCDIC · [1] · ⟵ B4.1 · (v1.1, approfondimento)
- **B4.12** L'arte ASCII · [1] · ⟵ B4.2 · (v1.1, approfondimento)

## B5 Codifica dei colori

### B5.1 Percezione e sintesi del colore
- **B5.1.1** Luce, spettro visibile, percezione del colore (i coni) · [1] · ⟵ —
- **B5.1.2** Sintesi additiva (luce) e sottrattiva (pigmenti) · [1] · ⟵ B5.1.1

### B5.2 Modelli di colore
- **B5.2.1** Modello RGB: canali e intensità da 0 a 255 · [1] · ⟵ B5.1.2, B3.1
- **B5.2.2** Modello CMYK e stampa · [1] · ⟵ B5.1.2
- **B5.2.3** Modelli HSV e HSL: tinta, saturazione, luminosità · [1–2] · ⟵ B5.2.1
- **B5.2.4** Scala di grigi; conversione da RGB con media pesata · [1] · ⟵ B5.2.1, A7.1.3
- **B5.2.5** Canale alfa, trasparenza e composizione · [2] · ⟵ B5.2.1

### B5.3 Profondità e notazione
- **B5.3.1** Profondità di colore (1, 8, 24, 32 bit); numero di colori 2ⁿ · [1] · ⟵ B5.2.1, A4.1.1
- **B5.3.2** Palette e colori indicizzati · [1] · ⟵ B5.3.1
- **B5.3.3** Notazione esadecimale `#RRGGBB` · [1] · ⟵ B5.2.1, B2.2.3 · ⟶ K3

### B5.4 Colore avanzato
- **B5.4.1** Spazi colore e gamut (sRGB, Display P3) · [2] · ⟵ B5.2.1
- **B5.4.2** Correzione gamma; percezione non lineare · [2–3] · ⟵ B5.4.1, A1.2.4
- **B5.4.3** Contrasto, accessibilità, daltonismo · [2] · ⟵ B5.2.3 · ⟶ K5, Q8
- **B5.4.4** Gestione del colore e profili ICC · [3] · ⟵ B5.4.1

## B6 Immagini
- **B6.1** Pixel; l'immagine raster come griglia · [1] · ⟵ B5.3.1
- **B6.2** Risoluzione, PPI/DPI, dimensioni fisiche · [1] · ⟵ B6.1
- **B6.3** Peso di un'immagine non compressa (larghezza × altezza × profondità) · [1] · ⟵ B6.1, B3.2
- **B6.4** Immagini vettoriali: primitive geometriche, scalabilità · [1] · ⟵ B6.1
- **B6.5** Raster e vettoriale a confronto; rasterizzazione e vettorializzazione · [1–2] · ⟵ B6.4
- **B6.6** Formati raster (BMP, PNG, GIF, JPEG, WebP) e quando usarli · [1–2] · ⟵ B6.3, B9.1.1
- **B6.7** Formati vettoriali (SVG, PDF, EPS) · [2] · ⟵ B6.4, B11.3 · ⟶ K12
- **B6.8** Metadati delle immagini (EXIF) e privacy · [1–2] · ⟵ B6.6, B11.6 · ⟶ U7
- **B6.9** Ricampionamento e interpolazione (ingrandire e rimpicciolire) · [2] · ⟵ B6.2 · ⟶ Q4
- **B6.10** Pixel art e sprite per videogiochi · [1–2] · ⟵ B6.6 · (v1.1, approfondimento)

## B7 Audio
- **B7.1** Il suono: onda, frequenza, ampiezza, campo udibile · [1] · ⟵ —
- **B7.2** Campionamento e frequenza di campionamento · [1] · ⟵ B7.1, B1.3
- **B7.3** Quantizzazione: profondità in bit, rumore di quantizzazione · [1] · ⟵ B7.2, B3.1
- **B7.4** Teorema di Nyquist-Shannon e aliasing (intuitivo; formale in A6.5.7) · [2] · ⟵ B7.2, A6.1.2
- **B7.5** Peso di un file audio (frequenza × bit × canali × durata) · [1] · ⟵ B7.3, B3.2
- **B7.6** Formati: WAV/PCM, FLAC, MP3, AAC, Opus · [1–2] · ⟵ B7.5, B9.1.1
- **B7.7** MIDI: rappresentazione simbolica della musica · [1] · ⟵ B1.4 · ⟶ Q6
- **B7.8** Decibel e scale logaritmiche · [2] · ⟵ B7.1, A1.2.5

## B8 Video
- **B8.1** Fotogrammi e frequenza dei fotogrammi · [1] · ⟵ B6.1
- **B8.2** Peso del video non compresso; bitrate · [1] · ⟵ B8.1, B6.3, B3.4
- **B8.3** Compressione video: fotogrammi chiave e compensazione del moto · [2–3] · ⟵ B8.2, B9.2.1
- **B8.4** Codec (H.264, H.265, AV1) e container (MP4, MKV, WebM) · [2] · ⟵ B8.3, B7.6
- **B8.5** Streaming e bitrate adattivo · [2] · ⟵ B8.4 · ⟶ J7
- **B8.6** Sottotitoli e tracce multiple · [2] · ⟵ B8.4, B4.5

## B9 Compressione

### B9.1 Compressione senza perdita
- **B9.1.1** Perché comprimere; rapporto di compressione · [1] · ⟵ B3.2
- **B9.1.2** Codifica a corse (RLE) · [1] · ⟵ B9.1.1
- **B9.1.3** Codifica di Huffman: costruzione dell'albero · [2] · ⟵ B9.1.1, A8.2.4
- **B9.1.4** Compressione a dizionario: LZ77, LZW, DEFLATE (ZIP, PNG) · [2–3] · ⟵ B9.1.2
- **B9.1.5** Limiti: nessun compressore riduce tutti i file · [2–3] · ⟵ B9.1.1, A4.1.4
- **B9.1.6** Formati d'archivio: ZIP, 7z, tar · [2] · ⟵ B9.1.4 · (v1.1, approfondimento)

### B9.2 Compressione con perdita
- **B9.2.1** Idea: eliminare ciò che non si percepisce · [1–2] · ⟵ B9.1.1
- **B9.2.2** La quantizzazione come fonte di perdita · [2] · ⟵ B9.2.1, B7.3
- **B9.2.3** JPEG: sottocampionamento cromatico, DCT, quantizzazione · [3] · ⟵ B9.2.2, A6.5.6
- **B9.2.4** MP3 e AAC: il modello psicoacustico · [3] · ⟵ B9.2.2, A6.5.6
- **B9.2.5** Artefatti; compromesso fra qualità e dimensione · [1–2] · ⟵ B9.2.1
- **B9.2.6** Compressione con reti neurali · [4] · ⟵ B9.2.3, O5
- **B9.2.7** Esperimenti di ascolto e di visione con diversi livelli di compressione · [2] · ⟵ B9.2.5 · (v1.1, approfondimento)

## B10 Rilevazione e correzione degli errori

### B10.1 Rilevazione
- **B10.1.1** Errori di trasmissione e di memorizzazione; il rumore · [1] · ⟵ B1.5
- **B10.1.2** Bit di parità (pari e dispari) · [1] · ⟵ B10.1.1, A2.1.3
- **B10.1.3** Parità bidimensionale · [1–2] · ⟵ B10.1.2
- **B10.1.4** Checksum e cifre di controllo · [1–2] · ⟵ B10.1.1, A1.4.1
- **B10.1.5** Rilevare o correggere: la ritrasmissione · [2] · ⟵ B10.1.2 · ⟶ J6

### B10.2 Codici a ridondanza ciclica
- **B10.2.1** CRC come divisione polinomiale con XOR · [2–3] · ⟵ B10.1.4, B2.3.5, A1.5.4
- **B10.2.2** CRC in Ethernet, ZIP, PNG · [2] · ⟵ B10.2.1

### B10.3 Codici correttori
- **B10.3.1** Distanza minima di un codice · [2] · ⟵ A8.3.3
- **B10.3.2** Codice di Hamming (7,4) · [2–3] · ⟵ B10.3.1, B10.1.2
- **B10.3.3** Codici Reed-Solomon (CD, QR code) · [4] · ⟵ B10.3.2, A4.4.4
- **B10.3.4** Codici moderni: LDPC, turbo, codici a fontana · [4] · ⟵ B10.3.2, A8.3.2 · ⟶ J9
- **B10.3.5** Memorie ECC e RAID come applicazioni · [2–3] · ⟵ B10.3.2 · ⟶ C17, I5

## B11 Dati strutturati
- **B11.1** Dati tabellari: record e campi · [1] · ⟵ B1.1
- **B11.2** CSV: separatori, virgolette, problemi comuni · [1] · ⟵ B11.1, B4.2
- **B11.3** Dati gerarchici: XML, tag e attributi; documento ben formato e valido · [2] · ⟵ B11.1, A4.3.3
- **B11.4** JSON: oggetti, array, tipi · [2] · ⟵ B11.1
- **B11.5** YAML, TOML e file di configurazione · [2] · ⟵ B11.4
- **B11.6** Metadati · [1] · ⟵ B1.1
- **B11.7** Schemi e validazione (XML Schema, JSON Schema) · [2–3] · ⟵ B11.3, B11.4
- **B11.8** Formati binari e serializzazione (Protocol Buffers, MessagePack) · [3] · ⟵ B11.4, B2.6.4
- **B11.9** Formati aperti e proprietari; interoperabilità · [1–2] · ⟵ B11.1 · ⟶ U4, L13
- **B11.10** Aprire dati pubblici in formato CSV (ISTAT, portali open data) · [2] · ⟵ B11.2 · (v1.1, approfondimento)

## B12 Codici identificativi
- **B12.1** Codici a barre (EAN-13) e cifra di controllo · [1] · ⟵ B10.1.4
- **B12.2** QR code: struttura e livelli di correzione · [1–2] · ⟵ B12.1, B10.1.2
- **B12.3** Codici con controllo: ISBN, IBAN, codice fiscale, carte di pagamento (algoritmo di Luhn) · [1–2] · ⟵ B10.1.4
- **B12.4** RFID e NFC · [2] · ⟵ B12.1 · ⟶ R10
- **B12.5** Identificatori univoci (UUID); l'hash come impronta · [2–3] · ⟵ B2.2.1 · ⟶ N3.2

## B13 Documenti digitali e tipografia digitale
- **B13.1** Testo semplice e testo formattato · [1] · ⟵ B4.2
- **B13.2** Font bitmap e vettoriali (TrueType, OpenType); famiglie e stili · [1–2] · ⟵ B6.4, B4.4
- **B13.3** Rendering del testo: antialiasing, hinting, crenatura · [2–3] · ⟵ B13.2
- **B13.4** Formati di documento: DOCX e ODF (XML compresso), PDF · [2] · ⟵ B13.1, B11.3, B9.1.4
- **B13.5** Markup leggero: Markdown · [1] · ⟵ B13.1 · ⟶ K2
- **B13.6** Composizione tipografica con LaTeX · [2–3] · ⟵ B13.5
- **B13.7** Accessibilità dei documenti · [2] · ⟵ B13.4 · ⟶ K5
- **B13.8** Firma digitale dei documenti; PDF/A per l'archiviazione · [2–3] · ⟵ B13.4, N3.4.1 · ⟶ L13
- **B13.9** Revisione e collaborazione sui documenti: commenti, revisioni, versioni · [1] · ⟵ B13.1 · (v1.1, approfondimento)
- **B13.10** Wiki e markup per la scrittura collaborativa · [2] · ⟵ B13.5 · (v1.1, approfondimento)
- **B13.11** Storia della tipografia: da Gutenberg ai caratteri digitali · [1–2] · ⟵ B13.2 · (v1.1, approfondimento)
- **B13.12** Caratteri e leggibilità: font ad alta leggibilità · [2] · ⟵ B13.2 · (v1.1, approfondimento)
