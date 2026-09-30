# Catena dei 30 personaggi e tessere della mappa (anno 1). Richiede build_anno1.py nella stessa cartella.
import json, re
exec(open("build_anno1.py").read().split("keys=[")[0])  # carica EPOCHE, LUOGHI, P
# Rinomina e nuovi luoghi (v0.2)
LUOGHI=[(a,("Piazza Trento Trieste e Palazzo della Ragione" if a=="L06" else b),c,d) for a,b,c,d in LUOGHI]
NUOVI=[("L33","Museo della Cattedrale (ex chiesa di San Romano)"),("L34","Loggia dei Merciai (fianco della Cattedrale)"),
("L35","Casa Romei"),("L36","Volto del Cavallo (Palazzo Municipale, statue di Nicolò III e Borso)"),
("L37","Orto Botanico dell'Università (corso Ercole I d'Este)"),("L38","Palazzo Renata di Francia (sede del Rettorato)"),
("L39","Palazzo Arcivescovile"),("L40","Area della Fortezza pontificia scomparsa (1608-1859)"),
("L41","Piazza Ariostea e la colonna (statua di Napoleone 1810, di Ariosto 1833)"),("L42","Mulino sul Po (ricostruzione, Ro Ferrarese)"),
("L43","Chiesa di San Domenico"),("L44","Via Ripagrande (casa di Bartolomeo Chiozzi)"),("L45","Darsena e Po di Volano in città"),
("L46","Mura: baluardi e fortificazioni per l'artiglieria (tratto nord)"),("L47","Castello Estense: appartamenti, Via Coperta, Loggia degli Aranci"),
("L49","Via delle Volte")]
LUOGHI+= [(a,b,False,"") for a,b in NUOVI]
LN={a:b for a,b,c,d in LUOGHI}; PN={t[0]:t[1] for t in P}
APP={ # titoli approfondimenti anno 1 (da videogioco-5-duchi-schema-livelli.md v1.1)
1:[("B11.6","Metadati"),("L1.5","La piramide DIKW")],2:[("B1.7","Vantaggi e limiti del digitale"),("B1.8","Strumenti analogici e digitali a confronto")],
3:[("B1.9","Il gioco delle venti domande"),("B1.10","Segnalazioni a due simboli nella storia")],4:[("B2.1.7","Numerazioni di altre culture"),("B2.1.8","Tracce di altre basi nella vita quotidiana")],
5:[("B2.6.1","BCD"),("B2.6.2","Codice Gray")],6:[("B12.5","UUID e hash come impronta"),("B2.2.4","Base64")],
7:[("B2.6.4","Big-endian e little-endian"),("B3.5","La crescita delle memorie nel tempo")],8:[("B2.3.3","Moltiplicazione, divisione, shift"),("B2.6.3","Interi a precisione arbitraria")],
9:[("B4.11","Codici storici: Morse, Baudot, EBCDIC"),("B4.12","L'arte ASCII")],10:[("N2.5","Cifrari a trasposizione"),("N2.9","Steganografia")],
11:[("B4.7","Mojibake"),("B4.8","Emoji e normalizzazione")],12:[("B5.2.2","CMYK e stampa"),("B5.3.2","Palette e colori indicizzati")],
13:[("B6.9","Ricampionamento e interpolazione"),("B8.1","Fotogrammi e frequenza")],14:[("C1.10","Sicurezza elettrica"),("C8.1","Dal componente al circuito integrato")],
15:[("U1.18","Informatica in Italia: CEP, Olivetti"),("D4.3","Architettura Harvard")],16:[("D4.5","Macchine didattiche (Little Man Computer)"),("D6.1","Istruzione macchina")],
17:[("C10.6","Supporti ottici"),("C10.7","Nastri e archiviazione a lungo termine")],18:[("D9.5","Bus di sistema, PCI Express"),("D9.2","Polling")],
19:[("D2.2","Simulatori di circuiti logici"),("D1.4","Semplificazione algebrica")],20:[("C1.6","Circuiti in serie e in parallelo"),("C13.2","Dissipazione termica")],
21:[("I10.1","L'avvio del computer"),("I7.5","Gestori di pacchetti")],22:[("I2.4","Thread"),("I2.2","Descrittore di processo e cambio di contesto")],
23:[("D8.3","Località spaziale e temporale"),("D4.4","Collo di bottiglia di von Neumann")],24:[("I11.1","Utenti, gruppi, privilegi"),("I5.5","File system diffusi")],
25:[("B13.9","Revisione e collaborazione sui documenti"),("U11.1","Scrivere per pubblici diversi")],26:[("B11.9","Formati aperti e proprietari"),("G10.3","Le formule come programmazione funzionale")],
27:[("A7.2.5","Numeri pseudocasuali"),("B5.2.4","Scala di grigi")],28:[("J8.3","Cavi sottomarini"),("J8.4","Tecnologie di accesso")],
29:[("N5.3","Autenticazione a più fattori"),("O1.3","Il test di Turing")],30:[("U6.1","Impronta ambientale del digitale"),("U9.1","Professioni ICT")]}
# livello: (personaggio della catena, luogo obbligato, rimando al successivo, [(personaggio facoltativo|None, luogo) x2])
C={
1:("P01","L02","Quello che sai di me ti arriva da copie di copie. Va' dove i monaci copiavano il sapere: l'abbazia di Pomposa.",[("P02","L03"),(None,"L33")]),
2:("P03","L04","Io ho messo ordine nei suoni. In città, invece, nessuno riesce a mettere ordine fra le fazioni: torna a Ferrara e cerca Salinguerra in piazza.",[("P92","L45"),(None,"L32")]),
3:("P06","L06","Le guerre le vince chi le paga: chiedi ai mercanti di via delle Volte.",[("P05","L34"),("P04","L06")]),
4:("P90","L49","I conti più precisi della città non li teniamo noi: li tengono le monache di Sant'Antonio.",[("P08","L49"),(None,"L45")]),
5:("P11","L07","Mio padre Azzo ha sconfitto Salinguerra; ora tocca a Obizzo diventare signore. Lo trovi nel palazzo di corte.",[("P91","L07"),("P10","L07")]),
6:("P12","L05","Il potere va difeso: un mio discendente costruirà una fortezza a due passi da qui.",[("P09","L05"),("P13","L05")]),
7:("P15","L08","Io ho costruito mura per difendermi. Mio fratello Alberto costruirà qualcosa per attirare gente: va' al suo palazzo.",[("P07","L08"),("P14","L08")]),
8:("P16","L09","Ho fondato lo Studio, ma servono maestri. Il più famoso arriverà da Verona.",[("P89","L09"),(None,"L38")]),
9:("P19","L35","Il mio allievo migliore è diventato signore di Ferrara: va' da Leonello.",[("P17","L35"),("P28","L35")]),
10:("P18","L36","Mio fratello Borso sarà il primo duca. Lo troverai dove ha voluto riposare: la Certosa.",[("P20","L36"),("P21","L36")]),
11:("P22","L11","Voglio che la mia corte sia dipinta mese per mese: va' a Schifanoia.",[("P88","L22"),(None,"L11")]),
12:("P24","L10","Tutti noi abbiamo imparato da Cosmè Tura: lo trovi fra i quadri della Pinacoteca.",[("P26","L10"),("P25","L10")]),
13:("P23","L12","Questo palazzo appartiene a una città nuova, voluta dal duca Ercole: va' all'incrocio degli Angeli.",[("P27","L12"),("P47","L12")]),
14:("P30","L13","Nella mia città nuova arrivano studenti da tutta Europa. Uno, polacco, sta per laurearsi.",[("P31","L13"),("P33","L13")]),
15:("P42","L39","Mentre mi laureavo, a Ferrara arrivava una sposa di cui tutti parlavano: Lucrezia.",[("P41","L09"),("P38","L39")]),
16:("P35","L15","Alla corte di mio marito c'è un poeta che racconta cavalieri e follie: Ludovico.",[("P57","L16"),("P40","L15")]),
17:("P37","L14","Il mio signore Alfonso preferisce i cannoni ai versi: lo trovi sulle mura.",[("P29","L14"),(None,"L09")]),
18:("P36","L46","La guerra ferisce. Per curare servono medici che osservano davvero: cerca Brasavola fra le sue piante.",[("P48","L47"),(None,"L46")]),
19:("P44","L37","Sono il medico del nuovo duca, Ercole II. Va' a corte: il Castello non è più una fortezza.",[("P45","L37"),("P43","L37")]),
20:("P49","L47","Mio figlio Alfonso sarà l'ultimo duca di Ferrara.",[("P50","L38"),(None,"L47")]),
21:("P51","L17","Non ho eredi. Il papa reclama la città: sarà lui a decidere.",[("P52","L17"),("P54","L47")]),
22:("P58","L40","Sotto il papa la città cambia ritmo. Nei vicoli si racconta di un uomo che parla con il diavolo.",[("P88","L22"),("P55","L02")]),
23:("P59","L18","Io mi occupavo di acque. Dopo di me un matematico le studierà meglio, senza che nessuno lo chiami mago.",[(None,"L43"),(None,"L44")]),
24:("P61","L45","Alla fine della mia vita arrivano i francesi, con un'altra idea di città, di leggi e di teatro.",[("P92","L01"),(None,"L11")]),
25:("P62","L19","Dopo i francesi torna il papa; ma nel 1848 i giovani ferraresi prendono le armi.",[("P63","L41"),(None,"L19")]),
26:("P65","L20","Dopo l'Unità questa terra è diventata campi, poi fabbriche: va' verso il Po.",[("P66","L21"),("P67","L20")]),
27:("P83","L25","Gli anni in cui costruivamo la fabbrica furono anche anni di leggi ingiuste. Uno scrittore li ha raccontati.",[("P71","L26"),("P73","L12")]),
28:("P79","L22","Io ho trasformato la storia in racconto. Un altro scrittore ha trasformato un uomo vero in un mago: cercalo sul Po.",[("P88","L23"),("P81","L30")]),
29:("P60","L42","Ora sai come si costruisce un racconto. Resta l'ultima prova: raccontare tu la città, dall'alto delle mura.",[("P82","L11"),("P74","L26")]),
30:("P93","L21","(fine dell'anno: la città intera è visibile)",[("P85","L27"),("P86","L28")]),
}
seen=set(); used=set()
for n in range(1,31):
    pid=C[n][0]; assert pid not in used,(n,pid); used.add(pid)
    for p,l in [(pid,C[n][1])]+C[n][3]: assert l in LN,(n,l); assert (p is None) or p in PN,(n,p)
opt_chars={}
for n in range(1,31):
    for k,(p,l) in enumerate(C[n][3]):
        if p: opt_chars.setdefault(p,[]).append(f"1-{n}/A{k+1}")
tessere=[]
for n in range(1,31):
    pid,l,rim,opts=C[n]
    tessere.append(dict(livello=f"1-{n}",tessera=f"T{n:02d}",passaggio_obbligato=dict(personaggio=pid,luogo=l),
      rimando_al_successivo=dict(testo=rim,verso=(C[n+1][0] if n<30 else None),condizione="soglia del livello raggiunta"),
      approfondimenti=[dict(slot=f"A{k+1}",nodo=APP[n][k][0],titolo=APP[n][k][1],personaggio=p,luogo=pl) for k,(p,pl) in enumerate(opts)],
      poligono=None))
esplor=[t[0] for t in P if t[0] not in used and t[0] not in opt_chars]
json.dump(dict(versione="0.1",data="2026-09-28",descrizione="Catena narrativa e tessere della mappa dell'anno 1. Coordinate e poligoni da compilare in fase GIS.",
  nuovi_luoghi=[dict(id=a,nome=b,coordinate=None) for a,b in NUOVI],tessere=tessere,
  personaggi_facoltativi=opt_chars,personaggi_solo_esplorazione=esplor),open("videogioco-5-duchi-anno1-mappa.json","w"),ensure_ascii=False,indent=1)
rows=["| Liv. | Tessera | Passaggio obbligato (personaggio → luogo) | Rimando al successivo | Approfondimento A1 (facoltativo) | Approfondimento A2 (facoltativo) |","|---|---|---|---|---|---|"]
def o(n,k):
    p,l=C[n][3][k]; nodo,tit=APP[n][k]
    return f"{tit} `{nodo}` · {LN[l]}"+(f" · {PN[p]}" if p else "")
for n in range(1,31):
    pid,l,rim,_=C[n]
    rows.append(f"| 1-{n} | T{n:02d} | **{PN[pid]}** → {LN[l]} | «{rim}» | {o(n,0)} | {o(n,1)} |")
open("catena.md","w").write("\n".join(rows))
print("catena ok; facoltativi:",len(opt_chars),"solo esplorazione:",len(esplor)); print([PN[e] for e in esplor])
