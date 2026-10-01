"""Costruisce dati/furioso/citazioni.json: una citazione per ogni tappa del 5º anno.

Perché i versi si prendono dal testo e non si scrivono qui: una citazione
dell'Orlando furioso composta a memoria è una citazione sbagliata, e su un
compito di scuola un errore di tre sillabe costa più di una parafrasi mediocre.
In questo file c'è **solo ciò che si può scrivere**: il canto, l'ottava, un
frammento che individua il verso, e il testo che le abbiamo messo intorno — la
parafrasi, il moto del personaggio, l'emozione, il legame col luogo. I versi
escono dal testo, ogni volta, e li si può riscontrare.

DIFETTO CORRETTO IN QUESTA VERSIONE, e racconta perché è il più subdolo di
tutti. Nella prima stesura la citazione indicava i versi per numero
(«ottava 22, versi 1, 5 e 6»). Il numero è fragile: basta che nell'ottava ci sia
una *rima extranea*, cioè un verso senza rima che il 1928 mette fra parentesi, e
tutto si sposta di una riga senza che nessuno se ne accorga. Il risultato è
stato che **53 versi su 78 erano attribuiti al verso sbagliato** — la citazione
esisteva, era quasi tutta giusta, e non combaciava con niente. Un errore che si
vede subito e che si sarebbe propagato in un documento.

Adesso la citazione indica un **frammento distintivo** e il costruttore lo cerca
dentro l'ottava, e prende i versi che vengono dopo. Se il testo cambia, il
frammento non si trova e lo script si ferma: è un errore che dice una parola
all'inizio invece di un refuso in fondo.

Uso:  python3 costruisci_citazioni.py            -> scrive il JSON
      python3 costruisci_citazioni.py --stampa   -> lo mostra in tavella
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import estrai_ottave as E  # noqa: E402

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(RADICE, "dati", "furioso", "citazioni.json")

# I dodici filoni della vicenda. Il codice è nel gioco e nel JSON: F1…F12.
FILONI = {
    "F1": ("La guerra e il patto", "canti 1, 4, 12-16, 18, 22, 33"),
    "F2": ("Angelica e la fuga", "canti 1-2, 5, 9-12, 21, 23"),
    "F3": ("Orlando e il ritorno di sé", "canti 1, 12-13, 23-24"),
    "F4": ("Atlante e il castello incantato", "canti 4, 6, 22-23, 30"),
    "F5": ("La corte di Scozia: Ginevra, Ariodante, Pinabello", "canti 4-5, 7, 23"),
    "F6": ("Alcina e l'isola", "canti 6, 8, 21"),
    "F7": ("Logistilla e l'anello", "canti 6, 22, 25-26"),
    "F8": ("Bradamante e Merlino", "canti 7-8, 21-22"),
    "F9": ("Astolfo e il viaggio straordinario", "canti 22-23, 34-35"),
    "F10": ("Malagigi e l'incantesimo", "canti 11, 25-26"),
    "F11": ("Ruggiero e la conversione", "canti 13-16, 22-26, 41"),
    "F12": ("La parola data a un altro", "canti 24, 30, 32, 46"),
}

# I luoghi che NON esistono, e che quindi sono gli unici a cui si puó assegnare
# il legame `I` secondo `videogioco-5-duchi-luoghi.md` §1.2. Elenco dichiarato,
# perché un elenco non scritto non si controlla: `verifica_citazioni.py` vieta
# a un `I` qualsiasi luogo che non sia in questo elenco.
#
# DIFETTO CORRETTO IN QUESTA VERSIONE: la tappa 5-17 aveva il legame `I` su
# «i monti Rifei», che sono una catena vera. Il tono della citazione è
# fantastico (l'ippogrifo non esiste) e il legame era stato scelto sul tono
# invece che sul luogo: è la regola dei luoghi violata nel modo più invisibile,
# perché nella scheda sembrava tutto coerente.
INESISTENTI = {
    "la Luna": "esiste e non esiste: nel gioco è il luogo perduto, ed è dichiarato come tale",
    "l'aria sopra la foresta": "non è un luogo ma una condizione: la si attraversa, non la si raggiunge",
    "l'isola di Alcina": "l'isola dell'incantesimo, nel canto VI",
    "il castello d'Atlante": "i due castelli che imprigionano nell'illusione, nel canto IV",
    "il regno di Logistilla": "il regno di Logistilla, nel canto VI",
}

# tappa, filone, canto, ottava, blocchi [(frammento, quanti versi)], luogo, tipo,
# moto, emozione, tema, parafrasi
T = [
 ("5-1", "F2", 1, 32, [("ferma baiardo mio", 3)],
  "la strada della fuga di Rinaldo", "A",
  "sdegno", "frustrazione",
  "la misura che hai è quella che hai, e nessuna riga di programma ti avvisa",
  "Una stima sbagliata non è un'idea: è un'altra idea, e il gioco non ti lascia accorgertene. "
  "Rinaldo grida al suo cavallo «ferma il piede!». Il cavallo è sordo e corre. "
  "Non ha nessuno a cui chiedere scusa: ha la distanza, e la distanza cresce."),
 ("5-2", "F3", 23, 124, [("quel letto quella casa", 3)],
  "il bosco dove Orlando perde il senno", "A",
  "ribrezzo", "sconcerto",
  "il punto in cui un'idea smette di reggere non lo scegli: te lo accorgi",
  "A Orlando, di colpo, ogni cosa che amava diventa odio: il letto, la casa, il pastore. "
  "La bisezione cerca esattamente quell'istante — non quello in cui l'idea è vera, "
  "quello in cui cessa di esser vera. Non lo scegli tu: te lo dice il numero."),
 ("5-3", "F9", 22, 30, [("stava mirando se vedea venire", 3)],
  "il bosco di Pontiero", "A",
  "insofferenza", "impazienza",
  "partire da una stima sbagliata porta altrove, e non è un problema di precisione",
  "Astolfo guarda il bosco dalla mattina alla sera aspettando qualcuno che gli porti Rabicano. "
  "Sbagli il punto di partenza e il metodo di Newton ti porta lontano, ordinatamente, "
  "senza sbagliare mai un passo. È la cosa che il livello 5-3 chiede di vedere con gli occhi."),
 ("5-4", "F9", 34, 49, [("zafir rubini oro", 4)],
  "la Luna", "I",
  "stupore", "meraviglia",
  "un'integrale è una somma di pezzi: più vera del disegno della curva",
  "Il paesaggio sulla Luna non si guarda, si conta: zaffiri, rubini, oro, topazi, perle, diamanti. "
  "È un inventario, eppure è la cosa più bella del canto. "
  "L'area sotto una curva è la stessa cosa: non la disegni, la sommi, pezzo per pezzo."),
 ("5-5", "F2", 1, 77, [("rivolgendo a caso gli occhi", 3)],
  "la foresta dove passa Ferraú", "A",
  "curiosità", "sorpresa",
  "un tiro casuale non è un tiro sbagliato: è un tiro senza garanzia",
  "Rinaldo non sta cercando niente: sta guardando, e gli capita addosso un uomo armato. "
  "È il tiro di Monte Carlo — frecce lanciate a caso in un quadrato — solo che lì "
  "nessuno ha bisogno di credere in un dio che abbia misurato la corda."),
 ("5-6", "F5", 5, 23, [("tornar da la radice", 3)],
  "la corte di Scozia", "A",
  "pazienza", "ostinazione",
  "un numero irrazionale si costruisce tagliando e ricominciando",
  "«Come suol tornar da la radice arbor che tronchi e quattro volte e sei.» "
  "L'albero che tagli torna dalla radice: è l'iterazione di Babilonia per √2, "
  "fatta con le mani e senza sapere di star facendo matematica. "
  "Il gioco chiede la stessa cosa: parti da 1, moltiplica per 1,4, arrotonda, ripeti."),
 ("5-7", "F1", 14, 133, [("tornò la fiamma sparsa", 3)],
  "il fossato di Sarza, sotto Parigi", "A",
  "terrore", "allarme",
  "una simulazione a tempo discreto è un incendio che avanza a passi",
  "La fiamma riaccende la fiamma, e in un attimo il fossato è pieno. "
  "Ogni simulazione del clima fa esattamente questo: calcola lo stato, poi il passo dopo. "
  "Se il passo è piccolo non è detto che sia giusto — ed è per questo che il modello va calibrato."),
 ("5-8", "F9", 23, 16, [("indi lo caccia", 3)],
  "l'aria sopra la foresta", "I",
  "risolutezza", "concentrazione",
  "ogni secondo di ritardo è un errore che non si cancella",
  "Astolfo non parte di scatto: va «lento lento». Un'orbita è la stessa frase detta in chiave. "
  "Il tempo che passa non è tempo perso: è tempo che si aggiunge all'errore, e l'errore si somma."),
 ("5-9", "F5", 23, 40, [("orme che di fresco", 3)],
  "la strada di Pontiero", "A",
  "inchiesta", "determinazione",
  "il dato non è il numero aggregato: è la sua distribuzione",
  "Un cavaliere segue le orme fresche per sapere chi ha ucciso. "
  "Non gli interessa «quante persone sono morte»: gli interessa **dove**, una alla volta. "
  "È il punto in cui Snow chiude la pompa di Broad Street, e il punto in cui una mappa cambia la decisione."),
 ("5-10", "F6", 8, 1, [("oh quante sono incantatrici", 3)],
  "il paese degli incantatori", "S",
  "sorpresa", "stupimento",
  "gli stessi dati, due storie opposte: dipende da dove guardi",
  "«Oh quante sono incantatrici, oh quanti incantator tra noi, che non si sanno.» "
  "Gli stessi fatti, due letture opposte, e in mezzo nessuno che si accorga di aver raccontato una cosa sola. "
  "Atlante, in questo, non è un mago: è un grafico."),
 ("5-11", "F6", 6, 35, [("sopra la bella spiaggia", 2)],
  "l'isola di Alcina", "I",
  "inganno", "seduzione",
  "un dataset con una classe sola produce un modello con una risposta sola",
  "Sull'isola di Alcina sono tutti belli, e sono belli **perché** sull'isola di Alcina "
  "non è mai capitato nessun altro. Non è un difetto dell'osservazione: è il campione. "
  "Un'immagine non è un dato finché qualcuno non l'ha chiamata «gatto» — e a chiamarla è stato qualcuno."),
 ("5-12", "F10", 11, 4, [("con questo fe' gl'incanti", 2)],
  "il petron di Merlino", "S",
  "meraviglia", "ammirazione",
  "quattro pezzi e un insieme finito di regole: e produce un testo infinito",
  "Un anello, e i campi si svuotano. Nessuno guarda dentro l'anello: c'è dentro un regolamento. "
  "Quello che il livello chiede — nastro, testina, stato, regola — è la stessa lista, "
  "e la stessa meraviglia: una cosa piccola che sa fare una cosa enorme."),
 ("5-13", "F3", 1, 2, [("dirò d'orlando", 3)],
  "la pagina", "S",
  "intenzione", "annuncio",
  "una macchina è bravissima a dire certe cose e cieca su tutte le altre",
  "Ariosto avvisa il lettore: «cosa non detta in prosa mai né in rima». "
  "È la stessa avvertenza che Turing mette all'inizio: quello che la macchina non sa dire "
  "non è che lo tacerà, è che non lo dirà mai. Il linguaggio è anche un limite."),
 ("5-14", "F12", 32, 102, [("quel che non si sa non si de' dire", 2)],
  "il campo", "S",
  "frontezza", "rifiuto",
  "ci sono domande ben poste che non hanno risposta: e va detto che è un limite",
  "«E quel che non si sa non si de' dire, e tanto men, quando altri n'ha a patire.» "
  "Non è un cinismo: è la forma più onesta che si possa dare a un programma che non termina. "
  "Nel gioco la scheda di questa tappa non ha una soluzione, e il pulsante lo dice."),
 ("5-15", "F4", 4, 30, [("disio d'onore", 2)],
  "il castello d'Atlante", "I",
  "slancio", "urgenza",
  "funziona e non sappiamo perché: la frase va sulla targa, non nel cassetto",
  "Ruggiero non obbedisce a nessun programma: è «disio d'onore e suo fiero destino». "
  "Un motore che gira e che nessuno sa spiegare non è rotto e non è magico: è un problema aperto. "
  "«Non sappiamo ancora» è una frase da mettere sulla targa del livello."),
 ("5-16", "F5", 7, 2, [("ponte e la riviera", 2)],
  "il ponte d'Erifilla sulla riviera", "A",
  "attenzione", "preoccupazione",
  "due reti collegate da un solo cavo: i messaggi girano in tondo",
  "Un ponte sopra un fiume: due sponde che non si parlano e un modo solo di attraversare. "
  "Se due reti si toccano con un cavo solo, il primo messaggio ci torna indietro e il secondo lo segue. "
  "Il ponte che funziona è quello che ha due strade."),
 ("5-17", "F4", 4, 18, [("non è finto il destrier", 2), ("chiamasi ippogrifo", 3)],
  # I monti Rifei ESISTONO: il legame è `S` — il luogo spiega il nome, che è
  # esattamente il tema della tappa — e non `I`. L'errore era nato perché la
  # citazione è fantastica (l'ippogrifo non esiste) e illegame era stato
  # scelto sul tono della citazione invece che sul luogo.
  "i monti Rifei", "S",
  "curiosità", "divertimento",
  "chi scrive lo standard sceglie la parola, e la parola finisce nel manuale di tutti",
  "«Non è finto il destrier, ma naturale, ch'una giumenta generò d'un grifo». "
  "Il nome lo mette chi ha scritto il nome, e poi quel nome gira di bocca in bocca e finisce nel manuale. "
  "Il byte è nato così: da un nome, non da una misura."),
 ("5-18", "F12", 24, 44, [("non si legge in turpin", 2)],
  "il libro di Turpino", "S",
  "scoperta", "soddisfazione",
  "chi decide che cosa è corretto è la fonte, non il giudizio",
  "«Non si legge in Turpin che n'avvenisse; ma vidi già un autor che più ne scrisse.» "
  "Stessa storia, due fonti, e la fonte decide. Nel 1983 sei ingegneri di sei paesi scrivono "
  "una pagina di regole, e quella pagina diventa il modo giusto di comunicare per vent'anni."),
 ("5-19", "F4", 30, 93, [("venne rinaldo a montalbano", 1), ("dopo gran fame", 2)],
  "Montalbano", "S",
  "sollievo", "arrivo",
  "un indirizzo non certifica niente: dice solo «qui», e si verifica arrivando",
  "Rinaldo arriva a Montalbano e ci trova la famiglia intera. "
  "È l'unico modo di sapere che l'indirizzo era giusto: arrivare. "
  "Un indirizzo IP non certifica niente e non garantisce niente; "
  "se sbagli la persona, il messaggio arriva lo stesso — e arriva a un altro."),
 ("5-20", "F1", 16, 37, [("di zibeltaro", 2)],
  "Zibeltaro e l'Erculeo segno, cioè Adria e Ferrara", "A",
  "preoccupazione", "concretezza",
  "una rete di un edificio si progetta con l'acqua che c'è, non con quella che si vorrebbe",
  "I Mori sono usciti «di Zibeltaro e de l'Erculeo segno» e hanno portato via cose. "
  "Zibeltaro ed Ercole sono Adria e Ferrara: la città del duca è dentro il libro che gioca. "
  "Alfonso II chiede una rete per un quartiere nuovo, e un acquedotto disegnato bene non basta "
  "se poi il quartiere resta senza acqua."),
 ("5-21", "F2", 1, 64, [("camin dritto", 2)],
  "la selva", "A",
  "decisione", "risolutezza",
  "il cammino più corto non è il più bello, e quando due costano uguale la scelta è tua",
  "«Ma dove per la selva è il camin dritto»: due sentieri, e uno solo è giusto. "
  "Dijkstra non cerca il sentiero più bello, cerca il più corto, e mette il costo sul tavolo. "
  "Quando due strade costano uguale lo dice, invece di scegliere di nascosto."),
 ("5-22", "F1", 1, 9, [("in premio promettendola", 3)],
  "il campo davanti a Parigi", "A",
  "sfida", "slancio",
  "l'ordine senza autorità funziona se il patto è chiaro e i fatti lo verificano",
  "Carlo Magno promette la donna «a quel d'essi ch'in quel conflitto... degli infideli più copia uccidessi». "
  "Nessuno garantisce il patto, e non serve: ci sono le spade a verificarlo. "
  "È così che funziona una rete senza autorità: la promessa è pubblica e i fatti la controllano."),
 ("5-23", "F7", 6, 45, [("ci terrebbe ormai spanna di terra", 2)],
  "il regno di Logistilla", "I",
  "autorità", "ammirazione",
  "un nome che non appartiene a nessuno è il motivo per cui funziona",
  "«Né ci terrebbe ormai spanna di terra colei, che Logistilla è nominata»: e con quel nome "
  "regna su tre porti. Il nome non è di nessuno ed è di tutti — per questo un indirizzo DNS "
  "può essere il nome di una cosa che appartiene a mezzo mondo. Se avesse un proprietario, l'avrebbe uno solo."),
 ("5-24", "F5", 5, 18, [("per suo amore", 2)],
  "la corte di Scozia", "A",
  "fiducia", "trepida",
  "un segreto che tutti hanno non è un segreto: è una telefonata",
  "Ginevra non ha bisogno che Arïodante glielo dimostri: «per suo amore Arïodante ardea per tutto il core». "
  "Lo sa, e basta. Nel gioco è la chiave: se la possiedi tutti, non protegge niente. "
  "La privacy è il numero di chi possiede la chiave."),
 ("5-25", "F12", 30, 80, [("lesse la carta quattro volte", 2)],
  "la strada del messaggero", "S",
  "impazienza", "ansia",
  "più banda non serve se il canale è lento: la capacità non è la velocità",
  "Una lettera letta quattro volte e sei arriva sei volte, e chi aspetta non smette di piangere. "
  "Aggiungere banda a una strada stretta non serve a nulla: Shannon lo scrisse prima "
  "che il primo computer arrivasse al mare, e per quello gli ho chiesto scusa."),
 ("5-26", "F5", 5, 36, [("sei da me molto discosto", 2)],
  "il duello di Ginevra", "A",
  "esigenza", "severità",
  "le etichette sono una scelta di qualcuno: prima di imparare, sapere chi ha chiamato le cose",
  "«Sei da me molto discosto, e vo' che di tua bocca anco tu 'l dica.» "
  "Ti si chiede di dirlo con la tua bocca, non con quella d'altri. Un dataset è fatto di nomi detti da persone: "
  "prima di imparare qualcosa, bisogna sapere chi l'ha chiamato."),
 ("5-27", "F8", 7, 38, [("vocal tomba di merlino", 2)],
  "la tomba di Merlino, nelle selve di Pontiero", "A",
  "attesa", "fiducia",
  "collegare unità a caso e aspettare che da sole venga fuori qualcosa di giusto",
  "Bradamante va da Merlino per una previsione, e sa che lì dentro c'è scritto. "
  "Nessuno le ha spiegato come si faccia una previsione: le ha detto solo di andare. "
  "È quello che fanno le reti neurali, ed è la cosa di cui bisogna avere più paura e meno certezze."),
 ("5-28", "F12", 30, 2, [("si ravvede e pente", 2)],
  "il luogo del pentimento", "S",
  "pentimento", "irreversibilità",
  "ciò che è stato detto resta, e la responsabilità è di chi lo ha detto",
  "«Si ravvede e pente e n'ha dispetto: ma quel c'ha detto, non può far non detto.» "
  "Il pentimento arriva dopo, e non cancella niente. È la regola dell'AI generativa "
  "e la regola del regolamento: l'uscita è irreversibile, e chi preme il tasto lo sa."),
 ("5-29", "F1", 12, 12, [("tutti cercando il van", 3), ("e vi son molti a questo inganno presi", 2)],
  "la corte di Scozia", "A",
  "sospetto", "irritazione",
  "il merito di una scoperta va a chi l'ha fatta, non a chi l'ha detta per primo",
  "«Tutti cercando il van, tutti gli dánno colpa di furto alcun che lor fatt'abbia.» "
  "Mesi a dare la colpa del metodo a qualcuno, e nessuno a chiedersi come funzioni. "
  "Se la macchina propone e noi non capiamo il ragionamento, la domanda non è se ha ragione: "
  "è di chi è la scoperta."),
 ("5-30", "F3", 1, 1, [("le donne i cavallier", 2), ("di vendicar la morte di troiano", 2)],
  "la prima pagina", "S",
  "impegno", "serietà",
  "un programma è l'elenco di ciò che farà: tutto, e nient'altro",
  "«Le donne, i cavallier, l'arme, gli amori.» Chi comincia un'opera così non promette: elenca. "
  "Il quinto anno finisce con sei fasce bianche e una domanda. "
  "L'elenco che Ariosto fa all'inizio è la stessa cosa: qui c'è scritto che cosa "
  "non troverai, e non è una scusa, è un impegno."),
]


def trova_blocco(versi, frammento, quanti, dove):
    """Cerca il frammento dentro l'ottava e restituisce i 'quanti' versi da lì.

    Fallisce rumorosamente e per nome: è un errore di una parola, e va detto
    subito, non corretto in silenzio.

    DIFETTO CORRETTO IN QUESTA STESSA RIGA, che era la trappola più ovvia del
    file: si contava il numero degli spazi prima del frammento per sapere a
    quale verso appartiene. Ma uno spazio c'è anche dentro un verso, e
    «— Ferma, Baiardo mio, deh, ferma il piede!» ne ha tre: il conto dava il
    verso tredicesimo di un'ottava che ne ha otto. Si cerca ora il frammento
    dentro ogni verso, e dentro i gruppi di due, tre e quattro versi, perché
    un frammento può anche attraversare il confine.
    """
    norm = [E.normalizza(v) for v in versi]
    f = E.normalizza(frammento)
    for larghezza in (1, 2, 3, 4):
        for i in range(len(versi) - larghezza + 1):
            if f in " ".join(norm[i:i + larghezza]):
                if i + quanti > len(versi):
                    raise SystemExit("il blocco %r di %s chiede %d versi e ne restano %d"
                                     % (frammento, dove, quanti, len(versi) - i))
                return i, versi[i:i + quanti]
    raise SystemExit("frammento %r non trovato in %s: %s" % (frammento, dove, versi))


def costruisci():
    ottave = E.indicizza("wikisource")
    righe = []
    for (tappa, filone, canto, n, blocchi, luogo, tipo, moto, emozione, tema,
         parafrasi) in T:
        versi = ottave.get((canto, n))
        dove = "canto %d, ottava %d" % (canto, n)
        if not versi:
            raise SystemExit("la tappa %s punta a %s, che non esiste nell'indice: "
                             "la citazione sarebbe inventata" % (tappa, dove))
        scelti = []
        numeri = []
        for frammento, quanti in blocchi:
            inizio, blocco = trova_blocco(versi, frammento, quanti, dove)
            # una posizione per ogni verso citato: `blocchi` serve al costruttore,
            # `numeri_versi` al verificatore, e se il secondo indicizza per blocco
            # e non per verso il controllo confronta ogni citazione con il primo
            # verso dell'ottava e non combacia mai
            numeri.extend(range(inizio + 1, inizio + quanti + 1))
            scelti.extend(blocco)
        titolo, canti = FILONI[filone]
        righe.append({
            "tappa": tappa,
            "filone": filone,
            "filone_titolo": titolo,
            "filone_canti": canti,
            "canto": canto,
            "ottava": n,
            "riferimento": dove,
            "numeri_versi": numeri,
            "versi": scelti,
            "parafrasi": parafrasi,
            "moto": moto,
            "emozione": emozione,
            "tema": tema,
            "luogo": luogo,
            "legame": tipo,
            "fonte": "Wikisource, Orlando furioso (1928), pubblico dominio",
        })
    attese = ["5-%d" % i for i in range(1, 31)]
    mancanti = [t for t in attese if t not in [r["tappa"] for r in righe]]
    if mancanti:
        raise SystemExit("tappe senza citazione: %s" % ", ".join(mancanti))
    usati = {r["filone"] for r in righe}
    return {
        "documento": "citazioni dell'Orlando furioso per le trenta tappe del quinto anno",
        "versione": 2,
        "data": "2026-10-02",
        "fonte": {
            "opera": "Ludovico Ariosto, Orlando furioso",
            "edizione": "1928, Biblioteca BEIC (tre volumi), trascrizione di Wikisource (it)",
            "licenza": "pubblico dominio",
            "come_si_ottiene": "sorgenti/furioso/scarica_wikisource.py -> dati/furioso/pagine_wikisource.jsonl",
            "come_si_legge": "python3 sorgenti/furioso/estrai_ottave.py --cerca parola",
            "come_si_verifica": "python3 sorgenti/furioso/verifica_citazioni.py",
            "avvertenza_1": "il testo del 1928 modernizza la grafia (sciolto, né, v'è) e conserva la rima "
                            "extranea: alcune ottave hanno sette versi, non otto",
            "avvertenza_2": "l'edizione del 1928 non è la princeps del 1516: dove i due testi divergono, "
                            "la scuola deve scegliere un'edizione e tenere quella. La scelta è di Pietro",
        },
        "regole": {
            "una_ottava_per_tappa": "sì: nessuna tappa riprende la stessa ottava di un'altra",
            "filone": "F1…F12, il racconto a cui la tappa appartiene",
            "legame": "B/A/S/I/C della regola dei luoghi; I solo per i luoghi che non esistono",
            "parafrasi": "due o tre frasi, in italiano di bocca: è ciò che il livello legge al ragazzo",
            "moto": "che cosa prova il personaggio del Furioso in quel momento",
            "emozione": "la sfumatura che il gioco deve far sentire",
            "tema": "la frase che il livello deve far capire, e che va sulla targa",
            "citazione": "il verso si individua con un frammento distintivo, non con un numero di riga: "
                         "nella stesura di Ottobre i numeri di riga sbagliavano 53 versi su 78",
        },
        "luoghi_inesistenti": INESISTENTI,
        "filoni": {
            codice: {"titolo": t, "canti": c,
                     "assegnato": codice in usati,
                     "tappe": [r["tappa"] for r in righe if r["filone"] == codice]}
            for codice, (t, c) in FILONI.items()
        },
        "citazioni": righe,
    }


if __name__ == "__main__":
    documento = costruisci()
    if "--stampa" in sys.argv:
        for r in documento["citazioni"]:
            print("\n%s  %s  %s  [%s]" % (r["tappa"], r["filone"], r["riferimento"], r["legame"]))
            for v in r["versi"]:
                print("    " + v)
            print("    parafrasi: " + r["parafrasi"])
    else:
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(documento, f, ensure_ascii=False, indent=1)
        print("scritte %d citazioni in %s" % (len(documento["citazioni"]), OUT))
        print("filoni usati: %d su %d"
              % (len({r["filone"] for r in documento["citazioni"]}), len(FILONI)))