import json, math
import os
from civici import to_wgs84
LAT0,LON0=44.8375,11.6200; KX=111320*math.cos(math.radians(LAT0)); KY=110540
def xy(la,lo): return ((lo-LON0)*KX,(la-LAT0)*KY)
BOX=(-1400,1450,-1250,1350)  # xmin,xmax,ymin,ymax in metri
if os.path.exists("civici_cache.json"):
    # ricalcolo delle etichette delle vie dai civici (richiede civici_cache.json, generato da civici.py dallo shapefile del Comune)
    from geo import IDX
    # civici del centro
    dots=[]; cache={}
    for via,lst in IDX.items():
        for n,e,p in lst:
            E,N=p
            if not (1703000<E<1708000 and 4965500<N<4970500): continue
            la,lo=to_wgs84(E,N); x,y=xy(la,lo)
            if BOX[0]<x<BOX[1] and BOX[2]<y<BOX[3]:
                dots.append((round(x),round(y))); cache.setdefault(via,[]).append((x,y))
    # assi delle vie principali
    VIE={"CORSO ERCOLE PRIMO D'ESTE":"Corso Ercole I d'Este","CORSO DELLA GIOVECCA":"Corso della Giovecca","CORSO PORTA MARE":"Corso Porta Mare","CORSO MARTIRI DELLA LIBERTA'":"Corso Martiri della Libertà","VIA RIPAGRANDE":"Via Ripagrande","VIA DELLE VOLTE":"Via delle Volte","VIA GIUSEPPE MAZZINI":"Via Mazzini","VIA GIROLAMO SAVONAROLA":"Via Savonarola","CORSO BIAGIO ROSSETTI":"Corso Biagio Rossetti","VIA DELLE SCIENZE":"Via delle Scienze","VIA SCANDIANA":"Via Scandiana","CORSO PORTA PO":"Corso Porta Po","VIA GIUSEPPE GARIBALDI":"Via Garibaldi","CORSO PORTA RENO":"Corso Porta Reno","VIA LUDOVICO ARIOSTO":"Via Ariosto","VIA PALESTRO":"Via Palestro","CORSO ISONZO":"Corso Isonzo","VIALE CAVOUR":"Viale Cavour","VIA CARLO MAYR":"Via Carlo Mayr","VIA BORSO":"Via Borso","VIA DELLE VIGNE":"Via delle Vigne","VIA ARIANUOVA":"Via Arianuova","CORSO PIAVE":"Corso Piave"}
    streets=[]
    for k,name in VIE.items():
        P=cache.get(k,[])
        if len(P)<6: continue
        mx=sum(p[0] for p in P)/len(P); my=sum(p[1] for p in P)/len(P)
        sxx=sum((p[0]-mx)**2 for p in P); syy=sum((p[1]-my)**2 for p in P); sxy=sum((p[0]-mx)*(p[1]-my) for p in P)
        ang=0.5*math.atan2(2*sxy,sxx-syy); ux,uy=math.cos(ang),math.sin(ang)
        bins={}
        for x,y in P:
            t=(x-mx)*ux+(y-my)*uy; b=int(t//40); bins.setdefault(b,[]).append((x,y))
        line=[]
        for b in sorted(bins):
            pts=bins[b]; line.append((round(sum(p[0] for p in pts)/len(pts)),round(sum(p[1] for p in pts)/len(pts))))
        # etichetta al centro
        streets.append(dict(nome=name,linea=line,ang=round(math.degrees(ang),1)))
    json.dump(streets,open("gis/vie_etichette.json","w"),ensure_ascii=False)
else:
    streets=json.load(open("gis/vie_etichette.json"))
M=json.load(open("videogioco-5-duchi-anno1-mappa.json"))
DB=json.load(open("videogioco-5-duchi-anno1-personaggi.json"))
PERS={p["id"]:p for p in DB["personaggi"]}
PERS["P01"]["anno_inizio"]=PERS["P01"]["anno_inizio"] or 650
PERS["P94"]=dict(nome="Giovanni Romei",periodo="XV secolo",anno_inizio=1402,anno_fine=1483,epoca="E4",certezza=["D"],domanda_critica="Che cosa racconta di chi l'ha costruita una casa dipinta?")
EP=DB["epoche"]
titles=["Informazione, dato, messaggio","Analogico e digitale","Il bit","Sistemi di numerazione posizionali","Conversioni binario ↔ decimale","Ottale ed esadecimale","Unità di misura","Aritmetica binaria e overflow","Codifica del testo: ASCII","Prova di corte: codifiche e cifrario di Cesare","Unicode e UTF-8","Colori RGB","Immagini raster","Hardware e software","Von Neumann e storia del calcolo","Ciclo fetch-decode-execute","Memorie","Periferiche e bus","Porte logiche e algebra di Boole","Prova di corte: assemblare un calcolatore","Il sistema operativo","Processi e scheduling","Gestione della memoria","File system, permessi, backup","Il documento elettronico","Foglio elettronico","Funzioni, grafici, statistica","Internet: struttura e servizi","Valutare le fonti, sicurezza, IA","Prova finale: inventario"]
PROVV={"L53":(44.84400,11.62590),"L52":(44.84440,11.62575)}  # posizioni provvisorie solo per il prototipo
stops=[]
for i,t in enumerate(M["tappe"]):
    c=t["coordinate"]; prov=False
    if not c: la,lo=PROVV[t["luogo"]]; prov=True
    else: la,lo=c["lat"],c["lon"]
    x,y=xy(la,lo); p=PERS[t["personaggio"]]
    opt=[]
    for k,a in enumerate(t["approfondimenti"]):
        oc=t["personaggi_facoltativi_nello_stesso_luogo"][k] if k<len(t["personaggi_facoltativi_nello_stesso_luogo"]) else None
        opt.append(dict(titolo=a["titolo"],nodo=a["nodo"],personaggio=(PERS[oc]["nome"] if oc else None)))
    extra=t["personaggi_facoltativi_nello_stesso_luogo"][2:]
    stops.append(dict(n=t["ordine"],x=round(x),y=round(y),provv=prov,luogo=t["nome_luogo"],indirizzo=t["indirizzo"],nome=p["nome"],periodo=p.get("periodo",""),
       a0=p.get("anno_inizio"),a1=p.get("anno_fine"),epoca=p.get("epoca"),epoca_nome=EP.get(p.get("epoca"),""),certezza=" + ".join(p.get("certezza",[])),
       domanda=p.get("domanda_critica",""),argomento=titles[i],aggancio=t["aggancio"],forza=t["forza_aggancio"],rimando=t["rimando"]["testo"],opz=opt))
CITY=json.load(open("gis/citta_centro.json"))
data=dict(mura=CITY["perimetro"],edifici=CITY["edifici_delta_mezzimetri"],box=BOX,streets=streets,stops=stops)
print(len(streets),"vie")
html=open("mappa_proto_template.html").read().replace("/*TAPPA1*/",open("esercizi1.js").read()+"\n"+open("zona1_dati.js").read()+"\n"+open("zona1.js").read()).replace("/*DATA*/",json.dumps(data,ensure_ascii=False,separators=(",",":")))
open("videogioco-5-duchi-anno1-prototipo-mappa.html","w").write(html)
print(len(html)//1024,"KB")
# nel repository: copia anche il prototipo pubblicabile
import os as _os
if _os.path.isdir("../prototipo"):
    open("../prototipo/index.html","w").write(html)
