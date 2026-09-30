---
titolo: Videogioco "I cinque duchi" — Motore, dati geografici e grafica (zone percorribili e mappa della città)
versione: 0.1
data: 2026-09-30
autore: Pietro Fabbri (con Claude)
fonte: richieste di Pietro del 30/09/2026 («mappa non realistica, troppo piccola, cattedrale e personaggi non riconoscibili, nebbia non chiara, più fluido»)
implementazione: videogioco-5-duchi-anno1-prototipo-mappa.html (sorgenti zona1.js, zona1_dati.js, esercizi1.js, mappa_proto_template.html)
documenti collegati: videogioco-5-duchi-tappa-1-01.md, videogioco-5-duchi-anno1-mappa.md, videogioco-5-duchi-gioco.md
---

# Motore, dati geografici e grafica

Questo documento spiega **come è costruito** il prototipo. Serve a chi deve rifare o estendere le zone delle altre 29 tappe, anche senza il contesto delle conversazioni.

## 0. Decisioni del 30/09/2026

| Tema | Decisione |
|---|---|
| Vista | Dall'alto in 3/4, stile Game Boy Advance: si vedono i tetti e le facciate rivolte verso chi gioca |
| Motore | **Canvas scritto a mano**, nessuna libreria esterna. Phaser 3 era la scelta di Pietro, ma il registro npm e i CDN non sono raggiungibili dall'ambiente di lavoro. Il motore canvas dà lo stesso risultato (movimento continuo a 60 fps, telecamera morbida) ed è più leggero di circa 1 MB. Il passaggio a Phaser resta possibile |
| Geometria | **Reale**: sagome e altezze degli edifici dagli open data del Comune di Ferrara |
| Scala | 1 tessera = 1,25 m = 16 px; altezze in 3/4 = 10 px per metro |
| Personaggi | Sprite 16 × 24 px (4 direzioni × 3 passi); ritratti 48 × 54 px nei dialoghi |

## 1. Fonti dei dati (open data, CC BY 4.0)

Server WFS del Comune di Ferrara: `https://sit.comune.fe.it/geoserverckan/Ferrara/wfs` (544 livelli). Livelli usati:

| Livello WFS | Contenuto | Uso nel gioco |
|---|---|---|
| `Ferrara:Edifici_preview` | Sagome degli edifici (EPSG:3003) | Pianta della zona percorribile e della mappa della città |
| `Ferrara:Fabbricati_USAGE_preview` | Fabbricati catastali con altezza `H` calcolata da LIDAR (DSM − DTM) | Altezza dei muri in 3/4 |
| `Ferrara:Potenziale_solare_edifici_preview` | Falde dei tetti con orientamento (`ORIENTGRAD`) e pendenza (`PENDGRADI`) | Luci e ombre dei tetti |
| `Ferrara:Aree_pedonali_esistenti_preview` | Piazze e vie pedonali | Pavimentazione in lastre |
| `Ferrara:Perimetro_centro_storico_di_Ferrara_preview` | Perimetro ufficiale del centro storico, lungo le mura | Mura sulla mappa della città (sostituisce la stima a mano della v0.6) |

Livelli utili per dopo: `Alberi_preview`, `Verde_pubblico_POC_vigenti_preview`, `Fiumi_e_canali_principali_preview`, `Sito_Unesco_preview`, `Beni_culturali_preview`, `Nuvola_di_punti_rilievo_LIDAR_preview`.

**Come sono stati letti.** Il server non è raggiungibile dall'ambiente cloud. I dati sono stati letti con il **browser integrato dell'app di Claude** (sito autorizzato da Pietro), con una richiesta `GetFeature` in `outputFormat=application/json` e `srsName=EPSG:4326`. Il riquadro va dato come `lon_min,lat_min,lon_max,lat_max,EPSG:4326`. I dati sono stati convertiti nel browser in coordinate locali e passati a pezzi da 200 000 caratteri. Script: `gis/estrai.py`.

**Coordinate locali (metri):** `x = (lon − 11,62) · 111320 · cos(44,8375°)`, `y = (lat − 44,8375) · 110540`. È lo stesso sistema di tutti gli altri file del progetto.

**File prodotti:**
- `gis/edifici_centro_local.json`: 4142 edifici attorno al centro;
- `gis/zona1_dati.json`: fabbricati con altezza, falde, aree pedonali;
- `gis/citta_centro.json`: perimetro ufficiale e 11 185 edifici del centro storico, semplificati a 0,8 m, in mezzi metri con codifica delta.

## 2. Sistema della zona percorribile

Ogni zona ha un sistema proprio, orientato in modo che **il monumento principale guardi verso chi gioca**. Nella vista 3/4 si vedono solo le facciate rivolte verso il basso dello schermo.

Per la tappa 1-1:
- **origine F**: centro della facciata della Cattedrale, cioè il punto medio tra i vertici 0 e 2 del poligono 129472 (la facciata è lunga 39,8 m);
- **asse "giù"**: normale uscente della facciata, verso ONO;
- **asse "destra"**: SSO. Così la Loggia dei Merciai (fianco sud) sta a destra;
- **coordinate di mappa**: `u` = metri verso destra, `v` = metri verso il basso;
- **punto della tappa**: `(0, 10)`, 10 m davanti al portale (44,835832 N, 11,61958 E). Sostituisce il civico 9, che era davanti all'Arcivescovado.

**Zona.** È la cella di Voronoi del punto della tappa rispetto a tutte le altre tappe, entro 150 m. Per la tappa 1 è un quadrilatero di circa 145 × 35–110 m: la piazza davanti alla facciata e il tratto verso corso Martiri della Libertà.

**Script:**
- `gis/zona1_build.py`: calcola rotazione, zona, edifici con altezza e falde, e scrive `gis/zona1_mappa.json`;
- `gis/zona1_pack.py`: assegna le falde agli edifici e impacchetta dati e immagini in `zona1_dati.js`, con gli oggetti `Z1DATA` e `Z1ART`.

**Per una nuova tappa** basta:
1. scegliere il monumento e il suo lato "facciata";
2. riusare i due script cambiando l'identificativo del poligono e il rettangolo di mappa;
3. disegnare solo le facciate speciali (come quella della Cattedrale).

Tutto il resto (edifici, finestre, tetti, collisioni, nebbia) viene generato in automatico.

## 3. Come disegna il motore (`zona1.js`)

**Preparazione (una volta sola, poi in cache in `window.__Z1`):**
1. **Suolo** in un'unica immagine:
   - ciottoli per le vie;
   - lastre di pietra per le aree pedonali, con la griglia chiara di fasce ogni 6 m;
   - ombre portate degli edifici, con la luce da sinistra in alto.
2. **Edifici**: un'immagine per edificio.
   - **Muri.** Sono i lati la cui normale, verso l'esterno del volume, guarda verso il basso. Vale anche per i cortili interni.
   - **Aspetto dei muri.** L'altezza viene dal LIDAR. Il colore è preso da una tavolozza di intonaci e mattoni ferraresi. Le finestre vanno ogni 3,1 m, i piani ogni 3,4 m; al piano terra ci sono porte. C'è un cornicione.
   - **Tetto.** È la sagoma spostata in alto dell'altezza. Ogni falda ha una luce diversa secondo il suo orientamento. Sopra ci sono le file dei coppi.
   - **Cattedrale.** Muri senza finestre, più l'immagine della facciata (509 × 312 px) appoggiata sulla linea `v = 0`. Le cuspidi superano il tetto, come nella realtà.
   - **Edifici fuori dalla zona.** Vengono schiariti, così fanno parte della nebbia.
3. **Maschera percorribile.** Quattro celle per metro: dentro la zona e fuori dagli edifici. I gradini della facciata non sono percorribili.
4. **Nebbia.** Maschera statica con bordo morbido (10 tratti sfumati) e una trama di nuvole generata con rumore morbido che si ripete.

**Ogni fotogramma:**
1. **Telecamera.** Segue Borso con un ritardo morbido (fattore 0,12). Borso resta al 64% dell'altezza dello schermo, al 74% sui telefoni in verticale, così si vedono gli edifici davanti.
2. **Disegno.** L'ordine è: suolo → nebbia con nuvole in movimento → confine tratteggiato dorato → edifici in ordine di profondità → personaggi, oggetti, biciclette e piccioni dall'alto in basso.
3. **Occlusione.** Se Borso è dietro un edificio, la parte di edificio che lo copre viene ridisegnata semitrasparente, così Borso resta visibile.
4. **Scala dei pixel.** Sullo schermo del computer è intera (2×, 3× o 4×). Sui telefoni è frazionaria, tra 1,25 e 2, così si vedono circa 25–30 m di piazza.

**Movimento.** È continuo, non a caselle.
- Velocità: 4,6 m/s, 7,5 m/s tenendo premuto Maiusc.
- Accelerazione morbida.
- Collisione separata sui due assi (si scivola lungo i muri).
- Animazione del passo legata alla distanza percorsa.

**Comandi.**
- Computer: frecce o WASD, spazio, Invio o E per parlare.
- Telefono: levetta virtuale e pulsante A, nascosti durante i dialoghi.

**Dialoghi.**
- Riquadro in stile GBA con ritratto, nome e testo che compare lettera per lettera. Un tocco completa la frase.
- Pausa di 250 ms dopo la chiusura, per non riaprire subito lo stesso dialogo.
- Il segno «A» compare sopra ciò con cui si può parlare, entro 2,3 m.

**Uscita.** Dopo la soglia, compare una freccia rossa sul confine destro, verso la Loggia dei Merciai. Il passaggio si apre per `u > 27`, `v` tra −2 e 14.

## 4. Mappa della città (`mappa_proto_template.html`)

- **Edifici veri** del centro storico: 11 185, semplificati. Il perimetro ufficiale è disegnato come terrapieno verde e cortina di mattoni.
- **Nebbia chiara.** Gli edifici delle zone chiuse sono grigio-beige. Sopra c'è un velo bianco con nuvole che scorrono. Le zone aperte sono ritagliate con bordo morbido e segnate da un tratteggio dorato in movimento.
- **Prossima tappa.** Dopo la soglia compare un «?» che pulsa, senza nome.
- **Fluidità.**
  - La città è disegnata una volta in un'immagine in cache e ridisegnata solo quando cambia lo zoom o lo stato.
  - Trascinamento con inerzia, zoom morbido con la rotella, pizzico a due dita.
  - Volo animato verso la tappa successiva.
- **Costo.** Circa 15 ms per fotogramma su un computer del 2024. Il file HTML pesa circa 770 kB.

## 5. Grafica e riconoscibilità

| Elemento | Come è fatto | Riferimento visivo (usato solo per forme e colori) |
|---|---|---|
| Facciata della Cattedrale | Disegno a codice (`art/facciata.py`, fattore 1,446): tre cuspidi con rosoni, pinnacoli su quattro pilastri, due ordini di logge, parte bassa romanica bianca e rosa, protiro con leoni in marmo rosso, lunetta di San Giorgio, loggia della Madonna, timpano del Giudizio, gradini | Xilografie ottocentesche della facciata (Wikimedia Commons, pubblico dominio); foto "Ferrara, duomo, facciata.JPG" (sailko, CC BY 2.5) |
| Borso, figura | Berretta rossa alta, capelli grigio-castani a caschetto, veste rossa con broccato d'oro e collare di perle | Ritratto di profilo (Vicino da Ferrara / Baldassarre d'Este, 1469-71) |
| Borso, ritratto nei dialoghi | Il dipinto ridotto a 48 × 54 px e 16 colori (media k-means) | "Borso d'Este.jpg", Wikimedia Commons: dipinto in pubblico dominio |
| Maurelio | Vescovo con mitra, piviale azzurro, tunica rosa, barba grigia, pastorale; il ritratto è disegnato a mano | Colori dei tondi di Cosmè Tura (1480, Pinacoteca di Ferrara) |
| San Giorgio (visione) | Cavaliere di pietra a cavallo, in tono seppia | Lunetta di Nicholaus (1135) |
| Arredo | Biciclette (Ferrara, città delle biciclette), lampioni, piccioni che volano via quando Borso si avvicina | — |

**Nota sulle immagini.** Le opere sono in pubblico dominio. In Italia la riproduzione di beni culturali è libera per scopi didattici e non commerciali (Codice dei beni culturali, art. 108). Per un uso commerciale va verificata l'autorizzazione.

**Sprite pronti per dopo:** statue di Borso seduto e di Niccolò III a cavallo (Volto del Cavallo, tappa 1-7).

## 6. Limiti noti e prossimi passi

1. **Altezze stimate.** Gli edifici senza fabbricato catastale corrispondente hanno altezza 11 m: sono 25 su 123 nella zona 1.
2. **Profondità approssimata.** L'ordine di disegno usa il punto più basso dell'edificio. Per edifici molto irregolari, come l'Arcivescovado, può sbagliare in punti ai margini della zona.
3. **Facciate generiche.** Vanno disegnate a mano solo quelle dei monumenti. Le altre sono generate.
4. **Dettagli da aggiungere.** Alberi (livello `Alberi_preview`), passanti, suoni, ciclo giorno e notte.
5. **Mappa della città.** Aggiungere il verde pubblico e l'acqua.

## 7. Registro modifiche

- **v0.1 (30/09/2026)**: prima versione. Motore canvas in 3/4, geometria reale dal WFS del Comune, grafica dei personaggi, nebbia e fluidità della mappa della città.
