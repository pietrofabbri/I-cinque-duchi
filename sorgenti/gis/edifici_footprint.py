"""Estrae da OpenStreetMap le sagome degli edifici attorno ai luoghi del gioco.

E' il buco piu' grande dei cinque che `fonti-visive.md` 3.2 dichiara: la fonte
(OSM, ODbL) era autorizzata e il file non esisteva. Questo e' quel file.

**Il problema che questo file deve risolvere bene e' l'altezza, non la forma.**
La forma si scarica: il poligono della facciata e' li'. L'altezza no, e OSM la
dichiara raramente. Nella prova sulla piazza della Cattedrale, su 201 edifici
36 hanno `height` e 7 hanno `building:levels`: circa un quinto. Su gli altri
quattro quinti **non si sa quanto sono alti**, e la regola del progetto e' gia'
scritta in `fonti-visive.md` 4.3: «una forma che non e' verificata non si
disegna». Qui la traduzione e' che un edificio senza altezza esce con
`altezza: null` e `fonte_altezza: "assente"`, e il motore ne fa un volume
neutro — non un cubo alto a caso, che sarebbe un'edificio inventato.

Le tre fonti di altezza, in quest'ordine di affidabilita', e ognuna dichiarata:

  osm_height    il tag `height`, in metri: e' la misura, quando c'e'
  osm_levels    `building:levels` moltiplicato per `M_PER_PIANO`, che e' una
                **costante dichiarata** di questo file (3,2 m) e non un fatto:
                un piano di un palazzo di mattoni e' piu' alto di un piano di
                legno, e il file non lo sa. Per questo `fonte_altezza` dice
                `osm_levels` e non `osm_height`: chi legge sa che quel numero
                e' una stima dichiarata
  assente       niente: `altezza: null`, e il motore disegna un volume neutro

**Cosa si tiene e cosa si scarta.** Un intorno di 250 m attorno al pin restituisce
centinaia di edifici, quasi tutti anonimi. Il file ne tiene i **significativi**,
con una regola dichiarata: ha un nome, ha un `wikidata`, ha un'altezza o dei
piani, e' un edificio di una categoria che il gioco sa riconoscere (chiese,
castelli, palazzi, torri), oppure ha un'area maggiore di `AREA_MINIMA`. Il resto
e' volume neutro anonimo e non serve a niente: il file scrive **quanti ne ha
scartati e perche'**, perche' una soglia non dichiarata e' un difetto che nessuno
vede.

La geometria si semplifica con `dp_chiuso` di `mappe_formato.py`, che gia' sa
chiudere gli anelli senza spostarli, e si scrive nel formato delta dello stesso
file: il motore ha gia' un lettore per quel formato e non ne serve un secondo.

La licenza non e' una formalita': OSM e' ODbL, quindi il file porta
`licenza` e `attribuzione` in testa, e `FONTI-E-LICENZE.md` li deve citare.

Uso:  python3 sorgenti/gis/edifici_footprint.py
      python3 sorgenti/gis/edifici_footprint.py --prova          # non scrive
      python3 sorgenti/gis/edifici_footprint.py --luogo Ferrara  # un posto solo
"""
import json
import math
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mappe_formato import dp_chiuso                               # noqa: E402

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
LUOGHI = os.path.join(RADICE, "dati", "luoghi_gioco.json")
USCITA = os.path.join(RADICE, "dati", "edifici_footprint.json")

OVERPASS = "https://overpass-api.de/api/interpreter"
UA = "i-cinque-duchi/0.1 (progetto didattico per liceo; pietrofabbri)"
LICENZA = "ODbL 1.0"
ATTRIBUZIONE = "(c) OpenStreetMap contributors"

RAGGIO_M = 250.0        # quanto intorno al pin si guarda
M_PER_PIANO = 3.2       # costante dichiarata, non un fatto storico
AREA_MINIMA = 120.0     # m^2: sotto, e' un edificio accessorio
TOLLERANZA = 1.5        # m: semplificazione della facciata
MAX_PER_LUOGO = 140     # oltre, il posto si riempie di cubi anonimi
GRUPPO = 3              # quanti luoghi per richiesta Overpass
Q = 100.0               # quantizzazione del formato delta (vedi scrivi)

# Le categorie che il gioco sa nominare. Non e' una scelta estetica: sono quelle
# per cui `dettagli_ferrara.json` e le schede degli edifici hanno una cronologia,
# e quindi un edificio senza nome ma di questa categoria ha comunque qualcosa da
# dire. Un `building=yes` anonimo non lo sa.
CATEGORIE = {
    "church": "chiesa", "cathedral": "cattedrale", "chapel": "cappella",
    "castle": "castello", "palace": "palazzo", "monastery": "monastero",
    "tower": "torre", "townhall": "palazzo_comunale", "museum": "museo",
    "theatre": "teatro", "library": "biblioteca", "university": "universita",
    "fortification": "fortificazione", "ruins": "rovina",
}


def overpass(aree, tentativi=4):
    """Gli edifici di piu' luoghi in una richiesta sola.

    Overpass vuole che non si martelli il server: 54 richieste una per una sono
    54 richieste, e si mette al sicuro. Qui ogni gruppo di `GRUPPO` luoghi viaggia
    in una richiesta sola, con le aree in unione.
    """
    parti = []
    for lat, lon, _ in aree:
        d = RAGGIO_M / 111320.0
        dlat = d * 1.0
        dlon = d / max(math.cos(math.radians(lat)), 1e-6)
        parti.append('way["building"](%f,%f,%f,%f);'
                     'relation["building"](%f,%f,%f,%f);'
                     % (lat - dlat, lon - dlon, lat + dlat, lon + dlon,
                        lat - dlat, lon - dlon, lat + dlat, lon + dlon))
    # Le aree si mettono una dopo l'altra **separate da un punto e virgola**: senza,
    # Overpass risponde 400 con «';' expected - '(' found». E' il primo tentativo
    # che si e' fermato su un errore di sintassi della ricerca, non dei dati.
    q = "[out:json][timeout:180];(\n" + "\n".join(parti) + "\n);out geom qt 2000;"
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


def overpass_spezzato(aree, prof=0):
    """Come `overpass`, ma se il server non regge il gruppo lo dimezza.

    Il primo tentativo chiedeva sei aree per volta e funzionava su tutti i gruppi
    tranne l'ultimo, che ha risposto 504 quattro volte di fila. Non era un errore
    dei dati: Overpass regge un certo carico per richiesta e basta. Qui un gruppo
    che fallisce viene chiesto in due meta', poi in quattro, e il file dice
    quanti gruppi hanno avuto bisogno dei tentativi. Un'estrazione che salta sei
    luoghi e lo dichiara sarebbe accettabile; una che salta sei luoghi **senza**
    dirlo no.
    """
    risposta = overpass(aree)
    if risposta is not None:
        return risposta, 0
    if len(aree) == 1 or prof >= 3:
        return None, prof
    meta = len(aree) // 2
    a, pa = overpass_spezzato(aree[:meta], prof + 1)
    b, pb = overpass_spezzato(aree[meta:], prof + 1)
    if a is None and b is None:
        return None, prof + 1
    return {"elements": (a or {}).get("elements", []) +
            (b or {}).get("elements", [])}, prof + 1 + pa + pb


def metri(lat0, lon0, pts):
    """Dall'equidistanza al piano, in metri, con l'origine nel pin.

    Il piano e' tangente alla sfera: a Ferrara la differenza e' di qualche
    centesimo di millimetro, ma il file lo dichiara perche' il motore usa le
    stesse coordinate per i fondi e le due cose devono combaciare.
    """
    mlat = 111132.92 - 559.82 * math.cos(2 * math.radians(lat0)) \
        + 1.175 * math.cos(4 * math.radians(lat0))
    mlon = 111412.84 * math.cos(math.radians(lat0)) \
        - 93.5 * math.cos(3 * math.radians(lat0))
    return [(round((lon - lon0) * mlon, 2), round((lat - lat0) * mlat, 2))
            for lon, lat in pts]


def area(pts):
    a = 0.0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % len(pts)]
        a += x1 * y2 - x2 * y1
    return abs(a) / 2.0


def altezza(tag):
    """L'altezza di un edificio, e **da dove viene**.

    Restituisce `(metri, fonte, livelli)`. I tre valori possono essere
    `(None, "assente", None)`: non e' un fallimento, e' la dichiarazione che
    quell'edificio non si sa quanto e' alto. La regola e' quella di
    `fonti-visive.md` 4.3.
    """
    h = (tag.get("height") or "").strip().split(";")[0].strip()
    if h:
        try:
            return float(h.rstrip("m").strip()), "osm_height", None
        except ValueError:
            pass
    lv = (tag.get("building:levels") or "").strip()
    if lv:
        try:
            n = float(lv)
            return round(n * M_PER_PIANO, 1), "osm_levels", n
        except ValueError:
            pass
    return None, "assente", None


def anello(el):
    """Il primo anello esterno di un elemento Overpass, in (lon, lat).

    Su una relazione multi-poligono Overpass con `out geom` mette i membri con
    `role: outer` in `geometry` e gli altri in nessun posto: si prende il primo
    anello con almeno tre vertici, che e' l'esterno per costruzione.
    """
    geo = el.get("geometry")
    if geo:
        return [(p["lon"], p["lat"]) for p in geo if "lon" in p]
    membri = el.get("members") or []
    for m in membri:
        g = m.get("geometry")
        if m.get("role") in ("outer", "") and g and len(g) >= 3:
            return [(p["lon"], p["lat"]) for p in g if "lon" in p]
    return []


def scegli(tag, sup):
    """Un edificio e' significativo? Tre ragioni, e si sa quale."""
    if tag.get("name") or tag.get("wikidata"):
        return "nominato"
    if sup["altezza"] is not None:
        return "altezza_dichiarata"
    cat = CATEGORIE.get((tag.get("building") or "").lower())
    if cat:
        return "categoria_" + cat
    if tag.get("heritage") or tag.get("historic"):
        return "patrimonio"
    if sup["area"] >= AREA_MINIMA:
        return "grande"
    return ""


def principale():
    solo_prova = "--prova" in sys.argv
    solo_luogo = None
    if "--luogo" in sys.argv:
        solo_luogo = sys.argv[sys.argv.index("--luogo") + 1]

    with open(LUOGHI, encoding="utf-8") as f:
        luoghi = json.load(f)["luoghi"]
    scelti = [l for l in luoghi
              if l.get("coord_stato") == "verificata" and l.get("lat") is not None
              and (solo_luogo is None or solo_luogo in l["luogo"])]

    # La ripresa esiste per una ragione concreta: Overpass risponde 504 e un
    # estrazione di 54 luoghi non finisce in un colpo. Senza ripresa si
    # ricomincerebbe da capo ogni volta che il server si stanca, e si perderebbero
    # anche i gruppi gia' fatti. Con la ripresa il file di uscita e' il punto di
    # partenza, e `--riprendi` salta i luoghi che ci sono gia'.
    gia = None
    if "--riprendi" in sys.argv and os.path.exists(USCITA):
        with open(USCITA, encoding="utf-8") as f:
            vecchio = json.load(f)
        gia = set(vecchio.get("luoghi", []))
        print("ripresa: %d luoghi gia' nel file" % len(gia))
    if gia:
        scelti = [l for l in scelti if l["luogo"] not in gia]
    print("luoghi da interrogare: %d" % len(scelti))

    edifici, scartati, per_luogo = [], {}, {}
    perduti, spezzati = [], {}
    if gia:
        edifici = vecchio.get("edifici", [])
        per_luogo = {k: v for k, v in
                     vecchio.get("riepilogo", {}).get("per_luogo", {}).items()}
        scartati = dict(vecchio.get("riepilogo", {}).get("scartati", {}))
        perduti = list(vecchio.get("luoghi_senza_edifici", []))
        spezzati = {"gruppo": vecchio.get("gruppi_spezzati", 0)}
    for i in range(0, len(scelti), GRUPPO):
        gruppo = scelti[i:i + GRUPPO]
        risposta, tentativi = overpass_spezzato(
            [(l["lat"], l["lon"], l["luogo"]) for l in gruppo])
        if tentativi:
            spezzati["gruppo"] = spezzati.get("gruppo", 0) + 1
        if risposta is None:
            perduti.append([l["luogo"] for l in gruppo])
            print("  gruppo %d: nessuna risposta (%d luoghi)"
                  % (i // GRUPPO + 1, len(gruppo)))
            continue
        for l in gruppo:
            per_luogo[l["luogo"]] = 0

        for el in risposta.get("elements", []):
            pts = anello(el)
            if len(pts) < 3:
                scartati["anello_troppo_corto"] = scartati.get(
                    "anello_troppo_corto", 0) + 1
                continue
            tag = el.get("tags") or {}
            # il piano e' locale al pin: ogni elemento e' attribuito al pin piu'
            # vicino fra quelli del gruppo, perche' Overpass non dice a quale
            # area appartiene
            l = min(gruppo, key=lambda x: (x["lat"] - pts[0][1]) ** 2
                    + ((x["lon"] - pts[0][0]) *
                       math.cos(math.radians(pts[0][1]))) ** 2)
            mp = metri(l["lat"], l["lon"], pts)
            sup = {"area": area(mp)}
            h, fonte, liv = altezza(tag)
            sup["altezza"] = h
            motivo = scegli(tag, sup)
            if not motivo:
                scartati["anonimo_e_piccolo"] = scartati.get(
                    "anonimo_e_piccolo", 0) + 1
                continue
            if sup["area"] > (math.pi * RAGGIO_M ** 2):
                scartati["fuori_raggio"] = scartati.get("fuori_raggio", 0) + 1
                continue
            per_luogo[l["luogo"]] = per_luogo.get(l["luogo"], 0) + 1

            sempl = dp_chiuso(mp, TOLLERANZA)
            if len(sempl) < 3:
                scartati["semplificato_troppo"] = scartati.get(
                    "semplificato_troppo", 0) + 1
                per_luogo[l["luogo"]] -= 1
                continue

            edifici.append({
                "luogo": l["luogo"],
                "id": "%s/%d" % (el["type"], el["id"]),
                "nome": tag.get("name"),
                "categoria": CATEGORIE.get((tag.get("building") or "").lower()),
                "wikidata": tag.get("wikidata"),
                "forma": [[round(x / Q), round(y / Q)] for x, y in sempl],
                "area_m2": round(sup["area"], 1),
                "altezza_m": sup["altezza"],
                "fonte_altezza": fonte,
                "livelli": liv,
                "perche": motivo,
                "start_date": tag.get("start_date"),
                "fonte": "openstreetmap",
            })
        print("  gruppo %d/%d: %d edifici tenuti"
              % (i // GRUPPO + 1, (len(scelti) + GRUPPO - 1) // GRUPPO,
                 len(edifici)), flush=True)
        time.sleep(2)

    # il tetto per luogo: un centro storico con 400 edifici non e' piu' un
    # ambiente, e' un muro. Il file tiene i piu' grandi e dichiara quanti sono
    # spariti, perche' il tetto e' una soglia e le soglie vanno dichiarate.
    per_id = {}
    for e in edifici:
        per_id.setdefault(e["luogo"], []).append(e)
    tenuti = []
    for luogo, lista in per_id.items():
        lista.sort(key=lambda e: -e["area_m2"])
        tenuti.extend(lista[:MAX_PER_LUOGO])
        if len(lista) > MAX_PER_LUOGO:
            scartati["oltre_tetto_luogo"] = scartati.get(
                "oltre_tetto_luogo", 0) + len(lista) - MAX_PER_LUOGO
    tenuti.sort(key=lambda e: (e["luogo"], e["id"]))

    per_origine = {"con_altezza": 0, "da_piani": 0, "senza_altezza": 0}
    for e in tenuti:
        if e["fonte_altezza"] == "osm_height":
            per_origine["con_altezza"] += 1
        elif e["fonte_altezza"] == "osm_levels":
            per_origine["da_piani"] += 1
        else:
            per_origine["senza_altezza"] += 1

    print("\nedifici tenuti: %d su %d luoghi" % (len(tenuti), len(per_luogo)))
    if perduti:
        print("  luoghi perduti (dichiarati): %s"
              % ", ".join(x for g in perduti for x in g))
    print("  altezza: %d con height, %d da levels (stima dichiarata), "
          "%d senza altezza (volume neutro)"
          % (per_origine["con_altezza"], per_origine["da_piani"],
             per_origine["senza_altezza"]))
    print("  scartati: %s" % (", ".join("%s %d" % kv for kv in
                                       sorted(scartati.items())) or "nessuno"))
    if solo_prova:
        return 0

    doc = {
        "versione": 1,
        "data": "2026-10-03",
        "fonte": "OpenStreetMap, via Overpass API",
        "licenza": LICENZA,
        "attribuzione": ATTRIBUZIONE,
        "nota_licenza": "ODbL e' copyleft: se il gioco riusa queste sagome "
                        "l'attribuzione va tenuta anche nei materiali derivati. "
                        "FONTI-E-LICENZE.md la cita",
        "formato": "coordinate locali in metri dal pin, quantizzate a 1/100 m "
                   "(campo `q`), e semplificate con tolleranza %.1f m. Il "
                   "formato e' quello di mappe_formato.py, che il motore gia' "
                   "sa leggere" % TOLLERANZA,
        "regole": {
            "raggio_m": RAGGIO_M,
            "m_per_piano": M_PER_PIANO,
            "area_minima_m2": AREA_MINIMA,
            "tetto_per_luogo": MAX_PER_LUOGO,
            "significativo": "ha un nome, ha un wikidata, ha un'altezza o dei "
                             "piani, e' di una categoria che il gioco sa "
                             "nomiare, e' patrimonio, oppure ha un'area "
                             "maggiore di area_minima_m2",
        },
        "altezza": {
            "principio": "un'altezza non dichiarata non si stima: l'edificio "
                         "esce con altezza_m null e il motore ne fa un volume "
                         "neutro, che e' la regola di fonti-visive.md 4.3",
            "fonti": {"osm_height": "il tag height: e' la misura",
                      "osm_levels": "building:levels per m_per_piano: e' una "
                                    "stima dichiarata, non una misura",
                      "assente": "nessuna delle due: volume neutro"},
        },
        "luoghi": sorted(per_luogo),
        "luoghi_senza_edifici": perduti,
        "gruppi_spezzati": spezzati.get("gruppo", 0),
        "edifici": tenuti,
        "riepilogo": {
            "edifici": len(tenuti),
            "luoghi": len(per_luogo),
            "per_luogo": per_luogo,
            "altezza": per_origine,
            "scartati": scartati,
        },
    }
    with open(USCITA, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, separators=(",", ":"))
    print("scritto %s (%.0f kB)"
          % (os.path.relpath(USCITA, RADICE), os.path.getsize(USCITA) / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(principale())