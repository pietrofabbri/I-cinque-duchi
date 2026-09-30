import json, math
from geo import g
# luogo -> (via ufficiale, civico, esponente, nota)
Q={"L02":("PIAZZA DELLA CATTEDRALE",9,"","civico del lato della Cattedrale"),
"L34":("PIAZZA TRENTO E TRIESTE",21,"","civico centrale della Loggia dei Merciai"),
"L06":("PIAZZA TRENTO E TRIESTE",4,"","civico del lato ovest della piazza (Palazzo della Ragione): da verificare"),
"L33":("VIA SAN ROMANO",7,"","nel dataset non esiste il n. 1: usato il civico dispari più a nord, da verificare"),
"L18":("VICOLO DEL CHIOZZINO",4,"",""),
"L23":("VIA PIANGIPANE",81,"",""),
"L05":("PIAZZA DEL MUNICIPIO",2,"",""),
"L08":("LARGO CASTELLO",1,"",""),
"L19":("CORSO MARTIRI DELLA LIBERTA'",5,"",""),
"L09":("VIA DELLE SCIENZE",17,"",""),
"L38":("VIA GIROLAMO SAVONAROLA",9,"",""),
"L35":("VIA GIROLAMO SAVONAROLA",30,"",""),
"L15":("VIA CAMPOFRANCO",1,"",""),
"L07":("VIA DEL GAMBONE",15,"","indirizzo fornito da Pietro"),
"L10":("VIA SCANDIANA",23,"",""),
"L50":("VIA CISTERNA DEL FOLLO",5,"",""),
"L16":("CORSO DELLA GIOVECCA",170,"",""),
"L17":("CORSO DELLA GIOVECCA",203,"","indirizzo fornito da Pietro (ingresso secondario: Rampari di San Rocco 15)"),
"L26":("CORSO PORTA MARE",9,"",""),
"L12":("CORSO ERCOLE PRIMO D'ESTE",21,"",""),
"L37":("CORSO ERCOLE PRIMO D'ESTE",32,"",""),
"L20":("CORSO ERCOLE PRIMO D'ESTE",19,"",""),
"L14":("VIA LUDOVICO ARIOSTO",67,"",""),
"L28":("CORSO PIAVE",28,"",""),
"L51":("CORSO ERCOLE PRIMO D'ESTE",152,"","ultimo civico del corso, presso la Porta degli Angeli"),
"L24":("VIA DELLE VIGNE",20,"",""),
"L11":("VIA BORSO",1,"","ingresso della Certosa"),
}
C={}
for l,(v,n,e,nota) in Q.items():
    c=g(v,n,e); assert c,(l,v,n); C[l]=dict(lat=c[0],lon=c[1],fonte=f"civico {v} {n}{e}",nota=nota or None)
# derivati
a,b=C["L12"],C["L37"]; C["L13"]=dict(lat=round((a['lat']+b['lat'])/2,6),lon=round((a['lon']+b['lon'])/2,6),fonte="punto medio fra Corso Ercole I d'Este 21 e 32 (centro dell'incrocio, stimato)",nota=None)
import statistics as s
from geo import allof
A=allof("PIAZZA ARIOSTEA"); C["L41"]=dict(lat=round(s.mean(x[2][0] for x in A),6),lon=round(s.mean(x[2][1] for x in A),6),fonte="baricentro dei civici di Piazza Ariostea (centro della piazza, stimato)",nota=None)
C["L52"]=dict(lat=None,lon=None,fonte=None,nota="la chiesa di San Cristoforo non ha un numero civico proprio: punto da posizionare a mano sulla facciata")
json.dump(C,open("coord_tappe.json","w"),ensure_ascii=False,indent=1)
