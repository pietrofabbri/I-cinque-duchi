---
titolo: Videogioco "I cinque duchi" — i test di ingresso: dieci domande, due minuti, e il poter tornare indietro
versione: 0.1
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte del materiale: richiesta di Pietro del 03/10/2026 («ogni volta che si interagisce con personaggio/emblema/monumento/cibo ecc ci siano max 10 domande su tutto ciò che è stato affrontato fino ad allora, prese randomicamente, su quella disciplina, idealmente max 2 minuti, per validare il ripasso; se tenti diverse volte puoi temporaneamente evocare il personaggio o l'oggetto da cui hai imparato quelle cose per rifare il livello, che puoi interrompere quando vuoi per tornare al momento presente; per gli anni dal secondo in poi il tempo massimo sale a 3 minuti, perché devi poter verificare in un minuto anche ciò che è stato fatto negli anni precedenti»), con le regole già prese su etichette, oggetti di interazione e vuoti dichiarati
dati: dati/lingue/associazioni.json (v1, le 180 voci: trenta per lingua, sei lingue); dati/lingue/immagini_oggetti.json (le 180 schede con etichetta e licenza); dati/ripassi.json (v1, le banche di domande e le finestre di tempo: ancora da generare, perché i livelli non esistono)
controllo: python3 sorgenti/verifica_ripassi.py (le sette regole R1-R7: dieci domande, due o tre minuti, campionamento casuale sulle sole voci superate, il richiamo all'origine, l'evocazione interruptibile, nessuna penalità, e l'etichetta di disciplina che rende leggibile la scelta)
documenti collegati: videogioco-5-duchi-lingue.md (v0.1, i 900 livelli), videogioco-5-duchi-lingue-immagini.md (v0.1, le 180 voci e le nove etichette), videogioco-5-duchi-schema-livelli.md (v1.1, i 150 livelli di informatica e la loro soglia minima), videogioco-5-duchi-esercizi.md (v0.1, i pool e la regola «nessuna risposta scritta»), videogioco-5-duchi-furioso.md (v0.6, la regola dei due strati, da cui prende il nome il richiamo all'origine), videogioco-5-duchi-meccaniche.md (v0.3, il file di consegna dove il risultato del test viene scritto), videogioco-5-duchi-fonti-visive.md (v0.3), AGENTS.md
---

# I test di ingresso

## 0. Che cosa sono, in una riga

Sono **dieci domande su dieci minuti della tua vita**, che il gioco ti chiede quando tocchi una persona, un emblema, un monumento, un cibo o un oggetto: **non ti dà niente di nuovo, ti fa vedere che cosa sai già**. E se sbagli, non ti lascia lì: ti porta indietro, da dove hai imparato, e poi ti riporta esattamente dove eri.

La regola è tutta qui, ed è la stessa del capitolo 2 del *Furioso*: **il punto dove il gioco si ferma non si muove, e dentro ci si mette un livello.**

## 1. Perché il test esiste, e perché non è un esame

Il gioco ha una regola che vale da sempre: **nessuna competenza in ingresso presupposta** (`schema-livelli.md` §2). Il rovescio di questa regola è un problema: se il gioco non presume niente, non può neppure dare per saputo niente. Un ragazzo che ha fatto i trenta livelli di latino nel primo anno e ne ha saltati sette il terzo, alla fine del quinto anno si trova con una mappa piena di cose che ha incontrato e non sa.

Il test di ingresso è la risposta più economica: non aggiunge contenuti, non aggiunge livelli, e usa **esattamente le istanze che il giocatore ha già visto**. Dieci domande sono un campione, non un esame: servono a dare un **dato reale** — «di questi dieci, sei li sai» — non un verdetto.

**Il vantaggio deve essere tangibile e non promesso** (`pedagogia.md` §1). Il vantaggio qui è letterale: dopo il test il giocatore sa **quali** dieci cose non sa, e ognuna di esse ha un nome e un luogo. Senza il test, quella informazione non esiste per lui.

## 2. Le sette regole

### R1. Dieci domande, mai di più, mai di meno

Dieci è un numero scelto per una ragione precisa: **è il numero che entra in due minuti**. Dieci domande in 120 secondi sono dodici secondi l'una; in 180 sono diciotto. Sotto i dieci secondi per domanda il ragazzo non legge, e sopra i venti sta a pensarci invece di rispondere: il test deve accertare che **sa**, non che **è veloce**.

Il numero è dichiarato e non si negozia: se la banca non ha dieci domande disponibili, il test **non parte** e il gioco lo dice («non hai ancora abbastanza di questa disciplina»). Non si allunga, non si accorcia: un test di sei domande non è la versione corta di uno di dieci, è un'altra cosa.

### R2. Due minuti nel primo anno, tre dal secondo in poi

| Anno | Tempo massimo | Perché |
|---|---|---|
| **1** | **120 secondi** | nel primo anno la banca è piccola e le voci sono tutte recenti: il rischio è di dimenticare, non di non aver mai visto |
| **2, 3, 4, 5** | **180 secondi** | dal secondo anno il campione può pesare su **tutti** gli anni precedenti, e una domanda del primo anno fra le dieci costa qualche secondi in più di richiedere il contesto |

La conseguenza è aritmetica e va detta: **un terzo del test del quinto anno può essere formato da domande di quattro anni prima**, pescate a caso. È il punto della regola, non un difetto: se il campione pesasse solo sull'anno in corso, il test non verificherebbe niente che il percorso non abbia già verificato.

### R3. Il campione si pesca sulle voci **superate**, non su quelle viste

È la regola che rende il test giusto, e la differenza è tutto: il sorteggio avviene **fra i livelli per i quali il giocatore ha raggiunto la soglia minima**. Una voce che il giocatore ha incontrato e non ha superato **non entra nel sorteggio**: non si può chiedere a caso se ci si ricorda una cosa che non si è imparata.

Il campo che il gioco deve già avere per fare questo è la **soglia minima** di `schema-livelli.md` §1 applicata ai 900 livelli linguistici: superato sì o no, e in data. Senza quel campo il test non è implementabile, ed è la ragione per cui questa regola è la prima da costruire.

### R4. Ogni domanda porta con sé **da dove viene**, e il richiamo è sempre visibile

Ciascuna delle dieci domande sa **l'oggetto, il personaggio, l'epigrafe o il cibo da cui è uscita** — cioè la sua **origine**. È il punto in cui il gioco si distingue da una verifica: la schermata finale non è «6/10», è **la lista delle dieci domande con accanto il nome di ciò da cui impararle**.

Questa è la **regola dei due strati** (`furioso.md` §2.2) applicata al ripasso: come nel quinto anno il **pin** resta reale e verificato e la **stanza** è quella del filone, così il **luogo** in cui il giocatore si trova non si muove mai e il **livello richiamato** è un secondo strato.

### R5. Si può tentare più volte, e si torna sempre indietro

Se il risultato non piace, il giocatore può **evocare** la persona, l'emblema, il monumento o il cibo da cui quella cosa aveva imparato, e **rifare quel livello**. Il livello evocato:

- **si interrompe quando vuole**, con un «torna indietro» sempre visibile in alto a destra, non nascosto in un menu;
- **non toglie niente**: nessun punteggio perso, nessuna soglia che scende, nessuna progressione che si interrompe. Il ritorno è immediato e senza annunci;
- **non è un salto sulla mappa**: il duca non torna a Atene se è a Ferrara. Il livello si apre **dove il giocatore è**, come una pagina sopra la pagina.

L'ultima delle tre è la più importante: è la differenza fra un ripasso e un teletrasporto, e il progetto conosce già la regola che vieta il teletrasporto (`luoghi.md` §4.7).

### R6. Il tempo è un dato, non una multa

Il countdown è **visibile** e il tempo impiegato viene **registrato** nel file di consegna, insieme al risultato. Ma il tempo **non toglie punti** e non blocca nulla: un ragazzo che risponde in due minuti e quaranta non ha perso niente, ha risposto in due minuti e quaranta.

È la stessa scelta di `meccaniche.md` §2.3, dove il tempo compare fra gli **indicatori da guardare** e non fra le sanzioni, e vale anche per la coerenza dei passaggi: il punteggio misura il processo.

### R7. Il punto di interazione **dichiara la disciplina**, prima che il giocatore lo tocchi

Il giocatore deve poter scegliere il percorso **a occhio**, non per tentativi. Ogni punto di interazione — le 180 voci degli oggetti, i personaggi, gli emblemi, i monumenti — porta **un'etichetta di disciplina** visibile **prima** dell'interazione, e tutti i test sono **facoltativi**.

Un'etichetta sola, testo, e non un codice colore da decodificare: le discipline sono **sei lingue più i quattro ambiti trasversali** (`quadro-trasversale.md` §1) e il giocatore le riconosce dal nome. Il colore, quando serve, è quello che la voce ha già nella tavolozza: **nessun colore nuovo**.

Le 180 voci hanno già un sistema di etichette (`lingue-immagini.md` §3): l'etichetta di disciplina è una **vocedici** della stessa famiglia, e le due non si confondono perché una descrive **l'immagine** e l'altra dice **a che cosa porta l'interazione**.

## 3. Il flusso, in cinque schermate

| # | schermata | che cosa contiene | tempo |
|---|---|---|---|
| 1 | **Il punto** | il nome della disciplina, «facoltativo», e il numero di voci già superate | — |
| 2 | **Le dieci domande** | una alla volta, con il resto delle nove in fila in basso, così il giocatore vede sempre quanto ne manca | countdown visibile |
| 3 | **Il conto** | **non** un giudizio: la lista delle dieci, con accanto **da dove** si impara ciascuna, e il tempo impiegato | — |
| 4 | **L'evocazione** | «rivedi il livello» su ciascuna voce; si apre **dove si è**, e si interrompe quando si vuole | — |
| 5 | **Il ritorno** | si torna al punto di interazione, con la stessa frase e la stessa luce di prima | immediato |

La schermata 5 è l'unica che non ha un numero: **il ritorno non è una schermata**, è l'assenza di una schermata. Il gioco che si interrompe per mostrare un ringraziamento è un gioco che ha deciso di essere disturbato.

## 4. Che cosa non è questo test

- **non è la soglia minima dei 150 livelli di informatica**: quelli hanno già la loro soglia (`schema-livelli.md` §1) e la loro prova di corte ogni dieci livelli. Il test di ingresso nasce per le **sei lingue e i quattro ambiti trasversali**, che non hanno ancora nessuna soglia dichiarata;
- **non è una verifica**: non entra nel curriculum, non ha voto, non viene confrontato fra compagni. Un confronto pubblico dei punteggi è l'opposto di ciò che il progetto dichiara su privacy e integrità (`meccaniche.md` §2.4);
- **non aggiunge contenuti**: dieci domande su cose già viste. Se per un domanda serve un contenuto nuovo, **quel livello non è pronto** e il problema è del livello, non del test.

## 5. Le domande aperte

1. **Il formato della domanda.** Il progetto vieta le risposte scritte (`esercizi.md`), e una domanda a scelta multipla da ricordare è più facile di una domanda che richiede di produrre: il test potrebbe diventare un esame di riconoscimento, cioè di niente. Le alternative sono il riordino, il collegamento, il «quale di questi è l'epigrafe di…», che sono tutte risposte **da costruire**. È una decisione di Pietro.
2. **Le 180 voci sono trenta per lingua, ma i livelli sono trenta per lingua per anno**: le stesse trenta voci si attraversano cinque volte, ognuna più in profondità. La banca deve quindi contenere **900 voci di livello**, non 180: il campione è sul livello, non sull'oggetto. La relazione fra le due cose va scritta nei dati.
3. **I quattro ambiti trasversali** (diritto, etica, filosofia, psicologia) non hanno ancore oggettuali come le 180 voci: non si sa ancora su quali oggetti si tocchi per fare un test di filosofia. Va deciso se il test esiste anche per loro e con quali punti.

## 6. Registro delle modifiche

- **v0.1 (03/10/2026)**: prima stesione, e nasce da una richiesta di Pietro che aveva tutte le cifre già dentro. Le sette regole sono R1-R7 e coprono i tre numeri che lui ha dato (dieci domande, due minuti, tre minuti dal secondo anno), la scelta casuale, la possibilità di tentare più volte, l'evocazione di chi ha insegnato e la sua interruzione, e l'obbligo di rendere visibile la disciplina al punto di interazione. La regola che il gioco non mette via ciò che il testo dice con quattro parole: **si torna sempre indietro, e il ritorno non è una schermata**.