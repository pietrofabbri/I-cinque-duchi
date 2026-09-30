import json,math
from PIL import Image,ImageDraw
LAT0,LON0=44.8375,11.62;KX=111320*math.cos(math.radians(LAT0));KY=110540
m=json.load(open('videogioco-5-duchi-anno1-mappa.json'))
T=[((t['coordinate']['lon']-LON0)*KX,(t['coordinate']['lat']-LAT0)*KY,t['livello']) for t in m['tappe'] if t.get('coordinate')]
E=json.load(open('gis/edifici_centro_local.json'))['edifici']
cx,cy,R,S=-15,-160,170,3  # centro, raggio visibile, pixel per metro
im=Image.new('RGB',(2*R*S,2*R*S),(235,232,222));g=ImageDraw.Draw(im)
f=lambda x,y:((x-cx+R)*S,(cy+R-y)*S)
# celle di Voronoi (colore per tappa)
cols=[(255,220,220),(220,235,255),(225,255,220),(255,245,200),(240,220,255),(210,250,250),(250,230,210)]
near=[t for t in T if abs(t[0]-cx)<R+60 and abs(t[1]-cy)<R+60]
for py in range(0,2*R*S,3):
    for px in range(0,2*R*S,3):
        x=px/S+cx-R;y=cy+R-py/S
        d=sorted((math.hypot(x-t[0],y-t[1]),i) for i,t in enumerate(near))
        if d[0][0]<150: g.rectangle((px,py,px+2,py+2),fill=cols[d[0][1]%len(cols)])
for e in E:
    for poly in e[3]:
        pts=[f(*p) for p in poly[0]]
        if all(abs(p[0]-cx)>R+50 for p in poly[0]): continue
        g.polygon(pts,fill=(150,110,95),outline=(90,60,50))
for x,y,l in near:
    g.ellipse((f(x,y)[0]-6,f(x,y)[1]-6,f(x,y)[0]+6,f(x,y)[1]+6),fill=(20,20,20));g.text((f(x,y)[0]+8,f(x,y)[1]-6),l,fill=(0,0,0))
im.save('gis/anteprima_tappa1.png');print(near)
