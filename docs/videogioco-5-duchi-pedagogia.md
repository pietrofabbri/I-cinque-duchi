---
titolo: Videogioco "I cinque duchi" — il modello pedagogico applicato al gioco: sei principi, quattro strati, e che cosa non entra
versione: 0.2
data: 2026-10-03
autore: Pietro Fabbri (con Claude)
fonte del materiale: «Modello pedagogico generale — esiti», documento di sintesi prodotto nel percorso di lavoro di Pietro (IPSIA trattata in altra sede), con la richiesta del 03/10/2026: «il gioco deve, quando non viene denaturato per quello che è as is, osservare anche questi principi pedagogici»
dati: nessuno: questo documento non aggiunge dati e non li inventa; dove manca una dichiarazione, la dice e la dichiara mancante
controllo: python3 sorgenti/verifica_pedagogia.py (P1-P5: il nucleo di ogni livello, la cadenza della tappa a mani nude, i sei domini della banca, l'assenza di costruzioni di ingegneria comportamentale, e la presenza delle sei regole in AGENTS.md)
documenti collegati: videogioco-5-duchi-schema-livelli.md (v1.1, i 150 livelli e le loro voci), videogioco-5-duchi-lingue.md (v0.1, i 900 livelli delle sei lingue), videogioco-5-duchi-quadro-trasversale.md (v0.1, i quattro ambiti e le arti per anno), videogioco-5-duchi-gioco.md (v0.5, il ciclo della tappa), videogioco-5-duchi-meccaniche.md (v0.3, punteggio e indicatori), videogioco-5-duchi-esercizi.md (v0.1, i pool), videogioco-5-duchi-ripassi.md (v0.1, i test di ingresso e il vantaggio tangibile che ne deriva), AGENTS.md
---

# Il modello pedagogico applicato al gioco

## 0. La regola che governa questo documento

Il modello è stato scritto per **una classe**: Fawl Tower, contatore meccanico, exit ticket di carta, quarantacinque minuti. Il gioco non è una classe, e il primo rischio è deformarlo per farlo entrare.

> **Una pratica entra nel gioco solo se conserva il principio e resta ciò che è: un gioco.**

Quindi la regola è a due tempi, e va detta prima delle altre perché è quella che decide tutto il resto:

1. **il principio entra**, con la sua ragione, e diventa una regola che chi lavora al gioco deve rispettare;
2. **lo strumento non entra** se è stato scelto per la classe e non per il gioco.

Un esempio per tutti. *Infrastruttura minima* entra come principio e si traduce in una regola che il gioco già rispetta e che nessuno aveva scritta: **una pagina HTML unica, offline, senza account, senza server, senza installare niente**. Il contatore meccanico non entra: è un oggetto di aula, e metterlo dentro un gioco significherebbe far dipendere la risposta da un oggetto che lo studente non ha.

## 1. I sei principi, e che cosa diventano nel gioco

### 1.1 Trasparenza radicale

**Nel gioco significa:** nessuna pratica che il giocatore non possa spiegare. Ogni meccanismo dichiara il suo perché, e nessuno è introdotto in silenzio.

Questo progetto ha già la regola, e ha una forma che nessun altro ha: **quando non si può dichiarare un vuoto, si dichiara il vuoto**. Le 51 ipotesi di coordinata portano il loro grado (`documentata`, `argomentata` con il raggio in metri, `immaginata` e nessun punto), i colori dichiarano la fonte da cui vengono, i ritratti dichiarano se sono autentici o emblemi, i luoghi dichiarano il tipo di legame. La trasparenza radicale qui non è un'aggiunta: è il modo in cui il progetto ha sempre lavorato.

**Il divieto nuovo:** nessun meccanismo di gratificazione può essere introdotto senza che il giocatore ne legga la funzione. Non a per sé — sarebbe noioso — ma accanto a ciò che fa.

### 1.2 Vantaggio tangibile, non promesso

**Nel gioco significa:** ogni esercizio deve lasciare **subito**, lì sullo schermo, qualcosa di vero: una risposta corretta, una mossa che funziona, un numero che si muove. Mai «poi vedrai che sarà utile».

Questo è il principio che ha prodotto la cosa più bella di oggi, e che nessuno dei due documenti avrebbe scritto da solo: i **test di ingresso** (`ripassi.md`). Dieci domande non danno una promessa: danno un **elenco di dieci nomi**, ciascuno con l'oggetto da cui impararlo. Il vantaggio è l'informazione stessa.

### 1.3 Infrastruttura minima

**Nel gioco significa:** nessuna installazione, nessun account, nessuna rete a runtime, nessun permesso. Una pagina, un file di consegna, e il computer della scuola.

La traduzione pratica è la stessa del modello — *solo l'essenziale* — ma l'oggetto essenziale è diverso: qui non è «niente smartphone in classe», è **niente dipendenza**. Nessuna piattaforma, nessun servizio proprietario, nessuna licenza che possa cambiare. È già la scelta del progetto (`README.md`), resa regola.

### 1.4 Formato individuale o comunitario

**Nel gioco significa:** ogni livello dichiara se si gioca da solo o in due o in piccolo gruppo, e **la dichiarazione segue l'obiettivo**, non la preferenza.

Questo è il punto in cui il gioco è più indietro, e va detto: **i 150 livelli non hanno nessun campo che dica come si gioca**. Oggi è implicito «da solo», perché il gioco è un file che ognuno apre sul proprio computer. La proposta è una voce nuova nello schema dei livelli — `Modalità`, con i valori `individuale`, `a coppie`, `piccolo gruppo` — e la regola che decide è quella del modello: **la si sceglie guardando che cosa il livello fa imparare**. Un livello di argomentazione sta in gruppo; un livello di codice no; e la differenza la si dichiara, non la si lascia al caso.

Lo stesso vale per i quattro ambiti trasversali, che sono quasi tutti discussione: diritto, etica, filosofia e psicologia sono gli ambiti in cui il formato comunitario non è un extra.

### 1.5 Nessuna impotenza appresa

**Nel gioco significa:** nessuna situazione in cui la macchina risolve e lo studente guarda. Nessun livello in cui il compito del giocatore sia osservare una risposta giusta.

Qui il progetto è avanti, e per una ragione che va detto perché è la più importante di tutte: il gioco **non usa l'intelligenza artificiale per prodursi**. Non un'immagine generata (`lingue-immagini.md` §1), non un testo inventato, non un volto. E nell'anno 5 l'IA è **contenuto**: si studia come cosa, si vedono i suoi limiti (`citazioni.json`), e la risposta del modello è sempre da verificare.

La regola che ne deriva è semplice e va scritta: **in questo gioco non si impara a usare l'IA per fare a meno di pensare**, perché il gioco stesso non lo fa.

### 1.6 La classe orientata al contagio

**Nel gioco significa:** nessun confronto pubblico, nessuna classifica, nessun meccanismo che metta uno studente in mostra davanti agli altri.

Nel gioco la cosa è più facile che in classe, e va scritta perché è una scelta, non un caso: **il punteggio è individuale, non c'è classifica, e il file di consegna è personale**. La regola che rende vera la prima parte è che il progetto vieta le risposte scritte e vieta il confronto fra studenti a schermo.

Una cosa resta **fuori dal gioco** ed è importante dirlo: l'escalation a basso profilo e il silenzio senza reazione visibile sono protocolli di classe, e il gioco non li sostituisce. Se li sostituisse, starebbe decidendo come si comportano le persone.

## 2. I quattro strati del «cosa», e dove stanno già

| strato | nel gioco | stato |
|---|---|---|
| **1. nucleo disciplinare essenziale** | i 150 livelli di `schema-livelli.md`, ciascuno con il suo `Nucleo` | **fatto**: 147 su 150 |
| **2. processi di pensiero** | **nessuna voce nei dati**: nessun livello dichiara quale processo esercita | **da costruire** |
| **3. IA come contenuto** | 1-29, 5-26, 5-27, 5-28, e l'anno 5 intero | **fatto** |
| **4. autoregolazione e relazione** | `meccaniche.md` (non sanziona, segnala), il ritorno come momento degli incontri (`percorsi.md` §4), `ripassi.md` | **fatto e in crescita** |

Il numero della prima riga è un risultato, non una lode: **tre livelli non dichiarano un nucleo nuovo**. Sono **2-13** (iterazione `for` e `range`: solo ripresa), **2-22** e **4-11**. Non è un difetto del metodo, è un elenco che ora esiste e che il prossimo livello scritto non potrà allungare senza dichiararlo.

**Lo strato 2 è la lacuna vera.** Il modello è netto su un punto: i processi di pensiero non si trasferiscono da un dominio all'altro, e quindi **non si insegnano come una materia**, si esercitano ripetutamente dentro domini ricavi e diversi. Il gioco ha dei domini ricavi — l'informatica, le sei lingue, la storia incarnata in persone e luoghi — e **non ha nessun modo di dire che cosa esercita**. È la modifica più grande che questo documento propone, e la forma è semplice: una voce in più nello schema di ogni livello, con un **catalogo chiuso** di processi (scomporre, astrarre, formulare un modello, distinguere un fatto da una fonte, valutare un'affermazione, riconoscere un pregiudizio, argomentare e confutare, controllare un risultato con un altro metodo). Tre regole: un processo non occupa mai un livello da solo, deve comparire in **almeno due domini diversi**, e ogni passaggio fra domini dev'essere **esplicito** — il gioco non può sperare che il ragazzo colleghi da solo.

## 3. La sfida a mani nude, tradotta in una meccanica del gioco

Il modello la descrive in classe: ogni quindici giorni, due o tre minuti, senza aiuti. Nel gioco la stessa cosa diventa **una tappa**, ed è la regola più semplice da scrivere di tutto il documento:

> **Una tappa ogni quindici livelli è «a mani nude»: due o tre minuti, nessun aiuto, nessuno strumento.**

Sono **dieci tappe su centocinquanta**, e sono alle posizioni `1-15`, `1-30`, `2-15`, `2-30`, `3-15`, `3-30`, `4-15`, `4-30`, `5-15`, `5-30`: la quindicesima e la trentesima di ogni anno, cioè **due volte per anno**, che è la cadenza che il modello chiede.

E la regola dell'interruzione è la stessa che vale per i **test di ingresso** (`ripassi.md` R5), ed è importante che siano la stessa: **si riparte senza penalità aggiuntiva e senza reazione visibile**. Nel gioco significa che una tappa a mani nude interrotta non lascia traccia negativa: il tempo impiegato è un dato, non un debito.

### I sei domini della banca, e la lacuna che c'è dentro

| dominio | dove sta oggi |
|---|---|
| `logica` | i 150 livelli, area `A2` e `E1`–`E9` |
| `calcolo mentale e stime` | i 150 livelli, `A1`, `A4`, `A7`, `A10`, e il livello 1-7 sulle unità di misura |
| `informatica` | i 150 livelli: il nucleo dell'intero gioco |
| `linguistica e testo` | i 900 livelli di `lingue.md` |
| `Costituzione e cittadinanza` | `quadro-trasversale.md`: Costituzione, fondamenti e fonti, diritto UE, diritto internazionale |
| `osservazione e attenzione` | il nucleo `Q8.2` del livello 3-27 (attenzione, percezione, memoria); l'osservazione linguistica dei 900 livelli; le tappe 1-23, 1-29 e 5-11 |

L'ultima riga era una scoperta, e la scoperta **era sbagliata**: il documento scriveva che «cinque domini su sei hanno già una casa nel progetto, il sesto non ce l'ha», e il gioco in realtà ci lavorava già sull'osservazione e sull'attenzione in quattro posti che nessuno aveva messi insieme — il nucleo `Q8.2` del livello 3-27, l'osservazione linguistica dei novecento livelli, le tappe 1-23 e 1-29, la 5-11 con la frase sul campione. La riga era `da_costruire` perché il dominio non aveva un capitolo, non perché non esistesse: **una cosa che il gioco fa senza dirlo non è una lacuna, è una riga rimasta indietro.** Le prove sono in `quadro-trasversale.md` §1.3, e lì il dominio ha anche il suo premio (la categoria `D`, la pianta e la sua soglia).

## 4. I cinque segnali di tracciamento, e chi li produce

| segnale | chi lo produce | nel gioco |
|---|---|---|
| tally disposizionale | l'insegnante, con il contatore | **fuori**: nessun contatore nel gioco |
| revisione di posizione | l'insegnante, in attività di gruppo | **fuori**: nessuna attività di gruppo oggi |
| exit ticket a scelta singola | l'insegnante, con la scatola | **fuori**: è carta, e il gioco è un file |
| calibrazione metacognitiva | l'insegnante, sul foglio | **fuori**, ma il gioco ne ha il equivalente: il **punteggio di processo** (`meccaniche.md` §2.3) dice al ragazzo quanto è stato coerente, prima del voto |
| tagging errori per tipologia | l'insegnante, con il codice-lettera | **fuori**: nessun tag degli errori nei dati |

Cinque segnali su cinque sono **del docente**, e questa è la parte importante: il tracciamento del bisogno reale non è un compito del gioco. Il gioco ha un solo dato che glielo rende facile — il **file di consegna**, che è già individuale e già scritto dal giocatore — e non ha né il contatore né la scatola. Costa meno al gioco, e resta comunque la parte che non si può delegare.

## 5. Che cosa non entra nel gioco, e perché

Elenco chiuso, dichiarato perché **un vuoto che non si dichiara viene rifatto**:

| non entra | perché |
|---|---|
| il contatore meccanico e la scatola per exit ticket | strumenti d'aula; dentro un gioco sarebbero un vincolo di materiale su un oggetto che lo studente non ha |
| l'architettura della lezione di 50 minuti | **è la scuola che adatta il gioco**, non il gioco la scuola: il gioco non sa quanto dura la lezione e non deve saperlo |
| l'apertura con burocrazia e clima, la chiusura con exit ticket | riti del docente |
| il protocollo di pausa di silenzio e l'escalation a basso profilo | regole di conduzione della classe; un gioco che le applica starebbe decidendo come si comportano le persone |
| il feedback a dita, il giro palese, il post-it anonimo | canali di aula, e sono tre modi di proteggere chi risponde: nel gioco la protezione è che **non c'è nessun altro che guarda** |
| le sei formazioni d'aula (file, quadranti, coppie, ali, ferro di cavallo, isole) | geografia di una stanza |
| il check-in posturale e la respirazione con misura del polso | pratiche corporee; il gioco è uno schermo e non ha un corpo |
| l'up-regulation (respiro, micro-movimento, scossa cognitiva) | idem |
| l'algoritmo in carne e ossa (bubble sort con i posti) | **è l'unica che si era salvata**, e l'avevo salvata per la ragione sbagliata: si può tradurre in gioco, ma allora è un livello, e i livelli ci sono già |
| il confronto pubblico classe-vs-IA | cancellato nel modello stesso per non indurre impotenza appresa; nel gioco non esiste e non deve esistere |
| il «riconosci chi ha scritto questo testo» | sopravvive solo fra compagni; nel gioco è un **livello fra compagni**, non un meccanismo |

L'ultima riga contiene l'unica cosa che merita di passare dall'aula al gioco, e passa bene: **riconoscere un testo** è esattamente il livello 5-12 (analisi testuale) e il primo livello di lingue. Non serve inventare niente.

## 6. Cosa c'è da fare

1. **La voce `Modalità`** nello schema dei centocinquanta livelli (`schema-livelli.md` §1), con i tre valori e con la regola che la scelta segue l'obiettivo.
2. **Il catalogo chiuso dei processi di pensiero** e la voce corrispondente nei livelli, cominciando dall'anno 1.
3. ~~**Il dominio `osservazione e attenzione`**~~ **chiusa il 03/10/2026**: la riga è riempita (`quadro-trasversale.md` §1.3), il dominio ha il suo premio e le quattro prove sono nel documento che le elenca.
4. **Le dieci tappe a mani nude** nella tabella dei livelli, con la regola che due volte per anno non è un caso.

## 7. Registro delle modifiche

- **v0.1 (03/10/2026)**: prima stesione. I sei principi del modello entrano tutti e sei nel gioco (§1); i quattro strati, di cui uno **fatto**, uno **da costruire** e due fatti (§2); la sfida a mani nude tradotta in **dieci tappe su centocinquanta**, due per anno, con la stessa regola di ripresa senza penalità dei test di ingresso (§3); i cinque segnali di tracciamento, **cinque su cinque del docente**, e la ragione per cui il gioco non deve costruirli (§4); l'elenco chiuso di ciò che non entra, con la ragione per ciascuna riga (§5). La regola che governa il documento è una sola e sta in testa: **una pratica entra nel gioco solo se conserva il principio e resta ciò che è**.
- **v0.2 (03/10/2026)**: **la sesta riga della banca era un difetto, non una scoperta.** «Osservazione e attenzione» era dichiarato `da_costruire` con la frase che «il gioco non ha mai lavorato sull'attenzione e sull'osservazione come oggetto», e il gioco ci lavora in quattro posti che nessuno aveva messi insieme: il nucleo `Q8.2` del livello 3-27 (attenzione, percezione, memoria), l'osservazione linguistica di tutti i novecento livelli, le tappe 1-23 e 1-29, e la 5-11 con la frase sul campione. La scoperta vera è un'altra, ed è nella regola: **una cosa che il gioco fa senza dirlo non è una lacuna, è una riga rimasta indietro**. La riga è riempita, il dominio ha il suo premio (la categoria `D`) in `quadro-trasversale.md` §1.3, e il punto 3 delle cose da fare è chiuso.
