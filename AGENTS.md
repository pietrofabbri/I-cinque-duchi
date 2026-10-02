# Istruzioni per chi lavora al progetto (persone e IA)

Questo file serve a chiunque riprenda il lavoro senza il contesto delle conversazioni in cui è nato, per esempio un'altra IA o un altro progetto di Claude. Va letto prima di modificare qualsiasi cosa.

## 1. Che cos'è

«I cinque duchi» è un videogioco didattico per insegnare informatica in un liceo scientifico, opzione scienze applicate: 5 anni, 30 livelli per anno. Il committente e autore è **Pietro Fabbri**, docente di informatica (classe di concorso A041) a Ferrara. Parti dal `README.md` per il quadro generale e l'elenco dei documenti.

## 2. Fonte di verità e ordine di lettura

1. `docs/` è la **fonte di verità**. `dati/` contiene gli stessi contenuti in forma leggibile dai programmi. `prototipo/` si genera da `sorgenti/`.
2. Ordine di lettura: `README.md` → `docs/videogioco-5-duchi-gioco.md` → `docs/videogioco-5-duchi-esercizi.md` → il documento del tema su cui lavori. Per gli anni 2, 3, 4 e 5, leggi prima la sezione §0 e le questioni aperte del documento dell'anno: contengono decisioni prese e limiti che non si possono dare per scontati. **Prima di assegnare un luogo a una tappa, leggi `docs/videogioco-5-duchi-luoghi.md`**: è trasversale e vale per tutti e cinque gli anni. **Prima di scrivere un livello linguistico, leggi `docs/videogioco-5-duchi-lingue.md`**: è trasversale, vale per tutti e cinque gli anni, e contiene i 900 titoli con la loro provenienza. **Prima di scegliere un'immagine per un oggetto o per un testo autentico, leggi `docs/videogioco-5-duchi-lingue-immagini.md`**: contiene la regola delle quattro categorie, le etichette, la misura 96×72 e i sette controlli.
3. Se due documenti si contraddicono, vale quello con la data più recente. Conviene segnalare la contraddizione a Pietro.

## 3. Decisioni di Pietro da rispettare (non cambiarle senza chiedere)

**Struttura**
- **30 livelli per anno**, in sequenza. Ogni livello ha una **soglia minima** per passare al successivo e **due approfondimenti facoltativi**, che non sono mai propedeutici a nulla.
- **Nessuna competenza in ingresso presupposta.** Ciò che non è informatica ma serve, il gioco lo costruisce.
- **Una sola modalità di gioco.** Si gioca sempre, anche a casa, e occasionalmente in classe.

**Anno 1**
- Un **percorso unico**: 30 tappe contigue dentro le mura di Ferrara, non cronologiche. Ogni personaggio rimanda al successivo solo dopo la soglia.
- **I facoltativi sono "visioni di Borso"**: consecutive, senza nuovi punti sulla mappa, in tono seppia.
- **Borso d'Este è il personaggio giocante.** Gli altri personaggi parlano **solo di sé e della propria epoca**, mai di Borso.
- **Zone percorribili** in vista dall'alto 3/4, stile GBA, con la geometria reale della città. Le zone non si sovrappongono: sono celle di Voronoi entro 150 m.

**Anno 2** (decisioni del 01/10/2026, vedi `anno2-penisola.md` §0.1)
- **Ercole I è il personaggio giocante**, come Borso nell'anno 1.
- **Carta d'Italia a strati**: la pianta della penisola in orizzontale, una colonna di 12 strati in verticale. Ogni tappa è un **pin** letto a una certa profondità. I personaggi che agiscono fuori dalla penisola entrano da una **porta** (la notizia che arriva a Ferrara).
- **30 personaggi obbligatori**, uno per livello; gli altri sono facoltativi o di atlante.
- **Nessun vincolo di monotonia degli strati**: il percorso scende e risale, perché l'ordine dei livelli è degli argomenti, non degli anni.

**Anno 3** (decisioni del 01/10/2026, vedi `anno3-europa.md` §0.1)
- **Dal terzo anno il duca non è il personaggio giocante ma la guida.** Chi gioca attraversa; il duca commenta e non viaggia mai. La regola «il duca è il personaggio giocante» vale per gli anni 1 e 2, non per il 3.
- **La corte di Ferrara è l'unico luogo percorribile.** Ogni tappa è una **risorsa che arriva** sulla tavola (ambasciatore, volume, opera, orefice, musica, carta geografica, mestiere). Le risorse di fuori entrano da una **porta**.
- **Carta d'Europa a strati**, con 15 strati. Alfonso **non sa** ciò che arriva dalle epoche che non ha vissuto, e il gioco lo dichiara.
- **Le 30 tappe coprono tutta l'Europa, da Atene a Torino.** Da cui una conseguenza da tenere presente: il Novecento **non ha tappe obbligatorie** (vedi `anno3-europa.md` §13 Q1).
- **Il decreto di espulsione degli ebrei del 1510** entra nel gioco con la fonte, confrontando tre voci (vedi `anno3-europa.md` §5, «3.10 bis»). **Non usarlo finché la verifica V1 non è fatta.**

**Anno 4** (vedi `anno4-mondo.md` §0.2–§3.5)
- **L'archivio della corte è l'unico luogo percorribile**, come la corte nell'anno 3. Ogni tappa è **un documento che entra** e che il giocatore **cataloga**: tavoletta, papiro, iscrizione, registro, lettera, diagramma. L'unità di gioco non è la risorsa, è il documento.
- **Il giocatore costruisce un registro**: ogni tappa deposita una riga con i campi `id`, `titolo`, `autore`, `data`, `luogo`, `strato`, `porta`, `tradotto_da`, `manca`, `attendibilita`. I campi `tradotto_da` e `manca` sono l'innovazione dell'anno. Alla tappa 4-30 il registro si stampa e **una riga resta vuota**.
- **Il pianeta a strati** con 16 strati `S60`–`S75`, in **scala logaritmica dichiarata**; due strati sono vuoti per costruzione (`S60`, prima delle città: non ci sono documenti; `S66`, India antica: scelta da rivedere).
- **Le sette porte** dell'archivio (`PT-SCR`, `PT-ORR`, `PT-CRR`, `PT-MAR`, `PT-REG`, `PT-LAB`, `PT-VOC`) dicono **come** è arrivato ogni documento. `PT-VOC` non si apre mai prima della fine.
- **Ercole II non viaggia e non sa**: commenta il documento, e la sua domanda è «a chi serve?». Non spiega mai la tappa.
- **La regola dei ritorni è più stretta**: il materiale dell'anno 4 contiene molti nomi già obbligatori negli anni 1–3 (Omero, Cesare, Marco Polo, Colombo, Leonardo, Gutenberg, Maometto, Carlo Magno…): nessuno di questi può essere obbligatorio nell'anno 4 (`anno4-mondo.md` §6.4).
- **Due questioni aperte bloccanti**: il buco dell'Asia meridionale antica (§13 Q1) e il peso del presente (§13 Q2).

**Anno 5** (decisioni del 01/10/2026, vedi `anno5-mondo.md` §0.2–§3.6)
- **Il quinto duca è Alfonso II d'Este, e il luogo è un cantiere**: la sala da progetto degli ingegneri ducali davanti alla pianta dell'**Addizione Erculea** (1592). È l'unico luogo percorribile dell'anno.
- **Il principio zero cambia oggetto**: non è il mondo a non esistere, è **il tempo**. Nessuno dei trenta personaggi sapeva che cosa sarebbe successo dopo, e il gioco, che sa, **non può dirlo**.
- **Ogni tappa è un numero, e il numero è sbagliato.** Regola non negoziabile: **nessun numero può essere mostrato senza il suo errore accanto**, e la domanda non è quanto hai indovinato ma **da quanto ti sei sbagliato e da che cosa dipende**.
- **Il tempo è la mappa**: sedici strati `S80`–`S95`, di cui **sei sono vuoti** (`S90`–`S95`, dal 2026 in poi) e restano **fasce bianche** per tutta la partita.
- **Le sette porte** sono `PT-LAB`, `PT-PAP`, `PT-MAT`, `PT-CAB`, `PT-CIT`, `PT-URB` e **`PT-FUT`, che non porta niente** e si apre solo alla tappa 5-30.
- **Il deliverable è la carta delle stime**: trenta righe con `livello`, `metodo`, `valore`, `errore`, `distanza`, `ipotesi`, `incertezza`, `porta`, `attendibilita`, `firma` — **più** le sei previsioni con la data.
- **Alfonso II non vede la fine del proprio progetto**: muore nel 1597 e nel 1598 il ducato passa al papato. È la prima volta nel gioco che la guida non attraversa la propria storia.
- **Sei persone viventi su trenta** (Fei-Fei Li, LeCun, Buolamwini, Hinton, Gebru, Hassabis): solo emblema, scheda `in formazione`, **nessuna affermazione di correttezza**.
- **Nessuna frase che contenga il futuro come dato**: non «l'IA sostituirà molti lavori» ma «dal 2015 esistono sistemi che scrivono testi».
- **Personaggi** `Q301`…`Q330`. Codici definitivi fino a nuova indicazione.

**Regola dei luoghi** (trasversale, vedi `luoghi.md`, valida dal 01/10/2026)
- **Ogni associazione fra una persona e un luogo dichiara un tipo di legame**: `B` biografico (nato, vissuto, morto lì), `A` dell'azione (lì è successo qualcosa di decisivo), `S` simbolico (il luogo fa capire l'eredità), `I` interpretativo (solo per i luoghi che **non esistono**), `C` di crescita (cresciuto lì, non nato).
- **La prova da superare**: la frase «questa persona è legata a questo luogo» deve essere vera **senza metafore**. Se devo ricorrere a «gli ricorda», «evoca», «è il simbolo», il legame non passa.
- **Il criterio è l'eliminazione, non l'inclusione**: se un altro luogo funzionerebbe uguale, non è un luogo. «Meglio 60 associazioni solidissime che 150 ottenute per analogia».
- **Un solo pin per tappa**, in tutti e cinque gli anni. Le associazioni multiple finiscono in `altri_luoghi`.
- **I luoghi fantastici non hanno coordinate** (Paradiso terrestre, Luna, castello di Atlante, isola di Alcina, regno di Logistilla, valle del Senno): vanno disegnati a mano sulla carta del gioco, con un segno dedicato, e **il gioco dichiara che non sono reali**. È l'unica eccezione alla regola dei pin.
- Un toponimo inesistente non entra nel catalogo finché non esiste come luogo reale.

**Mappe e dati geografici** (trasversale, vedi `mappe.md`)
- **Il fondo geografico degli anni 2, 3 e 4 è in `dati/mappe/`**: 19 file tolti da Natural Earth (pubblico dominio) in tre scale — 110m mondo, 50m Europa, 10m penisola.
- **I file di `dati/mappe/` NON sono JSON valido.** Sono in un formato a delta con quantizzazione, e si leggono **solo** con `sorgenti/gis/mappe_lettore.py`, che restituisce coordinate in gradi decimali. Non usare `json.load` su questi file.
- **Prima di assegnare un pin a una tappa degli anni 2, 3 e 4, verificalo** con `sorgenti/gis/punto_in_poligono.py`: il pin deve cadere nel Paese e nell'unità amministrativa che il documento dichiara. Sono 90 coordinate scritte a mano e la verifica non è ancora stata fatta.
- **Le altezze degli edifici non sono un dato disponibile**: misurate nel 24% dei casi a Milano e nel 3% a Roma. Ogni edificio che ne usa una deve dichiarare la fonte (`lidar`, `osm`, `stimata`), come fanno i campi `attendibilita` e `manca` del registro dell'anno 4.
- **OpenStreetMap è ODbL e non è ancora autorizzato** (`mappe.md` §10 Q1). Non scaricare dati OSM finché Pietro non ha deciso.
- Per rifare le mappe: `scarica_ne.py`, poi `mappe_formato.py`, poi **sempre** `verifica_mappe_numeriche.py`: dà 57 controlli e ne ha già trovati cinque difetti invisibili a occhio.

**Luoghi e sagome** (trasversale, vedi `luoghi-edifici.md`)
- **Ogni luogo ha un `tipo`** fra sette, e il tipo decide come si disegna: `citta`, `citta_antica`, `edificio`, `area`, `percorso`, `situazione`, `porta`. **`situazione` e `porta` non hanno coordinate e non si disegnano**: nel quinto anno la casella «Luogo (pin)» contiene una situazione (tappe 5-18, 5-22, 5-24…), e le porte `PT-*` sono uscite dal nodo, non strade.
- **Ogni scheda dichiara lo stato della coordinata** (`verificata`, `non_e_un_luogo`, `da_geocodificare_wfs`, `da_geocodificare_a_mano`) e **l'articolo a cui il nome ha risolto**. Nessuna coordinata manca in silenzio: un vuoto non dichiarato è una bugia.
- **Il dettaglio di un luogo ha sei campi**: `impianto`, `materiali`, `edifici`, `cronologia`, `terreno`, `vuoto`. Il campo `cronologia` non è decorativo: una tappa nel 1450 non può usare la piazza di oggi. Il campo `vuoto` dice **che cosa non si sa**, e va riempito come gli altri.
- **Un campo vuoto non si stima.** Le dimensioni in metri di una piazza, se la fonte non le dà, restano vuote. Il default tipologico lo sceglie il motore e lo dichiara.
- Il file dei luoghi si **rigenera** con `python3 sorgenti/luoghi/estrai_luoghi.py` e poi `classifica.py`: non si scrive a mano, perché un inventario scritto a parte diverge dai documenti, e un inventario che diverge è falso. **La tabella delle colonne va riletta** quando un documento cambia: nel 4º anno la colonna si chiama `Pin` e non `Luogo (pin)`, e la prima versione leggeva la colonna sbagliata trovandosi trenta nomi di persone al posto di trenta luoghi.
- **Il rilievo si misura, non si stima**: `sorgenti/gis/rilievo.py`, verificato su 14 punti ad altitudine nota con errore medio di 12,6 m. Non usare `lon mod 16` per il pixel dentro un tassello: è l'indice di un tassello, non di un pixel (256 pixel, non 16).
- **OpenStreetMap è autorizzato dal 02/10/2026** e i dati derivati viaggiano con ODbL e l'attribuzione «© OpenStreetMap contributors». Il codice del gioco non è obbligato a licenza libera.

**L'*Orlando furioso* nel quinto anno** (vedi `furioso.md`)
- **Il testo è l'edizione 1928** della Biblioteca BEIC, trascritta su Wikisource, **in pubblico dominio**, e si scarica con `python3 sorgenti/furioso/scarica_wikisource.py`. Non usare Project Gutenberg (solo 16 canti), né Liber Liber (non estraibile), né Internet Archive (OCR rovinato). Le tre scelte e i loro motivi sono nel documento, §1.1.
- **Il testo vive nella zona `Pagina:`**, non nelle pagine dei canti: `prop=extracts` su `Orlando furioso (1928)/Canto N` restituisce **zero caratteri** senza alcun errore. Si scarica `Pagina:<volume>/<n>` con `prop=revisions&rvslots=main`, in lotti da cinquanta.
- **Una citazione del *Furioso* non si scrive a memoria.** I versi si prendono dall'indice e si scrivono in `dati/furioso/citazioni.json` con `costruisci_citazioni.py`; si verificano con `verifica_citazioni.py`. Il verso si individua con un **frammento distintivo**, mai con un numero di riga: la *rima extranea* (metà delle ottave ne ha sette versi, non otto) sposta tutti i numeri, e i numeri di riga sbagliavano 53 versi.
- **Un buco dichiarato non si rimappa in silenzio.** Le 44 ottave assenti e i 44 numeri ripetuti dal trascrittore restano buchi: chi tiene l'indice tiene anche l'elenco dei numeri di cui non è sicuro. Un numero spostato di uno in un canto intero non si vede.
- **Il pin e la stanza sono due cose diverse** (regola dei due strati, **ratificata** il 02/10/2026, `furioso.md` §2.2): il **pin** — il luogo dove il gioco si **ferma** — resta il luogo reale e verificato del personaggio e va sulla mappa; la **stanza** è quella del filone e può non esistere (`I`) o non essere un luogo (`N`). Una stanza di tipo `I` o `N` **con** coordinate è un errore, ed è controllato (`verifica_citazioni.py`, verifica **F14**). `dati/luoghi_gioco.json` porta il blocco `tappe`: trenta record con `pin` e `stanza`, generato da `costruisci_citazioni.py --luoghi` e controllato dalla verifica **F15**.
- **Una tappa, una ottava**: nessuna citazione può riprendere l'ottava di un'altra tappa, e nessuna può cadere su un'ottava con un difetto di trascrizione. Lo controlla lo script, non l'occhio.
- **Il legame `I` si sceglie sul luogo, non sul tono.** `I` significa «questo luogo non esiste»: se il luogo esiste, il legame è `A` o `S`, per quanto fantastica sia la citazione. I quattro luoghi ammessi come inesistenti sono dichiarati in `citazioni.json` (`luoghi_inesistenti`), e `verifica_citazioni.py` vieta qualsiasi altro `I`.
- **Esiste anche il tipo `N`, il non luogo** (dal 02/10/2026): non è un luogo che non esiste, è una cosa che non è un luogo — una condizione che si attraversa, come «l'aria sopra la foresta». Gli elenchi `luoghi_inesistenti` e `non_luoghi` devono restare **disgiunti**, ed è controllato.
- **Una facoltativa è una persona o un luogo con cui il giocatore interagisce**, e va pensata per la parte informatica della tappa che la apre. Il suo codice è quello della tappa più la lettera `F` (`5-22F`), e una facoltativa **può portare il protagonista fuori dal continente purché lo dichiari**. Codice e apertura sono controllati.
- **L'Africa del *Furioso*** è il tema più serio del quinto anno e va trattato con la regola di `luoghi.md` §6.1, **riscritta il 02/10/2026 sulla parola del testo**: il poema chiama «i Mori» il nemico e usa «barbari» solo come voce di un personaggio; «Africa» è una terra, non un nome di popolo. Il gioco non deve insegnare nient'altro su quelle righe, e non deve mai usare quelle parole come etichetta di un popolo reale.

**Immagini dei personaggi** (trasversale, vedi `ritratti.md`)
- **Due immagini, non una**: **ritratto autentico** se esiste un'immagine con licenza libera che ritrae davvero la persona; altrimenti **emblema**, che dichiara **perché** la persona non ha un volto qui. Nessuna terza via e nessun volto generato.
- **Ogni ritratto porta un'etichetta**: `fotografia`, `dipinto`, `xilografia`, `miniatura`, `autoritratto`, `rilievo`, `immagine tradizionale`, `immagine di epoca`. Un autoritratto e una fotografia non si ritagliano come una miniatura, e un visitatore deve poter capire che cosa sta guardando.
- **La misura è 48×54 px**, come `ritratto_borso.png`. I file in `sorgenti/art/out/` sono già ridotti: non vanno ridimensionati di nuovo, e il motore non deve riportarli a una misura maggiore.
- **Una ricerca automatica propone, non decide.** Un nome di file non è una prova: la ricerca ha restituito un gatto per Renata Viganò e una ceramica iraniana per i mercanti di Ferrara. Ogni immagine entra nel gioco solo dopo un attestato in `sorgenti/art/attestazione_immagini.json`, che porta etichetta e motivo.
- **Una richiesta che non arriva non è una risposta negativa.** Vale per ogni ricerca, ogni download e ogni interrogazione: se la risposta non c'è, la scheda resta `da_rivedere` e non diventa un fatto. È la regola che ha salvato quindici schede dopo che un `HTTP 429` era stato letto come «nessun ritratto esiste».
- Le 53 immagini sotto CC BY o CC BY-SA richiedono di mostrare autore e licenza: i crediti del gioco li leggono da `ritratti_disponibili.json`, campo `dettagli`, e non si scrivono a mano.

**Sistema linguistico** (trasversale, vedi `lingue.md`, decisioni del 02/10/2026)
- **Sei lingue, cinque anni, trenta livelli all'anno: 900 livelli.** Italiano, ferrarese, latino, inglese, **LIS** (lingua dei segni italiana, non una generica «lingua dei segni»), greco. I 150 livelli informatici restano 150: i due sistemi sono **distinti** e non si sommano.
- **Il CEFR è metafora per il latino e il greco**, livello reale per inglese, ferrarese e LIS. Dove compare una sigla CEFR, il documento dice in una riga se è metafora o livello reale.
- **Nessuna delle sei lingue è la versione tradotta di un'altra.** Lo stesso argomento si presenta nelle sei con strutture diverse, e la differenza è il contenuto, non un dettaglio.
- **L'anno 1 parte dal basso e il resto no**: la padronanza iniziale è quella della 2ª-3ª primaria, ma contenuti, esempi e problemi sono degni di un adolescente. Nessun testo «da bambini».
- **Ogni livello ha nove componenti**: nucleo teorico, esempi, testo autentico, esercizi di comprensione, di produzione, di trasformazione, **osservazione linguistica**, piccola sfida, e confronto filologico (facoltativo come componente, mai vuoto quando c'è). Un livello senza testo autentico non esiste.
- **L'«occhio del linguista» è in tutti i 900 livelli**, anche nei primi. È il principio trasversale: non imparare soltanto una lingua, imparare a renderti conto di come funziona una lingua. Non è valutato e non fa perdere punti.
- **I trenta livelli di ogni anno si dividono in cinque blocchi da sei**: Fondamenta, Struttura, Comprensione, Produzione, Consapevolezza linguistica. I blocchi non sono le tappe: sono un taglio interno alla sequenza dei livelli.
- **Le sei associazioni fra lingua e oggetto** sono fissate e non si cambiano: Italiano→Cibi, Ferrarese→Detti popolari, Latino→Superstizioni, Inglese→Musiche, Lingua dei segni→Artigianato tipico, Greco→Bevande. Le ragioni sono in `lingue.md` §5.1.
- **L'oggetto è FACOLTATIVO in tutti i 900 livelli**: non blocca, non dà punti, non sblocca niente. Gli esercizi dell'oggetto sono **gli stessi meccanismi** di quelli informatici, cambia solo il contenuto.
- **Le trenta voci per lingua in `dati/lingue/associazioni.json` sono PROPOSTE**, non voci confermate. Per il ferrarese la voce non è un testo ma un **campo da rilevare**: i proverbi si raccolgono, non si scrivono.
- **I 900 titoli sono in `sorgenti/lingue/`**, sei file di 150 righe, e ogni riga dichiara la sua provenienza: `titolo` (di Pietro) oppure `tema` (proposto). `titoli_livelli.txt` è un output, non un sorgente. Prima di usare un titolo, `python3 sorgenti/lingue/verifica_titoli.py` deve dare **0 problemi**.
- **Non scrivere una lingua dei segni a tavolino**, e non raccogliere proverbi ferraresi senza la regola del consenso: entrambe le cose sono questioni aperte (`lingue.md` §7 Q3 e Q4).

**Questioni aperte** (trasversale, vedi `audit.md`)
- **Tutte le questioni aperte stanno in `docs/videogioco-5-duchi-audit.md`.** Prima di aprire una discussione, guarda l'audit: è possibile che la domanda sia già chiusa in un altro documento, o che sia una delle cinque bloccanti e non si possa rispondere.
- **Cinque bloccanti, e quattro sono la stessa**: `lingue.md` Q1 (livelli linguistici o informatici), Q2 (le trenta voci confermate), Q4 (la LIS), `lingue-immagini.md` Q1 (chi guarda le immagini), e `mappe.md` §10.5 (i novanta pin, che è un **lavoro** e non una domanda).
- **L'ordine è B1 → B2 → B4**: finché non si decide se le tappe sono 30 o 150 non ha senso scegliere le immagini, e finché non sono confermate le voci non ha senso scegliere le immagini.
- **Una domanda nuova va aggiunta all'audit**, non lasciata in un documento. Se è chiusa, si sposta nel registro del documento suo e non si cancella.
- **`conta_questioni.py` confronta il proprio conto con i numeri dell'audit**: se i due non concordano, è l'audit che ha torto. Non correggere il numero a mano senza far girare lo script.

**Immagini degli oggetti linguistici** (trasversale, vedi `lingue-immagini.md`, decisioni del 02/10/2026)
- **Quattro categorie, non una**: `foto`, `dipinto`, `stampa`, `nessuna`. Un oggetto che non ha immagine libera va **dichiarato** (`nessuna`), non disegnato. Nel gioco **non entra un'immagine generata** per nessun oggetto, come per i volti.
- **Le trenta voci ferraresi non hanno immagine** e non ne possono avere: sono campi di rilevazione. Non è una ricerca saltata, è una categoria dichiarata nei dati.
- **La scheda dell'oggetto è 96×72 px** (i ritratti sono 48×54). **Le immagini non si strecano mai**: il ritaglio è ammesso solo se non toglie l'oggetto, e si dichiara sulla scheda.
- **Sotto 160×120 l'immagine non entra**, perché nel gioco verrebbe ingrandita e il gioco non ingrandisce.
- **Ogni immagine porta etichetta, autore, licenza, data e museo/inventario**: la data solo se c'è, e «non c'è» è una risposta ammessa.
- **Una ricerca che restituisce un file non ha trovato l'oggetto.** La scelta la fa una persona e si registra in `dati/lingue/attestazione_oggetti.json` con etichetta e **motivo del giudizio**. Il lavoro di ieri ne ha prodotto la prova: alla voce «la correggia» il file migliore era un pittore che si chiama Correggio, alla voce «gli occhiali» una moschea di Istanbul, alla voce «la sete» un canale a Sète.
- **Il controllo G7** segnala le voci in cui nessun candidato nomina l'oggetto: sono 67 su 146, e vanno guardate per prime. Non è un errore ed è per questo che non fa fallire `verifica_immagini_oggetti.py`.
- **Il latino non si cerca su Commons**: le fonti sono i corpus epigrafici (EDCS, EDR) e le biblioteche digitali. 27 voci latine su 28 hanno solo proposte scoperte per caso.
- **Prima di ridimensionare**, aspetta che le immagini siano scelte: ridurre prima significa buttare via il lavoro.

**Esercizi e testo**
- **Pool per gradino**: per esempio 4 esercizi giusti su una pool di 20 equivalenti, estratti a caso.
- **Meccanismi sempre diversi**: tante schermate, colori, forme.
- **Poco testo nell'anno 1**, che cresce negli anni successivi (limiti in `esercizi.md` §3).
- **Linguaggio**: trattare i ragazzi da adulti, con parole che capirebbe un bambino.

**Quadro trasversale**
- Diritto → Etica → Filosofia → Psicologia → Arti, con il percorso IO → ORDINE → ALTRO → MONDO → SENSO. Si usa **al massimo un aggancio per tappa**, mai valutato. L'informatica resta il centro.

**Punteggio, privacy, integrità**
- Il punteggio misura il **processo**.
- Nessun account e nessun server. Consegna con un file su Google Classroom.
- Nessuna sorveglianza con webcam o IA (GDPR, AI Act).

## 4. Convenzioni

**Documenti**
- Ogni `.md` ha un'intestazione YAML (`titolo`, `versione`, `data`, `autore`, `documenti collegati`) e un **registro delle modifiche** in fondo.
- A ogni modifica si aumenta la versione e si aggiunge una riga al registro.

**Codici**
- **Livelli**: `anno-numero`, per esempio `1-1`.
- **Personaggi**: `P01…P94` (anno 1). Gli anni 2, 3, 4 e 5 usano la serie `Q`, che continua senza riaprire la numerazione: `Q01…Q92` (anno 2), `Q101…Q130` (anno 3), `Q201…Q230` (anno 4), `Q301…Q330` (anno 5). **Codici definitivi fino a nuova indicazione.**
- **Luoghi**: `L01…L32`.
- **Nodi della mappa dell'informatica**: `B1.1`, `E7.3`… (vedi `riferimenti/mappa-informatica/`).
- **Attendibilità delle fonti**: D (documentato), I (interpretato), M (memoria), L (leggenda), F (figura letteraria), C (collettivo).

**Coordinate**
- WGS84. Coordinate locali in metri: `x = (lon − 11,62) · 111320 · cos(44,8375°)`, `y = (lat − 44,8375) · 110540`.
- Ogni zona percorribile ha un proprio sistema ruotato (vedi `motore-e-grafica.md` §2).

**Stile dei testi**
Italiano semplice: frasi brevi, niente gergo non spiegato, niente tono infantile.

## 5. Vincoli tecnici e di contenuto

**Tecnica**
- Il prototipo è **una sola pagina HTML**, offline, senza librerie esterne e senza richieste di rete a runtime.

**Contenuti e immagini**
- **Immagini** solo in pubblico dominio o con licenza libera, sempre attribuite in `FONTI-E-LICENZE.md`.
- Niente volti inventati per le persone reali: si usa un emblema.
- Per le persone viventi, solo emblemi.
- **Fatti storici**: verificali prima di usarli. I dubbi vanno segnati nelle schede (`note_verifica`).

**Dati**
- **Dati geografici**: open data del Comune di Ferrara (CC BY 4.0), con attribuzione.
- **Niente dati degli studenti** nel repository.

**Persistenza**
- Il progetto **non ha server e non ha account**: niente telemetria, niente salvataggio remoto, niente richieste di rete a runtime.
- **Le previsioni che il giocatore scrive nelle fasce bianche sono dati personali**: restano nel file di consegna e non vanno mai pubblicate in un repository.

## 6. Come lavorare

1. Leggi i documenti pertinenti e verifica che la modifica rispetti il §3.
2. Modifica il documento in `docs/`, poi i dati in `dati/` se servono, poi il codice in `sorgenti/`.
3. Rigenera il prototipo con `python3 build_mappa_html.py` da `sorgenti/`. Se hai Playwright, esegui i test in `sorgenti/test/`.
4. Aggiorna versione e registro modifiche dei documenti toccati e, se serve, la tabella del `README.md`.
5. **Prima di dichiarare finito, passa `python3 sorgenti/verifica_coerenza.py`**: confronta le versioni fra intestazioni, tabella del README e rimandi incrociati, controlla che i file citati esistano (i file dichiarati «da produrre» sono un caso diverso e li riconosce), e riconcilia le cifre dichiarate con i dati. Se il checkout è parziale, aggiungi `--elenco` con l'elenco dei file del ramo remoto.
6. Nel messaggio di commit, spiega **che cosa** è cambiato e **perché**.

## 7. Da sapere

- `sorgenti/gis/estrai.py` legge i dati che una sessione di Claude aveva ricevuto dal browser integrato. Il percorso è specifico di quella sessione. Per rifare l'estrazione, interroga direttamente il WFS del Comune come descritto in `motore-e-grafica.md` §1.
- `sorgenti/civici.py` e `geo.py` richiedono lo shapefile dei numeri civici del Comune di Ferrara, che non è nel repository perché pesa circa 50 MB. Senza, il build usa `sorgenti/gis/vie_etichette.json`.
