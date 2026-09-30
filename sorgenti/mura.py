import json, math, numpy as np
from scipy import ndimage
from skimage import measure
from geo import IDX
from civici import to_wgs84
LAT0,LON0=44.8375,11.6200; KX=111320*math.cos(math.radians(LAT0)); KY=110540
def xy(la,lo): return ((lo-LON0)*KX,(la-LAT0)*KY)
X0,X1,Y0,Y1=-2600,2600,-2400,2600; C=20
nx,ny=int((X1-X0)/C),int((Y1-Y0)/C); occ=np.zeros((ny,nx),bool)
P=[]
for via,lst in IDX.items():
    for n,e,p in lst:
        E,N=p
        if not (1702000<E<1709500 and 4964500<N<4971500): continue
        x,y=xy(*to_wgs84(E,N)); P.append((x,y))
        i,j=int((y-Y0)/C),int((x-X0)/C)
        if 0<=i<ny and 0<=j<nx: occ[i,j]=True
np.save("occ.npy",occ)
import sys
for r in (2,3,4):
    st=ndimage.generate_binary_structure(2,1); st=ndimage.iterate_structure(st,r)
    dil=ndimage.binary_dilation(occ,st)
    lab,n=ndimage.label(dil)
    ci,cj=int((0-Y0)/C),int((0-X0)/C)
    comp=lab==lab[ci,cj]
    comp=ndimage.binary_fill_holes(comp); comp=ndimage.binary_erosion(comp,st)
    area=comp.sum()*C*C/1e6
    ys,xs=np.nonzero(comp); print(r,"area km2",round(area,2),"x",xs.min()*C+X0,xs.max()*C+X0,"y",ys.min()*C+Y0,ys.max()*C+Y0)
