---
titolo: Videogioco "I cinque duchi" — Salvataggio, consegna e integrità del punteggio
versione: 0.3
data: 2026-09-28
autore: Pietro Fabbri (con Claude)
fonte: requisiti di Pietro (28/09/2026), già emersi nel progetto "piattaforma gamificata"
documenti collegati: videogioco-5-duchi-curricolo.md, videogioco-5-duchi-schema-livelli.md, videogioco-5-duchi-anno1-ferrara.md
---

# Salvataggio, consegna e integrità del punteggio

## 0. Vincoli di partenza

- **Nessun account e nessun server che conservi dati degli studenti.** Lo stato del gioco vive nel browser dello studente e nel file che lo studente scarica.
- **Consegna settimanale su Google Classroom**, cioè tramite lo strumento già autorizzato dalla scuola.
- **Il punteggio valuta il processo, non solo l'esito.**
- **Onestà sui limiti.** Nessun sistema digitale è a prova di screenshot o di manomissione: tutto ciò che si legge sullo schermo può essere copiato, e tutto ciò che gira nel browser può essere ispezionato. L'obiettivo realistico è rendere il copiare **meno conveniente del giocare davvero** e far sì che **copiare la risposta non produca comunque un buon punteggio**.

---

## 1. Il file di consegna: un solo export, tre funzioni

Lo studente scarica **un solo file**, che è insieme:

1. **il compito da consegnare** su Classroom;
2. **un report leggibile** a colpo d'occhio dal docente;
3. **il salvataggio** che il gioco rilegge per far ripartire lo studente esattamente da dove aveva lasciato.

### 1.1 Formato

**Proposta:** file di testo UTF-8 con estensione `.txt`, nome `5duchi_<nome>_<AAAA-MM-GG>.txt`.

- **Perché `.txt`.** Classroom lo mostra in anteprima senza scaricarlo; si legge su qualsiasi dispositivo; non esegue codice. Un file `.html` sarebbe più bello, ma Classroom non lo mostra in anteprima e un HTML aperto in locale può contenere script.
- **Alternativa da valutare:** PDF generato dal browser. È più curato graficamente, ma rende più difficile la rilettura del codice da parte del gioco.

### 1.2 Struttura del file

```text
=== I CINQUE DUCHI — REPORT DI GIOCO ===
Nome inserito: Giulia R.            Classe: 1A
Esportato il: 2026-10-05 18:42      Versione del gioco: 0.3.1
Anno di gioco: 1 (Borso)            Livello attuale: 1-9 (Codifica del testo: ASCII)

--- RIEPILOGO ---
Livelli superati (soglia raggiunta): 8/30
Approfondimenti completati: 5
Punteggio totale: 742               Indice di processo medio: 0,81
Tempo di gioco totale: 3 h 12 min   (questa settimana: 58 min, 3 sessioni)
Tentativi totali: 214               Errori: 37   Suggerimenti usati: 6

--- DETTAGLIO PER LIVELLO ---
Livello  Argomento                         Stato      Punti  Processo  Tempo   Tent.  Err.  Sugg.
1-1      Informazione, dato, messaggio      superato     95    0,92    14 min    12     1     0
1-2      Analogico e digitale               superato     88    0,85    22 min    18     3     1
…
1-9      Codifica del testo: ASCII          in corso     31    0,64     9 min    11     4     2

--- INDICATORI DA GUARDARE ---
1-7: 4 istanze risolte con esito corretto e passaggi intermedi incoerenti
1-8: tempo di risposta molto inferiore al tempo atteso per la difficoltà, in 3 istanze

--- CODICE DI RIPRESA (non modificare) ---
5D1:eJyrVkrLz1eyUkpKLFKqBQAvWwXq…:c=7F3A91C2
=== FINE ===
```

### 1.3 Contenuti

| Sezione | Campi | Note |
|---|---|---|
| Intestazione | nome inserito, classe, data e ora dell'export, versione del gioco, anno e livello attuale | Il **nome è scritto a mano dallo studente**: è l'unico dato personale e serve solo al docente per riconoscere il file |
| Riepilogo | livelli superati, approfondimenti, punteggio totale, indice di processo medio, tempo totale e settimanale, sessioni, tentativi, errori, suggerimenti | Corrisponde ai campi richiesti da Pietro |
| Dettaglio per livello | stato, punti, indice di processo, tempo, tentativi, errori, suggerimenti | Il docente vede **dove** lo studente fatica |
| Dettaglio per argomento (facoltativo) | padronanza per nodo della mappa (es. `B2.1.4`) | Utile per collegare il gioco alla programmazione didattica |
| Indicatori da guardare | segnalazioni del §2.4 | **Non sono sanzioni**: sono spunti per un colloquio |
| Codice di ripresa | stringa compatta | Vedi §1.4 |

### 1.4 Il codice di ripresa

- **Contenuto:** lo stato completo del gioco in JSON (livelli, punteggi, parametri di padronanza, semi delle istanze in corso, registro sintetico degli eventi), compresso e codificato in base64url.
- **Formato:** `5D<versione>:<dati>:c=<checksum>`. Il prefisso con la versione permette di migrare i salvataggi quando il gioco cambia.
- **Checksum (CRC32):** rileva le corruzioni accidentali, per esempio un copia-incolla incompleto.
- **Coerenza fra report e codice.** Il testo del report è generato dal codice. Un docente può quindi verificare con uno **strumento del docente** (una pagina che legge uno o più file) che il report non sia stato ritoccato a mano: se lo studente modifica il testo leggibile, il riepilogo non corrisponde più al codice.
- **Limite dichiarato.** Qualsiasi chiave di firma contenuta nel gioco è visibile a chi ispeziona il codice. Il codice di ripresa è quindi un **deterrente**, non una garanzia. Il vero presidio è che il punteggio conta poco rispetto al processo osservato (§2) e al colloquio in classe (§2.5).
- **Dimensione:** il registro degli eventi va riassunto. Si conservano i totali per livello e solo gli ultimi N eventi di dettaglio, così che il codice resti copiabile.

### 1.5 Ripresa e privacy

- **Ripresa.** Lo studente apre il gioco, carica il file (o incolla il codice) e riparte da dove aveva lasciato. Il gioco salva anche nel browser (localStorage) per comodità, ma il file è l'unico salvataggio affidabile, perché il browser può essere svuotato.
- **Privacy.** Nessun dato esce dal dispositivo dello studente, se non tramite il file che lui stesso consegna su Classroom. Non si raccolgono dati diversi dal nome inserito. Sono coerenti con la minimizzazione dei dati e la protezione fin dalla progettazione (art. 5 e 25 GDPR).

### 1.6 Strumento del docente (proposta)

Una pagina statica, che funziona anche offline, in cui il docente carica tutti i file della classe di una settimana. La pagina:

- verifica la coerenza fra report e codice;
- produce una tabella della classe (studente × livello) con i progressi rispetto alla settimana precedente;
- elenca gli indicatori da guardare;
- esporta la tabella in CSV per il registro personale.

Come nel gioco, tutto avviene nel browser del docente, senza server.

---

## 2. Integrità del punteggio: rendere inutile lo screenshot dato in pasto a un'IA

### 2.1 Leva 1 — Interazione manipolativa, non domande testuali

Si evitano le domande a scelta multipla in forma di testo (per esempio "quale di queste è la codifica binaria di 13? A) B) C) D)"), perché sono perfette da incollare in un'IA. Lo studente invece **costruisce, manipola e prevede**.

| Famiglia di livelli | Interazione tipo |
|---|---|
| Codifiche e numerazione (1-3…1-11) | Accendere e spegnere bit su una rappresentazione visiva; comporre pesi su una bilancia; trascinare caratteri nella tabella di codifica |
| Colori e immagini (1-12, 1-13) | Regolare i canali RGB fino a ottenere un colore dato; dipingere pixel su una griglia |
| Architettura (1-14…1-20) | Eseguire passo per passo il ciclo fetch-decode-execute, **prevedendo l'effetto di ogni passo prima che venga rivelato**; collegare porte logiche |
| Sistemi operativi (1-21…1-24) | Ordinare processi in una coda; navigare un file system; assegnare permessi |
| Fogli elettronici (1-26, 1-27) | Scrivere formule su dati generati; costruire grafici |
| Algoritmi e programmazione (anno 2 e seguenti) | Tracciare l'esecuzione con previsione dei valori delle variabili; completare o correggere codice su istanze sempre diverse |
| Storia e fonti (§7 dell'anno 1) | Classificare affermazioni con le etichette D/I/M/L/F; collocare su linea del tempo e mappa; confrontare fonti |

**Principio "prevedi prima di vedere".** In molte interazioni lo studente deve **impegnarsi su una previsione** (il valore di una variabile, lo stato di un registro, l'esito di una formula) prima che il gioco mostri il risultato. La previsione entra nel calcolo del processo (§2.3).

Un'IA può dire allo studente che cosa cliccare, ma per farlo lo studente deve descriverle l'intera interfaccia e lo stato corrente, a ogni passo. È molto più laborioso che leggere un quiz, e a un certo punto conviene capire.

### 2.2 Leva 2 — Istanze generate proceduralmente

- Ogni istanza (numeri, testi, dati, grafi, programmi) è generata da un **seme casuale** e cambia a ogni tentativo.
- Così si annullano il copia-incolla fra compagni, le risposte "già viste" in rete e il riuso della soluzione di uno screenshot al tentativo successivo.
- Il seme viene salvato nel registro. Il docente può quindi **rigenerare esattamente l'istanza** che lo studente ha affrontato e chiedergliene conto (§2.5).

### 2.3 Leva 3 — Il punteggio misura il processo

Per ogni istanza il gioco registra:

| Misura | Definizione |
|---|---|
| **Esito** (E) | 1 se il risultato finale è corretto, 0 altrimenti |
| **Coerenza** (C) | Frazione dei passaggi intermedi e delle previsioni corretti, in [0, 1] |
| **Tentativi** (A) | Numero di tentativi prima dell'esito corretto |
| **Suggerimenti** (H) | Numero di suggerimenti usati, pesati per quanto rivelano |
| **Tempo relativo** (T) | Tempo impiegato diviso per il tempo atteso per quella difficoltà |

**Punteggio di un'istanza (proposta da calibrare):**

```text
indice_processo P = 0,50·C + 0,20·f(A) + 0,15·g(H) + 0,15·h(T)      con P in [0, 1]
punti = difficoltà × E × P
```

- f, g e h valgono 1 nel caso ideale e calano gradualmente (per esempio f(A) = 1 / A).
- h(T) penalizza sia i tempi **troppo lunghi** sia quelli **implausibilmente brevi** rispetto alla difficoltà.
- **La coerenza pesa più di tutto.** Chi indovina l'esito ma sbaglia sistematicamente i passaggi (segno di un esito copiato senza seguire il ragionamento) ottiene un punteggio **inferiore** a chi arriva più lentamente ma con un percorso coerente.
- **Soglia di sblocco** di un livello: *k* istanze consecutive con E = 1 **e** C ≥ θ. Valori iniziali: *k* = 3, θ = 0,7; per le prove di corte *k* = 5. Senza coerenza, l'esito da solo non sblocca il livello.
- **Calibrazione.** I pesi e le soglie sono provvisori e vanno tarati sul prototipo, con dati di gioco reali.

### 2.4 Indicatori da guardare

Il gioco non accusa e non sanziona: **segnala al docente**, nel report, alcuni schemi anomali.

- Esito corretto con coerenza bassa, ripetuto nello stesso livello.
- Tempi molto inferiori al tempo atteso in istanze difficili.
- Lunghe pause seguite da risposte perfette e immediate: uno schema compatibile con un aiuto esterno, ma anche con una distrazione.
- Salti di prestazione improvvisi rispetto alla storia dello studente.

Sono **indizi, non prove**. Il report li presenta come spunti per un colloquio. Coerenza con la politica sull'IA a cui Pietro sta lavorando: **nessuna decisione sugli studenti si basa unicamente su un trattamento automatizzato** (art. 22 GDPR), e il punteggio **non è un voto** ma un'informazione per il docente.

### 2.5 Il presidio umano

- **Verifica a campione in classe.** Il docente rigenera dal seme un'istanza già affrontata dallo studente e gli chiede di spiegarne un passaggio.
- **Poca posta in gioco.** Se il punteggio del gioco pesa poco sulla valutazione, l'incentivo a copiare cala. La valutazione vera resta affidata al docente, che usa il report come una delle fonti.

### 2.6 Limitare occhiali smart, IA, copia e incolla, screenshot

Richiesta di Pietro (28/09/2026). Le misure sono di due tipi: **tecniche**, dentro il gioco, e **organizzative**, in classe. Nessuna misura tecnica da sola basta. Per esempio, una foto dello schermo fatta con un telefono o con un paio di occhiali non si può impedire via software. Per questo le misure vanno combinate.

#### 2.6.1 Una sola modalità (decisione di Pietro, 28/09/2026)

Non ci sono modalità separate. Gli studenti giocano **sempre, anche a casa**; **in classe** si gioca occasionalmente, con lo stesso gioco e le stesse regole. Le misure tecniche (§2.6.2) valgono sempre. Quelle organizzative (§2.6.3) e il browser d'esame (§2.6.4) si usano quando si gioca in classe.

#### 2.6.2 Misure tecniche nel gioco

| Minaccia | Misura | Efficacia | Costo o effetti collaterali |
|---|---|---|---|
| Copia e incolla del testo verso un'IA | Disattivare selezione, copia, taglia e menu contestuale sui contenuti degli esercizi | Bassa (si aggira facilmente), ma elimina il gesto più comodo | Nessuno |
| Incolla di risposte generate altrove | Bloccare l'incolla nei campi di risposta; comunque quasi tutte le risposte sono manipolazioni, non testo digitato (§2.1) | Media | Nessuno |
| Assistenti IA integrati nel browser, che leggono il testo della pagina | Disegnare le consegne degli esercizi su **canvas** invece che come testo della pagina | Media: l'assistente deve passare da uno screenshot, non può leggere il testo | **Rende la pagina illeggibile agli screen reader**: serve una modalità accessibile per gli studenti con PDP o PEI (§2.6.5) |
| Screenshot o foto dati in pasto a un'IA | Istanze procedurali, interazione manipolativa, "prevedi prima di vedere" (§2.1–2.2); **un solo passo visibile alla volta**, così che uno screenshot non contenga mai l'intero problema | Media-alta: lo scambio diventa lento e costoso | Nessuno |
| Condivisione di screenshot fra compagni | **Filigrana dinamica** sullo schermo con nome inserito, seme dell'istanza e ora | Deterrente: ogni immagine è riconducibile a chi l'ha prodotta e all'istanza, che comunque è diversa per ciascuno | Nessuno |
| Uscita dalla finestra per consultare altro | Registrare nel log le perdite di focus e i cambi di scheda; nella prova in classe, schermo intero con segnalazione dell'uscita | Informativa: finisce fra gli "indicatori da guardare" (§2.4), senza sanzioni automatiche | Nessuno |
| Tempi di risposta innaturali | Indice di processo (§2.3) | Media | Va calibrato |
| **Bloccare gli screenshot del sistema operativo** | **Non è possibile in modo affidabile da una pagina web.** Esistono trucchi basati sulla protezione dei contenuti video (DRM), ma sono fragili e non si propongono | — | — |

#### 2.6.3 Misure organizzative per le sessioni in classe

- **Dispositivi personali.** La nota del Ministro prot. 3392 del 16/06/2025 estende al secondo ciclo il divieto di usare lo smartphone durante le lezioni, salvo autorizzazione del docente per attività didattiche o esigenze documentate. Gli occhiali con fotocamera o assistente vocale e gli smartwatch non sono nominati esplicitamente. **Proposta:** chiedere che il regolamento d'istituto estenda la regola a tutti i **dispositivi indossabili dotati di fotocamera, microfono o assistente IA** durante le prove. Il tema si collega al lavoro di Pietro sulla politica d'istituto per l'IA.
- **Occhiali smart.** Durante la prova chi porta occhiali con fotocamera li sostituisce con occhiali da vista normali, o li deposita. Il docente non può verificarlo tecnicamente, ma può vederlo: la regola va dichiarata prima della prova.
- **Rete del laboratorio.** Durante la prova, con il tecnico di laboratorio, si possono bloccare a livello di rete i siti di IA generativa più diffusi.
- **Verifica orale a campione** con rigenerazione dell'istanza dal seme (§2.5).

#### 2.6.4 Browser d'esame per le sessioni in laboratorio

**Safe Exam Browser** (software libero, per Windows, macOS e iPad) trasforma il computer in una postazione d'esame. Blocca l'accesso ad altre applicazioni, il cambio di finestra, gli appunti e la cattura dello schermo, e permette di consultare solo gli indirizzi autorizzati, cioè quello del gioco. È la misura tecnica più efficace per le **sessioni in classe** sui computer della scuola. Da verificare con il tecnico di laboratorio la compatibilità con le macchine del Carpeggiani.

#### 2.6.5 Limiti e cautele

- **Nessuna sorveglianza con webcam o riconoscimento automatico del comportamento.** Sarebbe invasiva e sproporzionata rispetto al GDPR. Inoltre l'AI Act classifica **ad alto rischio** i sistemi di IA destinati a monitorare e rilevare comportamenti vietati degli studenti durante le prove (Allegato III, punto 3), con obblighi dal 2 dicembre 2027, e **vieta** il riconoscimento delle emozioni negli istituti di istruzione (art. 5).
- **Accessibilità.** Canvas, tempi stretti e un solo passo visibile alla volta possono penalizzare gli studenti con DSA o disabilità. Il gioco deve avere una **modalità accessibile**, attivata dal docente secondo il PDP o il PEI: testo leggibile dagli screen reader, tempi estesi, sintesi vocale. Gli indicatori di tempo vanno ricalibrati per questi studenti.
- **Onestà del messaggio agli studenti.** Conviene dire apertamente come funziona il punteggio: "copiare l'esito non ti fa avanzare, perché conta la coerenza dei passaggi". È anche un deterrente.

---

## 3. Questioni aperte

1. Formato del file: `.txt` (proposta) oppure PDF.
2. Il gioco è un modulo della piattaforma gamificata o un prodotto a sé? I requisiti di questo documento valgono in entrambi i casi.
3. Pesi e soglie del §2.3 vanno calibrati sul prototipo.
4. Quanti eventi di dettaglio conservare nel codice di ripresa (§1.4).
5. Strumento del docente (§1.6): da realizzare subito o dopo il prototipo del gioco?
6. Proposta al regolamento d'istituto sui dispositivi indossabili (§2.6.3) e prova di Safe Exam Browser sui computer del laboratorio (§2.6.4).
7. Specifica della modalità accessibile (§2.6.5).

## 4. Registro modifiche

- **v0.3 (28/09/2026)**: eliminate le due modalità (allenamento e prova): si gioca sempre anche a casa e occasionalmente in classe.
- **v0.2 (28/09/2026)**: aggiunto §2.6 su occhiali smart, IA, copia e incolla e screenshot (modalità allenamento e prova, misure tecniche e organizzative, Safe Exam Browser, limiti e accessibilità). Aggiunta la verifica di coerenza della catena nel codice di ripresa (vedi `videogioco-5-duchi-anno1-mappa.md`, regola R6).
- **v0.1 (28/09/2026)**: prima formalizzazione dei requisiti di Pietro sul file di consegna e sull'integrità del punteggio.
