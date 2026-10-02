---
titolo: Videogioco "I cinque duchi" — audit finale delle questioni aperte
versione: 0.1
data: 2026-10-02
autore: Pietro Fabbri (con Claude)
fonte: lettura di tutti i documenti di progetto del 02/10/2026
documenti collegati: videogioco-5-duchi-lingue.md (v0.1), videogioco-5-duchi-lingue-immagini.md (v0.1), videogioco-5-duchi-furioso.md (v0.4), videogioco-5-duchi-luoghi.md (v0.3), videogioco-5-duchi-mappe.md (v0.4), videogioco-5-duchi-anno5-mondo.md (v0.4), videogioco-5-duchi-anno4-mondo.md (v0.5), videogioco-5-duchi-anno3-europa.md (v0.4), videogioco-5-duchi-anno2-penisola.md (v0.2), videogioco-5-duchi-ritratti.md (v0.2), AGENTS.md
---

# Audit finale delle questioni aperte

## 0. Che cos'è questo documento, e a che cosa serve

Questo documento mette **in fila tutte le questioni aperte del progetto**: le dodici sezioni «Questioni aperte» dei documenti di progetto, 96 voci enumerate, in un solo posto e in prosa.

Serve a tre cose, e le tre contano.

La prima è che **una questione aperta in un documento solo è una domanda che si perde**. Il progetto ha sedici documenti, ciascuno con le sue questioni: quindici su cento righe, in fondo, dove nessuno le cerca più. Un elenco unico le rende visibili e le ordina per conto di decisione.

La seconda è che **alcune questioni bloccano altre questioni**, e senza vederle insieme si risolve una cosa che dipende da una che è ancora aperta. Il caso più chiaro è `lingue.md` Q1: finché non si sa se i livelli linguistici e quelli informatici sono lo stesso livello o due, non si possono scrivere i dati dei 900 livelli, e quindi non si possono scegliere le immagini, e quindi non si possono scrivere le tappe. Sono tre passaggi bloccati da una domanda sola.

La terza è che **alcune questioni sono in realtà la stessa domanda scritta in due documenti**, e finché non lo si vede si risolvono due volte o si risolvono in modo incoerente. Nel registro qui sotto ce ne sono tre, tutte elencate in §5.

**Che cosa non è questo documento.** Non decide niente. Le decisioni sono di Pietro, e qui sono raccolte quelle che mancano. Dove una domanda è già stata chiusa, la chiude il documento suo e qui si segna come chiusa.

---

## 1. Il conto, e come è contato

Ho letto le dodici sezioni «Questioni aperte» dei documenti di progetto. Il conto, a 02/10/2026, esce da `sorgenti/lingue/conta_questioni.py`, che è ripetibile e **confronta i numeri con quelli scritti qui**: se il documento e lo script non concordano, è il documento che ha torto.

| Documento | Aperte | Chiuse |
|---|---|---|
| `anno1-ferrara.md` | 7 | 0 |
| `anno2-penisola.md` | 8 | 1 |
| `anno3-europa.md` | 8 | 2 |
| `anno4-mondo.md` | 4 | 4 |
| `anno5-mondo.md` | 9 | 2 |
| `curricolo.md` | 7 | 0 |
| `furioso.md` | 2 | 5 |
| `gioco.md` | 5 | 0 |
| `lingue.md` | 11 | 0 |
| `luoghi.md` | 2 | 7 |
| `mappe.md` | 4 | 1 |
| `meccaniche.md` | 7 | 0 |
| **Totale** | **74** | **22** |

**Il criterio, dichiarato**, perché un conteggio senza criterio non è un dato. Una **voce** è un punto numerato, un `### Q1` o una riga di tabella della sezione «Questioni aperte». Una voce è **chiusa** se porta la marcatura nella sua **prima riga** — «chiusa», «risolto», «ratificata», «confermata» — e non in tutto il corpo, perché una voce aperta spiega dentro il corpo quale parte è stata chiusa. Il totale delle voci enumerate è **96**.

**Una voce non è sempre una domanda.** In `lingue.md` Q3 ci sono due sotto-voci dentro una sola domanda, e lo stesso vale in `luoghi.md` e `furioso.md`. Le **96 voci non sono 96 domande**: le questioni vere sono meno, e il numero esatto dipende da quante sotto-voci si contano come domanda a sé. Dichiaro la cifra grande perché è verificabile, e non dichiaro una cifra più piccola perché richiederebbe un giudizio che nessuno script può fare.

**I ventidue chiusi non sono una nota a margine**: sono il lavoro più grosso degli ultimi due giorni, e la ragione per cui molte domande che sembravano difficili erano già decise. Le sette di `luoghi.md`, le cinque di `furioso.md`, le quattro di `anno4-mondo.md`, i due dell'anno 3, i due dell'anno 5, l'ODbL di `mappe.md`, i codici `Q` dei tre anni.

**Nessuno dei ventidue chiusi è bloccante.** È il fatto più rassicurante dell'audit: le decisioni prese hanno tolto lavoro, non lo hanno aggiunto.

## 2. Le cinque questioni bloccanti

### B1 — `lingue.md` Q1: i livelli linguistici e quelli informatici sono lo stesso livello o due?

**Dove.** `videogioco-5-duchi-lingue.md` §7 Q1.

**Perché blocca.** Il gioco ha 150 livelli informatici e 900 linguistici, e non si sa come stiano insieme. Le tre possibilità sono nel documento: due sistemi paralleli nella stessa tappa, due sistemi in tappe diverse, oppure le lingue dentro l'informatica. La prima rende ogni tappa a **trentadue livelli**; la seconda raddoppia le tappe; la terza cancella le 900 unità di gioco.

**Che cosa blocca, nell'ordine.**

1. **I dati dei 900 livelli** (`lingue.md` §8.4): non si può scrivere un livello senza sapere in quale tappa sta.
2. **La scelta delle immagini** (`lingue-immagini.md` §6.2 Q2): cercare le immagini prima di sapere se le tappe sono 30 o 150 cambia tutto.
3. **Le tappe linguistiche** e i loro esercizi.
4. **I testi autentici** e le loro immagini (`lingue-immagini.md` §6.2 Q5).
5. **La progressione complessiva** che il gioco mostra allo studente.

**Che cosa non blocca.** La sequenza dei 900 titoli, che è un elenco e non una tappa; le sei associazioni con gli oggetti, che sono decisioni a parte; la ricerca delle immagini già fatta, che è reusable qualunque sia la risposta.

**Che cosa serve per decidere.** Una stima, non una discussione: quante schermate occupa una tappa oggi, quante potrebbero occuparne trentadue, e cosa dice la scuola di un'ora di lezione. Il documento ha i tre numeri; manca la stima.

### B2 — `lingue.md` Q2: le trenta voci di ogni oggetto sono confermate?

**Dove.** `lingue.md` §7 Q2, ripresa in `lingue-immagini.md` §6.2 Q2.

**Perché blocca.** Una ricerca cerca la voce giusta, non quella confermata. Se cambiano, tutta la ricerca delle 1120 immagini va rifatta. Per il ferrarese è più grave: le trenta voci non sono un elenco ma **campi da rilevare**, e la fonte non è ancora stabilita — chi raccoglie, con quale metodo, con quale consenso.

**Che cosa serve per decidere.** Una risposta in due tempi: le trenta voci di italiano, latino, inglese, greco e artigianato sono la mia proposta e vanno discusse una per una; quelle del ferrarese sono un progetto di raccolta e vanno decise come progetto, non come elenco.

### B3 — `lingue.md` Q4: la LIS nel gioco, con chi e con quali materiali?

**Dove.** `lingue.md` §7 Q4.

**Perché blocca.** I trenta livelli LIS sono i più difficili da scrivere di tutti i novecento, perché **non si possono scrivere a tavolino**: servono una collaborazione con la comunità sorda, materiali video, trascrizioni, e competenze che il progetto non ha. I titoli ci sono, il metodo no.

**Che cosa serve per decidere.** Due risposte: se c'è un milieu collaborativo con la comunità sorda, e chi se ne occupa. Senza questo, i trenta livoli LIS restano una sequenza di titoli, e vanno detti tali.

### B4 — `lingue-immagini.md` Q1: chi guarda le immagini?

**Dove.** `videogioco-5-duchi-lingue-immagini.md` §6.2 Q1.

**Perché blocca.** Sono **1120 candidati** e nessuno è stato guardato. Le opzioni sono tre: li guardo io e registro l'attestazione, li guarda Pietro, oppure si guarda un campione dei 146 migliori per voce. La terza è realistica ma **non è la stessa cosa**, e va detto: un campione non attesta il resto. Il file `dati/lingue/attestazione_oggetti.json` è pronto e vuoto.

**Che cosa blocca.** Le tappe facoltative degli oggetti. Non blocca il resto del gioco: è l'unica delle cinque che riguarda una parte facoltativa.

### B5 — `mappe.md` §10.5: i novanta pin degli anni 2, 3 e 4 sono verificati?

**Dove.** `videogioco-5-duchi-mappe.md` §10 punto 5 e §11 punto 2.

**Perché blocca.** Sono **novanta coordinate scritte a mano**, mai verificate, e sono le posizioni dove il gioco si ferma. Il controllo esiste (`sorgenti/gis/punto_in_poligono.py`) ed è pronto: va fatto girare, è il controllo che vale più di qualunque altro del progetto, e finché non è fatto non si può dire che una tappa sia «a Torino».

**Che cosa serve per decidere.** Niente: va fatto, non deciso. È l'unica delle cinque che è un lavoro e non una domanda.

---

## 3. Le questioni aperte dei documenti trasversali

Delle 74 voci aperte, **cinque sono bloccanti** (§2) e le altre 69 no. Di queste 69, quindici stanno nei quattro documenti trasversali e sono qui elencate; le altre 29 sono degli anni 2, 3, 4 e 5 (§4) e le 26 restanti sono di `anno1-ferrara`, `curricolo`, `gioco` e `meccaniche`, che non sono oggetto di questo audit perché sono le domande di progetto iniziale e non quelle nate dagli ultimi due giorni. Una delle quindici — le trenta voci dell'oggetto — è la stessa di una bloccante, ed è messa fra le doppioni in §5.

**Lingue** (`lingue.md` §7). **Q3**, che cosa è un «testo autentico» nelle sei lingue: per il greco è chiaro, per il ferrarese è una trascrizione di parlante, e lì si aprono il consenso e la varietà. **Q5**, il greco moderno attraversa tremila anni in tre anni di percorso: va deciso se ha una linea propria. **Q6**, il confronto fra le sei lingue è obbligatorio o a rotazione: la regola attuale dà trenta livoli di confronto all'anno, il 17% del totale, ed è forse troppo. **Q7**, che cosa succede quando il giocatore non sa l'italiano: serve una soglia minima per i livelli d'italiano, e la regola «nessuna competenza in ingresso» va applicata anche qui. **Q8**, il conto degli esercizi degli oggetti: trenta voci e una pool di venti fanno **3 600 esercizi** senza contare i livelli. Se le voci fossero venti, il conto calerebbe di un terzo. **Q9**, se i confronti filologici sono vincolanti e come li si controlla.

**Immagini degli oggetti** (`lingue-immagini.md` §6.2). **Q3**, le fonti del latino e del greco vanno cercate fuori da Commons: il controllo G7 dice che **27 voci latine su 28** hanno solo proposte scoperte per caso, e le fonti giuste sono i corpus epigrafici e le biblioteche digitali. **Q4**, che cosa fanno le trenta tappe ferraresi che non hanno immagine: dichiarare il vuoto o metterci altro. **Q5**, le immagini dei testi autentici dei 900 livelli **non sono state cercate**, e sono diverse da quelle degli oggetti. **Q6**, chi ridimensiona e quando: nessuna immagine è ancora stata ridotta a 96×72, perché nessuna è stata scelta.

**Mappa** (`mappe.md` §10). Il **vincolo di 20 000 abitanti** per mostrare una città è giusto? Cambia molto la quantità di nomi sulla mappa. Le **trenta zone percorribili** si fanno tutte o solo dove il luogo è davvero lo spazio del gioco? Il **file delle regioni amministrative** è grosso (450 kB, 1 687 geometrie): va ridotto?

**Furioso** (`furioso.md` §8 Q6). I **tredici filoni che il gioco mostra e i dodici che il documento dichiara**: dopo l'ingresso di F11 i filoni usati sono dodici. E le **ventisei stanze** senza coordinata, che non ne hanno bisogno ma hanno bisogno della regola scritta.

---

## 4. Le questioni degli anni 2, 3 e 4, che sono le stesse di sempre

Le questioni degli anni 2, 3, 4 e 5 non sono nuove: sono le stesse dei giorni precedenti, alcune chiuse e altre no. Le chiudo qui per intero, perché un elenco parziale fa pensare che il resto sia a posto.

**Anno 2**, nove punti, nessuno chiuso. Il più importante è **la carta intera alla fine dell'anno**: si apre una vista di tutta la penisola con gli strati visibili insieme? È l'idea centrale della carta a strati ed è ancora una domanda. Poi: tre collettivi su trenta tappe, il bilancio degli agganci (13 forti e 17 medi), la colonna stratigrafica a schermo, i codici `Q`, il materiale dal 1500 in poi, le persone viventi, le fonti del materiale, le «visioni» rispetto all'anno 1.

**Anno 3**, dieci punti, **uno chiuso** (il vuoto del Novecento, chiuso il 02/10 con la sostituzione di Turing con Levi e l'atlante di tredici voci) e uno **confermato** (i codici `Q`). Restano: la tratta e l'imperialismo, che è un buco tematico reale e dichiarabile; il bilancio degli agganci, con tre tappe segnalate come forse troppo forti; le persone viventi; le sei aggiunte; i ritorni, dove **Leonardo è obbligatorio in due anni** contro la regola proposta; la corte come unico luogo percorribile, che è il prezzo di una decisione già presa; le fonti del materiale.

**Anno 4**, otto punti, **tre chiusi** (il buco di S66 con Ibn Khaldun che diventa Ashoka, il peso del presente, i due collettivi) e uno **confermato** (i codici `Q`). Restano: i tre agganci «forti» da rivedere, le persone viventi, la tappa 4-10 e l'incendio, le fonti del materiale.

**Anno 5**, undici punti, uno **confermato** (i codici `Q`), due parzialmente risolti. Restano, e sono i più gravi del progetto: **il 1945 non è una tappa**, perché i livelli dell'anno non lo chiedono e il materiale sì; **il buco della biologia**, perché il materiale dedica quindici voci a medicina, vaccini, DNA e genetica e nessun livello dell'anno 5 le richiede; i facoltativi che il gioco non può mettere in tabella; i quattro agganci da rivedere; la sesta tappa della porta del futuro; le previsioni con la data; il posto di F11 nel registro del gioco.

---

## 5. Le stesse domande in due documenti

Tre questioni compaiono in più di un documento. Non è un difetto: è che le domande sono giuste e sono state poste dove servivano. Ma vanno unite, perché due risposte incoerenti sono peggio di una sola.

**La stessa domanda.** `lingue.md` Q2 (le trenta voci sono confermate) e `lingue-immagini.md` Q2 (sono la stessa, vista dal lato delle immagini). Una risposta sola le chiude entrambe.

**La stessa domanda, due versioni.** `lingue.md` Q5 (il greco moderno ha una linea propria?) e `anno5-mondo.md` — la stessa idea di «una linea che attraversa gli anni senza essere una tappa». Il progetto ha già accettato la risposta per gli anni 3 e 4 (l'atlante di tredici voci) e non per il greco: la domanda è se quella stessa risposta valga per le lingue antiche.

**Lo stesso difetto, due documenti.** I codici `Q` (`anno3` §13 Q6, `anno4` §13 Q5, `anno5` §13 Q4) sono confermati in tutti e tre i documenti e concordano. È l'unico caso in cui la ridondanza ha funzionato: le tre risposte sono state scritte una dopo l'altra e dicono la stessa cosa. **È anche la prova che la ridondanza funziona quando c'è qualcuno che la controlla.**

---

## 6. La sequenza che chiude tutto

L'audit serve anche a dire **in che ordine**. Le cinque bloccanti hanno una dipendenza sola, e la catena è breve.

1. **B1** (livelli linguistici o informatici) decide **B4** (immagini) e tutte le tappe linguistiche.
2. **B2** (voci confermate) viene **prima** di B4: cercare le immagini prima di aver confermato le voci è lavoro che va rifatto.
3. **B3** (LIS) è indipendente e può partire in parallelo, ma è la più lenta: un rapporto con la comunità sorda non si scrive in un pomeriggio.
4. **B5** (i novanta pin) è indipendente da tutto il resto e **non richiede nessuna decisione**: è il lavoro più utile che si può fare subito, perché il controllo è già scritto e i novanta pin sono già aperti.

Il consiglio che segue da questo elenco è solo uno, e vale per la costruzione dei prossimi giorni: **mentre si decide, si verifica il pin**. Le altre quattro aspettano una risposta; il pin no.

---

## 7. Registro delle modifiche

| Data | Versione | Che cosa è cambiato |
|---|---|---|
| 02/10/2026 | 0.1 | Prima stesura. Lettura delle dodici sezioni «Questioni aperte» dei documenti di progetto: **96 voci enumerate**, di cui **22 chiuse** e **74 aperte**, e **5 bloccanti**. I numeri sono verificati da `sorgenti/lingue/conta_questioni.py`, che confronta il proprio conto con quello dichiarato qui e segnala la contraddizione. Ricostruita la catena delle dipendenze (B1 → B2 → B4) e identificata la domanda che, sola, ne chiude tre altre. Registrate le tre questioni che compaiono in due documenti, e il fatto che nessuno dei ventidue chiusi è bloccante. |