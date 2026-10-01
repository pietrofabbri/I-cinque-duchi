# Istruzioni per chi lavora al progetto (persone e IA)

Questo file serve a chiunque riprenda il lavoro senza il contesto delle conversazioni in cui è nato, per esempio un'altra IA o un altro progetto di Claude. Va letto prima di modificare qualsiasi cosa.

## 1. Che cos'è

«I cinque duchi» è un videogioco didattico per insegnare informatica in un liceo scientifico, opzione scienze applicate: 5 anni, 30 livelli per anno. Il committente e autore è **Pietro Fabbri**, docente di informatica (classe di concorso A041) a Ferrara. Parti dal `README.md` per il quadro generale e l'elenco dei documenti.

## 2. Fonte di verità e ordine di lettura

1. `docs/` è la **fonte di verità**. `dati/` contiene gli stessi contenuti in forma leggibile dai programmi. `prototipo/` si genera da `sorgenti/`.
2. Ordine di lettura: `README.md` → `docs/videogioco-5-duchi-gioco.md` → `docs/videogioco-5-duchi-esercizi.md` → il documento del tema su cui lavori. Per gli anni 2 e 3, leggi prima la sezione §0 e le questioni aperte del documento dell'anno: contengono decisioni prese e limiti che non si possono dare per scontati.
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
- **Personaggi**: `P01…P94` (anno 1). Gli anni 2 e 3 usano la serie `Q`, che continua da `Q01` (anno 2) a `Q101` (anno 3). **Codici definitivi fino a nuova indicazione.**
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

## 6. Come lavorare

1. Leggi i documenti pertinenti e verifica che la modifica rispetti il §3.
2. Modifica il documento in `docs/`, poi i dati in `dati/` se servono, poi il codice in `sorgenti/`.
3. Rigenera il prototipo con `python3 build_mappa_html.py` da `sorgenti/`. Se hai Playwright, esegui i test in `sorgenti/test/`.
4. Aggiorna versione e registro modifiche dei documenti toccati e, se serve, la tabella del `README.md`.
5. Nel messaggio di commit, spiega **che cosa** è cambiato e **perché**.

## 7. Da sapere

- `sorgenti/gis/estrai.py` legge i dati che una sessione di Claude aveva ricevuto dal browser integrato. Il percorso è specifico di quella sessione. Per rifare l'estrazione, interroga direttamente il WFS del Comune come descritto in `motore-e-grafica.md` §1.
- `sorgenti/civici.py` e `geo.py` richiedono lo shapefile dei numeri civici del Comune di Ferrara, che non è nel repository perché pesa circa 50 MB. Senza, il build usa `sorgenti/gis/vie_etichette.json`.
