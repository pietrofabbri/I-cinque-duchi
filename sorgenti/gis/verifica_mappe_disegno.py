"""Disegna in SVG le mappe estratte, per controllarle a vista.

Nessuna libreria: i file si aprono con doppio clic nel browser. Serve a vedere
se coste, confini e posizioni delle citta' sono davvero quelli giunti, prima di
fidarsi dei numeri e prima di archiviare.

**I colori non sono piu' in questo file.** Fino alla v0.2 erano dodici
esadecimali scritti qui dentro, e la domanda che se li guardava era giusta: un
colore che esiste solo nel codice non lo legge nessuno, e due persone che
colorano la stessa carta ne fanno due carte diverse. Ora si leggono da
`dati/fonti_visive/colori_cartografici.json`, che è l'unico posto in cui sono
dichiarati e che porta, per ciascuno, da dove viene.

La conseguenza voluta è che questo file non può più avere un colore che il file
dei colori non conosce: `sorgenti/verifica_colori.py` lo controlla, e cerca
esadecimali anche in questa fonte per trovare i colori rimasti indietro.

La stessa cosa è valida per i **punti**: il colore del segno arriva da
`stile_punti`, dichiarato dalla pagina che chiama `pagina()`, perché un
segnino che non dice quale categoria disegna è un colore che vive solo nel
codice — ed è successo: i punti delle città avevano il loro colore scritto
dentro `pagina()`, e le cime non potevano averne uno proprio.
"""
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mappe_lettore import leggi

OUT = os.path.join(RADICE, "dati", "mappe")
COLORI = os.path.join(RADICE, "dati", "fonti_visive", "colori_cartografici.json")
SVG = os.path.join(RADICE, "verifica")
os.makedirs(SVG, exist_ok=True)


def _tavolozza():
    with open(COLORI, encoding="utf-8") as f:
        voci = json.load(f)["voci"]
    return {v["chiave"]: v for v in voci}


def _col(voci, chiave):
    """`#rrggbb` per l'SVG.

    Nel file dei colori l'esadecimale e' **senza** cancelletto, come in
    `tavolozza.json`: il cancelletto e' un dettaglio del formato SVG e metterlo
    nel dato significa che il file non puo' piu' essere confrontato con la
    tavolozza senza toglierlo. Quindi si aggiunge qui, dove serve.

    DIFETTO CORRETTO: la prima versione scriveva `fill="F6FAFC"`, cioe' senza
    cancelletto, e l'SVG risultava senza colori: un file ben formato che non
    disegna niente. Il lettore di file accetta che un colore senza `#` sia
    spazio bianco, e su una pagina di verifica e' il modo peggiore di perdere
    un colore.
    """
    return "#" + voci[chiave]["hex"]


def stile(voci, riempimento=None, bordo=None, spessore="1"):
    """Il tratto `fill`/`stroke` di un gruppo SVG, letto dal file dei colori.

    I bordi si dichiarano senza cancellare il colore: `bordo` prende il colore
    della chiave `chiave_bordo`, e la chiave `senza_riempimento` resta
    esplicita quando la categoria non ha un riempimento proprio.
    """
    parti = []
    if riempimento:
        parti.append('fill="%s"' % _col(voci, riempimento))
    else:
        parti.append('fill="none"')
    if bordo:
        parti.append('stroke="%s"' % _col(voci, bordo))
    parti.append('stroke-width="%s"' % spessore)
    return " ".join(parti)


def pagina(nome, titolo, bbox, voci, W=940, H=640, stile_poligono="",
           nome_pt=None, stile_punti=None):
    geom, punti = leggi(os.path.join(OUT, nome))
    x0, y0, x1, y1 = bbox
    s = min(W / (x1 - x0), H / (y1 - y0))
    ox = (W - (x1 - x0) * s) / 2
    oy = (H - (y1 - y0) * s) / 2

    def sch(pt):
        return (ox + (pt[0] - x0) * s, oy + (y1 - pt[1]) * s)

    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
           'viewBox="0 0 %d %d">' % (W, H, W, H)]
    svg.append('<rect width="%d" height="%d" fill="%s"/>'
               % (W, H, _col(voci, "fondo_pagina")))
    svg.append('<g %s>' % stile_poligono)
    for props, anelli in geom:
        for a in anelli:
            if len(a) < 2:
                continue
            p = " ".join("%.1f,%.1f" % sch(pt) for pt in a)
            svg.append('<polygon points="%s"/>' % p)
    svg.append("</g>")
    # I colori del punto vengono da `stile_punti` e non sono piu' scritti qui:
    # era il modo per cui i punti delle citta' avevano un colore che nessuna
    # tabella dichiarava, e le cime non potevano avere un colore proprio senza
    # duplicare la riga. Un file che disegna deve dire quale categoria sta
    # disegnando, anche per il segno piu' piccolo.
    riempimento_pt, bordo_pt = stile_punti or ("citta", "citta_bordo")
    svg.append('<g fill="%s" stroke="%s" stroke-width="0.6">'
               % (_col(voci, riempimento_pt), _col(voci, bordo_pt)))
    for props, x, y in punti:
        X, Y = sch((x, y))
        svg.append('<circle cx="%.1f" cy="%.1f" r="2.4"/>' % (X, Y))
    svg.append("</g>")
    if nome_pt:
        svg.append('<g font-family="sans-serif" font-size="8.5" fill="%s">'
                   % _col(voci, "etichetta_mappa"))
        for props, x, y in punti:
            nm = props.get(nome_pt) or props.get("NAMEASCII") or ""
            if not nm:
                continue
            X, Y = sch((x, y))
            svg.append('<text x="%.1f" y="%.1f">%s</text>' % (X + 4, Y + 3, nm))
        svg.append("</g>")
    svg.append('<text x="14" y="26" font-size="15" font-family="sans-serif" '
               'fill="%s">%s</text>' % (_col(voci, "etichetta_titolo"), titolo))
    svg.append('<text x="14" y="44" font-size="10" fill="%s">%d geometrie, %d punti '
               '&#183; %s</text>'
               % (_col(voci, "etichetta_secondaria"), len(geom), len(punti), nome))
    svg.append("</svg>")
    path = os.path.join(SVG, nome.replace(".json", ".svg"))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(path)


IT = [5.0, 34.0, 20.0, 49.5]
EU = [-25.0, 33.0, 46.0, 73.0]

if __name__ == "__main__":
    V = _tavolozza()

    pagina("penisola_10_coste.json", "Anno 2 — coste d'Italia e isole", IT, V,
           stile_poligono='fill="none" stroke="%s" stroke-width="1.2"'
                          % _col(V, "costa"))
    pagina("penisola_10_paesi.json", "Anno 2 — paesi confinanti", IT, V,
           stile_poligono=stile(V, "stato_riempimento_anno2",
                                "stato_bordo_anno2"))
    pagina("penisola_10_regioni.json", "Anno 2 — regioni e province", IT, V,
           stile_poligono=stile(V, "unita_amministrativa",
                                "unita_amministrativa_bordo", "0.7"))
    pagina("penisola_10_fiumi.json", "Anno 2 — fiumi e laghi", IT, V,
           stile_poligono='fill="none" stroke="%s" stroke-width="1.4"'
                          % _col(V, "fiume"))
    pagina("penisola_10_citta.json", "Anno 2 — città (punti reali)",
           [6.0, 36.0, 19.0, 47.5], V, nome_pt="NAME_IT")
    pagina("europa_50_paesi.json", "Anno 3 — Europa", EU, V,
           stile_poligono=stile(V, "stato_riempimento", "stato_bordo"))
    pagina("europa_50_citta.json", "Anno 3 — città europee",
           [-11.0, 36.0, 32.0, 61.0], V, nome_pt="NAMEASCII")
    pagina("mondo_110_paesi.json", "Anno 4 — il mondo",
           [-175.0, -50.0, 180.0, 78.0], V, W=1120, H=560,
           stile_poligono=stile(V, "stato_riempimento", "stato_bordo"))

    # Le quattro pagine seguenti esistono perche' il file dei colori dichiara
    # categorie che nessuna pagina mostrava: terre, laghi, regioni fisiche e le
    # 50 unita' amministrative del mondo. Un colore dichiarato e mai disegnato
    # e' una promessa che nessuno verifica, e `verifica_colori.py` segnala
    # come inutilizzato un colore che questa pagina non usa.
    pagina("mondo_110_terre.json", "Anno 4 — terre emerse (solo bordo, senza riempimento)",
           [-175.0, -50.0, 180.0, 78.0], V, W=1120, H=560,
           stile_poligono='fill="none" stroke="%s" stroke-width="0.9"'
                          % _col(V, "poligono_bordo"))
    pagina("mondo_110_laghi.json", "Anno 4 — laghi", [-175.0, -50.0, 180.0, 78.0], V,
           W=1120, H=560,
           stile_poligono=stile(V, "lago", "lago", "0.8"))
    pagina("mondo_110_regioni.json", "Anno 4 — regioni fisiche (solo bordo)",
           [-175.0, -50.0, 180.0, 78.0], V, W=1120, H=560,
           stile_poligono='fill="none" stroke="%s" stroke-width="0.9"'
                          % _col(V, "poligono_bordo"))
    pagina("mondo_admin1.json", "Anno 5 — le 50 unità amministrative del mondo",
           [-175.0, -50.0, 180.0, 78.0], V, W=1120, H=560,
           stile_poligono=stile(V, "stato_riempimento", "stato_bordo"))

    # Le tre pagini delle cime sono nate da un controllo, non da un desiderio:
    # `verifica_colori.py` (C7) segnala che un file in `dati/mappe/` senza
    # nessun colore che lo riguardi non sa come si disegna. I tre file delle
    # cime erano esattamente quel caso, e la risposta non era dichiarare che
    # non ne hanno bisogno — un punto che non ha colore non si vede — ma
    # dichiarare il colore del segno cima e usarlo.
    pagina("mondo_110_altitudine.json",
           "Anno 4/5 — le 15 cime principali del mondo",
           [-175.0, -50.0, 180.0, 78.0], V, W=1120, H=560,
           nome_pt="name_it", stile_punti=("cima", "cima_bordo"))
    pagina("europa_50_altitudine.json",
           "Anno 3 — le 2 cime che la fonte elenca in Europa alla scala 50m",
           [-25.0, 33.0, 46.0, 73.0], V,
           nome_pt="name_it", stile_punti=("cima", "cima_bordo"))
    pagina("penisola_10_altitudine.json",
           "Anno 2 — le 26 cime del riquadro della penisola",
           [5.0, 34.0, 20.0, 49.5], V,
           nome_pt="name_it", stile_punti=("cima", "cima_bordo"))