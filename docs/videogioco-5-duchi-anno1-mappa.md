---
titolo: Videogioco "I cinque duchi" — Anno I sulla mappa di Ferrara: il percorso unico
versione: 0.8
data: 2026-09-30
autore: Pietro Fabbri (con Claude)
dati: videogioco-5-duchi-anno1-mappa.json (30 tappe, v0.8); videogioco-5-duchi-anno1-personaggi.json (schede)
documenti collegati: videogioco-5-duchi-gioco.md (interazione, strumenti, carte, memoria), videogioco-5-duchi-meccaniche.md (v0.3), videogioco-5-duchi-anno1-ferrara.md (v0.2), videogioco-5-duchi-schema-livelli.md (v1.1)
---

# Anno I sulla mappa di Ferrara: il percorso unico

## 0. Decisioni di Pietro

**Prima tornata (28/09/2026):**

- **Mappa reale.** Il primo anno si gioca su una vera mappa di Ferrara.
- **Una tessera per livello.** Ogni livello sblocca un pezzo della mappa, con un passaggio obbligato e due approfondimenti facoltativi.
- **Catena.** Ogni personaggio rimanda al successivo e non esistono obiettivi paralleli.

**Seconda tornata (28/09/2026), che modifica la v0.1:**

1. **Solo i luoghi indispensabili.** Tutto il percorso sta **dentro le mura**. Pomposa, le Valli, Ro, Pontelagoscuro e il Lido di Spina sono esclusi.
2. **Una pianta unica**, senza strati storici sovrapposti.
3. **La strada è una sola** e non si dirama. I livelli sono seriali e consecutivi, quindi in **punti contigui** della mappa.
4. **La cronologia non è necessaria**, ma chi gioca deve avere **tutte le informazioni per contestualizzare** ciò che incontra (vedi `videogioco-5-duchi-gioco.md` §5).
5. **Prima i punti, poi la mappa.** Ogni personaggio viene fissato in un punto preciso; la mappa si disegna dopo, attorno al percorso.

**Terza tornata (28/09/2026):**

6. **Paolo Mazza diventa facoltativo** e lo stadio esce dal percorso. Il livello 1-26 va a Natta, alla Porta degli Angeli; il livello 1-27 a Teodoro Bonati, al suo monumento nel chiostro della Certosa.
7. **Si procede a tappe**: prima una bozza di mappa del percorso, poi la pianta definitiva.

**Quarta tornata (28/09/2026):**

8. **I facoltativi non occupano spazio sulla mappa.** Dove i personaggi sono già fitti, i facoltativi compaiono come **visioni di Borso**: il narratore li immagina ed evoca senza aprire nuovi punti sulla mappa. I facoltativi sono **in più e consecutivi**. Si sbloccano solo dopo che il giocatore ha finito il personaggio obbligatorio della tappa: prima la visione A1, poi la A2.
9. **Tracciato approvato** così com'è; si procede con la pianta.

Questo documento sostituisce la v0.1, cioè la catena cronologica con luoghi anche fuori città.

---

## 1. Regole del percorso

| # | Regola |
|---|---|
| R1 | **30 tappe, 30 personaggi, un solo ordine.** Ogni tappa è vicina a quella precedente: il percorso è una passeggiata dentro le mura, dalla Cattedrale alla Certosa. |
| R2 | **Il rimando si ottiene solo raggiungendo la soglia del livello** (k istanze con esito corretto e passaggi coerenti, `meccaniche` §2.3). La tessera successiva si apre solo con il rimando. |
| R3 | **Gli approfondimenti sono "visioni di Borso"**: il narratore immagina la scena e il personaggio facoltativo, nello stesso luogo della tappa, **senza punti in più sulla mappa**. Sono facoltativi e non danno nulla che serva per proseguire. |
| R4 | **Ordine dei facoltativi.** La visione A1 si apre solo dopo aver superato la soglia del personaggio obbligatorio; la A2 solo dopo aver completato la A1. La tappa successiva si apre con il rimando, indipendentemente dalle visioni, che restano disponibili anche più avanti. |
| R5 | **Le tappe già superate restano visitabili**, per il ripasso (`gioco` §4), ma non aprono nulla. |
| R6 | **Il codice di ripresa contiene l'intera catena.** Uno stato con la tappa n aperta deve avere le soglie da 1 a n−1: in caso contrario il salvataggio viene rifiutato. |

**Espediente narrativo: la città-memoria.** Il giocatore cammina nella Ferrara di oggi. Ogni personaggio è la **voce del proprio luogo**: parla dalla propria epoca, ma conosce la città che è venuta dopo. Per questo può rimandare a personaggi di secoli diversi. **Borso d'Este è il personaggio giocante (v0.7)**: il giocatore cammina con lui per tutto il percorso. Ogni personaggio parla di sé e della propria epoca, non di Borso. La scheda di contesto (`gioco` §5) evita la confusione fra epoche.

---

## 2. Le 30 tappe

**Colonna "Forza".** Indica quanto il luogo e il personaggio illuminano davvero l'argomento informatico:

- **forte**: il legame è naturale;
- **medio**: il legame funziona ma va costruito nel racconto;
- **di scena**: il luogo fa solo da ambientazione.

In totale ci sono 18 agganci forti, 10 medi e 2 di scena: sono i primi candidati alla revisione.

| Tappa | Luogo (indirizzo) | Personaggio | Argomento del livello | Aggancio | Forza | Rimando al successivo | Facoltativi |
|---|---|---|---|---|---|---|---|
| 1-1 | Cattedrale di San Giorgio (Piazza della Cattedrale) | **San Maurelio** | Informazione, dato, messaggio | Una traccia (un'iscrizione, una reliquia, una leggenda) è un dato; diventa informazione solo quando qualcuno la interpreta | forte | «Le tracce passano di mano in mano. Lungo il fianco della chiesa si commercia da secoli. Vai a destra, verso la Loggia.» | San Giorgio |
| 1-2 | Loggia dei Merciai (Piazza Trento e Trieste, fianco sud della Cattedrale) | **Mercanti, artigiani e cittadini** | Analogico e digitale | La bilancia a bracci misura in modo continuo (analogico); le monete si contano (digitale) | forte | «Qui si parla di affari, ma in piazza si decide chi comanda: cerca Salinguerra.» | Gli Adelardi (famiglia) |
| 1-3 | Piazza Trento e Trieste e Palazzo della Ragione (Piazza Trento e Trieste) | **Salinguerra Torelli** | Il bit | Guelfi o ghibellini: ogni schieramento è una scelta sì/no; n scelte producono 2ⁿ scenari | forte | «Le fazioni passano, i canti restano: nel museo di fronte ci sono i libri del coro.» | Matilde di Canossa |
| 1-4 | Museo della Cattedrale (ex San Romano) (Via San Romano 1) | **Guido Monaco (Guido d'Arezzo) a Pomposa** | Sistemi di numerazione posizionali | Sul rigo musicale il valore di una nota dipende dalla sua posizione: è l'idea della notazione posizionale | forte | «Io ho messo ordine nei suoni. Scendi verso via Ripagrande: in un vicolo buio viveva un uomo che metteva ordine nelle acque.» | — |
| 1-5 | Vicolo del Chiozzino (dal volto in via Ripagrande a via Piangipane) | **Bartolomeo Chiozzi, il "Mago Chiozzino"** | Conversioni binario ↔ decimale | La bilancia dell'ingegnere con pesi 1, 2, 4, 8…: ogni quantità è una somma di potenze di 2 | forte | «Mi chiamavano mago perché calcolavo. In fondo al vicolo, in via Piangipane, c'è chi custodisce un altro modo di scrivere i numeri.» | — |
| 1-6 | MEIS (Via Piangipane 81) | **La comunità ebraica ferrarese** | Ottale ed esadecimale | Nell'alfabeto ebraico le lettere valgono anche come numeri; l'esadecimale usa lettere (A–F) come cifre | forte | «Torna verso il centro, di fronte alla Cattedrale: al palazzo di corte ti aspetta il primo signore della città.» | — |
| 1-7 | Palazzo Municipale e Volto del Cavallo (Piazza del Municipio 2) | **Obizzo II d'Este** | Unità di misura | Il signore fissa pesi e misure della città: stessa parola, valori diversi, come kB e KiB | forte | «Il potere va difeso: dietro questo palazzo c'è la fortezza. Cerca il duca che fonde i cannoni.» | Leonello d'Este, Leon Battista Alberti |
| 1-8 | Castello Estense (Largo Castello 1) | **Alfonso I d'Este** | Aritmetica binaria e overflow | Un registro, come una fortezza, ha una capienza fissa: che cosa succede quando il numero non ci sta (overflow) | medio | «Io faccio parlare i cannoni. Qui accanto, al teatro, si parla una lingua che tutti devono capire.» | Nicolò II d'Este, Dosso Dossi |
| 1-9 | Teatro Comunale (Corso Martiri della Libertà 5) | **Antonio Foschini** | Codifica del testo: ASCII | Il teatro pubblico nasce in un'epoca di regole uguali per tutti: ASCII è una tabella comune, adottata da tutti | medio | «Una lingua comune serve anche per i segreti. Allo Studio un maestro ha ritrovato in un libro antico il cifrario di Cesare.» | Napoleone e l'età francese |
| 1-10 | Palazzo Paradiso (Biblioteca Ariostea) (Via delle Scienze 17) | **Guarino Veronese** | Prova: codifiche e cifrario di Cesare | Gli umanisti rileggono Svetonio, che descrive il cifrario usato da Cesare: prova di corte su codifiche e cifrari | forte | «Il mio allievo Leonello è stato signore; oggi a corte si parla francese, latino e italiano. Va' dal duca Ercole II.» | Alberto V d'Este, Niccolò Copernico |
| 1-11 | Palazzo Renata di Francia (Via Savonarola 9) | **Ercole II d'Este** | Unicode e UTF-8 | Una corte multilingue (italiano, francese, latino) ha bisogno di un repertorio di simboli per tutte le lingue: Unicode | forte | «Mia moglie Renata ama i libri e le idee nuove. Poco più avanti, in via Savonarola, c'è una casa dipinta con molti colori.» | Renata di Francia |
| 1-12 | Casa Romei (Via Savonarola 30) | **Giovanni Romei** | Colori RGB | Gli affreschi della Sala delle Sibille: i colori come mescolanza di componenti (RGB) | medio | «Nel monastero qui dietro è sepolta una duchessa di cui tutti credono di conoscere il volto.» | Tito Vespasiano Strozzi |
| 1-13 | Monastero del Corpus Domini (Via Campofranco 1) | **Lucrezia Borgia** | Immagini raster | Un volto a bassa risoluzione non si riconosce: così il mito ha sostituito la persona | forte | «Scendi verso sud: il monastero più antico della città ha una regola che dura da secoli.» | Ludovico Bonaccioli |
| 1-14 | Monastero di Sant'Antonio in Polesine (Via del Gambone 15) | **Beata Beatrice II d'Este** | Hardware e software | Il monastero è l'hardware; la Regola che lo fa funzionare è il software | forte | «Da qui si vede il palazzo delle feste di Borso: vai a Schifanoia, dove il tempo è dipinto mese per mese.» | Le monache di Sant'Antonio in Polesine |
| 1-15 | Palazzo Schifanoia (Via Scandiana 23) | **Francesco del Cossa** | Von Neumann e storia del calcolo | Il Salone dei Mesi è un calendario calcolato: contare e calcolare prima delle macchine, fino a von Neumann | medio | «Io ho dipinto; ma chi ha deciso che cosa dipingere? Chiedilo all'archivista qui accanto.» | Ercole de' Roberti, Borso d'Este |
| 1-16 | Palazzo Bonacossi (Via Cisterna del Follo 5) | **Pellegrino Prisciani** | Ciclo fetch-decode-execute | Il duca ordina, l'archivista interpreta, i pittori eseguono: preleva, decodifica, esegui | forte | «Una storia non dipinta resta solo nella memoria. Risali verso la Giovecca, alla palazzina di Marfisa.» | Taddeo Crivelli e i miniatori della Bibbia di Borso |
| 1-17 | Palazzina Marfisa d'Este (Corso Giovecca 170) | **Marfisa d'Este** | Memorie | La città ricorda Marfisa più per la leggenda che per i documenti: memorie diverse, veloci o durevoli | medio | «Lungo la Giovecca c'è l'ospedale dove un duca tenne chiuso un poeta.» | — |
| 1-18 | Antico Ospedale di Sant'Anna (cella del Tasso) (Corso della Giovecca 203) | **Alfonso II d'Este** | Periferiche e bus | Il duca decide che cosa entra e che cosa esce dalla cella di Tasso: dispositivi di ingresso e di uscita | medio | «Io non ho eredi, e la mia città cambierà padrone molte volte. In piazza Ariostea una colonna lo racconta.» | Torquato Tasso |
| 1-19 | Piazza Ariostea e colonna (Piazza Ariostea) | **Napoleone e l'età francese** | Porte logiche e algebra di Boole | Sulla colonna: SE governa il papa ALLORA la sua statua; SE Napoleone ALLORA la sua; poi Ariosto. Condizioni e porte logiche | di scena | «Dopo di me arrivano i pittori moderni: a palazzo Massari ne trovi uno che ha conquistato Parigi.» | — |
| 1-20 | Palazzo Massari (Museo Boldini) (Corso Porta Mare 9) | **Giovanni Boldini** | Prova: assemblare un calcolatore | Prova di corte: scegliere i componenti giusti per lo scopo, come un ritrattista sceglie luce, posa e sfondo | di scena | «Ferrara mi ha dato l'occhio; ma questa parte della città l'ha disegnata un architetto. Lo trovi al palazzo dei Diamanti.» | Filippo de Pisis |
| 1-21 | Palazzo dei Diamanti (Pinacoteca) (Corso Ercole I d'Este 21) | **Biagio Rossetti** | Il sistema operativo | L'Addizione è un sistema che assegna risorse (strade, lotti, acqua) a chi vive nella città: un sistema operativo | medio | «Il mio committente è all'incrocio qui fuori: è lui che ha voluto la città nuova.» | Cosmè Tura |
| 1-22 | Quadrivio degli Angeli (Palazzo Prosperi-Sacrati) (incrocio Corso Ercole I d'Este / Corso Porta Mare / Corso Biagio Rossetti) | **Ercole I d'Este** | Processi e scheduling | I cantieri dell'Addizione si aprono uno dopo l'altro: processi, attese, turni | medio | «Nel palazzo di fronte crescono le piante del mio medico.» | Josquin des Prez |
| 1-23 | Palazzo Turchi di Bagno e Orto Botanico (Corso Ercole I d'Este 32) | **Antonio Musa Brasavola** | Gestione della memoria | L'orto è una memoria organizzata: ogni pianta ha il suo posto e il suo indirizzo | forte | «Poco più giù lungo il corso c'è il museo di chi ha combattuto per l'Italia.» | Gabriele Falloppio |
| 1-24 | Museo del Risorgimento e della Resistenza (Corso Ercole I d'Este 19) | **Tancredi Mosti Trotti Estense** | File system, permessi, backup | Archivi, lasciapassare, copie dei documenti: file, permessi, backup | medio | «Anche i poeti conservano copie: Ariosto ha riscritto il suo poema tre volte. Vai a casa sua.» | I Bersaglieri del Po |
| 1-25 | Casa di Ludovico Ariosto (Via Ariosto 67) | **Ludovico Ariosto** | Il documento elettronico | Tre edizioni dell'Orlando furioso (1516, 1521, 1532): struttura, stili e revisioni di un documento | forte | «Io ho raccontato cavalieri. In fondo al corso, alla porta degli Angeli, qualcuno racconta la pianura con i numeri.» | Matteo Maria Boiardo |
| 1-26 | Porta degli Angeli e mura nord (fine di Corso Ercole I d'Este) | **Giulio Natta** | Foglio elettronico: celle e formule | Tabelle di produzione: righe, colonne, formule che calcolano totali e differenze. Il foglio elettronico | medio | «I miei numeri parlano di fabbriche. Ma chi per primo ha misurato quest'acqua e questa terra riposa alla Certosa, qui vicino: Teodoro Bonati.» | Paolo Mazza |
| 1-27 | Certosa: chiostro, monumento a Teodoro Bonati (Certosa (punto interno, senza civico)) | **Teodoro Bonati** | Funzioni, grafici, statistica | Le serie dei livelli del Po nel tempo: medie, variabilità, grafici. La statistica | forte | «Dietro la Certosa, in via delle Vigne, riposa uno scrittore che ha raccontato gli anni più bui.» | Il territorio del Po |
| 1-28 | Cimitero ebraico (Via delle Vigne 20) | **Giorgio Bassani** | Internet: struttura e servizi | Evento → testimonianza → racconto → film: un messaggio che passa da un canale all'altro (sezione narrativa lenta e non valutata) | forte | «Il mio racconto è diventato un film. Alla Certosa riposa un regista che sapeva che ogni inquadratura è una scelta.» | La comunità ebraica ferrarese |
| 1-29 | Certosa: cimitero monumentale (Piazza della Certosa) | **Michelangelo Antonioni** | Valutare le fonti, sicurezza, IA | Valutare le fonti; la missione del Chiozzino (cinque versioni e una risposta di un'IA da verificare) | forte | «Hai visto molte Ferrara. Nella chiesa qui accanto ti aspetta chi te le ha raccontate fin dall'inizio.» | Florestano Vancini, Riccardo Bacchelli |
| 1-30 | Certosa: chiesa di San Cristoforo (Piazza della Certosa) | **La città (P93)** — *proposta, da confermare* | Prova finale: inventario | Prova finale: ordinare le 30 carte nel tempo e costruire l'inventario della città. Borso, nella chiesa che ha fondato, rilegge il percorso | forte | «(fine dell'anno)» | Brondi (P87) |

**Il percorso a grandi linee.** Piazza della Cattedrale (1–4) → vicolo del Chiozzino e via Piangipane (5–6) → Municipio e Castello (7–8) → Giovecca e via delle Scienze (9–10) → via Savonarola e quartiere di Sant'Antonio (11–14) → Schifanoia (15–16) → Giovecca (17–18) → Addizione Erculea (19–25) → Porta degli Angeli (26) → Certosa e via delle Vigne (27–30).

**Paolo Mazza** è facoltativo, alla tappa 1-26 (approfondimento sulle classifiche in un foglio elettronico).

**Cinque duchi:** Alfonso I (1-8), Ercole II (1-11), Alfonso II (1-18), Ercole I (1-22) si incontrano sul percorso; **Borso è il giocatore** (v0.7).

**Nuovo personaggio:** Giovanni Romei (P94), a Casa Romei (1-12). La scheda è da completare.

**Personaggi della v0.1 non più obbligatori.** Restano come facoltativi o nei luoghi di esplorazione:

- Nicolò II, Alberto V, Leonello, Guarino e Copernico, ora nei luoghi dove compaiono come facoltativi;
- Obizzo II resta obbligatorio a 1-7;
- Beatrice II resta obbligatoria a 1-14;
- Bonati è **obbligatorio a 1-27**, al suo monumento nel chiostro della Certosa;
- Natta è **obbligatorio a 1-26**, alla Porta degli Angeli, come luogo simbolico: la porta verso il Po e la pianura delle fabbriche. Il polo chimico, fuori dalle mura, resta citato nel racconto.

---

## 3. Posizione precisa dei punti

**Fonte.** Dataset ufficiale *Numeri civici* del Comune di Ferrara (CC BY 4.0), 57.207 civici, scaricato da Pietro il 28/09/2026.

**Conversione.** Il dataset è in Monte Mario / Italy zone 1 (EPSG:3003). Le coordinate sono state convertite in WGS84 con la proiezione di Gauss-Boaga inversa sull'ellissoide Internazionale 1924 e la trasformazione di datum a 7 parametri indicata nel file `.prj`. Lo script è in `videogioco-5-duchi-anno1-coordinate-build.py.md` e non usa librerie esterne.

**Controllo.** Il civico Largo Castello 1 risulta a 44,8381 N, 11,6196 E: meno di 50 m dalla posizione del Castello, sufficiente per una mappa di gioco.

**Indirizzi forniti da Pietro:** Sant'Antonio in Polesine, via del Gambone 15; antico Ospedale di Sant'Anna, corso della Giovecca 203; Quadrivio degli Angeli, centro dell'incrocio.

| Tappa | Luogo | Personaggio | Lat | Lon | Distanza dalla precedente (m) | Fonte delle coordinate |
|---|---|---|---|---|---|---|
| 1-1 | Cattedrale di San Giorgio | San Maurelio | 44.83604 | 11.619803 | — | civico PIAZZA DELLA CATTEDRALE 9 — civico del lato della Cattedrale |
| 1-2 | Loggia dei Merciai | Mercanti, artigiani e cittadini | 44.835513 | 11.619919 | 59 | civico PIAZZA TRENTO E TRIESTE 21 — civico centrale della Loggia dei Merciai |
| 1-3 | Piazza Trento e Trieste e Palazzo della Ragione | Salinguerra Torelli | 44.83536 | 11.61928 | 53 | civico PIAZZA TRENTO E TRIESTE 4 — civico del lato ovest della piazza (Palazzo della Ragione): da verificare |
| 1-4 | Museo della Cattedrale (ex San Romano) | Guido Monaco (Guido d'Arezzo) a Pomposa | 44.834809 | 11.62042 | 109 | civico VIA SAN ROMANO 7 — nel dataset non esiste il n. 1: usato il civico dispari più a nord, da verificare |
| 1-5 | Vicolo del Chiozzino | Bartolomeo Chiozzi, il "Mago Chiozzino" | 44.834336 | 11.615694 | 376 | civico VICOLO DEL CHIOZZINO 4 |
| 1-6 | MEIS | La comunità ebraica ferrarese | 44.835507 | 11.613407 | 222 | civico VIA PIANGIPANE 81 |
| 1-7 | Palazzo Municipale e Volto del Cavallo | Obizzo II d'Este | 44.836043 | 11.619067 | 450 | civico PIAZZA DEL MUNICIPIO 2 |
| 1-8 | Castello Estense | Alfonso I d'Este | 44.838137 | 11.619641 | 237 | civico LARGO CASTELLO 1 |
| 1-9 | Teatro Comunale | Antonio Foschini | 44.837645 | 11.62043 | 83 | civico CORSO MARTIRI DELLA LIBERTA' 5 |
| 1-10 | Palazzo Paradiso (Biblioteca Ariostea) | Guarino Veronese | 44.832931 | 11.621723 | 534 | civico VIA DELLE SCIENZE 17 |
| 1-11 | Palazzo Renata di Francia | Ercole II d'Este | 44.833382 | 11.626207 | 357 | civico VIA GIROLAMO SAVONAROLA 9 |
| 1-12 | Casa Romei | Giovanni Romei | 44.833276 | 11.626078 | 16 | civico VIA GIROLAMO SAVONAROLA 30 |
| 1-13 | Monastero del Corpus Domini | Lucrezia Borgia | 44.831886 | 11.625972 | 155 | civico VIA CAMPOFRANCO 1 |
| 1-14 | Monastero di Sant'Antonio in Polesine | Beata Beatrice II d'Este | 44.827233 | 11.623986 | 541 | civico VIA DEL GAMBONE 15 — indirizzo fornito da Pietro |
| 1-15 | Palazzo Schifanoia | Francesco del Cossa | 44.830497 | 11.628963 | 535 | civico VIA SCANDIANA 23 |
| 1-16 | Palazzo Bonacossi | Pellegrino Prisciani | 44.832026 | 11.628927 | 170 | civico VIA CISTERNA DEL FOLLO 5 |
| 1-17 | Palazzina Marfisa d'Este | Marfisa d'Este | 44.833222 | 11.629726 | 147 | civico CORSO DELLA GIOVECCA 170 |
| 1-18 | Antico Ospedale di Sant'Anna (cella del Tasso) | Alfonso II d'Este | 44.832833 | 11.631272 | 129 | civico CORSO DELLA GIOVECCA 203 — indirizzo fornito da Pietro (ingresso secondario: Rampari di San Rocco 15) |
| 1-19 | Piazza Ariostea e colonna | Napoleone e l'età francese | 44.84125 | 11.62647 | 1010 | baricentro dei civici di Piazza Ariostea (centro della piazza, stimato) |
| 1-20 | Palazzo Massari (Museo Boldini) | Giovanni Boldini | 44.842084 | 11.624949 | 152 | civico CORSO PORTA MARE 9 |
| 1-21 | Palazzo dei Diamanti (Pinacoteca) | Biagio Rossetti | 44.84206 | 11.621244 | 292 | civico CORSO ERCOLE PRIMO D'ESTE 21 |
| 1-22 | Quadrivio degli Angeli (Palazzo Prosperi-Sacrati) | Ercole I d'Este | 44.842052 | 11.621374 | 10 | punto medio fra Corso Ercole I d'Este 21 e 32 (centro dell'incrocio, stimato) |
| 1-23 | Palazzo Turchi di Bagno e Orto Botanico | Antonio Musa Brasavola | 44.842045 | 11.621503 | 10 | civico CORSO ERCOLE PRIMO D'ESTE 32 |
| 1-24 | Museo del Risorgimento e della Resistenza | Tancredi Mosti Trotti Estense | 44.84182 | 11.620847 | 57 | civico CORSO ERCOLE PRIMO D'ESTE 19 |
| 1-25 | Casa di Ludovico Ariosto | Ludovico Ariosto | 44.844362 | 11.616865 | 422 | civico VIA LUDOVICO ARIOSTO 67 |
| 1-26 | Porta degli Angeli e mura nord | Giulio Natta | 44.848871 | 11.624953 | 811 | civico CORSO ERCOLE PRIMO D'ESTE 152 — ultimo civico del corso, presso la Porta degli Angeli |
| 1-27 | Certosa: chiostro, monumento a Teodoro Bonati | Teodoro Bonati | — | — | — | monumento nel chiostro della Certosa, senza civico: punto da posizionare a mano |
| 1-28 | Cimitero ebraico | Giorgio Bassani | 44.84281 | 11.62999 | 782 | civico VIA DELLE VIGNE 20 |
| 1-29 | Certosa: cimitero monumentale | Michelangelo Antonioni | 44.844161 | 11.625337 | 396 | civico VIA BORSO 1 — ingresso della Certosa |
| 1-30 | Certosa: chiesa di San Cristoforo | La città (P93, proposta) | — | — | — | la chiesa di San Cristoforo non ha un numero civico proprio: punto da posizionare a mano sulla facciata |

**Da posizionare a mano (nessun civico):** 1-27 (monumento a Bonati nel chiostro della Certosa) e 1-30 (facciata della chiesa di San Cristoforo).

**Lunghezza.** Circa 8.1 km in linea d'aria, esclusi i due punti non ancora posizionati.

**Tratti più lunghi da valutare:**
- 1-10 → 1-11: circa 360 m;
- 1-13 → 1-14 e 1-14 → 1-15: circa 540 m ciascuno;
- 1-18 → 1-19: circa 1 km;
- 1-25 → 1-26: circa 800 m.

**File per programmi GIS:** `videogioco-5-duchi-anno1-tappe.geojson`, con i punti e la linea del percorso. Si apre in QGIS, uMap o geojson.io.

**Bozza grafica:** `videogioco-5-duchi-anno1-bozza-mappa.png`. I punti grigi sono i 14.407 civici del centro, che fanno emergere la forma degli isolati; sopra ci sono le tappe numerate collegate in linea d'aria.

## 4. La pianta unica

**Proposta.** Una **pianta schematica disegnata apposta**, in formato SVG. Si ricava dai dati di OpenStreetMap e del Comune e contiene solo:

- il perimetro delle mura;
- le strade principali;
- gli isolati in grigio chiaro;
- il Castello e il Po di Volano come riferimenti;
- i 30 punti del percorso.

**Perché:**

- è leggera (poche decine di kB);
- si legge bene anche sul telefono;
- non dipende da servizi esterni;
- è coerente con lo stile simbolico delle carte (`gioco` §3);
- si può "annebbiare" tessera per tessera.

**Alternativa.** Usare come pianta unica quella di Andrea Bolzoni (1747), in pubblico dominio: è molto bella, ma mancano gli edifici successivi (Teatro Comunale 1798, stadio, MEIS) e sul telefono si legge male. Può comparire come immagine dentro un approfondimento.

---

## 4bis. Prototipo della mappa (v0.5)

File: `videogioco-5-duchi-anno1-prototipo-mappa.html`. È una pagina singola, senza dipendenze esterne, di circa 190 kB.

Come è fatta:

- **Pianta.** Ci sono 16.582 civici del centro, disegnati come punti su canvas: formano gli isolati. Le 23 vie principali hanno l'asse ricavato dai civici (media per tratti di 40 m lungo la direzione principale) e un'etichetta.
- **Nebbia.** Sono visibili solo i punti entro 120 m dalle tappe aperte. Il percorso compare man mano.
- **Pannello della tappa.**
  - Contenuto: personaggio, periodo, epoca, etichetta di attendibilità, linea del tempo con i personaggi già incontrati, argomento del livello, aggancio, domanda critica.
  - Dopo la soglia, simulata con un pulsante: il rimando, il pulsante per la tappa successiva e le visioni di Borso A1 e A2 in sequenza.
- **Interazione.** Spostamento e zoom con trascinamento e rotella o pizzico. Tema chiaro e scuro.
- **Posizioni provvisorie.** Le tappe 1-27 e 1-30 (cerchio tratteggiato) sono vicine all'ingresso della Certosa, solo nel prototipo.
- **Mura (v0.6).** Il perimetro è **tracciato a mano da Claude**, perché OpenStreetMap non è raggiungibile né dal cloud né dal computer di Pietro. Il tracciato è ricostruito dai civici, distinguendo le vie interne alla cinta (Rampari di San Rocco e di San Paolo, via Mura di Porta Po, via Carlo Mayr, via Porta d'Amore, i capi di corso Ercole I d'Este, corso Porta Mare e corso Porta Po) da quelle esterne (via dei Baluardi, viale Alfonso I d'Este, via Porta Catena, via Pomposa, corso Piave, via Bologna, via Porta Romana). Sul lato ovest, dove le mura non esistono più, il tracciato segue corso Isonzo. Risultato: poligono di 24 vertici, perimetro di circa 8,2 km (le mura reali superano i 9 km, per via dei bastioni), area di circa 4,1 km², tutte le tappe all'interno. È **schematico e da verificare** con OpenStreetMap o con la cartografia ufficiale. File: `videogioco-5-duchi-anno1-mura-stima.geojson`.
- **Tappa 1-1 completa (v0.6).** Incontro, esercizi generati su 4 gradini, soglia con coerenza, carta, report esportabile, misure anti-copia. Specifica: `videogioco-5-duchi-tappa-1-01.md`.
- **Tappa 1-1 (v0.7).** Zona percorribile, pool di esercizi (4 su 20 per gradino), pausa, visioni A1 e A2.
- **Mancano:** il salvataggio fra sessioni e gli esercizi delle tappe 2–30.

**Correzione emersa dai dati.** Via Mazzini corre a sud-est della Cattedrale, verso via delle Scienze, non fra il MEIS e il Municipio. Il rimando della tappa 1-6 è stato corretto.


## 4ter. Zone delle tappe e zona percorribile (v0.7)

- **Zone.** Ogni tappa ha una zona: i punti più vicini a lei che a ogni altra tappa (cella di Voronoi), entro 150 m. Le zone **non si sovrappongono**. Nel prototipo la nebbia si dirada zona per zona.
- **Zona percorribile.** Dentro la zona, Borso si muove su una mappa a tessere in stile Pokémon. Per ora esiste solo quella della tappa 1-1 (piazza della Cattedrale, 22 × 14 tessere): Maurelio, San Giorgio (visione A1), la lapide (visione A2), leoni, cartello dell'art. 9, facciata. Dettagli in `videogioco-5-duchi-tappa-1-01.md` §3.
- **Dati.** Il JSON v0.7 ha i campi `protagonista` (Borso) e `zone` (raggio 150 m, metodo Voronoi).


## 4quater. Geometria reale e nuova mappa della città (v0.8)

- **Sagome vere degli edifici.** La mappa della città non usa più i punti dei civici. Disegna 11 185 edifici del centro storico e il **perimetro ufficiale del centro storico**, lungo le mura. Il perimetro sostituisce il tracciato stimato a mano della v0.6. Fonte: WFS open data del Comune di Ferrara (dettagli in `videogioco-5-duchi-motore-e-grafica.md`).
- **Nebbia chiara.** Le zone chiuse hanno edifici grigio-beige e un velo con nuvole che scorrono. Le zone aperte sono a colori, con bordo sfumato e tratteggio dorato. Dopo la soglia, la tappa successiva compare come «?».
- **Fluidità.** Trascinamento con inerzia, zoom morbido, pizzico e volo animato verso la tappa successiva.
- **Tappa 1-1 spostata** dal civico 9 (davanti all'Arcivescovado) a 10 m davanti al portale della Cattedrale: 44,835832 N, 11,61958 E. La zona 1 ora comprende la piazza davanti alla facciata.

## 5. Prossimi passi

1. Pietro allega i civici; si calcolano le coordinate.
2. Si disegna la pianta schematica SVG con il percorso.
3. Si rivedono i 12 agganci medi e di scena.
4. Si prototipano le prime tre tappe (Cattedrale, Loggia dei Merciai, Palazzo della Ragione) con incontro, carta e primo strumento.

---

## 6. Fonti

- Comune di Ferrara, dataset *Numeri civici* (CC BY 4.0): <https://dati.comune.fe.it/dataset/opendata-civici> (shapefile: <https://sit.comune.fe.it/geoserverckan/Ferrara/OPENDATA_CIVICI_preview/wfs?service=WFS&version=1.3.0&request=GetFeature&typename=Ferrara:OPENDATA_CIVICI_preview&outputformat=shape-zip>)
- Comune di Ferrara, *Open Data Territoriali*: <https://www.comune.ferrara.it/it/b/17343/open-data-territoriali>
- Wikipedia, voce "Vicolo del Chiozzino" (collega via Ripagrande e via Piangipane): <https://it.wikipedia.org/wiki/Vicolo_del_Chiozzino>
- Wikimedia Commons, pianta di Andrea Bolzoni (1747): <https://commons.wikimedia.org/wiki/Category:Map_of_Ferrara_by_Andrea_Bolzoni>

## 7. Registro modifiche

- **v0.8 (30/09/2026)**: mappa della città con gli edifici reali e il perimetro ufficiale del centro storico; nebbia più leggibile; navigazione fluida; punto della tappa 1-1 davanti al portale; zona 1 con geometria reale in vista 3/4.

- **v0.7 (30/09/2026)**: Borso personaggio giocante; tappa 1-30 affidata a «La città» (P93, proposta da confermare) con Brondi facoltativo; zone di Voronoi da 150 m; zona percorribile della tappa 1-1.

- **v0.6 (28/09/2026)**: perimetro delle mura tracciato a mano (stima) e disegnato nel prototipo; tappa 1-1 completa con bottega vera.

- **v0.5 (28/09/2026)**:
  - facoltativi come visioni di Borso consecutive, senza punti in più sulla mappa (R3, R4);
  - tracciato approvato;
  - prototipo HTML della mappa;
  - corretto il rimando 1-6 (via Mazzini).

- **v0.4 (28/09/2026)**:
  - Paolo Mazza facoltativo e stadio fuori dal percorso;
  - 1-26 Natta alla Porta degli Angeli, 1-27 Bonati al chiostro della Certosa;
  - coordinate ricalcolate e GeoJSON con la linea del percorso;
  - bozza grafica della mappa.
- **v0.3 (28/09/2026)**: coordinate WGS84 dal dataset dei civici.

- **v0.2 (28/09/2026)**:
  - percorso unico di 30 tappe contigue dentro le mura, non cronologico, con aggancio e forza dell'aggancio per ogni tappa;
  - approfondimenti nello stesso luogo della tappa;
  - pianta unica schematica;
  - Borso narratore incontrato all'ultima tappa;
  - rimossi luoghi esterni e strati storici.
- **v0.1 (28/09/2026)**: catena cronologica, tessere, risorse GIS.
