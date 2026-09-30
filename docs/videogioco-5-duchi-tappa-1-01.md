---
titolo: Videogioco "I cinque duchi" — Tappa 1-1 (San Maurelio, Cattedrale): specifica completa
versione: 0.3
data: 2026-09-30
autore: Pietro Fabbri (con Claude)
implementazione: videogioco-5-duchi-anno1-prototipo-mappa.html (sorgenti esercizi1.js, zona1.js, zona1_dati.js, incorporati dallo script build_mappa_html.py)
documenti collegati: videogioco-5-duchi-motore-e-grafica.md, videogioco-5-duchi-esercizi.md, videogioco-5-duchi-quadro-trasversale.md, videogioco-5-duchi-anno1-mappa.md, videogioco-5-duchi-gioco.md, videogioco-5-duchi-meccaniche.md
---

# Tappa 1-1 — San Maurelio alla Cattedrale

È la **prima tappa costruita per intero** e fa da modello per le altre 29.

## 1. Scheda

| Voce | Valore |
|---|---|
| Luogo | Cattedrale di San Giorgio, piazza della Cattedrale: punto della tappa 10 m davanti al portale (44,835832 N, 11,61958 E). Fino alla v0.2 era il civico 9, che sta davanti all'Arcivescovado |
| Personaggio | San Maurelio (P01), VII secolo, tradizione; attendibilità D + M |
| Chi gioca | **Borso**, che si muove nella zona e parla con i personaggi |
| Livello | 1-1 · Informazione, dato, messaggio |
| Nodo della mappa dell'informatica | `B1.1` Dato, informazione, conoscenza: differenze |
| Aggancio | Una traccia (un'iscrizione, una reliquia, una leggenda) è un dato; diventa informazione solo quando qualcuno la interpreta |
| Aggancio trasversale (chicca, non valutata) | Costituzione, art. 9: la Repubblica tutela il patrimonio storico e artistico (vedi `quadro-trasversale.md` §2.3) |
| Motto (carta) | «Il numero da solo tace; con un contesto parla; collegato ad altro, ragiona.» |
| Emblema (carta) | Mitra vescovile stilizzata (nessun ritratto: figura della tradizione) |
| Rimando | «Le tracce passano di mano in mano. Lungo il fianco della chiesa si commercia da secoli. Vai a destra, verso la Loggia.» → tappa 1-2, Loggia dei Merciai |
| Visioni di Borso | A1: `B11.6` Metadati, con San Giorgio · A2: `L1.5` Piramide DIKW, alla lapide |

## 2. Obiettivo di apprendimento

Alla fine lo studente sa:

1. riconoscere se una traccia è un **dato**, un'**informazione** o una **conoscenza**;
2. dare a un dato il contesto giusto (e scartare quelli falsi o inutili);
3. spiegare perché due informazioni collegate producono una conoscenza.

## 3. La zona percorribile (vista 3/4 in stile GBA)

Borso entra nella piazza con il pulsante «Entra nella piazza». La piazza è **quella vera**: sagome e altezze degli edifici vengono dagli open data del Comune di Ferrara. Il sistema è orientato in modo che la facciata della Cattedrale guardi verso chi gioca: in alto c'è la Cattedrale, a destra la Loggia dei Merciai, in basso il Palazzo Municipale. Come è costruita: `videogioco-5-duchi-motore-e-grafica.md`.

Le coordinate sono `(u, v)`, in metri dal centro della facciata: `u` verso destra, `v` verso il basso.

| Voce | Valore |
|---|---|
| Zona | Cella di Voronoi del punto della tappa, entro 150 m: la piazza davanti alla facciata (circa 40 × 33 m percorribili) e il tratto verso corso Martiri della Libertà. Non si sovrappone alle zone 2, 3 e 7 |
| Scala | 1 tessera = 1,25 m = 16 px; facciata larga 39,8 m (509 px) |
| Comandi | Computer: frecce o WASD, Maiusc per correre, spazio, Invio o E per parlare. Telefono: levetta e pulsante A |
| Partenza | (4, 15), al centro della piazza, rivolto verso la Cattedrale |
| Maurelio | (−3,4; 2,4), a sinistra del protiro |
| San Giorgio (visione A1) | (3,6; 2,6), a destra del protiro. Compare solo dopo la soglia, trasparente e color pietra |
| Lapide (visione A2) | (−13; 1,6), ai piedi della facciata, vicino alla porta sinistra. Si attiva solo dopo la A1 |
| Cartello dell'art. 9 | (−12,5; 17) |
| Arredo | 10 biciclette, 4 lampioni, 7 piccioni che volano via quando Borso si avvicina |
| Indicatori | Riquadro giallo sopra il personaggio da cercare; «A» sopra ciò con cui si può parlare (entro 2,3 m) |
| Confine | Tratteggio dorato. Oltre c'è la nebbia con i nomi delle tappe vicine (🔒) |
| Uscita | Dopo la soglia, freccia rossa sul confine destro, verso la Loggia dei Merciai (tappa 2). Attraversandola si torna alla mappa della città |

**Chicche (facoltative, mai valutate):**

- i **leoni** del protiro (in piedi davanti ai gradini, a 1,3 m dall'asse di un leone): «Due leoni di marmo rosso reggono le colonne del portale. Sono lì da quasi novecento anni.»;
- la **facciata** (ai piedi dei gradini, lontano dai leoni): «La facciata ha tre parti e tre punte. Sotto è romanica, sopra è gotica: due epoche in un solo muro. Anche un edificio è un messaggio, se sai leggerlo.»;
- il **cartello dell'art. 9**: «La Repubblica tutela il paesaggio e il patrimonio storico e artistico della Nazione.» (alla lettera) e «Questa piazza è una traccia: la legge la protegge.».

Altre chicche si aggiungeranno più avanti.

### 3.1 Il dialogo di Maurelio

Maurelio parla **solo di sé e della sua epoca**. Non parla di Borso.

1. «La tradizione dice che fui vescovo qui, più di mille anni fa.»
2. «Allora questa era terra di confine, tra acque e paludi.»
3. «Di me restano poche tracce: un nome, qualche data, dei racconti.»
4. «Una traccia, da sola, non parla. Vuoi imparare a farla parlare?» → [Sì, proviamo] apre la bottega · [Non ancora]

Dopo la soglia: carta di Maurelio, poi il rimando (§1).

## 4. La bottega: gradini e pool

Regole generali in `videogioco-5-duchi-esercizi.md` §1. Per ogni gradino: **4 esercizi giusti** su una **pool di 20** esercizi equivalenti, estratti a caso e generati con un seme diverso per ogni studente.

| Gradino | Nome | Meccanismi (a rotazione nella pool) | Passaggi |
|---|---|---|---|
| 0 | Esempio animato | 4 schermate: numero da solo → numero con contesto → due informazioni collegate → le tre parole con i loro colori | — |
| 1 | Riconosci | `smista` (tre cesti), `vf` (vero o falso lampo), `intruso` (griglia 2 × 2) | 1 |
| 2 | Trasforma | `vesti` (che cosa può essere questo valore?), `icona` (quale strumento dà senso al dato?), `costruisci` (metti in ordine i pezzi della frase) | 1 |
| 3 | Collega | `conclusione` (due informazioni → conclusione → perché), `scala` (dal più semplice al più ricco), `tripla` (tre etichette su tre carte) | 2–3 |

**Banche dati del generatore:**

- **9 fatti verificati**: Cattedrale 1135, Castello 1385, Università 1391, Borso duca 1471, Addizione Erculea 1492, Copernico laureato 1503, *Orlando furioso* 1516, Devoluzione 1598, UNESCO 1995;
- **10 valori** con tipo e frase in tre pezzi: 1135, 1492, 15:40, 08:05, 37,8 °C, 21 °C, 44121 (CAP), 9 km, 0532 (prefisso), 12;
- **12 affermazioni** vero/falso sulle tre parole.

Dentro una pool non ci sono due esercizi uguali (controllo di unicità in `buildPool`).

## 5. Punteggio, soglia e pausa

- **Gradini 1 e 2:** un esercizio conta se è giusto.
- **Gradino 3:** conta se l'esito è giusto (E = 1) **e** la coerenza dei passaggi è almeno 0,7.
- **Soglia della tappa:** 4 esercizi validi al gradino 3.
- **Pausa di autoregolazione.** Dopo due errori consecutivi compare un cerchio che si allarga e si stringe («Inspira mentre il cerchio cresce, espira mentre si stringe. Che cosa provi adesso?»). Il pulsante per ripartire si attiva dopo 4 secondi. Nei gradini 2 e 3, dopo la pausa si torna al gradino precedente. È l'aggancio all'anno 1 del quadro trasversale (emozioni e autoregolazione), fatto con un gesto e non con una lezione.
- **Da guardare nel report:** risposte al gradino 3 date in meno di 6 secondi (segnalate, senza penalità automatica).

## 6. Le visioni di Borso (facoltative, in tono seppia)

| Visione | Dove | Meccanismo | Contenuto |
|---|---|---|---|
| A1 · Metadati | San Giorgio, (16, 3) | `coppie`: collega campo e valore | Autore → Nicholaus, scultore · Anno → 1135 · Opera → Portale della Cattedrale · Soggetto → San Giorgio e il drago |
| A2 · Piramide DIKW | Lapide, (14, 10) | `piramide`: impila dal basso | Dato (arancio) → Informazione (blu) → Conoscenza (verde) → Saggezza (viola) |

Le visioni sono consecutive (A2 solo dopo A1), non servono per proseguire e restano disponibili anche dopo.

## 7. Misure contro copia e aiuti esterni

- Selezione, copia, taglia, menu contestuale e trascinamento disattivati.
- Filigrana con nome, numero dell'istanza e ora.
- Esercizi diversi per ogni studente e a ogni tentativo.
- Nessuna risposta scritta: solo scelte con tocco o clic.

## 8. Report

Il pulsante «Esporta il report» scarica un `.txt` con riepilogo, indicatori da guardare e codice di ripresa `5D1:<base64url del JSON>:c=<checksum>` (formato in `meccaniche.md` §1, versione ridotta).

## 9. Da completare

1. **Ripasso a distanza:** la carta entra nel sistema di Leitner; il primo ripasso è all'inizio della tappa 1-2.
2. **Dialoghi:** rivederli con Pietro per tono e registro.
3. **Grafica della zona:** alberi, passanti e suoni (vedi `motore-e-grafica.md` §6).
4. **Altre chicche** della piazza (da decidere con Pietro).
5. **Spazio vuoto** in alto nel riquadro degli esercizi su alcuni schermi (difetto grafico minore).

## 10. Registro modifiche

- **v0.3 (30/09/2026)**:
  - zona ricostruita con la geometria reale (open data del Comune);
  - vista 3/4 e movimento fluido;
  - facciata della Cattedrale riconoscibile, ritratti di Borso e Maurelio;
  - punto della tappa spostato davanti al portale;
  - uscita verso la Loggia.

- **v0.2 (30/09/2026)**:
  - Borso diventa il personaggio giocante;
  - zona percorribile in stile Pokémon;
  - nuovo dialogo di Maurelio, che parla solo di sé;
  - pool per gradino (4 su 20) con 9 meccanismi diversi ed esempio animato;
  - pausa di autoregolazione;
  - visioni A1 e A2 costruite;
  - chicche: leoni, art. 9, facciata.
- **v0.1 (28/09/2026)**: prima specifica e implementazione nel prototipo.
