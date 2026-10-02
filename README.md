# I cinque duchi

Videogioco didattico per imparare l'**informatica** al liceo scientifico, opzione scienze applicate. È ambientato a **Ferrara** al tempo dei cinque duchi d'Este.

- **Autore:** Pietro Fabbri (docente A041, IIS Copernico-Carpeggiani, Ferrara), con l'aiuto di Claude (Anthropic).
- **Stato:** progettazione avanzata e primo prototipo giocabile (anno 1, tappa 1). Molte informazioni mancano ancora (vedi [Stato del progetto](#stato-del-progetto)).
- **Lingua del progetto:** italiano.

## In breve

| Voce | Scelta |
|---|---|
| Struttura | 5 anni × 30 livelli = 150 livelli, in sequenza. Ogni livello ha una soglia minima per passare al successivo e approfondimenti facoltativi |
| Programma | Ricalca almeno le Indicazioni nazionali (liceo scientifico, scienze applicate, Informatica), anno per anno, e dove possibile va oltre |
| Anno 1 | Un percorso unico di 30 tappe contigue dentro le mura di Ferrara. A ogni tappa si incontra un personaggio storico e si impara un argomento di informatica |
| Chi gioca | **Borso d'Este** si muove nella città, parla con i personaggi e immagina le "visioni" (contenuti facoltativi) |
| Quadro trasversale | Diritto → Etica → Filosofia → Psicologia → Arti. Il percorso sui cinque anni va da IO a ORDINE, ALTRO, MONDO e SENSO. L'informatica resta il centro |
| Esercizi | Pool casuali per gradino (per esempio 4 giusti su 20 equivalenti), meccanismi sempre diversi, nessuna risposta scritta |
| Punteggio | Misura il processo (coerenza dei passaggi), non solo l'esito |
| Privacy | Nessun account e nessun server. Il salvataggio è un file che lo studente consegna su Google Classroom |
| Tecnica | Pagina HTML unica, offline, con motore canvas scritto a mano. Geometria reale della città dagli open data del Comune di Ferrara |

## Come provare il prototipo

**Online:** <https://pietrofabbri.github.io/i-cinque-duchi/>. Lo pubblica GitHub Pages, che si aggiorna da solo a ogni push sul ramo `main`.

**Come funziona la pubblicazione.**
- Il workflow `.github/workflows/pages.yml` rigenera `prototipo/index.html` da `sorgenti/` e lo pubblica.
- Va attivato una volta sola: Settings → Pages → Source: «GitHub Actions».
- GitHub Pages funziona con i repository pubblici, oppure privati con un piano a pagamento (Pro). Il sito pubblicato è comunque visibile a chiunque abbia l'indirizzo.

**In locale:** apri `prototipo/index.html` in un browser (Chrome, Firefox o Safari recenti). Non serve internet.

1. Si apre la mappa della città: le zone non ancora raggiunte sono coperte dalla nebbia.
2. Premi **«Entra nella piazza»**: sei Borso in piazza della Cattedrale.
3. Parla con **San Maurelio**, risolvi gli esercizi, ricevi la carta, segui le due visioni facoltative ed esci verso la Loggia dei Merciai.

**Comandi.**
- Computer: frecce o WASD per muoverti, Maiusc per correre, spazio per parlare.
- Telefono: levetta virtuale e pulsante A.

## Come è organizzato il repository

```
README.md                  questo file
.github/workflows/         pubblicazione automatica su GitHub Pages
AGENTS.md                  istruzioni per chi lavora al progetto con un'IA (leggere per primo)
CLAUDE.md                  rimando ad AGENTS.md
FONTI-E-LICENZE.md         dati, immagini, attribuzioni e licenze
docs/                      progettazione (Markdown): è la fonte di verità
dati/                      dati strutturati (JSON, GeoJSON) usati da documenti e prototipo
prototipo/index.html       prototipo giocabile, generato da sorgenti/
sorgenti/                  codice e script che generano dati e prototipo
riferimenti/mappa-informatica/   mappa delle propedeuticità dell'informatica (2375 nodi), usata dal curricolo
```

### Documenti (`docs/`), in ordine di lettura consigliato

| # | File | Contenuto | Versione |
|---|---|---|---|
| 1 | `videogioco-5-duchi-curricolo.md` | Requisiti, quadro normativo, modello di livello, cornice dei cinque anni, elenco dei 150 livelli | 0.1 |
| 2 | `videogioco-5-duchi-schema-livelli.md` | I 150 livelli con propedeuticità verificate sulla mappa dell'informatica e 300 approfondimenti | 1.1 |
| 3 | `videogioco-5-duchi-gioco.md` | Come si gioca: ciclo di una tappa, strumenti veri, carte, memoria, Borso giocante, zone percorribili | 0.5 |
| 4 | `videogioco-5-duchi-esercizi.md` | Pool di esercizi per gradino, catalogo dei meccanismi, quantità di testo per anno, linguaggio, colori | 0.1 |
| 5 | `videogioco-5-duchi-meccaniche.md` | Salvataggio e consegna (file unico), punteggio di processo, misure contro copia, IA e screenshot | 0.3 |
| 6 | `videogioco-5-duchi-quadro-trasversale.md` | Diritto, Etica, Filosofia, Psicologia, Arti sui cinque anni; agganci per le 30 tappe dell'anno 1 | 0.1 |
| 7 | `videogioco-5-duchi-anno1-ferrara.md` | Anno 1: le otto Ferrara, classificazioni, catalogo di 93 personaggi e 32 luoghi | 0.3 |
| 8 | `videogioco-5-duchi-anno1-mappa.md` | Anno 1: il percorso unico delle 30 tappe, posizioni, zone, mappa della città | 0.9 |
| 9 | `videogioco-5-duchi-tappa-1-01.md` | Tappa 1-1 (San Maurelio, Cattedrale): la prima tappa completa, modello per le altre | 0.3 |
| 10 | `videogioco-5-duchi-motore-e-grafica.md` | Motore, fonti GIS, sistema di coordinate, rendering 3/4, nebbia, grafica dei personaggi | 0.1 |
| 11 | `videogioco-5-duchi-anno2-penisola.md` | Anno 2: la penisola attraverso le persone. Carta a strati, 30 tappe, 30 schede, il secondo protagonistto | 0.2 |
| 12 | `videogioco-5-duchi-anno3-europa.md` | Anno 3: i personaggi d'Europa. La corte di Ferrara, 30 tappe, il decreto del 1510, il Novecento recuperato con una sostituzione e un atlante | 0.4 |
| 13 | `videogioco-5-duchi-anno4-mondo.md` | Anno 4: il mondo oltre l'Europa. L'archivio di Ferrara, il pianeta a 16 strati, il registro che il giocatore costruisce, le persone senza nome | 0.5 |
| 14 | `videogioco-5-duchi-luoghi.md` | **Trasversale**: i tipi di legame fra una persona e un luogo, il criterio di eliminazione, il catalogo verificato degli anni 2-4, i buchi geografici come facoltative continentali | 0.3 |
| 15 | `videogioco-5-duchi-anno5-mondo.md` | Anno 5: il mondo contemporaneo. Il cantiere dell'Addizione Erculea, il tempo come mappa, 30 tappe con la colonna della stanza del *Furioso*, il giocatore dentro il poema | 0.4 |
| 16 | `videogioco-5-duchi-mappe.md` | **Trasversale**: il fondo geografico degli anni 2, 3 e 4, i 19 file di mappe in `dati/mappe/`, e dove si prendono — e dove non si prendono — i dettagli delle tappe | 0.4 |
| 17 | `videogioco-5-duchi-ritratti.md` | **Trasversale**: i ritratti dei 213 personaggi, la regola fra ritratto autentico ed emblema, le otto immagini respinte e le tre etichette che il gioco deve dichiarare | 0.2 |
| 18 | `videogioco-5-duchi-luoghi-edifici.md` | **Trasversale**: i 95 luoghi del gioco classificati in sette tipi, lo schema del dettaglio per luogo, la decisione su ODbL e il rilievo del terreno come risposta alle altezze mancanti | 0.2 |
| 19 | `videogioco-5-duchi-furioso.md` | **Anno 5**: i dodici filoni dell'*Orlando furioso*, la regola dei due strati (pin reale, stanza del filone), il tipo `N` del non luogo e le **trenta citazioni** dei livelli più la facoltativa `5-22F` | 0.4 |

I nomi dei file conservano il prefisso storico `videogioco-5-duchi-`, perché i documenti si citano a vicenda con questi nomi. Il titolo del gioco è **«I cinque duchi»**.

**Ordine di lettura degli anni 2, 3 e 4.** I documenti dal secondo anno in poi sono nati dopo gli altri e contengono una sezione iniziale con le decisioni prese e le questioni aperte. **Prima di costruire le tappe di quegli anni, vanno letti `anno2-penisola.md` §13, `anno3-europa.md` §13 e `anno4-mondo.md` §13**: contengono le decisioni che il lettore non può dare per scontate — in particolare il catalogo dei personaggi fuori percorso, il Novecento (anno 3) e il buco dell'Asia meridionale antica e il presente (anno 4).

**Nota sulle mappe (documento trasversale).** `videogioco-5-duchi-mappe.md` raccoglie il fondo geografico degli anni dal secondo in poi: **19 file** in `dati/mappe/`, tolti da Natural Earth (pubblico dominio) in tre scale — 110m per il mondo, 50m per l'Europa, 10m per la penisola, metà metro di risoluzione sulla costa italiana. Non sono GeoJSON: sono in un **formato a delta** con quantizzazione, e si leggono con `sorgenti/gis/mappe_lettore.py`. Sono passati per **57 controlli automatici**, che hanno trovato cinque difetti reali (fra cui la Sardegna ridotta a un segno, che a occhio non si vedeva). Il documento dice anche la cosa scomoda: le **sagome** degli edifici si prendono da OpenStreetMap, le **altezze non esistono come dato** (misurate nel 24% dei casi a Milano e nel 3% a Roma), e la regola proposta è dichiarare per ogni edificio da dove viene la sua altezza.

**Nota sui ritratti (documento trasversale).** `videogioco-5-duchi-ritratti.md` vale per tutti e cinque gli anni e dice **da dove viene l'immagine di ogni personaggio**. Dei 213 personaggi, **169 hanno un ritratto autentico** (tutti con licenza libera, 116 in pubblico dominio) e **44 hanno un emblema**: 9 collettivi che non hanno un volto unico, 9 persone viventi, 26 senza ritratto libero esistente. Tutte le immagini sono a 48×54 px, come quella di Borso, e misurano 213 kB in totale. Il punto del documento non sono i numeri: è che **una ricerca automatica può sbagliare la persona, e lo ha fatto otto volte** — ha restituito un gatto per Renata Viganò, una ceramica iraniana per i mercanti di Ferrara e una parata di soldati di oggi per i Bersaglieri del 1848. Ogni immagine accettata porta dunque un'**etichetta** (fotografia, dipinto, xilografia, miniatura, autoritratto, rilievo, immagine tradizionale) e le 45 schede giudicate portano anche il **motivo** del giudizio, in `sorgenti/art/attestazione_immagini.json`. Lo stesso documento registra il difetto più importante incontrato: un `HTTP 429` di Wikipedia era stato letto come «nessun ritratto esiste», e quindici personaggi con un ritratto celebre erano stati dichiarati senza.

**Nota sui luoghi e le sagome (documento trasversale).** `videogioco-5-duchi-luoghi-edifici.md` raccoglie **che cosa deve sapere il motore per disegnare un luogo**: impianto della piazza, materiali e colori, edifici con le loro date, e **cronologia** — perché una tappa del 1450 a Ferrara non può usare la piazza di oggi: la statua di Alessandro VII non c'era, il monumento a Vittorio Emanuele II non c'era, e il sagrato non era stato abbassato. Tre sono le notizie che conta. **Primo**: i 95 luoghi del gioco non erano in un file: sono stati letti dalle colonne «Luogo (pin)» dei documenti, e **41 di questi non hanno coordinate perché non sono luoghi** — sono porte di gioco, percorsi fra due città, o (nel quinto anno, per costruzione) situazioni come «una sala di riunione, 1983». Ogni scheda dichiara il perché, e le 54 coordinate (53 verificate più Karakorum, dichiarata `da_verificare`) registrano anche **a quale articolo di Wikipedia** il nome ha corrisposto. **Secondo**: la Q1 su ODbL è risolta — entra, ma l'obbligo di licenza scatta solo sui **database derivati**, e un gioco che disegna geometrie su schermo non ne distribuisce: codice, documenti e grafica restano del progetto. **Terzo**: alle altezze degli edifici, che non esistono come dato, si risponde con il **terreno** — quota, pendenza, esposizione e rilievo locale, misurati su SRTM con un errore medio di 12,6 m su 14 punti di altitudine nota. Il rilievo dice quanto scende la strada e da che parte guarda il pendio, che sono tre delle quattro cose che si vedono in una vista 3/4.

**Nota sull'*Orlando furioso* (anno 5).** `videogioco-5-duchi-furioso.md` porta nel quinto anno il romanzo che Ferrara ha scritto nel 1516. Il testo è l'edizione del **1928** della Biblioteca BEIC, in pubblico dominio, trascritta su Wikisource: **46 canti, 1 244 pagine del digitalizzato, 4 796 ottave indicizzate**, scaricate da uno script ripetibile e non a mano. Le altre tre fonti sono state scartate una per una, e le ragioni sono nel documento: Project Gutenberg dà solo 16 canti, Liber Liber non è estraibile, Internet Archive è un OCR rovinato. Il documento risolve anche la **Q1** sulla mappa del quinto anno con la **regola dei due strati**: il **pin** — dove il gioco si ferma — resta il luogo reale e verificato del personaggio (Chicago, Los Alamos, Rotterdam), e la **stanza** che il giocatore attraversa è quella del **filone**, che può essere un luogo che non esiste e allora si dichiara con il tipo `I` — o con il tipo **`N`**, che è la novità del 02/10/2026 e vale per i **non luoghi**: cose che non sono «qui né altrove», come «l'aria sopra la foresta». La regola dei due strati è **ratificata** e scritta nei dati: `dati/luoghi_gioco.json` porta il blocco `tappe` con i trenta binomi pin/stanza, e due controlli automatici (**F14**: una stanza `I` o `N` non ha coordinate; **F15**: pin e stanza ci sono per tutte e trenta le tappe e combaciano con la citazione). Le **trenta tappe** hanno ciascuna **una citazione del poema** con una parafrasi breve, e tutte sono state verificate riestraendole dal testo: 30 citazioni, 82 versi, **0 problemi**, quindici legami `A`, dieci `S`, quattro `I`, un `N**. Una **trentunesima citazione è facoltativa** (`5-22F`, la conversione di Ruggiero) e si apre dalla tappa 5-22. Il riscontro con l'altra edizione (23 citazioni confrontate su 30) ha trovato tre differenze — un verso in più, un apostrofo eliso, una variante di accordo — e nessuna cambia l'insegnamento della tappa. Il difetto più instructive del lavoro è finito nel documento e nel codice: i numeri di riga sbagliavano **53 versi sui 78 della prima stesura** per colpa della *rima extranea*, e il metodo giusto è il **frammento distintivo** invece del numero.

**Nota sui luoghi (documento trasversale).** `videogioco-5-duchi-luoghi.md` vale per tutti e cinque gli anni e va letto **prima di assegnare un luogo a una tappa**. La sua regola è che ogni associazione fra una persona e un luogo dichiara un **tipo di legame** — `B` biografico, `A` dell'azione, `S` simbolico, `I` interpretativo (solo per i luoghi che non esistono), `C` di crescita — e deve superare un test: la frase «questa persona è legata a questo luogo» deve essere vera **senza metafore**, perché «se il luogo è sostituibile, non è un luogo». Nel quinto anno i luoghi fantastici (Paradiso terrestre, Luna, castello di Atlante, isola di Alcina, regno di Logistilla, valle del Senno) sono gli unici che ammettono il tipo `I`, e sono gli unici **senza coordinate**: vanno disegnati a mano e il gioco dichiara che non sono reali.

**Nota sul quinto anno.** L'anno 5 non si sposta sulla mappa: **si sposta nel tempo**. La mappa è il cantiere dell'Addizione Erculea ad Alfonso II, e le tappe sono i 30 metodi numerici dello schema; i sei strati superiori (`S90`–`S95`) sono **volutamente vuoti** e si aprono solo alla tappa 5-30. È l'unico anno in cui una tappa è un'operazione e non un luogo.

**Nota sul quarto anno.** L'anno 4 è l'anno in cui i livelli sono l'astrazione, i modelli, gli archivi, le tabelle, le query e la protezione dei dati. Per questo il documento di progetto è costruito sulla metafora dell'archivio: il giocatore non viaggia, **cataloga trenta documenti** e alla fine stampa il registro, in cui una riga resta vuota (`anno4-mondo.md` §7).

### Dati (`dati/`)

| File | Contenuto |
|---|---|
| `videogioco-5-duchi-livelli.json` | I 150 livelli (stesso contenuto di `schema-livelli.md`) |
| `videogioco-5-duchi-anno1-personaggi.json` | 93 personaggi, 32 luoghi, epoche e legende dell'anno 1 |
| `videogioco-5-duchi-anno1-mappa.json` | Le 30 tappe: luogo, personaggio, coordinate, aggancio, rimando, visioni |
| `videogioco-5-duchi-anno1-tappe.geojson` | Tappe e percorso in GeoJSON |
| `videogioco-5-duchi-anno1-mura-stima.geojson` | Perimetro delle mura stimato a mano (superato: ora si usa il perimetro ufficiale, vedi `sorgenti/gis/citta_centro.json`) |
| `videogioco-5-duchi-anno1-zona1.json` | Zona percorribile della tappa 1: edifici con altezze, falde, aree pedonali |
| `mappe/mondo_110_*.json` | Fondo del mondo per gli anni 4 e 5: paesi, terre emerse, regioni fisiche, fiumi, laghi (scala 110m) |
| `mappe/europa_50_*.json` | Fondo dell'Europa per l'anno 3: paesi, terre emerse, regioni fisiche, unità amministrative, 186 città (scala 50m) |
| `mappe/penisola_10_*.json` | Fondo della penisola per l'anno 2: coste, Paesi confinanti, 622 unità d'Italia, 212 città, fiumi, laghi, regioni fisiche (scala 10m) |

**I file in `dati/mappe/`** sono in un formato a delta e **non** sono JSON valido: si leggono con `sorgenti/gis/mappe_lettore.py`, che restituisce coordinate in gradi decimali. La fonte è Natural Earth, **pubblico dominio**: nessuna attribuzione richiesta. Il formato e la scelta della fonte sono descritti in `videogioco-5-duchi-mappe.md`.

I dati degli anni 2, 3 e 4 (`videogioco-5-duchi-anno2-*.json`, `videogioco-5-duchi-anno3-*.json`, `videogioco-5-duchi-anno4-*.json`) **non esistono ancora**: sono da generare dagli omonimi documenti in `docs/`, che ne indicano lo schema. Per l'anno 4 il primo file da progettare è `videogioco-5-duchi-anno4-registro.json`, cioè i campi del registro: tutto il resto dell'anno dipende da quello (`anno4-mondo.md` §7.2).

## Rigenerare il prototipo

Servono **Python 3** e **Pillow** (per la grafica). Da `sorgenti/`:

```bash
python3 art/sprites.py && python3 art/facciata.py 1.446 && python3 art/ritratti.py   # da sorgenti/art/
python3 gis/zona1_build.py && python3 gis/zona1_pack.py                             # da sorgenti/
python3 build_mappa_html.py                                                          # scrive ../prototipo/index.html
```

I test automatici (`sorgenti/test/*.js`) usano Playwright e giocano la tappa 1 dall'inizio alla fine.

### Controlli di coerenza

Il progetto non controlla solo il codice: controlla **se i documenti si raccontano bene fra loro**.

```bash
python3 sorgenti/furioso/verifica_citazioni.py     # le 30 citazioni sono davvero nel testo
python3 sorgenti/furioso/verifica_citazioni.py --gutenberg   # riscontro sull'altra edizione
python3 sorgenti/verifica_coerenza.py              # versioni, file citati, cifre dichiarate, tappe, personaggi
```

`verifica_coerenza.py` è nato da un controllo fatto a mano che trovava **diciannove problemi** in un colpo solo: otto rimandi di versione fermi a prima della revisione del documento che puntavano, un `legame I` su un luogo che esiste, otto immagini respinte che erano otto e non sette, un conto di licenze arrotondato su gruppi che nei dati non esistono. Sono tutti corretti, e tutti i tipi di errore hanno il loro controllo.

Se il checkout è parziale — cioè se ci sono file che stanno solo sul ramo remoto — il controllo dei file citati va fatto con l'elenco del repository:

```bash
gh api "repos/pietrofabbri/i-cinque-duchi/git/trees/main?recursive=1" --jq '.tree[].path' > /tmp/albero.txt
python3 sorgenti/verifica_coerenza.py --elenco /tmp/albero.txt
```

I file che un documento dichiara **da produrre** non sono un problema: sono distinti dai file mancanti, perché la differenza fra «non esiste» e «non esiste ancora» è tutta la differenza.

## Stato del progetto

**Fatto**
- curricolo e schema dei 150 livelli;
- anno 1: narrazione, personaggi, percorso delle 30 tappe con coordinate;
- anno 2: carta a strati, 30 tappe e 30 schede (documento di progetto);
- anno 3: la corte come centro, 30 tappe e 30 schede (documento di progetto);
- anno 4: l'archivio come centro, 30 tappe e 30 schede, il registro che il giocatore costruisce (documento di progetto);
- la regola dei luoghi, valida per tutti e cinque gli anni: cinque tipi di legame, il criterio di eliminazione, il catalogo verificato degli anni 2-4;
- tappa 1 giocabile.

**Da fare, in ordine**
1. **Decidere la licenza ODbL** (`mappe.md` §10 Q1): è la decisione che sblocca le sagome degli edifici fuori Ferrara, e quindi le trenta zone percorribili. Senza, gli edifici vengono dal WFS comunale, che esiste solo per Ferrara
2. **Verificare i 90 pin** degli anni 2, 3 e 4 contro i file di `dati/mappe/`: sono coordinate scritte a mano e questa è la prima volta che si può controllarle
3. ~~**Decidere la mappa del quinto anno**~~: **fatto e ratificato il 02/10/2026**. La regola dei due strati vale: il pin resta reale e verificato, la stanza è quella del filone, e i dati la portano nel blocco `tappe` di `dati/luoghi_gioco.json` con due controlli automatici.
4. **Decidere il vuoto del Novecento** (anno 3, §13 Q1): è la decisione che condiziona gli anni 3–4.
5. **Decidere il buco dell'Asia meridionale antica e il presente** (anno 4, §13 Q1 e Q2): un anno che si intitola «il mondo oltre l'Europa» non può lasciare fuori l'India antica.
6. **Verificare il decreto di espulsione degli ebrei del 1510** (anno 3, §12 V1) prima di qualunque uso didattico.
7. Verifiche storiche degli anni 2, 3, 4 e 5, le **quattordici verifiche sui luoghi** (`luoghi.md` §7): **V9** (la parentela di Agramante) e **V10** (il dipinto di Caravaggio alla Brera) sono **chiuse il 02/10/2026**: Agramante è figlio di Troiano e «padre di Bradamante» è dichiarato errato; il dipinto di Caravaggio alla Brera è la **Cena in Emmaus** del 1606. Insieme a loro sono chiuse **V8**, **V12**, **V13** e **V14**.
8. **Applicare le correzioni geografiche** di `luoghi.md` §3 agli elenchi degli anni 2, 3 e 4: in particolare il **pin di Mansa Musa** in `anno4-mondo.md` (Cairo, non Timbuctù) e **Marconi** (Pontecchio, non Bologna).
9. Migliorare la parte didattica della tappa 1.
10. Tappe 1-2 … 1-30.
11. Coordinate delle tappe 27 e 30.
12. Generare i dati degli anni 2, 3 e 4 in `dati/`, iniziando dal registro dell'anno 4, e poi `videogioco-5-duchi-luoghi.json`.
13. Ricerca dei ritratti: i **150** ritratti ancora non guardati a vista (`ritratti.md` §6) e i **44** emblemi, che non esistono ancora.
14. I **tre fogli di controllo** del taglio automatico delle immagini (`ritratti.md` §5): sono l'unica cosa che quel documento non può sapere da solo.
15. Strumento del docente.
16. Modalità accessibile.

**Decisioni in sospeso:** vedi le sezioni «Questioni aperte» di ciascun documento. In particolare: la tappa 1-30 affidata a «La città» (P93), gli agganci trasversali da confermare, il formato del file di consegna, e — dal 01/10/2026 — il catalogo dei personaggi fuori percorso (anno 2 §13 Q6) e la licenza dei dati di OpenStreetMap (`mappe.md` §10 Q1). **Chiusi il 02/10/2026**: il Novecento (anno 3 §13 Q1), l'Asia meridionale antica (anno 4 §13 Q1), la mappa del quinto anno e l'ingresso del tipo di legame `C` (`luoghi.md` §8 Q1 e Q2), e i due problemi di disegno delle stanze senza coordinate (`furioso.md` §8).
