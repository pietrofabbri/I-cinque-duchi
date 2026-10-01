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
| 3 | `videogioco-5-duchi-gioco.md` | Come si gioca: ciclo di una tappa, strumenti veri, carte, memoria, Borso giocante, zone percorribili | 0.4 |
| 4 | `videogioco-5-duchi-esercizi.md` | Pool di esercizi per gradino, catalogo dei meccanismi, quantità di testo per anno, linguaggio, colori | 0.1 |
| 5 | `videogioco-5-duchi-meccaniche.md` | Salvataggio e consegna (file unico), punteggio di processo, misure contro copia, IA e screenshot | 0.3 |
| 6 | `videogioco-5-duchi-quadro-trasversale.md` | Diritto, Etica, Filosofia, Psicologia, Arti sui cinque anni; agganci per le 30 tappe dell'anno 1 | 0.1 |
| 7 | `videogioco-5-duchi-anno1-ferrara.md` | Anno 1: le otto Ferrara, classificazioni, catalogo di 93 personaggi e 32 luoghi | 0.3 |
| 8 | `videogioco-5-duchi-anno1-mappa.md` | Anno 1: il percorso unico delle 30 tappe, posizioni, zone, mappa della città | 0.8 |
| 9 | `videogioco-5-duchi-tappa-1-01.md` | Tappa 1-1 (San Maurelio, Cattedrale): la prima tappa completa, modello per le altre | 0.3 |
| 10 | `videogioco-5-duchi-motore-e-grafica.md` | Motore, fonti GIS, sistema di coordinate, rendering 3/4, nebbia, grafica dei personaggi | 0.1 |

I nomi dei file conservano il prefisso storico `videogioco-5-duchi-`, perché i documenti si citano a vicenda con questi nomi. Il titolo del gioco è **«I cinque duchi»**.

### Dati (`dati/`)

| File | Contenuto |
|---|---|
| `videogioco-5-duchi-livelli.json` | I 150 livelli (stesso contenuto di `schema-livelli.md`) |
| `videogioco-5-duchi-anno1-personaggi.json` | 93 personaggi, 32 luoghi, epoche e legende dell'anno 1 |
| `videogioco-5-duchi-anno1-mappa.json` | Le 30 tappe: luogo, personaggio, coordinate, aggancio, rimando, visioni |
| `videogioco-5-duchi-anno1-tappe.geojson` | Tappe e percorso in GeoJSON |
| `videogioco-5-duchi-anno1-mura-stima.geojson` | Perimetro delle mura stimato a mano (superato: ora si usa il perimetro ufficiale, vedi `sorgenti/gis/citta_centro.json`) |
| `videogioco-5-duchi-anno1-zona1.json` | Zona percorribile della tappa 1: edifici con altezze, falde, aree pedonali |

## Rigenerare il prototipo

Servono **Python 3** e **Pillow** (per la grafica). Da `sorgenti/`:

```bash
python3 art/sprites.py && python3 art/facciata.py 1.446 && python3 art/ritratti.py   # da sorgenti/art/
python3 gis/zona1_build.py && python3 gis/zona1_pack.py                             # da sorgenti/
python3 build_mappa_html.py                                                          # scrive ../prototipo/index.html
```

I test automatici (`sorgenti/test/*.js`) usano Playwright e giocano la tappa 1 dall'inizio alla fine.

## Stato del progetto

**Fatto**
- curricolo e schema dei 150 livelli;
- anno 1: narrazione, personaggi, percorso delle 30 tappe con coordinate;
- tappa 1 giocabile.

**Da fare, in ordine**
1. Migliorare la parte didattica della tappa 1.
2. Tappe 1-2 … 1-30.
3. Coordinate delle tappe 27 e 30.
4. Materiali degli anni 2–5, in arrivo da Pietro.
5. Ricerca dei ritratti.
6. Strumento del docente.
7. Modalità accessibile.

**Decisioni in sospeso:** vedi le sezioni «Questioni aperte» di ciascun documento. In particolare: la tappa 1-30 affidata a «La città» (P93), gli agganci trasversali da confermare, il formato del file di consegna.
