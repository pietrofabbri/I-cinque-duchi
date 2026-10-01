---
titolo: I ritratti dei personaggi — dove vengono e perché sono dichiarati
versione: 0.1
data: 2026-10-01
autore: Buffy (per pietrofabbri)
documenti collegati:
  - docs/videogioco-5-duchi-mappe.md
  - docs/videogioco-5-duchi-luoghi.md
  - AGENTS.md
  - FONTI-E-LICENZE.md
---

# I ritratti dei personaggi

## 0. A che cosa serve

Il gioco ha 213 schede di personaggio. Borso ha già un ritratto a 48×54, e
Maurelio ha una figura disegnata a mano. Gli altri 211 no.

Il progetto vieta i volti inventati per le persone reali (`AGENTS.md` §3): si usa
un **ritratto autentico** quando esiste, e un **emblema** quando non esiste o
quando la persona non può avere un volto. Maurelio è l'eccezione già prevista:
non è un ritratto, è una figura della tradizione.

Questo documento dice **quali immagini sono state scelte, con quale licenza, e
quali sono state rifiutate**. È un documento di controllo, non un catalogo da
sfogliare.

## 1. La regola: due immagini, non una

| | Ritratto autentico | Emblema |
|---|---|---|
| quando | esiste un'immagine libera che **ritrae la persona** | non esiste, o la persona non può, o l'immagine non la ritrae |
| chi decide | una ricerca automatica **proposta**, poi un attestato a vista | idem |
| dichiarazione | l'**etichetta** del ritratto (§4) | il **motivo** per cui non c'è un ritratto |
| regola del progetto | il valore di un contributo scientifico si separa dal valore della persona; qui vale lo stesso per un'immagine | nessun volto inventato |

Le schede senza ritratto non sono un difetto: sono la parte del gioco in cui si
vede che la conoscenza ha un bordo. Un emblema con la scritta «nessun ritratto
libero esiste» insegna più di un ritratto generato.

## 2. I numeri

| | |
|---|---|
| schede di personaggio | **213** |
| con ritratto autentico | **169** |
| con emblema | **44** |
| di cui collettivi (famiglie, gruppi, città, «le mani che hanno approssimato √2») | 9 |
| di cui persone viventi, che per regola hanno solo l'emblema | 9 |
| di cui senza ritratto libero esistente, verificato | 26 |
| ritratti guardati uno per uno e attestati | 19 |
| ritratti ancora da guardare a vista | 150 |
| misura | 48×54 px, come il ritratto di Borso |
| peso complessivo dei 169 file | 213 kB (media 1 258 byte) |

Le 19 licenze, tutte libere: 116 pubblico dominio, 16 CC BY-SA 3.0, 15 CC BY-SA
4.0, 4 CC0, 4 CC BY-SA 2.0, e 14 fra CC BY e CC BY-SA di versioni diverse.

## 3. La ricerca, e il suo difetto più importante

La ricerca è in tre script, e si può rifare:

1. `cerca_ritratti.py` interroga l'API di Wikipedia in blocchi da 40 titoli e
   restituisce l'immagine in testa all'articolo;
2. `cerca_ritratti_2.py` passa ai titoli scelti a mano e all'endpoint REST dei
   riassunti per chi non è stato risolto;
3. `cerca_commons.py` cerca direttamente **su Commons**, per i nomi in cui la
   ricerca su Wikipedia non trova nulla.

**Il difetto, da non ripetere.** La prima versione chiedeva 213 nomi di
seguito e, quando la risposta non arrivava, semplicemente non aveva più
immagini: scriveva allora «nessun ritratto in testa all'articolo di
Wikipedia». Ma Wikipedia risponde **HTTP 429 Too Many Requests** quando le
richieste si susseguono troppo veloce, e quel codice di errore finiva letto come
«non esiste».

Il risultato era che quindici personaggi con un ritratto celebre e documentato
venivano dichiarati privi di ritratto: Albrecht Dürer, Alan Turing, Leibniz,
John Snow, Alonzo Church, Josquin des Prez, Giovanni Bellini, Leon Battista
Alberti, Federico II, Aldo Manuzio, William Caxton, Sergej Korolëv, Riccardo
Bacchelli, Giulio Natta, Renata Viganò.

Non era un errore di ricerca. Era **un fatto falso scritto come se fosse
vero**, in un progetto la cui tesi è che i fatti vanno verificati.

La correzione è in due righe di principio, e sta in tutti e tre gli script:

- un client che aspetta un tempo minimo fra le richieste e, su 429, ascolta
  l'`Retry-After` invece di arrendersi;
- l'esito distingue `non_trovato` (risposta avuta, nessuna immagine) da
  `richiesta_fallita` (nessuna risposta). **Una richiesta fallita non genera
  mai una conclusione**: la scheda resta «da rivedere».

Lo stesso difetto è ricomparso due volte dopo, in forma diverse: una volta
perché la ricerca delle licenze cercava pagine invece che file (manca il
prefisso `File:`), e una volta perché il ciclo di scaricamento non ascoltava il
429 e sei immagini su centosessantanove finivano fuori con la scritta «download
fallito», che sembrava un file corrotto. Tutte e tre le volte la causa era la
stessa: **una risposta che non arriva è stata letta come una risposta negativa**.

## 4. L'attestazione: sette immagini respinte

Un file di ricerca può sbagliare la persona, e l'ha fatto sette volte. Il nome
del file non è una prova. Le sette, viste una per una:

| Scheda | Cosa aveva trovato la ricerca | Perché è stata respinta |
|---|---|---|
| `P80` Renata Viganò | `Renata_Viganò_gatto.jpg` | il nome della persona e il nome del gatto si somigliano in italiano. Il file ritraeva un gatto. |
| `P90` Mercanti, artigiani e cittadini | `Iranian_handicraft.jpg` | una ceramica persiana, con l'autore Reza Hajipour. Per i mercanti di Ferrara è falso. |
| `P66` I Bersaglieri del Po | `2june_2007_367.jpg` | soldati di oggi che sfilano in strada, uniformi attuali, foto del 2007. Per il 1848 è un'affermazione falsa. |
| `P88` La comunità ebraica ferrarese | `Judaica.jpg` | una fotografia d'oggetti di culto su un tavolo: non è la comunità di Ferrara, e non è nemmeno antica. |
| `P89` Gli studenti dello Studio | il convento di Santa Lucia | lo Studio è a Palazzo Paradiso: sono due cose diverse, e la somiglianza dei nomi è quello che ha fatto sbagliare la ricerca. |
| `P27` Taddeo Crivelli | una scena della Bibbia di Borso | è un'opera, non un ritratto: il miniatore non c'è. |
| `P63` Napoleone e l'età francese | David, il passaggio del San Bernardo | una scena di guerra, non un ritratto. Resta una buona immagine **di livello**. |
| `Q126` William Caxton | la xilografia di una stamperia | è l'opera di Caxton, non la sua faccia. Preziosissima come immagine di livello. |

Il giudizio è in `sorgenti/art/attestazione_immagini.json`, e non è rimesso
alla ricerca: ogni voce accettata porta **il nome del file**, l'**etichetta**
(fotografia, dipinto, xilografia, miniatura, autoritratto, rilievo, immagine
tradizionale) e **il motivo**. `applica_attestazione.py` riverifica ogni nome
su Commons prima di accettarlo: un titolo scritto a mano che non esiste porta la
scheda a emblema e lo dichiara. È successo una volta, con Cornelia.

### Le etichette servono al gioco, non alla bibliografia

Un visitatore che vede Leonardo accanto a Einstein deve poter capire che cosa sta
guardando. Un autoritratto di Bellini e una fotografia di Turing sono entrambe
immagini di due persone, ma non dicono la stessa cosa: uno ha deciso come
siamo fatti, l'altro non poteva scegliere. Le etichette separano questi casi,
e servono anche al motore: un autoritratto e una miniatura non si ritagliano
come una fotografia.

## 5. Le tre cose che non si possono sapere

1. **Le altezze non esistono come dato**, e qui non c'è rimedio: nessuna fonte
   libera e nessuna fonte a pagamento dà l'altezza degli edifici fuori Ferrara
   (misure in `mappe.md` §5). Un ritratto a 48×54 non soffre di questo, perché
   non ha bisogno di misure: soffrono le sagome degli edifici.
2. **19 fonti sono più strette di 300 pixel**, e ci sono state ridotte a
   48×54. Si vedono meno nitide e non si possono più migliorare. La
   risoluzione della fonte è registrata in `ritratti_disponibili.json`, campo
   `larghezza`, e va mostrata in fase di prova.
3. **Il taglio del viso è automatico** e non c'è riconoscimento facciale: la
   regola è una finestra con le proporzioni del riquadro, centrata sul contenuto
   e non sull'immagine. Va guardata. I fogli di controllo sono
   `sorgenti/art/provino_ritratti_1..3.png`.

## 6. Quello che resta da fare

| | |
|---|---|
| guardare a vista i **150** ritratti non ancora attestati | il primo di tutti: sono entrati senza controllo, e sette su venti sbagliati vengono da una ricerca fatta bene, non da una fatta male |
| costruire i **44 emblemi** | con la stessa regola del ritratto: ogni emblema dichiara perché la persona non ha un volto qui |
| decidere se gli emblemi siano disegni o forme tipografiche | se sono forme, l'anno 1 (maurelio) resta l'unico con disegno |
| ridare le 600 px di partenza | 300 px per le 19 fonti strette non bastano: si può solo rifare la ricerca su una fonte più grande |
| rivedere la P80 | Renata Viganò potrebbe avere un ritratto sotto un'altra forma: la ricerca su Commons non ne ha trovato |

## 7. Il registro delle modifiche

### v0.1 — 01/10/2026

Prima stesura. Creati: `cerca_ritratti.py` (v0.3, col client che ascolta il 429 e
distingue `richiesta_fallita` da `non_trovato`), `cerca_ritratti_2.py`,
`cerca_commons.py`, `ripara_licenze.py`, `applica_attestazione.py`,
`attestazione_immagini.json`, `roster.py`, `ritratto_reale.py`. Prodotti 169
ritratti a 48×54 e tre fogli di controllo.

Correzioni lungo il cammino, tutte nella stessa classe di errore:

1. il `HTTP 429` letto come «nessun ritratto»: quindici schede sbagliate;
2. la riduzione a 48×54 che non ridimensionava: i file erano di 500×562 e
   pesavano 97 kB l'uno, 14 MB in tutto, dentro un riquadro che il motore già
   dava per 48×54;
3. i nomi di miniatura (`3840px-…`) scambiati per nomi di file, e i titoli di
   Commons cercati senza il prefisso `File:`: sei immagini e otto licenze
   dichiarate assenti quando esistevano.

Esito: 169 ritratti su 213 schede, 44 emblemi, **zero** richieste fallite non
distinte da risposte negative.
