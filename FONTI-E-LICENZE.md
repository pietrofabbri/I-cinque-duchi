# Fonti, attribuzioni e licenze

## Licenza del progetto

**Da decidere** (Pietro Fabbri). Finché non è indicata, tutti i diritti sui testi, sul codice e sulla grafica originale restano all'autore. Il repository è privato.

## Dati geografici

- **Comune di Ferrara, open data** (CC BY 4.0). Livelli usati:
  - numeri civici (shapefile `OPENDATA_CIVICI_preview`);
  - servizio WFS `https://sit.comune.fe.it/geoserverckan/Ferrara/wfs`, con i livelli `Edifici_preview`, `Fabbricati_USAGE_preview` (altezze da LIDAR), `Potenziale_solare_edifici_preview`, `Aree_pedonali_esistenti_preview` e `Perimetro_centro_storico_di_Ferrara_preview`.
- Attribuzione da mostrare nel gioco: «Dati: Comune di Ferrara, open data, CC BY 4.0».

### Fondo geografico degli anni 2, 3 e 4

- **Le tre scale non sono tre estensioni.** La fonte delle cime, `geography_regions_elevation_points`, è **mondiale in tutte e tre**: la scala che le precede nel nome è il dettaglio, non l'estensione. Il file chiamato `europa_50_altitudine` contiene due cime (Elbrus e Monte Bianco) e gli altri 84 punti della fonte vanno da longitudine −167 a +160. Perciò i tre file **non sono annidati** e non sono tre risoluzioni dello stesso elenco: sono selezioni diverse della stessa fonte globale a dettagli diversi (`mappe.md` §2.5). La licuzione non cambia — è sempre pubblico dominio — ma il nome del file sì, e il nome del file è ciò che il lettore legge per primo.

- **Natural Earth**, scale 110m, 50m e 10m: **pubblico dominio**, nessuna attribuzione richiesta e nessun vincolo. È la fonte dei 23 file in `dati/mappe/`: i 19 del 01/10/2026 (mondo, Europa e penisola: paesi, terre emerse, coste, unità amministrative, città, fiumi, laghi, regioni fisiche), `mondo_admin1.json` (unità amministrative di primo livello) e i tre `*_altitudine.json` (cime e quota): i 19 del 01/10/2026 (mondo, Europa e penisola: paesi, terre emerse, coste, unità amministrative, città, fiumi, laghi, regioni fisiche) più i 2 del 03/10/2026, `mondo_admin1.json` (50 unità amministrative di primo livello del mondo) e `mondo_admin1_copertura.json` (il conto della copertura). Scaricati ed estratti con `sorgenti/gis/scarica_ne.py` e `sorgenti/gis/mappe_formato.py`; le unità mondiali con `sorgenti/gis/mondo_admin1.py`, che usa `sorgenti/gis/shapefile_lettore.py` perché **`pyshp` non è installato su questa macchina e il progetto non installa pacchetti**. Formato e scelte della fonte in `docs/videogioco-5-duchi-mappe.md`.
- **OpenStreetMap** — **ODbL, e la decisione è presa il 02/10/2026: entra nel progetto** (`mappe.md` §10 Q1, risolta). Va detto perché sembrava una scelta molto piu' pesante di quanto sia: l'obbligo di condividere con la stessa licenza scatta solo quando si distribuisce un **database derivato** da OSM, e un gioco che disegna geometrie su schermo distribuisce un'opera, non un database. Quindi **il codice, i documenti e la grafica originale restano del progetto**. I file che invece sono database derivati viaggiano con ODbL e con la dichiarazione «© OpenStreetMap contributors» nei crediti del gioco.

**Sono tre, e sono stati scaricati il 03/10/2026:**

| File | Che cosa è | Licenza |
|---|---|---|
| `dati/edifici_footprint.json` | **5209 sagome di edifici su 54 luoghi**, con `forma`, `altezza_m` e `fonte_altezza` (`osm_height` / `osm_levels` / `assente`) | ODbL 1.0 |
| `dati/ferrara_fondo.json` | **14 tratti delle mura di Ferrara**, anello ricostruito a 60 m di tolleranza, 8601 m di perimetro e 4,20 km² di area interna | ODbL 1.0 |
| — | entrambi riportano nel campo `attribuzione` la dicitura `(c) OpenStreetMap contributors` | — |

Entrambi si rigenerano con `sorgenti/gis/edifici_footprint.py` e `sorgenti/gis/ferrara_fondo.py`. Il vincolo resta quello dichiarato il 02/10: ODbL è copyleft, e se il gioco riusa queste sagome **l'attribuzione va tenuta anche nei materiali derivati**. Il file delle sagome lo scrive da sé nel campo `nota_licenza`.

La misura del 01/10/2026 resta valida e va ricordata accanto ai file: **le sagome ci sono, le altezze no**. Dei 5209 edifici presi, 588 hanno l'altezza misurata, 1285 si ricavano dai piani, e **3336 non hanno niente** e diventano un volume neutro dichiarato (`mappe.md` §5).

### Rilievo del terreno

- **Terrarium tiles**, derivati da SRTM, da AWS Open Data: **nessuna registrazione**, una richiesta HTTP per tassello. Usati solo per la quota, la pendenza, l'esposizione e il rilievo locale di ogni città: `sorgenti/gis/rilievo.py`, che verifica i numeri su 14 punti ad altitudine nota e riporta un errore medio assoluto di 12,6 m. Formato e uso in `docs/videogioco-5-duchi-luoghi-edifici.md` §4.

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
| CC BY-SA 3.0 (di cui una in francese) | 17 | **attribuzione e licenza** |
| CC BY-SA 4.0 | 15 | **attribuzione e licenza** |
| CC BY-SA 2.0 / 2.0 (ted.) / 1.0 | 6 | **attribuzione e licenza** |
| CC BY 4.0 / 3.0 (it.) / 3.0 / 2.5 / 2.0 | 8 | **attribuzione** |
| CC0 | 4 | nessuno (dichiarazione di provenienza consigliata) |
| Attribution | 2 | **attribuzione** |
| No restrictions | 1 | nessuno |

Tutte e 169 sono licenze libere: **non c'è nessuna immagine senza licenza libera nel gioco**. Le **48** sotto CC BY o CC BY-SA richiedono di mostrare autore e licenza: la finestra dei crediti del gioco deve leggerle da `ritratti_disponibili.json`, campo `dettagli`, senza scriverle a mano. Il conto è per famiglia di licenza e viene dai dati: le stringhe del campo `licenza` portano anche la variante linguistica (`CC BY-SA 2.0 de`, `CC BY 3.0 it`, `CC BY-SA 3.0 fr`), e contarle per gruppo senza disaggregarle dava numeri che non tornavano.

Le riduzioni a 48×54 sono **opere derivate**: per CC BY-SA la condizione di ri-distribuzione con la stessa licenza riguarda il file, non l'opera derivata, ma per prudenza le riduzioni viaggiano con la stessa licenza della fonte, dichiarata in `dettagli.licenza`. Nessun ritratto è stato alterato nel contenuto: solo ritagliato e ridotto.

Sono state **respinte** otto immagini perché non ritraevano la persona (tra cui un gatto per Renata Viganò, una ceramica iraniana per i mercanti di Ferrara e una parata di soldati di oggi per i Bersaglieri del 1848). Non sono nel gioco, e il motivo è registrato. Le giudicazioni sono **45** in tutto — 19 accettate e 26 respinte — e tutte e 45 portano il motivo.

## Testi letterari citati

- **Ludovico Ariosto, *Orlando furioso*** — le **30 citazioni** del quinto anno (`videogioco-5-duchi-furioso.md`). Fonte: **edizione 1928**, Biblioteca BEIC, tre volumi, trascrizione di **Wikisource in italiano** (`Orlando furioso (1928)/Canto N` e le pagine `Pagina:<volume>/<n>` del digitalizzato).
  - **Licenza: pubblico dominio.** Non ha nessun obbligo di attribuzione; il gioco la dichiara egualmente perché un ragazzo che cerca la citazione deve poterla ritrovare.
  - I **versi sono copiati dal testo a ogni esecuzione**, non a mano: `sorgenti/furioso/costruisci_citazioni.py` li prende dall'indice delle ottave e `verifica_citazioni.py` li riverifica.
  - L'edizione del 1928 **modernizza la grafia** (sciolto, né, v'è) e conserva la *rima extranea* (sette versi invece di otto). Le **parafrasi, i temi, i moti e le emozioni sono di questo progetto**, non del testo: non sono una traduzione e non possono essere citate come versi dell'Ariosto.
  - **Non è la princeps del 1516.** Il riscontro con l'edizione di Project Gutenberg (che contiene i soli canti 1-16) ha trovato tre differenze sulle 23 citazioni confrontabili: un verso in più nel canto 5 ottava 23, l'apostrofo eliso in 1,9 e una variante di accordo in 5,18. Nessuna cambia l'insegnamento della tappa.

## Testi normativi citati

- Indicazioni nazionali per i licei, DPR 89/2010.
- Costituzione della Repubblica italiana (articoli citati alla lettera nel gioco).
- GDPR (Reg. UE 2016/679) e AI Act (Reg. UE 2024/1689), per le scelte su privacy e sorveglianza.
