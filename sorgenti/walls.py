import json, math, numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from geo import IDX
from civici import to_wgs84
LAT0,LON0=44.8375,11.6200; KX=111320*math.cos(math.radians(LAT0)); KY=110540
def xy(p):
    la,lo=to_wgs84(*p); return ((lo-LON0)*KX,(la-LAT0)*KY)
R=json.load(open("ring.json")); P=np.array(R["allp"])
# poligono delle mura (stima), in senso orario da Porta degli Angeli
W=[(395,1300),(760,1235),(1110,1150),(1195,720),(1185,380),(1170,-150),(1115,-600),(1010,-830),(905,-990),(860,-1120),(795,-1225),(720,-1360),(470,-1350),(270,-1245),(110,-1030),(-70,-790),(-200,-610),(-480,-470),(-820,-160),(-925,-235),(-620,430),(-885,765),(-700,1020),(-450,1325)]
json.dump(W,open("walls_est.json","w"))
fig,ax=plt.subplots(figsize=(13,13),dpi=85)
ax.scatter(P[:,0],P[:,1],s=1,c="#999",linewidths=0)
cols={"inside":"#1a7f37","outside":"#c2410c"}
INS=["RAMPARI DI SAN ROCCO","RAMPARI DI SAN PAOLO","VIA MURA DI PORTA PO","VIA CARLO MAYR","VIA PORTA D'AMORE","VIA DELLE VIGNE","VIALE DELLA CERTOSA","VIA ARIANUOVA","CORSO PORTA MARE","CORSO PORTA PO","CORSO DELLA GIOVECCA","CORSO ERCOLE PRIMO D'ESTE"]
OUT=["VIA DEI BALUARDI","VIALE ALFONSO PRIMO D'ESTE","VIA POMPOSA","VIA PORTA CATENA","VIALE ORLANDO FURIOSO","VIALE DEGLI ANGELI","CORSO PIAVE","VIA BOLOGNA","VIA SAN MAURELIO","VIA PORTA ROMANA","CORSO ISONZO"]
for grp,names in (("inside",INS),("outside",OUT)):
    for v in names:
        pts=[xy(p) for n,e,p in IDX.get(v,[])]
        pts=[p for p in pts if -1700<p[0]<1600 and -1700<p[1]<1600]
        ax.scatter([p[0] for p in pts],[p[1] for p in pts],s=5,c=cols[grp])
        if pts: m=pts[len(pts)//2]; ax.text(m[0],m[1],v.title()[:22],fontsize=6,color=cols[grp])
ax.plot([w[0] for w in W]+[W[0][0]],[w[1] for w in W]+[W[0][1]],"b-",lw=1.5)
for i,w in enumerate(W): ax.text(w[0],w[1],str(i),color="b",fontsize=7)
ax.set_xlim(-1300,1500); ax.set_ylim(-1700,1600); ax.set_aspect(1); ax.grid(lw=.3)
plt.savefig("walls.png",bbox_inches="tight")
