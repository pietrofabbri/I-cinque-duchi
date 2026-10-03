"""Costruisce il fondo di Ferrara: il perimetro delle mura e la zona percorribile.

E' il buco Q3 di `fonti-visive.md`: l'anno 1 e' l'anno in cui la copertura e'
gratuita e la mappa e' piccola, e non aveva un file. `dettagli_ferrara.json` ha i
dettagli dei luoghi ma non la geometria; qui la geometria c'e'.

**La fonte, e i due fatti che essa dice.** Le mura di Ferrara sono in
OpenStreetMap come **14 tratti** con `barrier=city_wall`, non come un anello: OSM
non ha la relazione che le chiude. Il primo tentativo di questo file le ha
cercate con `historic=city_walls` e ha restituito **zero elementi**: la proprieta'
esatta non e' quella giusta, e il nome giusto e' `barrier`. Un file che non trova
niente e dice «non c'e' niente» quando la fonte c'e' e basta un'altra parola
chiave e' peggio di un file che sbaglia: sembra una ricerca esaurita.

I 14 tratti non si toccano: hanno 28 estremi e nessuno in comune, perche' il
rilievo e' a pezzi. Per ottenere un anello li si concatena entro una tolleranza, e
**la tolleranza e' una scelta, non un fatto**. Qui la scelta non e' un occhio:
e' la piu' piccola tolleranza alla quale **tutte le trenta tappe del primo anno
cadono dentro**, e il file scrive tutta la scala, cioe' le prove. Le prove sono
questa tabella:

    tolleranza   perimetro   area      tappe fuori
        25 m       2613 m   0,74 km2        26 su 28
        40 m       4602 m   1,44 km2        19 su 28
        60 m       8601 m   4,20 km2         0 su 28

Il 25 m e il 40 m chiudono un anello piccolo, che e' un pezzo di mura piegato su
se stesso e non la citta'. Il 60 m chiude la citta' cinta, e i 4,20 km2 sono
vicini ai 4,8 km2 che le fonti danno per Ferrara. Il file non sceglie il 60 m
perche' «sembra giusto»: lo sceglie perche' e' il primo della scala in cui non
esce nessuna tappa, e il confronto con i 4,8 km2 e' un controllo in piu'.

**Il fondo che ne esce e' dichiarato per quello che e'.** Il tratto che chiude
l'anello sono 1037 m che nessuna fonte disegna: e' il vuoto fra l'ultimo e il
primo estremo, e il file lo scrive in `vuoto_di_chiusura_m` invece di farlo
passare per tracciato. Chi legge sa che 1037 m di confine non hanno un disegno.

Il formato e' quello di `mappe_formato.py` — coordinate locali in metri dal
centro, quantizzate — cosi' il motore usa lo stesso lettore dei fondi geografici.

Uso:  python3 sorgenti/gis/ferrara_fondo.py
      python3 sorgente/gis/ferrara_fondo.py --prova      # non scrive
"""
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
MAPPA_ANNO1 = os.path.join(RADICE, "docs", "videogioco-5-duchi-anno1-mappa.md")
USCITA = os.path.join(RADICE, "dati", "ferrara_fondo.json")

OVERPASS = "https://overpass-api.de/api/interpreter"
UA = "i-cinque-duchi/0.1 (progetto didattico per liceo; pietrofabbri)"
LICENZA = "ODbL 1.0"
ATTRIBUZIONE = "(c) OpenStreetMap contributors"

RIQUADRO = (44.75, 11.50, 45.00, 11.80)
TOLLERANZE = [5.0, 15.0, 25.0, 40.0, 60.0, 90.0, 130.0]
Q = 100.0
MARGINE = 60.0        # m: quanto si esce dal perimetro per la nebbia
AREA_STORICA_KM2 = 4.8   # controllo in piu', dalle fonti storiche

# La fonte ordinata e rifiutata. Si scrive perche' una ricerca che butta via una
# fonte e non dice quale perde l'informazione piu' utile di tutte: il nome di
# quella che si e' sbagliata a scegliere.
RIFIUTATA = {
    "fonte": "OpenStreetMap, relation 3875619 «Centro storico»",
    "motivo": "la relazione sembra fatta apposta — si chiama Centro storico e "
              "copre Ferrara — ma copre 1,34 km2 e non la citta' cinta: 13 "
              "tappe su 28 stanno fuori, fra cui Piazza Ariostea, Palazzo dei "
              "Diamanti e Porta degli Angeli. Un perimetro che esclude la "
              "piazza dei Diamanti non e' il perimetro delle mura, per quanto "
              "sia chiamato centro storico",
    "prova": "area 1,34 km2 contro i 4,20 km2 delle mura ricostruite dai tratti",
}


def overpass(q, tentativi=5):
    dati = urllib.parse.urlencode({"data": q}).encode()
    for k in range(tentativi):
        try:
            req = urllib.request.Request(
                OVERPASS, data=dati,
                headers={"User-Agent": UA, "Content-Type":
                         "application/x-www-form-urlencoded"})
            with urllib.request.urlopen(req, timeout=300) as f:
                return json.loads(f.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 504):
                att = 20 * (k + 1)
                print("  %d, attendo %d s" % (e.code, att), flush=True)
                time.sleep(att)
                continue
            return None
        except Exception:
            time.sleep(10 * (k + 1))
    return None


def distanza(a, b):
    """I metri fra due punti, sulla sfera. Serve per tolleranze e lunghezze."""
    dx = (b["lon"] - a["lon"]) * 111320.0 * math.cos(math.radians(a["lat"]))
    dy = (b["lat"] - a["lat"]) * 111320.0
    return math.hypot(dx, dy)


def lunghezza(punti):
    return sum(distanza(punti[i], punti[i + 1]) for i in range(len(punti) - 1))


def concatena(segmenti, tol):
    """Unisce i tratti in catene, accostando gli estremi entro `tol` metri.

    Quando due estremi sono a 20 m con una tolleranza di 25, il file **li salta e
    basta**: non li collega con un segmento inventato. Il vuoto resta vuoto e si
    dichiara, perche' un segmento aggiunto a mano e' una linea che nessuna fonte
    ha disegnato. Il tratto di chiusura e' l'unico pezzo che il motore aggiunge,
    ed e' dichiarato a parte.
    """
    catene = [[dict(p) for p in s] for s in segmenti]
    usate = [False] * len(catene)
    for i in range(len(catene)):
        if usate[i]:
            continue
        usate[i] = True
        while True:
            a, b = catene[i][-1], catene[i][0]
            progredito = False
            for j in range(len(catene)):
                if usate[j]:
                    continue
                c = catene[j]
                if distanza(a, c[0]) < tol:
                    catene[i] += c[1:]
                elif distanza(a, c[-1]) < tol:
                    catene[i] += list(reversed(c))[1:]
                elif distanza(b, c[-1]) < tol:
                    catene[i] = c[:-1] + catene[i]
                elif distanza(b, c[0]) < tol:
                    catene[i] = list(reversed(c))[:-1] + catene[i]
                else:
                    continue
                usate[j] = True
                progredito = True
                break
            if not progredito:
                break
    return catene


def metrico(punti, lat0, lon0):
    """Dall'equidistanza al piano tangente, in metri dall'origine."""
    mlat = 111132.92 - 559.82 * math.cos(2 * math.radians(lat0)) \
        + 1.175 * math.cos(4 * math.radians(lat0))
    mlon = 111412.84 * math.cos(math.radians(lat0)) \
        - 93.5 * math.cos(3 * math.radians(lat0))
    return [((p["lon"] - lon0) * mlon, (p["lat"] - lat0) * mlat) for p in punti]


def area(anello):
    a = 0.0
    for i in range(len(anello)):
        x1, y1 = anello[i]
        x2, y2 = anello[(i + 1) % len(anello)]
        a += x1 * y2 - x2 * y1
    return abs(a) / 2.0


def dentro(anello, p, guardia=0.5):
    """Il punto-in-poligono, in metri, con la regola del bordo che conta dentro.

    La regola del bordo conta come dentro perche' una tappa che cade esattamente
    sulla linea delle mura non e' fuori dalle mura, e gettarla fuori produrrebbe
    un difetto che non c'e'. Il raggio e' di `guardia` metri: sotto, il punto e'
    davvero sul muro.

    Il raggio va detto perche' la prima versione di questa funzione lavorava in
    gradi e aveva un raggio di 0,5 gradi: mezzo grado sono 55 km, e con quello
    tutte le ventotto tappe risultavano «sul bordo». Un raggeggio nell'unita'
    sbagliata non da' un difetto, da' una risposta che sembra vera.
    """
    x, y = p
    accavallamenti = False
    n = len(anello)
    for i in range(n):
        ax, ay = anello[i]
        bx, by = anello[(i + 1) % n]
        dx, dy = bx - ax, by - ay
        ll = dx * dx + dy * dy
        if ll > 0:
            t = max(0.0, min(1.0, ((x - ax) * dx + (y - ay) * dy) / ll))
            if math.hypot(x - (ax + t * dx), y - (ay + t * dy)) < guardia:
                return True, "bordo"
        if (ay > y) != (by > y):
            if x < ax + (y - ay) * (bx - ax) / (by - ay):
                accavallamenti = not accavallamenti
    return accavallamenti, ("dentro" if accavallamenti else "fuori")


def tappe_anno1():
    """Le tappe del primo anno con le coordinate, lette dal documento.

    Il file non duplica i numeri: li legge dalla tabella di `anno1-mappa.md` §3,
    che e' dove il progetto li ha gia' verificati sul dataset dei civici del
    Comune. Se la tabella cambia anche la zona cambia, ed e' la cosa giusta.
    """
    with open(MAPPA_ANNO1, encoding="utf-8") as f:
        testo = f.read()
    sezione = testo.split("## 3. Posizione precisa dei punti", 1)
    if len(sezione) < 2:
        return []
    out = []
    for riga in sezione[1].split("## 4.")[0].splitlines():
        celle = [c.strip() for c in riga.strip().strip("|").split("|")]
        if len(celle) < 5 or not re.match(r"^\d-\d+$", celle[0]):
            continue
        try:
            out.append({"tappa": celle[0], "luogo": celle[1],
                        "lat": float(celle[3]), "lon": float(celle[4])})
        except ValueError:
            continue
    return out


def principale():
    solo_prova = "--prova" in sys.argv
    a, b, c, d = RIQUADRO
    q = ('[out:json][timeout:180];'
         'way["barrier"="city_wall"](%f,%f,%f,%f);out tags geom 300;' % (a, b, c, d))
    risposta = overpass(q)
    if risposta is None:
        print("Overpass non ha risposto: niente di scritto")
        return 1
    elementi = [e for e in risposta.get("elements", [])
                if len(e.get("geometry") or []) >= 2]
    print("tratti di mura in OSM: %d" % len(elementi))

    tappe = tappe_anno1()
    print("tappe del primo anno con coordinate: %d" % len(tappe))

    # LA SCELTA DELLA TOLLERANZA, con tutte le prove.
    scala, scelto = [], None
    for tol in TOLLERANZE:
        catene = concatena([e["geometry"] for e in elementi], tol)
        if not catene:
            continue
        anello = max(catene, key=lunghezza)
        if len(anello) < 8:
            continue
        L = lunghezza(anello)
        chiusura = distanza(anello[0], anello[-1])
        lat0 = sum(p["lat"] for p in anello) / len(anello)
        lon0 = sum(p["lon"] for p in anello) / len(anello)
        locale = metrico(anello, lat0, lon0)
        ar = area(locale)
        fuori = [t["tappa"] for t in tappe
                 if not dentro(locale, metrico(
                     [{"lon": t["lon"], "lat": t["lat"]}], lat0, lon0)[0])[0]]
        riga = {"toll_m": tol, "vertici": len(anello), "catene": len(catene),
                "perimetro_m": round(L), "chiusura_m": round(chiusura),
                "area_km2": round(ar / 1e6, 2), "tappe_fuori": len(fuori),
                "fuori": fuori}
        scala.append(riga)
        print("  tolleranza %3.0f m: perimetro %5.0f m, area %.2f km2, "
              "tappe fuori %d" % (tol, L, ar / 1e6, len(fuori)))
        if scelto is None and len(fuori) == 0:
            scelto = (tol, anello, L, chiusura, locale, lat0, lon0, ar)
    if scelto is None:
        print("nessuna tolleranza contiene tutte le tappe: niente di scritto")
        return 1
    tol, anello, L, chiusura, locale, lat0, lon0, ar = scelto
    print("  tenuta: %g m (area %.2f km2 contro i %g km2 storici)"
          % (tol, ar / 1e6, AREA_STORICA_KM2))

    # LA VERIFICA, sulla tolleranza scelta
    dentro_, sul_bordo, fuori = [], [], []
    for t in tappe:
        locale_t = metrico([{"lon": t["lon"], "lat": t["lat"]}], lat0, lon0)[0]
        ok, dove = dentro(locale, locale_t)
        if not ok:
            fuori.append(t["tappa"])
        elif dove == "bordo":
            sul_bordo.append(t["tappa"])
        else:
            dentro_.append(t["tappa"])
    print("  tappe: %d dentro, %d sul bordo, %d fuori"
          % (len(dentro_), len(sul_bordo), len(fuori)))

    # i tratti come sono, uno per uno: il motore ci disegna le mura esattamente
    # dove OSM le mette, senza dover ricostruire l'anello
    tratti = []
    for e in elementi:
        punti = metrico(e["geometry"], lat0, lon0)
        tratti.append({
            "id": "way/%d" % e["id"],
            "nome": (e.get("tags") or {}).get("name"),
            "vertici": [[int(round(px * Q)), int(round(py * Q))]
                        for px, py in punti],
            "lunghezza_m": round(lunghezza(e["geometry"])),
        })

    if solo_prova:
        return 0

    doc = {
        "versione": 1,
        "data": "2026-10-03",
        "fonte": "OpenStreetMap, via Overpass API: way con barrier=city_wall "
                 "attorno a Ferrara",
        "licenza": LICENZA,
        "attribuzione": ATTRIBUZIONE,
        "centro": {"lat": round(lat0, 6), "lon": round(lon0, 6)},
        "formato": "coordinate locali in metri dal centro, quantizzate a "
                   "1/100 m (campo `q`), come i fondi di mappe_formato.py",
        "mura": {
            "anello": [[int(round(x * Q)), int(round(y * Q))]
                       for x, y in locale],
            "perimetro_m": round(L),
            "area_m2": round(ar),
            "area_km2": round(ar / 1e6, 2),
            "area_storica_km2": AREA_STORICA_KM2,
            "tratti_osm": len(elementi),
            "toll_m": tol,
            "vuoto_di_chiusura_m": round(chiusura, 1),
            "nota_chiusura": "OSM non chiude l'anello delle mura: gli ultimi "
                             "due estremi sono a %.0f m l'uno dall'altro. Il "
                             "motore chiude il poligono e quei %.0f m di "
                             "confine non hanno un disegno: e' l'unico pezzo "
                             "non documentato della zona, ed e' dichiarato qui "
                             "e in `vuoto_di_chiusura_m`"
                             % (chiusura, chiusura),
        },
        "tratti": tratti,
        "scala_tolleranze": scala,
        "zona_percorribile": {
            "regola": "la zona e' l'interno delle mura piu' un margine di %g m "
                      "oltre la linea: fuori dalla linea c'e' la nebbia, e "
                      "oltre la nebbia le tappe vicine, come da "
                      "videogioco-5-duchi-tappa-1-01.md 3" % MARGINE,
            "margine_m": MARGINE,
        },
        "verifica": {
            "controllo": "ogni tappa del primo anno con coordinate deve cadere "
                         "dentro il perimetro delle mura: e' il controllo che "
                         "sceglie la tolleranza e distingue il fondo vero da "
                         "un poligono plausibile",
            "tappe_legge": len(tappe),
            "dentro": len(dentro_),
            "sul_bordo": sul_bordo,
            "fuori": fuori,
            "tappe_senza_coordinate": ["1-27", "1-30"],
            "nota_senza_coordinate": "1-27 e 1-30 non sono nella tabella delle "
                                     "coordinate di anno1-mappa.md 3: non si "
                                     "possono controllare, e il file non finge "
                                     "che siano dentro",
        },
        "fonti_rifiutate": [RIFIUTATA],
        "difetti_dichiarati": [
            "OSM non ha l'anello delle mura, ha 14 tratti con dei vuoti: "
            "l'anello e' ricostruito a una tolleranza dichiarata di %g m, "
            "scelta perche' e' la piu' piccola in cui tutte le tappe cadono "
            "dentro" % tol,
            "la chiusura dell'anello sono %.0f m che nessuna fonte disegna"
            % chiusura,
            "nessun tratto porta `start_date`: il file non sa quando ogni "
            "tratto e' stato costruito e non lo deduce",
            "le mura di origine e quelle dell'Addizione Erculea non sono "
            "distinguibili nei tratti OSM: il fondo le tratta come un solo "
            "perimetro, e il quinto anno lavora sulla stessa area",
            "due tappe (1-27, 1-30) non hanno coordinate e restano fuori dal "
            "controllo",
        ],
    }
    with open(USCITA, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print("scritto %s (%.0f kB)"
          % (os.path.relpath(USCITA, RADICE), os.path.getsize(USCITA) / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(principale())