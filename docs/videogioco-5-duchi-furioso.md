---
titolo: Videogioco "I cinque duchi" — I filoni dell'Orlando furioso: i luoghi del quinto anno e le citazioni delle trenta tappe
versione: 0.3
data: 2026-10-02
autore: Pietro Fabbri (con Claude)
revisioni: v0.1 (testo e trenta citazioni); v0.2 (controllo di coerenza del 02/10/2026: tre citazioni erano nel filone sbagliato, due tappe confinanti citavano ottave adiacenti, e le cifre del risconto sono state ricalcolate); v0.3 (seconda tornata dello stesso controllo: un legame `I` posto su un luogo che esiste, l'elenco degli inesistenti dichiarato nei dati, la tabella delle verifiche riordinata e due rimandi corretti)
fonte del materiale: la richiesta di Pietro (02/10/2026) — «sulla base dell'Orlando furioso dobbiamo creare i vari luoghi, cercando di ricalcare il più possibile i filoni della vicenda; devono esserci, in ogni livello, delle brevi citazioni del poema con parafrasi interattiva, intuitiva, emozionale, breve che diano senso alla trama ariostesca del Furioso» — e il testo dell'Orlando furioso edizione 1928 (Biblioteca BEIC) trascritto su Wikisource
dati: dati/furioso/citazioni.json (v2, trenta record: tappa, filone, canto, ottava, versi, parafrasi, moto, emozione, tema, luogo, legame, e l'elenco `luoghi_inesistenti`), dati/furioso/pagine_wikisource.jsonl (1 244 pagine del digitalizzato), dati/furioso/orlando_furioso_1928.txt (4 796 ottave indicizzate, testo normalizzato)
strumenti: sorgenti/furioso/scarica_wikisource.py, sorgenti/furioso/estrai_ottave.py, sorgenti/furioso/costruisci_citazioni.py, sorgenti/furioso/verifica_citazioni.py, sorgenti/furioso/provino_html.py, sorgenti/verifica_coerenza.py
controllo: python3 sorgenti/furioso/verifica_citazioni.py (30 citazioni, 82 versi, 0 problemi) e --gutenberg (23 citazioni a riscontro, 3 differenze dichiarate); python3 sorgenti/verifica_coerenza.py (versioni, file citati, cifre dichiarate, tappe e personaggi)
prototipo: provino_furioso.html (una pagina, offline, generata)
documenti collegati: videogioco-5-duchi-luoghi.md (v0.2, §4.5 e la Q1 che questo documento scioglie), videogioco-5-duchi-anno5-mondo.md (v0.3, le trenta tappe 5-1…5-30), videogioco-5-duchi-luoghi-edifici.md (v0.2), AGENTS.md, FONTI-E-LICENZE.md
---
# I filoni dell'*Orlando furioso*

## 0. Che cosa chiede la richiesta, e che cosa c'è dentro

Pietro chiede tre cose, e sono tre cose diverse:

1. **i luoghi** del gioco devono venire dall'*Orlando furioso*, ricalcando i **filoni** della vicenda;
2. **in ogni livello** ci devono essere **brevi citazioni del poema**;
3. le citazioni devono avere una **parafrasi interattiva, intuitiva, emozionale, breve**, che dia senso alla trama ariostesca.

Questo documento risponde alle tre, e risponde anche a una quarta domanda che nessuno ha fatto ma che era lì sotto: **se i luoghi vengono dal poema, dove vanno i trenta personaggi dell'anno, che sono persone vere e non paladini?**

La risposta è in §2, ed è una risposta che scioglie la **Q1** di `videogioco-5-duchi-luoghi.md` §8.

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

### 1.5 Le due edizioni a riscontro: tre differenze, tutte dichiarate

`verifica_citazioni.py --gutenberg` confronta le citazioni che cadono nella prima parte — quella che il *Gutenberg* contiene — con l'altra edizione. Sono **23 su 30**; le altre sette sono fuori dal *Gutenberg* e il loro elenco è stampato ogni volta, non tacito.

Il risultato: **20 citazioni coincidono**, e **tre** dicono cose diverse.

| tappa | che cosa diverge | gravità |
|---|---|---|
| 5-6 | **canto 5, ottava 23 ha sette versi nel 1928 e otto nel *Gutenberg***: l'edizione moderna stampa entro parentesi «(che così son nomata)», che il 1928 non ha. Nella nostra citazione i tre versi sono il 2°, 3° e 4° del 1928 e il 3°, 4° e 5° del *Gutenberg* | **reale**, e proprio la prova che l'edizione va scelta e dichiarata |
| 5-22 | «degli infideli» contro «degl'infideli» | **forma**: l'apostrofo eliso, non un'altra parola |
| 5-24 | «**quante** ella conoscea» contro «**quanto** ella conoscea» | **variante di testo**: un'altra lezione, che cambia l'accordo con «le fiamme» del verso prima |

*(nota)* L'apostrofo non viene contato come differenza. «degl'infideli» e «degli infideli» sono la stessa parola in due edizioni, e segnalarlo sarebbe rumore: un controllo che segnala duecento cose non viene letto, e un controllo che non si legge non controlla.

**La conclusione che conta** è che **nessuna delle tre differenze cambia l'insegnamento della tappa**. Il gioco può tenere il 1928 senza perdere nulla, purché lo dichiari — e lo dichiara, in tre righe, sulla prima pagina del testo e in fondo a ogni record.

---

## 2. La risposta alla Q1: il pin resta, la stanza è del filone

### 2.1 Il problema, riformulato

`videogioco-5-duchi-luoghi.md` §4.5 metteva il dito sul punto: se la mappa del quinto anno fosse **tutta** la geografia del *Furioso*, Fermi non starebbe a Chicago e Dijkstra non sulla Luna, e per metterli lì servirebbero legami «ottenuti per analogia», che la regola di Pietro vieta.

### 2.2 La regola: due strati, un solo pin

> **Il `pin` — il luogo dove il gioco si ferma — resta il luogo reale e verificato del personaggio. La `stanza` — lo spazio che il giocatore attraversa — è quella del filone, e può essere un luogo che non esiste, dichiarato con il tipo `I`.**

È la stessa distinzione che il progetto ha già per i **strati**: la colonna dice l'anno e l'epoca storica, la nebbia dipende dal **pin visitato**. Qui la colonna storica resta, e la stanza è un'altra cosa.

Le conseguenze sono tre, e vanno dichiarate perché sono le regole del gioco:

1. **un solo pin per tappa**, come sempre: nessuna tappa ha due luoghi sulla mappa;
2. **nessun legame analogico verso un luogo reale**: se il filone è ambientato in un luogo reale, il legame dichiara *che cosa è successo lì* (`A`) o *che cosa quel luogo spiega* (`S`); se il luogo non esiste, il legame è `I` e non può essere altro;
3. **il giocatore sa sempre in che mondo è**: la scheda della tappa porta tre righe — il pin (dove), il filone (di chi è questa storia), il luogo della stanza (dove sta accadendo). Le prime due sono vere; la terza può essere una favola, e lo dichiara.

### 2.3 Perché la risposta è «entrambe le cose»

La Q1 chiedeva di scegliere fra «mappa = *Furioso*» e «*Furioso* = atlante e finale». Con la regola dei due strati la scelta non è necessaria, ed è il risultato migliore: **la mappa resta quella storica e verificata**, e il *Furioso* diventa il **racconto che attraversa l'anno**, tappa per tappa, non più solo alla fine. Il finale che `luoghi.md` §4.5 progettava (le fasce vuote che diventano la Luna) resta, e adesso ha il resto dell'anno che lo precede.

### 2.4 Che cosa si perde, e lo dichiaro

Si perde la promessa che **Fermi entri sulla Luna**. Era una buona promessa e l'ho voluta bene. Ma il costo dell'alternativa era il progetto intero: trenta personaggi fuori percorso obbligatorio, trenta legami `I` che la regola vieta, e una mappa che non sa più dire a un ragazzo di Chicago perché ci sta andando. **Il gioco deve poter essere spiegato in una frase**, e questa si spiega in una frase sola.

---

## 3. I dodici filoni

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
| `F11` | **Ruggiero e la conversione** | 13-16, 22-26, 41 | il campo di battaglia, la chiesa | **nessuna nel 5º anno** |
| `F12` | **La parola data a un altro** | 24, 30, 32, 46 | il libro di Turpino, il campo, la strada del messaggero | 5-14, 5-18, 5-25, 5-28 |

La colonna dei **canti** è vincolante, non decorativa: ogni citazione deve cadere in un canto che il suo filone dichiara, e lo controlla `verifica_citazioni.py`. È una regola che è nata da un errore (§4.5).

*(nota)* **`F11` non ha tappa nel quinto anno**, e non è un errore: la conversione di Ruggiero è un racconto che chiede un livello tutto suo (la fede, il battesimo, la scelta che non si può disfare) e quel livello è di un anno diverso, o del sesto. È dichiarato in `citazioni.json` con `assegnato: false` invece di essere cancellato, perché un filone senza tappa è un pensiero rimandato, non un pensiero scartato.

---

## 4. Le trenta citazioni

### 4.1 La regola della citazione

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
12. il legame **`I`** non si sceglie sul tono della citazione ma sul luogo: va solo a un luogo che **non esiste**, e quel luogo deve essere nell'elenco dichiarato `luoghi_inesistenti` di `citazioni.json` (§4.7).

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
| **5-8** | F9 | canto 23, ottava 16 | `I` | l'aria sopra la foresta | risolutezza / concentrazione | ogni secondo di ritardo è un errore che non si cancella |
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
| **5-20** | F1 | canto 16, ottava 37 | `A` | **Zibeltaro e l'Erculeo segno: Adria e Ferrara** | preoccupazione / concretezza | una rete di un edificio si progetta con l'acqua che c'è, non con quella che si vorrebbe |
| **5-21** | F2 | canto 1, ottava 64 | `A` | la selva | decisione / risolutezza | il cammino più corto non è il più bello, e quando due costano uguale la scelta è tua |
| **5-22** | F1 | canto 1, ottava 9 | `A` | il campo davanti a Parigi | sfida / slancio | l'ordine senza autorità funziona se il patto è chiaro e i fatti lo verificano |
| **5-23** | F7 | canto 6, ottava 45 | `I` | il regno di Logistilla | autorità / ammirazione | un nome che non appartiene a nessuno è il motivo per cui funziona |
| **5-24** | F5 | canto 5, ottava 18 | `A` | la corte di Scozia | fiducia / trepida | un segreto che tutti hanno non è un segreto: è una telefonata |
| **5-25** | F12 | canto 30, ottava 80 | `S` | la strada del messaggero | impazienza / ansia | più banda non serve se il canale è lento: la capacità non è la velocità |
| **5-26** | F5 | canto 5, ottava 36 | `A` | il duello di Ginevra | esigenza / severità | le etichette sono una scelta di qualcuno: prima di imparare, sapere chi ha chiamato le cose |
| **5-27** | F8 | canto 7, ottava 38 | `A` | la tomba di Merlino, nelle selve di Pontiero | attesa / fiducia | collegare unità a caso e aspettare che da sole venga fuori qualcosa di giusto |
| **5-28** | F12 | canto 30, ottava 2 | `S` | il luogo del pentimento | pentimento / irreversibilità | ciò che è stato detto resta, e la responsabilità è di chi lo ha detto |
| **5-29** | F1 | canto 12, ottava 12 | `A` | la corte di Scozia | sospetto / irritazione | il merito di una scoperta va a chi l'ha fatta, non a chi l'ha detta per primo |
| **5-30** | F3 | canto 1, ottava 1 | `S` | la prima pagina | impegno / serietà | un programma è l'elenco di ciò che farà: tutto, e nient'altro |

I **legami** si distribuiscono così: quindici `A`, dieci `S`, cinque `I`. Nessun `B` e nessun `C`, ed è giusto: **nessuna delle trenta citazioni è un luogo di nascita**, perché il libro non è un libro di biografie. I cinque `I` sono tutti luoghi che non esistono, come deve essere, e sono i cinque dell'elenco dichiarato in `citazioni.json` (`luoghi_inesistenti`): la Luna, l'aria sopra la foresta, l'isola di Alcina, il castello d'Atlante, il regno di Logistilla. Gli altri luoghi delle stanze sono reali — strade, boschi, ponti, un campo — e prendono `A` o `S` secondo che sia successo qualcosa lì o quel luogo spieghi qualcosa.

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

## 5. La parafrasi interattiva

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
| `luogo`, `legame` | testo, `B/A/S/I/C` | il luogo della stanza e il tipo di legame, secondo `videogioco-5-duchi-luoghi.md` §1.2 |
| `fonte` | testo | l'edizione, sempre |

Accanto ai record, nella stessa radice del JSON, ci sono due dizionari che non sono tappe e che pure sono controllati: `filoni` (codice, titolo, canti, `assegnato`, `tappe`) e `luoghi_inesistenti` (gli unici luoghi a cui il legame `I` può arrivare, ciascuno con il perché). Una tappa senza questi due campi non viene dal generatore, e un generatore che li scrive a mano è un generatore che un giorno dirà una cosa diversa dal file.

### 6.2 Che cosa va fatto anche in `dati/luoghi_gioco.json`

Ogni record di tappa che oggi ha un solo `luogo` ne avrà due campi distinti, e la distinzione non è una formalità:

```json
"pin":   {"nome": "Chicago", "tipo": "A"},
"stanza": {"nome": "la strada della fuga di Rinaldo", "filone": "F2",
           "canto": 1, "ottava": 32, "tipo": "A"}
```

Il `pin` va sulla mappa e ha coordinate; la `stanza` non ha coordinate quando il luogo non esiste, e questo diventa un controllo automatico: **una stanza di tipo `I` con coordinate è un errore**, e come ogni errore automatico va detto (§7).

---

## 7. Verifiche

| # | verifica | stato |
|---|---|---|
| **F1** | l'ottava 1 del canto 1 dice «Le donne, i cavallier, l'arme, gli amori» | **fatta** (è la prima riga di `dati/furioso/orlando_furioso_1928.txt`) |
| **F2** | tutti i 46 canti sono coperti | **fatta** (46/46, nessuna pagina mancante) |
| **F3** | le trenta citazioni corrispondono al testo | **fatta**: 30 citazioni, 82 versi, 0 problemi |
| **F4** | nessuna ottava è citata due volte | **fatta** (controllata dallo script) |
| **F5** | nessuna citazione cade su un'ottava difettosa o ambigua | **fatta** (controllata dallo script) |
| **F6** | il prototipo non chiede niente a nessuno | **fatta** (nessun `http`, `fetch`, `XMLHttpRequest`, `<script src`, `<link>`) |
| **F7** | la stessa ottava, nelle due edizioni disponibili (*Gutenberg* e 1928), dà lo stesso testo | **fatta**: 23 citazioni confrontate, **20 coincidono**, tre divergono (§1.5): un verso in più, un apostrofo, una variante di accordo. Nessuna cambia l'insegnamento |
| **F8** | Zibeltaro è Adria e «l'Erculeo segno» è Ferrara | **da fare**: la citazione 5-20 è di Adria e Ferrara, ed è il fatto che collega il poema alla città del gioco; va verificato su fonte |
| **F9** | la «vocal tomba di Merlino» (5-27) è la grotta che Bradamante visita, non quella che Astolfo visita | **da fare**: il testo è chiaro (7,38), ma nel *Furioso* ci sono due visite e i nomi si somigliano |
| **F10** | le trenta parafrasi sono state lette ad alta voce da qualcuno che non le ha scritte | **da fare**, ed è la verifica più importante: una parafrasi che a voce suona male è una parafrasi da rifare |
| **F11** | ogni citazione cade in un canto che il suo filone dichiara | **fatta**: prima del controllo tre erano fuori (§4.5), ora zero |
| **F12** | due tappe confinanti non citano ottave dello stesso canto a meno di tre distanza | **fatta** (§4.6) |
| **F13** | il legame `I` va solo a un luogo che non esiste, e quel luogo è dichiarato | **fatta**: prima del controllo 5-17 aveva `I` su un luogo reale (§4.7), ora zero |

---

## 8. Questioni aperte

1. **Q1 → risolta** (la Q1 di `luoghi.md` §8): il *pin* resta reale e verificato, la stanza è quella del filone, e la Q1 non si pone più. Va ratificata da Pietro, perché è una sua decisione e non mia.
2. **`F11` senza tappa**: Ruggiero e la conversione restano fuori dal quinto anno. Va deciso se diventano il livello di un altro anno, o se il filone entra con una sola tappa.
3. **L'Africa del *Furioso***: `videogioco-5-duchi-luoghi.md` §6.1 dichiara già che è il tema più serio del quinto anno. Con quattro tappe su `F1` — la guerra e il patto — questa parte va riscritta con la stessa onestà: nel poema il nemico è «il Moro», e il gioco non deve insegnare nient'altro su quella riga.
4. **L'edizione**: qui si usa il 1928, che modernizza la grafia. A scuola si sceglie un'edizione e si tiene quella. La scelta è di Pietro (V, `citazioni.json → fonte.avvertenza_2`).
5. **Il *Furioso* anche negli anni 2–4?** Fin qui il poema è del quinto anno. Se la stanza del filone funziona, è la cosa più bella che si possa fare anche all'anno III (Europa: Ruggiero, Bradamante, Atlante). Non propongo di farlo adesso: propongo di sapere che si può.

---

## 9. Cosa c'è da fare

1. **ratificare la regola dei due strati** (§2.2): è la decisione che regge tutto il resto, e finché non è presa il documento resta una proposta.
2. **estendere `dati/luoghi_gioco.json`** con `pin` e `stanza`, e aggiungere il controllo automatico *stanza di tipo `I` senza coordinate*.
3. **fare F8 e F9**, che sono le due verifiche da fonte, e non da script.
4. **le trenta parafrasi, lette ad alta voce** (F10): da fare con la classe, non prima.
5. **riscrivere §4.5 di `luoghi.md`** con la regola dei due strati, e chiudere la Q1.
6. **decidere il posto di `F11`** (questione 2).
7. **scegliere l'edizione per la scuola** (§1.5): il 1928 va bene, ma va detto, e va detto anche *quale* differenza si trova chi apre un'altra edizione.
8. **arrecare l'elenco degli inesistenti di `luoghi.md` §4.3**: delle cinque stanze con legame `I`, quattro sono già nell'elenco dei luoghi fantastici; «l'aria sopra la foresta» non c'è, ed è un caso che va deciso — è un luogo che non esiste, o è una condizione (l'aria che si attraversa) e quindi non un luogo?

---

## 10. Registro modifiche

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
