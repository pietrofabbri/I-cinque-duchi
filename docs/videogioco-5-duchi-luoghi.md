---
titolo: Videogioco "I cinque duchi" — La regola dei luoghi: i tipi di legame fra personaggio e luogo, catalogo per anno e mappa del quinto anno
versione: 0.1
data: 2026-10-01
autore: Pietro Fabbri (con Claude)
fonte del materiale: le liste di associazioni personaggio–luogo per gli anni 2, 3 e 4 e la revisione delle associazioni con i luoghi dell'Orlando furioso per il quinto anno, proposte da Pietro (01/10/2026), con i criteri di tre e quattro tipi di legame e l'elenco delle associazioni da eliminare
dati: videogioco-5-duchi-luoghi.json (da generare, v0.1: un record per associazione, con anno, personaggio, luogo, tipo di legame, pin o porta, nota, attendibilità)
documenti collegati: videogioco-5-duchi-schema-livelli.md (v1.1), videogioco-5-duchi-anno5-mondo.md (v0.1, in costruzione), videogioco-5-duchi-anno4-mondo.md (v0.2), videogioco-5-duchi-anno3-europa.md (v0.2), videogioco-5-duchi-anno2-penisola.md (v0.1), videogioco-5-duchi-anno1-ferrara.md (v0.3), videogioco-5-duchi-anno1-mappa.md (v0.8), videogioco-5-duchi-motore-e-grafica.md (v0.1), AGENTS.md
---
# La regola dei luoghi

## 0. Che cosa contiene questo documento, e perché è trasversale

Il documento **formalizza** il materiale geografico di Pietro e ne verifica le associazioni. Non è il documento di un anno: è **la regola che valge per tutti e cinque**, e i documenti degli anni la richiamano.

Il problema che risolve è il più silenzioso di tutto il progetto. Fino ad ora la mappa si è costruita per tappe, e ogni tappa ha avuto «un luogo» senza che nessuno si chiedesse **perché quel luogo e non un altro**. Il risultato è una mappa in cui la metà dei pin sono città di nascita, il resto sono monumenti, e nessuno dei due è detto al giocatore.

La regola che Pietro propone è semplice e va bene:

> **meglio 60 associazioni solidissime che 150 collegamenti ottenuti per analogia.**

Questo documento la rende operativa con quattro passi:

1. i **cinque tipi di legame** fra una persona e un luogo, con un codice e una prova da superare (§1);
2. il **criterio di eliminazione**, che è più forte del criterio di inclusione (§2);
3. il **catalogo verificato** delle associazioni degli anni 2, 3 e 4, con le correzioni e i buchi geografici (§3);
4. la **mappa del quinto anno**, che è la geografia dell'*Orlando furioso* (§4).

*(aggiunta)* C'è un quinto tipo, che non era nella lista di Pietro ma che il catalogo rende necessario: il **luogo di crescita**. Se ne parla in §1.5.

---

## 1. I tipi di legame

### 1.1 La distinzione di partenza

Pietro propone tre tipi:

| Tipo | Definizione | Esempio |
|---|---|---|
| **Luogo biografico** | il personaggio è nato, ha vissuto o è morto lì | Dante → Firenze |
| **Luogo dell'azione** | lì è avvenuto qualcosa di decisivo | Garibaldi → Marsala |
| **Luogo simbolico** | il luogo permette di comprendere l'eredità o il significato della persona | Marx → Manchester |

Il terzo tipo è prezioso per una ragione precisa: **impedisce alla mappa di diventare una catina delle case natali**. Ma da solo non basta, perché il «luogo simbolico» è la categoria che, senza una prova, diventa un contenitore per qualsiasi cosa.

### 1.2 I quattro tipi operativi

*(aggiunta — il quarto tipo serve per i luoghi fantastici del quinto anno)*

| Codice | Tipo | Che cosa ammette | Prova da superare |
|---|---|---|---|
| `B` | **biografico** | nascita, residenza, morte | un fatto documentato, con data e fonte |
| `A` | **dell'azione** | il fatto decisivo è avvenuto lì | il fatto, non il monumento che lo ricorda |
| `S` | **simbolico** | il luogo *spiega* la persona o l'epoca | una frase, e non un'intuizione |
| `I` | **interpretativo** | **solo luoghi che non esistono** | il personaggio aiuta a capire il significato del luogo |

La distinzione fra `S` e `I` è la più importante del documento, ed è la ragione per cui il quinto anno funziona:

> **`S` e `I` non si confondono mai.** Un luogo reale (`S`) dice qualcosa di vero su una persona: Garibaldi a Marsala, Marx a Manchester, Oppenheimer a Los Alamos. Un luogo inesistente (`I`) dice qualcosa di vero su un **testo**: il castello di Atlante, l'isola di Alcina, la valle del Senno, la Luna.

Se si permette un legame interpretativo verso un luogo reale, la mappa si riempie di falsi e il gioco diventa un atlante delle metafore. Se lo si vieta anche per i luoghi fantastici, il *Furioso* resta un libro chiuso. **La regola è dunque: `I` esiste, e vale solo per i luoghi che non esistono.**

*(nota)* Nel documento i codici sono `B`, `A`, `S`, `I` e `C` (crescita, §1.5). Il `C` **non** collide con l'`C` della scala di attendibilità (`collettivo`): sono due campi diversi e non vengono mai scritti nello stesso campo.

### 1.3 Il test della frase

*(regola operativa, da usare nella catalogazione)*

> **Ogni associazione deve poter essere spiegata in una frase, senza aggettivi che non si possano verificare, e senza «perché evoca».**

Se la frase contiene «evoca», «richiama», «è il simbolo di», il legame è `I` e va in un luogo inesistente — oppure va eliminato.

Esempi di frase che **passano**:
- «Marconi vi fece i primi esperimenti alla Villa Griffone di Pontecchio nel 1895» → `A`.
- «Mandela fu rinchiuso per diciotto anni a Robben Island» → `A`.
- «Oppenheimer diresse Los Alamos, che non esisteva prima della guerra» → `A`, e il luogo è *nato per il progetto*: questo è il caso migliore.

Esempi di frase che **non passano**:
- «Marconi → Bologna, le comunicazioni senza fili» → non passava: il fatto è a Pontecchio, e il resto è etichetta. *(corretto, §3.1)*
- «Sacagawea → Missouri, i popoli indigeni» → non passa: il fatto c'è, il luogo no. *(corretto, §3.3)*

### 1.4 Un pin per tappa, non un nome per tappa

*(aggiunta — conseguenza tecnica)*

Il progetto ha una sola scelta per tappa. Quindi **un personaggio con due luoghi non crea due pin**: crea **un pin e una nota**. La scheda del personaggio porta un solo `pin`, dichiarato come `B` quando possibile; gli altri luoghi vanno in `altri_luoghi`, con il loro tipo.

Esempio, il modello che vale per tutti gli anni: **Leonardo → Vinci (`B`), Milano e il Cenacolo (`A`)**. Un solo pin (Vinci), perché è dove il gioco si ferma; il Cenacolo è il rimando.

### 1.5 Il quinto tipo: il luogo di crescita `C`

*(aggiunta — necessaria, e non evitabile)*

Nel catalogo dell'Anno II c'è un caso che nessuno dei tre tipi copre: **Sophia Loren → Napoli**. Loren è nata a Roma ed è cresciuta a Pozzuoli. Napoli non è né il luogo di nascita né il luogo di un'azione decisiva: è **dove è cresciuta**, e quel luogo le ha dato la lingua, il dialetto, il cibo e il modo di guardare.

Eliminare l'associazione sarebbe una perdita; classarla come `B` sarebbe una bugia. La soluzione è un quinto tipo:

| Codice | Tipo | Esempio |
|---|---|---|
| `C` | **di crescita** | Sophia Loren → Pozzuoli; Maria Montessori → Chiaravalle |

*(proposta)* Il tipo `C` si usa **una volta sola per personaggio**, e il gioco lo dichiara: «questa persona è cresciuta in un luogo che le ha lasciato qualcosa che non compare nei libri di storia». È anche il tipo che rende il gioco meno noioso, perché spiega perché certe persone hanno un accento e altre no.

---

## 2. Il criterio di eliminazione

*(criterio di Pietro, verificato e reso operativo)*

### 2.1 Le eliminazioni proposte, e il mio giudizio

| Associazione proposta | Decisione | Verifica |
|---|---|---|
| Alan Turing → Parigi | **eliminare** | **concordo.** Il luogo corretto è Bletchley Park (`A`); Turing è passato da Parigi, non c'è nato né ci ha lavorato. Il collegamento è un'allusione, non un fatto |
| Claude Shannon → Parigi | **eliminare** | **concordo.** Nessun fatto. Shannon è di Michigan e Bell Labs |
| Tim Berners-Lee → Alessandria | **eliminare** | **concordo**, ed è un caso che vale la pena tenere come esempio didattico: la Library of Alexandria è l'immagine giusta per «il Web», e la stima sbagliata del contesto è esattamente ciò che il gioco chiede di evitare |
| Jimmy Wales → Alessandria | **eliminare** | **concordo** |
| Steve Jobs → Isola di Alcina | **eliminare** | **concordo.** È una metafora travestita da luogo |
| Jeff Bezos → Isola di Alcina | **eliminare** | **concordo**, per lo stesso motivo |
| Mark Zuckerberg → Isola di Alcina | **tenere solo in una missione specifica** | **concordo**, con una precisazione: se la missione è sulle piattaforme e l'attenzione, va nella missione; nel catalogo resta `S` sulla piattaforma, non sull'isola |
| Greta Thunberg → Africa | **spostare** | **concordo.** Thunberg ha una radice sami; ma il legame pertinente è il clima e gli oceani. Africa come «luogo povero che soffre il clima» è una delle trappole che il gioco combatte |
| Edward Snowden → Spagna | **eliminare** | **concordo** |
| Akira Kurosawa → Spagna | **eliminare** | **concordo**, ma annoto un fatto che il catalogo dovrebbe poter usare: Kurosawa ha detto che la **cineasta italiana** gli ha insegnato a filmare (*I Vitelloni*, De Sica). È un legame di influenza documentato e sarebbe un bellissimo `A` fra due culture — ma non è un legame con la Spagna |
| Frida Kahlo → Spagna | **eliminare** | **concordo** |
| Noam Chomsky → Arabia | **eliminare** | **concordo.** Chomsky ha una tesi nota sulla lingua araba, ma non è un legame di luogo |
| Salman Rushdie → Arabia | **spostare** | **concordo**: India (nascita), Regno Unito (vita e cittadinanza), e il caso dei *Versi satanici* riguarda il Pakistan e l'India. Nessuno dei tre è l'Arabia |
| Einstein → Luna | **tenere** | **concordo**: non un legame biografico, ma la relatività generale è ciò che rende possibile l'orbita. È `S` e va dichiarato `S` |
| Neil Armstrong → Luna | **tenere** | **concordo**: `A` e `B` insieme. È l'unico caso in cui il luogo è veramente il punto di arrivo e di nascita della notizia |
| Katherine Johnson → Luna | **tenere** | **concordo**: `A`, perché i calcoli di traiettoria sono suoi. È il caso che rende il giusto il punto: **l'uomo che non ci è andato è più importante, per l'orbita, di quelli che ci sono andati** |
| Daniel Kahneman → Valle del Senno | **tenere** | **concordo**: `I`, e la frase passa: «la valle del *Furioso* raccoglie ciò che gli uomini hanno perduto; Kahneman ha studiato ciò che il nostro giudizio perde» |
| Shoshana Zuboff → Castello di Atlante | **tenere** | **concordo**: `I`, ma va riformulata. Il castello funziona perché l'illusione è *confezionata* con immagini; Zuboff descrive ambienti costruiti per orientare il comportamento. La frase passa, ma con una riformulazione esatta |
| Timnit Gebru → Castello di Atlante | **tenere** | **concordo**: `I`, per l'incorporazione dei pregiudizi nei sistemi |
| Joy Buolamwini → Castello di Atlante | **tenere** | **concordo**, ed è il più forte dei tre: il castello è la realtà **rappresentata in modo sistematicamente distorto**, che è la definizione stessa del suo lavoro |
| Jane Goodall → Paradiso terrestre | **tenere** | **concordo**, come `A` (l'osservazione degli scimpanzé a Gombe) e non come `I` |
| Wangari Maathai → Paradiso terrestre | **tenere** | **concordo**, come `A` (il Giardino delle Donne a Nairobi) |

### 2.2 Un'eliminazione che manca nella lista, e va aggiunta

*(aggiunta)*

| Associazione | Decisione | Motivo |
|---|---|---|
| Claude Shannon → Alessandria | **eliminare** | «la biblioteca» è l'immagine giusta per l'informazione, ed è l'ennesima stima sbagliata. Shannon è di Michigan e di Bell Labs |
| Kurosawa → Spagna | **eliminare** (già nella lista) | e annotare il legame vero: **De Sica → Kurosawa**, documentato, in un'altra direzione |
| Fellini, Calvino, Eco → Ferrara | **attenzione** | v. §4.2: sono `S` o `C` e non `B`; se restano `B` il catal mente |

### 2.3 Il test dell'eliminazione, in tre domande

1. **Il fatto c'è?** Se devo ricorrere a «gli ricorda», «evoca», «è il simbolo», la risposta è no.
2. **Il nome del luogo è sbagliato?** Se il luogo vero è un frazione, un palazzo, un campus e io ho scritto la città grande, la risposta è sì: correggo il nome.
3. **Un altro luogo funzionerebbe uguale?** Se sì, il legame non è di questo luogo: è un legame in generale. Vanno allora cercati i luoghi specifici, o va eliminato.

La terza domanda è quella che ha eliminato di più: **se il luogo è sostituibile, non è un luogo**.

---

## 3. Il catalogo verificato degli anni 2, 3 e 4

*(materiale di Pietro, 01/10/2026; verificato voce per voce dove il fatto era dubbio)*

### 3.1 Anno II — la penisola

**Criterio di copertura (Pietro).** Il criterio geografico deve coprire l'intera penisola e le isole, dall'antichità al contemporaneo.

**Esito della verifica: il catalogo copre bene il territorio e ha tre problemi, nessuno grave.**

| # | Voce | Esito | Correzione |
|---|---|---|---|
| 1 | Marconi → Bologna | **da correggere** | i primi esperimenti sono alla **Villa Griffone di Pontecchio (Sasso Marconi, BO)**, nel 1895; Marconi è nato a Roma. Tipo `A`, nome esatto «Pontecchio Marconi, Villa Griffone» *(verificato)* |
| 2 | Marinetti → Milano (due volte) | **da sciogliere** | stessa città due volte: una sola riga, tipo `B` (nato a Milano) e, se si vuole il Futurismo, il **Teatro della Scala come `A`**, che è un fatto |
| 3 | Margherita Hack (due volte: Firenze/Trieste e Trieste) | **da sciogliere** | una sola riga: **Trieste, `A`** (direttrice dell'osservatorio astronomico di Trieste); Firenze-Arcetri come `A` secondaria da dichiarare |
| 4 | Sophia Loren → Napoli | **da riclassificare** | nata a Roma, cresciuta a Pozzuoli. Tipo `C` (§1.5), pin **Pozzuoli** |
| 5 | Caravaggio → Milano, Pinacoteca di Brera | **da verificare prima dell'uso** | Caravaggio è nato a Caravaggio (MI): il legame con Milano è l'opera, quindi `A`, e serve **il nome del dipinto**. Senza il nome del dipinto l'associazione non supera il test della frase |
| 6 | Leonardo → Vinci **e** → Milano, Cenacolo | **corretto, è il modello** | un solo pin (`B`, Vinci) e il Cenacolo come `A` (§1.4). È l'esempio da copiare per tutte le coppie |
| 7 | Galileo → Padova, Università | **da sdoppiare** | `A` a Padova; `B` a Pisa. Il progetto ha un solo pin per tappa: va deciso quale dei due |
| 8 | Boccaccio → Certaldo | **corretto di tipo** | non vi nacque: si ritirò e vi morì. Tipo `A`, non `B` |
| 9 | Petrarca → Arezzo | **confermato** `B` | e in Anno III lo stesso personaggio è ad Avignone `A`: è un doppio uso **corretto** e va dichiarato come `ritorno di pin` |
| 10 | Anta Garibaldi → Roma, Gianicolo | **confermato** `A` | ferita al Gianicolo durante la difesa di Roma, 1849 |
| 11 | Gramsci → Ales/Torino | **confermato** | `B` ad Ales, `A` a Torino; la prigione di Turi è un terzo luogo, non un quarto |
| 12 | **Ariosto assente** | **da aggiungere** | non è nell'elenco dell'Anno II, ma è l'autore del poema che dà il nome al gioco ed è il centro del quinto anno (§4). Va almeno in catalogo, come `B` (Ferrara) e `A` (la corte estense) |
| 13 | **Isabella d'Este assente** | **da aggiungere** | è già la voce obbligatoria della tappa 3-30 del terzo anno: il suo `pin` (Mantova) va dichiarato `A` e non restare senza tipo |
| 14 | **Squilibrio Roma/Firenze** | **da correggere** | Roma compare 9 volte, Firenze 8. Non è un errore in sé (sono le due capitali del diritto e della lingua), ma **il catalogo deve dire che la maggioranza dei pin sono in due città**, e il gioco deve mostrarlo: è il primo caso in cui la mappa racconta la distribuzione del potere in Italia |

**Buchi geografici dell'Anno II**: nessuno di dimensione. Sono presenti Nord (Vinci, Milano, Venezia, Torino, Genova, Ivrea, Bra, Como, Pavia, Arezzo, Bologna, Trieste), Centro (Roma, Firenze, Assisi, Arezzo, Certaldo), Sud e isole (Canne, Castel del Monte, Agrigento, Catania, Palermo, Marsala, Nuoro, Trento). **Mancano Puglia e Sardegna interna**, che si possono aggiungere o dichiarare come scelta.

### 3.2 Anno III — l'Europa

**Criterio di copertura (Pietro).** Non «i grandi europei», ma Europa occidentale, centrale, orientale, nordica, balcanica e mediterranea, tutte presenti.

**Esito della verifica: la scala è corretta e l'equilibrio è quasi raggiunto, con tre correzioni e quattro buchi.**

| # | Voce | Esito | Correzione |
|---|---|---|---|
| 1 | Edmund Burke → Londra | **da correggere** | Burke nacque a **Dublino**; Londra è dove scrisse e fu deputato. Due pin: `B` Dublino, `A` Londra |
| 2 | Robert Schuman → Strasburgo/Metz | **da correggere** | la **Dichiarazione Schuman** del 9 maggio 1950 è di **Parigi**; Metz è dove Schuman fu sindaco. Tipo `A` per entrambe, **Strasburgo esce** |
| 3 | Omero → Smirne | **confermato ma da dichiarare** | l'antica lista lo dà «re di Smirne»: è una tradizione, non un fatto. Va tenuto come `B` **contestato**, con nota. Lo stesso vale per Aristotele → Stagira (tradizione) e per Dante → Firenze, che è `B` ma anche `A` per l'esilio |
| 4 | Nietzsche → Basilea | **confermato** `A` | insegnò a Basilea 1869-79; il luogo biografico è Röcken |
| 5 | Marx → Londra | **confermato** `A` | la sede è il quartiere dei lavoratori, oggi lo spazio museale del Marx Memorial Library, e **non** la sede del British Museum, che è un equivoco diffuso |
| 6 | Čechov → Mosca; Dostoevskij → San Pietroburgo | **confermati** `A` | e sono l'unico caso in cui due città russe compaiono con due funzioni diverse: mantenerle distinte |
| 7 | Leibniz → Hannover | **confermato** `A` | curò la biblioteca e i manoscritti di Leibniz ad Hannover; nascita a Lipsia |
| 8 | **Unghere e Romania assenti** | **da aggiungere** | nell'elenco non c'è Budapest né Bucarest. È un buco reale: senza l'Europa centro-orientale il «non avere un centro» del terzo anno resta un'affermazione |
| 9 | **Europa nordica assente** | **da aggiungere** | ci sono scozzesi (Watt, Smith, Bell), ma nessun nome scandinavo. Lo stesso vale per Danimarca, Paesi Bassi (c'è Spinoza ✓) e Finlandia |
| 10 | **Balcani assenti** | **da aggiungere** | Costantinopoli ✓ c'è, ma nessun nome dei Balcani occidentali (Belgrado, Zagabria, Sarajevo, Tirana) |
| 11 | **Ferrara, Bassani, Antonioni, De Pisis assenti** | **da decidere** | sono figure ferraresi: vanno nell'Anno II (o nell'atlante) e **non** nel terzo, che è dedicato all'Europa come spazio. Elencarli qui confonderebbe le due scale |

### 3.3 Anno IV — il mondo

**Criterio di copertura (Pietro).** Evitare una lista dominata da Stati Uniti ed Europa; obbligare il giocatore a percorrere Africa, Asia, Medio Oriente, Americhe, Oceania e Pacifico.

**Esito della verifica: il criterio è centrato e l'equilibrio è il più buono dei cinque anni, con una correzione necessaria e cinque buchi.**

| # | Voce | Esito | Correzione |
|---|---|---|---|
| 1 | **Sacagawea → Missouri** | **errore** | Sacagawea nacque verso il 1788-90 nel **Lemhi Valley, oggi Idaho**, e si unì alla spedizione a **Fort Mandan, Dakota del Nord**. Nessuno dei due è il Missouri. Tipo `B` Idaho; `A` Fort Mandan *(verificato)* |
| 2 | **Mandricardo «imperatore di Mongolia»** | **errore** | nel poema è **re de' Tartari**, figlio di Agramante. «Imperatore di Mongolia» non risulta da nessuna fonte: correggere *(il Tarantar compare in testi secondari, ma la formula esatta va verificata)* |
| 3 | Mansa Musa → Timbuctù | **da riclassificare** | il fatto documentato del 1324 è il **Cairo**, dove la delegazione fu ricevuta e dove l'oro fu distribuito; la capitale del Mali era **Niani**; Timbuctù è la grande città del Sahara ma non è attestata come tappa del viaggio. Correggere in **Cairo `A`** + **Timbuctù `S`** — e **correggere di conseguenza `anno4-mondo.md`**, dove il pin di 4-9 è Timbuctù |
| 4 | Ciro → Pasargadae | **da motivare** | Ciro morì a Pasargadae e vi fu sepolto; la battaglia decisiva fu ad **Aria**. Il legame regge, ma per la ragione giusta: il luogo della morte e della tomba |
| 5 | Maometto → Medina | **confermato** `A` | e la Mecca è `B` (nascita): due pin distinti, che il progetto non può avere. Va scelto il più forte per il gioco |
| 6 | Wangari Maathai → Nairobi | **da correggere** | nacque a **Nyeri**; Nairobi è `A` (l'università, il Giardino delle Donne). Stesso caso di Sophia Loren: due pin, uno solo nel gioco |
| 7 | **Laozi → Luoyang; Sun Tzu → Suzhou; Zarathustra → «Iran orientale»** | **contestati** | tutti e tre sono tradizioni, non fatti verificabili, e il terzo indica un luogo che **non esiste come toponimo**. Regola: si possono tenere, ma solo con la dicitura «secondo la tradizione» e senza usarle come pin obbligatorio |
| 8 | **Brasile assente** | **da aggiungere** | l'America latina ha Messico, Perù, Venezuela, Cuba, Cile, Colombia e niente Brasile. È il più grande paese del continente e la sua assenza è visibile |
| 9 | **Indonesia, Corea, Nuova Zelanda assenti** | **da aggiungere** | l'Asia sud-orientale c'è col Vietnam; l'Asia orientale c'è con la Cina e il Giappone; ma gli stati che oggi contano di più nell'economia e nella cultura globale non ci sono |
| 10 | **Canada e Artide assenti** | **da valutare** | Sacagawea è l'unica voce nordamericana dell'elenco, e il Canada non c'è. Per un anno che vuole non essere euro-atlantico, è un buco |
| 11 | Mandela compare due volte | **confermato** | Robben Island (`A`) e Johannesburg (`A`, la prigionia domestica, il 1961-1990) sono due fatti diversi e giustificano due righe di catalogo con un solo pin |
| 12 | **Karikó, Charpentier, Hassabis, Rubbia, Doudna, Marconi viventi** | **da dichiarare** | sono persone vive: valgono le regole decise per il quinto anno (emblema, scheda «in formazione», nessuna affermazione di correttezza) |

---
## 4. Il quinto anno: la geografia dell'Orlando furioso

*(materiale di Pietro, «5º ANNO — ASSOCIAZIONI RIVISTE TRA PERSONAGGI E LUOGHI DELL'ORLANDO FURIOSO», 01/10/2026)*

### 4.1 Perché il *Furioso* è la mappa giusta per il quinto anno

Tre fatti, tutti verificati:

1. **Il poema è nato a Ferrara**: prima edizione del 1516, dedicata a Ippolito d'Este, scritto da un funzionario della corte estense che lavorava per gli Este *(verificato)*.
2. **Ruggiero e Bradamante sono, nel romanzo genealogico del poema, gli antenati della casa d'Este**: dalla loro unione «origina la linea ancestrale della famiglia Este, i patroni dell'autore» *(Britannica, Treccani — verificato)*. Il gioco può dire questo ai ragazzi senza ironia: **il poema contiene la storia della famiglia che ha pagato chi l'ha scritto**.
3. **Ferrara è il centro, e tutto il resto è un viaggio**: il proemio annuncia tre filoni, di cui due sono «invenzioni» e uno è la **war continua** di Carlo Magno e Agramante; la geografia del poema parte dall'Europa e arriva alla Luna *(verificato)*.

Se il quarto anno ha portato il giocatore sulla superficie del pianeta, il quinto gli può dare **un luogo che non è sulla superficie del pianeta**. È l'unico modo che ha il gioco di chiudere i cinque anni con una mappa che non è la mappa reale.

### 4.2 Le tre entrate in un luogo del poema

Ogni luogo del *Furioso* si raggiunge da tre porte diverse, e vanno tenute distinte perché hanno un peso didattico diverso:

| Entrata | Che cosa è | Che cosa porta |
|---|---|---|
| **storica reale** | il luogo esiste davvero e lì è successa una cosa vera | storia con fonti: Garibaldi a Marsala, Van Gogh ad Arles, Fanon in Algeria |
| **poetica** | il luogo esiste solo nel poema e i suoi protagonisti sono i personaggi del testo | la struttura del romanzo: Parigi come teatro della guerra, Biserta come capitale di Agramante |
| **contemporanea** | il luogo esiste oggi e la sua storia prosegue | geopolitica, economia, scienza: Alessandria oggi, Catai oggi, il deserto oggi |

### 4.3 I luoghi fantastici, e il legame interpretativo

Questi sono i luoghi che **non esistono**, e sono gli unici ai quali si può applicare il tipo `I`:

| Luogo | Che cosa è | Che cosa significa nel poema | Chi può stare lì (`I`) |
|---|---|---|---|
| **Il castello di Atlante** | due castelli in cui l'illusione tiene prigioniero chi entra | una realtà costruita per sembrare quella che vuoi | Gebru, Buolamwini, Zuboff, Orwell, Kahneman |
| **L'isola di Alcina** | l'isola in cui Ruggiero vede ciò che vuole vedere e Melissa lo libera con l'anello | **l'inganno ha sembrato realtà** e il consenso estorto sembrava scelta | Zuboff, McLuhan, Debord, Kahneman |
| **Il regno di Logistilla** | il regno verso cui Ruggiero deve dirigersi | metodo, misura, verità | Popper, Curie, Gianotti, Doudna |
| **La luna** | il luogo in cui le cose perdute dagli uomini sono raccolte | **ciò che gli uomini hanno perso** | Kant, Marx, Freud, Oppenheimer, Ciolkovskij, Korolëv, Johnson, Armstrong |
| **La valle del Senno** | valle sulla luna, dove Orlando ritrova la ragione | la ragione perduta e recuperata | **Kahneman, Tversky** |
| **L'ippogrifo** | il cavallo alato | il desiderio di superare il limite naturale | Lilienthal, i fratelli Wright, Earhart, Gagarin |

*(nota tecnica)* **L'ippogrifo non è un luogo**: è un emblema. Va nella scheda di Ariosto come `emblema`, non nella tabella dei luoghi. La distinzione conta, perché un emblema non ha coordinate e non si può raggiungere.

*(nota tecnica)* **I luoghi fantastici non hanno coordinate.** Non vanno in `sorgenti/gis/` e non si possono selezionare con il mouse: il gioco li disegna a mano sulla carta, con un segno proprio, e **dichiara al giocatore che non sono reali**. È l'unica eccezione alla regola dei pin e va scritta in `AGENTS.md`.

### 4.4 Il catalogo dei luoghi del quinto anno

*(da Pietro, verificato dove il fatto era incerto)*

| Luogo | Tipo | Chi ci sta | Legame |
|---|---|---|---|
| **Ferrara** | `B`+`A` | Ariosto, Ruggiero, Bradamante | il poema, la corte, la genesi degli Este |
| Ferrara | `S` | Bassani, Antonioni, De Pisis | `B` (ci sono nati); Eco, Calvino solo `S` o `C`, **non `B`** |
| **Parigi** | poetica | Carlo Magno, Agramante | il teatro della guerra nella prima parte |
| **Londra / Inghilterra** | storica reale | Ada Lovelace, Turing, Berners-Lee, Newton, Darwin, Woolf, Orwell, Franklin; e **Astolfo** (poetica) | |
| **Scozia** | poetica e reale | Ginevra e Ariodante (poetica); Watt, Smith, Bell (reale) | |
| **Spagna** | poetica e reale | Marsilio (poetica); Cervantes, Goya, Dalí, Picasso, Lorca, Ramón y Cajal (reale) | |
| **Africa / Biserta** | poetica | Agramante, Medoro, Rodomonte | **attenzione, v. §6.1** |
| Africa reale | storica reale | Mandela, Tutu, Nkrumah, Lumumba, Maathai, Achebe, Soyinka, Fanon, Camus, Diop | |
| **Arles** | poetica e reale | Agramante e Rodomonte (poetica); **Van Gogh** (`B`, e `A` per la Notte stellata) | dopo la sconfitta i Saraceni si ritirano ad Arles *(verificato)* |
| **Alessandria** | storica reale | Eratostene, Euclide, Tolomeo, Ipazia | Tolomeo è anche il nome di un personaggio del poema *(verificato)*: il gioco può usare la doppia porta |
| **Gerusalemme** | storica reale | Gesù, Erode, Tito, Arendt, Edward Said, Elie Wiesel | **v. §6.2, tema sensibile** |
| **Catai / Cina** | poetica e reale | Angelica (poetica); Marco Polo, Matteo Ricci, Confucio, Sun Yat-sen, Mao, Deng, Tu Youyou, Ai Weiwei (reale) | |
| **Tartaria / Mongolia** | poetica e reale | Mandricardo (poetica, **re de' Tartari**: non «imperatore di Mongolia», §3.3); Gengis Khan, Kublai, Tamerlano (reale) | |
| **Circassia / Caucaso** | poetica e reale | Sacripante (poetica); lo Caucaso reale, e da lì la catena fino all'Unione Sovietica | |
| **Nubia / Etiopia** | poetica e reale | Astolfo e Senapo (poetica); Haile Selassie, Menelik II, Tedros Adhanom (reale) | |
| **Paradiso terrestre** | fantastica `I` | Carson, Goodall, Maathai, Earle, Lovelock | |
| **Luna** | fantastica `I` e storica reale | Kant, Ciolkovskij, Goddard, Korolëv, von Braun, Johnson, Armstrong, Gagarin | due porte diverse sullo stesso segno |
| **Valle del Senno** | fantastica `I` | **Kahneman, Tversky** | la costellazione finale del capitolo |
| **Castello di Atlante** | fantastica `I` | Gebru, Buolamwini, Zuboff, Orwell, Kahneman | |
| **Isola di Alcina** | fantastica `I` | Zuboff, McLuhan, Debord, Kahneman | Jobs, Bezos e Zuckerberg **eliminati** |
| **Regno di Logistilla** | fantastica `I` | Popper, Curie, Gianotti, Doudna | |
| **Mare e oceani** | storica reale | Colombo, Magellano, Cook, Heyerdahl, Earle, Cousteau | |

### 4.5 Il problema che questa mappa pone, e come l'ho risolto

*(aggiunta — è il punto più serio di questo documento)*

Se la mappa del quinto anno fosse **interamente** la geografia del *Furioso*, i trenta personaggi dell'anno si troverebbero quasi tutti fuori posto. Fermi non è mai stato a Biserta, Popper non è mai stato ad Arles, Dijkstra non è mai stato sulla Luna: per metterli lì servirebbero legami `I`, e cioè esattamente i legamenti «ottenuti per analogia» che la regola di Pietro vieta.

La verifica lo conferma in modo netto: delle associazioni proposte per il quinto anno, quelle che **superano il test** verso un luogo del poema sono tutte verso luoghi fantastici (`I`) o verso luoghi reali con un fatto (`B`/`A`). Non ce n'è quasi nessuna verso un luogo del poema e storico insieme.

**Proposta (da decidere): il *Furioso* è l'atlante e il finale del quinto anno, non la sua mappa.**

- la **mappa** del quinto anno resta quella del documento `anno5-mondo.md`, cioè i luoghi reali e verificati dei trenta personaggi: Chicago, Vienna, Los Alamos, Broad Street, Rotterdam, Bell Labs, il CERN, Seattle;
- l'**atlante** che il giocatore costruisce durante l'anno è un **codice del poema**, e alla tappa finale il gioco lo apre: le fasce vuote del futuro (i sei strati `S90`–`S95`) diventano la **Luna**, e la prova finale di Kahneman si gioca nella **valle del Senno**;
- **chi può stare nel codice del poema** è governato dalla regola che è già scritta: `B`, `A`, `S` per i luoghi reali e `I` **solo** per i fantastici. Nessuna eccezione;
- **la stessa identica regola vale per gli atlanti degli anni 2, 3 e 4**: chi vuole stare in un luogo deve superare il test della frase.

Il vantaggio è che il quinto anno resta agganciato ai suoi livelli (metodi numerici, reti, intelligenza artificiale) senza inventare luoghi; lo svantaggio è che la Luna arriva solo alla fine. Se preferisci il contrario — **la mappa del quinto anno è il *Furioso*** — la conseguenza è concreta e va detto: le trenta tappe vanno rifondate sui luoghi del poema, e la maggior parte dei trenta personaggi esce dal percorso obbligatorio o diventa facoltativa. È la **Q1** di §8.

### 4.6 La costellazione finale, come nel progetto di Pietro

Nove nomi, non trenta, e una sola domanda:

> **che cosa significa essere capaci di giudicare in un mondo nel quale si può sbagliare, essere manipolati, interpretare male ciò che si vede, e delegare sempre più decisioni a sistemi costruiti da altri?**

Orlando (ha perso il senno), Astolfo (va a cercarlo), Kahneman e Tversky (errori sistematici), Orwell (la realtà manipolata), Arendt (la responsabilità), Popper (la critica), Eco (l'interpretazione), Gebru (i limiti dei sistemi).

*(proposta)* Questa costellazione è **l'ultima tappa del gioco** e l'unica in cui compaiono più di due voci insieme. Va costruita per prima, perché se non funziona il gioco non finisce.

---

## 5. Come si registra tutto questo nei dati

### 5.1 Lo schema

`dati/videogioco-5-duchi-luoghi.json`: un record per associazione.

| Campo | Che cosa contiene |
|---|---|
| `anno` | `1`, `2`, `3`, `4`, `5` |
| `personaggio` | il nome, o il collettivo |
| `luogo` | il nome del luogo, **esatto** (comune, frazione, palazzo) |
| `tipo` | `B`, `A`, `S`, `I`, `C` |
| `pin` | `true` se è il pin della tappa, `false` altrimenti |
| `porta` | se il luogo non è percorribile, da quale porta entra |
| `altri_luoghi` | lista di `{luogo, tipo}` per le associazioni multiple |
| `nota` | una frase: perché quell'associazione e non un'altra |
| `attendibilita` | la scala già in uso: `D`, `I`, `M`, `L`, `F`, `C` |
| `fonte` | dove il fatto è documentato |

### 5.2 Il vincolo dei pin

**Un solo pin per tappa, in tutti e cinque gli anni.** Le associazioni multiple finiscono in `altri_luoghi`. Il numero massimo di pin per anno è **il numero di tappe**: 30 all'anno. Tutto il resto è catalogo.

*(proposta — da discutere)* Un **tetto di 60–70 pin per anno** come obiettivo di progetto: meno di quanti sono i luoghi potenzialmente percorribili, il giocatore non raggiunge la metà della mappa, e il gioco perde il senso del viaggio. È la versione numerica della regola «meglio 60 associazioni solidissime che 150 per analogia».

### 5.3 I dati geografici

- **luoghi reali**: coordinate WGS84 in `sorgenti/gis/`, come già previsto da `AGENTS.md` §4 e `motore-e-grafica.md`;
- **luoghi fantastici**: **nessuna coordinata**. Vanno disegnati a mano sulla carta del gioco, con un segno dedicato, e il gioco dichiara che non esistono. È l'unica eccezione e va scritta in `AGENTS.md`;
- **luoghi inesistenti per errore** (l'esempio è «Iran orientale»): non entrano nel catalogo finché non esiste un toponimo reale.

---

## 6. Temi sensibili, e due che il quinto anno rende espliciti

*(coerente con `anno1-ferrara.md` §8 e con i documenti degli anni 2-5)*

### 6.1 Il problema più serio: l'Africa del *Furioso* è il campo nemico

*(aggiunta — questa la metto per prima perché è la più importante)*

Nel poema **Agramante è il re saraceno d'Africa** ed è «il più grande nemico dei cristiani» *(verificato)*. La campagna africana di Astolfo è, nella struttura del romanzo, una **spedizione contro l'Africa**.

Ora, nello stesso capitolo del catalogo, all'Africa si collegano **Mandela, Tutu, Nkrumah, Lumumba, Maathai, Achebe, Soyinka, Fanon, Diop**: cioè la costruzione politica africana e il pensiero anticoloniale.

Il gioco **non può mettere le due cose una accanto all'altra senza dirlo**, e non può nemmeno far finta che il primo sia una descrizione e il secondo una versione. La regola che propongo è questa:

1. la campagna africana del poema è **una costruzione letteraria**, e il gioco lo dice alla prima occasizione, senza chiedere scusa;
2. il passaggio all'Africa reale **deve passare per almeno una voce africana che parli di quella costruzione**: Fanon e Diop esistono per questo, e la loro scheda è lunga come le altre;
3. **non si usa mai** il nome «saraceno» come etichetta di un popolo reale: nel gioco la parola esiste solo come voce dei personaggi del poema, e ogni volta che compare il gioco spiega chi la usa e con quale intento;
4. nessun personaggio del gioco deve «vincere» la guerra contro Agramante e uscirne con la morale di chi ha vinto: il poema finisce con un matrimonio e con una pace, e questa è la parte che il gioco deve raccontare.

### 6.2 Gerusalemme

Gerusalemme è l'unico luogo della lista che è **contemporaneamente sacro per tre religioni e conteso**. Le tre regole del progetto valgono:

- **nessuna tappa giocabile dentro le mura della Città Vecchia**, e nessun ritratto di luogo di culto;
- i personaggi che ci arrivano **per ragioni politiche** (Erode, Tito) sono distinti da quelli che ci arrivano **per ragioni religiose** (Gesù), e il gioco non li mette nella stessa scena;
- **la tappa su Gerusalemme è una tappa di fonti**: il giocatore vede la stessa città descritta da tre fonti che non si somigliano, e la domanda è perché.

### 6.3 Le altre regole che il quinto anno rende attive

| Tema | Dove | Regola |
|---|---|---|
| **Le donne del poema** | tutto il capitolo 5 | Angelica, Bradamante, Marfisa, Alcina, Melissa sono ** protagoniste**, non premi: il gioco non usa Alcina come semplice «la seduttrice» e non usa Melissa come semplice «colei che salva». La domanda sull'isola di Alcina è sul consenso estorto, ed è la stessa domanda che il capitolo 5 pone alle piattaforme |
| **Profezia e destino** | tutto | il *Furioso* è un romanzo che sa già come va a finire. Il gioco deve sfruttare questa cosa: **l'oracolo esiste**, e questo è un ottimo caso didattico per distinguere «che cosa è scritto in un testo» da «che cosa è vero» |
| **La scrittura e la circolazione** | 4-23, 4-25 | le edizioni del 1516, 1521, 1532 sono già nel terzo anno: il quinto anno non le ripete, usa il *Furioso* come **corpus** |
| **Persone vive** | 5-11, 5-15, 5-16, 5-17, 5-23, 5-26…5-29 | regole decise il 01/10/2026: solo emblema, scheda «in formazione», nessuna affermazione di correttezza |

---

## 7. Verifiche

*(le verifiche già fatte il 01/10/2026 sono segnate con ✓; le altre sono da fare)*

| # | Voce | Che cosa è stato verificato, e che cosa resta |
|---|---|---|
| **V1** | Sacagawea → Missouri | ✓ **errore**: nascita nel Lemhi Valley (Idaho), 1788-90; la spedizione la incontra a Fort Mandan (Dakota del Nord). Correzione da applicare a `anno4-mondo.md` se quel nome compare |
| **V2** | Mandricardo «imperatore di Mongolia» | ✓ **errore**: nel poema è re de' Tartari, figlio di Agramante. La formula «imperatore di Mongolia» non è stata trovata in fonte |
| **V3** | Ruggiero e Bradamante antenati degli Este | ✓ **confermato**: Britannica e Treccani; è la genesi che il romanzo stesso dichiara |
| **V4** | Agramante re di Biserta, nemico dei cristiani | ✓ **confermato**: «Agramante of Biserta», re saraceno d'Africa, guerra con Carlo Magno; assedio di Biserta alla fine |
| **V5** | Il passaggio del centro della guerra da Parigi ad Arles | ✓ **confermato** per Arles come base di Agramante dopo le sconfitte; la formula «cambio di centro geografico della guerra» va verificata sul testo dei canti |
| **V6** | Astolfo figlio del re d'Inghilterra | ✓ **confermato**: «paladino e figlio d'Ottone re d'Inghilterra» |
| **V7** | Marconi → Bologna | ✓ **confermato** che i primi esperimenti sono a Pontecchio (Villa Griffone), 1895: il nome del luogo va corretto |
| **V8** | Parola del libro: «mantricardo re de' Tartari e imperatore di Mongolia» | **da verificare** sulla fonte citata (l'atlante del *Furioso*): può essere un refuso dell'atlante |
| **V9** | La parentela di Agramante | **da verificare**: alcune liste lo danno «padre di Bradamante», che è quasi certamente errato. Il gioco non deve dirla finché non è verificata |
| **V10** | Caravaggio alla Pinacoteca di Brera | **da verificare**: quale dipinto, e se «Milano» è `A` (l'opera) o `C` (dove è vissuto). Senza il nome del dipinto l'associazione non passa |
| **V11** | I luoghi babilonesi, il Catai, la Nubia | **da verificare** sul testo: sono i tre segmenti di viaggio più importanti e i tre più citati |
| **V12** | Sophia Loren → Pozzuoli come `C` | **da verificare** il tipo `C` come categoria generale, con altri casi (Montessori a Chiaravalle) |
| **V13** | Mansa Musa → Cairo come `A` | **da verificare** sul documento dell'Anno IV, che ha il pin su Timbuctù |
| **V14** | I buchi geografici (Brasile, Indonesia, Corea, Ungheria, Scandinavia, Balcani) | **da decidere**: sono buchi reali e vanno colmati, o dichiarati come scelta? §8 Q4 |

---

## 8. Questioni aperte

1. **La mappa del quinto anno è il *Furioso*, o il *Furioso* è l'atlante e il finale?** (§4.5). La mia proposta è la seconda: con la prima, venticinque dei trenta personaggi dell'anno perdono il loro luogo verificato. È la decisione più importante di questo documento.
2. **Il tipo `C` (luogo di crescita) entra nella scala ufficiale?** Se no, Sophia Loren va a Roma e si perde una delle lezioni più difficili del gioco.
3. **Il tetto di 60-70 pin per anno** (§5.2) è un numero che Pietro vuole fissare, o resta una proposta? Cambia il modo in cui si costruisce ogni mappa.
4. **I buchi geografici** (Brasile, Indonesia, Corea, Nuova Zelanda, Canada, Artide, Ungheria, Romania, Scandinavia, Balcani, Puglia): si colmano con nomi nuovi, o si dichiarano come scelta e il gioco li mostra come spazi vuoti? La seconda è più onesta e anche più interessante.
5. **Il collegamento De Sica → Kurosawa** (l'influenza documentata) entra nel catalogo? È l'unico caso in cui un legame fra due culture è una fonte, non un'analogia.
6. **Chi è il protagonista del quinto anno?** Se la mappa è il *Furioso*, il giocatore è dentro il romanzo (e i personaggi parlano di sé e della propria età, che è la regola degli anni 3-4); se la mappa è il mondo reale, il giocatore resta alla tavola di progetto. Sono due giochi diversi.
7. **Il quarto tipo per l'Anno III e l'Anno IV.** Nell'Anno III c'è il posto di un luogo interpretativo (nessuno: l'Anno III non ha luoghi fantastici, e va bene così). Nell'Anno IV il posto c'è: che cosa vi mettiamo? Proposta: il **Parlamento dei popoli**? No: **nessun luogo interpretativo negli anni 2-4**, e tutti i legami interpretativi restano nella Tavola del Cinquecento (5-12, Borges).

---

## 9. Cosa c'è da fare

1. **Decidere Q1** (la mappa del quinto anno). Tutto il resto del capitolo 5 dipende da questa scelta.
2. **Applicare le correzioni del §3** agli elenchi degli anni 2, 3 e 4, e in particolare correggere **il pin di Mansa Musa** in `anno4-mondo.md` (v. V13).
3. **Verificare V10** (il dipinto di Caravaggio a Brera) e **V9** (la parentela di Agramante): sono le due che, se sbagliate, fanno scrivere al gioco una frase falsa.
4. **Colmare i buchi geografici** o dichiararli (§8 Q4): la scelta va fatta per anno, non per nome.
5. **Generare `dati/videogioco-5-duchi-luoghi.json`** con lo schema di §5.1, cominciando dall'Anno II, che è l'unico con una mappa già costruita e verificata.
6. **Aggiornare `AGENTS.md`** con: i cinque tipi di legame, il vincolo del pin unico, e l'eccezione dei luoghi fantastici (nessuna coordinata).
7. **La costellazione finale del §4.6**: nove voci e una domanda. Va prototipata prima di tutto il resto, perché è la fine del gioco.

---

## 10. Registro modifiche

- **v0.1 (01/10/2026)**: prima stesione. Documento trasversale, valido per i cinque anni:
  - i **quattro tipi di legame** fra persona e luogo (`B` biografico, `A` dell'azione, `S` simbolico, `I` interpretativo) con la prova da superare per ciascuno, e la regola che separa `S` da `I` (`I` vale solo per i luoghi che non esistono);
  - il **quinto tipo** `C`, luogo di crescita, necessario per casi come Sophia Loren a Pozzuoli;
  - il **test della frase**, il **test dell'eliminazione** in tre domande, e la regola «se il luogo è sostituibile, non è un luogo»;
  - il **vincolo del pin unico** per tappa, con le associazioni multiple in `altri_luoghi`;
  - il **catalogo verificato** degli anni 2, 3 e 4: quattordici correzioni e dodici buchi geografici, con i tre errori documentati (Sacagawea, Mandricardo, Marconi);
  - il **catalogo verificato dei luoghi dell'*Orlando furioso***, con i fatti del poema controllati (Ruggiero e Bradamante antenati degli Este; Agramante re di Biserta; Astolfo figlio di Ottone re d'Inghilterra; il ritiro ad Arles);
  - il **problema dell'Africa del poema**, che è il tema più serio del quinto anno, con quattro regole di conduzione;
  - lo **schema dei dati** e la regola di eccezione per i luoghi fantastici;
  - **quattordici verifiche**, di cui sette già fatte, e **sette questioni aperte**, la prima delle quali è la scelta fra «mappa = *Furioso*» e «*Furioso* = atlante e finale».
