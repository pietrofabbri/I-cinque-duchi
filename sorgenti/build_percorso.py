# Percorso unico dell'anno 1 (v0.2): 30 tappe contigue dentro le mura, un personaggio per tappa.
import json
exec(open("build_mappa.py").read().split("# livello: (personaggio")[0])  # EPOCHE, LUOGHI, P, APP, LN, PN
PN["P94"]="Giovanni Romei"
ADDR={ # luogo -> (nome breve, indirizzo di riferimento). Indirizzi da verificare sul dataset civici del Comune.
"L02":("Cattedrale di San Giorgio","Piazza della Cattedrale"),
"L34":("Loggia dei Merciai","Piazza Trento e Trieste, fianco sud della Cattedrale"),
"L06":("Piazza Trento e Trieste e Palazzo della Ragione","Piazza Trento e Trieste"),
"L33":("Museo della Cattedrale (ex San Romano)","Via San Romano 1"),
"L18":("Vicolo del Chiozzino","dal volto in via Ripagrande a via Piangipane"),
"L23":("MEIS","Via Piangipane 81"),
"L05":("Palazzo Municipale e Volto del Cavallo","Piazza del Municipio 2"),
"L08":("Castello Estense","Largo Castello 1"),
"L19":("Teatro Comunale","Corso Martiri della Libertà 5"),
"L09":("Palazzo Paradiso (Biblioteca Ariostea)","Via delle Scienze 17"),
"L38":("Palazzo Renata di Francia","Via Savonarola 9"),
"L35":("Casa Romei","Via Savonarola 30"),
"L15":("Monastero del Corpus Domini","Via Campofranco 1"),
"L07":("Monastero di Sant'Antonio in Polesine","Vicolo del Gambone 17 (indicazione di Pietro)"),
"L10":("Palazzo Schifanoia","Via Scandiana 23"),
"L50":("Palazzo Bonacossi","Via Cisterna del Follo 5"),
"L16":("Palazzina Marfisa d'Este","Corso Giovecca 170"),
"L17":("Antico Ospedale di Sant'Anna (cella del Tasso)","Corso Giovecca (civico da verificare)"),
"L41":("Piazza Ariostea e colonna","Piazza Ariostea"),
"L26":("Palazzo Massari (Museo Boldini)","Corso Porta Mare 9"),
"L12":("Palazzo dei Diamanti (Pinacoteca)","Corso Ercole I d'Este 21"),
"L13":("Quadrivio degli Angeli (Palazzo Prosperi-Sacrati)","incrocio Corso Ercole I d'Este / Corso Porta Mare / Corso Biagio Rossetti"),
"L37":("Palazzo Turchi di Bagno e Orto Botanico","Corso Ercole I d'Este 32"),
"L20":("Museo del Risorgimento e della Resistenza","Corso Ercole I d'Este 19"),
"L14":("Casa di Ludovico Ariosto","Via Ariosto 67"),
"L28":("Stadio Paolo Mazza","Corso Piave 28"),
"L51":("Porta degli Angeli e mura nord","fine di Corso Ercole I d'Este"),
"L53":("Certosa: chiostro, monumento a Teodoro Bonati","Certosa (punto interno, senza civico)"),
"L24":("Cimitero ebraico","Via delle Vigne 20"),
"L11":("Certosa: cimitero monumentale","Piazza della Certosa"),
"L52":("Certosa: chiesa di San Cristoforo","Piazza della Certosa"),
}
# tappa: (luogo, personaggio della catena, aggancio con l'argomento, forza dell'aggancio, battuta di rimando, [facoltativi nello stesso luogo])
T=[
("L02","P01","Una traccia (un'iscrizione, una reliquia, una leggenda) è un dato; diventa informazione solo quando qualcuno la interpreta","forte","Le tracce passano di mano in mano. Esci verso sud: sul fianco della chiesa si commercia da secoli.",["P02"]),
("L34","P90","La bilancia a bracci misura in modo continuo (analogico); le monete si contano (digitale)","forte","Qui si parla di affari, ma in piazza si decide chi comanda: cerca Salinguerra.",["P05"]),
("L06","P06","Guelfi o ghibellini: ogni schieramento è una scelta sì/no; n scelte producono 2ⁿ scenari","forte","Le fazioni passano, i canti restano: nel museo di fronte ci sono i libri del coro.",["P04"]),
("L33","P03","Sul rigo musicale il valore di una nota dipende dalla sua posizione: è l'idea della notazione posizionale","forte","Io ho messo ordine nei suoni. Scendi verso via Ripagrande: in un vicolo buio viveva un uomo che metteva ordine nelle acque.",[]),
("L18","P59","La bilancia dell'ingegnere con pesi 1, 2, 4, 8…: ogni quantità è una somma di potenze di 2","forte","Mi chiamavano mago perché calcolavo. In fondo al vicolo, in via Piangipane, c'è chi custodisce un altro modo di scrivere i numeri.",[]),
("L23","P88","Nell'alfabeto ebraico le lettere valgono anche come numeri; l'esadecimale usa lettere (A–F) come cifre","forte","Torna verso il centro, di fronte alla Cattedrale: al palazzo di corte ti aspetta il primo signore della città.",[]),
("L05","P12","Il signore fissa pesi e misure della città: stessa parola, valori diversi, come kB e KiB","forte","Il potere va difeso: dietro questo palazzo c'è la fortezza. Cerca il duca che fonde i cannoni.",["P18","P20"]),
("L08","P36","Un registro, come una fortezza, ha una capienza fissa: che cosa succede quando il numero non ci sta (overflow)","medio","Io faccio parlare i cannoni. Qui accanto, al teatro, si parla una lingua che tutti devono capire.",["P15","P48"]),
("L19","P62","Il teatro pubblico nasce in un'epoca di regole uguali per tutti: ASCII è una tabella comune, adottata da tutti","medio","Una lingua comune serve anche per i segreti. Allo Studio un maestro ha ritrovato in un libro antico il cifrario di Cesare.",["P63"]),
("L09","P19","Gli umanisti rileggono Svetonio, che descrive il cifrario usato da Cesare: prova di corte su codifiche e cifrari","forte","Il mio allievo Leonello è stato signore; oggi a corte si parla francese, latino e italiano. Va' dal duca Ercole II.",["P16","P42"]),
("L38","P49","Una corte multilingue (italiano, francese, latino) ha bisogno di un repertorio di simboli per tutte le lingue: Unicode","forte","Mia moglie Renata ama i libri e le idee nuove. Poco più avanti, in via Savonarola, c'è una casa dipinta con molti colori.",["P50"]),
("L35","P94","Gli affreschi della Sala delle Sibille: i colori come mescolanza di componenti (RGB)","medio","Nel monastero qui dietro è sepolta una duchessa di cui tutti credono di conoscere il volto.",["P28"]),
("L15","P35","Un volto a bassa risoluzione non si riconosce: così il mito ha sostituito la persona","forte","Scendi verso sud: il monastero più antico della città ha una regola che dura da secoli.",["P40"]),
("L07","P11","Il monastero è l'hardware; la Regola che lo fa funzionare è il software","forte","Da qui si vede il palazzo delle feste di Borso: vai a Schifanoia, dove il tempo è dipinto mese per mese.",["P91"]),
("L10","P24","Il Salone dei Mesi è un calendario calcolato: contare e calcolare prima delle macchine, fino a von Neumann","medio","Io ho dipinto; ma chi ha deciso che cosa dipingere? Chiedilo all'archivista qui accanto.",["P25","P22"]),
("L50","P26","Il duca ordina, l'archivista interpreta, i pittori eseguono: preleva, decodifica, esegui","forte","Una storia non dipinta resta solo nella memoria. Risali verso la Giovecca, alla palazzina di Marfisa.",["P27"]),
("L16","P57","La città ricorda Marfisa più per la leggenda che per i documenti: memorie diverse, veloci o durevoli","medio","Lungo la Giovecca c'è l'ospedale dove un duca tenne chiuso un poeta.",[]),
("L17","P51","Il duca decide che cosa entra e che cosa esce dalla cella di Tasso: dispositivi di ingresso e di uscita","medio","Io non ho eredi, e la mia città cambierà padrone molte volte. In piazza Ariostea una colonna lo racconta.",["P52"]),
("L41","P63","Sulla colonna: SE governa il papa ALLORA la sua statua; SE Napoleone ALLORA la sua; poi Ariosto. Condizioni e porte logiche","di scena","Dopo di me arrivano i pittori moderni: a palazzo Massari ne trovi uno che ha conquistato Parigi.",[]),
("L26","P71","Prova di corte: scegliere i componenti giusti per lo scopo, come un ritrattista sceglie luce, posa e sfondo","di scena","Ferrara mi ha dato l'occhio; ma questa parte della città l'ha disegnata un architetto. Lo trovi al palazzo dei Diamanti.",["P74"]),
("L12","P31","L'Addizione è un sistema che assegna risorse (strade, lotti, acqua) a chi vive nella città: un sistema operativo","medio","Il mio committente è all'incrocio qui fuori: è lui che ha voluto la città nuova.",["P23"]),
("L13","P30","I cantieri dell'Addizione si aprono uno dopo l'altro: processi, attese, turni","medio","Nel palazzo di fronte crescono le piante del mio medico.",["P33"]),
("L37","P44","L'orto è una memoria organizzata: ogni pianta ha il suo posto e il suo indirizzo","forte","Poco più giù lungo il corso c'è il museo di chi ha combattuto per l'Italia.",["P45"]),
("L20","P65","Archivi, lasciapassare, copie dei documenti: file, permessi, backup","medio","Anche i poeti conservano copie: Ariosto ha riscritto il suo poema tre volte. Vai a casa sua.",["P66"]),
("L14","P37","Tre edizioni dell'Orlando furioso (1516, 1521, 1532): struttura, stili e revisioni di un documento","forte","Io ho raccontato cavalieri. In fondo al corso, alla porta degli Angeli, qualcuno racconta la pianura con i numeri.",["P29"]),
("L51","P83","Tabelle di produzione: righe, colonne, formule che calcolano totali e differenze. Il foglio elettronico","medio","I miei numeri parlano di fabbriche. Ma chi per primo ha misurato quest'acqua e questa terra riposa alla Certosa, qui vicino: Teodoro Bonati.",["P86"]),
("L53","P61","Le serie dei livelli del Po nel tempo: medie, variabilità, grafici. La statistica","forte","Dietro la Certosa, in via delle Vigne, riposa uno scrittore che ha raccontato gli anni più bui.",["P92"]),
("L24","P79","Evento → testimonianza → racconto → film: un messaggio che passa da un canale all'altro (sezione narrativa lenta e non valutata)","forte","Il mio racconto è diventato un film. Alla Certosa riposa un regista che sapeva che ogni inquadratura è una scelta.",["P88"]),
("L11","P82","Valutare le fonti; la missione del Chiozzino (cinque versioni e una risposta di un'IA da verificare)","forte","Hai visto molte Ferrara. Nella chiesa qui accanto ti aspetta chi te le ha raccontate fin dall'inizio.",["P81","P60"]),
("L52","P93","Prova finale: la città, con la voce dei suoi luoghi, chiede a Borso di ordinare le 30 carte nel tempo e di costruirne l'inventario","forte","(fine dell'anno)",["P87"]),
]
assert len(T)==30
used=[t[1] for t in T]; assert len(set(used))==30
for t in T: assert t[0] in ADDR
tappe=[]
for i,(l,pid,agg,forza,rim,opt) in enumerate(T,1):
    tappe.append(dict(livello=f"1-{i}",ordine=i,luogo=l,nome_luogo=ADDR[l][0],indirizzo=ADDR[l][1],coordinate=None,
      personaggio=pid,nome=PN[pid],aggancio=agg,forza_aggancio=forza,
      rimando=dict(testo=rim,verso=(T[i][1] if i<30 else None),condizione="soglia del livello raggiunta"),
      approfondimenti=[dict(slot=f"A{k+1}",nodo=APP[i][k][0],titolo=APP[i][k][1]) for k in range(2)],
      personaggi_facoltativi_nello_stesso_luogo=opt))
json.dump(dict(versione="0.4",data="2026-09-28",
  descrizione="Percorso unico dell'anno 1: 30 tappe contigue dentro le mura di Ferrara, un personaggio per tappa. Coordinate da ricavare dagli indirizzi con il dataset civici del Comune (CC BY 4.0).",
  nuovi_personaggi=[dict(id="P94",nome="Giovanni Romei",nota="Mercante e banchiere legato agli Este, committente di Casa Romei (metà XV secolo). Scheda da completare e date da verificare.")],
  tappe=tappe),open("videogioco-5-duchi-anno1-mappa.json","w"),ensure_ascii=False,indent=1)
rows=["| Tappa | Luogo (indirizzo) | Personaggio | Argomento del livello | Aggancio | Forza | Rimando al successivo | Facoltativi |","|---|---|---|---|---|---|---|---|"]
import re
TIT={}
for line in open("/home/claude/duchi/catena.md"): pass
titles=["Informazione, dato, messaggio","Analogico e digitale","Il bit","Sistemi di numerazione posizionali","Conversioni binario ↔ decimale","Ottale ed esadecimale","Unità di misura","Aritmetica binaria e overflow","Codifica del testo: ASCII","Prova: codifiche e cifrario di Cesare","Unicode e UTF-8","Colori RGB","Immagini raster","Hardware e software","Von Neumann e storia del calcolo","Ciclo fetch-decode-execute","Memorie","Periferiche e bus","Porte logiche e algebra di Boole","Prova: assemblare un calcolatore","Il sistema operativo","Processi e scheduling","Gestione della memoria","File system, permessi, backup","Il documento elettronico","Foglio elettronico: celle e formule","Funzioni, grafici, statistica","Internet: struttura e servizi","Valutare le fonti, sicurezza, IA","Prova finale: inventario"]
for i,t in enumerate(tappe):
    f=", ".join(PN[x] for x in t["personaggi_facoltativi_nello_stesso_luogo"]) or "—"
    rows.append(f"| {t['livello']} | {t['nome_luogo']} ({t['indirizzo']}) | **{t['nome']}** | {titles[i]} | {t['aggancio']} | {t['forza_aggancio']} | «{t['rimando']['testo']}» | {f} |")
open("percorso.md","w").write("\n".join(rows))
from collections import Counter; print(Counter(t[3] for t in T))
