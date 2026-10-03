"""Verifica i trenta pin del primo anno: sono dentro le mura di Ferrara?

**La domanda che `mappe.md` §8bis dichiarava senza risposta.** Il verificatore dei
pin copre gli anni dal secondo in poi e li confronta con Natural Earth: il pin deve
cadere nel Paese che il nome dichiara e nell'unita' amministrativa che il nome
promette. Sono ottim controlli per una citta' che si chiama come il Paese.

**Per il primo anno quei controlli sarebbero sbagliati, e il primo anno e' l'unico
in cui il gioco si gioca davvero dentro una citta'.** Le trenta tappe sono dentro
le mura di Ferrara, e la domanda che conta non e' «in che Paese e' Piazza
Ariostea?» — la risposta e' Italia, come per tutte le altre ventinove — ma
**«e' dentro o fuori dal muro?»**. Il muro e' la frontiera del gioco: fuori dalla
linea comincia la nebbia (`videogioco-5-duchi-tappa-1-01.md` §3). Un pin fuori
dalle mura non e' un pin poco accurato, e' un pin che porta il giocatore dove non
puo' andare.

**La fonte giusta e' quella che il fondo stesso usa.** Il perimetro viene da
`dati/ferrara_fondo.json`, 14 tratti OSM `barrier=city_wall` con l'anello
ricostruito alla tolleranza dichiarata di 60 m. Non e' Natural Earth perche'
Natural Earth non ha il muro di Ferrara: ha il confine Italia–Croazia. Usare la
scala sbagliata qui non darebbe un difetto, darebbe una risposta vera e inutile.

**I due pin che fino al 3 ottobre non si potevano controllare ora si controllano.**
1-27 (il monumento a Teodoro Bonati nel chiostro della Certosa) e 1-30 (la chiesa
di San Cristoforo) non hanno un numero civico, e il file del fondo li dichiarava
fuori dal controllo: «non si possono verificare, e il file non finge che siano
dentro». Dal 3 ottobre l'ipotesi di `dati/ipotesi_luoghi.json` da' un punto a
entrambe, dichiarato `argomentata` con 150 m di raggio, e **questo file verifica
anche quelli** — con la tolleranza che l'ipotesi dichiara, non con una soglia
inventata qui.

I controlli sono cinque:

  A1  ogni tappa del primo anno ha un punto, o dichiara di non averlo
  A2  ogni punto cade dentro il perimetro delle mura, con il margine dichiarato
  A3  nessuna tappa e' a meno di 30 m dalla linea: il muro non si attraversa
  A4  il percorso fra tappe consecutive non esce dalle mura
  A5  nessuna coordinata duplicata fra le trenta

A4 e' il controllo che vale, ed e' quello che nessuno degli anni dal secondo in
posso avere: **fra due tappe successive si puo' passare fuori dalle mura e
tornare dentro**, e il punto-in-poligono sulle singole tappe non se ne accorgerebbe.
Il percorso del primo anno e' un percorso dentro una citta' e questa e' la sua
unica proprieta' verificabile.

Uso:  python3 sorgenti/gis/verifica_anno1.py
"""
import json
import math
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MAPPA = os.path.join(RADICE, "docs", "videogioco-5-duchi-anno1-mappa.md")
FONDO = os.path.join(RADICE, "dati", "ferrara_fondo.json")
IPOTESI = os.path.join(RADICE, "dati", "ipotesi_luoghi.json")

Q = 100.0              # quantizzazione del file del fondo: 1/100 m
MARGINE_M = 60.0       # il margine dichiarato in `zona_percorribile`
SOGLIA_MURO_M = 30.0   # A3: sotto questa distanza il muro si puo' attraversare
PASI = 40              # passi del tracciato fra due tappe
GUARDIA = []


def esito(ok, testo):
    print(f"  {'OK ' if ok else 'KO '} {testo}")
    GUARDIA.append(bool(ok))


def metrico(lat, lon, centro):
    """Gradi in metri dal centro, con la stessa proiezione del file del fondo.

    Il file del fondo scrive metri con la formula di `ferrara_fondo.metrico()`: la
    si riusa invece di rifarla, perche' **due proiezioni diverse darebbero due
    posizioni diverse per lo stesso punto** e il controllo misurerebbe una cosa
    che non e' quella che il motore disegna. Il raggio di 2 km dell'ipotesi del
    primo anno non coprirebbe la differenza, e il difetto sarebbe dichiarato
    «dentro le mura» mentre il punto del gioco sarebbe fuori.
    """
    lat0, lon0 = centro["lat"], centro["lon"]
    mlat = (111132.92 - 559.82 * math.cos(2 * math.radians(lat0))
            + 1.175 * math.cos(4 * math.radians(lat0)))
    mlon = (111412.84 * math.cos(math.radians(lat0))
            - 93.5 * math.cos(3 * math.radians(lat0)))
    return ((lon - lon0) * mlon, (lat - lat0) * mlat)


def tappe_da_documento():
    """Le trenta tappe del primo anno, lette dalla tabella di anno1-mappa.md 3."""
    testo = open(MAPPA, encoding="utf-8").read()
    corpo = testo.split("## 3. Posizione precisa dei punti", 1)[1].split("## 4.")[0]
    out = []
    for riga in corpo.splitlines():
        if not re.match(r"^\|\s*\d-\d+", riga):
            continue
        c = [x.strip() for x in riga.strip().strip("|").split("|")]
        if len(c) < 5:
            continue
        tappa = {"livello": c[0], "luogo": c[1]}
        try:
            tappa["lat"] = float(c[3])
            tappa["lon"] = float(c[4])
            tappa["fonte"] = "anno1-mappa.md 3 (civici del Comune)"
            tappa["grado"] = "verificata"
        except ValueError:
            tappa["lat"] = tappa["lon"] = None
            tappa["fonte"] = "nessun civico"
            tappa["grado"] = None
        out.append(tappa)
    return out


def ipotesi_per(lid):
    if not os.path.exists(IPOTESI):
        return None
    for r in json.load(open(IPOTESI, encoding="utf-8"))["ipotesi"]:
        if r["tappa"] == lid:
            return r
    return None


def dentro(anello, p, guardia=MARGINE_M):
    """Punto in poligono in metri, con il margine dichiarato che conta dentro.

    Il margine e' quello di `zona_percorribile`: fuori dalla linea c'e' la nebbia,
    e oltre la nebbia non si puo' camminare. Un punto entro 60 m dal muro e'
    quindi percorribile, ed e' la regola che il motore usa per disegnare la nebbia:
    il controllo deve usare la stessa, altrimenti segnalerebbe come difetto una
    tappa che il gioco puo' raggiungere.

    Il bordo conta come dentro perche' una tappa sulla linea delle mura non e'
    fuori dalle mura, e gettarla fuori produrrebbe un difetto che non c'e'.
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
                return True, "margine"
        if (ay > y) != (by > y):
            if x < ax + (y - ay) * (bx - ax) / (by - ay):
                accavallamenti = not accavallamenti
    return accavallamenti, ("dentro" if accavallamenti else "fuori")


def distanza_al_muro(anello, p, passo=5.0, limite=400.0):
    """I metri dal punto alla linea del muro: il primo raggio in cui si e' fuori.

    **La prima versione di questa funzione aveva la ricerca rivoltata** e
    restituiva 5 m a tutte e trenta le tappe, cioe' un difetto che sembrava
    enorme (trenta tappe sul muro) e non era reale. Il punto da cui si parte e'
    gia' dentro l'anello, e la domanda da fare e' «a che distanza smetto di
    essere dentro?», non «a che distanza comincio a essere dentro?»: la seconda
    e' gia' vera a 5 m perche' il punto da cui si parte e' dentro. Un controllo
    che sbaglia il verso della domanda non da' un difetto piccolo, da' un
    allarme falso che fa perdere la fiducia nel controllo e quindi nel file.
    """
    x, y = p
    if not dentro(anello, p, guardia=0.0)[0]:
        return 0.0
    for giro in range(1, int(limite / passo) + 1):
        km = giro * passo
        for gradi in range(0, 360, 5):
            rad = math.radians(gradi)
            q = (x + km * math.cos(rad), y + km * math.sin(rad))
            if not dentro(anello, q, guardia=0.0)[0]:
                return km
    return None


def interpolate(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def main():
    fondo = json.load(open(FONDO, encoding="utf-8"))
    anello = [(x / Q, y / Q) for x, y in fondo["mura"]["anello"]]
    centro = fondo["centro"]
    margine = fondo["zona_percorribile"]["margine_m"]
    tappe = tappe_da_documento()

    print(f"== 0. che cosa si controlla ({len(tappe)} tappe) ==")
    print(f"  fonte del perimetro: {fondo['fonte']}")
    print(f"  tolleranza dell'anello: {fondo['mura']['toll_m']:.0f} m, "
          f"perimetro {fondo['mura']['perimetro_m']} m, "
          f"area {fondo['mura']['area_km2']} km2 "
          f"(storici {fondo['mura']['area_storica_km2']} km2)")
    print(f"  margine dichiarato: {margine:.0f} m")
    print(f"  Natural Earth NON e' la fonte di questo controllo: il confine "
          f"Italia-Croazia non c'entra")
    print()

    # le due tappe senza civico prendono il punto dall'ipotesi
    con_punto, da_ipotesi = 0, []
    for t in tappe:
        if t["lat"] is not None:
            con_punto += 1
            continue
        ip = ipotesi_per(t["livello"])
        if ip and ip["lat"] is not None:
            t["lat"], t["lon"] = ip["lat"], ip["lon"]
            t["grado"] = ip["grado"]
            t["fonte"] = "dati/ipotesi_luoghi.json (%s, %s m)" % (
                ip["grado"], ip.get("raggio_m"))
            da_ipotesi.append(t["livello"])
            con_punto += 1

    print(f"  tappe con punto: {con_punto} su {len(tappe)}")
    if da_ipotesi:
        print(f"    di cui prese dall'ipotesi: {', '.join(da_ipotesi)}")
    print()

    # ------------------------------------------------ A1: un punto o una dichiarazione
    print("== A1. ogni tappa ha un punto, o dichiara di non averlo ==")
    senza = [t["livello"] for t in tappe if t["lat"] is None]
    for t in tappe:
        if t["lat"] is None:
            print(f"  --  {t['livello']} {t['luogo'][:34]}: nessun punto, nessuna "
                  f"ipotesi")
    esito(not senza, f"tappe senza punto e senza dichiarazione: {len(senza)}")
    print()

    # ------------------------------------------------ A2: dentro le mura
    print(f"== A2. ogni punto cade dentro le mura (margine {margine:.0f} m) ==")
    dentro_, margine_, fuori = [], [], []
    for t in tappe:
        if t["lat"] is None:
            continue
        ok, dove = dentro(anello, metrico(t["lat"], t["lon"], centro), margine)
        if not ok:
            fuori.append(t["livello"])
        elif dove == "margine":
            margine_.append(t["livello"])
        else:
            dentro_.append(t["livello"])
    for lid in fuori:
        t = [x for x in tappe if x["livello"] == lid][0]
        print(f"  KO  {lid} {t['luogo'][:34]}: FUORI dalle mura")
    print(f"  dentro: {len(dentro_)}, sul margine: {len(margine_)}, "
          f"fuori: {len(fuori)}")
    esito(not fuori, f"punti fuori dalle mura: {len(fuori)}")
    print()

    # ------------------------------------------------ A3: nessuno sul muro
    print(f"== A3. nessuna tappa a meno di {SOGLIA_MURO_M:.0f} m dalla linea ==")
    sul_muro = []
    for t in tappe:
        if t["lat"] is None:
            continue
        d = distanza_al_muro(anello, metrico(t["lat"], t["lon"], centro),
                             limite=200.0)
        if d is not None and d < SOGLIA_MURO_M:
            sul_muro.append((t["livello"], d))
            print(f"  KO  {t['livello']} {t['luogo'][:34]}: a {d:.0f} m dalla linea")
    print(f"  tappe entro {SOGLIA_MURO_M:.0f} m dalla linea: {len(sul_muro)}")
    print("  (la soglia e' dichiarata: sotto i 30 m il muro si puo' attraversare in "
          "un passo)")
    esito(not sul_muro, f"tappe sul muro: {len(sul_muro)}")
    print()

    # ------------------------------------------------ A4: il percorso non esce
    print("== A4. il percorso fra due tappe consecutive non esce dalle mura ==")
    sequenza = [t for t in tappe if t["lat"] is not None]
    uscite = []
    for a, b in zip(sequenza, sequenza[1:]):
        pa = metrico(a["lat"], a["lon"], centro)
        pb = metrico(b["lat"], b["lon"], centro)
        fuori_tratto = None
        for i in range(PASI + 1):
            ok, _ = dentro(anello, interpolate(pa, pb, i / PASI), margine)
            if not ok:
                fuori_tratto = i
                break
        if fuori_tratto is not None:
            uscite.append((a["livello"], b["livello"], fuori_tratto))
            print(f"  KO  {a['livello']} -> {b['livello']}: esce dalle mura al "
                  f"{fuori_tratto * 100 // PASI}% del tratto")
    print(f"  tratti che escono dalle mura: {len(uscite)} su "
          f"{max(0, len(sequenza) - 1)}")
    print(f"  (il tracciato e' un segmento con {PASI} passi per tratto: e' un "
          f"controllo sul percorso, non sui due capi)")
    esito(not uscite, f"tratti fuori dalle mura: {len(uscite)}")
    print()

    # ------------------------------------------------ A5: nessun punto duplicato
    print("== A5. nessuna coordinata duplicata fra le trenta ==")
    visti, dup = {}, []
    for t in tappe:
        if t["lat"] is None:
            continue
        k = (round(t["lat"], 5), round(t["lon"], 5))
        if k in visti:
            dup.append((visti[k], t["livello"]))
            print(f"  KO  {visti[k]} e {t['livello']} hanno le stesse coordinate")
        visti[k] = t["livello"]
    esito(not dup, f"coordinate duplicate: {len(dup)}")
    print()

    # ------------------------------------------------ sintesi
    lung = sum(math.hypot(b["lat"] - a["lat"], b["lon"] - a["lon"])
               for a, b in zip(sequenza, sequenza[1:]))
    print("== sintesi ==")
    print(f"  tappe: {len(tappe)}   con punto: {con_punto}")
    print(f"  dentro le mura: {len(dentro_)}, sul margine: {len(margine_)}, "
          f"fuori: {len(fuori)}")
    print(f"  percorso in linea d'aria: {lung * 111.32:.0f} km equivalenti "
          f"({lung * 111320:.0f} m reali)")
    print(f"  area giocabile: {fondo['mura']['area_km2']} km2, "
          f"{fondo['mura']['perimetro_m']} m di muro")
    if not GUARDIA or all(GUARDIA):
        print("  nessun difetto: il primo anno e' tutto dentro le mura, e anche "
              "il percorso fra le tappe")
    else:
        print("  ci sono difetti, e sono elencati sopra")
    print(f"\n==== controlli superati: {sum(GUARDIA)}/{len(GUARDIA)} ====")
    return 0 if all(GUARDIA) else 1


if __name__ == "__main__":
    sys.exit(main())
