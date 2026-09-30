# Mappa dell'informatica — Area C: Fisica, elettronica e tecnologia dell'hardware (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** la base fisica ed elettronica del calcolo: dall'elettricità al transistor, dalla fabbricazione dei chip alla legge di Moore, fino alle memorie, alle interfacce e alle tecnologie emergenti. Nel grafo è il ponte fra la fisica e l'architettura (D).

---

## C1 Elettricità di base
- **C1.1** Grandezze fisiche, unità SI, prefissi (milli, micro, nano) · [1] · ⟵ A1.1.5
- **C1.2** Carica elettrica; conduttori e isolanti · [1] · ⟵ —
- **C1.3** Corrente, tensione, resistenza · [1] · ⟵ C1.2, C1.1
- **C1.4** Legge di Ohm · [1] · ⟵ C1.3, A1.5.2
- **C1.5** Potenza ed energia elettrica; effetto Joule · [1] · ⟵ C1.4
- **C1.6** Circuiti in serie e in parallelo · [1] · ⟵ C1.4
- **C1.7** Leggi di Kirchhoff; partitore di tensione · [2] · ⟵ C1.6, A1.5.3
- **C1.8** Corrente continua e alternata; la rete elettrica · [1–2] · ⟵ C1.3
- **C1.9** Strumenti di misura: multimetro, oscilloscopio · [1–2] · ⟵ C1.4
- **C1.10** Sicurezza elettrica · [1] · ⟵ C1.3

## C2 Componenti passivi
- **C2.1** Resistori; codice dei colori · [1] · ⟵ C1.4
- **C2.2** Condensatori: carica e scarica · [2] · ⟵ C1.4
- **C2.3** Circuito RC e costante di tempo · [2] · ⟵ C2.2, C2.1, A1.2.4
- **C2.4** Induttori; circuiti RL e RLC; risonanza · [3] · ⟵ C2.3, A6.4.2
- **C2.5** Breadboard e montaggio di circuiti · [1] · ⟵ C1.6, C2.1

## C3 Semiconduttori
- **C3.1** Bande di energia: conduttori, isolanti, semiconduttori · [2] · ⟵ C1.2
- **C3.2** Silicio; drogaggio di tipo N e P · [2] · ⟵ C3.1
- **C3.3** Giunzione PN; diodo e raddrizzamento · [2] · ⟵ C3.2, C1.8
- **C3.4** LED e fotodiodi · [2] · ⟵ C3.3 · ⟶ R1
- **C3.5** Celle fotovoltaiche · [2] · ⟵ C3.3

## C4 Transistor
- **C4.1** Il transistor come interruttore comandato (idea intuitiva) · [1] · ⟵ C1.3
- **C4.2** Transistor bipolare (BJT): funzionamento di base · [2] · ⟵ C3.3
- **C4.3** MOSFET: canale, gate, tensione di soglia · [2–3] · ⟵ C3.2, C4.1
- **C4.4** Il transistor come amplificatore · [2–3] · ⟵ C4.2
- **C4.5** Storia: relè, valvole termoioniche, transistor (1947) · [1] · ⟵ C4.1 · ⟶ U1

## C5 Logica CMOS
- **C5.1** Porte logiche realizzate con interruttori (anche con relè) · [1–2] · ⟵ C4.1, D1.2
- **C5.2** L'invertitore CMOS · [3] · ⟵ C4.3, C5.1
- **C5.3** Porte NAND e NOR in CMOS · [3] · ⟵ C5.2, A2.1.8
- **C5.4** Livelli logici, margini di rumore, fan-out · [2–3] · ⟵ C5.1
- **C5.5** Ritardo di propagazione e consumo dinamico (∝ C·V²·f) · [3] · ⟵ C5.2, C2.2, C1.5 · ⟶ C9.2
- **C5.6** Famiglie logiche (TTL, CMOS) · [2] · ⟵ C5.4

## C6 Elettronica analogica
- **C6.1** Amplificatore operazionale ideale · [2–3] · ⟵ C1.7
- **C6.2** Configurazioni invertente, non invertente, comparatore · [2–3] · ⟵ C6.1
- **C6.3** Filtri passa-basso e passa-alto · [3] · ⟵ C2.3, A6.5.1
- **C6.4** Oscillatori e generatori di clock (quarzo) · [3] · ⟵ C2.4 · ⟶ D5

## C7 Conversione analogico-digitale e digitale-analogico
- **C7.1** ADC: risoluzione e frequenza di conversione · [2] · ⟵ B7.2, B7.3, C6.2
- **C7.2** Architetture di ADC (a rampa, ad approssimazioni successive, flash) · [3] · ⟵ C7.1
- **C7.3** DAC; la PWM come conversione "povera" · [2] · ⟵ C7.1 · ⟶ R2

## C8 Circuiti integrati e fabbricazione
- **C8.1** Dal componente discreto al circuito integrato (Kilby, Noyce) · [1–2] · ⟵ C4.1
- **C8.2** Wafer di silicio, camere bianche · [2] · ⟵ C8.1, C3.2
- **C8.3** Fotolitografia (anche EUV), drogaggio, strati di metallizzazione · [2–3] · ⟵ C8.2
- **C8.4** Nodi di processo ("nanometri"): significato fisico e commerciale · [2–3] · ⟵ C8.3
- **C8.5** Resa produttiva, difetti, binning · [3] · ⟵ C8.3, A7.2.2
- **C8.6** Filiera dei semiconduttori: aziende fabless, fonderie, packaging · [2] · ⟵ C8.1 · ⟶ U5

## C9 Legge di Moore e scaling
- **C9.1** Enunciato e storia (1965, 1975); legge empirica, non legge fisica · [1–2] · ⟵ C8.1, A1.2.2
- **C9.2** Scaling di Dennard e sua fine (~2005); power wall · [3] · ⟵ C9.1, C5.5
- **C9.3** Conseguenze: multicore, acceleratori specializzati, "silicio scuro" · [3] · ⟵ C9.2 · ⟶ D11, D12, M1
- **C9.4** Oltre Moore: impilamento 3D, chiplet, nuovi materiali, "More than Moore" · [3–4] · ⟵ C9.3, C8.4
- **C9.5** Leggi analoghe: Kryder (memorie), Koomey (efficienza energetica), Nielsen (banda) · [2–3] · ⟵ C9.1
- **C9.6** Limiti fisici: scala atomica, effetto tunnel, dissipazione termica · [3] · ⟵ C9.2, C15.2

## C10 Tecnologie di memoria
- **C10.1** Principio della memorizzazione: stati fisici stabili · [1] · ⟵ B1.6
- **C10.2** SRAM (flip-flop) e DRAM (condensatore, refresh) · [2–3] · ⟵ C10.1, C2.2, C4.1
- **C10.3** Memorie non volatili: ROM, EEPROM, flash NAND e NOR; usura · [2–3] · ⟵ C10.1, C4.3
- **C10.4** Dischi magnetici: piatti, testine, tempo di accesso · [2] · ⟵ C10.1
- **C10.5** SSD: controller, wear leveling · [2–3] · ⟵ C10.3
- **C10.6** Supporti ottici (CD, DVD, Blu-ray) · [1–2] · ⟵ C10.1
- **C10.7** Nastri magnetici e archiviazione a lungo termine · [2] · ⟵ C10.4 · ⟶ L13
- **C10.8** Memorie emergenti (MRAM, ReRAM, a cambiamento di fase) · [4] · ⟵ C10.3

## C11 Periferiche e interfacce
- **C11.1** Dispositivi di input e di output: panoramica · [1] · ⟵ —
- **C11.2** Tastiera, mouse, encoder · [1–2] · ⟵ C11.1
- **C11.3** Display (LCD, OLED, e-ink); risoluzione e frequenza di aggiornamento · [1–2] · ⟵ C11.1, B6.2
- **C11.4** Stampanti (laser, a getto d'inchiostro, 3D) · [1] · ⟵ C11.1, B5.2.2
- **C11.5** Comunicazione seriale e parallela; il bus · [2] · ⟵ C11.1, B3.4
- **C11.6** USB, HDMI, Thunderbolt: evoluzione e prestazioni · [1–2] · ⟵ C11.1
- **C11.7** Protocolli per microcontrollori: UART, I²C, SPI · [2–3] · ⟵ C11.5 · ⟶ R2

## C12 Logica programmabile
- **C12.1** PLD e CPLD · [3] · ⟵ D2.9, D3.8
- **C12.2** FPGA: blocchi logici, tabelle di lookup, interconnessioni · [3] · ⟵ C12.1
- **C12.3** Linguaggi di descrizione dell'hardware (VHDL, Verilog) · [3] · ⟵ C12.2, G1
- **C12.4** Simulazione e sintesi di un progetto · [3] · ⟵ C12.3
- **C12.5** FPGA come acceleratori · [4] · ⟵ C12.2, D12

## C13 Energia e calore
- **C13.1** Consumo di un dispositivo: potenza, energia, capacità delle batterie (mAh, Wh) · [1] · ⟵ C1.5
- **C13.2** Dissipazione termica: dissipatori, ventole, raffreddamento a liquido · [1–2] · ⟵ C13.1
- **C13.3** Gestione dinamica di tensione e frequenza (DVFS) · [3] · ⟵ C5.5
- **C13.4** Consumi dei data center; indicatore PUE · [2–3] · ⟵ C13.1 · ⟶ M8, U6
- **C13.5** Alimentatori e conversione AC/DC · [2] · ⟵ C3.3, C1.8

## C14 Mezzi di trasmissione fisica
- **C14.1** Onde elettromagnetiche: frequenza, lunghezza d'onda, spettro · [1–2] · ⟵ B7.1
- **C14.2** Cavi in rame (doppino, coassiale); attenuazione e disturbi · [2] · ⟵ C14.1, C1.3
- **C14.3** Fibra ottica: riflessione totale, fibre monomodali e multimodali · [2] · ⟵ C14.1
- **C14.4** Radio: antenne, propagazione, bande libere e soggette a licenza · [2] · ⟵ C14.1
- **C14.5** Rapporto segnale/rumore · [2] · ⟵ C14.2, B7.8
- **C14.6** Codifica di linea (NRZ, Manchester) · [2–3] · ⟵ C14.2, B1.6 · ⟶ J4

## C15 Fisica quantistica di base
- **C15.1** Quantizzazione dell'energia; il fotone · [2–3] · ⟵ C14.1
- **C15.2** Dualismo onda-particella; effetto tunnel · [3] · ⟵ C15.1
- **C15.3** Sovrapposizione e misura (a livello concettuale) · [3] · ⟵ C15.2, A7.2.2
- **C15.4** Lo spin · [3–4] · ⟵ C15.3
- **C15.5** Postulati della meccanica quantistica (formalismo) · [4] · ⟵ C15.3, A5.4.2

## C16 Progettazione di sistemi digitali ed EDA
- **C16.1** Flusso di progetto di un chip: specifica, RTL, sintesi, piazzamento e instradamento · [3–4] · ⟵ C12.4, C8.3
- **C16.2** Simulazione e verifica funzionale · [3–4] · ⟵ C16.1
- **C16.3** Verifica formale dell'hardware · [4] · ⟵ C16.2, F9
- **C16.4** Collaudo del chip (test, scan chain) · [4] · ⟵ C16.1
- **C16.5** Hardware aperto (RISC-V, strumenti EDA open source) · [3–4] · ⟵ C16.1, D6

## C17 Affidabilità dell'hardware
- **C17.1** Guasti permanenti e transitori; tasso di guasto, MTBF · [2–3] · ⟵ C1.3, A7.3.2
- **C17.2** Invecchiamento ed elettromigrazione · [4] · ⟵ C17.1, C8.3
- **C17.3** Errori indotti da radiazione (soft error) · [3] · ⟵ C17.1, C10.2
- **C17.4** Ridondanza: TMR, memorie ECC, sostituzione a caldo · [3] · ⟵ C17.1, B10.3.5

## C18 Tecnologie emergenti di dispositivo
- **C18.1** Memristori e calcolo in memoria · [4] · ⟵ C10.8, C9.4
- **C18.2** Spintronica · [4] · ⟵ C15.4, C10.8
- **C18.3** Transistor a nanotubi e materiali bidimensionali (grafene) · [4] · ⟵ C4.3, C9.6
- **C18.4** Elettronica flessibile e stampata · [3–4] · ⟵ C8.3
- **C18.5** Fotonica integrata su silicio · [4] · ⟵ C14.3, C8.3 · ⟶ T10.3
