---
titolo: Videogioco "I cinque duchi" — l'inventario: che cosa si tocca a ogni livello, che cosa dà in cambio, e che cosa il giocatore si porta via
versione: 0.2
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte del materiale: richiesta di Pietro del 03/10/2026 («fammi un recap dei vari elementi del gioco con cui si può interagire in ogni livello e una volta risposti tutti i quiz, cosa danno in cambio, che l'utente deve salvarsi e può consultarsi?»), con le regole già prese su oggetti di interazione, test di ingresso, premi e file di consegna
dati: dati/lingue/associazioni.json (v1, le 180 voci degli oggetti di interazione: trenta per lingua); dati/sequenza_tappe.json (v1, le novanta tappe degli anni 2-4 con la voce che si incontra); dati/ambienti_livelli.json (v1, i centocinquanta ambienti); dati/premi.json (da generare, dopo la cardinalità decisa: un premio per livello)
controllo: python3 sorgenti/verifica_inventario.py (I1-I5: gli elementi interattivi sono un elenco chiuso, ognuno dichiara che cosa dà e se è facoltativo, i quattro registri personali sono dichiarati e leggibili dal gioco, nessun elemento dà un vantaggio che non esista nel testo del livello, e la mappa degli scambi è completa in ogni sua cella)
documenti collegati: videogioco-5-duchi-gioco.md (v0.5, il ciclo della tappa), videogioco-5-duchi-meccaniche.md (v0.3, il file di consegna e i suoi tre ruoli), videogioco-5-duchi-lingue.md (v0.1, le sei lingue e i 900 livelli), videogioco-5-duchi-lingue-immagini.md (v0.1, le 180 voci), videogioco-5-duchi-ripassi.md (v0.1, i test di ingresso), videogioco-5-duchi-premi.md (v0.2, i premi e la salvadanaio), videogioco-5-duchi-sequenza.md (v0.1, le voci in fila), videogioco-5-duchi-pedagogia.md (v0.2), AGENTS.md
---

# L'inventario

## 0. Che cosa è questo documento, in una riga

È **la risposta alla domanda «a che cosa gioco?»**: sette cose con cui il giocatore interagisce a ogni livello, che cosa ciascuna dà in cambio, e le quattro cose che il giocatore si porta via quando chiude il gioco.

Il documento esiste perché quelle risposte erano sparse in sei file e nessuno le aveva messe in fila. Una mappa degli scambi che non c'è è la ragione per cui un gioco sembra più grande di quanto faccia.

## 1. I sette elementi, e che cosa danno

| # | elemento | che cosa è | che cosa dà in cambio | facoltativo? |
|---|---|---|---|---|
| **1** | **la voce** | la persona storica della tappa: Ötzi a Bolzano, Copernico a Frombork, Ambedkar a Delhi | il **nucleo**: l'argomento del livello, con la sua frase e il suo rimando | no |
| **2** | **l'oggetto di interazione** | una delle 180 voci: la pizza, il vino, i numeri romani, gli auspici, i proverbi ferraresi | il **passaggio facoltativo** dentro la lingua: il vocabolo, la forma, l'etimologia che l'oggetto porta con sé | **sì**, in tutti i 900 livelli |
| **3** | **il pin e la strada** | la posizione sulla carta e il mezzo del viaggio | la **distanza e il tempo**: quanto si è viaggiato davvero, in giorni | no |
| **4** | **il test di ingresso** | dieci domande sulle voci già superate, due o tre minuti | l'**elenco dei dieci nomi** con l'origine di ciascuno: che cosa sai e che cosa no | **sì** |
| **5** | **il richiamo all'origine** | il livello da cui una di quelle dieci cose era imparata, aperto lì dove si è | la possibilità di **rifare quel livello** e tornare indietro quando si vuole, senza perdere niente | sì, e non si può disattivare |
| **6** | **il premio** | un oggetto vero con tre righe di spiegazione | l'oggetto, che va nella **salvadanaio** | no, uno per livello |
| **7** | **la fascia bianca** | la striscia in cui il giocatore scrive a mano | la **previsione**: che cosa secondo lui succederà, e con quale incertezza | sì, ma è **dato personale** e non esce mai dal file |

**Cinque cose su sette sono facoltative**, e non per generosità: sono le cinque che il progetto può permettersi di rendere opzionali senza che il livello perda il suo nucleo. Il nucleo e la soglia non sono facoltativi, e i due elementi non facoltativi che non sono la voce sono il viaggio e il premio.

### 1.1 La differenza fra la voce e l'oggetto, che è quella che il giocatore sente

La voce è **la persona** e porta l'argomento; l'oggetto è **la cosa** e porta il pezzo di lingua. Sono due porte diverse e il gioco non le confonde: la prima apre il livello, la seconda ci passa dentro e si può saltare. Il gioco lo dice già (`associazioni.json`): *«l'oggetto di interazione è facoltativo in tutti i 900 livelli: se lo si salta, il livello resta valido»*.

### 1.2 Il test di ingresso non è un premio, ed è l'unico che «rende»

Degli sette elementi, il test di ingresso è l'unico che dà qualcosa che il giocatore non aveva e che non può comprare: **la consapevolezza di che cosa non sa, con i nomi**. Il premio dà un oggetto, il test dà un'informazione, e l'informazione è più utile dell'oggetto perché si può usare subito (`ripassi.md` §1).

## 2. Che cosa danno in cambio, in una tabella sola

Se il gioco è guardato come una sequenza di scambi, la tabella è questa, e ogni casella è un posto dove il progetto può sbagliare:

| | il giocatore dà | il gioco dà |
|---|---|---|
| alla voce | attenzione e una risposta | l'argomento del livello |
| all'oggetto | una scelta, cioè dice che cosa gli interessa | il pezzo di lingua che quell'oggetto porta |
| al viaggio | niente: il viaggio è automatico | la distanza e i giorni, che sono dati e non premi |
| al test | due o tre minuti e la risposta vera | i dieci nomi da ripassare |
| al richiamo | nulla: si può interrompere | il livetto rifatto, e il ritorno |
| al premio | la soglia raggiunta | un oggetto con tre righe che spiegano chi è e cosa ha cambiato |
| alla fascia | una frase scritta a mano | niente: la fascia è sua e resta sua |

**L'ultima riga è l'unica in cui il gioco non dà niente**, ed è voluta: la previsione del giocatore non viene valutata, commentata o confrontata. Il progetto vieta le risposte scritte e vieta che il gioco raccolga dati personali per fare profili.

## 3. Che cosa il giocatore deve salvare, e che cosa può consultare

Il salvataggio è **un file solo** (`meccaniche.md` §1), e quel file fa tre cose insieme: è il compito che consegna, è il report che il docente legge, ed è lo stato da cui il gioco riparte. Ma dentro quel file ci sono **quattro registri che sono del giocatore**, e sono la parte che nessuno deve poter alterare:

| registro | che cosa contiene | a che cosa serve | come si consulta |
|---|---|---|---|
| **la salvadanaio** | i premi, uno per livello superato, con le tre righe | il **catalogo personale** di ciò che il giocatore ha imparato | dalla schermata del livello, e dal file |
| **il quaderno dei segni** | per la LIS: **una scheda per livello**, con il segno che il livello ha insegnato e **la frase che il giocatore ha scritto lui** | la **memoria** della lingua, e l'unica prova che non si può copiare | dal gioco, sempre |
| **il registro dei ripassi** | ogni test di ingresso: le dieci domande, quante risposte giuste, il tempo, e da quale voce erano | il **progresso nella comprensione**, non nel punteggio | dal gioco, e dal file |
| **la fascia** | le previsioni scritte a mano | il **confronto con sé stesso** fra dieci anni | dal file, e dal gioco |

**La regola che tiene insieme i quattro**: il gioco deve poter rileggerli. Un registro che il gioco non sa rileggere non è un registro del giocatore, è un diario che si perde alla prima reinstallazione. E nessuno dei quattro contiene dati di altri studenti: non c'è classifica, non c'è confronto, non c'è nulla che descriva un compagno.

### 3.1 Il file di consegna, e che cosa non ci mette dentro

Il file contiene i quattro registri e i numeri del percorso. **Non** contiene: nessun dato di altri studenti, nessun risultato riconducibile a chi l'ha prodotto oltre il nome che il giocatore ha inserito, nessuna webcam, nessun riconoscimento del comportamento. Le previsioni nelle fasce sono **dati personali** e non vanno mai pubblicate in un repository (`meccaniche.md` §5).

## 4. Le cifre, che sono la parte onesta di questo documento

| | per anno | in cinque anni |
|---|---|---|
| voci incontrate (l'elemento 1) | 30 | 150 |
| oggetti di interazione (l'elemento 2) | 30 per lingua, sei lingue | 180 voci, apribili in ogni livello |
| test di ingresso possibili | uno per oggetto toccato | fino a 180 |
| **premi** (l'elemento 6) | **uno per livello**, meno l'informatica | **1050** (`premi.md` §4.0) |
| registri personali | quattro | quattro |

I **1050 premi** sono la cifra che rende questo documento pesante: sono la decisione di oggi (`premi.md` §4) e sono anche il motivo per cui la prova 3 dei premi — *non è già nella storia* — è la più difficile da soddisfare. Un premio per livello significa che **non si possono regalare gli stessi venti oggetti venti volte**, e il catalogo deve avere novanta fonti diverse.

## 5. Che cosa manca perché l'inventario sia completo

1. ~~**Il numero dei livelli trasversali**~~ **chiusa il 03/10/2026**: sono **zero** — il trasversale è un aggancio dentro i livelli, non un livello (`quadro-trasversale.md` §1.3) — e il conto è **1050**, non «circa 900»: la cifra vecchia contava i soli livelli linguistici e dimenticava i centocinquanta informatici.
2. **La mappa degli scambi in ogni sua cella**: le sette righe della tabella di §2 dicono che cosa dà ogni elemento, ma non c'è ancora un controllo che verifichi che ogni elemento dia davvero quello che promette. Le righe che oggi sarebbero false sono quelle del premio, perché il catalogo non esiste.
3. **Le fasce bianche nel ciclo della tappa**: sono dichiarate da `gioco.md`, ma non hanno una schermata né un posto nell'inventario delle schermate. Se sono la previsione del giocatore, sono il quinto elemento che dà qualcosa.

## 6. Registro delle modifiche

- **v0.1 (03/10/2026)**: prima stesione, e nasce da una domanda che nessun documento aveva raccolto: **a che cosa gioco, che cosa ne ricavo, e che cosa mi porto via**. Sette elementi interattivi, ognuno con che cosa dà e se è facoltativo; la tabella degli scambi; i quattro registri personali e la regola che il gioco deve poter rileggerli; e le cifre, con i **circa 900 premi** che la decisione di oggi rende esatti e che la prova «non è già nella storia» rende difficili. La riga vuota è quella delle fasce: **è l'unico scambio in cui il gioco non dà niente**, ed è l'unico in cui il giocatore scrive.
- **v0.2 (03/10/2026)**: **il numero dei premi è chiuso, ed era sbagliato.** I livelli sono **1050**, non «circa 900»: i quattro ambiti trasversali non aggiungono livelli (`quadro-trasversale.md` §1.3, che chiude anche la riga `osservazione e attenzione` che due documenti davano per assente) e la cifra precedente contava i soli livelli linguistici. Le due cose da fare scendono a una: scrivere il catalogo dei premi.
