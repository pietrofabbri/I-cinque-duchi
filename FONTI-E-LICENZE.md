# Fonti, attribuzioni e licenze

## Licenza del progetto

**Da decidere** (Pietro Fabbri). Finché non è indicata, tutti i diritti sui testi, sul codice e sulla grafica originale restano all'autore. Il repository è privato.

## Dati geografici

- **Comune di Ferrara, open data** (CC BY 4.0). Livelli usati:
  - numeri civici (shapefile `OPENDATA_CIVICI_preview`);
  - servizio WFS `https://sit.comune.fe.it/geoserverckan/Ferrara/wfs`, con i livelli `Edifici_preview`, `Fabbricati_USAGE_preview` (altezze da LIDAR), `Potenziale_solare_edifici_preview`, `Aree_pedonali_esistenti_preview` e `Perimetro_centro_storico_di_Ferrara_preview`.
- Attribuzione da mostrare nel gioco: «Dati: Comune di Ferrara, open data, CC BY 4.0».

### Fondo geografico degli anni 2, 3 e 4

- **Natural Earth**, scale 110m, 50m e 10m: **pubblico dominio**, nessuna attribuzione richiesta e nessun vincolo. È la fonte dei 19 file in `dati/mappe/` (mondo, Europa e penisola: paesi, terre emerse, coste, unità amministrative, città, fiumi, laghi, regioni fisiche). Scaricati ed estratti il 01/10/2026 con `sorgenti/gis/scarica_ne.py` e `sorgenti/gis/mappe_formato.py`. Formato e scelte della fonte in `docs/videogioco-5-duchi-mappe.md`.
- **OpenStreetMap** — **non ancora usato nei dati del gioco**. È la fonte prevista per le sagome degli edifici fuori Ferrara, ed è **ODbL**: obbliga ad attribuire «© OpenStreetMap contributors» e a distribuire con la stessa licenza i database derivati. **La decisione di accettare o no questa licenza spetta a Pietro e non è ancora presa** (`mappe.md` §10 Q1). Le interrogazioni del 01/10/2026 via Overpass API sono state fatte solo per misurare quanto i dati siano disponibili, e nulla è stato scaricato nel repository.

## Immagini usate come riferimento o come base

Wikimedia Commons, file consultati il 30/09/2026.

| Uso | Opera o file | Licenza o stato |
|---|---|---|
| Ritratto di Borso nei dialoghi, ridotto a 48×54 px e 16 colori | «Borso d'Este.jpg»: ritratto di profilo attribuito a Vicino da Ferrara o Baldassarre d'Este, 1469-71 | Dipinto in pubblico dominio |
| Riferimento di forme e colori per la figura di Borso | Stesso ritratto; medaglie di Amadio da Milano e di Petrecino da Firenze | Pubblico dominio (opere); foto CC BY-SA 3.0 |
| Riferimento di colori per Maurelio | Cosmè Tura, *Giudizio di san Maurelio* (1480), Pinacoteca Nazionale di Ferrara | Pubblico dominio (opera) |
| Riferimento per la facciata della Cattedrale | Xilografie ottocentesche della facciata; «Ferrara, duomo, facciata.JPG» e «…portale.JPG» (sailko) | Pubblico dominio; CC BY 2.5 |
| Riferimento per San Giorgio | Lunetta di Nicholaus (1135), foto «Ferrara, duomo, nicholaus, lunetta 04.JPG» (sailko) | CC BY 2.5 (foto) |

**Solo il ritratto di Borso** deriva direttamente dai pixel di un'immagine. Tutti gli altri elementi grafici (sprite, facciata, ritratto di Maurelio, arredo) sono disegnati da zero con codice, in `sorgenti/art/`.

**Nota.** In Italia la riproduzione di beni culturali è libera per scopi didattici non commerciali (Codice dei beni culturali, art. 108). Per un uso commerciale serve una verifica.

### I ritratti dei 169 personaggi (01/10/2026)

Fonti: **Wikimedia Commons**, file scaricati l'01/10/2026 con `sorgenti/art/ritratto_reale.py`. L'elenco completo, con per ogni scheda il codice, il nome del file su Commons, l'autore, la licenza e la risoluzione, è `sorgenti/art/ritratti_disponibili.json`. Il giudizio su ogni immagine è `sorgenti/art/attestazione_immagini.json`; il perché di tutto è in `docs/videogioco-5-duchi-ritratti.md`.

| Licenza | Ritratti | Obbligo |
|---|---|---|
| Pubblico dominio | 116 | nessuno |
| CC BY-SA 3.0 | 17 | **attribuzione e licenza** |
| CC BY-SA 4.0 | 15 | **attribuzione e licenza** |
| CC BY-SA 2.0 / 2.5 | 5 | **attribuzione e licenza** |
| CC BY-SA 1.0 / 3.0 | 1 | **attribuzione e licenza** |
| CC0 | 4 | nessuno (dichiarazione di provenienza consigliata) |
| CC BY 2.0 / 2.5 / 3.0 / 4.0 | 11 | **attribuzione** |

Tutte e 169 sono licenze libere: **non c'è nessuna immagine senza licenza libera nel gioco**. Le 53 sotto CC BY o CC BY-SA richiedono di mostrare autore e licenza: la finestra dei crediti del gioco deve leggerle da `ritratti_disponibili.json`, campo `dettagli`, senza scriverle a mano.

Le riduzioni a 48×54 sono **opere derivate**: per CC BY-SA la condizione di ri-distribuzione con la stessa licenza riguarda il file, non l'opera derivata, ma per prudenza le riduzioni viaggiano con la stessa licenza della fonte, dichiarata in `dettagli.licenza`. Nessun ritratto è stato alterato nel contenuto: solo ritagliato e ridotto.

Sono state **respinte** sette immagini perché non ritraevano la persona (tra cui un gatto per Renata Viganò, una ceramica iraniana per i mercanti di Ferrara e una parata di soldati di oggi per i Bersaglieri del 1848). Non sono nel gioco, e il motivo è registrato.

## Testi normativi citati

- Indicazioni nazionali per i licei, DPR 89/2010.
- Costituzione della Repubblica italiana (articoli citati alla lettera nel gioco).
- GDPR (Reg. UE 2016/679) e AI Act (Reg. UE 2024/1689), per le scelte su privacy e sorveglianza.
