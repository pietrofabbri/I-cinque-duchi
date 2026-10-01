---
titolo: Videogioco "I cinque duchi" — Come si gioca: interazione, strumenti veri, carte dei personaggi, memoria, contesto
versione: 0.5
data: 2026-10-02
autore: Pietro Fabbri (con Claude)
documenti collegati: videogioco-5-duchi-esercizi.md (v0.1), videogioco-5-duchi-quadro-trasversale.md (v0.1), videogioco-5-duchi-tappa-1-01.md (v0.3), videogioco-5-duchi-anno1-mappa.md (v0.9), videogioco-5-duchi-meccaniche.md (v0.3), videogioco-5-duchi-schema-livelli.md (v1.1), videogioco-5-duchi-anno1-ferrara.md (v0.3)
---

# Come si gioca

> **Novità della v0.3 (30/09/2026).** **Borso è il personaggio giocante**: si muove, parla, agisce. I personaggi parlano solo di sé e della propria epoca. Ogni tappa ha una **zona percorribile** in stile Pokémon (§3.5). Esercizi, pool e quantità di testo sono in `videogioco-5-duchi-esercizi.md`; i collegamenti con Diritto, Etica, Filosofia, Psicologia e Arti sono in `videogioco-5-duchi-quadro-trasversale.md`.

## 0. Requisiti di Pietro (28/09/2026)

1. **Interazione leggera e credibile.**
2. **Strumenti veri.** Gli studenti programmano, usano fogli di calcolo, fanno simulazioni: non roba finta, ma competenze che potranno spendere fuori dal gioco.
3. **Personaggi riconoscibili.** Hanno le sembianze di dipinti o foto che li rappresentano, ma sempre in modo simbolico, portabile, veloce e leggibile, senza pretese grafiche ("tipo Pokémon?").
4. **Apprendimento graduale, divertente e che lascia il segno**, usando i principi della memoria (mnemotecniche, curva dell'oblio di Ebbinghaus…).
5. **Una sola strada**, non cronologica, ma con tutte le informazioni per contestualizzare.
6. **Una sola modalità.** Si gioca sempre anche a casa; in classe solo occasionalmente.

---

## 1. Il ciclo di una tappa

```text
MAPPA ──▶ INCONTRO ──▶ RIPASSO ──▶ BOTTEGA ──▶ SOGLIA ──▶ CARTA ──▶ RIMANDO ──▶ tappa successiva
          (personaggio,  (2-4 domande  (esercizi      (k istanze   (si aggiunge     (battuta del
           contesto)     su tappe       con strumenti  coerenti)    alla collezione)  personaggio)
                         precedenti)    veri)
                                                                                 └── visioni di Borso A1 → A2
                                                                                     (facoltative, consecutive,
                                                                                      nessun punto in più sulla mappa)
```

Durata tipica di una sessione: **10–20 minuti**. Una tappa richiede da una a più sessioni.

---

## 2. Input e strumenti veri

### 2.1 Principio

**Ogni esercizio si svolge in uno strumento vero, o in una sua parte fedele, e ogni prodotto si può esportare e riaprire con lo strumento standard.**

Una formula scritta nel gioco è una formula vera, che funziona anche in LibreOffice, Excel o Google Fogli. Un programma scritto nel gioco è Python vero, che gira identico in Thonny o IDLE.

### 2.2 Modi di input

| Input | Dove | Esempi |
|---|---|---|
| **Mouse o tocco** | Mappa, incontri, manipolazioni | Accendere bit, spostare pesi sulla bilancia, collegare porte logiche, ordinare carte sulla linea del tempo |
| **Tastiera** | Formule, codice, comandi | Scrivere una formula, un comando di shell, una riga di Python |
| **File veri** | Esercizi fatti con applicazioni esterne | Lo studente lavora in LibreOffice, Word, Excel o Google Fogli, scarica il file e lo carica nel gioco. Il gioco lo apre (i formati .docx, .odt, .xlsx e .ods sono archivi di XML) e controlla i requisiti sui **dati personalizzati** di quello studente |

**Dispositivi.** La mappa, gli incontri, le carte e i ripassi funzionano anche sul telefono. Gli esercizi con tastiera richiedono un computer o un Chromebook.

### 2.3 Strumenti per l'anno 1 (e oltre)

| Strumento nel gioco | Tecnologia (libera, gira nel browser, senza server) | Livelli | Che cosa resta allo studente |
|---|---|---|---|
| **Console Python** usata come "calcolatrice dell'informatico" | Pyodide (il vero CPython compilato per il browser) | 1-3…1-11: `bin()`, `hex()`, `int(x, 2)`, `ord()`, `chr()`, `.encode('utf-8')`; poi tutto l'anno 2 | Python vero, dal primo mese |
| **Manipolatori** (bit, bilancia, tabelle di codifica, rigo musicale) | Componenti del gioco | 1-2…1-11 | Intuizione, verificata subito con la console Python |
| **Selettore di colori e editor di pixel** | Componenti del gioco con esportazione in PNG | 1-12, 1-13 | Codici `#RRGGBB` veri; immagini che si aprono in qualsiasi programma di grafica |
| **Simulatore di CPU didattica** | Componente del gioco (macchina a registri minima) | 1-14…1-20 | Il modello concettuale |
| **Il tuo computer, dati veri** | Lettura di informazioni reali del dispositivo (numero di core, memoria indicativa, sistema operativo) | 1-14, 1-20, 1-21 | Collegamento fra teoria e macchina reale |
| **Terminale Linux vero** | v86 (emulatore libero che esegue un vero Linux minimo nel browser) | 1-21…1-24: `ls`, `cd`, `mkdir`, `cp`, `chmod`, `ps`, backup di cartelle | Comandi di shell veri, gli stessi di un server |
| **Documenti** | Esercizi da svolgere in LibreOffice, Word o Google Documenti, con caricamento del file | 1-25 | Uso corretto degli stili, dei titoli, dell'indice: competenze da ufficio vere |
| **Foglio di calcolo** | Foglio nel gioco con formule compatibili con Excel e LibreOffice, più import ed esportazione in .xlsx e .ods; oppure file caricato | 1-26, 1-27 | Formule e grafici veri. Il gioco **controlla che ci siano le formule** e non solo i valori: anche questo misura il processo |
| **Strumenti di rete** | Interrogazioni DNS reali dal browser; analisi di URL veri | 1-28 | Come funziona davvero un indirizzo |
| **Ricerca e verifica delle fonti** | Motore di ricerca vero, fuori dal gioco; il gioco raccoglie le fonti trovate e le fa classificare | 1-29 | Metodo di verifica |
| Anni successivi | Python con matplotlib (simulazioni, grafici), SQLite vero (sql.js), editor HTML/CSS/JS con anteprima, simulatore di circuiti | Anni 2–5 | Programmi, database e siti che funzionano fuori dal gioco |

**Peso.** Pyodide e v86 si scaricano la prima volta (decine di MB) e poi restano in cache nel browser. Il gioco funziona anche offline.

### 2.4 Gradualità dentro ogni tappa

Ogni argomento segue una **scala a cinque gradini**, dal molto facile al raffinato:

1. **Esempio svolto**, mostrato dal personaggio.
2. **Esempio da completare**: manca un solo passaggio.
3. **Esercizio guidato**, con suggerimenti disponibili.
4. **Esercizio autonomo** su un'istanza nuova.
5. **Trasferimento**: lo stesso concetto in un contesto diverso, per esempio dalla bilancia alla console Python.

La soglia per proseguire sta al gradino 4. Il gradino 5 e i gradi superiori sono negli approfondimenti.

**Obiettivo di tasso di successo: circa 80–85%.** La difficoltà si adatta: dopo due errori sullo stesso gradino si torna al gradino precedente con un'istanza nuova.

---

## 3. Le carte dei personaggi

### 3.1 Formato: le carte da collezione

Ogni personaggio incontrato diventa una **carta**, nello spirito delle carte da collezione (Pokémon, figurine), ma sobria.

**Fronte**

```text
┌──────────────────────────┐
│  [ritratto 48×48 pixel]  │   ← ritratto simbolico, 16 colori
│  GUIDO MONACO     XI sec │
│  ▓▓▓ epoca E2  · luogo 4 │   ← fascia colorata dell'epoca, numero della tappa
│  Etichetta: D            │   ← documentato / interpretato / memoria / leggenda…
│  ♪ "La nota vale per     │
│    dove sta"             │   ← motto mnemonico (§4.3)
│  CONCETTO: notazione     │
│  posizionale             │
└──────────────────────────┘
```

**Retro**

- tre fatti essenziali;
- la domanda critica;
- la posizione sulla linea del tempo;
- il livello di padronanza della carta: bronzo, argento, oro (§4.2).

### 3.2 I ritratti

- **Fonte.** Dipinti, miniature, medaglie o foto **in pubblico dominio o con licenza libera**. La ricerca strutturata delle immagini è rinviata, come chiesto da Pietro.
- **Stile.** Ogni ritratto viene ridotto a **48×54 pixel con 16 colori**, con uno script automatico (ridimensionamento e media k-means dei colori). Primo esempio: Borso, dal ritratto di profilo del 1469-71. Il risultato è riconoscibile ma simbolico; ogni file pesa pochi kB e lo stile è uniforme per tutti.
- **Aggancio didattico.** La riduzione di un'immagine a pochi pixel e pochi colori è proprio l'argomento dei livelli 1-12 e 1-13. Un approfondimento può chiedere allo studente di **creare lui stesso** la carta di un personaggio facoltativo.
- **Personaggi senza immagine libera** (per esempio le figure del Novecento con foto protette, le persone viventi o i gruppi): un **emblema simbolico** al posto del volto, come una macchina da presa per Antonioni, una chitarra per Brondi o un pallone per Mazza.
- **Personaggi collettivi** (mercanti, comunità): un emblema, mai un volto inventato.

### 3.3 La scena dell'incontro

La scena richiama un incontro nei giochi di ruolo classici:

- il ritratto del personaggio da un lato;
- il luogo sullo sfondo (una semplice sagoma del monumento);
- un riquadro di dialogo in basso.

La "sfida" non è un combattimento: è l'esercizio in bottega.

---

### 3.4 Le visioni di Borso (personaggi e approfondimenti facoltativi)

Decisione di Pietro del 28/09/2026. Molte tappe sono vicinissime (per esempio la piazza della Cattedrale e il Quadrivio degli Angeli), quindi i contenuti facoltativi non diventano nuovi punti sulla mappa.

- **Che cosa sono.** Dopo che il giocatore ha finito con il personaggio obbligatorio, **Borso immagina** una scena nello stesso luogo: un personaggio facoltativo e l'approfondimento informatico collegato. Per esempio, alla Casa di Ariosto Borso immagina Boiardo che rivede il suo poema, e da lì nasce l'approfondimento sulla revisione collaborativa dei documenti.
- **Ordine.** Le visioni sono **consecutive**: la A1 si apre dopo il personaggio obbligatorio, la A2 dopo la A1.
- **Nessun effetto sul percorso.** Le visioni non aprono tappe e non danno nulla che serva più avanti; la tappa successiva si apre con il rimando. Restano disponibili anche dopo, per chi vuole tornarci.
- **Grafica.** La scena della visione ha un tono diverso (per esempio seppia e bordi sfumati), così il giocatore capisce subito che si tratta di un'evocazione di Borso e non di un incontro sulla strada.
- **Collezione.** Anche i personaggi delle visioni diventano carte, con un contrassegno "visione".

### 3.5 Borso giocante e zone percorribili (v0.3)

Decisione di Pietro del 30/09/2026.

- **Borso è chi gioca.** Il giocatore è Borso d'Este: si muove nella città, parla con i personaggi, immagina le visioni. Non è più un narratore da incontrare all'ultima tappa.
- **I personaggi parlano di sé.** Ognuno racconta la propria vita e la propria epoca, in prima persona. Non commentano Borso e non parlano di lui.
- **Zona percorribile.** Il pulsante «Entra» apre una piccola mappa a tessere, in stile Pokémon, con il personaggio obbligatorio, le due visioni facoltative e alcune **chicche** (oggetti da guardare, mai valutati).
- **Confini.** La zona è la cella di Voronoi della tappa entro 150 m: non si sovrappone alle zone vicine. Si esce da un cancello che si apre solo dopo la soglia.
- **Comandi.** Frecce o WASD, pulsanti a croce sullo schermo del telefono; A o spazio per parlare.
- **Grafica (v0.4).** Vista dall'alto in 3/4, stile GBA, con la geometria reale degli edifici (open data del Comune): tessere da 16 px pari a 1,25 m, figure 16 × 24 px, ritratti 48 × 54 px nei dialoghi. Movimento continuo e fluido. Le visioni restano in seppia. Dettagli: `videogioco-5-duchi-motore-e-grafica.md`.
- **Esempio completo:** tappa 1-1 (`videogioco-5-duchi-tappa-1-01.md` §3).

### 3.6 Pausa di autoregolazione

Dopo due errori consecutivi il gioco non punisce: mostra un cerchio che respira per 4 secondi e chiede «Che cosa provi adesso?». Poi si riparte, un gradino più in basso. È l'aggancio dell'anno 1 a «emozioni e autoregolazione» (quadro trasversale), fatto con un gesto e non con una lezione.

## 4. Memoria: far durare ciò che si impara

Principi usati, con le relative fonti, e come si traducono nel gioco.

| Principio | Riferimento | Traduzione nel gioco |
|---|---|---|
| **Curva dell'oblio**: si dimentica molto nei primi giorni, meno se si ripassa | Ebbinghaus (1885) | Ripassi programmati (§4.2) |
| **Ripetizione dilazionata**: ripassi distanziati sono più efficaci di ripassi concentrati | Cepeda et al. (2006); Dunlosky et al. (2013) | Intervalli crescenti di 1, 3, 7, 14 e 30 giorni, calcolati sulle date salvate nel codice di ripresa |
| **Effetto test**: richiamare dalla memoria consolida più che rileggere | Roediger e Karpicke (2006) | I ripassi sono domande da risolvere, non schede da rileggere |
| **Alternanza** di argomenti diversi | Dunlosky et al. (2013) | I ripassi mescolano tappe diverse |
| **Metodo dei loci**: associare contenuti a luoghi in un percorso | Tradizione retorica antica (Simonide, Cicerone) | **La mappa è un palazzo della memoria**: ogni concetto ha un luogo e il percorso è sempre lo stesso. Esercizio ricorrente: "ripercorri la strada" |
| **Doppia codifica**: parola + immagine | Paivio (1971) | Carta con ritratto, luogo e concetto |
| **Effetto generazione**: si ricorda meglio ciò che si produce | Slamecka e Graf (1978) | Lo studente costruisce: numeri, formule, programmi, carte |
| **Carico cognitivo**: poche cose nuove alla volta, esempi svolti poi sfumati | Sweller (1988) | Scala a cinque gradini (§2.4) |
| **Difficoltà desiderabili** | Bjork (1994) | Istanze sempre nuove, richiamo senza aiuti prima del suggerimento |
| **Autospiegazione** | Chi et al. (1989) | Dopo alcuni esercizi, domanda "perché?" a risposta chiusa: la spiegazione giusta fra tre plausibili |
| **Emozione e narrazione** | Ricerca sul ricordo di episodi e storie | Ogni concetto è legato a una storia e a un personaggio (l'aggancio) |

**Da evitare:** gli "stili di apprendimento" (visivo, uditivo…), che non hanno sostegno sperimentale.

### 4.2 Ripasso integrato nella strada (senza obiettivi paralleli)

- **All'inizio di ogni tappa** il personaggio pone **2–4 domande di ripasso** sulle carte "in scadenza", cioè le tappe precedenti il cui intervallo è trascorso.
- **Il ripasso fa parte della soglia.** Non è una missione a parte, quindi la strada resta unica.
- **Sistema di Leitner.** Ogni carta sale di livello (bronzo → argento → oro) quando il ripasso riesce e scende quando fallisce. Una carta d'oro torna in ripasso dopo 30 giorni.
- **Lunghe pause.** Se lo studente non gioca per giorni, alla ripresa trova più carte in scadenza, ma **al massimo 6 per sessione**, per non scoraggiarlo.
- **Nel report del docente** compare la **tenuta nel tempo**: la percentuale di ripassi riusciti a 7 e a 30 giorni. È la misura più onesta di ciò che resta.

### 4.3 Mnemotecniche

- **Un motto per carta**, breve e ritmato. Esempi da scrivere per ogni tappa:
  - «La nota vale per dove sta» (1-4, posizionale);
  - «Otto bit, un byte: come otto torri per un castello» (1-7).
- **Acronimi** dove servono, per esempio la triade di sicurezza RID: Riservatezza, Integrità, Disponibilità.
- **Parole chiave e immagini** per i termini difficili.
- **Ripercorri la strada.** Ogni 10 tappe, durante la prova di corte, lo studente ricostruisce la sequenza di luoghi, personaggi e concetti: è il metodo dei loci applicato.

### 4.4 Divertimento

- **Curiosità.** Il rimando è un piccolo gancio narrativo verso la tappa successiva.
- **Collezione.** 30 carte obbligatorie più quelle facoltative; padronanza bronzo, argento e oro.
- **Progresso visibile.** La mappa si schiarisce.
- **Umorismo nei dialoghi.** I personaggi hanno una voce riconoscibile: Salinguerra sanguigno, Chiozzi misterioso, Ariosto ironico.
- **Sessioni brevi**, e nessuna punizione per le pause, solo più ripassi.

---

## 5. Contesto: una strada non cronologica ma comprensibile

La strada segue la geografia, non il tempo. Perché chi gioca sappia sempre dove si trova nella storia, ogni incontro si apre con una **scheda di contesto**:

1. **Linea del tempo**, dal VII secolo a oggi. Mostra la posizione del personaggio e le carte già raccolte, colorate per epoca (E1–E8).
2. **Tre righe**: *dove siamo*, *quando*, *che cosa succede intorno*.
3. **Chi c'era prima e chi dopo**: i due personaggi già incontrati più vicini nel tempo.
4. **Etichetta epistemologica** (D, I, M, L, F, C) con una frase che la spiega.

**Taccuino di Borso.** Una cronologia personale si riempie da sola a ogni incontro e il giocatore può riordinarla. Nella **prova finale (1-30)** lo studente ordina tutte le 30 carte nel tempo e ricostruisce la storia della città a partire da incontri avvenuti in ordine geografico. È un esercizio di richiamo e di elaborazione insieme.

---

## 6. Una sola modalità di gioco

Si gioca **sempre**, anche a casa. **In classe** si gioca occasionalmente, con gli stessi contenuti e le stesse regole. Le misure contro copie e aiuti esterni sono descritte in `videogioco-5-duchi-meccaniche.md` §2.

---

## 7. Questioni aperte

1. Scrivere motti e dialoghi delle 30 tappe (il tono di voce di ogni personaggio), rispettando i limiti di testo dell'anno (`esercizi.md` §3).
5. Confermare la tappa 1-30: con Borso giocante, la proposta è **P93 La città** (vedi `anno1-mappa.md`).
2. Ricerca strutturata dei ritratti, quando Pietro darà il via: fonti, licenze, scelta dell'immagine.
3. Verificare che v86 e Pyodide funzionino sui computer del laboratorio e sui Chromebook.
4. Decidere se per 1-25 e 1-26 usare lo strumento nel gioco, il file caricato o entrambi.

## 8. Riferimenti

- H. Ebbinghaus, *Über das Gedächtnis*, 1885.
- N. J. Cepeda et al., "Distributed practice in verbal recall tasks", *Psychological Bulletin*, 2006.
- J. Dunlosky et al., "Improving students' learning with effective learning techniques", *Psychological Science in the Public Interest*, 2013.
- H. L. Roediger, J. D. Karpicke, "Test-enhanced learning", *Psychological Science*, 2006.
- A. Paivio, *Imagery and Verbal Processes*, 1971.
- N. J. Slamecka, P. Graf, "The generation effect", *Journal of Experimental Psychology: Human Learning and Memory*, 1978.
- J. Sweller, "Cognitive load during problem solving", *Cognitive Science*, 1988.
- R. A. Bjork, "Memory and metamemory considerations in the training of human beings", 1994.
- M. T. H. Chi et al., "Self-explanations", *Cognitive Science*, 1989.
- Strumenti: Pyodide (pyodide.org), v86 (github.com/copy/v86), sql.js, SheetJS: tutti software libero.

## 9. Registro modifiche

- **v0.5 (02/10/2026)**: controllo di coerenza: tre rimandi di versione erano fermi a prima della loro ultima revisione (`tappa-1-01.md` v0.2, `anno1-mappa.md` v0.7, `anno1-ferrara.md` v0.2). Il testo non cambia.

- **v0.4 (30/09/2026)**: grafica della zona in 3/4 con geometria reale; ritratti 48×54; rinvio a `motore-e-grafica.md`.

- **v0.3 (30/09/2026)**: Borso personaggio giocante; zone percorribili in stile Pokémon (§3.5); pausa di autoregolazione (§3.6); rinvii a `esercizi.md` e `quadro-trasversale.md`.

- **v0.2 (28/09/2026)**: aggiunte le visioni di Borso per i facoltativi (§3.4).

- **v0.1 (28/09/2026)**: prima versione.
