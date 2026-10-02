---
titolo: Videogioco "I cinque duchi" — audit delle questioni aperte: la lista operativa
versione: 0.2
data: 2026-10-02
autore: Pietro Fabbri (con Claude)
fonte: lettura di tutti i quindici documenti di progetto, verificata da sorgenti/lingue/conta_questioni.py
documenti collegati: videogioco-5-duchi-lingue.md (v0.1), videogioco-5-duchi-lingue-immagini.md (v0.1), videogioco-5-duchi-percorsi.md (v0.1), videogioco-5-duchi-fonti-visive.md (v0.1), videogioco-5-duchi-furioso.md (v0.4), videogioco-5-duchi-luoghi.md (v0.3), videogioco-5-duchi-mappe.md (v0.4), videogioco-5-duchi-anno5-mondo.md (v0.4), videogioco-5-duchi-anno4-mondo.md (v0.5), videogioco-5-duchi-anno3-europa.md (v0.4), videogioco-5-duchi-anno2-penisola.md (v0.2), videogioco-5-duchi-anno1-ferrara.md (v0.3), videogioco-5-duchi-curricolo.md (v0.1), videogioco-5-duchi-gioco.md (v0.5), videogioco-5-duchi-meccaniche.md (v0.3), AGENTS.md
---

# Audit delle questioni aperte: la lista

## 0. Che cosa c'è in questo documento

La **lista operativa** di tutte le questioni aperte del progetto: che cosa si deve decidere, che cosa si può fare, e **chi decide**.

Ogni voce ha quattro cose: la **domanda** in una riga, il **pro**, il **contro**, la **valutazione** (che è la mia, e come tale si può confutare), e la **responsabilità** (chi decide: Pietro, il progetto, una comunità, un'istituzione).

Il documento è verificato da `sorgenti/lingue/conta_questioni.py`, che confronta il proprio conto con i numeri scritti qui.

## 1. Il conto

| | |
|---|---|
| Documenti con una sezione «Questioni aperte» | **15** |
| Voci enumerate | **114** |
| **Chiuse** | **22** |
| **Aperte** | **92** |
| Di cui bloccanti | cinque |
| Di cui importanti (cambiano il gioco) | diciannove |
| Di cui minori (si possono rimandare) | le altre |

**Il criterio**, dichiarato perché un numero senza criterio non è un dato. Una **voce** è un punto numerato, un `### Q1` o una riga di tabella della sezione «Questioni aperte». Una voce è **chiusa** se porta la marcatura nella sua **prima riga** — «chiusa», «risolto», «ratificata», «confermata» — e non in tutto il corpo, perché una voce aperta spiega dentro il corpo quale parte è stata chiusa.

**Una voce non è sempre una domanda.** In `lingue.md` Q3 ci sono due sotto-voci dentro una sola domanda. Le **114 voci non sono 114 domande**.

**Nessuna delle ventidue chiuse è bloccante**: le decisioni prese hanno tolto lavoro, non lo hanno aggiunto.

---

## 2. Le cinque bloccanti

Sono le uniche che fermano qualcosa. Ognuna ha una scheda.

---

### B1 · I livelli linguistici e quelli informatici sono lo stesso livello o due?

`lingue.md` §7 Q1 · **pro**: due sistemi paralleli nella stessa tappa dà 32 livelli per tappa ed è l'unica forma in cui i due percorsi si incontrano. **contro**: rende ogni tappa enorme, e le trenta tappe coprirebbero 150 informatici più 900 linguistici in un'ora di lezione; l'alternativa «lingue dentro l'informatica» cancella le 900 unità di gioco. **valutazione**: è la decisione con la conseguenza più grande e la meno reversibile; va presa con la stima delle schermate per tappa, che nessuno ha fatto. **responsabilità**: Pietro. **blocca**: i dati dei livelli, la scelta delle immagini, tutte le tappe linguistiche, i testi autentici, la progressione.

### B2 · Le trenta voci di ogni oggetto sono confermate?

`lingue.md` §7 Q2 e `lingue-immagini.md` §6.2 Q2 · **pro**: le voci esistono e sono lavorate; confermarle sblocca 1120 candidati già cercati. **contro**: per il ferrarese non sono un elenco ma **campi da rilevare**, e la fonte non è stabilita (chi raccoglie, con che metodo, con quale consenso); un proverbo scritto a tavolino è un proverbo italiano in maschera. **valutazione**: va chiusa **prima** di scegliere le immagini, altrimenti si rifà la ricerca; per le altre cinque lingue è una revisione di trenta voci, per il ferrarese è un progetto. **responsabilità**: Pietro, e per il ferrarese **anche chi raccoglierà i proverbi**. **blocca**: B4, e le tappe facoltative degli oggetti.

### B3 · La LIS nel gioco: chi insegna, e con quali materiali?

`lingue.md` §7 Q4 · **pro**: la lingua dei segni è la scelta che rende il progetto serio; le trenta voci ci sono. **contro**: non si scrive a tavolino; servono collaborazione con la comunità sorda, video, trascrizioni, competenze che il progetto non dichiara di avere. **valutazione**: la più lenta di tutte, perché un rapporto con la comunità non si scrive in un pomeriggio; è l'unica che non si può sblocare con una decisione. **responsabilità**: Pietro **e la comunità sorda** — non è una decisione che il progetto può prendere da solo, e questa è la ragione per cui la domanda è bloccante e non importante. **blocca**: i trenta livelli LIS.

### B4 · Chi guarda le 1120 immagini degli oggetti?

`lingue-immagini.md` §6.2 Q1 · **pro**: guardarle è lavoro di ore, non di minuti; i candidati sono già tutti e hanno licenza libera. **contro**: nessuna è stata guardata; 67 su 146 sono a rischio (G7). **valutazione**: l'opzione realistica è **un campione** — i 146 migliori per voce — dichiarando che un campione non attesta il resto; le tre opzioni sono guardarle tutte, guardarle un campione, o non guardarle. **responsabilità**: io (l'IA) o Pietro; la decisione di *quanto* guardare è di Pietro. **blocca**: le tappe facoltative degli oggetti, e nient'altro.

### B5 · I novanta pin degli anni 2, 3 e 4 sono verificati?

`mappe.md` §10 · **pro**: il controllo esiste (`punto_in_poligono.py`), le coordinate sono già scritte a mano; è il controllo che vale più di qualunque altro. **contro**: non è una domanda, è un lavoro; non c'è contro, e per questo è l'unica bloccante che non aspetta nessuna decisione. **valutazione**: **va fatto subito, mentre si decide tutto il resto** — è l'unica delle cinque che non ha una risposta da aspettare. **responsabilità**: il progetto (l'IA), non Pietro. **blocca**: le tappe degli anni 2-4 che dicono «a Torino» senza averlo verificato.

---

## 3. Le diciannove importanti

Quelle che, se risposte male, cambiano il gioco. In ordine di peso.

| # | Domanda | Pro | Contro | Valutazione | Chi decide |
|---|---|---|---|---|---|
| I1 | **Il percorso del duca è l'ordine delle tappe o un giro a parte?** (`percorsi.md` Q1) | Il giro copre tutta la mappa e dimezza il viaggio (−31/−49/−43/−58%) | Richiede di cambiare il modo in cui la mappa si disegna: due sequenze invece di una | Il giro: è ciò che rende la mappa un percorso e non una distribuzione di punti | Pietro |
| I2 | **La tavolozza va prodotta?** (`fonti-visive.md` Q1) | Senza, i tre sistemi di immagini non concordano e il gioco è un mosaico | Richiede una decisione di gusto, che è sua, non del progetto | Va prodotta, e la scelta è dichiarare i colori di ogni fonte (coerente con le tre regole già prese su etichette e proporzioni) | Pietro |
| I3 | **Le sagome degli edifici si costruiscono?** (`fonti-visive.md` Q2) | OSM è autorizzata da tre giorni; il gioco non può disegnare città senza sagome | Il file è il più grosso dei cinque buchi, e senza di esso si disegnano volumi neutri | Sì, ma non è la prima cosa: prima la tavolozza, che è più piccola e più urgente | Il progetto |
| I4 | **Il fondo di Ferrara si costruisce?** (`fonti-visive.md` Q3) | L'anno 1 è quello in cui la copertura è gratuita e la mappa è piccola | Serve il perimetro ufficiale delle mura e le sagome degli edifici (che sono I3) | Sì, dopo I3: senza le sagome il fondo non si disegna | Il progetto |
| I5 | **Che cosa è un «testo autentico» nelle sei lingue?** (`lingue.md` Q3) | Il progetto vieta i testi inventati; per il greco la regola è chiara | Per il ferrarese è una trascrizione di parlante, e lì si aprono consenso e varietà | Serve una regola scritta **prima** di registrare chiunque, non dopo | Pietro, e chi parla per il ferrarese |
| I6 | **Il greco moderno ha una linea propria?** (`lingue.md` Q5) | Tremila anni in tre anni di percorso rischiano di essere un elenco di argomenti | Aggiunge una settima linea a un sistema già largo | Una linea dentro i blocchi 4 e 5, come l'atlante per gli anni 3 e 4 | Pietro |
| I7 | **Che cosa succede se il giocatore non sa l'italiano?** (`lingue.md` Q7) | Il gioco è in italiano, e il percorso presuppone che si perdano punti sui livelli d'italiano | Una soglia diversa per chi l'italiano non ce l'ha è una scelta che va dichiarata, non fatta implicitamente | Una soglia minima per i livelli d'italiano, la stessa soglia alta per chi ce l'ha già; è la regola «nessuna competenza in ingresso» applicata alle lingue | Pietro |
| I8 | **Quanti esercizi fanno le trenta voci?** (`lingue.md` Q8) | Con pool da 20 per gradino sono 3 600 esercizi: è il lavoro più grande del progetto | Se le voci fossero venti, il conto calerebbe di un terzo | Il conto va detto prima di promettere; 3 600 è tanto ma il gioco è tanto | Pietro |
| I9 | **Le fonti del latino e del greco vanno cercate altrove?** (`lingue-immagini.md` Q3) | Il controllo G7 dice che 27 voci latine su 28 hanno solo proposte scoperte per caso | Commons ha le immagini degli oggetti, non le fonti filologiche: servono EDCS, EDR, biblioteche digitali | Sì: per il latino Commons è il posto sbagliato, e va detto | Pietro |
| I10 | **Le immagini servono solo per le facoltative?** (`lingue-immagini.md` Q5) | Le tappe sui testi autentici hanno bisogno di immagini diverse (la pagina di Cesare, non una coppa) | Sono almeno 900 immagini, e nessuna è stata cercata | Sì, e va detto subito: è il buco più grande dopo le sagome | Il progetto |
| I11 | **Le Nuove Indicazioni 2026 vanno acquisite?** (`curricolo.md`) | Sono il riferimento normativo del liceo scientifico | Il fascicolo non è stato acquisito e il §6 è rifatto sul vecchio | Prima di costruire il curricolo, non prima del gioco: è una settimana di lavoro | Pietro |
| I12 | **Quanto dura un livello?** (`curricolo.md`) | Ogni livello deve durare da 5 minuti a qualche ora; senza stima non si sa se 150 livelli stanno in 5 anni | La stima dipende dal prototipo, che non c'è | Stimare sul primo prototipo, non prima | Il progetto |
| I13 | **Il 1945 non è una tappa.** (`anno5-mondo.md` §13) | Il materiale ci mette Roosevelt, Cassin, Lauterpacht, e i livelli non li chiedono | Sostituirlo significa scegliere un'altra tappa che i livelli non coprono | Va deciso con il buco della biologia (I14), e sono lo stesso problema | Pietro |
| I14 | **Il buco della biologia nel quinto anno.** (`anno5-mondo.md` §13) | Il materiale dedica quindici voci a medicina, vaccini, DNA e nessun livello le copre | Levare voci dal materiale è una decisione sua, non del progetto | È il buco tematico più grosso del quinto anno | Pietro |
| I15 | **La tratta e l'imperialismo nell'anno 3.** (`anno3-europa.md` §13) | È un buco reale: nessun personaggio obbligatorio porta l'Europa fuori dall'Europa | Aggiungere una scheda di atlante che i livelli non chiedono, o dichiarare il limite | Dichiarare il limite è più onesto; una scheda di atlante sul colonialismo è giusta ma è un atlante | Pietro |
| I16 | **Leonardo in due anni.** (`anno3-europa.md` §13) | È il caso più bello del percorso: la stessa persona è «il linguaggio delle figure» e poi «la scomposizione del metodo» | Viola la regola dei ritorni che il progetto si è data | Si tiene: il ritorno forte vale più della regola, e la regola va corretta con l'eccezione | Pietro |
| I17 | **Il formato del file di consegna.** (`meccaniche.md`) | `.txt` è la proposta, ed è leggibile ovunque | Il PDF è più sicuro contro le manomissioni | `.txt` con firma, e la firma è ciò che rende la consegna verificabile | Pietro |
| I18 | **Il gioco è un modulo della piattaforma gamificata o un prodotto a sé?** (`meccaniche.md`, `curricolo.md`) | Le due scelte danno requisiti diversi su privacy, punteggio, consegna | Rimandarla non blocca niente subito | Prodotto a sé, con i requisiti della piattaforma come caso particolare | Pietro |
| I19 | **I colori dei fondi geografici.** (`fonti-visive.md` Q4) | Oggi stanno nel codice, dove nessuno li legge | Nessun contrario | In un file, come tutti gli altri; costa mezz'ora | Il progetto |

---

## 4. Le altre, in sintesi

Le **restanti**: minori, o già decise nella sostanza e che aspettano solo l'esecuzione. Chi decide è Pietro quasi sempre, e dove è il progetto è perché non è una domanda ma un lavoro.

### Sistema linguistico (restano 8)

| Domanda | Chi decide |
|---|---|
| Il confronto fra le sei lingue è obbligatorio o a rotazione? Il calcolo dà il 17% del totale | Pietro |
| I confronti filologici sono vincolanti, e come li si controlla | Pietro |
| Le trenta voci ferraresi: che tappa hanno, se non hanno immagine | Pietro |
| Chi ridimensiona le immagini scelte a 96×72, e quando | Il progetto |
| Il livello 30 di ogni lingua è un compito: che cosa produce, e con quale criterio di superamento | Pietro |

### Percorsi (restano 5)

| Domanda | Chi decide |
|---|---|
| Il giro si chiude a Ferrara? Costo 10-101 giorni di viaggio che il gioco non fa pagare | Pietro |
| Il mezzo cambia dentro l'anno? Nel quarto anno è il mezzo di chi porta il documento | Pietro |
| Le facoltative continentali si aprono sul ritorno | Pietro |
| I buchi continentali degli anni 3, 4 e 5 | Pietro |
| Il tempo di viaggio è un esercizio giocabile o una dichiarazione | Pietro |

### Fonti visive (restano 2)

| Domanda | Chi decide |
|---|---|
| Chi guarda i 125 candidati delle fonti visive | Io o Pietro |
| Le due facoltative continentali dell'anno 4 si aprono sul ritorno | Pietro |

### Anno 1 (7) e curricolo (5)

| Domanda | Chi decide |
|---|---|
| Il narratore: che ruolo hanno gli altri duchi nel percorso | Pietro |
| Renzo Ravenna e le 20 schede aggiunte: approvare o scartare | Pietro |
| La mappa digitale di Ferrara che Pietro deve fornire | Pietro |
| Le fonti primarie, scheda per scheda | Il progetto |
| La verifica storica complessiva, con un collega o con l'Archivio di Stato | Pietro **e un istituto** |
| Il secondo linguaggio tipizzato (C++ o Java) al 3º o 4º anno | Pietro |
| Il rapporto con la piattaforma gamificata (vedi I18) | Pietro |
| L'allineamento interdisciplinare con le programmazioni reali di classe | Pietro **e i colleghi** |
| Le fonti storiche del §4 | Il progetto |

### Anno 2 (8)

| Domanda | Chi decide |
|---|---|
| La carta intera alla fine dell'anno: si aprono tutti gli strati insieme | Pietro |
| Tre collettivi su trenta tappe: alternativa (a) o (b) | Pietro |
| Il bilancio degli agganci: 13 forti e 17 medi | Pietro |
| La colonna stratigrafica sempre visibile a schermo | Pietro |
| Il materiale dal 1500 in poi | Pietro |
| Le persone viventi (Cristoforetti) | Pietro |
| Le fonti del materiale | Il progetto |
| Le «visioni» dell'anno 1 nell'anno 2 | Pietro |

### Anno 3 (restano 7), anno 4 (4), anno 5 (restano 7)

| Domanda | Chi decide |
|---|---|
| Il bilancio degli agganci: 21 forti, 9 medi, e tre forse troppo forti | Pietro |
| Persone viventi (von der Leyen, Merkel, Macron): solo emblemi | Pietro |
| Le sei aggiunte (Josquin, Bellini, Dürer, Manuzio, Caxton, Levi) | Pietro |
| La corte come unico luogo percorribile: la alternativa è il visitatore-inviato | Pietro |
| La regola di AGENTS.md sul duca guida dal terzo anno (già scritta, va tenuta allineata) | Il progetto |
| I tre agganci «forti» da rivedere dell'anno 4 | Pietro |
| La tappa 4-10 e l'incendio dell'archivio | Pietro |
| Chi è il protagonista del quinto anno: dentro il *Furioso*, con la regola dei due strati (parzialmente risolta) | Pietro |
| Il quinto anno e l'anno 3: come si dividono il Novecento | Pietro |
| I facoltativi che il gioco non può mettere in tabella | Il progetto |
| I quattro agganci da rivedere del quinto anno | Pietro |
| Le previsioni con la data: si rileggono fra dieci anni, e con quale formato | Pietro |
| Il posto di F11 nel registro del gioco | Pietro |

### Luoghi (2), mappe (3), *Furioso* (3), gioco (5), meccaniche (5)

| Domanda | Chi decide |
|---|---|
| Le undici facoltative continentali: proposte e non schede | Pietro |
| Il tipo di legame dei ventisei pin del quinto anno | Pietro |
| Il vincolo di 20 000 abitanti per mostrare una città | Pietro |
| Le trenta zone percorribili: tutte, o solo dove il luogo è lo spazio del gioco | Pietro |
| Il file delle regioni amministrative: intero o ridotto | Il progetto |
| I tredici filoni mostrati e i dodici dichiarati | Il progetto |
| Le ventisei stanze senza coordinata: la regola che le dichiara | Pietro |
| I motti e i dialoghi delle trenta tappe | Pietro |
| Confermare la tappa 1-30 (P93, la città) | Pietro |
| Verificare che v86 e Pyodide funzionino sui computer del laboratorio e sui Chromebook | Il progetto **e il laboratorio** |
| Per 1-25 e 1-26: strumento nel gioco, file caricato, o entrambi | Pietro |
| I pesi e le soglie del meccaniche §2.3, calibrati sul prototipo | Il progetto |
| Quanti eventi di dettaglio conservare nel codice di ripresa | Il progetto |
| Lo strumento del docente: subito o dopo il prototipo | Pietro |
| Safe Exam Browser e la proposta al regolamento d'istituto sui dispositivi indossabili | Pietro **e l'istituto** |
| La specifica della modalità accessibile | Il progetto **e il progetto di accessibilità del gioco** |

---

## 5. Le domande che sono due

Tre questioni compaiono in due documenti, e una è la stessa identica:

| La domanda | Dove | Nota |
|---|---|---|
| Le trenta voci sono confermate | `lingue.md` Q2 = `lingue-immagini.md` Q2 | Una risposta sola chiude due |
| Una linea che attraversa gli anni senza essere una tappa | `lingue.md` Q5 = `anno5-mondo.md` | Stessa idea, risposta data per gli anni 3-4 e non per le lingue antiche |
| I codici `Q` dei personaggi | `anno3` Q6 = `anno4` Q5 = `anno5` Q4 | **L'unica ridondanza che funziona**: confermati in tutti e tre i documenti e concordanti. È la prova che funziona quando qualcuno la controlla |

---

## 6. La sequenza che chiude tutto

Le cinque bloccanti hanno una catena sola.

**B2** (voci confermate) viene **prima** di **B4** (chi guarda le immagini): cercare le immagini prima di aver confermato le voci è lavoro da rifare. **B1** (livelli linguistici o informatici) decide quanti tipi di tappa esistono, e quindi decide se B4 ha senso come domanda.

La catena è: **B1 → B2 → B4**. **B3** (la LIS) è indipendente e parte in parallelo, ed è la più lenta. **B5** (i novanta pin) non aspetta nessuna e va fatto adesso.

E la regola che segue, la sola che conta per il lavoro di oggi:

> **Mentre si decide, si verifica il pin.** Le altre quattro aspettano una risposta; quella no.

---

## 7. Registro delle modifiche

| Data | Versione | Che cosa è cambiato |
|---|---|---|
| 02/10/2026 | 0.1 | Prima stesura. Le dodici sezioni «Questioni aperte» allora esistenti, **96 voci**, 22 chiuse e 74 aperte, cinque bloccanti, e la catena delle dipendenze. |
| 02/10/2026 | 0.2 | La **lista operativa**. Il contatore è stato corretto perché vedeva tredici documenti su quindici e sbagliava il conto: ora sono **114 voci**, 22 chiuse e **92 aperte**, con i documenti nuovi (`lingue.md`, `lingue-immagini.md`, `percorsi.md`, `fonti-visive.md`) dentro. Ogni bloccante e ogni importante ha **pro, contro, valutazione e responsabilità**; le altre settantatre sono in sintesi con chi decide. Registrata una doppia domanda (`lingue.md` Q5 = `anno5-mondo.md`) e la catena B1 → B2 → B4. |