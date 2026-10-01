"""Estrae, per ogni città già presente nelle mappe, i quattro numeri che servono
a generare le sagome degli edifici: quota, pendenza, esposizione e rilievo.

Perché questo, se le altezze degli edifici non esistono come dato. Perché
l'altezza non è l'unica cosa che si vede in una vista 3/4: si vede anche **dove
il terreno sale e scende**, e quello è un dato pubblico, libero e preciso. Una
città su un pendio ha edifici che seguono la curva di livello e si sfalsano a
gradini; una città in piano no. Un generatore che non sa quanto scende la
strada produce un Effect.

La fonte: i **Terrarium** di AWS Open Data, derivati da SRTM, che si
prendono con una richiesta HTTP per tassello e **senza registrazione**. Sono
state verificate dieci città a mano e le quote tornano: Ferrara 4,9 m (è sotto
il livello del mare, e sotto c'è), Venezia 0,0 m, Cortina 2 150 m, Aosta 569 m,
Siracusa 6 m.

Il formato di uscita è lo stesso a delta di `dati/mappe/`, e ogni punto porta
`fonte` e `quota_fonte`: nessun numero entra nel gioco senza dire da dove viene,
come già vale per `attendibilita` e `manca` nel registro dell'anno 4.

Uso:  python3 rilievo.py            (estrae e scrive in dati/mappe/)
      python3 rilievo.py --prova    (scarica e verifica, non scrive)
"""
import json
import math
import os
import sys
import time
import urllib.error
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GIS = os.path.join(RADICE, "sorgenti", "gis")
DATI = os.path.join(RADICE, "dati", "mappe")
UA = "i-cinque-duchi/0.1 (progetto didattico per liceo; pietrofabbri)"

# risoluzione: z=12 copre circa 7 km di lato a 44° di latitudine, che e' la
# scala giusta per decidere se una citta' e' in piano o in pendio. z=14
# coprirebbe 1,8 km, che e' gia' dentro la citta' e non dice piu' nulla sulla
# pendenza media del luogo dove nascono le sagome.
ZOOM = 12
BASE = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium"
CACHE = {}

# l'encoding Terrarium: quota = (R*256 + G + B/256) - 32768, in metri
ORIGINE = 32768.0


def carica_lettore():
    sys.path.insert(0, GIS)
    import mappe_lettore
    return mappe_lettore


def deg2tile(lat, lon, z):
    n = 2.0 ** z
    xt = (lon + 180.0) / 360.0 * n
    la = math.radians(max(min(lat, 85.05), -85.05))
    yt = (1.0 - math.log(math.tan(la) + 1.0 / math.cos(la)) / math.pi) / 2.0 * n
    return int(xt), int(yt)


def pixel_dentro(lat, lon, z, tx, ty):
    """Il pixel del punto dentro il suo tassello, in 0..255.

    DIFETTO CORRETTO, e il piu' subdolo incontrato finora: si potrebbe pensare
    di prendere il tassello a livello z+4 e usarne il resto della divisione per
    16, e sembra funzionare — ma `x mod 16` e' l'indice di un **tassello** a
    livello z+4, non di un **pixel**: il tassello ha 256 pixel, non 16. Il
    risultato era leggere un punto diverso da quello richiesto, e i numeri
    erano sbagliati di qualche centinaio di metri senza che nulla lo
    segnalasse. Il Duomo di Firenze leggeva 254 m (e' a 50) e piazza Grande ad
    Aosta 1 085 m (e' a 583).

    Il metodo che funziona e' diretto: si calcola il pixel **globale** a quel
    livello e si sottrae l'origine del tassello. E' stato verificato leggendo il
    profilo del tassello: la riga del Duomo dà 57-72 m e quella di Aosta 581-583 m.
    """
    lato = 2.0 ** z * 256.0
    gx = (lon + 180.0) / 360.0 * lato
    la = math.radians(max(min(lat, 85.05), -85.05))
    gy = (1.0 - math.asinh(math.tan(la)) / math.pi) / 2.0 * lato
    return int(gx) - tx * 256, int(gy) - ty * 256


def metri_per_pixel(lat, z):
    """A quella latitudine un pixel copre questa distanza, in metri."""
    return 156543.03392 * math.cos(math.radians(lat)) / 2.0 ** z


def scarica_tassello(x, y, z, tentativi=5):
    """Un tassello, con pazienza per i 429. Una risposta che non arriva non
    viene mai registrata come quota zero: si solleva, e la citta' resta senza
    dato. Uno zero a Ferrara o a Venezia sarebbe un dato falso, e questa e' la
    citta' di cui il progetto tratta."""
    chiave = (z, x, y)
    if chiave in CACHE:
        return CACHE[chiave]
    url = f"{BASE}/{z}/{x}/{y}.png"
    from PIL import Image
    import io
    for k in range(tentativi):
        try:
            r = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(r, timeout=60) as f:
                grezzi = f.read()
            im = Image.open(io.BytesIO(grezzi))
            im.load()
            px = im.convert("RGB")
            griglia = []
            for j in range(px.height):
                riga = []
                for i in range(px.width):
                    R, G, B = px.getpixel((i, j))
                    riga.append((R * 256 + G + B / 256.0) - ORIGINE)
                griglia.append(riga)
            CACHE[chiave] = griglia
            return griglia
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 5 * (k + 1)
                print("   %d su %d/%d, attendo %.0f s" % (e.code, z, x, att),
                      flush=True)
                time.sleep(att)
                continue
            raise SystemExit("tassello %d/%d/%d: HTTP %d" % (z, x, y, e.code))
        except Exception as e:
            if k == tentativi - 1:
                raise SystemExit("tassello %d/%d/%d: %s" % (z, x, y, e))
            time.sleep(3 * (k + 1))
    raise SystemExit("tassello %d/%d/%d non ottenuto" % (z, x, y))


def misura(lat, lon):
    """I quattro numeri. None significa: nessun dato, non uno zero."""
    x, y = deg2tile(lat, lon, ZOOM)
    g = scarica_tassello(x, y, ZOOM)
    h, w = len(g), len(g[0])
    # il pixel esatto della citta', non il centro del tassello: a z=12 il centro
    # puo' distare 3 km dal pin, e su un pendio 3 km sono 300 metri
    i, j = pixel_dentro(lat, lon, ZOOM, x, y)
    if not (0 <= i < w and 0 <= j < h):
        return None

    # NON si legge un solo pixel. Il confronto con altitudini note ha mostrato
    # che il singolo pixel e' inaffidabile: il Duomo di Firenze leggeva 257 m a
    # 700 metri dal Ponte Vecchio, che leggeva 59 m; piazza Grande ad Aosta
    # leggeva 1 086 m in una valle che e' a 583 m. Sono i vuoti del SRTM
    # riempiti male, e in citta' accadono anche perche' gli edifici alti vengono
    # interpolati come se fossero rilievo. Un edificio appoggiato su quei numeri
    # sorgerebbe a 257 metri a Firenze, e si vedrebbe.
    # La mediana su 7x7 pixel (circa 130 metri) butta via i picchi e tiene il
    # valore vero: e' il filtro che va bene quando il dato ha dei vuoti.
    RAGGIO = 3
    finestra = []
    for jj in range(max(0, j - RAGGIO), min(h, j + RAGGIO + 1)):
        for ii in range(max(0, i - RAGGIO), min(w, i + RAGGIO + 1)):
            finestra.append(g[jj][ii])
    finestra.sort()
    mediana = finestra[len(finestra) // 2]
    scarto = finestra[-1] - finestra[0]

    quota = mediana

    m = metri_per_pixel(lat, ZOOM)
    # pendenza media su una finestra di 5 pixel: la differenza di quota lungo
    # l'ascendente e quella lungo l'ascissa danno il gradiente
    def mediana(sotto):
        sotto = sorted(sotto)
        return sotto[len(sotto) // 2]

    passi = 5
    # il gradiente prende la mediana su strisce, non su singoli pixel: se il
    # gradiente non usa la mediana, un solo vuoto lo rovina tutto
    righe = list(range(max(0, j - RAGGIO), min(h, j + RAGGIO + 1)))
    colonne = list(range(max(0, i - RAGGIO), min(w, i + RAGGIO + 1)))
    gx = mediana([g[jj][min(i + passi, w - 1)] for jj in righe]) - \
        mediana([g[jj][max(i - passi, 0)] for jj in righe])
    gy = mediana([g[min(j + passi, h - 1)][ii] for ii in colonne]) - \
        mediana([g[max(j - passi, 0)][ii] for ii in colonne])
    dist = 2 * passi * m
    pend = math.hypot(gx, gy) / dist * 1000.0          # metri per chilometro
    if abs(gx) < 1e-6 and abs(gy) < 1e-6:
        espo = 0.0                                    # pianura: nessuna esposizione
    else:
        espo = (math.degrees(math.atan2(-gx, gy)) + 360.0) % 360.0
    valori = [r for riga in g for r in riga]
    return {"quota": round(quota, 1),
            "pend": round(pend, 1),
            "espo": round(espo, 1),
            "rel": round(max(valori) - min(valori), 1),
            "scarto": round(scarto, 1)}


def citta_da(percorso):
    lettore = carica_lettore()
    _, punti = lettore.leggi(percorso)
    return punti


def scrivi(path, q, punti):
    """Formato a delta identico a quello delle altre mappe."""
    with open(path, "w", encoding="utf-8") as f:
        f.write('{"q":%g,"f":[],' % q)
        f.write('"p":[')
        for n, (props, x, y) in enumerate(punti):
            if n:
                f.write(",")
            f.write(json.dumps([props, round(x, 5), round(y, 5)],
                               ensure_ascii=False, separators=(",", ":")))
        f.write("]}")


if __name__ == "__main__":
    solo_prova = "--prova" in sys.argv

    GRUPPI = [("penisola_10_citta", os.path.join(DATI, "penisola_10_citta.json")),
              ("europa_50_citta", os.path.join(DATI, "europa_50_citta.json"))]

    for nome, percorso in GRUPPI:
        if not os.path.exists(percorso):
            print("salto: manca", percorso)
            continue
        città = citta_da(percorso)
        print("%s: %d città" % (nome, len(città)), flush=True)

        punti = []
        senza = 0
        for n, (props, x, y) in enumerate(città, 1):
            nome_c = props[0] if isinstance(props, list) else props
            try:
                m = misura(y, x)
            except SystemExit as e:
                print("  interrotto:", e)
                break
            if not m:
                senza += 1
                continue
            punti.append(([nome_c, m["quota"], m["pend"], m["espo"], m["rel"],
                           "terrarium/SRTM", "misurata"], x, y))
            if n % 40 == 0:
                print("  %d/%d  (tasselli in cache: %d)"
                      % (n, len(città), len(CACHE)), flush=True)
            time.sleep(0.12)

        print(" misurate %d, saltate %d, tasselli scaricati %d"
              % (len(punti), senza, len(CACHE)))
        if not solo_prova and punti:
            uscita = os.path.join(DATI, "rilievo_%s.json" % nome)
            scrivi(uscita, 1.0, punti)
            print(" scritto %s (%d byte)" % (uscita, os.path.getsize(uscita)))
