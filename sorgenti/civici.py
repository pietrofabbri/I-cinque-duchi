# Lettura shapefile punti + dbf senza librerie esterne; conversione EPSG:3003 (Monte Mario / Italy 1) -> WGS84
import struct, math
B="/mnt/user-data/uploads/OPENDATA_CIVICI_preview/OPENDATA_CIVICI_previewPoint"
def read_dbf(path):
    f=open(path,'rb'); h=f.read(32); n=struct.unpack('<I',h[4:8])[0]; hl,rl=struct.unpack('<HH',h[8:12])
    fields=[]
    while True:
        d=f.read(32)
        if d[0]==0x0D: break
        fields.append((d[:11].split(b'\0')[0].decode(),d[11:12].decode(),d[16]))
    f.seek(hl); rows=[]
    for i in range(n):
        rec=f.read(rl); p=1; row={}
        for name,t,l in fields:
            row[name]=rec[p:p+l].decode('latin1').strip(); p+=l
        rows.append(row)
    return fields,rows
def read_shp_points(path):
    f=open(path,'rb'); f.seek(100); pts=[]
    while True:
        h=f.read(8)
        if len(h)<8: break
        num,clen=struct.unpack('>ii',h); c=f.read(clen*2); st=struct.unpack('<i',c[:4])[0]
        pts.append(struct.unpack('<dd',c[4:20]) if st==1 else None)
    return pts
def tm_inverse(E,N,a=6378388.0,f=1/297.0,lon0=9.0,k0=0.9996,FE=1500000.0):
    e2=f*(2-f); ep2=e2/(1-e2); x=(E-FE)/k0; M=N/k0
    mu=M/(a*(1-e2/4-3*e2**2/64-5*e2**3/256)); e1=(1-math.sqrt(1-e2))/(1+math.sqrt(1-e2))
    p1=mu+(3*e1/2-27*e1**3/32)*math.sin(2*mu)+(21*e1**2/16-55*e1**4/32)*math.sin(4*mu)+(151*e1**3/96)*math.sin(6*mu)+(1097*e1**4/512)*math.sin(8*mu)
    C1=ep2*math.cos(p1)**2; T1=math.tan(p1)**2; N1=a/math.sqrt(1-e2*math.sin(p1)**2); R1=a*(1-e2)/(1-e2*math.sin(p1)**2)**1.5; D=x/N1
    lat=p1-(N1*math.tan(p1)/R1)*(D**2/2-(5+3*T1+10*C1-4*C1**2-9*ep2)*D**4/24+(61+90*T1+298*C1+45*T1**2-252*ep2-3*C1**2)*D**6/720)
    lon=math.radians(lon0)+(D-(1+2*T1+C1)*D**3/6+(5-2*C1+28*T1-3*C1**2+8*ep2+24*T1**2)*D**5/120)/math.cos(p1)
    return lat,lon
def geo2ecef(lat,lon,a,f,h=0):
    e2=f*(2-f); N=a/math.sqrt(1-e2*math.sin(lat)**2)
    return ((N+h)*math.cos(lat)*math.cos(lon),(N+h)*math.cos(lat)*math.sin(lon),(N*(1-e2)+h)*math.sin(lat))
def ecef2geo(X,Y,Z,a=6378137.0,f=1/298.257223563):
    e2=f*(2-f); lon=math.atan2(Y,X); p=math.hypot(X,Y); lat=math.atan2(Z,p*(1-e2))
    for _ in range(10):
        N=a/math.sqrt(1-e2*math.sin(lat)**2); lat=math.atan2(Z+e2*N*math.sin(lat),p)
    return math.degrees(lat),math.degrees(lon)
def to_wgs84(E,N):
    lat,lon=tm_inverse(E,N); X,Y,Z=geo2ecef(lat,lon,6378388.0,1/297.0)
    tx,ty,tz=-104.1,-49.1,-9.9; rx,ry,rz=[math.radians(s/3600) for s in (0.971,-2.917,0.714)]; s=-11.68e-6
    # position vector convention (EPSG 1660 usa coordinate frame? il WKT usa la convenzione Bursa-Wolf/position vector)
    X2=tx+(1+s)*(X-rz*Y+ry*Z); Y2=ty+(1+s)*(rz*X+Y-rx*Z); Z2=tz+(1+s)*(-ry*X+rx*Y+Z)
    return ecef2geo(X2,Y2,Z2)
if __name__=="__main__":
    fl,rows=read_dbf(B+".dbf"); pts=read_shp_points(B+".shp")
    print(fl[:12]); print(len(rows),len(pts)); print(rows[0],pts[0])
    import json; json.dump(dict(rows=rows,pts=pts),open("/home/claude/duchi/civici_cache.json","w"))
