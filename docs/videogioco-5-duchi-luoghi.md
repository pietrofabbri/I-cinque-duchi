---
titolo: Videogioco "I cinque duchi" — La regola dei luoghi: i tipi di legame fra personaggio e luogo, catalogo per anno e mappa del quinto anno
versione: 0.3
data: 2026-10-02
autore: Pietro Fabbri (con Claude)
revisioni: v0.1 (prima stesione del 01/10/2026); v0.2 (controllo di coerenza del 02/10/2026: rimandi di versione, Q1 dichiarata risolta ma non ratificata, «l'aria sopra la foresta» dichiarata aperta); v0.3 (le sedici decisioni di Pietro del 02/10/2026: la regola dei due strati entra in §4.5, il tipo `C` nella scala ufficiale, il tipo `N` dei non luoghi in §4.3, V8 V9 V10 fatte, i buchi geografici affidati ai facoltativi, il tetto dei pin riscritto, e l'Africa riscritta sulla parola del testo)
fonte del materiale: le liste di associazioni personaggio–luogo per gli anni 2, 3 e 4 e la revisione delle associazioni con i luoghi dell'Orlando furioso per il quinto anno, proposte da Pietro (01/10/2026), con i criteri di tre e quattro tipi di legame e l'elenco delle associazioni da eliminare
dati: videogioco-5-duchi-luoghi.json (da generare, v0.1: un record per associazione, con anno, personaggio, luogo, tipo di legame, pin o porta, nota, attendibilità); dati/luoghi_gioco.json (95 luoghi e il blocco `tappe` con i trenta binomi pin/stanza del quinto anno, generato da sorgenti/furioso/costruisci_citazioni.py --luoghi)
controllo: python3 sorgenti/furioso/verifica_citazioni.py (controlla anche i legami I/N e il blocco `tappe`: verifiche F13, F14, F15); python3 sorgenti/verifica_coerenza.py (versioni, file citati, cifre dichiarate, tappe e personaggi)
documenti collegati: videogioco-5-duchi-schema-livelli.md (v1.1), videogioco-5-duchi-anno5-mondo.md (v0.4), videogioco-5-duchi-anno4-mondo.md (v0.5), videogioco-5-duchi-anno3-europa.md (v0.4), videogioco-5-duchi-anno2-penisola.md (v0.2), videogioco-5-duchi-anno1-ferrara.md (v0.3), videogioco-5-duchi-anno1-mappa.md (v0.9), videogioco-5-duchi-furioso.md (v0.4), videogioco-5-duchi-motore-e-grafica.md (v0.1), AGENTS.md
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
4. la **mappa del quinto anno**, che è quella delle persone reali e verificate dei trenta personaggi, con la geografia dell'*Orlando furioso* nelle **stanze** delle trenta tappe (§4, e §4.5 per la regola dei due strati).

*(aggiunta)* C'è un quinto tipo, che non era nella lista di Pietro ma che il catalogo rende necessario: il **luogo di crescita**. Se ne parla in §1.5.

*(aggiunta, 02/10/2026)* Nel quinto anno c'è anche un **sesto codice, `N`**, che non è un tipo di legame fra persona e luogo ma il tipo della **stanza**: serve alle stanze dei filoni che non sono né un luogo reale né un luogo inesistente (§4.3). La scala dei legami persona–luogo resta `B/A/S/I/C`; `N` si aggiunge solo alle stanze.

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

*(nota)* Nel documento i codici sono `B`, `A`, `S`, `I` e `C` (crescita, §1.5). Il `C` **non** collide con l'`C` della scala di attendibilità (`collettivo`): sono due campi diversi e non vengono mai scritti nello stesso campo. Alle **stanze** si aggiunge `N` (non luogo, §4.3), che non è un sesto tipo di legame persona–luogo: è il tipo di ciò che non è un luogo.

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

*(ratificato da Pietro il 02/10/2026: «A favore: tiene Sophia Loren dov'è cresciuta e salva una delle lezioni più difficili del gioco».)* Il tipo `C` è **nella scala ufficiale**. Si usa **una volta sola per personaggio**, e il gioco lo dichiara: «questa persona è cresciuta in un luogo che le ha lasciato qualcosa che non compare nei libri di storia». È anche il tipo che rende il gioco meno noioso, perché spiega perché certe persone hanno un accento e altre no.

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
| Akira Kurosawa → Spagna | **eliminare** | **concordo**, e annoto il fatto vero che il catalogo deve poter usare: Kurosawa ha detto che la **cineasta italiana** gli ha insegnato a filmare (*I Vitelloni*, di Vittorio De Sica). È un'influenza documentata fra due culture, e sarebbe un bellissimo `A` — ma non è un legame con la Spagna. La sua direzione è **De Sica → Kurosawa** |
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
| 5 | Caravaggio → Milano, Pinacoteca di Brera | **fatto (V10)** | Caravaggio è nato a Caravaggio (MI): il legame con Milano è **l'opera**, quindi `A`, e il dipinto c'è: è la **Cena in Emmaus**, 1606, olio su tela 141 × 175 cm, dipinta a Palestrina o a Zagarolo per il marchese Patrizi, identificata nel 1912 nella Collezione Patrizi e alla Brera dal 1939, dono dell'Associazione «Amici di Brera». Il nome del dipinto non è un dettaglio: senza il nome l'associazione non supera il test della frase, e con il nome diventa l'insegnamento migliore del caso — *è il momento in cui i discepoli riconoscono da un pezzo di pane spezzato che hanno davanti la persona giusta, e non lo sanno prima*: un segnale povero che significa tutto, che è la definizione buona di un dato |
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
| **L'aria sopra la foresta** *(dal 02/10/2026)* | non è un luogo: è l'aria che Astolfo attraversa sopra la foresta | **non luogo**: esistono cose che non sono né qui né altrove | nessuno: è il tipo `N`, non il tipo `I` |

*(nota, decisione di Pietro del 02/10/2026)* **«L'aria sopra la foresta» ha il tipo `N`, non `I`.** Il testo non nega che l'aria esista — nega che sia un luogo. «Un luogo inesistente» è un'immagine: ci si può ragionare. «Un non luogo» è una condizione: **la si attraversa, e mentre la si attraversa non si è da nessuna parte**. La distinzione non è una sfumatura, perché è la distinzione fra *non esiste* e *non è una cosa di cui si possa dire dove sia*, ed è una domanda che il quinto anno deve poter fare: dove sta un dato che sta solo in memoria? dove sta una promessa che non è ancora scaduta? Come `I`, `N` non ha coordinate e va dichiarato — in un elenco separato (`non_luoghi` in `citazioni.json`), perché se i due elenchi si mescolassero il tipo `N` non significherebbe niente.

*(nota tecnica)* **L'ippogrifo non è un luogo**: è un emblema. Va nella scheda di Ariosto come `emblema`, non nella tabella dei luoghi. La distinzione conta, perché un emblema non ha coordinate e non si può raggiungere.

*(nota tecnica)* **I luoghi fantastici non hanno coordinate.** Non vanno in `sorgenti/gis/` e non si possono selezionare con il mouse: il gioco li disegna a mano sulla carta, con un segno proprio, e **dichiara al giocatore che non sono reali**. È l'unica eccezione alla regola dei pin e va scritta in `AGENTS.md`.

*(aggiunta, 02/10/2026 — chiusa)* **Questa tabella è ora l'elenco completo.** `videogioco-5-duchi-furioso.md` v0.3 aveva introdotto un sesto nome con legame `I` che qui non c'era, **«l'aria sopra la foresta»**, che è la stanza della tappa 5-8. La domanda era se fosse un luogo che non esiste o una condizione che quindi non è un luogo: **la decisione di Pietro è che è un non luogo**, ed è nato il tipo `N` (§4.3 e `furioso.md` §4.9). Da qui l'elenco ha sei righe, di cui quattro `I` e una `N`, più l'ippogrifo che è un emblema e non un luogo.

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

### 4.5 Il problema che questa mappa pone, e la sua soluzione: due strati

*(aggiunta il 01/10/2026, riscritta e **ratificata** il 02/10/2026 — è il punto più serio di questo documento)*

Se la mappa del quinto anno fosse **interamente** la geografia del *Furioso*, i trenta personaggi dell'anno si troverebbero quasi tutti fuori posto. Fermi non è mai stato a Biserta, Popper non è mai stato ad Arles, Dijkstra non è mai stato sulla Luna: per metterli lì servirebbero legami `I`, e cioè esattamente i legamenti «ottenuti per analogia» che la regola di Pietro vieta.

La verifica lo conferma in modo netto: delle associazioni proposte per il quinto anno, quelle che **superano il test** verso un luogo del poema sono tutte verso luoghi fantastici (`I`) o verso luoghi reali con un fatto (`B`/`A`). Non ce n'è quasi nessuna verso un luogo del poema e storico insieme.

**La soluzione: due strati, un solo pin.** Non «mappa *Furioso*» né «atlante e finale»: nessuna delle due, perché entrambe sacrificavano qualcosa che il progetto non può sacrificare.

> **Il `pin` — il luogo dove il gioco si ferma — resta il luogo reale e verificato del personaggio. La `stanza` — lo spazio che il giocatore attraversa — è quella del filone, e può essere un luogo che non esiste (`I`) o che non è un luogo (`N`).**

Le tre conseguenze, che sono le regole del gioco:

1. **un solo pin per tappa**, in tutti e cinque gli anni: nessuna tappa ha due luoghi sulla mappa;
2. **nessun legame analogico verso un luogo reale**: se il filone è ambientato in un luogo reale, il legame dichiara *che cosa è successo lì* (`A`) o *che cosa quel luogo spiega* (`S`); se il luogo non esiste, il legame è `I`; se non è un luogo, è `N`;
3. **il giocatore sa sempre in che mondo è**: la scheda della tappa porta tre righe — il pin (dove siamo oggi), il filone (di chi è questa storia), il luogo della stanza (dove sta accadendo). Le prime due sono vere; la terza può essere una favola, e lo dichiara.

**Che cosa si guadagna e che cosa si perde, detto chiaramente.** Si guadagna il *Furioso* **in tutto l'anno** e non solo alla fine: la Luna non arrende al livello 5-4 e sparisce, e la Luna è già la stanza di un livello sui metodi numerici. Si perde la promessa che **Fermi entri sulla Luna**, che era una buona promessa. Ma il costo dell'alternativa era il progetto intero: trenta personaggi fuori percorso obbligatorio, trenta legami analogici che la regola vieta, e una mappa che non sa più dire a un ragazzo di Chicago perché ci sta andando. **Il gioco deve poter essere spiegato in una frase**, e questa si spiega in una frase sola.

**Come è fatto nei dati.** `dati/luoghi_gioco.json` porta un blocco `tappe` — trenta record, uno per tappa del quinto anno — in cui il `pin` è **derivato** dai luoghi che già dichiarano le tappe che usano (non riscritto: due verità sullo stesso fatto sono il difetto che questo progetto cerca) e la `stanza` viene dai dati delle citazioni, che sono la fonte unica anche loro. Due controlli automatici, **F14** e **F15**, verificano che una stanza `I` o `N` non abbia coordinate e che `pin` e `stanza` ci siano per tutte e trenta le tappe e combacino con la citazione.

**La stessa identica regola vale per gli atlanti degli anni 2, 3 e 4**: chi vuole stare in un luogo deve superare il test della frase, e nessuno dei tre anni ha stanze del *Furioso* (decisione di Pietro, 02/10/2026).

### 4.6 La costellazione finale, come nel progetto di Pietro

---

### 4.7 I buchi geografici non sono vuoti: sono facoltativi

*(decisione di Pietro, 02/10/2026: «dobbiamo includere un po' tutto, lo facciamo con i facoltativi che si possono far spostare il protagonista anche continentalmente in un livello: basta giustificarlo correttamente».)*

Undici nomi che mancavano dal catalogo degli anni 2, 3 e 4 erano la **Q4** di §8, e la risposta non è «colmateli» né «dichiarali vuoti». La risposta è: **un buco geografico è una stanza che non è ancora stata scritta, e la si scrive come facoltativa**.

**La regola, che vale per tutti e cinque gli anni:**

> **Una facoltativa può portare il protagonista fuori dal continente, e in quel caso lo dichiara.** Un facoltativo che sposta il giocatore in un altro continente senza spiegarlo è un teletrasporto, cioè la stessa cosa che il progetto chiama «stima sbagliata»: il giocatore accetta una posizione che nessun dato sostiene. Un facoltativo che lo sposta **e dice perché** — perché il livello è su una rete che quel continente attraversa, o perché l'informazione di quel livello è nata là — è invece il caso migliore del capitolo, perché obbliga a ragionare su una scala più grande di quella dello schermo.

La tabella dei tredici buchi, uno per facoltativa. La colonna «perché è qui» è la parte che passa il test della frase (§1.3); la colonna «che cosa resta da verificare» è la parte onesta.

| Buco | Anno | Facoltativa proposta | Perché è qui (la frase) | Che cosa resta |
|---|---|---|---|---|
| **Brasile** | IV | **Irineu Evangelista de Sousa, detto Mauá** (Iraty, 1854) | costruì la prima ferrovia del Brasile: l'infrastruttura come rete, che è l'argomento del capitolo | data esatta del tracciato; il nome «Mauá» nei cataloghi |
| **Corea** | V | una **situazione**: «uno stabilimento di semiconduttori, Corea del Sud, anni 1980» | il livello è su reti e computo: chi fabbrica i pezzi non è il paese che li usa | coordinate e nome dello stabilimento, quando verranno verificati |
| **Indonesia** | IV | **B. J. Habibie** | ingegnere aeronautico e presidente: la competenza che costruisce, e il posto dove la competenza viene da un continente che l'Europa non conosce | il legame esatto con uno dei 30 livelli |
| **Nuova Zelanda** | IV | **Ernest Rutherford** | la prima trasmutazione nucleare artificiale (1919): un esperimento che cambia la natura della cosa misurata | il pin esatto (il luogo del 1919 è in India: va dichiarato, non nascosto) |
| **Canada** | IV | **James Gosling** (nato a Calgary) | il designer di Java: un uomo che ha scritto una lingua che gira su milioni di macchine in tutto il mondo, e il posto da cui è partito | biografia e data, `FONTI-E-LICENZE.md` |
| **Artide** | IV | **nessuna persona: una situazione**, «una stazione di osservazione dell'Artide» | l'Artide è il luogo senza dati scritti: il gioco lo mostra come uno spazio bianco, come i sei strati del quinto anno | le coordinate, che **non sono facoltative**: restano bianche |
| **Ungheria** | III | **John von Neumann** (Budapest) | l'algoritmo che cerca un cammino e l'architettura della macchina: il luogo della ricerca informatica più importante del Novecento, in un'Europa che non è l'Europa occidentale | il livello che la apre (3-6, ricerca binaria, è il più adatto) |
| **Romania** | III | **Henri Coandă** | l'ingegnere che ha costruito il primo aereo a reazione: l'Europa orientale non è una nota a margine, è un laboratorio | il livello che la apre |
| **Scandinavia** | III | **Torben Rask e la prima tabella ASCII** (Danimarca, 1963) | una tabella che assegna un numero a ogni carattere: una **ricerca in tabella**, che è il livello 3-6 | il luogo esatto in Danimarca |
| **Balcani** | III | **Vuk Karadžić** (Trnovo, oggi Belgrado) | un testo che porta dentro di sé la propria struttura: è la definizione di un linguaggio di markup, e Balkano è dove l'alfabeto è stato rifatto | il livello che la apre (3-22, XML, è il più adatto) |
| **Puglia** | II | una **situazione**: «la costa adriatica pugliese, i cavi sottomarini» | il livello è su reti e trasmissione: la Puglia è dove una rotta di cavi attraversa il mare, e il gioco lo dice come percorso, non come città | il tracciato e la data, che sono da verificare |

*(nota)* **La colonna «che cosa resta» è deliberatamente piena.** Undici facoltative su tredici non hanno ancora una fonte controllata, e il gioco non le userà finché non l'hanno. Il catalogo le contiene come **proposte**, non come schede: la differenza è la stessa che c'è fra «abbiamo verificato» e «crediamo che sia», e in questo progetto le due parole non si scambiano.

Nove nomi, non trenta, e una sola domanda:

> **che cosa significa essere capaci di giudicare in un mondo nel quale si può sbagliare, essere manipolati, interpretare male ciò che si vede, e delegare sempre più decisioni a sistemi costruiti da altri?**

Orlando (ha perso il senno), Astolfo (va a cercarlo), Kahneman e Tversky (errori sistematici), Orwell (la realtà manipolata), Arendt (la responsabilità), Popper (la critica), Eco (l'interpretazione), Gebru (i limiti dei sistemi).

*(proposta)* Questa costellazione è **l'ultima tappa del gioco** e l'unica in cui compaiono più di due voci insieme. Va costruita per prima, perché se non funziona il gioco non finisce.


## 5. Come si registra tutto questo nei dati

### 5.1 Lo schema

`dati/videogioco-5-duchi-luoghi.json` (**da generare**): un record per associazione.

| Campo | Che cosa contiene |
|---|---|
| `anno` | `1`, `2`, `3`, `4`, `5` |
| `personaggio` | il nome, o il collettivo |
| `luogo` | il nome del luogo, **esatto** (comune, frazione, palazzo) |
| `tipo` | `B`, `A`, `S`, `I`, `C` (`N` solo per le stanze, §4.3) |
| `pin` | `true` se è il pin della tappa, `false` altrimenti. **Il pin è il luogo dove il gioco si ferma**: uno per tappa, e più tappe possono fermarsi nello stesso posto (ritorno) |
| `porta` | se il luogo non è percorribile, da quale porta entra |
| `altri_luoghi` | lista di `{luogo, tipo}` per le associazioni multiple |
| `nota` | una frase: perché quell'associazione e non un'altra |
| `attendibilita` | la scala già in uso: `D`, `I`, `M`, `L`, `F`, `C` |
| `fonte` | dove il fatto è documentato |

### 5.2 Il vincolo dei pin

**Che cosa sono i pin, in una frase.** Un **pin** è il luogo in cui il gioco si **ferma**: quello su cui il giocatore può posare il dito e dire «sono qui». Il progetto ne ammette **uno per tappa**, e i trenta pin di un anno sono dunque trenta. Ma più tappe possono fermarsi nello stesso posto — Londra è il pin di 5-3, 5-7 e 5-19 — e in quel caso il posto è uno solo e i pin sono tre: è un **ritorno**, non una contraddizione. Nei dati (`dati/luoghi_gioco.json`) il campo `pin` di ciascun luogo è esattamente questo: **quante tappe si fermano lì**, e la somma su tutti i luoghi dà il numero delle tappe del gioco.

*La parola viene dalla cartografia dei programmi e qui ha due sensi, di cui solo uno è il suo: il pin è una **tappa**, non un indirizzo. Il pin è «dove il gioco si ferma», l'indirizzo è «dove si trova quella cosa». Sono due righe diverse, ed è per questo che la regola dei due strati ne fa due campi.*

**Un solo pin per tappa, in tutti e cinque gli anni.** Le associazioni multiple finiscono in `altri_luoghi`. Il numero massimo di pin per anno è **il numero di tappe**: 30 all'anno. Tutto il resto è catalogo.

**Il vecchio tetto di 60–70 pin era sbagliato, e i dati lo dimostrano.** Era una proposta per impedire che la mappa si riempisse di luoghi analogici, cioè per evitare un rischio che **non si è verificato**: i dati hanno 95 luoghi e 120 tappe in tutto il gioco, e per anno i pin-tappe sono 37 (anno II), 46 (anno III), 36 (anno IV), 30 (anno V). Un tetto di 60–70 non vincolerebbe niente: il massimo reale è 46, cioè due terzi del tetto. La versione numerica giusta della regola «meglio 60 associazioni solidissime che 150 per analogia» non è un tetto di pin, è **un tetto di luoghi distinti**: la mappa di un anno deve avere abbastanza posti diversi da non sembrare un corridoio, e i dati dicono che ne ha 21, 26, 30 e 27 — che è la cifra giusta, non quella che il tetto propose.

Quindi: **la Q3 è chiusa come «non era una domanda»**, e la regola che resta è quella che i dati già applicano da soli — trenta pin all'anno, uno per tappa, e i luoghi distinti il più possibile.

### 5.3 I dati geografici

- **luoghi reali**: coordinate WGS84 in `sorgenti/gis/`, come già previsto da `AGENTS.md` §4 e `motore-e-grafica.md`;
- **luoghi fantastici e non luoghi**: **nessuna coordinata**, e nessuna nel blocco `tappe` (verifica **F14**, automatica). Vanno disegnati a mano sulla carta del gioco, con un segno dedicato, e il gioco dichiara che non esistono — o che non sono luoghi. È l'unica eccezione e va scritta in `AGENTS.md`;
- **luoghi inesistenti per errore** (l'esempio è «Iran orientale»): non entrano nel catalogo finché non esiste un toponimo reale.

---

## 6. Temi sensibili, e due che il quinto anno rende espliciti

*(coerente con `anno1-ferrara.md` §8 e con i documenti degli anni 2-5)*

### 6.1 Il problema più serio: l'Africa del *Furioso* è il campo nemico

*(aggiunta il 01/10/2026; **riscritta il 02/10/2026** per decisione di Pietro: «va bene, riscriviamola in modo filologicamente accurato e rispettoso». Il testo è la fonte; dove il testo parla, si cita il testo, e dove il testo non parla, il gioco non parla al suo posto.)*

**Che cosa dice il testo, parola per parola.** Il *Furioso* non chiama quasi mai «Africa» il nemico: chiama **«i Mori»**, e li chiama anche **«i pagani»** e **«l'ospite saracin»**. «Africa» compare invece come **terra**, all'inizio del canto I, quando il poeta annuncia di voler cantare «l'ire e i giovenil furori / d'Agramante lor re» e la «morte di Troiano»: sono **i fatti di Agramante**, non un nome di popolo. Le formule che il testo usa davvero sono tre, e vanno citate:

- **c. I,9** — «degli infideli piú copia uccidessi»: il nemico è **un numero**, ed è il numero che il re promette come premio (è la citazione della tappa 5-22);
- **c. I,2** — «in fuga andò la gente battezzata»: l'unico fatto di questo genere che il testo racconta così è una **fuga**, non una vittoria;
- **c. XVI,29** — «se di fuor Agramante avesse astretto […] i barbari assalire»: e qui «barbari» è detto **da un personaggio**, non dalla voce del poeta.

Tre conseguenze, che sono la sostanza della riscrittura:

1. **la campagna africana del poema è una costruzione letteraria, e il gioco lo dice alla prima occorrenza**, senza chiedere scusa e senza chiedere il permesso a nessuno. Non è una descrizione di un continente: è il modo in cui un libro del 1516 immagina una guerra, e tutta la differenza è la lezione;
2. **non si usa mai** «saraceno», «Moro» o «pagano» come etichetta di un popolo reale: nel gioco la parola esiste solo come voce dei personaggi del poema, e ogni volta che compare il gioco spiega **chi la usa e con quale intento** — che è la domanda giusta, e l'unica che non sia razzista;
3. **nessun personaggio del gioco deve «vincere» la guerra e uscirne con la morale di chi ha vinto**: il poema finisce con un matrimonio e con una pace, e quella è la parte che il gioco deve raccontare.

**Il passaggio all'Africa reale deve passare per almeno una voce africana che parli di quella costruzione.** Fanon e Diop esistono per questo, e la loro scheda è lunga come le altre: non sono la voce neutra che arbitra, sono due intellettuali che hanno scritto del mondo in cui vivono, e il gioco li mette accanto al poema **per contrasto**, non per conferma.

**Che cosa il gioco non farà, dichiarato in anticipo.** Non dirà che «anche oggi è come nel poema», e non farà parlare Agramante come se fosse un politico contemporaneo. La frase che chiude il capitolo è una sola, ed è già sulla targa della tappa 5-20: **l'avversario di cui parla il poema non è sempre l'estraneo, e la minaccia di cui Rinaldo avverte è quella che viene da una parte che credevamo sicura.**

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
| **V8** | Parola del libro: «mandricardo re de' Tartari e imperatore di Mongolia» | **✓ risolto (02/10/2026)**: il testo del *Furioso* dice **Agrican**, padre di Mandricardo (c. XII,30: «figlio e successore in Tartaria del re Agrican gagliardo»), e **mai** «imperatore di Mongolia». La formula «imperatore di Mongolia» è del materiale di Pietro, non del poema: si scrive «re de' Tartari» e si dichiara che è la parola del testo |
| **V9** | La parentela di Agramante | **✓ risolto (02/10/2026)**: **Agramante è figlio di Troiano**, e la sua genealogia è tuttawarsimile a quella di Bradamante — il gioco non deve dirla finché non è verificata. Sul testo: Troiano è il padre di Agramante (c. I,1: «di vendicar la morte di Troiano»); Agolante è suo parente, con i figli **Almonte** e **Galaciella**, e **Ruggiero II** scontra Agolante; **Marfisa** è figlia di Agolante. «Padre di Bradamante» è **errato**: Bradamante è figlia di Ruggiero (c. XXIII). **La regola per il gioco: nessuna parentela si scrive senza il canto che la dice** |
| **V10** | Caravaggio alla Pinacoteca di Brera | **✓ risolto (02/10/2026)**: il dipinto è la **Cena in Emmaus**, 1606, olio su tela 141 × 175 cm, dipinta a Palestrina o a Zagarolo per il marchese Patrizi; identificata nel 1912 nella Collezione Patrizi, alla Brera dal **1939**, dono dell'Associazione «Amici di Brera». Il legame con Milano è `A` (l'opera): Caravaggio è nato a Caravaggio (MI). Cfr. §3.1 voce 5 |
| **V11** | I luoghi babilonesi, il Catai, la Nubia | **da verificare** sul testo: sono i tre segmenti di viaggio più importanti e i tre più citati |
| **V12** | Sophia Loren → Pozzuoli come `C` | **✓ risolto (02/10/2026)**: il tipo `C` è **nella scala ufficiale** per decisione di Pietro (§1.5); resta da compilare il **catalogo** con gli altri casi verificabili (Montessori a Chiaravalle), che è lavoro di `dati/` e non una verifica |
| **V13** | Mansa Musa → Cairo come `A` | **✓ risolto (02/10/2026)**: il documento dell'Anno IV ha il pin su **Il Cairo** e **Timbuctù in `S`**, che è la formulazione corretta (Cairo `A`, il fatto documentato del 1324; Timbuctù `S`, la città del deserto che non è attestata come tappa) |
| **V14** | I buchi geografici (Brasile, Indonesia, Corea, Nuova Zelanda, Canada, Artide, Ungheria, Romania, Scandinavia, Balcani, Puglia) | **✓ chiuso come domanda (02/10/2026)**: non sono né da colmare né da dichiarare vuoti, ma da **affidare ai facoltativi** (§4.7). Undici buchi, undici facoltative |

---

## 8. Questioni aperte

*(aggiornato il 02/10/2026, dopo le risposte di Pietro. **Le sette questioni sono chiuse, tutte e sette.**)*

| # | questione | esito |
|---|---|---|
| 1 | La mappa è il *Furioso* o il *Furioso* è l'atlante? | **chiusa** — la regola dei due strati, ratificata (§4.5), con i dati in `dati/luoghi_gioco.json` e i controlli F14 e F15 |
| 2 | Il tipo `C` entra nella scala? | **chiusa** — entra (§1.5) |
| 3 | Il tetto di 60-70 pin | **chiusa come «non era una domanda»** — i dati hanno al massimo 46 pin-tappe in un anno, e il tetto non avrebbe vincolato niente (§5.2) |
| 4 | I buchi geografici | **chiusa** — diventano facoltative, una per buco, con la facoltativa continentale dichiarata (§4.7) |
| 5 | De Sica → Kurosawa | **chiusa** — entra, e la sua direzione è **Decisca → Kurosawa**: un'influenza documentata fra due culture è una fonte, non un'analogia (§2.1) |
| 6 | Chi è il protagonista del quinto anno? | **chiusa** — è **dentro** il *Furioso*, e i personaggi parlano di sé e della propria età come negli anni 3-4 (`furioso.md` §2.5, `anno5-mondo.md` §4.2) |
| 7 | Il quarto tipo negli anni 3 e 4 | **chiusa** — **nessun luogo interpretativo negli anni 2-4**: tutti i legami `I` restano nella stanza del *Furioso* (5-12, Borges) |

**Le due questioni nuove, che sono le vere.**

1. **Le undici facoltative continentali sono proposte e non schede** (§4.7). Otto hanno una frase che passa il test della frase; tre sono **situazioni** senza persona (Corea, Artide, Puglia) e hanno bisogno di un controllo di fonte. La domanda è se bastano le fonti che ho o se serve un abbozzo di bibliografia prima (§7 V14, e `anno2/3/4` §13 Q10, che è la stessa domanda tre volte).
2. **Il tipo di legame dei ventisei pin del quinto anno** non è scritto da nessuna parte. `dati/luoghi_gioco.json` porta il **luogo** e il suo stato di coordinata; il tipo `B/A/S/I/C` del pin è un'altra cosa, e sta nel catalogo degli accoppiamenti persona–luogo, che è ancora da generare. Finché quel catalogo non esiste, **la mappa sa dove il gioco si ferma ma non sa perché**: è la metà del lavoro, ed è dichiarato invece che taciuto.

---

## 9. Cosa c'è da fare

*(i primi quattro punti della v0.2 sono **fatti** e non sono più nella lista; una cosa fatta sta nel registro, non nella lista)*

1. **Generare `dati/videogioco-5-duchi-luoghi.json`** con lo schema di §5.1, cominciando dall'Anno II, che è l'unico con una mappa già costruita e verificata. È il punto che chiude la Q8.2.
2. **Le undici fonti delle facoltative continentali** (§4.7): tre situazioni senza persona e otto biografie. È un abbozzo di bibliografia, non una verifica.
3. **Aggiornare `AGENTS.md`** con: i cinque tipi di legame, il tipo `N`, il vincolo del pin unico, la regola dei due strati, e l'eccezione dei luoghi fantastici (nessuna coordinata).
4. **La costellazione finale del §4.6**: nove voci e una domanda. Va prototipata prima di tutto il resto, perché è la fine del gioco.
5. **La resa grafica delle stanze**: un quarto dei luoghi delle stanze non ha coordinate e non può essere disegnato come gli altri (`furioso.md` §8, Q6.2).

---

## 10. Registro modifiche

- **v0.3 (02/10/2026)**: le sedici decisioni di Pietro applicate. Il capitolo 4 è stato riscritto quasi tutto; il capitolo 3 ha una correzione vera e le verifiche V8, V9, V10, V12, V13, V14 sono chiuse.
  - **la regola dei due strati entra in §4.5 come soluzione**, non più come proposta: il pin reale e verificato, la stanza del filone, e la spiegazione di che cosa sono i pin (che era la domanda di Pietro: il pin è il luogo dove il gioco si ferma, uno per tappa, e più tappe possono fermarsi nello stesso posto). Il blocco `tappe` di `dati/luoghi_gioco.json` porta i trenta binomi pin/stanza, con due verifiche automatiche nuove;
  - **il tipo `C` entra nella scala ufficiale** (§1.5): Sophia Loren resta a Pozzuoli e con lei una delle lezioni più difficili del gioco;
  - **nasce il tipo `N`, il non luogo**: «l'aria sopra la foresta» non è un luogo che non esiste, è una condizione che si attraversa (§4.3, `furioso.md` §4.9). Gli elenchi dei luoghi inesistenti e dei non luoghi restano disgiunti, ed è controllato;
  - **tre verifiche fatte e una correzione vera nel catalogo**: Caravaggio a Brera è la **Cena in Emmaus** del 1606, e il nome del dipinto cambia l'insegnamento (§3.1 voce 5, V10); la parentela di Agramante è verificata sul testo e **«padre di Bradamante» è dichiarato errato** (V9); «imperatore di Mongolia» è del materiale, non del poema, che dice **Agrican** (V8);
  - **l'Africa del §6.1 è riscritta sulla parola del testo**: il poema dice «i Mori», «i pagani», «l'ospite saracin», e «Africa» è una terra non un nome di popolo. Le tre formule che il testo usa davvero sono citate con il canto, e da esse esce la regola di conduzione. Il gioco non dirà che «anche oggi è come nel poema»;
  - **i buchi geografici diventano facoltative** (§4.7): undici nomi, undici stanze, ciascuna con la frase che passa il test della frase e con l'elenco di ciò che resta da verificare. Una facoltativa può portare il protagonista **fuori dal continente**, e in quel caso lo dichiara;
  - **il tetto di 60-70 pin era sbagliato**, e lo dicono i dati: i pin-tappe per anno sono 37, 46, 36 e 30. Il tetto non avrebbe vincolato niente, e la regola che resta è quella che i dati applicano da soli;
  - **De Sica → Kurosawa entra**, nella sua direzione vera;
  - **le sette questioni aperte sono chiuse** e al loro posto ne sono nate due: le fonti delle undici facoltative, e il tipo di legame dei pin che nessun file porta ancora.

- **v0.2 (02/10/2026)**: controllo di coerenza su tutto il progetto. Il testo non cambia: cambiano i rimandi e due dichiarazioni.
  - **due rimandi di versione erano fermi**: `anno5-mondo.md` era indicato alla v0.1 (è alla v0.2) e `anno4-mondo.md` alla v0.2 (è alla v0.3);
  - **la Q1 ha una proposta**: `videogioco-5-duchi-furioso.md` v0.3 §2.2 scioglie la domanda con la **regola dei due strati** — il pin resta reale e verificato, la stanza è quella del filone — e la Q1 §8 passa a «proposta risolta, da ratificare». Non è chiusa: è una decisione di Pietro;
  - **l'elenco dei luoghi fantastici è dichiarato non definitivo**: le stanze dei filoni ne introducono uno in più, «l'aria sopra la foresta», che è una condizione e non un luogo, e la decisione su se sia un luogo o no è dichiarata aperta in §4.3;
  - **`videogioco-5-duchi-luoghi.json`** è marcato **da generare** dove viene descritto, non solo dove lo si promette: un file promesso in un punto e dimenticato in un altro è un file che non arriva.

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
