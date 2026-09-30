---
titolo: Videogioco "I cinque duchi" — schema dei 150 livelli con propedeuticità e approfondimenti
versione: 1.1
data: 2026-09-27
autore: Pietro Fabbri (con Claude)
deriva_da: videogioco-5-duchi-curricolo.md v0.1 (scansione dei livelli)
dipende_da: mappa-informatica.md v0.5 e file di area mappa-informatica-A…W.md (ID dei nodi)
dati: videogioco-5-duchi-livelli.json (stesso contenuto, in formato leggibile da programmi)
---

# Videogioco "I cinque duchi": schema dei 150 livelli

## 0. Che cosa contiene questo documento

Questo documento riprende la scansione dei 150 livelli (30 per anno, un duca per anno) del curricolo v0.1. Per ogni livello:

1. tiene **solo gli argomenti**, senza gli agganci storico-culturali;
2. controlla sulla mappa delle propedeuticità che **tutto ciò che serve prima sia già stato fatto**, nello stesso livello o in quelli precedenti. Quando manca qualcosa, lo aggiunge dentro il livello stesso oppure lo anticipa in un livello precedente;
3. aggiunge **due argomenti facoltativi di approfondimento**. Nessuno dei due è prerequisito di un argomento obbligatorio, in nessun punto del percorso.

Regole seguite, fissate da Pietro:

- **nessun argomento del curricolo v0.1 è stato tolto**: si è solo aggiunto;
- i contenuti si possono **anticipare** (anche da un anno a uno precedente) e **spostare all'interno dello stesso anno**;
- gli approfondimenti **non sono propedeutici a nulla** di quello che viene dopo.

## 1. Come leggere ogni livello

Ogni livello ha fino a cinque voci:

| Voce | Significato |
|---|---|
| **Nucleo** | Argomenti obbligatori nuovi del livello: sono quelli del curricolo v0.1, collegati ai nodi della mappa. |
| **Ripresa in un nuovo contesto** | Argomenti obbligatori già introdotti prima, che il livello riprende (per esempio il ciclo `for` in Python dopo il ciclo a conteggio in pseudocodice). |
| **Prerequisiti integrati nel livello** | Argomenti di informatica che mancavano e che servono per il nucleo. Sono obbligatori, fanno parte del livello e si trattano prima del nucleo. |
| **Prerequisiti di altre discipline, costruiti nel gioco** | Contenuti di matematica, fisica o biologia necessari per il nucleo. Il gioco li **costruisce per intero** e non si affida a ciò che le altre materie hanno già trattato o tratteranno. Si fanno nel livello, prima del nucleo, e sono obbligatori. |
| **Nota didattica** | Presente solo dove c'è una decisione didattica da rispettare (livelli 1-27 e 2-28). |
| **Approfondimenti facoltativi** | Due argomenti collegati, liberi, che non sbloccano nulla. Tutti i loro prerequisiti sono già stati trattati come obbligatori entro quel livello. |

Il codice fra apici inversi (per esempio `B2.1.4`) è l'ID del nodo nella mappa dell'informatica. Il titolo del nodo e i suoi prerequisiti si trovano nel file di area corrispondente.

## 2. Nessuna competenza in ingresso presupposta

Decisione di Pietro (27/09/2026): **tutto ciò che non è informatica ed è propedeutico, lo (ri)costruisce il gioco.** Il gioco quindi non presuppone nulla dalla scuola secondaria di primo grado e non si appoggia alla programmazione di matematica, fisica o scienze della classe. Ogni prerequisito non informatico compare come "prerequisito di altra disciplina, costruito nel gioco" nel primo livello che ne ha bisogno.

Conseguenze:
- i primi livelli del primo anno costruiscono anche numeri, potenze, divisione con resto, insiemi, logica elementare, statistica elementare, luce e suono;
- i livelli del quinto anno (5-2…5-9, 5-14) costruiscono limiti, derivate, integrali ed equazioni differenziali al livello minimo necessario per il nucleo. Sono i livelli più pesanti del gioco (vedi §6).

## 3. Metodo e verifica

- **Grafo di riferimento:** ogni argomento è collegato a un nodo della mappa (2375 nodi, grafo aciclico). I prerequisiti di un nodo sono quelli dichiarati nella mappa. Un prerequisito che indica un gruppo di nodi (per esempio `D2`) vale come "tutti i nodi del gruppo".
- **Controllo delle propedeuticità:** per ogni livello, nell'ordine del gioco, si calcolano **tutti** i prerequisiti (diretti e indiretti) dei nodi del nucleo. Quelli non ancora trattati vengono aggiunti al livello: come prerequisiti integrati se sono di informatica, come prerequisiti di altre discipline costruiti nel gioco negli altri casi. Non si presuppone nessuna competenza in ingresso (§2). Il controllo si ripete dopo ogni modifica, finché non manca più nulla.
- **Controllo degli approfondimenti:** per ciascuno dei 300 approfondimenti si verifica che:
  - non sia antenato di nessun nodo obbligatorio, in nessun livello;
  - non ripeta un altro approfondimento;
  - abbia un livello di difficoltà compatibile con l'anno;
  - abbia tutti i prerequisiti già trattati come obbligatori entro quel livello.
- **Esito finale:**
  - 150 livelli, con 425 nodi di nucleo, 50 prerequisiti informatici integrati, 87 prerequisiti di altre discipline costruiti nel gioco e 300 approfondimenti;
  - **0 prerequisiti mancanti** e **0 violazioni** sugli approfondimenti.
- **Nodi aggiunti alla mappa:** 99 nuovi nodi di approfondimento, marcati "(v1.1, approfondimento)" nei file di area. Servivano soprattutto nei primi livelli, dove la mappa aveva pochi argomenti facoltativi raggiungibili con le sole conoscenze iniziali.
- **Una correzione alla mappa:** i modelli epidemici `S14.4` ora richiedono la simulazione di equazioni differenziali (`A6.4.1`, `S1.4`) invece dello studio della stabilità dei sistemi, che avrebbe portato l'algebra lineare universitaria nel quinto anno.
- Gli script di verifica sono in `claude/videogioco-5-duchi-script.py.md` e si possono rieseguire dopo ogni modifica.

## 4. Spostamenti e anticipazioni rispetto al curricolo v0.1

### 4.1 Spostamenti all'interno dello stesso anno

| Anno | Da (v0.1) | A (v1.0) | Motivo |
|---|---|---|---|
| 1 | "Quantità d'informazione ★", in 1-3 | 1-27 | Richiede il logaritmo in base 2 e la probabilità elementare, costruiti in forma intuitiva insieme alla statistica. Il livello 1-3 resta sul bit. |
| 2 | 2-5 Sequenza, selezione, iterazione | 2-7 | Il ciclo a conteggio e le condizioni richiedono variabili ed espressioni. |
| 2 | 2-6 Variabili · 2-7 Espressioni | 2-5 · 2-6 | Come sopra. |
| 3 | 3-16 SVG | 3-24 | SVG è XML e si incorpora nell'HTML: viene dopo 3-22 XML e 3-23 HTML. |
| 3 | 3-17 Compressione senza perdita · 3-18 con perdita · 3-19 Audio | 3-16 · 3-18 · 3-17 | La compressione con perdita dell'audio (MP3) richiede campionamento e quantizzazione. |
| 3 | 3-22 Markup e Markdown · 3-23 XML · 3-24 HTML | 3-19 · 3-22 · 3-23 | Il concetto di markup prepara la prova 3-20 e precede XML e HTML. |
| 4 | 4-8 Pile e code | 4-2 | Classi e oggetti richiedono il concetto di tipo di dato astratto, costruito su pile e code. I livelli 4-2…4-7 scalano di uno. |
| 4 | 4-27 SQL DDL e DML | 4-24 | Per interrogare una tabella bisogna prima crearla e popolarla. I livelli SELECT, JOIN e aggregazioni scalano di uno. |

### 4.2 Anticipazioni (contenuti portati in un livello precedente)

| Contenuto | Dove era previsto o sarebbe servito | Dove è ora |
|---|---|---|
| Storia del calcolo, da abaco e macchine meccaniche a von Neumann, transistor e personal computer `U1.1…U1.13` | prerequisito di 2-8 (storia dei linguaggi) e 3-29 (licenze) | 1-15, 1-21 |
| Il transistor come interruttore `C4.1`, `C4.5` | prerequisito della storia del microprocessore | 1-14 |
| Primi passi di pensiero computazionale e selezione `E1.x`, `E3.1`, `E3.2` | anno 2 | 1-27 (la funzione SE del foglio elettronico) |
| Operazioni bit a bit `B2.3.5` | prerequisito di UTF-8 (1-11) | 1-8 |
| Array e scansione `E6.1.1`, `E6.1.2` | 2-21 | 2-15 (massimo, minimo, somma, media) |
| Dizionari `E6.1.6` | prerequisito di 5-21 | 2-21 |
| Kerckhoffs, one-time pad `N2.6`, `N2.7` | prerequisiti della crittografia di 5-24 | 2-24 |
| Strati di rete e trasporto `J3.1…J3.4`, `J6.1`, `J6.2` | anno 5 | 2-28 (indirizzi, DNS, pacchetti) |
| Tipo di dato astratto, pile e code `E6.3.1`, `E6.3.2`, `E6.3.5` | anno 4 | 3-13 (modularità) |
| Memoizzazione, tabelle hash, programmazione dinamica `E5.8`, `E6.5.1`, `E8.5` | prerequisiti di 5-21 (instradamento) | 3-8, 3-9 |
| Misurare i tempi `E9.8` | prerequisito di 5-25 | 3-7 |
| Correlazione e causalità `A7.1.6` | prerequisito di 5-28 | 2-26 |
| Code con priorità (heap) `E6.4.5` | prerequisito di Dijkstra (5-21) | 4-14 (alberi) |
| Liste di adiacenza e visita in ampiezza `E6.6.2`, `E7.3.1` | prerequisiti di Dijkstra | 5-16 (reti come grafi) |
| Imparare dai dati: esempi, classificazione, regressione `O4.1.1`, `O4.1.2` | 5-26 | 5-11 (minimi quadrati) |

## 5. Lo schema, livello per livello

## Anno 1 — Borso

### 1-1 · Informazione, dato, messaggio

- **Nucleo:** Dato, informazione, conoscenza: differenze `B1.1`
- **Approfondimenti facoltativi:** 1) Metadati `B11.6` · 2) La piramide dati-informazione-conoscenza-saggezza (DIKW) `L1.5`

### 1-2 · Analogico e digitale

- **Nucleo:** Segnale; grandezze analogiche e digitali `B1.2`; Discretizzazione: campionare nel tempo e quantizzare i valori (idea intuitiva) `B1.3`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Numeri naturali: successore, operazioni, ordinamento `A1.1.1`; Interi relativi, valore assoluto `A1.1.2`; Razionali: frazioni, rappresentazione decimale limitata e periodica `A1.1.3`
- **Approfondimenti facoltativi:** 1) Vantaggi e limiti del digitale: copie identiche, robustezza al rumore, obsolescenza dei supporti `B1.7` · 2) Strumenti analogici e digitali a confronto (orologi, termometri, dischi in vinile e streaming) `B1.8`

### 1-3 · Il bit

- **Nucleo:** Codifica: associare simboli a configurazioni; un codice come corrispondenza `B1.4`; Il bit come unità minima; quante informazioni distinguono n bit `B1.5`; Perché il binario: due stati fisici stabili e distinguibili `B1.6`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Potenze a esponente intero e loro proprietà `A1.2.1`; Insieme e appartenenza; rappresentazioni per elencazione, per proprietà, con diagrammi di Venn `A3.1.1`; Sottoinsiemi, insieme vuoto, insieme delle parti `A3.1.2`; Principi della somma e del prodotto; configurazioni possibili con n bit (2ⁿ) `A4.1.1`
- **Approfondimenti facoltativi:** 1) Il gioco delle venti domande: dimezzare le possibilità `B1.9` · 2) Segnalazioni a due simboli nella storia (fuochi, bandiere, telegrafo) `B1.10`

### 1-4 · Sistemi di numerazione posizionali

- **Nucleo:** Sistemi additivi (numeri romani) e posizionali; la base `B2.1.1`
- **Approfondimenti facoltativi:** 1) Sistemi di numerazione di altre culture: babilonese (base 60), maya (base 20) `B2.1.7` · 2) Tracce di altre basi nella vita quotidiana: ore, minuti, dozzine `B2.1.8`

### 1-5 · Conversioni binario ↔ decimale

- **Nucleo:** Numerazione binaria: contare in binario `B2.1.2`; Conversione binario → decimale (somma di potenze) `B2.1.3`; Conversione decimale → binario (divisioni successive) `B2.1.4`; Conversione fra basi qualsiasi `B2.1.5`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Potenze di 2 e di 10 (tabella da 2⁰ a 2²⁰; 2¹⁰ ≈ 10³) `A1.2.2`; Divisione euclidea: quoziente e resto `A1.3.1`
- **Approfondimenti facoltativi:** 1) BCD (decimale codificato in binario) `B2.6.1` · 2) Codice Gray `B2.6.2`

### 1-6 · Ottale ed esadecimale

- **Nucleo:** Basi 8 e 16 `B2.2.1`; Conversione rapida binario ↔ esadecimale per gruppi di 4 bit `B2.2.2`; Usi dell'esadecimale: colori, indirizzi di memoria, indirizzi MAC, dump `B2.2.3`
- **Approfondimenti facoltativi:** 1) Identificatori univoci (UUID); l'hash come impronta `B12.5` · 2) La codifica Base64: dati binari scritti come testo `B2.2.4`

### 1-7 · Unità di misura: bit, byte, prefissi SI e IEC

- **Nucleo:** Bit, nibble, byte, word `B3.1`; Multipli SI (kB, MB, GB) e IEC (KiB, MiB, GiB); l'ambiguità nell'uso comune `B3.2`; Stimare dimensioni: una pagina di testo, una foto, una canzone, un film `B3.3`; Velocità di trasmissione: bit/s e byte/s `B3.4`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Reali e irrazionali; approssimazione, cifre significative `A1.1.4`; Notazione scientifica e ordini di grandezza `A1.1.5`
- **Approfondimenti facoltativi:** 1) Ordine dei byte: big-endian e little-endian `B2.6.4` · 2) La crescita delle capacità di memoria nel tempo: dal kilobyte al petabyte `B3.5`

### 1-8 · Aritmetica binaria e overflow

- **Nucleo:** Addizione binaria e riporto `B2.3.1`; Sottrazione binaria e prestito `B2.3.2`; Parole di lunghezza fissa; overflow `B2.3.4`; Operazioni bit a bit (AND, OR, XOR, NOT) e maschere `B2.3.5`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Enunciati e valori di verità `A2.1.1`; Connettivi NOT, AND, OR `A2.1.2`; XOR, implicazione, bicondizionale; NAND e NOR `A2.1.3`
- **Approfondimenti facoltativi:** 1) Moltiplicazione e divisione binaria; lo scorrimento (shift) come ×2 e ÷2 `B2.3.3` · 2) Interi a precisione arbitraria (bignum) `B2.6.3`

### 1-9 · Codifica del testo: ASCII

- **Nucleo:** Caratteri, glifi, codici: l'idea di tabella di codifica `B4.1`; ASCII a 7 bit; caratteri di controllo; fine riga (LF, CR LF) `B4.2`
- **Approfondimenti facoltativi:** 1) Codici storici per il testo: Morse, Baudot, EBCDIC `B4.11` · 2) L'arte ASCII `B4.12`

### 1-10 · Prova di corte: codifiche e cifrario di Cesare ★

- **Nucleo:** Storia e terminologia: testo in chiaro, testo cifrato, chiave `N2.1`; Cifrari a sostituzione: il cifrario di Cesare `N2.2`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Congruenze, "aritmetica dell'orologio" `A1.4.1`
- **Approfondimenti facoltativi:** 1) Cifrari a trasposizione `N2.5` · 2) Steganografia: nascondere l'esistenza di un messaggio `N2.9`

### 1-11 · Unicode e UTF-8

- **Nucleo:** ASCII esteso e code page (Latin-1, Windows-1252); il problema delle lettere accentate `B4.3`; Unicode: punti di codice, piani, repertorio universale `B4.4`; UTF-8: codifica a lunghezza variabile, compatibilità con ASCII `B4.5`
- **Approfondimenti facoltativi:** 1) Mojibake: errori di decodifica e come diagnosticarli `B4.7` · 2) Emoji, sequenze combinate, normalizzazione (NFC, NFD) `B4.8`

### 1-12 · Colori: RGB e notazione esadecimale

- **Nucleo:** Sintesi additiva (luce) e sottrattiva (pigmenti) `B5.1.2`; Modello RGB: canali e intensità da 0 a 255 `B5.2.1`; Profondità di colore (1, 8, 24, 32 bit); numero di colori 2ⁿ `B5.3.1`; Notazione esadecimale `#RRGGBB` `B5.3.3`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Luce, spettro visibile, percezione del colore (i coni) `B5.1.1`
- **Approfondimenti facoltativi:** 1) Modello CMYK e stampa `B5.2.2` · 2) Palette e colori indicizzati `B5.3.2`

### 1-13 · Immagini raster: pixel e risoluzione

- **Nucleo:** Pixel; l'immagine raster come griglia `B6.1`; Risoluzione, PPI/DPI, dimensioni fisiche `B6.2`; Peso di un'immagine non compressa (larghezza × altezza × profondità) `B6.3`
- **Approfondimenti facoltativi:** 1) Ricampionamento e interpolazione (ingrandire e rimpicciolire) `B6.9` · 2) Fotogrammi e frequenza dei fotogrammi `B8.1`

### 1-14 · Hardware e software

- **Nucleo:** Dispositivi di input e di output: panoramica `C11.1`; Il programma memorizzato: dati e istruzioni nella stessa memoria `D4.1`; Il transistor come interruttore comandato (idea intuitiva) `C4.1`; Storia: relè, valvole termoioniche, transistor (1947) `C4.5`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Grandezze fisiche, unità SI, prefissi (milli, micro, nano) `C1.1`; Carica elettrica; conduttori e isolanti `C1.2`; Corrente, tensione, resistenza `C1.3`
- **Approfondimenti facoltativi:** 1) Sicurezza elettrica `C1.10` · 2) Dal componente discreto al circuito integrato (Kilby, Noyce) `C8.1`

### 1-15 · La macchina di von Neumann: CPU, memoria, bus

- **Nucleo:** L'architettura di von Neumann: CPU, memoria, I/O, bus `D4.2`; Registri: contatore di programma, registro istruzione, accumulatore, registri generali `D5.1`; Contare e calcolare prima delle macchine: dita, tacche, abaco, sistemi di numerazione `U1.1`; Calcolatrici meccaniche: Schickard, Pascal, Leibniz `U1.3`; Il telaio Jacquard e le schede perforate `U1.4`; Hollerith e il censimento statunitense; nascita di IBM `U1.7`; La seconda guerra mondiale: Enigma, Bletchley Park, Colossus, Zuse `U1.9`; ENIAC, EDVAC e l'architettura di von Neumann `U1.10`; Transistor, circuito integrato, microprocessore (Intel 4004, 1971; Federico Faggin) `U1.11`; Personal computer e interfacce grafiche (Xerox PARC, Apple, IBM PC) `U1.13`
- **Approfondimenti facoltativi:** 1) Storia dell'informatica in Italia: CEP di Pisa, Olivetti Elea e Programma 101 `U1.18` · 2) Architettura Harvard e Harvard modificata `D4.3`

### 1-16 · Il ciclo fetch-decode-execute

- **Nucleo:** Il ciclo di fetch, decodifica ed esecuzione `D5.2`
- **Approfondimenti facoltativi:** 1) Macchine didattiche (Little Man Computer, CPU simulate a 8 bit) `D4.5` · 2) Istruzione macchina: codice operativo e operandi `D6.1`

### 1-17 · Memorie: RAM, dischi, SSD, gerarchia di memoria

- **Nucleo:** Principio della memorizzazione: stati fisici stabili `C10.1`; Dischi magnetici: piatti, testine, tempo di accesso `C10.4`; Indirizzi e celle di memoria; spazio di indirizzamento `D8.1`; La gerarchia: registri, cache, RAM, memoria di massa (costo, capacità, velocità) `D8.2`
- **Approfondimenti facoltativi:** 1) Supporti ottici (CD, DVD, Blu-ray) `C10.6` · 2) Nastri magnetici e archiviazione a lungo termine `C10.7`

### 1-18 · Periferiche e bus

- **Nucleo:** Tastiera, mouse, encoder `C11.2`; Display (LCD, OLED, e-ink); risoluzione e frequenza di aggiornamento `C11.3`; Comunicazione seriale e parallela; il bus `C11.5`; USB, HDMI, Thunderbolt: evoluzione e prestazioni `C11.6`; Controller e porte di I/O `D9.1`
- **Approfondimenti facoltativi:** 1) Bus di sistema (dati, indirizzi, controllo); arbitraggio; PCI Express `D9.5` · 2) I/O a controllo di programma (polling) `D9.2`

### 1-19 · Porte logiche e algebra di Boole ★

- **Nucleo:** Tavole di verità; tautologie e contraddizioni `A2.1.4`; Variabili e funzioni booleane; tabella di verità di una funzione `D1.1`; Operatori e porte logiche AND, OR, NOT, NAND, NOR, XOR e i loro simboli `D1.2`; Proprietà e teoremi dell'algebra di Boole; De Morgan `D1.3`
- **Ripresa in un nuovo contesto:** Connettivi NOT, AND, OR `A2.1.2`; XOR, implicazione, bicondizionale; NAND e NOR `A2.1.3`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Equivalenze logiche; leggi di De Morgan `A2.1.5`
- **Approfondimenti facoltativi:** 1) Simulatori di circuiti logici (Logisim, Digital) `D2.2` · 2) Semplificazione algebrica `D1.4`

### 1-20 · Prova di corte: assemblare un calcolatore (scelta dei componenti, prestazioni, consumi)

- **Nucleo:** Consumo di un dispositivo: potenza, energia, capacità delle batterie (mAh, Wh) `C13.1`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Espressioni letterali; la lettera come incognita, parametro, variabile `A1.5.1`; Equazioni e disequazioni lineari `A1.5.2`; Legge di Ohm `C1.4`; Potenza ed energia elettrica; effetto Joule `C1.5`
- **Approfondimenti facoltativi:** 1) Circuiti in serie e in parallelo `C1.6` · 2) Dissipazione termica: dissipatori, ventole, raffreddamento a liquido `C13.2`

### 1-21 · Il sistema operativo: funzioni e sistemi più comuni

- **Nucleo:** Che cos'è un sistema operativo; gli strati hardware, sistema operativo, applicazioni `I1.1`; Funzioni: gestione delle risorse, astrazione, protezione `I1.2`; Interfacce grafiche: finestre, desktop, metafore `I7.2`; Uso consapevole del sistema: impostazioni, aggiornamenti, account `I7.3`; Unix e Linux: filosofia, distribuzioni `I8.1`; Windows `I8.2`; macOS `I8.3`; Sistemi mobili (Android, iOS); permessi delle app `I8.4`; Mainframe, minicomputer, time-sharing; Unix `U1.12`; Software libero e open source (GNU, Linux) `U1.15`
- **Prerequisiti integrati nel livello:** File e cartelle: nomi, estensioni, percorsi assoluti e relativi `I5.1`; La riga di comando: shell, comandi di base, navigazione fra cartelle `I7.1`
- **Approfondimenti facoltativi:** 1) Il processo di avvio del computer `I10.1` · 2) Gestori di pacchetti e installazione del software `I7.5`

### 1-22 · Processi e scheduling

- **Nucleo:** Programma e processo; stati di un processo `I2.1`; Scheduling: obiettivi e metriche `I2.5`
- **Approfondimenti facoltativi:** 1) Thread: thread utente e thread del kernel `I2.4` · 2) Descrittore di processo e cambio di contesto `I2.2`

### 1-23 · Gestione della memoria

- **Nucleo:** Lo spazio degli indirizzi di un processo `I4.1`
- **Approfondimenti facoltativi:** 1) Località spaziale e temporale `D8.3` · 2) Il collo di bottiglia di von Neumann `D4.4`

### 1-24 · File system: cartelle, percorsi, permessi, backup

- **Nucleo:** Operazioni sui file; metadati e attributi `I5.2`; Permessi e controllo degli accessi (rwx di Unix, ACL) `I5.4`; Backup: strategia 3-2-1, backup incrementali e differenziali `I11.3`
- **Ripresa in un nuovo contesto:** File e cartelle: nomi, estensioni, percorsi assoluti e relativi `I5.1`; La riga di comando: shell, comandi di base, navigazione fra cartelle `I7.1`
- **Approfondimenti facoltativi:** 1) Utenti, gruppi, privilegi (sudo, amministratore) `I11.1` · 2) File system diffusi: FAT, NTFS, ext4, APFS `I5.5`

### 1-25 · Il documento elettronico: struttura e stili

- **Nucleo:** Testo semplice e testo formattato `B13.1`
- **Approfondimenti facoltativi:** 1) Revisione e collaborazione sui documenti: commenti, revisioni, versioni `B13.9` · 2) Scrivere per un pubblico tecnico e non tecnico `U11.1`

### 1-26 · Foglio elettronico: celle, formule, riferimenti relativi e assoluti

- **Nucleo:** Celle, righe, colonne; tipi di dato nelle celle `L2.1`; Formule; riferimenti relativi e assoluti `L2.2`; Ordinare, filtrare, formattazione condizionale `L2.5`
- **Prerequisiti integrati nel livello:** Dati tabellari: record e campi `B11.1`
- **Approfondimenti facoltativi:** 1) Formati aperti e proprietari; interoperabilità `B11.9` · 2) Le formule dei fogli di calcolo come programmazione funzionale `G10.3`

### 1-27 · Foglio elettronico: funzioni, grafici, statistica descrittiva; quantità d'informazione di un evento ★

- **Nucleo:** Funzioni: somma, media, conteggio, SE, CERCA `L2.3`; Grafici `L2.4`; Varianza, deviazione standard, quartili `A7.1.4`; Quantità di informazione di un evento (−log₂ p); il bit come unità di misura `A8.1.1`
- **Prerequisiti integrati nel livello:** Problema, istanza, soluzione `E1.1`; Scomporre un problema in sottoproblemi `E1.2`; Algoritmo: definizione e proprietà (finitezza, non ambiguità, eseguibilità) `E1.5`; Esecutore e istruzioni elementari; esecutore umano e macchina `E1.6`; Sequenza `E3.1`; Selezione semplice e doppia `E3.2`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Radici ed esponenti razionali `A1.2.3`; Funzione esponenziale; crescita esponenziale `A1.2.4`; Logaritmi (in particolare log₂), proprietà, cambiamento di base `A1.2.5`; Unione, intersezione, differenza, complemento; corrispondenza con i connettivi logici `A3.1.3`; Prodotto cartesiano; coppie e n-uple `A3.1.4`; Relazione binaria; rappresentazioni con matrice e con grafo `A3.2.1`; Funzione come relazione; dominio, codominio, immagine `A3.3.1`; Funzioni notevoli per l'informatica: parte intera inferiore e superiore, mod, fattoriale `A3.3.5`; Permutazioni, disposizioni, combinazioni `A4.1.2`; Popolazione e campione; variabili qualitative e quantitative `A7.1.1`; Distribuzioni di frequenza; tabelle e grafici `A7.1.2`; Media, mediana, moda `A7.1.3`; Esperimento aleatorio, spazio campionario, eventi `A7.2.1`; Definizioni di probabilità (classica, frequentista, soggettiva); assiomi `A7.2.2`
- **Nota didattica:** la quantità d'informazione si presenta in forma intuitiva: quante domande sì/no servono per individuare un caso, quante volte si dimezzano le possibilità. Logaritmo in base 2 e probabilità si costruiscono a questo livello di intuizione, senza formalismo (decisione di Pietro, 27/09/2026).
- **Approfondimenti facoltativi:** 1) Numeri pseudocasuali e generatori `A7.2.5` · 2) Scala di grigi; conversione da RGB con media pesata `B5.2.4`

### 1-28 · Internet: struttura e servizi

- **Nucleo:** Che cos'è una rete: nodi, collegamenti, vantaggi `J2.1`; Classificazione per estensione: PAN, LAN, MAN, WAN `J2.2`; Struttura di Internet: provider, punti di interscambio, dorsali `J8.1`; Internet e Web: la differenza `K1.1`; Browser, server web, pagine `K1.2`; L'URL: schema, dominio, percorso, parametri `K1.3`
- **Prerequisiti integrati nel livello:** Sistema di comunicazione: sorgente, trasmettitore, canale, ricevitore `J1.1`
- **Approfondimenti facoltativi:** 1) Cavi sottomarini e infrastruttura fisica globale `J8.3` · 2) Tecnologie di accesso: DSL, fibra, rete mobile, satellite `J8.4`

### 1-29 · Cercare e valutare le fonti; regole e sicurezza in rete; l'IA come fonte ★

- **Nucleo:** Identità digitale e reputazione online `U7.1`; Impronta digitale e tracciamento `U7.2`; Valutare le fonti; disinformazione e misinformazione `U7.3`; Ingegneria sociale `N9.1`; Phishing: riconoscerlo e difendersi `N9.2`; Igiene digitale: aggiornamenti, backup, password `N9.3`; Identificazione, autenticazione, autorizzazione `N5.1`; Fattori di autenticazione; password robuste e gestori di password `N5.2`; Privacy a scuola e tutela dei minori online `U4.2`; Usare bene un motore di ricerca: operatori, valutazione dei risultati `L11.8`; Che cos'è l'intelligenza artificiale: definizioni e approcci `O1.1`; L'IA nella vita quotidiana: riconoscerla e usarla con consapevolezza `O1.6`; Usare i modelli: prompt, contesto, esempi `O6.4`; Allucinazioni, limiti, verifica delle risposte `O6.5`
- **Prerequisiti integrati nel livello:** Sicurezza informatica: riservatezza, integrità, disponibilità `N1.1`; Tecnologia e valori: la tecnologia non è neutrale `U3.1`; Protezione dei dati personali: GDPR, principi, basi giuridiche, diritti dell'interessato `U4.1`
- **Approfondimenti facoltativi:** 1) Autenticazione a più fattori; codici monouso `N5.3` · 2) Il test di Turing `O1.3`

### 1-30 · Prova finale dell'anno: inventario (foglio elettronico, codifiche, hardware)

- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi
- **Approfondimenti facoltativi:** 1) Impronta ambientale del digitale: produzione, uso, fine vita `U6.1` · 2) Mappa delle professioni ICT (sviluppatore, sistemista, data scientist, esperto di sicurezza…) `U9.1`


## Anno 2 — Ercole I

### 2-1 · Pensiero computazionale: scomporre un problema

- **Nucleo:** Riconoscere schemi ricorrenti `E1.3`; Astrazione: che cosa tenere e che cosa trascurare; il modello `E1.4`
- **Ripresa in un nuovo contesto:** Problema, istanza, soluzione `E1.1`; Scomporre un problema in sottoproblemi `E1.2`
- **Approfondimenti facoltativi:** 1) Attività unplugged (percorsi su griglia, ordinare carte) `E1.7` · 2) Rompicapi e giochi di logica come problemi computazionali (labirinti, travasi) `E1.9`

### 2-2 · Che cos'è un algoritmo

- **Nucleo:** Algoritmi nella vita quotidiana e loro limiti `E1.8`
- **Ripresa in un nuovo contesto:** Algoritmo: definizione e proprietà (finitezza, non ambiguità, eseguibilità) `E1.5`; Esecutore e istruzioni elementari; esecutore umano e macchina `E1.6`
- **Approfondimenti facoltativi:** 1) Algoritmi antichi: Euclide, al-Khwārizmī (origine della parola "algoritmo") `U1.2` · 2) Robot didattici programmabili (Bee-Bot, LEGO, mBot) `R12.1`

### 2-3 · Diagrammi di flusso

- **Nucleo:** Descrizione in linguaggio naturale; il problema dell'ambiguità `E2.1`; Diagrammi di flusso: simboli standard `E2.2`
- **Approfondimenti facoltativi:** 1) Programmazione a blocchi come rappresentazione eseguibile `E2.4` · 2) Strumenti per disegnare diagrammi di flusso eseguibili (Flowgorithm) `E2.6`

### 2-4 · Pseudocodice

- **Nucleo:** Pseudocodice `E2.3`
- **Approfondimenti facoltativi:** 1) Babbage (macchina differenziale e analitica) e Ada Lovelace `U1.5` · 2) Inglese tecnico `U11.7`

### 2-5 · Variabili, tipi, assegnazione

- **Nucleo:** La variabile come contenitore con nome; assegnazione `E4.1`; Tipi elementari: intero, reale, booleano, carattere, stringa `E4.2`; Input e output `E4.4`; Scambio di due variabili; misconcezioni sull'assegnazione `E4.6`; Simulare l'esecuzione a mano (tabella di traccia) `E2.5`
- **Approfondimenti facoltativi:** 1) Nomi delle variabili e convenzioni di scrittura (camelCase, snake_case) `E4.8` · 2) Variabili nei fogli di calcolo e nei programmi: somiglianze e differenze `E4.10`

### 2-6 · Espressioni e operatori logici

- **Nucleo:** Espressioni aritmetiche, relazionali e logiche; precedenza degli operatori `E4.3`
- **Approfondimenti facoltativi:** 1) Forme normali congiuntiva e disgiuntiva (CNF, DNF) `A2.1.6` · 2) Predicati, dominio, variabili libere e vincolate `A2.2.1`

### 2-7 · Sequenza, selezione, iterazione (Böhm-Jacopini)

- **Nucleo:** Selezione multipla; condizioni composte `E3.3`; Iterazione con condizione (ciclo con controllo in testa e in coda) `E3.4`; Iterazione a conteggio (ciclo for) `E3.5`; Terminazione dei cicli; cicli infiniti `E3.7`; Teorema di Böhm-Jacopini; programmazione strutturata `E3.8`
- **Ripresa in un nuovo contesto:** Sequenza `E3.1`; Selezione semplice e doppia `E3.2`
- **Approfondimenti facoltativi:** 1) Diagrammi di Nassi-Shneiderman `E3.10` · 2) Programmare un personaggio con sequenze, scelte e ripetizioni (giochi di coding) `E3.11`

### 2-8 · Tipologie di linguaggi: livelli, compilati e interpretati, breve storia

- **Nucleo:** Programma e linguaggio di programmazione; sintassi e semantica `G1.1`; L'ambiente di sviluppo: editor, interprete o compilatore, esecuzione `G1.2`; Le fasi di un compilatore: panoramica `G7.1.1`; I primi linguaggi: assembly, Fortran, COBOL, Lisp, ALGOL `G9.1`
- **Approfondimenti facoltativi:** 1) Linguaggi educativi: Logo, BASIC, Pascal, Scratch `G9.6` · 2) Programmazione strutturata: Pascal, C `G9.2`

### 2-9 · Il primo linguaggio (Python): input, output, sintassi

- **Nucleo:** Interprete, script, notebook `G2.2.1`; Tipi di base (int, float, bool, str); tipizzazione dinamica `G2.2.2`; Errori di sintassi, di esecuzione e logici; leggere i messaggi di errore `G1.3`; Variabili, tipi e assegnazione in un linguaggio reale `G1.4`; Operatori ed espressioni; conversioni di tipo `G1.5`; Input e output da console; formattazione `G1.6`; Commenti, nomi significativi, stile del codice `G1.11`
- **Approfondimenti facoltativi:** 1) Notebook computazionali (Jupyter) `G5.8.4` · 2) Piattaforme low-code e no-code `G10.2`

### 2-10 · Prova di corte: tracing di programmi

- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi
- **Approfondimenti facoltativi:** 1) Analisi statica e linter `H6.10` · 2) Tipizzazione statica e dinamica `G6.1`

### 2-11 · Selezione: if, elif, else

- **Nucleo:** Selezione e iterazione nel linguaggio `G1.7`; Strutture di controllo; l'indentazione come sintassi `G2.2.3`
- **Approfondimenti facoltativi:** 1) Struttura di un programma C; compilazione `G5.1.1` · 2) Selezione multipla con match/case `G1.16`

### 2-12 · Iterazione: while, contatori, accumulatori

- **Nucleo:** Costanti; contatori e accumulatori `E4.5`
- **Approfondimenti facoltativi:** 1) La congettura di Collatz (3n+1) esplorata con un programma `E4.9` · 2) Programmare in linguaggio naturale con assistenti IA `G10.4`

### 2-13 · Iterazione: for e range

- **Ripresa in un nuovo contesto:** Iterazione a conteggio (ciclo for) `E3.5`
- **Approfondimenti facoltativi:** 1) Tabelline e schemi numerici stampati con i cicli `E3.12` · 2) Cicli infiniti voluti: il ciclo principale di un gioco o di un dispositivo `E3.13`

### 2-14 · Cicli annidati

- **Nucleo:** Cicli annidati `E3.6`
- **Approfondimenti facoltativi:** 1) Forza bruta ed enumerazione `E8.1` · 2) Disegnare figure con i caratteri: triangoli, scacchiere, rombi `E3.14`

### 2-15 · Algoritmi classici: massimo, minimo, somma, media

- **Nucleo:** Array: accesso per indice, lunghezza `E6.1.1`; Scorrere un array: somma, massimo, conteggio `E6.1.2`; Ricerca del massimo e del minimo; ricerca con sentinella `E7.1.2`
- **Prerequisiti integrati nel livello:** Tipi composti: array e record `E4.7`; Ricerca lineare `E7.1.1`
- **Approfondimenti facoltativi:** 1) Il secondo massimo e il valore più frequente `E7.1.5` · 2) Media mobile sui dati di un sensore `E6.1.7`

### 2-16 · Algoritmo di Euclide e numeri primi

- **Nucleo:** Algoritmi aritmetici: Euclide, potenza veloce, crivello `E7.5.1`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Multipli, divisori, criteri di divisibilità `A1.3.2`; Numeri primi, crivello di Eratostene, fattorizzazione unica `A1.3.3`; MCD e mcm; algoritmo di Euclide `A1.3.4`
- **Approfondimenti facoltativi:** 1) Numeri perfetti, amicabili e congettura di Goldbach `E7.5.6` · 2) Semplificare frazioni con il massimo comune divisore `E7.5.7`

### 2-17 · Funzioni: definizione, parametri, valore di ritorno

- **Nucleo:** Sottoprogrammi: funzioni, parametri, valore restituito `E3.9`; Funzioni: definizione, parametri, valore restituito `G1.8`; Funzioni; parametri con valore predefinito e per nome `G2.2.7`
- **Approfondimenti facoltativi:** 1) Kotlin, Swift, PHP, Ruby, Lua, Dart, Zig: caratteristiche e ambiti d'uso `G5.11` · 2) Macro e automazione (VBA, Apps Script) `L2.8`

### 2-18 · Visibilità e scomposizione in funzioni

- **Nucleo:** Visibilità e durata delle variabili; locali e globali `G1.9`; Passaggio dei parametri: per valore, per riferimento, per condivisione `G1.10`; Stato, istruzioni, effetti collaterali `G3.1.1`; Programmazione procedurale; scomposizione dall'alto verso il basso `G3.1.2`
- **Approfondimenti facoltativi:** 1) Programmazione strutturata e istruzione goto `G3.1.3` · 2) Funzioni pure ed effetti collaterali `G3.3.1`

### 2-19 · Test e debugging

- **Nucleo:** Debugging: stampe di controllo, punti di interruzione, esecuzione passo passo `G1.12`; Verifica e validazione; errore, difetto, malfunzionamento `H6.1`; Test di unità e framework di test (pytest, JUnit) `H6.2`
- **Prerequisiti integrati nel livello:** Programma e prodotto software; le qualità attese `H1.1`; Le fasi: requisiti, analisi, progettazione, realizzazione, verifica, rilascio, manutenzione `H1.2`
- **Approfondimenti facoltativi:** 1) La "crisi del software" e la nascita dell'ingegneria del software `H1.3` · 2) Progettare i casi di test: classi di equivalenza, valori limite `H6.3`

### 2-20 · Prova di corte: problemi con funzioni

- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi
- **Approfondimenti facoltativi:** 1) Ruoli nel gruppo di sviluppo `H1.4` · 2) Requisiti funzionali e non funzionali `H11.1`

### 2-21 · Liste e array

- **Nucleo:** Liste e tuple `G2.2.5`; Array dinamici (le liste di Python); crescita ammortizzata `E6.1.3`; Dizionari (array associativi): uso `E6.1.6`
- **Approfondimenti facoltativi:** 1) Dizionari e insiemi `G2.2.6` · 2) Comprensioni di lista `G2.2.8`

### 2-22 · Ricerca lineare

- **Ripresa in un nuovo contesto:** Ricerca lineare `E7.1.1`
- **Approfondimenti facoltativi:** 1) Cercare nel mondo reale: indici, rubriche, dizionari cartacei `E7.1.6` · 2) Contare i confronti della ricerca lineare nel caso peggiore `E7.1.7`

### 2-23 · Stringhe e testo

- **Nucleo:** Stringhe come sequenze di caratteri `E6.1.5`; Stringhe: indici, slicing, metodi `G2.2.4`
- **Approfondimenti facoltativi:** 1) Confronto e ordinamento di stringhe; collazione e maiuscole/minuscole secondo la lingua `B4.9` · 2) Il testo come sequenza di caratteri; problemi di codifica `P3.1`

### 2-24 · Cifrari di Cesare e di Vigenère in codice ★

- **Nucleo:** Crittoanalisi con l'analisi delle frequenze `N2.3`; Il cifrario di Vigenère e come si rompe `N2.4`; Principio di Kerckhoffs `N2.6`; One-time pad e sicurezza perfetta `N2.7`
- **Approfondimenti facoltativi:** 1) Enigma e le macchine cifranti `N2.8` · 2) Cifrari del Rinascimento: il disco di Leon Battista Alberti `N2.10`

### 2-25 · Grafica con la tartaruga

- **Nucleo:** Coordinate dello schermo e pixel `Q1.1`; Disegnare primitive: punti, linee, forme (turtle, Processing) `Q1.2`; Grafica e giochi: turtle, pygame `G2.2.12`
- **Approfondimenti facoltativi:** 1) Creative coding: Processing, p5.js `Q14.1` · 2) Poligoni e stelle con la tartaruga: angoli esterni `Q1.8`

### 2-26 · Il caso: dadi, frequenze, probabilità simulate ★

- **Nucleo:** Probabilità condizionata e indipendenza `A7.2.3`; Numeri casuali nei programmi; simulazioni semplici `E7.5.2`; Modello e simulazione: perché simulare `S1.1`; Correlazione e causalità; paradosso di Simpson `A7.1.6`
- **Ripresa in un nuovo contesto:** Esperimento aleatorio, spazio campionario, eventi `A7.2.1`; Definizioni di probabilità (classica, frequentista, soggettiva); assiomi `A7.2.2`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Correlazione e regressione lineare semplice `A7.1.5`
- **Approfondimenti facoltativi:** 1) Teorema di Bayes `A7.2.4` · 2) Il problema di Monty Hall simulato `A7.2.6`

### 2-27 · Foglio elettronico avanzato: SE, CERCA, tabelle pivot

- **Nucleo:** Tabelle pivot `L2.6`; Il foglio di calcolo usato come base di dati, e i suoi limiti `L2.7`
- **Prerequisiti integrati nel livello:** Dati strutturati, semi-strutturati, non strutturati `L1.1`; Archivi tradizionali e basi di dati; i problemi di ridondanza e incoerenza `L1.4`
- **Approfondimenti facoltativi:** 1) Big data: volume, velocità, varietà, veridicità `L8.5` · 2) Organizzazione, processi, informazione `V1.1`

### 2-28 · Come è fatta Internet: indirizzi, DNS, pacchetti

- **Nucleo:** Commutazione di circuito e di pacchetto `J2.4`; Indirizzi IPv4: struttura, notazione, classi storiche `J5.1`; DNS: nomi di dominio, gerarchia, risoluzione `J7.1`
- **Prerequisiti integrati nel livello:** Perché gli strati: protocollo, servizio, interfaccia `J3.1`; Il modello ISO/OSI `J3.2`; La pila TCP/IP e il confronto con OSI `J3.3`; Incapsulamento: intestazioni e unità di dati (trama, pacchetto, segmento) `J3.4`; Porte e multiplazione delle applicazioni `J6.1`; UDP `J6.2`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Grafo: nodi, archi; orientato e non orientato; pesato `A4.3.1`; Grado, cammini, cicli, connessione (i ponti di Königsberg) `A4.3.2`; Alberi: radice, foglie, altezza; alberi ricoprenti `A4.3.3`
- **Nota didattica:** livello volutamente denso: gli strati di rete sono anticipati dal quinto anno per spiegare indirizzi, DNS e pacchetti (decisione di Pietro, 27/09/2026). Nella scala di difficoltà interna conviene separarli in più tappe.
- **Approfondimenti facoltativi:** 1) Sincronizzazione dell'orologio (NTP) `J7.9` · 2) Enti di standardizzazione: IETF, IEEE, ITU, W3C, ISO `J14.1`

### 2-29 · Collaborare in rete: cloud, posta elettronica, privacy, diritto d'autore

- **Nucleo:** Il cloud nella vita scolastica: suite collaborative, archiviazione condivisa `M4.8`; Strumenti di collaborazione: documenti condivisi, videoconferenza `Q13.1`; Diritto d'autore e opere digitali `U4.3`; Creative Commons e contenuti aperti `U4.5`; Cyberbullismo, comportamento online, netiquette `U7.7`
- **Ripresa in un nuovo contesto:** Protezione dei dati personali: GDPR, principi, basi giuridiche, diritti dell'interessato `U4.1`
- **Approfondimenti facoltativi:** 1) Codice dell'amministrazione digitale; firma digitale, PEC, SPID `U4.10` · 2) Bolle di filtro e algoritmi di raccomandazione (livello divulgativo) `U7.4`

### 2-30 · Prova finale dell'anno: generare una pianta rispettando vincoli

- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi
- **Approfondimenti facoltativi:** 1) Quadro europeo DigComp 2.2 `U7.10` · 2) Comunità online e piattaforme sociali `Q13.2`


## Anno 3 — Alfonso I

### 3-1 · Interi con segno e complemento a 2

- **Nucleo:** Modulo e segno `B2.4.1`; Complemento a 1 `B2.4.2`; Complemento a 2: rappresentazione e intervallo rappresentabile `B2.4.3`; Sottrazione come somma in complemento a 2; overflow con segno `B2.4.4`; Rappresentazione in eccesso (con bias) `B2.4.5`
- **Approfondimenti facoltativi:** 1) Tipi interi con e senza segno nei linguaggi (int, unsigned, long) `B2.4.6` · 2) Errori famosi dovuti all'overflow (Ariane 5, problema dell'anno 2038) `B2.4.7`

### 3-2 · Virgola mobile (IEEE 754) ed errori di rappresentazione

- **Nucleo:** Numeri frazionari in binario (moltiplicazioni successive); frazioni non rappresentabili esattamente `B2.1.6`; Virgola fissa `B2.5.1`; Notazione scientifica in base 2: segno, mantissa, esponente `B2.5.2`; Standard IEEE 754 a precisione singola e doppia `B2.5.3`; Errori di rappresentazione (0,1 + 0,2 ≠ 0,3) e arrotondamento `B2.5.5`
- **Approfondimenti facoltativi:** 1) Valori speciali: zero con segno, infiniti, NaN, numeri denormalizzati `B2.5.4` · 2) Formati ridotti per l'IA (half, bfloat16, int8) `B2.5.6`

### 3-3 · Array e matrici

- **Nucleo:** Matrici e array multidimensionali `E6.1.4`
- **Approfondimenti facoltativi:** 1) Il Gioco della vita di Conway `S11.2` · 2) Matrice di adiacenza `E6.6.1`

### 3-4 · Ordinamento: selection sort e bubble sort

- **Nucleo:** Il problema dell'ordinamento; stabilità e ordinamento in loco `E7.2.1`; Ordinamento per selezione (selection sort) `E7.2.2`; Bubble sort `E7.2.3`
- **Approfondimenti facoltativi:** 1) Ordinamenti non basati su confronti: counting, radix, bucket `E7.2.8` · 2) Algoritmi greedy e quando funzionano `E8.3`

### 3-5 · Ordinamento: insertion sort; confronti e scambi

- **Nucleo:** Ordinamento per inserimento (insertion sort) `E7.2.4`
- **Approfondimenti facoltativi:** 1) Visualizzare gli algoritmi di ordinamento (animazioni, danze) `E7.2.11` · 2) Ordinare dati composti: chiavi di ordinamento e stabilità in pratica `E7.2.12`

### 3-6 · Ricerca binaria; logaritmi ★

- **Nucleo:** Ricerca binaria su un array ordinato `E7.1.3`
- **Ripresa in un nuovo contesto:** Logaritmi (in particolare log₂), proprietà, cambiamento di base `A1.2.5`
- **Approfondimenti facoltativi:** 1) Ricerca binaria sulla risposta (bisezione) `E7.1.4` · 2) Indovina il numero: la strategia migliore `E7.1.8`

### 3-7 · Contare i passi: complessità intuitiva

- **Nucleo:** Costo di un algoritmo: contare le operazioni `E9.2`; Confronto di crescite: costante, logaritmica, lineare, n log n, polinomiale, esponenziale, fattoriale `A1.2.6`; Misurare sperimentalmente i tempi `E9.8`
- **Approfondimenti facoltativi:** 1) Tempi di esecuzione reali: dai microsecondi ai secoli `E9.10` · 2) Il commesso viaggiatore giocato a mano `E9.11`

### 3-8 · Ricorsione

- **Nucleo:** Definizioni ricorsive: caso base e passo ricorsivo `E5.1`; Ricorsione sui numeri: fattoriale, Fibonacci, potenza `E5.2`; La pila delle chiamate e la traccia di esecuzione `E5.3`; Classici: torre di Hanoi, permutazioni, flood fill `E5.6`; Memoizzazione `E5.8`
- **Prerequisiti integrati nel livello:** Funzione hash: dal valore all'indice `E6.5.1`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Definire per casi base e casi induttivi (numeri naturali, liste, alberi, espressioni) `A3.5`; Successioni definite per ricorrenza (Fibonacci) `A4.2.1`
- **Approfondimenti facoltativi:** 1) Ricorsione e iterazione: equivalenza, ricorsione di coda `E5.4` · 2) Backtracking (N regine, sudoku) `E8.4`

### 3-9 · Divide et impera: merge sort ★

- **Nucleo:** Divide et impera `E8.2`; Merge sort `E7.2.5`; Fusione di sequenze ordinate `E7.2.10`; Programmazione dinamica: sottostruttura ottima, tabelle `E8.5`
- **Approfondimenti facoltativi:** 1) Quick sort; scelta del pivot `E7.2.6` · 2) Distanza di edit (Levenshtein) `E7.4.4`

### 3-10 · Prova di corte: ordinare e contare i passi

- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi
- **Approfondimenti facoltativi:** 1) Più lunga sottosequenza comune `E7.4.5` · 2) Insiemi e dizionari implementati con hash `E6.5.4`

### 3-11 · Stringhe avanzate e ricerca di schemi; automi ★

- **Nucleo:** Ricerca ingenua di una sottostringa `E7.4.1`; Espressioni regolari come strumento pratico di ricerca `E7.4.6`; Automa a stati finiti deterministico (DFA): stati, transizioni, accettazione `F1.1`; Espressioni regolari in senso formale `F1.3`
- **Ripresa in un nuovo contesto:** Funzione hash: dal valore all'indice `E6.5.1`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Alfabeti, stringhe, sequenze; multiinsiemi `A3.1.5`
- **Approfondimenti facoltativi:** 1) Rabin-Karp e hash di stringhe `E7.4.3` · 2) Knuth-Morris-Pratt e Boyer-Moore `E7.4.2`

### 3-12 · File e CSV

- **Nucleo:** CSV: separatori, virgolette, problemi comuni `B11.2`; Leggere e scrivere file di testo `G1.13`; Gestione delle eccezioni `G1.14`; File ed eccezioni in Python `G2.2.9`
- **Ripresa in un nuovo contesto:** Dati tabellari: record e campi `B11.1`
- **Approfondimenti facoltativi:** 1) Aprire dati pubblici in formato CSV (ISTAT, portali open data) `B11.10` · 2) R: vettori, data frame, statistica `G5.8.1`

### 3-13 · Metodologie di programmazione: top-down e modularità

- **Nucleo:** Moduli e librerie `G1.15`; Modularità, astrazione, occultamento dell'informazione `H4.1`; Coesione e accoppiamento `H4.2`
- **Prerequisiti integrati nel livello:** Pila (LIFO): push e pop `E6.3.1`; Coda (FIFO); buffer circolare `E6.3.2`; Tipo di dato astratto: interfaccia e implementazione `E6.3.5`
- **Approfondimenti facoltativi:** 1) Progettare le API `H4.7` · 2) Architettura a strati e MVC `H4.9`

### 3-14 · Documentazione, stile, controllo di versione (Git) ★

- **Nucleo:** Controllo di versione: storia, versioni, differenze `H5.1`; Git: repository, commit, stato, cronologia `H5.2`; Buone pratiche: messaggi di commit, .gitignore, tag `H5.7`; Documentazione nel codice: docstring, generatori automatici `H8.2`; Guide di stile e convenzioni di codifica `H8.3`
- **Approfondimenti facoltativi:** 1) Rami e fusioni; conflitti `H5.3` · 2) Storia dei sistemi di controllo di versione `H5.8`

### 3-15 · Formati di immagine: bitmap e vettoriale

- **Nucleo:** Immagini vettoriali: primitive geometriche, scalabilità `B6.4`; Raster e vettoriale a confronto; rasterizzazione e vettorializzazione `B6.5`; Formati raster (BMP, PNG, GIF, JPEG, WebP) e quando usarli `B6.6`
- **Prerequisiti integrati nel livello:** Perché comprimere; rapporto di compressione `B9.1.1`
- **Approfondimenti facoltativi:** 1) Pixel art e sprite per videogiochi `B6.10` · 2) Patrimonio culturale digitale: digitalizzazione, musei, archivi `S10.1`

### 3-16 · Compressione senza perdita: RLE e Huffman

- **Nucleo:** Codifica a corse (RLE) `B9.1.2`; Codifica di Huffman: costruzione dell'albero `B9.1.3`; Compressione a dizionario: LZ77, LZW, DEFLATE (ZIP, PNG) `B9.1.4`; Limiti: nessun compressore riduce tutti i file `B9.1.5`
- **Ripresa in un nuovo contesto:** Perché comprimere; rapporto di compressione `B9.1.1`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Coefficienti binomiali, triangolo di Tartaglia `A4.1.3`; Principio dei cassetti `A4.1.4`; Variabili discrete: Bernoulli, binomiale, geometrica, Poisson `A7.3.1`; Valore atteso e varianza `A7.3.2`; Entropia di una sorgente `A8.1.2`; Codici a lunghezza fissa e variabile; codici prefissi `A8.2.1`; Codifica di Huffman e codifica aritmetica `A8.2.4`
- **Approfondimenti facoltativi:** 1) Ridondanza del linguaggio naturale (esperimento di Shannon) `A8.1.4` · 2) Disuguaglianza di Kraft `A8.2.2`

### 3-17 · Audio digitale: campionamento e quantizzazione

- **Nucleo:** Campionamento e frequenza di campionamento `B7.2`; Quantizzazione: profondità in bit, rumore di quantizzazione `B7.3`; Teorema di Nyquist-Shannon e aliasing (intuitivo; formale in A6.5.7) `B7.4`; Peso di un file audio (frequenza × bit × canali × durata) `B7.5`; Formati: WAV/PCM, FLAC, MP3, AAC, Opus `B7.6`; MIDI: rappresentazione simbolica della musica `B7.7`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Funzioni elementari e loro grafici: lineari, quadratiche, esponenziali, logaritmiche `A6.1.1`; Funzioni trigonometriche; oscillazioni: periodo, frequenza, fase `A6.1.2`; Il suono: onda, frequenza, ampiezza, campo udibile `B7.1`
- **Approfondimenti facoltativi:** 1) Registrare e modificare l'audio (Audacity) `Q6.1` · 2) Sintesi del suono: oscillatori, inviluppi, sintesi sottrattiva `Q6.2`

### 3-18 · Compressione con perdita: l'idea di JPEG e MP3

- **Nucleo:** Idea: eliminare ciò che non si percepisce `B9.2.1`; La quantizzazione come fonte di perdita `B9.2.2`; Artefatti; compromesso fra qualità e dimensione `B9.2.5`
- **Approfondimenti facoltativi:** 1) Esperimenti di ascolto e di visione con diversi livelli di compressione `B9.2.7` · 2) Idea di spettro: un segnale come somma di sinusoidi `A6.5.1`

### 3-19 · Linguaggi di markup: il concetto, Markdown

- **Nucleo:** Markup leggero: Markdown `B13.5`
- **Approfondimenti facoltativi:** 1) Composizione tipografica con LaTeX `B13.6` · 2) Wiki e markup per la scrittura collaborativa `B13.10`

### 3-20 · Prova di corte: formati, compressione, qualità

- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi
- **Approfondimenti facoltativi:** 1) Formati d'archivio: ZIP, 7z, tar `B9.1.6` · 2) L'immagine come matrice; l'istogramma `Q4.1`

### 3-21 · Font e tipografia digitale

- **Nucleo:** Font bitmap e vettoriali (TrueType, OpenType); famiglie e stili `B13.2`; Rendering del testo: antialiasing, hinting, crenatura `B13.3`
- **Approfondimenti facoltativi:** 1) Storia della tipografia: da Gutenberg ai caratteri digitali `B13.11` · 2) Caratteri e leggibilità: font ad alta leggibilità `B13.12`

### 3-22 · XML: elementi, attributi, buona formazione

- **Nucleo:** Dati gerarchici: XML, tag e attributi; documento ben formato e valido `B11.3`; JSON: oggetti, array, tipi `B11.4`; Schemi e validazione (XML Schema, JSON Schema) `B11.7`
- **Approfondimenti facoltativi:** 1) YAML, TOML e file di configurazione `B11.5` · 2) Formati di documento: DOCX e ODF (XML compresso), PDF `B13.4`

### 3-23 · HTML: struttura e semantica

- **Nucleo:** Il documento HTML: tag, elementi, attributi, struttura `K2.1`; Testo, titoli, paragrafi, elenchi `K2.2`; Collegamenti e percorsi relativi `K2.3`; Immagini e contenuti multimediali `K2.4`; Tabelle `K2.5`; Moduli e controlli di input `K2.6`; HTML semantico (header, nav, main, article) `K2.7`; Validazione del codice HTML `K2.8`; Metadati della pagina e codifica dei caratteri `K2.9`
- **Approfondimenti facoltativi:** 1) Dati strutturati nelle pagine (schema.org, JSON-LD) `K10.1` · 2) Immagini nel web: formati e immagini responsive `K12.1`

### 3-24 · SVG: la grafica vettoriale come testo

- **Nucleo:** Formati vettoriali (SVG, PDF, EPS) `B6.7`; SVG nel web `K12.2`
- **Approfondimenti facoltativi:** 1) Animare la grafica SVG `K12.6` · 2) Progettare un'icona vettoriale `K12.7`

### 3-25 · CSS: selettori, box model, colori

- **Nucleo:** Regole, selettori, proprietà; cascata ed ereditarietà `K3.1`; Colori e unità di misura `K3.2`; Tipografia web e font `K3.3`; Il box model `K3.4`; Posizionamento e flusso del documento `K3.5`
- **Approfondimenti facoltativi:** 1) Transizioni e animazioni `K3.9` · 2) Temi chiari e scuri; variabili CSS `K3.11`

### 3-26 · Impaginazione e design responsive

- **Nucleo:** Flexbox `K3.6`; Grid `K3.7`; Design responsive: media query, approccio mobile first `K3.8`
- **Approfondimenti facoltativi:** 1) Preprocessori e framework CSS `K3.10` · 2) CSS per la stampa `K3.12`

### 3-27 · Progettazione web: usabilità e accessibilità

- **Nucleo:** L'interazione uomo-macchina: definizione e storia delle interfacce `Q8.1`; Basi di psicologia cognitiva: percezione, attenzione, memoria, modelli mentali `Q8.2`; Principi di usabilità ed euristiche di Nielsen `Q8.3`; Perché l'accessibilità; disabilità e tecnologie assistive `K5.1`; Linee guida WCAG: principi e livelli di conformità `K5.2`; Testi alternativi, struttura dei titoli, etichette dei moduli `K5.3`; Contrasto dei colori e navigazione da tastiera `K5.4`
- **Prerequisiti integrati nel livello:** Modelli HSV e HSL: tinta, saturazione, luminosità `B5.2.3`; Contrasto, accessibilità, daltonismo `B5.4.3`; Accessibilità come diritto; disabilità e tecnologie assistive `U8.3`
- **Approfondimenti facoltativi:** 1) Verificare l'accessibilità: strumenti automatici e lettori di schermo `K5.6` · 2) Design persuasivo e dark pattern `Q8.10`

### 3-28 · JavaScript di base: la pagina che reagisce ★

- **Nucleo:** Inserire script in una pagina; la console `K4.1`; Il DOM: selezionare e modificare elementi `K4.2`; Gli eventi del browser `K4.3`
- **Prerequisiti integrati nel livello:** Nodi e riferimenti; lista semplice `E6.2.1`; Alberi: terminologia e rappresentazione `E6.4.1`; Eventi, gestori (callback) e ciclo degli eventi `G3.6.1`; Sintassi, tipi, oggetti e array in JavaScript `G5.5.1`
- **Approfondimenti facoltativi:** 1) Validazione dei moduli lato client `K4.4` · 2) API del browser: canvas, geolocalizzazione, audio `K4.7`

### 3-29 · Pubblicare un sito; licenze e diritto d'autore

- **Nucleo:** Hosting, domini e DNS per un sito `K8.1`; Pubblicare un sito statico (GitHub Pages, Netlify) `K8.2`; Licenze software: proprietarie, copyleft (GPL), permissive (MIT, Apache) `U4.4`
- **Prerequisiti integrati nel livello:** Repository remoti (GitHub, GitLab); push e pull `H5.4`
- **Approfondimenti facoltativi:** 1) Generatori di siti statici (Hugo, Jekyll) `K8.3` · 2) Scegliere una licenza per il proprio software `H8.4`

### 3-30 · Prova finale dell'anno: un sito completo (testi marcati, immagini ottimizzate, stile)

- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi
- **Approfondimenti facoltativi:** 1) Obblighi normativi (Legge Stanca, European Accessibility Act) `K5.7` · 2) Progettazione centrata sull'utente: personas e scenari `Q8.4`


## Anno 4 — Ercole II

### 4-1 · Astrazione: dal problema al modello

- **Nucleo:** Perché modellare; UML: panoramica dei diagrammi `H3.1`
- **Approfondimenti facoltativi:** 1) Diagrammi di sequenza e di attività `H3.4` · 2) Diagrammi di stato `H3.5`

### 4-2 · Pile e code

- **Nucleo:** Coda a doppio ingresso (deque) `E6.3.3`; Applicazioni: parentesi bilanciate, notazione polacca inversa, annulla/ripeti `E6.3.4`
- **Ripresa in un nuovo contesto:** Pila (LIFO): push e pop `E6.3.1`; Coda (FIFO); buffer circolare `E6.3.2`; Tipo di dato astratto: interfaccia e implementazione `E6.3.5`
- **Approfondimenti facoltativi:** 1) Algoritmi di scheduling: FCFS, SJF, round robin, priorità, code multilivello `I2.6` · 2) Code con priorità nella vita quotidiana: il triage `E6.3.6`

### 4-3 · Classi e oggetti

- **Nucleo:** Classi e oggetti; attributi e metodi `G3.2.1`; Classi e oggetti in Python `G2.2.11`
- **Approfondimenti facoltativi:** 1) Programmare interfacce grafiche `G3.6.2` · 2) Tipizzazione statica, classi, package `G5.4.1`

### 4-4 · Attributi, metodi, costruttori

- **Nucleo:** Costruttori, stato e identità di un oggetto `G3.2.2`; Membri statici `G3.2.8`
- **Approfondimenti facoltativi:** 1) Riflessione e introspezione `G8.1` · 2) Metodi speciali in Python (__str__, __eq__) `G3.2.10`

### 4-5 · Incapsulamento

- **Nucleo:** Incapsulamento e visibilità `G3.2.3`
- **Approfondimenti facoltativi:** 1) Proprietà: getter, setter e @property `G3.2.11` · 2) Oggetti immutabili e dataclass `G3.2.12`

### 4-6 · Ereditarietà

- **Nucleo:** Ereditarietà `G3.2.4`; Composizione e aggregazione in alternativa all'ereditarietà `G3.2.7`
- **Approfondimenti facoltativi:** 1) Ereditarietà multipla e ordine di risoluzione dei metodi `G3.2.13` · 2) Gerarchie di classi nella libreria standard: le eccezioni `G3.2.14`

### 4-7 · Polimorfismo e interfacce

- **Nucleo:** Polimorfismo e ridefinizione dei metodi `G3.2.5`; Classi astratte e interfacce `G3.2.6`
- **Approfondimenti facoltativi:** 1) Programmazione basata su prototipi (JavaScript) `G3.2.9` · 2) Sintassi, tipi, struct e interfacce `G5.6.1`

### 4-8 · Diagramma UML delle classi

- **Nucleo:** Diagramma dei casi d'uso `H3.2`; Diagramma delle classi `H3.3`
- **Approfondimenti facoltativi:** 1) Diagrammi dei componenti e di dislocamento `H3.6` · 2) Diagrammi come codice (PlantUML, Mermaid) `H3.9`

### 4-9 · Liste collegate e riferimenti ★

- **Nucleo:** Variabili e indirizzi di memoria `G4.1`; Riferimenti e puntatori; aritmetica dei puntatori `G4.3`; Inserimento e cancellazione; confronto con l'array `E6.2.2`; Liste doppie e circolari `E6.2.3`
- **Ripresa in un nuovo contesto:** Nodi e riferimenti; lista semplice `E6.2.1`
- **Approfondimenti facoltativi:** 1) Skip list `E6.7.2` · 2) Stack e heap; record di attivazione `G4.2`

### 4-10 · Prova di corte: modellare un sistema a oggetti

- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi
- **Approfondimenti facoltativi:** 1) Principi SOLID `H4.3` · 2) Progettare un gioco a oggetti: personaggi, oggetti, stanze `G3.2.15`

### 4-11 · Implementare un linguaggio: compilatore e interprete

- **Ripresa in un nuovo contesto:** Le fasi di un compilatore: panoramica `G7.1.1`
- **Approfondimenti facoltativi:** 1) Esplorare il bytecode di Python (modulo dis) `G7.1.6` · 2) Nascita di Internet (ARPANET, TCP/IP) e del Web (Berners-Lee, CERN, 1989–91) `U1.14`

### 4-12 · Analisi lessicale: i token

- **Nucleo:** Analisi lessicale: token e scanner `G7.1.2`
- **Prerequisiti integrati nel livello:** Applicazioni: analizzatori lessicali, protocolli, interfacce `F1.8`
- **Approfondimenti facoltativi:** 1) Come funziona l'evidenziazione della sintassi negli editor `G7.1.7` · 2) Suddividere in token un testo in italiano: parole, punteggiatura, apostrofi `G7.1.8`

### 4-13 · Grammatiche e sintassi (BNF)

- **Nucleo:** Grammatiche formali: terminali, non terminali, produzioni, derivazioni `F2.1`; Notazioni BNF ed EBNF; diagrammi sintattici `F2.2`; Alberi di derivazione; ambiguità `F2.3`
- **Approfondimenti facoltativi:** 1) Sintassi e semantica dei linguaggi di programmazione `F8.1` · 2) Grammatiche per generare frasi casuali `F2.10`

### 4-14 · Alberi sintattici e valutazione delle espressioni

- **Nucleo:** Alberi binari; visite in preordine, simmetrica, in postordine e per livelli `E6.4.2`; Alberi di espressioni e alberi sintattici `E6.4.8`; Grammatiche e linguaggi liberi dal contesto `F2.5`; Analisi sintattica discendente ricorsiva `G7.1.3`; Albero sintattico astratto (AST) `G7.1.5`; Heap e code con priorità `E6.4.5`
- **Ripresa in un nuovo contesto:** Alberi: terminologia e rappresentazione `E6.4.1`
- **Approfondimenti facoltativi:** 1) Alberi binari di ricerca: ricerca, inserimento, cancellazione `E6.4.3` · 2) Trie `E6.4.6`

### 4-15 · Un mini-interprete: la calcolatrice ★

- **Nucleo:** Interpreti: il ciclo di valutazione; scrivere un piccolo interprete `G7.3.1`
- **Approfondimenti facoltativi:** 1) Transpiler e compilazione verso il web `G7.3.4` · 2) Estendere la calcolatrice con variabili e funzioni `G7.3.6`

### 4-16 · Dato, informazione, archivio: dagli archivi ai database

- **Nucleo:** Ciclo di vita del dato: raccolta, archiviazione, elaborazione, conservazione, cancellazione `L1.2`; Qualità dei dati: accuratezza, completezza, coerenza, attualità `L1.3`
- **Ripresa in un nuovo contesto:** Dati strutturati, semi-strutturati, non strutturati `L1.1`; Archivi tradizionali e basi di dati; i problemi di ridondanza e incoerenza `L1.4`
- **Approfondimenti facoltativi:** 1) Biblioteche e archivi digitali `L13.1` · 2) Il ciclo di un progetto di analisi dei dati `L9.1`

### 4-17 · Modello E/R: entità, attributi, relazioni

- **Nucleo:** Livelli di astrazione: concettuale, logico, fisico `L3.1`; Entità e attributi; identificatori `L3.2`
- **Approfondimenti facoltativi:** 1) Strumenti per disegnare schemi E/R `L3.7` · 2) Governance dei dati: ruoli, responsabilità, politiche `L10.3`

### 4-18 · Cardinalità e vincoli

- **Nucleo:** Associazioni e cardinalità (1:1, 1:N, N:M) `L3.3`; Diagrammi Entità/Relazioni e loro notazioni `L3.4`; Dai requisiti al modello concettuale `L3.6`
- **Approfondimenti facoltativi:** 1) Generalizzazioni e gerarchie `L3.5` · 2) I modelli E/R all'interno del progetto software `H3.7`

### 4-19 · Modello relazionale: tabelle e chiavi

- **Nucleo:** La relazione come tabella: attributi, tuple, domini `L4.1`; Chiavi: superchiave, chiave candidata, primaria, esterna `L4.2`; Vincoli di integrità: di dominio, di entità, referenziale `L4.3`
- **Approfondimenti facoltativi:** 1) Architettura di un DBMS `L6.1` · 2) Codd e la nascita del modello relazionale `L4.10`

### 4-20 · Prova di corte: progettare uno schema E/R

- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi
- **Approfondimenti facoltativi:** 1) Errori tipici negli schemi E/R e come correggerli `L3.8` · 2) Confrontare schemi alternativi per lo stesso problema `L3.9`

### 4-21 · Dallo schema E/R allo schema relazionale

- **Nucleo:** Traduzione dal modello E/R al modello relazionale `L4.4`
- **Approfondimenti facoltativi:** 1) Generare lo schema con uno strumento di progettazione `L4.11` · 2) Schemi di database reali: negozio online, social network `L4.12`

### 4-22 · Normalizzazione (fino alla 3FN) ★

- **Nucleo:** Dipendenze funzionali `L4.6`; Normalizzazione: 1NF, 2NF, 3NF, BCNF `L4.7`
- **Approfondimenti facoltativi:** 1) Denormalizzazione consapevole `L4.8` · 2) Anomalie di inserimento, modifica, cancellazione in un foglio di calcolo reale `L4.13`

### 4-23 · Algebra relazionale: selezione, proiezione, join

- **Nucleo:** Algebra relazionale: selezione, proiezione, join, unione, differenza `L4.5`
- **Approfondimenti facoltativi:** 1) Calcolatori di algebra relazionale `L4.14` · 2) Tradurre domande in linguaggio naturale in algebra relazionale `L4.15`

### 4-24 · SQL: creare e modificare (DDL e DML)

- **Nucleo:** DDL: CREATE, ALTER, DROP; tipi di dato `L5.1`; DML: INSERT, UPDATE, DELETE `L5.2`; DBMS diffusi: SQLite, PostgreSQL, MySQL/MariaDB `L6.8`
- **Approfondimenti facoltativi:** 1) Controllo degli accessi: GRANT e REVOKE `L5.9` · 2) Trigger e procedure memorizzate `L5.11`

### 4-25 · SQL: SELECT, WHERE, ORDER BY

- **Nucleo:** SELECT con condizioni e ordinamento `L5.3`; Valori NULL e logica a tre valori `L5.7`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Logiche a più valori (a tre valori: il NULL di SQL) `A2.6.1`
- **Approfondimenti facoltativi:** 1) Ricerca testuale in SQL: LIKE ed espressioni regolari `L5.13` · 2) Logica fuzzy: gradi di verità `A2.6.2`

### 4-26 · SQL: JOIN

- **Nucleo:** Join interni ed esterni `L5.4`; Interrogazioni annidate `L5.6`
- **Approfondimenti facoltativi:** 1) I join rappresentati con i diagrammi di Venn, e i limiti di questa rappresentazione `L5.14` · 2) Self-join: una tabella collegata a se stessa (alberi genealogici) `L5.15`

### 4-27 · SQL: aggregazioni e GROUP BY

- **Nucleo:** Funzioni di aggregazione, GROUP BY, HAVING `L5.5`; Viste `L5.8`
- **Approfondimenti facoltativi:** 1) Mediana e percentili in SQL `L5.16` · 2) Riepiloghi in SQL e tabelle pivot a confronto `L5.17`

### 4-28 · Database e programmi: SQL da Python ★

- **Nucleo:** SQL dentro i programmi: connettori, query parametriche, ORM `L5.12`
- **Approfondimenti facoltativi:** 1) SQL injection e difese `L15.3` · 2) Salvare i progressi di un gioco in SQLite `L5.18`

### 4-29 · Privacy, GDPR, open data

- **Nucleo:** Open data: definizione, licenze, portali nazionali `L10.1`; Scala a cinque stelle degli open data `L10.2`; Protezione dei dati personali nel trattamento dei dati `L10.6`
- **Approfondimenti facoltativi:** 1) Anonimizzazione e pseudonimizzazione `L15.4` · 2) Altre norme UE sul digitale: DSA, DMA, Data Act, NIS2 `U4.9`

### 4-30 · Prova finale dell'anno: database più applicazione a oggetti

- **Nucleo:** integrazione dei livelli precedenti dell'anno, senza argomenti nuovi
- **Approfondimenti facoltativi:** 1) Quando le tabelle non bastano: panoramica dei database NoSQL `L7.8` · 2) Cruscotti costruiti sui dati di un database `L9.10`


## Anno 5 — Alfonso II

### 5-1 · Errori numerici e approssimazione

- **Nucleo:** Errore assoluto e relativo `A10.1.1`; Aritmetica in virgola mobile: epsilon di macchina, cancellazione numerica `A10.1.2`
- **Approfondimenti facoltativi:** 1) Incidenti causati da errori numerici (missile Patriot) `A10.1.4` · 2) Aritmetica esatta: frazioni e decimali a precisione arbitraria in Python `A10.1.5`

### 5-2 · Zeri di funzione: il metodo di bisezione

- **Nucleo:** Zeri di funzioni: bisezione e metodo di Newton `A10.2.1`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Limiti e comportamento asintotico `A6.1.3`; Continuità `A6.1.4`; Derivata come tasso di variazione `A6.2.1`
- **Approfondimenti facoltativi:** 1) Condizionamento di un problema e stabilità di un algoritmo `A10.1.3` · 2) Metodo delle secanti e regula falsi `A10.2.4`

### 5-3 · Il metodo di Newton ★

- **Nucleo:** Regole di derivazione; regola della catena `A6.2.2`
- **Approfondimenti facoltativi:** 1) Massimi e minimi `A6.2.3` · 2) Il metodo di Erone per la radice quadrata come caso del metodo di Newton `A10.2.5`

### 5-4 · Aree sotto una curva: rettangoli e trapezi

- **Nucleo:** Integrazione numerica (trapezi, Simpson) `A10.2.3`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Integrale come area e come accumulo `A6.3.1`
- **Approfondimenti facoltativi:** 1) Lunghezze di curve e volumi calcolati numericamente `A10.2.6` · 2) Integrare numericamente dati sperimentali (dalla velocità allo spazio) `A10.2.7`

### 5-5 · Stimare π con il metodo Monte Carlo

- **Nucleo:** Metodi Monte Carlo `S1.3`
- **Approfondimenti facoltativi:** 1) Modelli finanziari e simulazione del rischio `S8.2` · 2) L'ago di Buffon `S1.9`

### 5-6 · Successioni e ricorrenze: approssimare √2

- **Nucleo:** Progressioni aritmetiche e geometriche `A4.2.2`; Successioni e serie numeriche; convergenza `A6.1.5`
- **Ripresa in un nuovo contesto:** Successioni definite per ricorrenza (Fibonacci) `A4.2.1`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Sommatorie e produttorie (notazione Σ, Π); somme notevoli aritmetiche e geometriche `A1.5.5`
- **Approfondimenti facoltativi:** 1) Serie di Taylor e approssimazione polinomiale `A6.2.7` · 2) La successione di Fibonacci e il rapporto aureo `A4.2.5`

### 5-7 · Simulazione a tempo discreto: il moto (metodo di Eulero)

- **Nucleo:** Modelli dinamici elementari: crescita e decadimento `A6.4.1`; Soluzione numerica (metodi di Eulero e di Runge-Kutta) `A6.4.4`; Simulazioni a tempo discreto e a eventi discreti `S1.2`; Simulare sistemi dinamici con equazioni differenziali `S1.4`
- **Approfondimenti facoltativi:** 1) Il moto del proiettile con la resistenza dell'aria `S1.10` · 2) Visualizzare traiettorie e risultati di una simulazione `S1.11`

### 5-8 · Oscillatori e attrito

- **Nucleo:** Equazioni differenziali ordinarie lineari di 1° e 2° ordine; oscillatori `A6.4.2`; Simulare sistemi fisici: moto, gravitazione, problema degli N corpi `S5.1`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Teorema fondamentale del calcolo; tecniche di integrazione `A6.3.2`
- **Approfondimenti facoltativi:** 1) Il pendolo: piccole e grandi oscillazioni `S5.5` · 2) La risonanza: dall'altalena ai ponti `S5.6`

### 5-9 · Modelli di popolazione e di epidemia

- **Nucleo:** Sistemi complessi: emergenza e non linearità `S14.1`; Modelli epidemici (SIR) `S14.4`; Modelli ad agenti `S1.5`
- **Approfondimenti facoltativi:** 1) Caos deterministico (mappa logistica) `S14.2` · 2) Frattali e dimensione frattale `S14.5`

### 5-10 · Prova di corte: simulazione di un fenomeno e confronto con le fonti

- **Nucleo:** Validazione dei modelli, incertezza, analisi di sensibilità `S1.6`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Variabili continue: uniforme, esponenziale, normale `A7.3.3`; Legge dei grandi numeri e teorema del limite centrale `A7.3.4`; Stimatori e intervalli di confidenza `A7.4.1`
- **Approfondimenti facoltativi:** 1) Test di ipotesi e p-value `A7.4.2` · 2) Ricampionamento: bootstrap e validazione incrociata `A7.4.6`

### 5-11 · Confrontare un modello con i dati: minimi quadrati; apprendimento supervisionato ★

- **Nucleo:** Regressione lineare `O4.1.4`
- **Ripresa in un nuovo contesto:** Correlazione e regressione lineare semplice `A7.1.5`
- **Prerequisiti integrati nel livello:** Imparare dai dati: esempi, caratteristiche, etichette `O4.1.1`; Classificazione e regressione `O4.1.2`
- **Approfondimenti facoltativi:** 1) Alberi di decisione `O4.1.6` · 2) Adattare curve non lineari ai dati (esponenziali, potenze) `S1.12`

### 5-12 · Automi a stati finiti

- **Nucleo:** Automi non deterministici (NFA) ed equivalenza con i DFA `F1.2`; Trasduttori (automi con uscita) `F1.9`
- **Approfondimenti facoltativi:** 1) Teorema di Kleene: equivalenza fra espressioni regolari e automi `F1.4` · 2) Automi a pila ed equivalenza con le grammatiche libere `F2.6`

### 5-13 · La macchina di Turing

- **Nucleo:** Macchina di Turing: nastro, testina, stati; esempi `F3.1`; Varianti (più nastri, non determinismo) e loro equivalenza `F3.2`; La macchina di Turing universale `F3.3`; Tesi di Church-Turing `F3.5`
- **Approfondimenti facoltativi:** 1) Turing-completezza di linguaggi e sistemi (anche giochi e automi cellulari) `F3.6` · 2) Complessità di Kolmogorov di una stringa `F10.1`

### 5-14 · Calcolabilità: il problema della fermata

- **Nucleo:** Funzioni calcolabili e non calcolabili; argomento di cardinalità `F4.1`; Il problema della fermata e la sua indecidibilità `F4.2`; Conseguenze pratiche: i limiti dell'analisi automatica dei programmi `F4.7`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Conseguenza logica; regole di inferenza (modus ponens, modus tollens); deduzione naturale `A2.1.7`; Che cos'è una dimostrazione: ipotesi, tesi, controesempio `A2.3.1`; Dimostrazione per assurdo `A2.3.3`; Funzioni iniettive, suriettive, biiettive; funzione inversa `A3.3.2`; Cardinalità finita; corrispondenza biunivoca `A3.4.1`; Insiemi infiniti numerabili `A3.4.2`; Diagonalizzazione di Cantor; insiemi non numerabili `A3.4.3`
- **Approfondimenti facoltativi:** 1) Linguaggi decidibili, semidecidibili, non semidecidibili `F4.3` · 2) Dimostrazione diretta e per contrapposizione `A2.3.2`

### 5-15 · Complessità: P e NP in modo intuitivo

- **Nucleo:** Notazioni asintotiche O, Ω, Θ `E9.3`; Problemi trattabili e intrattabili (panoramica intuitiva) `E9.9`; Il problema P vs NP e le sue conseguenze `F5.5`
- **Approfondimenti facoltativi:** 1) Caso migliore, peggiore e medio `E9.4` · 2) Classi di complessità temporale; la classe P `F5.1`

### 5-16 · Reti: tipi, topologie, commutazione

- **Nucleo:** Banda, velocità di trasmissione, latenza `J1.2`; Simplex, half-duplex, full-duplex; trasmissione sincrona e asincrona `J1.6`; Topologie fisiche e logiche: bus, stella, anello, maglia `J2.3`; Architetture client-server e peer-to-peer `J2.5`; Dispositivi di rete: scheda di rete, hub, switch, router, access point, modem `J2.6`; Liste di adiacenza `E6.6.2`; Visita in ampiezza (BFS); cammini minimi non pesati `E7.3.1`
- **Ripresa in un nuovo contesto:** Sistema di comunicazione: sorgente, trasmettitore, canale, ricevitore `J1.1`
- **Approfondimenti facoltativi:** 1) Visita in profondità (DFS); componenti connesse `E7.3.2` · 2) Analisi delle reti sociali: centralità e comunità `S9.1`

### 5-17 · Modelli a strati: ISO/OSI e TCP/IP

- **Nucleo:** Analizzare il traffico con Wireshark `J3.5`
- **Ripresa in un nuovo contesto:** Il modello ISO/OSI `J3.2`; La pila TCP/IP e il confronto con OSI `J3.3`; Incapsulamento: intestazioni e unità di dati (trama, pacchetto, segmento) `J3.4`
- **Approfondimenti facoltativi:** 1) I socket come interfaccia verso il trasporto `J6.7` · 2) Protocolli di comunicazione prima di Internet: telegrafo, telefono, X.25 `J3.6`

### 5-18 · Livello fisico e di collegamento: Ethernet, Wi-Fi, errori

- **Nucleo:** Livello fisico: cablaggio strutturato, connettori, categorie di cavi `J4.1`; Livello di collegamento: trame e indirizzi MAC `J4.2`; Controllo degli errori sul collegamento (CRC) `J4.3`; Accesso al mezzo: CSMA/CD e CSMA/CA `J4.4`; Ethernet: evoluzione e velocità `J4.5`; Lo switch: tabella MAC, apprendimento, domini di collisione e di broadcast `J4.6`; Wi-Fi (IEEE 802.11): standard, canali, SSID `J4.9`; Errori di trasmissione e di memorizzazione; il rumore `B10.1.1`; Bit di parità (pari e dispari) `B10.1.2`; Checksum e cifre di controllo `B10.1.4`
- **Prerequisiti integrati nel livello:** CRC come divisione polinomiale con XOR `B10.2.1`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Polinomi; equazioni di secondo grado `A1.5.4`; Onde elettromagnetiche: frequenza, lunghezza d'onda, spettro `C14.1`; Cavi in rame (doppino, coassiale); attenuazione e disturbi `C14.2`; Radio: antenne, propagazione, bande libere e soggette a licenza `C14.4`
- **Approfondimenti facoltativi:** 1) Bluetooth, Zigbee e reti personali `J4.10` · 2) Fibra ottica: riflessione totale, fibre monomodali e multimodali `C14.3`

### 5-19 · Indirizzi IP e subnetting

- **Nucleo:** Maschere di sottorete e CIDR; calcolo delle sottoreti `J5.2`; Indirizzi privati e pubblici; NAT `J5.3`; ICMP: ping e traceroute `J5.6`; IPv6: indirizzamento, autoconfigurazione, transizione `J5.7`
- **Approfondimenti facoltativi:** 1) Frammentazione e MTU `J5.8` · 2) IPv6 in pratica: gli indirizzi della propria rete `J5.10`

### 5-20 · Prova di corte: progettare la rete di un edificio (componenti, configurazione, prestazioni)

- **Nucleo:** Instradamento: tabelle di routing, gateway predefinito `J5.4`; Configurare una rete in un simulatore (Packet Tracer) `J5.9`
- **Approfondimenti facoltativi:** 1) VLAN `J4.7` · 2) Protocollo ARP `J4.11`

### 5-21 · Instradamento e grafi: l'algoritmo di Dijkstra

- **Nucleo:** Algoritmo di Dijkstra `E7.3.4`; Protocolli di instradamento: distance vector (RIP) e link state (OSPF) `J5.5`
- **Prerequisiti integrati nel livello:** Bellman-Ford e Floyd-Warshall `E7.3.5`
- **Approfondimenti facoltativi:** 1) Ricerca informata A* ed euristiche ammissibili `E7.3.9` · 2) Sistemi autonomi e BGP `J8.2`

### 5-22 · TCP, UDP e porte

- **Nucleo:** TCP: connessione (three-way handshake), affidabilità, numeri di sequenza `J6.3`; Controllo di flusso: la finestra scorrevole `J6.4`; Controllo della congestione `J6.5`
- **Prerequisiti integrati nel livello:** Rilevare o correggere: la ritrasmissione `B10.1.5`
- **Approfondimenti facoltativi:** 1) QUIC e protocolli di trasporto recenti `J6.6` · 2) Qualità del servizio (QoS) `J11.5`

### 5-23 · Servizi di rete: DNS, HTTP, posta elettronica

- **Nucleo:** DHCP `J7.2`; HTTP: richieste e risposte, metodi, codici di stato, intestazioni `J7.3`; Posta elettronica: SMTP, IMAP, POP3 `J7.5`
- **Approfondimenti facoltativi:** 1) Proxy e proxy inversi `J11.6` · 2) Reti per la distribuzione di contenuti (CDN) `J12.2`

### 5-24 · Sicurezza in rete: crittografia asimmetrica e HTTPS

- **Nucleo:** L'idea della crittografia a chiave pubblica `N3.3.1`; Scambio di chiavi Diffie-Hellman `N3.3.2`; RSA `N3.3.3`; Firma digitale `N3.4.1`; Certificati X.509 e autorità di certificazione `N3.4.2`; HTTPS e TLS: visione d'insieme `J7.4`; TLS: handshake, negoziazione, certificati `N4.1`
- **Prerequisiti integrati nel livello:** Cifrari a blocchi e a flusso `N3.1.1`; DES e AES `N3.1.2`; Funzioni hash crittografiche e loro proprietà `N3.2.1`; Cifratura ibrida `N3.3.5`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Identità di Bézout, algoritmo di Euclide esteso `A1.3.5`; Operazioni modulo n, inverso moltiplicativo `A1.4.2`; Piccolo teorema di Fermat; funzione φ e teorema di Eulero `A1.4.4`
- **Approfondimenti facoltativi:** 1) Codici di autenticazione dei messaggi (HMAC) `N3.2.3` · 2) Memorizzare le password: sale e funzioni lente (bcrypt, Argon2) `N3.2.4`

### 5-25 · Prestazioni: banda, latenza, throughput; mantenere l'efficienza

- **Nucleo:** Metriche: latenza, throughput, utilizzo `I12.1`; Benchmarking e profilazione `I12.2`; Misurare la connessione: velocità, latenza, jitter `J8.5`; Installare e aggiornare il sistema `I11.2`
- **Approfondimenti facoltativi:** 1) Colli di bottiglia; legge di Little `I12.3` · 2) Misurare la propria connessione e il proprio computer: strumenti di benchmark `I12.8`

### 5-26 · Intelligenza artificiale: imparare dai dati ★

- **Nucleo:** k vicini più prossimi `O4.1.3`; Insiemi di addestramento, di validazione e di test `O4.3.1`; Metriche: accuratezza, precisione, richiamo, F1, matrice di confusione `O4.3.3`; Clustering: k-means `O4.2.1`
- **Ripresa in un nuovo contesto:** Imparare dai dati: esempi, caratteristiche, etichette `O4.1.1`; Classificazione e regressione `O4.1.2`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Vettori nel piano e nello spazio; componenti `A5.1.1`; Somma di vettori e prodotto per uno scalare `A5.1.2`; Prodotto scalare, norma, distanza, similarità del coseno `A5.1.3`
- **Approfondimenti facoltativi:** 1) Clustering gerarchico e basato sulla densità `O4.2.2` · 2) Rilevamento di anomalie `O4.2.5`

### 5-27 · Reti neurali in modo intuitivo ★

- **Nucleo:** Neurone artificiale e percettrone `O5.1.1`; Funzioni di attivazione `O5.1.2`; Reti multistrato; approssimazione universale `O5.1.3`
- **Prerequisiti di altre discipline, costruiti nel gioco:** Matrici e operazioni elementari; un'immagine come matrice `A5.1.5`; Prodotto matriciale `A5.1.6`
- **Approfondimenti facoltativi:** 1) Embedding: parole e oggetti come vettori `O5.4.1` · 2) Sperimentare con una rete neurale nel browser (TensorFlow Playground) `O5.6`

### 5-28 · IA generativa: limiti, etica, AI Act ★

- **Nucleo:** Modello linguistico: prevedere il token successivo `O6.1`; Rischi e benefici dell'IA per la società `O10.1`; Trasparenza e responsabilità dei sistemi di IA `O10.3`; Bias algoritmico e discriminazione `U3.2`; Principi e linee guida per un'IA etica (UE, UNESCO, OCSE) `U3.6`; Regolamento europeo sull'IA (AI Act): livelli di rischio e obblighi `U4.8`
- **Prerequisiti integrati nel livello:** Trasparenza, spiegabilità, diritto alla spiegazione `U3.3`; Responsabilità: chi risponde degli errori di un sistema automatico `U3.4`
- **Approfondimenti facoltativi:** 1) IA, lavoro, creatività, diritto d'autore `O10.5` · 2) Bias nei dati ed equità dei modelli `O4.3.6`

### 5-29 · L'informatica e il metodo scientifico: la nascita di nuove scienze

- **Nucleo:** Che cos'è l'informazione: prospettive filosofiche `U2.1`; Epistemologia della simulazione e dei dati `U2.6`
- **Approfondimenti facoltativi:** 1) Filosofia della tecnologia; l'infosfera (Floridi) `U2.7` · 2) Scienze nate con il calcolatore: bioinformatica, climatologia computazionale, scienze sociali computazionali `U2.9`

### 5-30 · Prova finale dell'anno: un progetto di simulazione scientifica completo

- **Nucleo:** Software scientifico riproducibile `S1.7`
- **Approfondimenti facoltativi:** 1) Pubblicare i risultati di una simulazione: notebook e dati aperti `S1.13` · 2) Reti complesse: piccolo mondo, invarianza di scala, dinamiche sulle reti `S14.3`

## 6. Decisioni prese e questioni aperte

**Decisioni (Pietro, 27/09/2026)**
1. **Livello 1-27:** la quantità d'informazione si presenta in forma intuitiva (domande sì/no, dimezzamenti). Logaritmo e probabilità si costruiscono allo stesso livello di intuizione.
2. **Livello 2-28:** resta denso, con gli strati di rete anticipati. Nella scala di difficoltà interna conviene dividerlo in più tappe.
3. **Prerequisiti non informatici:** il gioco li (ri)costruisce tutti e non presuppone l'allineamento con le altre materie (§2).

**Questioni aperte**
1. **Carico dei livelli di matematica del quinto anno.** Costruire nel gioco limiti, derivate, integrali ed equazioni differenziali (5-2…5-9) richiede sottolivelli dedicati. Vanno progettati "al minimo necessario" per il metodo numerico di ogni livello.
2. **Prove di corte senza argomenti nuovi.** 1-30, 2-10, 2-20, 2-30, 3-10, 3-20, 3-30, 4-10, 4-20, 4-30 integrano i livelli precedenti. Le prove 1-10, 1-20, 5-10, 5-20 e 5-30 contengono invece anche un argomento nuovo, già presente nel curricolo v0.1.
3. **Granularità disomogenea.** Alcuni livelli hanno un solo nodo di nucleo, altri molti, anche per via dei prerequisiti costruiti (es. 1-2, 1-27, 5-2). La durata va stimata in fase di prototipo e i livelli più densi vanno articolati nella loro scala interna.
4. **Nuove Indicazioni nazionali 2026.** Valgono le avvertenze del curricolo v0.1: acquisita la sezione di Informatica, si rifà la verifica di copertura e si rieseguono gli script.

## 7. Registro modifiche

- **v1.1 (27/09/2026)**: recepite le decisioni di Pietro (§6). Nessuna competenza in ingresso presupposta: 87 prerequisiti di altre discipline costruiti nel gioco (i 66 richiami della v1.0 più le 21 competenze prima date per acquisite; luce e suono, B5.1.1 e B7.1, sono contati fra le altre discipline). Aggiunte le note didattiche per 1-27 e 2-28. Approfondimenti di 1-12 e 1-27 riassegnati (B5.3.2; B5.2.4) perché restino accessibili. Verifica: 0 prerequisiti mancanti, 0 violazioni.

- **v1.0 (27/09/2026)**: prima versione dello schema. Argomenti ripresi dal curricolo v0.1 senza gli agganci storico-culturali; propedeuticità verificate sulla mappa; 300 approfondimenti non propedeutici; spostamenti e anticipazioni documentati al §4.
