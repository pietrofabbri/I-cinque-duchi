---
titolo: Videogioco "I cinque duchi" — Ascolto e parlato (la parte orale delle sei lingue)
versione: 0.2
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte: richiesta di Pietro del 03/10/2026 («per ferrarese, inglese e meno spesso in italiano, occorrerà anche una parte cospicua di speaking e di listening: occorre un modo per rendere questo possibile nel gioco»); fatti tecnici e fonti verificati il 03/10/2026 con le API di Wikimedia
documenti collegati: videogioco-5-duchi-lingue.md (v0.1, le sei lingue e i 900 livelli), videogioco-5-duchi-meccaniche.md (v0.3, il file unico e la privacy), videogioco-5-duchi-gioco.md (v0.5, gli strumenti che girano nel browser), videogioco-5-duchi-esercizi.md (v0.1, le famiglie di esercizi), videogioco-5-duchi-pedagogia.md (v0.2), videogioco-5-duchi-premi.md (v0.3)
---

# Ascolto e parlato: come si rende possibile nel gioco

## 0. Che cosa c'è qui

Qui c'è **un'architettura e i fatti che la costringono**, non un piano di esercizi. Le
famiglie di esercizi (`Ascolta`, e le altre) sono già dichiarate in `lingue.md` §5.3
senza sapere se il motore può realizzarle: è la stessa forma di dichiarazione che il
progetto ha già corretto due volte (`osservazione e attenzione`, la 4-16). Questo
documento chiude il «se può».

Le domande interattive arrivano dopo, quando le altre cose saranno fissate. Qui si
prepara **il terreno**: che cosa è tecnicamente possibile, che cosa è impossibile oggi,
e che cosa diventa possibile solo con una decisione di Pietro.

## 1. La domanda, e perché tre lingue e non sei

Pietro lo ha detto con precisione: **ferrarese, inglese, e meno spesso italiano**. La
distinzione non è una preferenza estetica, è la differenza fra una lingua che si
impara a **parlare** e una lingua che si impara a **leggere**:

| lingua | perché il parlato pesa |
|---|---|
| **Ferrarese** | è la lingua dei nonni degli studenti. Un ragazzo di Ferrara che studia la propria lingua locale impara a **parlare con chi ha parlato con lui**, non a leggere. Il dialetto è in via di estinzione: chi non lo parla più non lo passa. |
| **Inglese** | è l'unica delle sei in cui l'ascolto ha una quantità quasi illimitata di materiale autentico libero (89 381 registrazioni, §2.3), e in cui il gioco può offrire testi lunghi veri senza cercare nulla di nuovo |
| **Italiano** | serve, ma il patrimonio è enorme e l'orecchio è già allenato: meno spesso |
| **Latino, greco** | si studiano per la scrittura. Il parlato non esiste e non verrà: sono lingue morte da quindici e ventiquattro secoli. Nessun audio autentico può esistere, e questo non è un buco del progetto. |
| **LIS** | non è una lingua orale: il canale è il movimento delle mani e del viso, e la «voce» è il volto. Vede `lingue.md` Q4: il gioco non sa disegnare la propria lingua dei segni, e qui vale la stessa regola con un'altra forma. |

## 2. I fatti, con la fonte e la data

Una decisione di architettura senza fatti è un'opinione. Questi sono verificati, e
la regola del progetto li vuole dichiarati con la fonte accanto.

### 2.1 Il vincolo che decide tutto: nessun server

`meccaniche.md` §1 e `gioco.md` §2.3: **nessun account, nessun server che conservi
dati degli studenti**; lo stato vive nel browser; il gioco funziona offline; la consegna
è **un solo file `.txt`**. Pyodide e v86 girano nel browser e restano in cache.

Ne segue che **qualunque cosa dell'orecchio che debba uscire dal dispositivo è
esclusa**, non per sfavore ma per la regola che il progetto ha già scritto: «nessuna
sorveglianza con webcam o IA (GDPR, AI Act)» (`meccaniche.md` §2.2). Il microfono
non è una sorveglianza se non esce, e diventa una sorveglianza se esce.

### 2.2 Perché l'API di riconoscimento vocale del browser è esclusa

**Fatto.** La Web Speech API (`SpeechRecognition`) è la via ovvia, ed è **quella
sbagliata**: su Chrome e Edge **invia l'audio ai server di Google** per la
riconoscimento, non funziona offline, e la documentazione di Mozilla lo scrive
esplicitamente (*«your audio is sent to a web service for recognition processing, so
it won't work offline»*).

È quindi esclusa per due ragioni indipendenti, e basta una: **il gioco non deve
poter mandare la voce di un adolescente a un server esterno**, e il progetto ha già
scelto di non avere server. Una decisione che dipende solo da «è comodo» o «è gratis»
qui diventa una scelta di privacy, e va scritta come tale.

### 2.3 Che cosa c'è davvero da ascoltare, e quanto

Verificato il 03/10/2026 con l'API di Wikimedia Commons e salvato in
`dati/lingue/audio_disponibili.json`, che porta la query che ha prodotto ogni numero
(`sorgenti/lingue/cerca_audio_oggetti.py`):

| lingua | registrazioni libere trovate |
|---|---|
| **inglese** | **89 381** |
| **italiano** | **9 179** |
| **greco** | 79 |
| **latino** | 24 |
| **ferrarese** | **0** |
| **LIS** | **0**, e non è un buco: non è una lingua orale |

Il numero del ferrarese è il risultato più importante di questo documento, e non è un
buco: **è la ragione per cui il progetto del ferrarese è un progetto di ascolto**. La
lingua che il gioco ha più bisogno di ascoltare è **l'unica che su Wikimedia non ha
una sola registrazione**.

C'è inoltre un patrimonio più ampio e non ancora contato: le registrazioni di opere
intere (spoken books, LibriVox e simili) su Commons e su Wikisource, che per l'inglese
e l'italiano sono centinaia. Il 3 ottobre non è stato contato, e va contato prima di
scrivere i livelli: **è la differenza fra audio di una parola e audio di un testo**.

## 3. La risposta: cinque livelli, e perché non è tutto o niente

La domanda «si può fare speaking nel gioco?» ha una risposta che non è sì e non è
no: **si può fare tutto il parlato che non richiede di riconoscere la voce del
giocatore**, e quella è la parte grossa del lavoro. La parte che richiede riconoscimento
è dichiarata, non simulata.

### L1 · Ascolto autentico, dove esiste

Il gioco riproduce una registrazione **vera**, con la sua provenienza dichiarata
(registratore, data, licenza, eventuale revisione), e il livello chiede di capire.
Copre inglese e italiano senza problemi, greco e latino solo per testi brevi.

**Regola che vale per tutti i livelli:** ogni audio ha la sua scheda con autore,
data, licenza ed etichetta, sul modello delle 180 immagini degli oggetti
(`lingue-immagini.md` §1). Un audio senza provenienza non entra, come un'immagine
senza provenienza non entra.

### L2 · Ascolto prodotto dal giocatore: la voce della famiglia

È la risposta al ferrarese, e non è un ripiego: è **il cuore del progetto per quella
lingua**. Il gioco non ha audio del ferrarese perché il ferrarese dei ragazzi di oggi
non è registrato da nessuna parte; l'unico modo di averlo è **chiedere a chi lo parla**.

Il gioco può quindi chiedere a uno studente (o alla classe, o al gruppo di famiglia) di
**registrare una frase della propria lingua** e di metterla nel **quaderno dei segni e
delle voci**, che è già uno dei quattro registri personali (`inventario.md` §3). Da quel
momento il gioco ha un pezzo di ferrarese autentico che **non poteva esistere prima**,
e che è di un ragazzo di quindici anni.

Tre regole, per la stessa ragione che vale alla LIS:
- **la registrazione resta del ragazzo e della sua famiglia**, e non entra nel file di consegna (audio = dato personale);
- **il gioco non giudica la qualità della voce**: è un ascolto, non un concorso di dizione;
- **chi non ha nessuno che parli la lingua non è penalizzato**: l'esercizio diventa lettura, e il gioco lo dichiara.

### L3 · Parlare senza riconoscimento: la ripetizione misurata

Qui è il punto che rende la cosa possibile **oggi**, e la chiave è che **il gioco non
deve capire la voce del giocatore per poterlo far lavorare**.

Quattro cose che il motore può misurare senza riconoscere niente, perché sono
proprietà del segnale audio grezzo:

| cosa misura | come | perché serve al livello |
|---|---|---|
| **durata del parlato** | dal pulsante allo silenzio | il ragazzo che sa la frase parla in un tempo; quello che non sa, si ferma |
| **numero di pause** | segmenti di silenzio sopra una soglia | è la firma di chi sta cercando la parola giusta |
| **coerenza** | il gioco riproduce il modello **a intervalli irregolari** e il ragatore segue il ritmo | misura il contatto con la pronuncia, non la pronuncia |
| **riascolto** | il gioco fa riascoltare **la propria voce** subito dopo | è la modalità più efficace di autocorrezione, e non costa nulla |

Queste quattro misure sono le uniche che il gioco può prendere **senza inviare niente
fuori e senza riconoscere niente**, e sono sufficienti per il punteggio di processo: il
gioco non dice «hai detto bene», dice «hai tenuto il ritmo per tredici secondi senza
interromperti», che è un'informazione vera e verificabile.

### L4 · Parlare con una scelta: la discriminazione uditiva

Il livello più importante, e quello che nessuno sta costruendo: **si può chiedere di
parlare e si può verificare la risposta senza ascoltare**.

Il gioco riproduce **due o tre registrazioni** (o la voce dello stesso giocatore in due
passaggi) e chiede: «quale di queste è la frase del testo?», «che cosa hai sentito che
non c'era nel testo?», «questa registrazione è della tua frase o di una frase
somigliante?». Il compito è **di ascolto e di linguistica**, non di dizione, ed è
completamente verificabile.

È la stessa intuizione che regge gli altri due sport che il progetto ha già scelto: la
**scelta di una mappa** invece che la costruzione di un compito (`tappa-1-01.md` §3), la
**manipolazione** invece della digitazione (`meccaniche.md` §2.1). Nel gioco si misura
**la decisione**, non l'esecuzione.

### L5 · Riconoscimento automatico: dichiarato, non fatto

È l'unico livello che richiede un modello. Le opzioni esistono e sono libere —
**Vosk** (WASM, leggero) e **Whisper** compilato per il browser (più pesante, usa
WebGPU quando c'è) — e funzionano **offline**, dentro il browser, senza mandare
niente fuori. Ma:

- i modelli sono **decine di megabyte per lingua** e si scaricano la prima volta: il
  progetto ha già accettato questo costo per Pyodide e v86, e qui è ben maggiore;
- **non esiste un modello del ferrarese**, e addirittura è improbabile che ne nasca
  (i dati non ci sono, §2.3);
- riconoscere la voce di un adolescente è, tecnicamente, **trattare dati personali
  di un minore**: anche in locale, la decisione è di Pietro e va scritta, non
  assunta.

Quindi L5 è **dichiarato come non fatto**, con la condizione che lo sblocchi: un modello
on-device **solo per le lingue che ne hanno**, il consenso esplicito, e il tempo di CPU
messo a bilancio. Il gioco deve poter funzionare **senza** L5, perché L5 è l'unico
livello che può non arrivare mai.

## 4. Che cosa cambia nella parte scritta, e che cosa non cambia

Nulla, e questa è la parte importante: **la parte orale non è un sistema a sé**, come
la `Ascolta` non è una famiglia di esercizi separata.

| cosa | prima | dopo |
|---|---|---|
| **componente del livello** | le nove componenti di `lingue.md` §2 | **le stesse nove**, e la parte orale è dentro il **nucleo teorico**, gli **esercizi di comprensione** e la **piccola sfida**. Nessuna componente nuova: si aggiunge una **modalità** |
| **famiglie di esercizi** | cinque (`lingue.md` §5.3), con `Ascolta` già dichiarata | le stesse cinque. `Ascolta` passa da **famiglia** a **famiglia con due forme**: ascoltare, e parlare |
| **blocchi da sei** | cinque blocchi | gli stessi. Il blocco **4 · Produzione** è quello dove il parlato pesa di più, ma nessun blocco cambia struttura |
| **file di consegna** | un solo `.txt` | **lo stesso `.txt`**, e cambia una riga: nel rapporto dei livelli linguistici compare **la misura del parlato** (durata, pause, ritmo), non l'audio. L'audio non entra, perché è dato personale |
| **premio** | categoria K per la LIS | **K vale anche per il parlato**: il quaderno del giocatore, con la sua voce o la sua frase, è l'unico premio che non si può copiare |

**La regola che tiene tutto insieme** è la stessa della LIS: **quello che il gioco non
sa fare non si simula, si dichiara e si aggira**. Il gioco non sa riconoscere la voce e
non lo farà finta; non ha il ferrarese e non lo farà finta; non sa disegnare i segni e
non lo farà finta. In tutti e tre i casi la soluzione è la stessa e non è un compromise:
**il giocatore mette dentro la cosa che il gioco non sa fare**, e il gioco la organizza.

## 5. Il terreno che si prepara adesso

Cosa si può costruire senza aspettare nessuna decisione:

1. ~~**Il contatore delle fonti audio**~~ **fatto il 03/10/2026**:
   `sorgenti/lingue/cerca_audio_oggetti.py` → `dati/lingue/audio_disponibili.json`,
   sei lingue su sei contate. Manca ancora il **secondo** conteggio, che è quello
   difficile: quante registrazioni per **voce** e quante per livello di difficoltà.
2. **Il secondo conteggio** e **lo schema del dato audio**, che è lo stesso delle 180
   immagini e quindi si sa già scrivere: `voce`, `file`, `registratore`, `data`,
   `licenza`, `etichetta`, `durata`, `lingua`, `provenienza` (nativo, prodotto dal
   giocatore, sintesi).
3. **Le misure del parlato** (durata, pause, ritmo, riascolto), che sono quattro numeri
   e la loro soglia: è il pezzo che rende L3 possibile senza alcun modello.

## 6. Le decisioni che sono di Pietro

| # | domanda | perché è di lui |
|---|---|---|
| **P1** | il gioco può **chiedere il permesso del microfono**? | è il presupposto di L2 e L3. Senza la risposta, il parlato è L4 e basta. Il progetto ha già deciso di non usare webcam e IA per sorveglianza; il microfono per imparare è un'altra cosa, e la decisione va detta |
| **P2** | l'**audio entra nel file di consegna**? | la risposta consigliata è **no** (dato personale di un minore), e in quel caso il file porta la misura e non la voce |
| **P3** | **le opere intere** (spoken books) entrano come ascolto lungo? | per l'inglese e l'italiano sono centinaia e cambiano la natura del blocco 3 · Comprensione. Il conteggio non è fatto |
| **P4** | **L5 si apre** (modello on-device), e per quali lingue? | è la sola che comporti modelli enormi e dati personali. Per il ferrarese è esclusa dai dati, non dalla decisione |
| **P5** | chi **raccoglie le registrazioni** dei nonni ferraresi, e con quale consenso? | per il ferrarese non basta il gioco: le trenta voci ferraresi sono già dichiarate «proposte, non voci confermate» (`lingue.md` §5.4), e l'audio è la prova che le voci sono vere |

## 7. Cosa c'è da fare

1. ~~**Il contatore delle fonti audio**~~ **chiusa il 03/10/2026**; resta il secondo, per voce.
2. **Lo schema del dato audio** (§5.2) — lavoro.
3. **Le misure del parlato** (§5.3) — lavoro.
4. **Le cinque decisioni** di §6.

## 8. Registro delle modifiche

- **v0.1 (03/10/2026)**: prima stesione. Nasce dalla richiesta di Pietro sullo speaking e il
  listening per ferrarese, inglese e italiano. Il documento chiude il «si può fare» con quattro
  fatti verificati in giornata e una risposta in cinque livelli. Il fatto che decide è uno solo:
  **su Wikimedia Commons non esiste una registrazione di ferrarese**, mentre l'inglese ne ha
  89 381 e l'italiano 9 179. Quindi l'ascolto del ferrarese non si compra e non si cerca: **si fa**,
  chiedendo a chi parla la lingua, ed è un registro personale che il gioco non può costruire
  da solo. Le tre tecnologie disponibili sono tutte escluse o dichiarate per una ragione precisa:
  la Web Speech API perché manda l'audio ai server di Google, i modelli on-device perché non
  esistono per il ferrarese e perché trattano dati di un minore, e il riconoscimento automatico
  perché un gioco senza server non può fingere di averlo. La parte che resta è la più grande:
  **si può allenare il parlato senza riconoscere la voce**, misurando durata, pause, ritmo e
  riascolto, e chiedendo scelte che il gioco può verificare. Nessuna delle cinque decisioni
  di §6 è presa qui.
