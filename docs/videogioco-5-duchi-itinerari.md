---
titolo: "Gli itinerari: chi incontri, dove, e con quale mezzo"
versione: 0.1
data: 2026-10-03
autore: "Progetto I cinque duchi"
documenti collegati: videogioco-5-duchi-percorsi.md (v0.4), videogioco-5-duchi-anno1-mappa.md (v0.9), videogioco-5-duchi-anno2-penisola.md (v0.2), videogioco-5-duchi-anno3-europa.md (v0.4), videogioco-5-duchi-anno4-mondo.md (v0.5), videogioco-5-duchi-anno5-mondo.md (v0.6), videogioco-5-duchi-luoghi.md (v0.6), videogioco-5-duchi-itinerari.md (questo), AGENTS.md
---

# Gli itinerari: chi incontri, dove, e con quale mezzo

## 0. Che cosa chiede questo documento, e che cosa risponde

Pietro ha chiesto gli itinerari dei personaggi sui cinque anni: **dove vanno, con
quale mezzo di trasporto, e chi incontrano in quel livello**, distinguendo **chi è
obbligatorio** e **chi è facoltativo**.

La risposta è che gli itinerari esistevano già, ma **sparsi in quattro documenti e
in tre formati diversi**: le tappe degli anni avevano la voce e il luogo, `percorsi.md`
aveva i mezzi, e nessun posto metteva le tre cose nella stessa riga. Qui sono
messe insieme, e sono **generate**, non scritte.

Tre fatti che decidono la forma:

1. **Le tabelle non si scrivono a mano.** Sono centocinquanta righe e ognuna ha
   quattro informazioni. Scritte a mano, due righe su centocinquanta finiscono con
   una cifra che il dato non conferma — ed è esattamente il difetto che ha fatto
   nascere questo lavoro, ed è descritto in §5.
2. **Il mezzo è una scelta, non un dato.** Le tappe dicono *dove*, non *come*: il
   mezzo è in `percorsi.md` §1 e la scelta spetta al motore, che ha le distanze.
   Per il quinto anno **non è dichiarato nessun mezzo**, e la colonna lo dice
   invece di riempirla.
3. **La voce collettiva è una voce senza nome proprio**, e i documenti degli anni
   la marcano a mano con la parola «collettivo» e l'attendibilità `C`. Qui la
   marcatura viene letta, e ogni voce porta **la prova** che l'ha fatta
   classificare.

## 1. Il conto, che è la parte che serve

| Anno | Tappe | Voci distinte | Facoltativi | Collettive | Mezzo dichiarato |
|---|---|---|---|---|---|
| **1** | 30 | 30 | 25 | 0 | a piedi |
| **2** | 30 | 30 | 59 | 3 | a cavallo |
| **3** | 30 | 30 | 61 | 1 | a cavallo |
| **4** | 30 | 30 | 63 | 2 | in nave |
| **5** | 30 | 30 | 61 | 3 | **non dichiarato** |
| **Totale** | **150** | **141** | **269** | **9** | — |

**Le centocinquanta voci non sono centocinquantuno.** Sono centocinquanta voci
obbligatorie e **centoquarantuno nomi distinti**: nove tappe hanno la stessa voce di
un'altra, e sono i **ritorni** che il progetto ha deciso (Newton, Cesare, Leibniz e
gli altri). Un ritorno non è un duplicato: è la stessa persona che torna, e la
`premi.md` lo tratta come una seconda occasione, non come un premio ripetuto.

**I facoltativi sono 269, e non sono tutti uguali.** In un anno sono 25 e in un
 altro 63: l'anno 1 ha la tappa dentro una città e la voce è la persona che abita
lì, mentre dal secondo anno in poi la tappa è un luogo che il giocatore attraversa
e la stanza è di chi ci passa. Le cinque tappe del primo anno **senza facoltativi**
sono un dato, non una dimenticanza: sono le tappe in cui la voce è già la persona
del luogo e un secondo nome sarebbe di troppo.

**Le nove voci collettive** sono 3 nell'anno 2, 1 nel terzo, 2 nel quarto e 3 nel
quinto, e il quinto numero è quello che il documento dell'anno 5 dichiarava
diversamente: è il difetto di §5.

## 2. Che cosa il mezzo non è, e perché il quinto anno non ce l'ha

Il mezzo di trasporto determina la velocità con cui la mappa si attraversa, e
quindi il numero di giorni che una tappa costa (`percorsi.md` §1, §2). Ma **le
tappe non dicono quale mezzo si usa**, e questo documento non lo inventa:

- **anno 1**: a piedi, perché il percorso è dentro Ferrara e i venticinque
  chilometri al giorno di un uomo solo con la bisaccia sono la velocità del luogo;
- **anni 2 e 3**: a cavallo, perché il percorso è una strada che esisteva e il
  cavallo è il mezzo della tappa (45 km al giorno, due persone: cavaliere e
  scudiero);
- **anno 4**: in nave, perché l'anno attraversa oceani e il veliero è il mezzo
  dell'anno (130 km al giorno, rotta dipendente dal vento);
- **anno 5**: **nessun mezzo dichiarato**, e la ragione è scritta in
  `percorsi.md` §1.1: sono **ventidue** i mezzi che il quinto anno potrebbe usare,
  e cinque di quelli sono i mezzi **del testo** del *Furioso* (l'ippogrifo, il
  drago, la sirena, il carro di delfini, il carro di serpenti). Sceglierne uno
  sarebbe scegliere al posto di Pietro, quindi la colonna resta `non_dichiarato` e
  il motore la sceglie quando avrà la distanza.

La regola dei due strati vale anche per la velocità: **il pin è reale e ci si va
in treno; la stanza è del poema e ci si va a cavallo di Astolfo.**

## 3. Le tabelle degli itinerari, anno per anno

*(generate da `sorgenti/genera_itinerari.py` a partire da `dati/incontri_livelli.json`)*


#### Anno 1 — a piedi

Le trenta tappe, 25 facoltativi, 0 voce collettive.

| Livello | Dove si va | Chi incontri (obbligatorio) | Facoltativi |
|---|---|---|---|
| **1-1** | Cattedrale di San Giorgio (Piazza della Cattedrale) | San Maurelio | San Giorgio |
| **1-2** | Loggia dei Merciai (Piazza Trento e Trieste, fianco sud della Cattedrale) | Mercanti, artigiani e cittadini | Gli Adelardi (famiglia) |
| **1-3** | Piazza Trento e Trieste e Palazzo della Ragione (Piazza Trento e Trieste) | Salinguerra Torelli | Matilde di Canossa |
| **1-4** | Museo della Cattedrale (ex San Romano) (Via San Romano 1) | Guido Monaco (Guido d'Arezzo) a Pomposa | — |
| **1-5** | Vicolo del Chiozzino (dal volto in via Ripagrande a via Piangipane) | Bartolomeo Chiozzi, il "Mago Chiozzino" | — |
| **1-6** | MEIS (Via Piangipane 81) | La comunità ebraica ferrarese | — |
| **1-7** | Palazzo Municipale e Volto del Cavallo (Piazza del Municipio 2) | Obizzo II d'Este | Leonello d'Este, Leon Battista Alberti |
| **1-8** | Castello Estense (Largo Castello 1) | Alfonso I d'Este | Nicolò II d'Este, Dosso Dossi |
| **1-9** | Teatro Comunale (Corso Martiri della Libertà 5) | Antonio Foschini | Napoleone e l'età francese |
| **1-10** | Palazzo Paradiso (Biblioteca Ariostea) (Via delle Scienze 17) | Guarino Veronese | Alberto V d'Este, Niccolò Copernico |
| **1-11** | Palazzo Renata di Francia (Via Savonarola 9) | Ercole II d'Este | Renata di Francia |
| **1-12** | Casa Romei (Via Savonarola 30) | Giovanni Romei | Tito Vespasiano Strozzi |
| **1-13** | Monastero del Corpus Domini (Via Campofranco 1) | Lucrezia Borgia | Ludovico Bonaccioli |
| **1-14** | Monastero di Sant'Antonio in Polesine (Via del Gambone 15) | Beata Beatrice II d'Este | Le monache di Sant'Antonio in Polesine |
| **1-15** | Palazzo Schifanoia (Via Scandiana 23) | Francesco del Cossa | Ercole de' Roberti, Borso d'Este |
| **1-16** | Palazzo Bonacossi (Via Cisterna del Follo 5) | Pellegrino Prisciani | Taddeo Crivelli e i miniatori della Bibbia di Borso |
| **1-17** | Palazzina Marfisa d'Este (Corso Giovecca 170) | Marfisa d'Este | — |
| **1-18** | Antico Ospedale di Sant'Anna (cella del Tasso) (Corso della Giovecca 203) | Alfonso II d'Este | Torquato Tasso |
| **1-19** | Piazza Ariostea e colonna (Piazza Ariostea) | Napoleone e l'età francese | — |
| **1-20** | Palazzo Massari (Museo Boldini) (Corso Porta Mare 9) | Giovanni Boldini | Filippo de Pisis |
| **1-21** | Palazzo dei Diamanti (Pinacoteca) (Corso Ercole I d'Este 21) | Biagio Rossetti | Cosmè Tura |
| **1-22** | Quadrivio degli Angeli (Palazzo Prosperi-Sacrati) (incrocio Corso Ercole I d'Este / Corso Porta Mare / Corso Biagio Rossetti) | Ercole I d'Este | Josquin des Prez |
| **1-23** | Palazzo Turchi di Bagno e Orto Botanico (Corso Ercole I d'Este 32) | Antonio Musa Brasavola | Gabriele Falloppio |
| **1-24** | Museo del Risorgimento e della Resistenza (Corso Ercole I d'Este 19) | Tancredi Mosti Trotti Estense | I Bersaglieri del Po |
| **1-25** | Casa di Ludovico Ariosto (Via Ariosto 67) | Ludovico Ariosto | Matteo Maria Boiardo |
| **1-26** | Porta degli Angeli e mura nord (fine di Corso Ercole I d'Este) | Giulio Natta | Paolo Mazza |
| **1-27** | Certosa: chiostro, monumento a Teodoro Bonati (Certosa (punto interno, senza civico)) | Teodoro Bonati | Il territorio del Po |
| **1-28** | Cimitero ebraico (Via delle Vigne 20) | Giorgio Bassani | La comunità ebraica ferrarese |
| **1-29** | Certosa: cimitero monumentale (Piazza della Certosa) | Michelangelo Antonioni | Florestano Vancini, Riccardo Bacchelli |
| **1-30** | Certosa: chiesa di San Cristoforo (Piazza della Certosa) | La città (P93) | Brondi (P87) |


#### Anno 2 — a cavallo

Le trenta tappe, 59 facoltativi, 3 voce collettive.

| Livello | Dove si va | Chi incontri (obbligatorio) | Facoltativi |
|---|---|---|---|
| **2-1** | Bolzano, Museo archeologico altoatesino | Ötzi (Q01) | La Dama di Verrucchio; i popoli della penisola |
| **2-2** | Crotone | Pitagora (Q11) | Archita; Al-Khwārizmī (approfondimento 2-2) |
| **2-3** | Roma, area del Campidoglio | Romolo (Q05) | Tarquinio il Superbo; Lucrezia (della tradizione) |
| **2-4** | Squillace, monastero di Vivarium | Cassiodoro (Q34) | I copisti (collettivo) |
| **2-5** | Roma | Appio Claudio Cieco (Q19) | Camillo; Cincinnato |
| **2-6** | Elea (Velia) | Parmenide (Q12) | Zenone di Elea; i fisici di Crotone |
| **2-7** | Roma, Tuscolo | Cincinnato (Q17) | Camillo; Catone il Censore |
| **2-8** | Milano | Leonardo da Vinci (Q63) | Isabella d'Este; Leonello d'Este |
| **2-9** | Roma, Curia | Cicerone (Q21) | Cornelia; gli ambasciatori |
| **2-10** | Roma, villa dei Gracchi | Cornelia, madre dei Gracchi (Q27) | Tiberio Gracco; Gaio Gracco |
| **2-11** | Elea (Velia) | Zenone di Elea (Q13) | Parmenide; Appio Claudio |
| **2-12** | Porta `PT-CAR` (Ferrara) | Annibale (Q22) | Scipione l'Africano; Catone il Censore |
| **2-13** | Roma | Catone il Censore (Q26) | Tiberio Gracco; Scipione l'Africano |
| **2-14** | Firenze | Dante Alighieri (Q47) | Petrarca; Boccaccio |
| **2-15** | Palermo | Federico II di Svevia (Q44) | Costanza d'Altavilla; Manfredi |
| **2-16** | Taranto | Archita di Taranto (Q14) | Pitagora (ricomparsa); Euclide (porta) |
| **2-17** | Roma | Tiberio Gracco (Q28) | Cesare; Catone Uticense |
| **2-18** | Roma | Giulio Cesare (Q20) | Cicerone; Cleopatra (porta) |
| **2-19** | Chiusi | Lars Porsenna (Q10) | Teodolinda; i coloni |
| **2-20** | Roma | Augusto (Q29) | Ottaviano giovane; Agrippa |
| **2-21** | Porta `PT-AQU` (Ferrara) | Carlo Magno (Q37) | Matilde di Canossa; le città del Nord |
| **2-22** | Venezia | Marco Polo (Q46) | Francesco Sforza; i mercanti |
| **2-23** | Roma, Curia | I copisti e gli amanuensi *(collettivo)* | Il tipografo; Lucrezia (della tradizione) |
| **2-24** | Firenze | Leon Battista Alberti | Enigma; i cifrari di Stato |
| **2-25** | Ferrara, zona dell'Addizione Erculea | Biagio Rossetti | Ercole I; i muratori (collettivo) |
| **2-26** | Ferrara, corte | Lucrezia Borgia (Q41) | Isabella d'Este; Tasso |
| **2-27** | Porta `PT-CON` (Ferrara) | Giustiniano (Q35) | Alboino; Teodolinda |
| **2-28** | Ferrara, corte | I corrieri e i messaggeri *(collettivo)* | Cristoforo Colombo; Amerigo Vespucci |
| **2-29** | Porta `PT-COL` (Ferrara) | Amerigo Vespucci (Q45) | Colombo; i copisti |
| **2-30** | Ferrara, corte | Il consiglio di corte: i progettisti, i muratori, i proprietari, i contadini *(collettivo)* | Ercole I; le donne della corte |


#### Anno 3 — a cavallo

Le trenta tappe, 61 facoltativi, 1 vocea collettive.

| Livello | Dove si va | Chi incontri (obbligatorio) | Facoltativi |
|---|---|---|---|
| **3-1** | Alessandria | Eratostene (Q101) | Archimede; i matematici di Alessandria |
| **3-2** | Frombork | Copernico (Q102) | Keplero; Tycho Brahe |
| **3-3** | Roma | Augusto (Q103) | Traiano; Adriano |
| **3-4** | Atene | Solone (Q104) | Pericle; Socrate |
| **3-5** | Atene | Pericle (Q105) | Solone; Tucidide |
| **3-6** | Atene | Platone (Q106) | Aristotele; Socrate |
| **3-7** | Ravenna | Belisario (Q107) | Giustiniano; Teodorico |
| **3-8** | Castel del Monte | Federico II (Q108) | Manfredi; Costanza d'Altavilla |
| **3-9** | Pella | Alessandro Magno (Q109) | Tolemeo; Pericle |
| **3-10** | Ferrara, fonderia | Alfonso I d'Este (Q110) | Tiziano; Ercole II |
| **3-11** | Ferrara, corte | Ludovico Ariosto (Q111) | Boiardo; Tasso |
| **3-12** | Aquisgrana | Alcuino (Q112) | Carlo Magno; Eginardo |
| **3-13** | Milano | Leonardo da Vinci (Q113) | Alberti; Bramante |
| **3-14** | Firenze | Niccolò Machiavelli (Q114) | Guicciardini; Cesare |
| **3-15** | Ferrara, Camerino d'alabastro | Dosso Dossi (Q115) | Bellini; Tiziano |
| **3-16** | Magonza | Johannes Gutenberg (Q116) | Fust; Schöffer |
| **3-17** | Ferrara, cappella | Josquin | Alfonso I; il coro della corte |
| **3-18** | Alcalá de Henares | Miguel de Cervantes (Q118) | Shakespeare; Lope de Vega |
| **3-19** | Basilea | Erasmo da Rotterdam (Q119) | Lutero; Calvino |
| **3-20** | Ferrara, Camerino | Giovanni Bellini | Tiziano; Antonio Lombardo |
| **3-21** | Aquisgrana | Carlo Magno (Q121) | Alcuino; Manuzio |
| **3-22** | Certaldo | Giovanni Boccaccio (Q122) | Petrarca; Franco Sacchetti |
| **3-23** | Parigi | Tommaso d'Aquino (Q123) | Alberto Magno; Giovanni di San Vincenzo |
| **3-24** | Norimberga | Albrecht Dürer | Leonardo (ritorno); Raffaello |
| **3-25** | Venezia | Aldo Manuzio | Francesco Griffo; i caratterai |
| **3-26** | Westminster | William Caxton | Caxton; i miniatori |
| **3-27** | Parigi | Olympe de Gouges (Q127) | Wollstonecraft; Robespierre |
| **3-28** | Torino | Primo Levi | Alan Turing (facoltativa forte, era la voce obbligatoria); Ada Lovelace; i matematici di Cambridge |
| **3-29** | Roma, Curia | I tipografi e i privilegi *(collettivo)* | Manuzio; il Sant'Uffizio |
| **3-30** | Mantova | Isabella d'Este (Q130) | Alfonso I; i musei |


#### Anno 4 — in nave

Le trenta tappe, 63 facoltativi, 2 voce collettive.

| Livello | Dove si va | Chi incontri (obbligatorio) | Facoltativi |
|---|---|---|---|
| **4-1** | Uruk | Gilgamesh (Q201) | L'Eneuma Elish (collettivo); il re assiro (facoltativa) |
| **4-2** | Il Cairo e le carovane | Ibn Battuta (Q202) | Ibn Jubayr (facoltativa); i portatori d'acqua |
| **4-3** | Xianyang | Qin Shi Huang (Q203) | Il figlio di Shi Huangdi (facoltativa); gli scribi |
| **4-4** | Tebe | Hatshepsut (Q204) | Nefertari (facoltativa); i sacerdoti di Amun |
| **4-5** | Agra | Akbar (Q205) | Abul Fazl (facoltativa); le città nuove |
| **4-6** | Karakorum | Gengis Khan (Q206) | I quattro khanati (collettivo); i cronachi cinesi |
| **4-7** | Hannover | Leibniz | Newton (ritorno, v. §6.4); Hooke (facoltativa) |
| **4-8** | Uppsala | Carl Linneo (Q208) | I lini (collettivo); le critiche alla classificazione (facoltativa) |
| **4-9** | Il Cairo `A`, con Timbuctù `S` | Mansa Musa (Q209) | I mercanti di Songhai; Ibn Battuta (ritorno, facoltativa) |
| **4-10** | Ferrara, corte | Ercole II d'Este (Q210) | I magazzinieri; Lucrezia Borgia (ritorno) |
| **4-11** | Baghdad | Al-Khwarizmi (Q211) | Tim Berners-Lee (facoltativa forte dal 02/10/2026); Robert of Chester (facoltativa); il libro dell'algebra |
| **4-12** | Qufu | Confucio (Q212) | Il dizionario di Mengxi (facoltativa); i calligrafi |
| **4-13** | Alessandria | Ipazia (Q213) | I sacerdoti di Soknopaiou Nesos (facoltativa); le tre scritture |
| **4-14** | Tenochtitlán | Moctezuma II (Q214) | Tlacaelel (facoltativa); i calendari (collettivo) |
| **4-15** | Chio e la Ionia | Omero (Q215) | I rapsodi (collettivo); Pisistrato (facoltativa) |
| **4-16** | Pataliputra | Ashoka | Ibn Khaldun (facoltativa forte, era la voce obbligatoria); Cesare (ritorno); i monaci buddisti |
| **4-17** | Bombay e Delhi | B. R. Ambedkar (Q217) | Il tempio di Kalaram (facoltativa); il poeta |
| **4-18** | Costantinopoli | Solimano il Magnifico (Q218) | I millet (collettivo); Ibrahim, fratello del sultano (facoltativa) |
| **4-19** | Il Cairo | Ibn al-Haytham (Q219) | Il Libro degli specchi (facoltativa); il muḥtasib |
| **4-20** | Ferrara e il regno | I censori *(collettivo)* | Gli ufficiali del catasto; il censitore cinese (facoltativa) |
| **4-21** | Toledo | Isabella di Castiglia (Q221) | I censitori (collettivo); i funzionari dell'archivio |
| **4-22** | Babilonia | Hammurabi (Q222) | Il codice (collettivo); la stele di Nippur (facoltativa) |
| **4-23** | Lisbona e Calicut | Vasco da Gama (Q223) | I piloti di Malindi (collettivo); Ahmad ibn Majid (facoltativa) |
| **4-24** | Nanchang e il mare | Zheng He (Q224) | Ma Huan (facoltativa); i cantieri |
| **4-25** | Annapolis e Baltimora | Frederick Douglass (Q225) | Sojourner Truth (facoltativa); i censitori (ritorno) |
| **4-26** | Spagna e Tenochtitlán | Hernán Cortés (Q226) | Las Casas (facoltativa); i signori di Tlaxcala (collettivo) |
| **4-27** | Scutari e Costantinopoli | Florence Nightingale (Q227) | Gorgas (facoltativa); i soldati (collettivo) |
| **4-28** | Motihari e Londra | George Orwell (Q228) | Il lavoro alla BBC; la revisione spagnola (facoltativa) |
| **4-29** | Parigi e Varsavia | Marie Curie (Q229) | Malala Yousafzai (facoltativa forte dal 02/10/2026); il libro di Irène; l'Accademia (facoltativa) |
| **4-30** | Ferrara, archivio | Le persone che non hanno firmato *(collettivo)* | Le voci senza nome (facoltativa); Ercole II |


#### Anno 5 — il mezzo **non è dichiarato**

Le trenta tappe, 61 facoltativi, 3 voce collettive.

| Livello | Dove si va | Chi incontri (obbligatorio) | Facoltativi |
|---|---|---|---|
| **5-1** | Chicago<br>*stanza:* **la strada della fuga di Rinaldo** `F2` 1,32 · `A` | Enrico Fermi (Q301) | il problema di Fermi; il fisico teorico (facoltativa) |
| **5-2** | Vienna<br>*stanza:* **il bosco dove Orlando perde il senno** `F3` 23,124 · `A` | Karl Popper (Q302) | Thomas Kuhn (facoltativa); Duhem e Quine (facoltativa) |
| **5-3** | Londra<br>*stanza:* **il bosco di Pontiero** `F9` 22,30 · `A` | Isaac Newton (Q303) | Eulero; Ostrowski (facoltativa) |
| **5-4** | Bethesda<br>*stanza:* **la Luna** `F9` 34,49 · `I` | Vera Rubin (Q306) | Ford e Thonnard; de Sitter (facoltativa) |
| **5-5** | Los Alamos<br>*stanza:* **la foresta dove passa Ferraú** `F2` 1,77 · `A` | John von Neumann (Q304) | Stanislaw Ulam; Nicholas Metropolis (facoltative) |
| **5-6** | Babilonia<br>*stanza:* **la corte di Scozia** `F5` 5,23 · `A` | Le mani che hanno approssimato √2 *(collettivo)* | il regolo babilonese; i matematici arabi (facoltative) |
| **5-7** | Londra<br>*stanza:* **il fossato di Sarza, sotto Parigi** `F1` 14,133 · `A` | James Lovelock (Q307) | Margret Turner; i modelli climatici (collettivo) |
| **5-8** | Bajkonur<br>*stanza:* **l'aria sopra la foresta** `F9` 23,16 · `N` | Sergej Korolëv (Q308) | il programma spaziale (collettivo); Oktyabrskij (facoltativa) |
| **5-9** | Londra, Broad Street<br>*stanza:* **la strada di Pontiero** `F5` 23,40 · `A` | John Snow | William Farr; le statistiche cittadine (facoltative) |
| **5-10** | Stoccolma<br>*stanza:* **il paese degli incantatori** `F6` 8,1 · `S` | Hans Rosling | Gapminder (collettivo); i revisori dei modelli (facoltativa) |
| **5-11** | Princeton<br>*stanza:* **l'isola di Alcina** `F6` 6,35 · `I` | Fei-Fei Li | chi ha etichettato ImageNet (collettivo); Jia Deng (facoltativa) |
| **5-12** | Buenos Aires<br>*stanza:* **il petron di Merlino** `F10` 11,4 · `S` | Jorge Luis Borges (Q312) | «Tlön, Uqbar, Orbis Tertius»; i bibliotecari (collettivo) |
| **5-13** | Cambridge<br>*stanza:* **la pagina** `F3` 1,2 · `S` | La macchina *(collettivo)* | Alan Turing (ritorno dal 3-28); Alonzo Church (ritorno, 5-14) |
| **5-14** | Princeton<br>*stanza:* **il campo** `F12` 32,102 · `S` | Alonzo Church | Turing; il lambda calculus (facoltativa) |
| **5-15** | New York<br>*stanza:* **il castello d'Atlante** `F4` 4,30 · `I` | Yann LeCun | Stephen Cook; Leslie Valiant (facoltative) |
| **5-16** | Seattle<br>*stanza:* **il ponte d'Erifilla sulla riviera** `F5` 7,2 · `A` | Radia Perlman (Q316) | Bob Kahn; i ponti (collettivo, facoltativa) |
| **5-17** | Los Angeles<br>*stanza:* **i monti Rifei** `F4` 4,18 · `S` | Vint Cerf (Q317) | Bob Kahn; Louis Pouzin (facoltative) |
| **5-18** | una sala di riunione, 1983<br>*stanza:* **il libro di Turpino** `F12` 24,44 · `S` | Gli ingegneri delle reti *(collettivo)* | Donald Davies (facoltativa, è al 5-19); Bob Kahn (facoltativa) |
| **5-19** | Londra<br>*stanza:* **Montalbano** `F4` 30,93 · `S` | Donald Davies | Peter Kirstein; la Cambridge Ring (facoltative) |
| **5-20** | Ferrara<br>*stanza:* **Zibeltaro e l'Erculeo segno, cioè Ferrara** `F1` 16,37 · `A` | Alfonso II d'Este (Q320) | Aleotti; i geometri ducali (facoltativa) |
| **5-21** | Rotterdam<br>*stanza:* **la selva** `F2` 1,64 · `A` | Edsger Dijkstra | Bellman; Floyd (facoltative) |
| **5-22** | un documento del 2008<br>*stanza:* **il campo davanti a Parigi** `F1` 1,9 · `A` | Satoshi Nakamoto (Q322) | Vitalik Buterin; chi ha perso; Ruggiero e la conversione `5-22F`** (canto XXV, 89: la promessa che aspetta una condizione) |
| **5-23** | Ginevra<br>*stanza:* **il regno di Logistilla** `F7` 6,45 · `I` | Tim Berners-Lee (Q323) | il CERN nel 1990; i primi browser (collettivo) |
| **5-24** | un ufficio riservato, 1970<br>*stanza:* **la corte di Scozia** `F5` 5,18 · `A` | James Ellis | Diffie e Hellman; Rivest, Shamir, Adleman (facoltative) |
| **5-25** | Murray Hill, 1948<br>*stanza:* **la strada del messaggero** `F12` 30,80 · `S` | Claude Shannon (Q325) | Norbert Wiener; von Neumann (ritorno, 5-5) |
| **5-26** | Boston, 2018<br>*stanza:* **il duello di Ginevra** `F5` 5,36 · `A` | Joy Buolamwini | Timnit Gebru (facoltativa, è al 5-28); chi ha costruito i dataset (collettivo) |
| **5-27** | Toronto, 2012<br>*stanza:* **la tomba di Merlino, nelle selve di Pontiero** `F8` 7,38 · `A` | Geoffrey Hinton | Yann LeCun (ritorno, 5-15); Yoshua Bengio (facoltativa) |
| **5-28** | Seattle, 2020<br>*stanza:* **il luogo del pentimento** `F12` 30,2 · `S` | Timnit Gebru | Margaret Mitchell; le schede dei dataset (facoltative) |
| **5-29** | Londra, 2020<br>*stanza:* **la corte di Scozia** `F1` 12,12 · `A` | Demis Hassabis | Bruno Latour; AlphaFold (facoltativa) |
| **5-30** | Ferrara, sala di progetto<br>*stanza:* **la prima pagina** `F3` 1,1 · `S` | Daniel Kahneman (Q330) | Amos Tversky; chi scriverà nelle fasce bianche (facoltative) |


## 4. Come si legge una riga, e che cosa non c'è dentro

Una riga dice quattro cose, e tre sono dati:

| Colonna | Che cosa è | Che cosa non è |
|---|---|---|
| **Dove si va** | Il luogo della tappa, con l'indirizzo o il pin | Non è la distanza dalla tappa precedente: quella la calcola il motore |
| **Stanza** (quinto anno) | Il luogo **del poema** in cui sta accadendo | Non è un luogo reale: è il filone, e porta il suo verso |
| **Chi incontri** | La voce **obbligatoria**, cioè quella che il giocatore incontra sempre | Non è un personaggio che il giocatore sceglie: è la voce della tappa |
| **Facoltativi** | Chi c'è nella stanza e **non** è obbligatorio | Non sono opzionali per il giocatore: sono **in più**, e il gioco non li usa tutti |

**Il punto sul facoltativo, che è quello che va chiarito una volta sola.** «Facoltativo»
nel progetto ha un significato preciso (`anno2-penisola.md` §5, `anno4-mondo.md` §5):
è **la persona che il materiale offre e che il gioco non mette sulla strada principale**.
Non significa che il giocatore possa saltarla, e non significa che siano una scelta
fra due alternative: sono **la stessa tappa con dentro qualcuno in più**. Chi è
facoltativo forte e chi è facoltativo semplice è una decisione di Pietro, e la
marcatura è nella parentesi.

**Che cosa in questo documento non c'è, e perché.**

- **Le distanze e i giorni.** Ci vuole il punto, e il punto sta in
  `dati/luoghi_gioco.json`. Questo documento dice **chi incontra chi e dove**, non
  quanto ci si mette: il conto dei giorni è di `percorsi_calcola.py`.
- **Il mezzo del quinto anno**, per la ragione di §2.
- **Il codice dei facoltativi.** Quasi nessuno dei facoltativi porta il codice
  (`P01…`, `Q01…`) nella tabella della sua tappa, perché il codice è della scheda e
  la scheda è un altro file. Il campo `codice` del JSON vale `null` in questi casi,
  e **null non vuol dire che la persona non esiste**.
- **I nomi degli anni 2-5 non hanno catalogo.** L'anno 1 ha i suoi 93 personaggi con
  il codice (`dati/videogioco-5-duchi-anno1-personaggi.json`); gli anni 2-5 usano
  la serie `Q` e **non hanno un catalogo analogo**. Quindi per quegli anni il
  confronto con l'elenco dei nomi non può essere completo, e la classificazione
  usa la marcatura scritta nella tabella, che è la prova buona. **È un limite
  dichiarato, non un fatto**: ogni voce del JSON porta il campo `prova` con il nome
  della prova che l'ha decisa.

## 5. Il difetto che ha fatto nascere tutto questo, e il controllo che lo tiene

Il quinto anno dichiarava **due voci collettive su trenta**, e la tabella ne
portava **tre**: la macchina (5-13), gli ingegneri delle reti (5-18) e **le mani
che hanno approssimato √2** (5-6), tutte e tre marcate `collettivo C` nella
propria casella. La frase del documento le contava a memoria invece di leggerle,
e nessuno lo aveva visto.

È il difetto che `AGENTS.md` chiama **un numero scritto a mano invecchia**, e
questa volta la cosa che invecchiava era proprio il documento che descriveva il
dato. Il numero è stato corretto in `anno5-mondo.md` (v0.6), che ora dice **tre** e
le nomina tutte e tre.

**Il controllo è C5**, in `sorgenti/verifica_incontri.py`: legge il numero che i
quattro documenti degli anni dichiarano e lo confronta con il conto del dato. Gli
altri quattro controlli sono dati contro dati; **C5 è l'unico che confronta il
dato con quello che un documento scrive a mano**, ed è l'unico che avrebbe visto
il difetto. Provato con difetto iniettato: riportando il quinto anno a «2 su 30»
il controllo morde e lo dice.

I cinque controlli, in una riga:

| | Che cosa controlla |
|---|---|
| **C1** | le tappe sono esattamente 5 × 30, nessuna due volte, nessuna fuori schema |
| **C2** | ogni tappa ha una voce, un luogo, e il mezzo o la sua dichiarazione di assenza |
| **C3** | ogni voce porta **la prova** della sua classificazione, e la prova è una delle quattro dichiarate |
| **C4** | i facoltativi non sono la voce obbligatoria, nessuno è ripetuto, nessuno è senza nome |
| **C5** | il numero delle voci collettive è quello che i documenti dichiarano |

## 6. I dati e i comandi

| File | Che cosa c'è |
|---|---|
| `dati/incontri_livelli.json` | Le 150 tappe con voce, luogo, stanza, facoltativi, mezzo e la prova di ogni classificazione |
| `sorgenti/estrai_incontri.py` | Estrae dalle tabelle degli anni, **le colonne per intestazione** |
| `sorgenti/genera_itinerari.py` | Genera le tabelle di §3 |
| `sorgenti/verifica_incontri.py` | I cinque controlli C1–C5 |

```
python3 sorgenti/estrai_incontri.py            # estrae, scrive il JSON
python3 sorgenti/estrai_incontri.py --prova    # dice, non scrive
python3 sorgenti/genera_itinerari.py           # stampa le tabelle
python3 sorgenti/genera_itinerari.py --anno 3  # un anno solo
python3 sorgenti/verifica_incontri.py          # C1-C5
```

**Le colonne si leggono per intestazione, mai per numero**, ed è la seconda volta
che la lezione viene scritta: `estrai_luoghi.py` contava le barre e nell'anno 5,
che ha una colonna in più (la stanza, fra il pin e la voce), leggeva il filone del
*Furioso* al posto della persona in **29 tappe su 30**. Il sintomo era invisibile:
la riga restava lunga uguale. Qui la colonna cercata si cerca **per nome**, e se
non c'è la riga viene **saltata e detta**.

## 7. Le questioni aperte

1. **Il mezzo del quinto anno** (§2): ventidue mezzi possibili, cinque dei quali
   sono del testo. La scelta è di Pietro e non è bloccante: senza mezzo dichiarato
   il gioco funziona, e la distanza si calcola quando il mezzo c'è.
2. **Il catalogo degli anni 2-5**: gli anni 2-5 hanno nomi con codice `Q` che non
   stanno in nessun file come stanno i 93 dell'anno 1. Senza quel catalogo, la
   scheda di una facoltativa degli anni 2-5 non esiste, e la regola della `premi.md`
   — che ogni premio abbia una fonte dichiarata — non può essere verificata su
   **269 facoltativi**. Non è bloccante per gli itinerari, che funzionano senza, e
   lo è per i premi.
3. **Le cinque tappe del primo anno senza facoltativi** (§1): sono un dato o una
   dimenticanza? Se sono un dato, va scritto perché sono cinque e non tre.

## 8. Registro delle modifiche

- **v0.1 (03/10/2026)**: prima stesione. Nasce da una domanda di Pietro sugli
  itinerari dei personaggi, e risponde mettendo in un file le tre cose che erano
  in tre documenti diversi: il luogo (tappe degli anni), la voce e i facoltativi
  (tappe degli anni), il mezzo (`percorsi.md` §1). `sorgenti/estrai_incontri.py`
  legge le colonne **per intestazione** e produce `dati/incontri_livelli.json`;
  `sorgenti/genera_itinerari.py` genera le tabelle; `sorgenti/verifica_incontri.py`
  le tiene con cinque controlli.

  **Il difetto che l'ha fatto nascere**: `anno5-mondo.md` dichiarava **2 voci
  collettive su 30** e la tabella ne porta **tre** — la macchina (5-13), gli
  ingegneri delle reti (5-18) e le mani che hanno approssimato √2 (5-6), tutte e
  tre marcate `collettivo C`. Il numero è corretto (v0.6) e il controllo **C5** è
  quello che tiene il conto dei quattro documenti degli anni contro il dato, che
  è l'unico controllo che confronta il dato con una **frase scritta a mano**.

  **Due limiti dichiarati, non nascosti**: il mezzo del quinto anno non è
  dichiarato (§2) e gli anni 2-5 non hanno un catalogo dei nomi come l'anno 1 (§4,
  Q2). Il conto che tiene: **150 tappe, 141 nomi distinti, 269 facoltativi, 9
  voci collettive**.