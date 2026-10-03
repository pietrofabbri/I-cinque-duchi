---
titolo: Videogioco "I cinque duchi" — I filoni dell'Orlando furioso: i luoghi del quinto anno e le citazioni delle trenta tappe
versione: 0.6
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
revisioni: v0.1 (testo e trenta citazioni); v0.2 (controllo di coerenza del 02/10/2026: tre citazioni erano nel filone sbagliato, due tappe confinanti citavano ottave adiacenti, e le cifre del riscontro sono state ricalcolate); v0.3 (seconda tornata dello stesso controllo: un legame `I` posto su un luogo che esiste, l'elenco degli inesistenti dichiarato nei dati, la tabella delle verifiche riordinata e due rimandi corretti); v0.4 (le sedici decisioni di Pietro del 02/10/2026 applicate: regola dei due strati ratificata, `F8` e `F9` fatte sul testo, il tipo `N` di non luogo, `F11` come tappa facoltativa, il giocatore dentro il *Furioso*, l'Africa riscritta, l'edizione spiegata in modo semplice); v0.5 (la Q6.1 chiusa: `F11` dichiarato filone **non assegnato**, cioè stanza aperta da un'altra, la decisione scritta nei dati e la verifica F16 che la tiene ferma); v0.6 (03/10/2026: la Q6.2 chiusa in §4.12, nessuna stanza ha un disegno proprio, quattro regole e il tempo di Pietro a zero)
fonte del materiale: la richiesta di Pietro (02/10/2026) — «sulla base dell'Orlando furioso dobbiamo creare i vari luoghi, cercando di ricalcare il più possibile i filoni della vicenda; devono esserci, in ogni livello, delle brevi citazioni del poema con parafrasi interattiva, intuitiva, emozionale, breve che diano senso alla trama ariostesca del Furioso» — e il testo dell'Orlando furioso edizione 1928 (Biblioteca BEIC) trascritto su Wikisource
dati: dati/furioso/citazioni.json (v4, trenta record: tappa, filone, canto, ottava, versi, parafrasi, moto, emozione, tema, luogo, legame, e l'elenco `luoghi_inesistenti`), dati/furioso/pagine_wikisource.jsonl (1 244 pagine del digitalizzato), dati/furioso/orlando_furioso_1928.txt (4 796 ottave indicizzate, testo normalizzato)
strumenti: sorgenti/furioso/scarica_wikisource.py, sorgenti/furioso/estrai_ottave.py, sorgenti/furioso/costruisci_citazioni.py, sorgenti/furioso/verifica_citazioni.py, sorgenti/furioso/provino_html.py, sorgenti/verifica_coerenza.py
controllo: python3 sorgenti/furioso/verifica_citazioni.py (30 citazioni obbligatorie, 82 versi, 1 citazione facoltativa, 12 filoni dichiarati di cui 11 giocabili, 0 problemi) e --gutenberg (23 citazioni a riscontro, 3 differenze dichiarate); python3 sorgenti/verifica_coerenza.py (versioni, file citati, cifre dichiarate, tappe e personaggi)
prototipo: provino_furioso.html (una pagina, offline, generata)
documenti collegati: videogioco-5-duchi-luoghi.md (v0.3, §4.5 con la regola dei due strati e il tipo `N` di non luogo), videogioco-5-duchi-anno5-mondo.md (v0.4, le trenta tappe 5-1…5-30 e la sezione sul giocatore dentro il *Furioso*), videogioco-5-duchi-luoghi-edifici.md (v0.2), AGENTS.md, FONTI-E-LICENZE.md
---
# I filoni dell'*Orlando furioso*

## 0. Che cosa chiede la richiesta, e che cosa c'è dentro

Pietro chiede tre cose, e sono tre cose diverse:

1. **i luoghi** del gioco devono venire dall'*Orlando furioso*, ricalcando i **filoni** della vicenda;
2. **in ogni livello** ci devono essere **brevi citazioni del poema**;
3. le citazioni devono avere una **parafrasi interattiva, intuitiva, emozionale, breve**, che dia senso alla trama ariostesca.

Questo documento risponde alle tre, e risponde anche a una quarta domanda che nessuno ha fatto ma che era lì sotto: **se i luoghi vengono dal poema, dove vanno i trenta personaggi dell'anno, che sono persone vere e non paladini?**

La risposta è in §2, ed è una risposta che scioglie la **Q1** di `videogioco-5-duchi-luoghi.md` §8. La Q1 è **chiusa**: Pietro ha ratificato la regola dei due strati il 02/10/2026 (§2.2).

---

## 1. Il testo: perché Wikisource, e perché è stato difficile

### 1.1 Le quattro strade, e come sono andate

| Fonte | Che cosa dà | Perché è stata scartata o scelta |
|---|---|---|
| **Project Gutenberg 3747** | i primi **16 canti**, testo piatto, edizione *modernizzata* («inchiostro» per «inchïostro») | **non va bene**: 16 canti sono un terzo della vicenda, e il gioco ha trenta tappe |
| **Liber Liber** | l'edizione Segre, 46 canti | **non va bene**: l'URL del testo restituisce 404 e la pagina HTML (1,9 MB) mescola il poema con le introduzioni di un curatore moderno. Il testo non è estraibile |
| **Internet Archive** (`orlandofuriosod00ariogoog`) | testo «completo» | **non va bene**: è un OCR rovinato — «nocquer taii» per «no' quer' tai», doppi spazi ovunque. Su un OCR non si cita: in un compito un errore di tre sillabe costa più di una parafrasi mediocre |
| **Wikisource it, `Orlando furioso (1928)`** | edizione della **Biblioteca BEIC**, tre volumi, in pubblico dominio, trascritta dal digitalizzato | **scelta**: 46 canti, testo in pubblico dominio, e — decisive — il numero d'ottava è **esplicito** nella trascrizione |

### 1.2 Il fatto tecnico che ha fatto perdere mezza giornata

Le sottopagine `Orlando furioso (1928)/Canto N` **non contengono il testo**: contengono un `<pages index="…–BEIC 1737380.djvu" from="7" to="27"/>`, cioè un richiamo alle pagine del digitalizzato. Il testo vive nella zona `Pagina:`.

Di conseguenza:

* `action=query&prop=extracts` sulla pagina del canto **restituisce zero caratteri**, e lo fa senza errore: è il caso peggiore, perché sembra che la pagina sia vuota;
* `prop=wikitext` sul canto dà 221 caratteri e basta;
* il file giusto è `prop=revisions&rvslots=main` sulla zona `Pagina:`, in lotti da cinquanta.

Il canto 16 usa un attributo in più (`tosection="s1"`) e per questo il primo tentativo lo dava per vuoto: **era una richiesta fallita, non un'assenza**. È la regola che questo progetto si dà da quattro cicli di controllo, e qui ha funzionato: *una richiesta che non arriva non è una risposta negativa*.

### 1.3 Che cosa è stato scaricato, e con quali difetti dichiarati

```
pagine scaricate            1 244   (46 canti su 46, nessuna mancante)
ottave indicizzate          4 796   numero reale del Furioso: 4 861
canti coperti                  46
```

I **65 ottave mancanti** (4796 + 65 = 4861) non sono sparite: sono i buchi della trascrizione, e sono **dichiarati** perché il primo numero che sembra giusto e non lo è. Nel dettaglio:

| Difetto | Quanti | Cosa significa |
|---|---|---|
| ottave assenti dalla trascrizione | **44** | il numero salta: l'indice lo dichiara (`canto 5: 3 ottave mancanti (38, 72, 88)`) e non lo nasconde |
| numero d'ottava ripetuto dal trascrittore | **44 chiavi** | il numero è scritto due volte (`16 17 19 19`): l'indice tiene il primo testo e dichiara l'ambiguità |
| ottave con 6 o 16 versi | **10** | refuso grave, o due ottave fuse: nessuna delle trenta citazioni le tocca |
| ottave con 7 versi | centinaia | **non è un difetto**: è la *rima extranea*, il verso senza rima che Ariosto mette a chiudere metà delle ottave e che il 1928 mette fra parentesi |

### 1.4 Una correzione che è anche un metodo

Nella prima stesura, `estrai_ottave.py` indicizzava i numeri di ottava del Gutenberg e accettava i doppi. Poi sono arrivati i canti 17–46 e **cinquanta numeri non erano quelli giusti**: la stessa ottava finiva sotto due chiavi diverse.

La correzione non è stata «toccare i numeri», che avrebbe prodotto un indice bellissimo e falso. È stata: **chi tiene l'indice tiene anche l'elenco dei numeri di cui non è sicuro**, e non li rimappa in nessun modo. Un buco dichiarato è recuperabile; un numero spostato di uno in un canto intero non lo è, e non si vede.

### 1.5 L'edizione, e che cosa si trova aprendo un'altra

*(decisione di Pietro, 02/10/2026: «mantiene la rima extranea (7 versi), che è un difetto dell'edizione e non del testo; a scuola serve sapere quale differenza si trova aprendo un'altra edizione. Specificandolo in modo chiaro e semplice».)*

**La scelta: si tiene il 1928.** Il gioco cita l'edizione della **Biblioteca BEIC** di tutte le lettere, perché è in pubblico dominio ed è l'unica delle quattro fonti di §1.1 che abbia il numero d'ottava scritto esplicitamente.

**La rima extranea, in parole semplici.** Un'ottava dell'*Orlando furioso* ha normalmente **otto versi**. Ma metà delle ottave del poema ne ha **sette**: l'ultimo, quello che non rima, si chiama appunto **rima extranea**, e serve a dare un riposo all'orecchio prima del ritmo di nuovo. Ariosto lo mette in corsivo. Il 1928 lo mette **fra parentesi** e in fondo al verso c'è un **50** di pagina: cosa voglia quel numero non è dichiarato in nessuna delle quattro edizioni, e va detto che non lo sappiamo.

Perché questa cosa conta al gioco, e non è una curiosità da filologo: **è un difetto dell'edizione, non un difetto del testo**. Chi stampa il 1928 e conta i versi a mano sbaglia; chi sbaglia i numeri poi sbaglia le citazioni. Per questo la prima stesura indicava i versi per numero di riga e sbagliava **53 versi su 78** (§4.4), e per questo oggi la citazione si individua con un **frammento distintivo** e non con un numero.

Le altre due cose da dire ai ragazzi, che vengono dalla stessa esperienza:

- **la rima extranea sposta i numeri ma non sposta le parole**: il verso c'è, e basta cercarlo dentro l'ottava;
- **aprire un'altra edizione può cambiare una riga, e va detto quale**: sotto, le tre differenze trovate fra il 1928 e il *Gutenberg*, tutte dichiarate e tutte verificabili con le mani.

### 1.6 Le due edizioni a riscontro: tre differenze, tutte dichiarate

`verifica_citazioni.py --gutenberg` confronta le citazioni che cadono nella prima parte — quella che il *Gutenberg* contiene — con l'altra edizione. Sono **23 su 30**; le altre sette sono fuori dal *Gutenberg* e il loro elenco è stampato ogni volta, non tacito.

Il risultato: **20 citazioni coincidono**, e **tre** dicono cose diverse.

| tappa | che cosa diverge | gravità |
|---|---|---|
| 5-6 | **canto 5, ottava 23 ha sette versi nel 1928 e otto nel *Gutenberg***: l'edizione moderna stampa entro parentesi «(che così son nomata)», che il 1928 non ha. Nella nostra citazione i tre versi sono il 2°, 3° e 4° del 1928 e il 3°, 4° e 5° del *Gutenberg* | **reale**, e proprio la prova che l'edizione va scelta e dichiarata |
| 5-22 | «degli infideli» contro «degl'infideli» | **forma**: l'apostrofo eliso, non un'altra parola |
| 5-24 | «**quante** ella conoscea» contro «**quanto** ella conoscea» | **variante di testo**: un'altra lezione, che cambia l'accordo con «le fiamme» del verso prima |

*(nota)* L'apostrofo non viene contato come differenza. «degl'infideli» e «degli infideli» sono la stessa parola in due edizioni, e segnalarlo sarebbe rumore: un controllo che segnala duecento cose non viene letto, e un controllo che non si legge non controlla.

*(nota)* **Le tre differenze sono tutte di scrittura, non di significato.** Una è un verso che un'edizione mette fra parentesi e l'altra no; una è l'apostrofo eliso; una è «quante» contro «quanto». In nessuna delle tre un ragazzo perde il senso della tappa. La regola che ne segue è semplice e la vale per ogni disciplina: **un'edizione non è la verità, è una scelta** — e la scelta va detta, altrimenti il libro che il ragazzo ha in mano non è quello che il gioco gli ha citato.

**La conclusione che conta** è che **nessuna delle tre differenze cambia l'insegnamento della tappa**. Il gioco può tenere il 1928 senza perdere nulla, purché lo dichiari — e lo dichiara, in tre righe, sulla prima pagina del testo e in fondo a ogni record.

---

## 2. La risposta alla Q1: il pin resta, la stanza è del filone

### 2.1 Il problema, riformulato

`videogioco-5-duchi-luoghi.md` §4.5 metteva il dito sul punto: se la mappa del quinto anno fosse **tutta** la geografia del *Furioso*, Fermi non starebbe a Chicago e Dijkstra non sulla Luna, e per metterli lì servirebbero legami «ottenuti per analogia», che la regola di Pietro vieta.

### 2.2 La regola: due strati, un solo pin

*(ratificata da Pietro il 02/10/2026: «va bene, estendiamo il file nel miglior modo possibile».)*

> **Il `pin` — il luogo dove il gioco si ferma — resta il luogo reale e verificato del personaggio. La `stanza` — lo spazio che il giocatore attraversa — è quella del filone, e può essere un luogo che non esiste, dichiarato con il tipo `I`.**

**Che cosa sono i pin, in una frase.** Un **pin** è il luogo in cui il gioco si **ferma**: quello su cui il giocatore può posare il dito e dire «sono qui». Il progetto ne ammette **uno per tappa**, e i trenta pin di un anno sono dunque trenta. Ma più tappe possono fermarsi nello stesso posto — Londra è il pin di 5-3, 5-7 e 5-19 — e in quel caso il posto è uno solo e i pin sono tre: è un **ritorno**, non una contraddizione. Nei dati (`dati/luoghi_gioco.json`) il campo `pin` di ciascun luogo è proprio questo: **quante tappe si fermano lì**, e la somma su tutti i luoghi dà esattamente il numero delle tappe del gioco (120).

Lo si dice perché la parola «pin» viene dalla cartografia dei programmi e qui ha due sensi, e solo uno dei due è il suo. **Il pin è una tappa, non un indirizzo:** il pin è *dove il gioco si ferma*, l'indirizzo è *dove si trova quella cosa*. Sono due righe diverse, ed è per questo che la regola seguente ne fa due campi.

È la stessa distinzione che il progetto ha già per i **strati**: la colonna dice l'anno e l'epoca storica, la nebbia dipende dal **pin visitato**. Qui la colonna storica resta, e la stanza è un'altra cosa.

Le conseguenze sono tre, e vanno dichiarate perché sono le regole del gioco:

1. **un solo pin per tappa**, come sempre: nessuna tappa ha due luoghi sulla mappa;
2. **nessun legame analogico verso un luogo reale**: se il filone è ambientato in un luogo reale, il legame dichiara *che cosa è successo lì* (`A`) o *che cosa quel luogo spiega* (`S`); se il luogo non esiste, il legame è `I` e non può essere altro;
3. **il giocatore sa sempre in che mondo è**: la scheda della tappa porta tre righe — il pin (dove), il filone (di chi è questa storia), il luogo della stanza (dove sta accadendo). Le prime due sono vere; la terza può essere una favola, e lo dichiara.

**La conseguenza tecnica, ratificata insieme alla regola.** `dati/luoghi_gioco.json` si estende con un blocco `tappe`: per ciascuna delle trenta tappe del quinto anno, il `pin` (il luogo reale, con il suo stato di coordinata) e la `stanza` (il luogo del filone, con filone, canto, ottava e tipo di legame). I due controlli automatici che ne derivano sono **F14** e **F15** (§7).

### 2.3 Perché la risposta è «entrambe le cose»

La Q1 chiedeva di scegliere fra «mappa = *Furioso*» e «*Furioso* = atlante e finale». Con la regola dei due strati la scelta non è necessaria, ed è il risultato migliore: **la mappa resta quella storica e verificata**, e il *Furioso* diventa il **racconto che attraversa l'anno**, tappa per tappa, non più solo alla fine. Il finale che `luoghi.md` §4.5 progettava (le fasce vuote che diventano la Luna) resta, e adesso ha il resto dell'anno che lo precede.

### 2.4 Che cosa si perde, e lo dichiaro

Si perde la promessa che **Fermi entri sulla Luna**. Era una buona promessa e l'ho voluta bene. Ma il costo dell'alternativa era il progetto intero: trenta personaggi fuori percorso obbligatorio, trenta legami `I` che la regola vieta, e una mappa che non sa più dire a un ragazzo di Chicago perché ci sta andando. **Il gioco deve poter essere spiegato in una frase**, e questa si spiega in una frase sola.

---

### 2.5 Il giocatore è dentro il *Furioso*

*(decisione di Pietro, 02/10/2026: il giocatore è **dentro** il poema; «i personaggi parlano di sé e della propria età, come negli anni 3-4»; la sezione per esteso è in `videogioco-5-duchi-anno5-mondo.md` §4.2.)*

La regola dei due strati non è solo una regola sui dati: è una scelta su **chi gioca**. Negli anni 3 e 4 chi gioca è **il visitatore che attraversa** la corte o l'archivio di un duca morto da secoli, e la domanda dell'anno è sua. Nel quinto anno la domanda è la stessa, ma la risposta la dà **il poema**: il giocatore è dentro l'*Orlando furioso*, e la domanda che lo riguarda non è «che cosa succede a Chicago» ma **«che cosa succede, in questo momento, a me che sto qui»**.

Le tre conseguenze, che sono tutte verificabili nel testo del progetto:

1. **i personaggi del parlano di sé e della loro età**, come negli anni 3 e 4: se l'anno sta a Ferrara nel 1592, la domanda di ogni persona che entra è *«da quanto sono qui?»*, e la risposta vale per lei e per il gioco;
2. **la domanda dell'anno diventa leggibile** perché ha due facce: il *pin* dice quanto siamo lontani da oggi (Chicago, 1942), la *stanza* dice in che anno siamo (la strada della fuga di Rinaldo, 1513). Il gioco mette le due facce sulla stessa scheda e non sceglie;
3. **i sei strati bianchi in fondo diventano la prova finale**: se il giocatore è dentro un racconto che sa già come va a finire, l'ultima tappa non è «che cosa succederà» ma **«che cosa ci resta da scrivere»** — che è la stessa domanda dei sei strati `S90`–`S95` (`anno5-mondo.md` §0.3 c).

La regola che ne discende, e che vale per tutti i documenti: **chi gioca dentro il *Furioso* non è un personaggio del *Furioso*.** Non ha nome proprio nel testo, non viene ritratto, e non «vince» niente: sta dove la stanza dice che sta, e quando la stanza è un luogo che non esiste, il gioco lo dichiara prima di aprirla.

Un **filone** è un racconto che attraversa più canti e più luoghi, e a cui il giocatore può tornare. Dodici sono molti per trenta tappe: la media è due e mezzo tappe per filone, e le tappe che si accavallano sono quelle in cui un filone riappare dopo venti canti — che è esattamente ciò che succede nel *Furioso*, e che il giocatore deve sentire.

| Codice | Filone | Canti che lo sorreggono | Luoghi principali | Tappe assegnate |
|---|---|---|---|---|
| `F1` | **La guerra e il patto** | 1, 4, 12-16, 18, 22, 33 | i monti Pirenei, Parigi, il fossato di Sarza, il campo di Agramante | 5-7, 5-20, 5-22, 5-29 |
| `F2` | **Angelica e la fuga** | 1-2, 5, 9-12, 21, 23 | la selva, il bosco di Ferraú, la riva, la fonte | 5-1, 5-5, 5-21 |
| `F3` | **Orlando e il ritorno di sé** | 1, 12-13, 23-24 | il bosco, la strada, la prima pagina | 5-2, 5-13, 5-30 |
| `F4` | **Atlante e il castello incantato** | 4, 6, 22-23, 30 | il castello d'Atlante, Montalbano, i monti Rifei | 5-15, 5-17, 5-19 |
| `F5` | **La corte di Scozia: Ginevra, Ariodante, Pinabello** | 4-5, 7, 23 | la corte di Scozia, il duello, il ponte d'Erifilla, la strada di Pontiero | 5-6, 5-9, 5-16, 5-24, 5-26 |
| `F6` | **Alcina e l'isola** | 6, 8, 21 | l'isola, la spiaggia, il paese degli incantatori | 5-10, 5-11 |
| `F7` | **Logistilla e l'anello** | 6, 22, 25-26 | il regno di Logistilla, il golfo e la montagna inabitata | 5-23 |
| `F8` | **Bradamante e Merlino** | 7-8, 21-22 | la tomba di Merlino, le selve di Pontiero | 5-27 |
| `F9` | **Astolfo e il viaggio straordinario** | 22-23, 34-35 | il bosco, l'aria, **la Luna** | 5-3, 5-4, 5-8 |
| `F10` | **Malagigi e l'incantesimo** | 11, 25-26 | il petron di Merlino, la torre | 5-12 |
| `F11` | **Ruggiero e la conversione** | 13-16, 22-26, 41 | il campo sotto l'assedio, la lettera | **5-22, facoltativa (`5-22F`)** |
| `F12` | **La parola data a un altro** | 24, 30, 32, 46 | il libro di Turpino, il campo, la strada del messaggero | 5-14, 5-18, 5-25, 5-28 |

La colonna dei **canti** è vincolante, non decorativa: ogni citazione deve cadere in un canto che il suo filone dichiara, e lo controlla `verifica_citazioni.py`. È una regola che è nata da un errore (§4.5).

*(nota, 02/10/2026 — decisione di Pietro)* **`F11` entra come tappa facoltativa**, non come tappa obbligatoria. La conversione di Ruggiero è un racconto che chiede un livello con due condizioni insieme: **una scelta che non si può disfare** e **la disponibilità ad aspettare che una condizione si verifichi prima di poterla onorare**. Le due condizioni sono esattamente l'argomento della tappa **5-22** (*ordine e affidabilità senza un'autorità che garantisca niente*), e il testo gliele dà entrambe nel canto XXV, dove Ruggiero promette per iscritto che «finito il tempo in che per fede astretto era al suo re […] si fará cristian». Non sostituisce nessuna delle trenta tappe: è una stanza in più, che si apre da 5-22 e che si può anche non aprire.

**La definizione dei facoltativi**, che da qui vale per tutto il progetto (decisione di Pietro: «i facoltativi dovranno essere personaggi/posti con cui interagire e vanno tutti pensati anche in base alla parte informatica»):

> **Un facoltativo è una persona o un luogo con cui il giocatore può interagire, e ogni facoltativo esiste per una ragione informatica dichiarata.** Se non c'è una parte del livello per cui quella persona serve, non è un facoltativo: è un nome in fondo alla scheda.

I tre vincoli che ne derivano, e che `verifica_coerenza.py` controlla dal 02/10/2026: **un facoltativo è sempre un essere con cui si parla o un posto in cui si entra** (non un libro, non un'idea); **ha un tipo di legame dichiarato** (`B/A/S/I/C/N`); **e il suo spostamento geografico va giustificato** — se il facoltativo porta il protagonista su un altro continente, la tappa lo dichiara, perché un teletrasporto non spiegato è il difetto che questo progetto combatte.

---


## 3. I dodici filoni

*(la sezione 2.5 è stata spostata in `videogioco-5-duchi-anno5-mondo.md` §4.2, che è il documento che descrive il quinto anno: questo documento dice *che cosa è* il gioco dentro il poema, quello dice *come si gioca*)*

## 4. Le trenta citazioni

### 4.1 La regola della citazione

*(aggiornata il 02/10/2026: tredici regole. La tredicesima è il tipo `N` di non luogo, §4.2 e `videogioco-5-duchi-luoghi.md` §4.3.)*

> **Una tappa, un'ottava, due o quattro versi, e una parafrasi che si possa dire a voce.**

Dodici regole, tutte verificabili da `verifica_citazioni.py`:

1. **una ottava per tappa, e nessuna ottava due volte**;
2. il testo è **ristretto dal sorgente**, non copiato a mano: `costruisci_citazioni.py` prende i versi dall'indice e li scrive nel JSON;
3. il verso si individua con un **frammento distintivo**, non con un numero di riga (§4.4);
4. ogni citazione è **riverificata a parte**, rileggendo il JSON e confrontandolo con l'indice delle ottave;
5. nessuna citazione cade su un'ottava con un difetto di trascrizione dichiarato, né su un'ottava il cui numero è ambiguo;
6. **ogni citazione cade in un canto che il suo filone dichiara** (§4.5);
7. **due tappe confinanti non citano ottave dello stesso canto a meno di tre distanza** (§4.6);
8. il **legame** è sempre uno dei cinque della regola dei luoghi, e `I` solo per luoghi che non esistono;
9. nessun campo obbligatorio è vuoto, e la **parafrasi** è di 186–300 caratteri: sotto i 120 è un titolo, e una tappa non ha un titolo al posto della spiegazione;
10. il **`moto`** è una parola sola: è l'emozione che il personaggio *prova*, non quella che il lettore deve provare;
11. il **`tema`** è la frase che va sulla targa, e deve stare anche da sola;
12. il legame **`I`** non si sceglie sul tono della citazione ma sul luogo: va solo a un luogo che **non esiste**, e quel luogo deve essere nell'elenco dichiarato `luoghi_inesistenti` di `citazioni.json` (§4.7);
13. il legame **`N`** (non luogo) si usa per ciò che non è un luogo ma non è nemmeno un luogo inesistente: una condizione attraversata, un'aria, un intervallo di tempo. Come `I`, non ammette coordinate; come `I`, va dichiarato in `citazioni.json`, in un elenco separato.

### 4.2 La tabella

Verificata il 02/10/2026: **30 citazioni, 82 versi, 0 problemi**.

| tappa | filone | riferimento | legame | luogo del *Furioso* | moto / emozione | tema |
|---|---|---|---|---|---|---|
| **5-1** | F2 | canto 1, ottava 32 | `A` | la strada della fuga di Rinaldo | sdegno / frustrazione | la misura che hai è quella che hai, e nessuna riga di programma ti avvisa |
| **5-2** | F3 | canto 23, ottava 124 | `A` | il bosco dove Orlando perde il senno | ribrezzo / sconcerto | il punto in cui un'idea smette di reggere non lo scegli: te lo accorgi |
| **5-3** | F9 | canto 22, ottava 30 | `A` | il bosco di Pontiero | insofferenza / impazienza | partire da una stima sbagliata porta altrove, e non è un problema di precisione |
| **5-4** | F9 | canto 34, ottava 49 | `I` | **la Luna** | stupore / meraviglia | un'integrale è una somma di pezzi: più vera del disegno della curva |
| **5-5** | F2 | canto 1, ottava 77 | `A` | la foresta dove passa Ferraú | curiosità / sorpresa | un tiro casuale non è un tiro sbagliato: è un tiro senza garanzia |
| **5-6** | F5 | canto 5, ottava 23 | `A` | la corte di Scozia | pazienza / ostinazione | un numero irrazionale si costruisce tagliando e ricominciando |
| **5-7** | F1 | canto 14, ottava 133 | `A` | il fossato di Sarza, sotto Parigi | terrore / allarme | una simulazione a tempo discreto è un incendio che avanza a passi |
| **5-8** | F9 | canto 23, ottava 16 | `N` | **l'aria sopra la foresta** *(non luogo)* | risolutezza / concentrazione | ogni secondo di ritardo è un errore che non si cancella |
| **5-9** | F5 | canto 23, ottava 40 | `A` | la strada di Pontiero | inchiesta / determinazione | il dato non è il numero aggregato: è la sua distribuzione |
| **5-10** | F6 | canto 8, ottava 1 | `S` | il paese degli incantatori | sorpresa / stupimento | gli stessi dati, due storie opposte: dipende da dove guardi |
| **5-11** | F6 | canto 6, ottava 35 | `I` | **l'isola di Alcina** | inganno / seduzione | un dataset con una classe sola produce un modello con una risposta sola |
| **5-12** | F10 | canto 11, ottava 4 | `S` | il petron di Merlino | meraviglia / ammirazione | quattro pezzi e un insieme finito di regole: e produce un testo infinito |
| **5-13** | F3 | canto 1, ottava 2 | `S` | la pagina | intenzione / annuncio | una macchina è bravissima a dire certe cose e cieca su tutte le altre |
| **5-14** | F12 | canto 32, ottava 102 | `S` | il campo | frontezza / rifiuto | ci sono domande ben poste che non hanno risposta: e va detto che è un limite |
| **5-15** | F4 | canto 4, ottava 30 | `I` | il castello d'Atlante | slancio / urgenza | funziona e non sappiamo perché: la frase va sulla targa, non nel cassetto |
| **5-16** | F5 | canto 7, ottava 2 | `A` | il ponte d'Erifilla sulla riviera | attenzione / preoccupazione | due reti collegate da un solo cavo: i messaggi girano in tondo |
| **5-17** | F4 | canto 4, ottava 18 | `S` | i monti Rifei | curiosità / divertimento | chi scrive lo standard sceglie la parola, e la parola finisce nel manuale di tutti |
| **5-18** | F12 | canto 24, ottava 44 | `S` | il libro di Turpino | scoperta / soddisfazione | chi decide che cosa è corretto è la fonte, non il giudizio |
| **5-19** | F4 | canto 30, ottava 93 | `S` | Montalbano | sollievo / arrivo | un indirizzo non certifica niente: dice solo «qui», e si verifica arrivando |
| **5-20** | F1 | canto 16, ottava 37 | `A` | **Zibeltaro e l'Erculeo segno, cioè Ferrara** (v. §4.8, verifica **F8**) | preoccupazione / concretezza | una rete di un edificio si progetta con l'acqua che c'è, non con quella che si vorrebbe |
| **5-21** | F2 | canto 1, ottava 64 | `A` | la selva | decisione / risolutezza | il cammino più corto non è il più bello, e quando due costano uguale la scelta è tua |
| **5-22** | F1 | canto 1, ottava 9 | `A` | il campo davanti a Parigi | sfida / slancio | l'ordine senza autorità funziona se il patto è chiaro e i fatti lo verificano |
| ***5-22F*** *(facoltativa)* | F11 | canto 25, ottava 89 | `A` | il campo sotto l'assedio, dove Ruggiero scrive | prudenza / risoluzione | una promessa non è un'azione: è un'obbligazione che aspetta che una condizione si verifichi |
| **5-23** | F7 | canto 6, ottava 45 | `I` | il regno di Logistilla | autorità / ammirazione | un nome che non appartiene a nessuno è il motivo per cui funziona |
| **5-24** | F5 | canto 5, ottava 18 | `A` | la corte di Scozia | fiducia / trepida | un segreto che tutti hanno non è un segreto: è una telefonata |
| **5-25** | F12 | canto 30, ottava 80 | `S` | la strada del messaggero | impazienza / ansia | più banda non serve se il canale è lento: la capacità non è la velocità |
| **5-26** | F5 | canto 5, ottava 36 | `A` | il duello di Ginevra | esigenza / severità | le etichette sono una scelta di qualcuno: prima di imparare, sapere chi ha chiamato le cose |
| **5-27** | F8 | canto 7, ottava 38 | `A` | la tomba di Merlino, nelle selve di Pontiero | attesa / fiducia | collegare unità a caso e aspettare che da sole venga fuori qualcosa di giusto |
| **5-28** | F12 | canto 30, ottava 2 | `S` | il luogo del pentimento | pentimento / irreversibilità | ciò che è stato detto resta, e la responsabilità è di chi lo ha detto |
| **5-29** | F1 | canto 12, ottava 12 | `A` | la corte di Scozia | sospetto / irritazione | il merito di una scoperta va a chi l'ha fatta, non a chi l'ha detta per primo |
| **5-30** | F3 | canto 1, ottava 1 | `S` | la prima pagina | impegno / serietà | un programma è l'elenco di ciò che farà: tutto, e nient'altro |

I **legami** si distribuiscono così: quindici `A`, dieci `S`, quattro `I`, un `N`. Nessun `B` e nessun `C`, ed è giusto: **nessuna delle trenta citazioni è un luogo di nascita**, perché il libro non è un libro di biografie. I quattro `I` sono tutti luoghi che non esistono, come deve essere, e sono quelli dell'elenco dichiarato in `citazioni.json` (`luoghi_inesistenti`): la Luna, l'isola di Alcina, il castello d'Atlante, il regno di Logistilla. Il quinto nome di quell'elenco è **«l'aria sopra la foresta»**, che dal 02/10/2026 ha il tipo **`N`**: non è un luogo che non esiste, è **un non luogo**, e la differenza non è una sfumatura (v. §4.9). Gli altri luoghi delle stanze sono reali — strade, boschi, ponti, un campo — e prendono `A` o `S` secondo che sia successo qualcosa lì o quel luogo spieghi qualcosa.

**La citazione facoltativa `5-22F`** non è una delle trenta e non conta nei numeri della tabella: sta nel dizionario `facoltative` di `citazioni.json`, con lo stesso schema. `verifica_citazioni.py` la riverifica come tutte le altre e le controlla tre cose che le altre non hanno: **il filone è uno dei dodici**; **il canto è fra quelli che il filone dichiara**; **il codice è quello della tappa che la apre, con la lettera `F` in coda**. Una facoltativa che non si sa da dove si apre è una voce in più, non un livello.

I **canti** da cui attingono le trenta citazioni sono sedici, e nessuno porta più di sei tappe: il canto 1 (il proemio, la dedica, l'inizio della fuga di Angelica) sei, il canto 23 tre, il canto 30 tre, il canto 5 tre, gli altri uno o due.

### 4.3 Le parafrasi, per tappa

Sono in `citazioni.json` e vengono lette al ragazzo. Sei esempi, uno per ogni modo di usare il poema:

- **5-1 — il cavallo sordo.** «Una stima sbagliata non è un'idea: è un'altra idea, e il gioco non ti lascia accorgertene. Rinaldo grida al suo cavallo «ferma il piede!». Il cavallo è sordo e corre. Non ha nessuno a cui chiedere scusa: ha la distanza, e la distanza cresce.»
- **5-4 — la Luna.** «Il paesaggio sulla Luna non si guarda, si conta: zaffiri, rubini, oro, topazi, perle, diamanti. È un inventario, eppure è la cosa più bella del canto. L'area sotto una curva è la stessa cosa: non la disegni, la sommi, pezzo per pezzo.»
- **5-6 — l'albero che torna dalla radice.** «Come suol tornar da la radice arbor che tronchi e quattro volte e sei.» L'albero che tagli torna dalla radice: è l'iterazione di Babilonia per √2, fatta con le mani e senza sapere di star facendo matematica.
- **5-11 — l'isola.** «Sull'isola di Alcina sono tutti belli, e sono belli **perché** sull'isola di Alcina non è mai capitato nessun altro. Non è un difetto dell'osservazione: è il campione.»
- **5-14 — la cosa che non si sa.** «E quel che non si sa non si de' dire, e tanto men, quando altri n'ha a patire.» Non è un cinismo: è la forma più onesta che si possa dare a un programma che non termina. Nel gioco la scheda di questa tappa non ha una soluzione, e il pulsante lo dice.
- **5-28 — il pentimento.** «Si ravvede e pente e n'ha dispetto: ma quel c'ha detto, non può far non detto.» Il pentimento arriva dopo, e non cancella niente.

### 4.4 Il difetto che ha prodotto il metodo giusto

Nella prima stesura ogni citazione dichiarava i propri versi per **numero di riga** («ottava 22, versi 1, 5 e 6»). La verifica ne ha contati **53 non combacianti su 78**: la citazione esisteva, era quasi tutta giusta, e non corrispondeva a niente.

La causa è la *rima extranea*: metà delle ottave del *Furioso* ha sette versi invece di otto, e il 1928 lo dichiara con una parentesi chiusa in fondo al verso. Bastava quello perché tutti i numeri successivi si spostassero di uno.

La correzione non è stata aggiustare i numeri — sarebbe stato facile e sarebbe stato sbagliato, perché il numero avrebbe continuato a non combaciare con il libro stampato che il ragazzo ha davanti. La correzione è stata: **la citazione si individua con un frammento distintivo**, e lo script cerca il frammento dentro l'ottava e prende i versi che vengono dopo. Se il testo cambia, lo script si ferma e lo dice per nome.

### 4.5 Il secondo difetto: un filone che non conteneva le sue citazioni

Il controllo di coerenza del 02/10/2026 ha trovato che **tre citazioni erano assegnate a un filone i cui canti non le contenevano**: il ponte d'Erifilla (canto 7) stava dentro «la guerra e il patto», che è la battaglia di Parigi; la strada di Pontiero (canto 23) nello stesso filone, quando il canto 23 è già la palinodia di Orlando; la lettera del messaggero (canto 30) idem.

Non era un errore di testo: i tre versi erano giusti, al posto giusto, con la parafrasi giusta. Era un errore di **tassonomia**, ed è il peggiore perché non si vede: il giocatore legge «F1 — la guerra e il patto» e poi legge di una vedova che scrive, e pensa che il gioco abbia sbagliato il titolo. Il nome del filone è la prima riga che appare a schermo.

La correzione è stata assegnare ogni citazione al filone che la contiene davvero — il ponte d'Erifilla alla corte di Scozia, dove sta; la lettera a «la parola data a un altro» — e rendere la colonna dei canti **vincolante**, cioè controllata. Le tre citazioni cambiate sono: 5-9 e 5-16 passano a `F5`, 5-25 passa a `F12`.

### 4.6 Il terzo difetto: due tappe di fila, stesso canto

Nella stessa revisione è emerso che **5-8 e 5-19 citavano due ottave consecutive della stessa ottava** (23,16 e 23,17), e che il canto 1 compariva sette volte su trenta, con due coppie di tappe confinanti.

Il testo non è corto: sono quarantasei canti e 4 861 ottave, e non c'è ragione di far leggere due volte la stessa pagina a chi gioca. La regola aggiunta è che **due tappe confinanti non citino ottave dello stesso canto a meno di tre distanza**, e 5-19 è passata dal canto 23 al canto 30 — dove Rinaldo arriva davvero a Montalbano, che è anche un'immagine migliore per un livello sugli indirizzi.

Il canto 1 porta ancora sei tappe su trenta, ed è accettato: il proemio, la dedica a Ippolito e l'inizio della fuga di Angelica sono le tre righe che il libro mette in faccia al lettore, e usarle è giusto. Ma **non più di due tappe confinanti dello stesso canto**, e non più di sei citazioni in totale da un canto: è il tetto, e lo dichiara il dato, non la buona intenzione.

### 4.7 Il quarto difetto: un `I` su un luogo che esiste

Sempre nella stessa tornata di controllo, un difetto di un altro genere: la tappa **5-17** aveva il legame `I` su «i monti Rifei». I monti Rifei sono una catena vera, e `I` significa, nella regola di `videogioco-5-duchi-luoghi.md` §1.2, **questo luogo non esiste**.

Il legame era stato scelto sul **tono** della citazione e non sul luogo. La citazione è fantastica — l'ippogrifo non esiste, e il verso dice che è «naturale» — e il tono aveva fatto scrivere `I` accanto a un nome che invece è geografia. È la classe di errore più difficile da vedere: nella scheda la riga sembrava coerente, il nome del luogo è giusto, il verso è giusto, e solo la **regola** è violata.

La correzione è in due parti. Il legame di 5-17 diventa `S`, che è esattamente ciò che quel luogo fa: **i monti Rifei spiegano il nome dell'ippogrifo**, e il tema della tappa è che il nome lo mette chi scrive il nome. E, perché un `I` non torni fuori senza dichiarazione, `citazioni.json` porta adesso un campo `luoghi_inesistenti`: i cinque luoghi che il gioco ammette come inesistenti, ciascuno con il perché. `verifica_citazioni.py` vieta a un `I` qualsiasi altro luogo, e vieta anche che un luogo dichiarato rimanga senza uso.

La lezione è la stessa delle altre tre, detta diversamente: **ogni regola che non è scritta in un controllo viene violata senza che nessuno se ne accorga**, e la prima cosa da chiedersi non è «l'ho scritto bene» ma «come faccio a vederlo se è sbagliato».

---

### 4.8 Il quinto difetto: due nomi che il gioco aveva sbagliati (**F8** e **F9**, fatte)

*(le due verifiche da fonte del 02/10/2026 sono state risolte sul testo, non sull'atlante: la regola del progetto è che quando due fonti non concordano, il testo del 1928 è il testimone e l'atlante è l'imputato.)*

**F8 — «Zibeltaro» e «l'Erculeo segno» (16,37; ottava 5-20).**

La citazione è di **Rinaldo**, che nella piana fuori di Parigi ragiona ai baroni. Il testo è netto su un punto e reticente su un altro, e la distinzione è la lezione:

| nome nel testo | che cosa si può verificare sul 1928 | conclusione |
|---|---|---|
| **l'Erculeo segno** | è lo stemma degli **Estensi**: il poeta stesso, al canto XXVI (ottava 51), scrive «Duo Erculi, duo Ippoliti da Este, un altro Ercule, un altro Ippolito anco», mettendo «Ercole» e «Este» nella stessa frase | **è Ferrara**, e il gioco può dirlo: è la città del duca dentro il libro che gioca |
| **Zibeltaro** | il poema lo richiama in un solo altro punto (canto XXX, ottava 10: «Zizera detta, che siede allo stretto / di Zibeltarro, o vuoi di Zibelterra») e non lo localizza mai | **non si può dichiarare**: è una terra di là dello stretto, e due letture sono in campo |

L'errore che il gioco stava per perpetuare era doppio, euguale: la parafrasi della tappa 5-20 scriveva «Zibeltaro ed Ercole sono **Adria** e Ferrara», e **Adria non risulta da nessuna parte** — né dal testo né dall'atlante. La parafrasi è stata corretta e il luogo della stanza è diventato «Zibeltaro e l'Erculeo segno, cioè Ferrara», con una nota che dichiara che **Zibeltaro resta non localizzato**.

La cosa più preziosa che ne esce non è la coordinata: è che **la tappa ha un argomento migliore di quanto non avesse**. Rinaldo avverte che i Mori sono già usciti una volta, e che l'attacco non viene da lontano: viene da una parte che credevano sicura. È esattamente il tema di 5-20 — **progettare una rete idrica con l'acqua che c'è, non con quella che si vorrebbe** — e diventa il caso in cui la minaccia è *dentro casa*. Ferrara è il nome della minaccia: il gioco può dirlo, e lo dice, con la fonte.

**F9 — «la vocal tomba di Merlino» (7,38; ottava 5-27).**

Il testo lo dice in quattro versi, e li dice senza equivoci:

> Con questa intenzïon prese il camino / verso le selve prossime a Pontiero, / dove la vocal tomba di Merlino / era nascosa in loco alpestro e fiero. / **Ma quella maga** che sempre vicino / **tenuto a Bradamante avea il pensiero**, / quella, dico io, che nella bella grotta / l'avea de la sua stirpe instrutta e dotta;

è **Bradamante** che parte, e non Astolfo. Il filone `F8` si chiama giustamente «Bradamante e Merlino» e la parafrasi era già corretta: **non c'è stato nessun errore, e il rischio era un altro** — il *Furioso* contiene **due** episodi che si somigliano, e chi li confonde scrive che è andata Astolfo:

- **canto VII,38** — Bradamante va alla tomba e vi riceve la previsione (è la nostra tappa);
- **canto XXXIV,5-6** — Astolfo entra in un antro dove cerca Merlino e **non lo trova**;
- **canto XXIII,72** — Pinabello, sconfitto, **butta il cavallo nella tomba di Merlino**.

La regola che ne segue è scritta nel dato: **ogni stanza del poema porta il nome di chi la abita**, e `verifica_citazioni.py` vieta che una stanza di Merlino venga assegnata ad Astolfo. Le lettere e le previsioni che Orlando cerca sono sulla **Luna** (canto XXXIV,83-87), e la tappa 5-4 le dichiara già: due posti diversi, due filoni diversi.

### 4.9 Il sesto difetto, che è una decisione di genere: «l'aria sopra la foresta»

*(decisione di Pietro, 02/10/2026: «mi piace come luogo non luogo (utile anche per eventuale filosofia)».)*

Cinque stanze su trenta non hanno un luogo. Quattro sono **luoghi che non esistono** — la Luna, l'isola di Alcina, il castello d'Atlante, il regno di Logistilla — e hanno il tipo `I`: sono immagini, e su un'immagine si può ragionare. La quinta, **«l'aria sopra la foresta»**, è un'altra cosa: **non è un luogo inesistente, è un non luogo**. L'aria non si raggiunge, non si pinza, non ha coordinate: **la si attraversa**, e mentre la attraversi non sei da nessuna parte.

Metterla fra gli inesistenti era comodo e sbagliato: obbligava a dire che l'aria «non esiste», che è falso, e nascondeva la cosa più interessante della stanza, cioè che **esistono cose che non sono né qui né altrove**.

Da qui il **tipo `N`**, che è il sesto della scala dei legami:

| Codice | Tipo | Che cosa ammette | Prova |
|---|---|---|---|
| `I` | **luogo che non esiste** | un'immagine, un regno favoloso, un corpo celeste | il luogo è dichiarato inesistente in `citazioni.json` |
| `N` | **non luogo** | una condizione, un attraversamento, un intervallo | il luogo è dichiarato in un elenco separato, `non_luoghi` |

Come `I`, `N` **non ammette coordinate**: è controllato dalla verifica **F14**. E come `I` va dichiarato, perché la regola vale per entrambi: se domani si può mettere `I` o `N` a piacere, il gioco perde la capacità di dire al ragazzo *quando una cosa è finta*.

**Perché è utile anche per la filosofia, come dice Pietro, e in modo concreto.** «L'aria che attraversi» è il posto giusto per due domande che il quinto anno deve poter fare a voce: **dove si trova una cosa che non è in nessun posto?** (un dato in memoria, una promessa, un valore che passa da una variabile a un'altra) e **che cosa distingue un luogo da una condizione?** (una coordinata dice *dove*; una coordinata mancante dice *che tipo di cosa è*). Sono due domande di epistemologia, e nascono da una stanza in cui non si può disegnare niente.

### 4.10 Il settimo difetto: due paragrafi che il gioco non poteva onorare

Non un difetto del testo: un difetto del progetto, dichiarato perché anche i difetti di progetto vanno scritti. Il documento promises due cose che nessuno dei due poteva fare: **una tappa per `F11`** (§3) e **la definizione dei luoghi fantastici per tutte le stanze** (§4.2). La prima è risolta come facoltativa, la seconda come tipo `N`: sono le due cose che la revisione del 02/10/2026 ha cambiato, ed entrambe erano state scritte nella stessa settimana in cui il gioco si è accorto che i facoltativi non erano mai stati definiti.

---


### 5.1 Che cosa deve fare, e che cosa non deve

La parafrasi è **interattiva** nel senso che il gioco non la dà: la fa tirare fuori al ragazzo, e poi gliela corregge. Il meccanismo del provino è di tre passi:

1. la stanza mostra **due o quattro versi** e chiede: *che cosa prova, in quei versi, chi li sta vivendo?* — quattro possibilità: **una giusta** (il `moto`) e **tre sbagliate**, ognuna con la ragione per cui è sbagliata;
2. il gioco **non premia e non punisce**: dice soltanto perché la risposta è quella e perché l'altra no. Un quiz che dice solo «sbagliato» non insegna niente; un quiz che dice «non è orgoglio: è qualcuno che grida a chi non può ascoltarlo» insegna una cosa sola, ma la insegna per sempre;
3. **solo dopo** la scelta si apre la parafrasi, con la **targa** del tema.

### 5.2 Le regole che la rendono «breve, intuitiva, emozionale»

| regola | come si realizza | controllo |
|---|---|---|
| **breve** | 186–300 caratteri, tre frasi al massimo | controllato dallo script: sotto i 120 caratteri la parafrasi è un titolo, e il gioco si ferma |
| **intuitiva** | parte da un'immagine, non da una definizione. Nessuna tappa comincia con «questo passaggio è da leggere come…» | revisione manuale |
| **emozionale** | il `moto` è una parola sola e non coincide con l'`emozione`: il personaggio prova una cosa, il lettore ne prova un'altra | revisione manuale |
| **non frettante** | il testo del *Furioso* non viene spiegato: viene **riconosciuto**. La tappa 5-6 non spiega √2, dice che l'albero torna dalla radice quattro volte e sei | revisione manuale |
| **onesta** | nessuna parafrasi promette una soluzione che il livello non ha (5-14 e 5-15 sono su questo) | revisione manuale |

### 5.3 Il prototipo

`provino_furioso.html` — **una pagina, offline, nessuna richiesta di rete**, verificato: il file non contiene `http`, `fetch`, `XMLHttpRequest`, `<script src` né `<link>`.

Il provino contiene **quattro tappe** (5-1, 5-11, 5-20, 5-30) e mostra la stanza completa: pin, filone, canto e ottava, legame, luogo, versi, moto, emozione, la domanda, le quattro scelte e — dopo la scelta — la parafrasi e la targa.

I **distrattori non stanno nel modello**: sono scritti a parte in `provino_html.py`, perché un gioco che mostra i propri errori come se fossero del progetto non sta verificando niente.

Il provino è **generato**, non scritto: `sorgenti/furioso/provino_html.py` lo ricostruisce da `citazioni.json`, perché una pagina con i dati ricopiati a mano è una pagina che un giorno dirà una cosa diversa dal file.

---

---

### 4.11 La Q6.1 chiusa: undici filoni giocabili e dodici dichiarati

*(03/10/2026 — `citazioni.json` v4, verifica F16)*

La domanda che chiude qui era precisa: il gioco mostra **tredici** filoni e il documento ne dichiara **dodici**, e la differenza era `F11`. La domanda era giusta ma il conto che la circondava era sbagliato, e la ragione per cui era sbagliato è la cosa più interessante di tutta la faccenda.

**Il conto vero.** Le trenta tappe obbligatorie portano **undici** filoni: `F1`–`F10` e `F12`. `F11` compare solo nella stanza facoltativa `5-22F`. Quindi il giocatore vede dodici nomi di filone, non tredici, e il documento ne dichiara dodici: **la cifra tornava già**. Il tredicesimo era un residuo di quando `F11` non era ancora entrato come facoltativa.

**Il difetto vero, che nessuno dei due conti vedeva.** Il campo `assegnato` nel JSON si calcolava su tutti i filoni usati, obbligatorie e facoltative insieme. `F11` risultava quindi `assegnato: true` con `tappe: ["5-22F"]`: il file diceva che `F11` è un filone giocabile, cioè per cui si viaggia, e la sua unica tappa non era una delle trenta. Chi leggeva il registro vedeva un filone che il gioco non permetteva di raggiungere.

**La decisione, che è quella che il documento consigliava.** `assegnato` vuol dire **giocabile**, cioè *con almeno una delle trenta tappe*. `F11` resta **dichiarato** — non cancellato, perché la vicenda di Ruggiero esiste e il registro del gioco deve saperla nominare — ma `assegnato: false`, con la sua stanza in un campo nuovo, `facoltative`, che dice da dove si apre.

```
F11  Ruggiero e la conversione   assegnato: false   tappe: []   facoltative: [5-22F]
```

**Perché la decisione sta nei dati e non solo qui.** Una decisione scritta in un documento che il programma non legge è una decisione che il prossimo che tocca il JSON non incontra. Ora il generatore la calcola (§ `costruisci_citazioni.py`, il commento è sul campo `assegnato`) e la verifica **F16** la controlla su cinque cose: le `tappe` di un filone sono esattamente le citazioni obbligatorie che lo portano; le `facoltative` sono esattamente le stanze facoltative; `assegnato` è vero se e solo se `tappe` non è vuota; ogni filone usato è dichiarato; e il titolo e i canti che ogni citazione porta addosso sono quelli del filone dichiarato, perché sono due copie dello stesso fatto e due copie divergono.

**Il controllo è stato provato contro il difetto**, perché un controllo che non è mai fallito non è un controllo: girato sul file di prima dichiara esattamente i tre problemi che la v4 aveva, e su un file con difetti iniettati ne dichiara nove.

---

### 4.12 La Q6.2 chiusa: le stanze senza coordinate, e la regola che le disegna a tempo zero

*(03/10/2026 — proposta di `sorgenti/ipotesi_luoghi.py`, `dati/ipotesi_luoghi.json`, verifica **B7**; la domanda era di Pietro: «casa proponi per risolvere a minimo impatto sul mio tempo? idealmente 0»)*

La Q6.2 chiedeva come si disegna sulla carta del gioco una strada che non ha nome, una grotta, un campo, un non luogo e una Luna. La risposta che il progetto ha scelto è la più economica di tutte quante si potevano immaginare, e vale anche per le **venticinque** stanze `A` e `S` che hanno una coordinata: **nessuna stanza ha un disegno proprio.**

> **Una stanza non si disegna: si dichiara. Il segno sulla carta è lo stesso per tutte, e cambia solo la sua etichetta.**

#### Le quattro regole, che sono tutto il lavoro

| # | Regola | Perché |
|---|---|---|
| **1** | La stanza ha il **pin reale e verificato** del personaggio, e su quel pin il gioco scrive il nome del filone. Il punto non serve a posto della stanza: serve a posto della persona | è la **regola dei due strati** (§2.2) già scritta, e le stanze non hanno coordinate perché *non ne hanno bisogno*: il punto sulla carta è quello del pin, che è verificato |
| **2** | Un nome doppio («Bombay e Delhi») **non si riduce a un punto**: si tirano fuori i due punti e si disegna **il tratto**. Otto nomi del quarto anno hanno una strada vera | qui la mappa *guadagna* informazione rispetto a prima: una linea fra due città verificate è un dato, e il progetto si rifiutava di perderlo |
| **3** | Un nome in cui una parte **non è un luogo** («Chio e la **Ionia**», «Ferrara e **il regno**», «Nanchang e **il mare**») **non ha strada**: la parte non geografica resta a parole, e il gioco lo dice | è la differenza fra una strada e una frase. Fingersi che siano la stessa cosa sarebbe la «stima sbagliata» che il progetto combatte ovunque |
| **4** | Se **non c'è un luogo**, non si disegna niente e il gioco **lo dice al giocatore**. Due tappe su trenta | un vuoto dichiarato non è una mancanza: è una risposta. Il vuoto ha nome (`nessun_luogo_dichiarato`) ed è l'unico che il controllo accetta senza punto |

#### Perché il tempo di Pietro è zero

Il conto, riga per riga:

- **non c'è nessuna illustrazione da fare.** Nessuna delle ventisei stanze ha un'immagine, e nessuna la chiederà: il testo del progetto vieta i testi inventati e la Q6.1 ha già dichiarato che le stanze sono dati (`citazioni.json`), non immagini;
- **non c'è nessuna mappa da disegnare.** La stanza è un'etichetta sopra un pin che esiste già, e il tratto è una linea fra due punti che il motore sa già trasformare in pixel;
- **c'è una riga di testo per ogni stanza, e la riga è già scritta.** Il campo `frase` di `dati/ipotesi_luoghi.json` contiene, per ciascuna delle 51 tappe, la frase che il gioco può mostrare al ragazzo — per esempio, per 5-9: *«John Snow non ha contato i morti: ha spostato la pompa»*;
- **il resto è una verifica**, e le verifiche le scrive il progetto: `B7` in `verifica_ambienti.py` pretende che ogni ambiente dichiari che cosa deve disegnare e da quale dei due file lo prende, e accetta un punto mancante **solo** dove c'è la dichiarazione di grado `immaginata`.

#### Che cosa è cambiato nei numeri

| | prima | dopo |
|---|---|---|
| ambienti con un punto da disegnare | 99 su 150 | **148 su 150** |
| ambienti con un punto *verificato* | 99 | 99 (il registro non si tocca) |
| ambienti con un punto *ipotizzato* e dichiarato | 0 | 49 |
| ambienti senza punto, **per decisione** | 0 (erano un buco) | 2 |

Le due tappe senza punto sono **5-18** (una sala di riunione del 1983 di cui nessuno ha ricordato il nome) e **5-22** (un documento del 2008: un documento non si punta sulla carta). Non sono un buco: sono le due stanze in cui il gioco può dire al ragazzo che *quello non è un posto*, che è la lezione più onesta del quinto anno.

#### Il principio che la Q6.2 ha fatto maturare

La domanda era «come si disegna una cosa senza coordinate», e la risposta ha spostato la domanda: **non era un problema di disegno, era un problema di etichette.** Un ambiente non è un'immagine, è **una promessa con dentro quattro campi**: che cosa ci sta, di che tipo è, da che cosa viene il suo punto, e che cosa non si sa. Il file `dati/ambienti_livelli.json` le aveva già tutte; mancava solo il quarto campo, e il quarto campo era la coordinata, che era **l'unico dei quattro che non riguardava il disegno**.

---

## 5. La parafrasi interattiva

---

## 6. Come si collega al resto dei dati

### 6.1 Lo schema di un record (`dati/furioso/citazioni.json`)

| campo | tipo | che cosa dice |
|---|---|---|
| `tappa` | `5-1`…`5-30` | il codice della tappa, unico |
| `filone`, `filone_titolo`, `filone_canti` | `F1`…`F12` | il racconto a cui la tappa appartiene e i canti che lo sorreggono |
| `canto`, `ottava`, `riferimento` | intero, intero, testo | il riferimento del testo, in due forme per non doverlo comporre a mano |
| `numeri_versi` | lista di interi | **la posizione di ogni verso citato**: è ciò che il verificatore confronta |
| `versi` | lista di testo | i versi, presi dall'indice e non copiati |
| `parafrasi` | testo | le due o tre frasi che il livello legge |
| `moto`, `emozione`, `tema` | testo, testo, testo | il sentimento del personaggio, la sfumatura del gioco, la frase sulla targa |
| `luogo`, `legame` | testo, `B/A/S/I/C/N` | il luogo della stanza e il tipo di legame, secondo `videogioco-5-duchi-luoghi.md` §1.2 e §4.3 |
| `fonte` | testo | l'edizione, sempre |

Accanto ai record, nella stessa radice del JSON, ci sono quattro strutture che non sono tappe e che pure sono controllate: `filoni` (codice, titolo, canti, `assegnato`, `tappe`, `facoltative` — gli ultimi tre campi sono i tre che la verifica **F16** confronta, §4.11), `luoghi_inesistenti` (gli unici luoghi a cui il legame `I` può arrivare, ciascuno con il perché), `non_luoghi` (gli unici a cui può arrivare `N`) e `facoltative` (le citazioni delle stanze facoltative, con il codice `5-NN F` della tappa che le apre). Una tappa senza questi campi non viene dal generatore, e un generatore che li scrive a mano è un generatore che un giorno dirà una cosa diversa dal file.

### 6.2 Che cosa va fatto anche in `dati/luoghi_gioco.json`

Ogni record di tappa che oggi ha un solo `luogo` ne avrà due distinti, e la distinzione non è una formalità. `dati/luoghi_gioco.json` ha una chiave nuova, **`tappe`**, accanto a `luoghi`: trenta record, uno per tappa del quinto anno.

```json
{"tappa": "5-20",
 "pin":   {"luogo": "Ferrara", "coord_stato": "verificata"},
 "stanza": {"luogo": "Zibeltaro e l'Erculeo segno", "legame": "A",
            "filone": "F1", "canto": 16, "ottava": 37,
            "coordinate": null}}
```

* il **`pin`** è il luogo reale: quello su cui il giocatore si ferma, con il suo stato di coordinata, che in `luoghi_gioco.json` è già dichiarato e non va ricreato;
* la **`stanza`** è il luogo del filone, con il suo tipo di legame e il rimando al testo.

I due campi hanno una sola regola in comune, ed è automatica: **una stanza di tipo `I` o `N` con coordinate è un errore** (verifica **F14**). E una seconda, che è quella che rende il blocco utile invece che decorativo: **`pin` e `stanza` devono essere dichiarati per tutte e trenta le tappe, e la stanza deve coincidere con la citazione** (verifica **F15**).

Il `pin` **non porta qui il tipo di legame `B/A/S/…`**: quel tipo appartiene al catalogo degli accoppiamenti persona–luogo (`videogioco-5-duchi-luoghi.json`, ancora da generare, §5.1 di `luoghi.md`), e qui compitarlo sarebbe inventare ventisei valutazioni non verificate. Il blocco porta il **luogo** e il suo **stato di coordinata**: tutto ciò che la mappa sa già.

---

## 7. Verifiche

| # | verifica | stato |
|---|---|---|
| **F1** | l'ottava 1 del canto 1 dice «Le donne, i cavallier, l'arme, gli amori» | **fatta** (è la prima riga di `dati/furioso/orlando_furioso_1928.txt`) |
| **F2** | tutti i 46 canti sono coperti | **fatta** (46/46, nessuna pagina mancante) |
| **F3** | le trenta citazioni corrispondono al testo | **fatta**: 30 citazioni obbligatorie, 82 versi, più la citazione facoltativa `5-22F`; 0 problemi |
| **F4** | nessuna ottava è citata due volte | **fatta** (controllata dallo script) |
| **F5** | nessuna citazione cade su un'ottava difettosa o ambigua | **fatta** (controllata dallo script) |
| **F6** | il prototipo non chiede niente a nessuno | **fatta** (nessun `http`, `fetch`, `XMLHttpRequest`, `<script src`, `<link>`) |
| **F7** | la stessa ottava, nelle due edizioni disponibili (*Gutenberg* e 1928), dà lo stesso testo | **fatta**: 23 citazioni confrontate, **20 coincidono**, tre divergono (§1.6): un verso in più, un apostrofo, una variante di accordo. Nessuna cambia l'insegnamento |
| **F8** | «l'Erculeo segno» è Ferrara, e che cosa è «Zibeltaro» | **fatta** (§4.8): l'Erculeo segno è **lo stemma degli Estensi** — lo dice il poeta stesso al canto XXVI, 51, «Duo Erculi, duo Ippoliti da Este» — e dunque Ferrara. **Zibeltaro non è localizzabile sul testo** e resta dichiarato tale. La parafrasi di 5-20, che diceva «Zibeltaro ed Ercole sono Adria e Ferrara», era **sbagliata**: Adria non compare né nel testo né nell'atlante, ed è stata corretta |
| **F9** | la «vocal tomba di Merlino» (5-27) è la grotta che Bradamante visita, non quella che Astolfo visita | **fatta** (§4.8): **è Bradamante** (7,38, «quella maga che sempre vicino / tenuto a Bradamante avea il pensiero»). La parafrasi era già giusta; il pericolo era la confusione con i due altri episodi — Astolfo nell'antro senza trovar Merlino (34,5-6) e il cavallo di Pinabello gettato nella tomba (23,72). Ora ogni stanza porta il nome di chi la abita |
| **F10** | le trenta parafrasi sono state lette ad alta voce da qualcuno che non le ha scritte | **lasciata in sospeso** per decisione di Pietro (02/10/2026): è l'unica verifica che **non si può chiudere da solo**, perché richiede una voce estranea al testo. Va fatta con la classe, prima della pubblicazione, e finché non è fatta il capitolo dei dati porta `F10: sospesa` invece di `fatta` — che è la differenza fra «non l'abbiamo fatto» e «abbiamo deciso di non farlo adesso» |
| **F11** | ogni citazione cade in un canto che il suo filone dichiara | **fatta**: prima del controllo tre erano fuori (§4.5), ora zero |
| **F12** | due tappe confinanti non citano ottave dello stesso canto a meno di tre distanza | **fatta** (§4.6) |
| **F13** | il legame `I` va solo a un luogo che non esiste, e quel luogo è dichiarato | **fatta**: prima del controllo 5-17 aveva `I` su un luogo reale (§4.7), ora zero |
| **F14** | una stanza di tipo `I` o `N` non ha coordinate | **fatta** (controllata dallo script, su tutti e trenta i record `tappe` di `dati/luoghi_gioco.json`): prima della regola dei due strati la domanda non era nemmeno formulabile, perché la stanza non era un campo |
| **F15** | `pin` e `stanza` sono dichiarati per tutte e trenta le tappe, e la stanza combacia con la citazione | **fatta**: trenta record, trenta pin (il gioco si ferma in trenta posti), trenta stanze, nessuna senza il suo filone, canto e ottava |
| **F16** | i filoni dichiarati, le loro tappe e il campo `assegnato` combaciano con le citazioni che li portano | **fatta** (§4.11): 12 filoni dichiarati, 11 giocabili, `F11` solo da stanza facoltativa; prima del controllo `F11` risultava `assegnato: true` con `5-22F` fra le tappe; `citazioni.json` è salito a v4 e le citazioni sono identiche byte per byte |

---

## 8. Questioni aperte

*(aggiornato il 02/10/2026, dopo le risposte di Pietro. Le cinque questioni di v0.3 sono **chiuse**, tutte e cinque, e al loro posto sono nate due nuove che sono davvero aperte.)*

| # | questione | esito |
|---|---|---|
| 1 | La mappa è il *Furioso* o il *Furioso* è l'atlante? | **chiusa** — la regola dei due strati, ratificata (§2.2) |
| 2 | `F11` senza tappa | **chiusa** — entra come **facoltativa `5-22F`**, con la definizione dei facoltativi (§3) |
| 3 | L'Africa del *Furioso* | **chiusa** — riscritta in `videogioco-5-duchi-luoghi.md` §6.1, sulla parola del testo |
| 4 | L'edizione | **chiusa** — si tiene il **1928**, e la rima extranea e le tre differenze sono spiegate in modo semplice (§1.5) |
| 5 | Il *Furioso* anche negli anni 2–4? | **chiusa** — **no**, per decisione di Pietro: riaprirebbe tre documenti già coerenti e aggiungerebbe un secondo strato agli anni 2–4, dove nessuno lo chiede. Resta scritto che si potrebbe |

**Q6 — le due nuove questioni, che sono le vere.**

1. ~~**I tredici filoni che il gioco mostra e i dodici che il documento dichiara.**~~ **chiusa il 03/10/2026, in §4.11.** Il conto era sbagliato e la differenza non era quella che sembrava: le trenta tappe portano **undici** filoni, `F11` compare solo nella facoltativa `5-22F`, e il giocatore vede dodici nomi come il documento ne dichiara dodici. Il difetto vero era un altro, e stava nei dati: `F11` risultava `assegnato: true` con la sua unica tappa in `tappe`, cioè un filone giocabile che non si raggiunge. Ora è `assegnato: false` con la stanza in `facoltative`, e la verifica **F16** lo tiene fermo.
2. ~~**Le ventisei stanze che non hanno una coordinata e non ne hanno bisogno.**~~ **chiusa il 03/10/2026, in §4.12.** Non era un problema di disegno: era un problema di etichette. La regola è che **nessuna stanza ha un disegno proprio** — la stanza è un'etichetta sul pin verificato del personaggio, un nome doppio con due parti geografiche diventa un tratto (otto nomi del quarto anno), un nome con una parte che non è un luogo resta a parole, e dove non c'è un luogo non si disegna niente e il gioco lo dice. Le 51 tappe senza coordinate hanno tutte un'ipotesi con tre gradi dichiarati in `dati/ipotesi_luoghi.json`: **148 ambienti su 150 hanno un punto da disegnare**, e i due che non lo hanno è perché non c'è un posto. Il tempo richiesto a Pietro è **zero illustrazioni e zero mappe nuove**.

---

## 9. Cosa c'è da fare

*(i primi otto punti della v0.3 sono **fatti** e sono spariti dalla lista, non dimenticati: la regola è che una cosa fatta non resta nella lista, resta nel registro)*

1. **la regola dei due strati** (era punto 1): fatta, ratificata (§2.2).
2. **`dati/luoghi_gioco.json` esteso** (era punto 2): fatto, con `pin`, `stanza` e i due controlli F14 e F15 (§6.2).
3. **F8 e F9** (era punto 3): fatte sul testo, e una delle due ha trovato un errore vero nella parafrasi (§4.8).
4. **le trenta parafrasi lette ad alta voce** (era punto 4): **sospese** per decisione di Pietro, non cancellate (§7, F10).
5. **`luoghi.md` §4.5 riscritta** (era punto 5): fatto, v0.3.
6. **il posto di `F11`** (era punto 6): fatto, è la facoltativa `5-22F`.
7. **l'edizione** (era punto 7): fatto, §1.5.
8. **«l'aria sopra la foresta»** (era punto 8): fatto, è il tipo `N` e ha una sezione tutta sua (§4.9).

**Quello che resta, in ordine di utilità:**

1. **`F10`**, quando ci sarà qualcuno che legga ad alta voce.

La Q6.1 e la Q6.2 sono chiuse il 03/10/2026 e non sono più qui: le cose fatte non restano nella lista, restano nel registro (§4.11 e §4.12).
4. **la scheda di `citazioni.json` per la tappa 5-20**: il luogo «Zibeltaro e l'Erculeo segno» non ha coordinate e non deve Averle, ma la scheda del giocatore deve dire *perché* — e il perché è che uno dei due nomi non è localizzato. Un luogo non localizzato dichiarato vale più di un luogo inventato.
7. *(fatto — l'edizione è scelta e spiegata: §1.5)*
8. *(fatto — «l'aria sopra la foresta» è il tipo `N`: §4.9)*

---

## 10. Registro modifiche

- **v0.6 (03/10/2026)**: **la Q6.2 è chiusa, ed è chiusa nella forma più economica possibile: nessuna stanza ha un disegno proprio.** La domanda di Pietro — «come si disegna sulla carta del gioco una strada che non ha nome, una grotta, un campo, un non luogo e una Luna, a minimo impatto sul mio tempo?» — si è rivelata, riscritta, una domanda di **etichette** e non di disegno: un ambiente non è un'immagine, è una promessa con dentro quattro campi, e l'unico che mancava era la coordinata, che è anche l'unico dei quattro che non riguarda il disegno (§4.12).
  - **quattro regole**: la stanza prende il pin reale e verificato del personaggio; un nome doppio non si riduce a un punto ma si tira fuori come **tratto** fra due punti veri (otto nomi del quarto anno); un nome in cui una parte non è un luogo non ha strada e la parte non geografica resta a parole (cinque casi); e se non c'è un luogo **non si disegna niente e il gioco lo dice**;
  - **il tempo di Pietro è zero**: nessuna illustrazione, nessuna mappa nuova. L'unica cosa che resta da fare è leggere la riga `frase` di ciascuna delle 51 ipotesi, che è già scritta, e adattarla al tono del livello;
  - **il conto**: da 99 ambienti con un punto a 150 a **148 su 150**, dei quali 49 con un punto ipotizzato e dichiarato. I due che restano senza sono **5-18** (una sala di riunione del 1983 di cui nessuno ha ricordato il nome) e **5-22** (un documento del 2008: un documento non si punta sulla carta), e sono le due sole ipotesi di grado `immaginata`;
  - **i tre gradi dell'ipotesi** sono in `luoghi.md` §4.8 e vengono controllati dalle regole **R1-R6** di `sorgenti/ipotesi_luoghi.py` e dal controllo **B7** di `sorgenti/verifica_ambienti.py`.

- **v0.5 (03/10/2026)**: **la Q6.1 è chiusa, e il difetto che le stava sotto era uno che nessuno dei due conti vedeva.** La domanda chiedeva perché il gioco mostrasse tredici filoni e il documento ne dichiarasse dodici: il conto era sbagliato, perché le trenta tappe obbligatorie portano **undici** filoni e `F11` compare solo nella facoltativa `5-22F`, quindi il giocatore vede dodici nomi come il documento ne dichiara dodici. Ma il campo `assegnato` di `citazioni.json` si calcolava su tutti i filoni usati, facoltative comprese: `F11` risultava `assegnato: true` con `tappe: ["5-22F"]`, cioè un filone giocabile la cui unica tappa non è fra le trenta. **La decisione** — quella che il documento consigliava — è ora nei dati: `assegnato` vuol dire giocabile, `F11` resta dichiarato e diventa `assegnato: false` con la stanza in un campo nuovo, `facoltative`. **La verifica F16** la tiene ferma su cinque cose, ed è stata provata sia contro il difetto di prima (tre problemi, tutti e tre giusti) sia su un file con difetti iniettati (nove problemi). Il generatore è stato modificato perché produca la stessa cosa: una decisione scritta solo in un documento che il programma non legge è una decisione che il prossimo che tocca il JSON non incontra. `citazioni.json` sale a v4; le trenta citazioni e la facoltativa sono identiche byte per byte, cambia solo il blocco `filoni`.

- **v0.1 (02/10/2026)**: prima stesione. Risponde alla richiesta di Pietro del 02/10/2026 sui luoghi, sui filoni e sulle citazioni per livello, e scioglie la Q1 di `videogioco-5-duchi-luoghi.md`:
  - **il testo completo**, per la prima volta in questo progetto: 46 canti dell'edizione 1928 della Biblioteca BEIC, trascritti da Wikisource e scaricati pagina per pagina (1 244 pagine), con il perché delle quattro fonti scartate e il fatto tecnico che le aveva bloccate (`prop=extracts` restituisce zero caratteri perché il testo vive nella zona `Pagina:`);
  - **lo stato della trascrizione, dichiarato**: 4 796 ottave indicizzate su 4 861, 44 ottave assenti, 44 numeri ripetuti dal trascrittore, 10 ottave con 6 o 16 versi; e la regola che un buco dichiarato non si rimappa in silenzio;
  - **i dodici filoni**, con i canti che li sorreggono, i luoghi, le tappe assegnate, e `F11` dichiarato non assegnato invece che cancellato;
  - **la regola dei due strati** (pin reale e verificato, stanza del filone, `I` solo per i luoghi che non esistono), con le tre conseguenze e con quello che si perde;
  - **le trenta citazioni**, tutte verificate riestraendole dal testo: 30 record, 78 versi, 0 problemi, quindici legami `A`, nove `S`, sei `I`, nessun `B` e nessun `C`;
  - **le nove regole della citazione** e il difetto che le ha fatte nascere: i numeri di riga sbagliavano 53 versi su 78 per colpa della rima extranea, e il metodo giusto è il frammento distintivo;
  - **il meccanismo della parafrasi interattiva** e le cinque regole che la rendono breve, intuitiva ed emozionale;
  - **il prototipo** `provino_furioso.html`, una pagina offline generata dal JSON, con quattro tappe complete;
  - **dieci verifiche**, di cui sette fatte, e **cinque questioni aperte**, delle quali la prima è la ratifica della regola dei due strati.
  - **il riscontro con la seconda edizione**: 22 citazioni confrontate con il *Gutenberg*, 19 identiche e 3 diverse — un verso in più nel canto 5 ottava 23, l'apostrofo eliso in 1,9, e una variante di accordo in 5,18; nessuna delle tre cambia l'insegnamento della tappa, e tutte e tre sono dichiarate.
- **v0.2 (02/10/2026)**: controllo di coerenza su tutto il progetto, e quattro correzioni che erano necessarie:
  - **tre citazioni erano nel filone sbagliato** — il ponte d'Erifilla e la strada di Pontiero erano dentro «la guerra e il patto», che è la battaglia di Parigi; la lettera del messaggero idem. Nessun verso era sbagliato: era sbagliato il nome che il giocatore legge per primo. 5-9 e 5-16 passano a `F5`, 5-25 a `F12`, e la colonna dei canti dei filoni è diventata **vincolante** (§4.5);
  - **due tappe confinanti citavano ottave consecutive** della stessa ottava, e il canto 1 compariva sette volte su trenta. 5-19 è passata dal canto 23 al canto 30 (l'arrivo di Rinaldo a Montalbano, che è anche un'immagine migliore per un livello sugli indirizzi), e la regola nuova — niente ottave dello stesso canto a meno di tre distanza fra tappe confinanti — è ora controllata (§4.6);
  - **i numeri del risconto con il *Gutenberg*** ricalcolati dopo quei cambiamenti: 23 citazioni confrontate, 20 coincidono, tre divergono; erano 22 e 19. Le tre differenze sono le stesse di §1.5;
  - **due verifiche nuove** (F11 e F12) e le regole della citazione da nove a undici. Le trenta citazioni sono ora 82 versi, non 78.
- **v0.3 (02/10/2026)**: seconda tornata dello stesso controllo a tappeto, e due correzioni vere:
  - **un legame `I` su un luogo che esiste**: la tappa 5-17 portava «i monti Rifei» con il legame interpretativo, ma quei monti sono una catena vera, e `I` significa «questo luogo non esiste» (§4.7). Il legame diventa `S` — sono i monti Rifei che spiegano il nome dell'ippogrifo, che è il tema della tappa — e i legami diventano quindici `A`, dieci `S`, cinque `I`;
  - **l'elenco degli inesistenti è dichiarato nei dati**: `citazioni.json` ha ora il campo `luoghi_inesistenti`, con i cinque luoghi ammessi come inesistenti e il perché di ognuno; `verifica_citazioni.py` vieta a un `I` qualsiasi altro luogo (nuova verifica **F13**, regola numero 12);
  - la tabella delle verifiche è riordinata da F1…F13, il rimando a `anno5-mondo.md` torna alla v0.2 (quella che il documento ha davvero, e non una v0.3 che non esiste ancora), il punto 5 di §9 punta a `luoghi.md` §4.5 e non a §6.1, e c'è un punto nuovo: decidere che cosa sia «l'aria sopra la foresta».
- **v0.4 (02/10/2026)**: le sedici decisioni di Pietro applicate. Il testo non è stato riscritto: sono state prese cinque decisioni, fatte due verifiche da fonte, corretti un errore vero e un difetto di conteggio.
  - **la regola dei due strati è ratificata** e la Q1 è chiusa (§2.2), con la spiegazione di che cosa sono i pin — che è una domanda che il documento non aveva mai risposto e che chi legge i dati si fa subito: il pin è il luogo dove il gioco si **ferma**, uno per tappa, e più tappe possono fermarsi nello stesso posto (Londra è il pin di 5-3, 5-7 e 5-19);
  - **`F8` fatta e con un errore trovato**: «l'Erculeo segno» è **Ferrara** — lo stemma degli Estensi, che il poeta stesso dichiara al canto XXVI, 51 — mentre **«Zibeltaro» non è localizzabile sul testo** e resta dichiarato tale. La parafrasi della tappa 5-20 diceva «Zibeltaro ed Ercole sono **Adria** e Ferrara»: **Adria non compare né nel testo né nell'atlante**, ed è stata tolta. Il luogo della stanza è ora «Zibeltaro e l'Erculeo segno, cioè Ferrara» (§4.8);
  - **`F9` fatta**: è **Bradamante** ad andare alla tomba di Merlino (7,38), non Astolfo; la parafrasi era già giusta, il pericolo era la confusione con i due altri episodi della tomba e dell'antro. Ora ogni stanza del poema porta il nome di chi la abita;
  - **`F10` sospesa**, non cancellata: è l'unica verifica che richiede una voce estranea al testo, e il registro dice *sospesa* invece di *fatta*;
  - **il giocatore è dentro il *Furioso*** (§2.5, e per esteso `anno5-mondo.md` §4.2): pin e stanza sulla stessa scheda, con due domande diverse — quanto siamo lontani da oggi, e in che anno siamo;
  - **`F11` entra come tappa facoltativa `5-22F`** (canto XXV, 89: la promessa che aspetta una condizione), ed è definita la **facoltativa** come «una persona o un luogo con cui si interagisce, pensato per la parte informatica della tappa, con il suo spostamento dichiarato»;
  - **nasce il tipo `N`, non luogo**: «l'aria sopra la foresta» non è un luogo inesistente ma una condizione attraversata, e va detto al ragazzo, perché è la domanda che riguarda i dati in memoria e le promesse non ancora scadute;
  - **l'edizione è scelta e spiegata in modo semplice** (§1.5): si tiene il 1928, la **rima extranea** (sette versi invece di otto) è spiegata come **difetto dell'edizione e non del testo**, e le tre differenze con il *Gutenberg* sono dichiarate una per una;
  - **`dati/luoghi_gioco.json` ha il blocco `tappe`**: trenta record con `pin` e `stanza`, e due verifiche nuove, **F14** (una stanza `I` o `N` non ha coordinate) e **F15** (pin e stanza per tutte e trenta le tappe, e la stanza combacia con la citazione);
  - **le questioni aperte passano da cinque a due**, e sono due nuove: il posto di `F11` nel registro del gioco, e il disegno delle stanze senza coordinate;
  - **un difetto di conteggio corretto**: i legami erano «quindici `A`, dieci `S`, cinque `I`» e dopo il tipo `N` sono quindici `A`, dieci `S`, quattro `I`, un `N`. Cinque `I` erano la somma sbagliata di quattro luoghi inesistenti più un non luogo.
