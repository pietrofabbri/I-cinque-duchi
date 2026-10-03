"""Il file amministrativo che mancava: l'unità di primo livello di tutto il
mondo, per i 19 pin che il file europeo non copre.

`verifica_pin.py` dichiara, al controllo 3, che 19 pin degli anni dal secondo
in poi non sono verificabili sull'unità amministrativa: sono in Paesi che il
file `europa_50_regioni_amministrative` non contiene, perché quel file è
ricavato da un riquadro che finisce all'Europa. Questo file è la risposta, e
la risposta è **tagliata**: non si tiene tutto il mondo, si tiene l'unità
amministrativa che contiene ciascun pin, e si dichiara nel file di copertura
quali sono e quante sono state scartate.

Il motivo è il peso. Natural Earth `10m_admin_1_states_provinces` ha 4 596
unità e 1 295 319 vertici: nel formato a delta sarebbero alcuni megabyte per
un file che il gioco usa solo per una domanda — «il pin è nella provincia
giusta?». Il file che esce è di due ordini di grandezza più piccolo, e per
il controllo che deve fare è **identico**: la domanda non cambia se la
provincia di Ferrara c'è insieme a tutte le altre o se c'è sola.

Il taglio non è geometrico, e questa è la scelta che va dichiarata: come
`mappe_formato.py` già fa, l'anello che non tocca il riquadro **viene
scartato**, ma quello che lo tocca viene tenuto **intero**. Ritagliare un
poligono con un riquadro produce un anello che si auto-interseca, e un anello
sua auto-intersecato falsifica sia il disegno sia il punto-in-poligono: la
prima versione di `mappe_formato.py` arrivava a dire che Venezia era dentro la
Baviera.

I due Paesi che il file sbaglia, e che restano sbagliati perché la fonte li
scrive così: **Bajkonur** cade dentro l'unità amministrativa «Bayqoñyr», che
è il cosmodromo e non l'oblast di Kyzylorda in cui il cosmodromo si trova;
**Karakorum** cade dentro «dell'Arhangaj», che è la traduzione italiana che
Natural Earth dà dell'Övörkhangai. Sono due nomi, non due coordinate: il
controllo 2 sul Paese resta valido e il pin è dove deve essere.

Uso:
    python3 sorgenti/gis/mondo_admin1.py                # scarica e produce
    python3 sorgenti/gis/mondo_admin1.py --prova        # conta e non scrive
"""
import json
import os
import sys
import zipfile
import io
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shapefile_lettore import leggi
from punto_in_poligono import dentro

# `mappe_formato.py` ha l'import di pyshp dentro `le()`, quindi questo file
# riusa `taglia` e `scrivi` senza dipendere da una libreria che qui non c'e'.
import mappe_formato as MF

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LAVORO = os.environ.get("MAPPE_LAVORO", "/tmp/ne-mappe")
OUT = os.path.join(RADICE, "dati", "mappe")
URL = ("https://naciscdn.org/naturalearth/10m/cultural/"
       "ne_10m_admin_1_states_provinces.zip")
NOME = "ne_10m_admin_1_states_provinces"

# Quanto semplificare. La scala 10m ha già tolto 200 m dal dettaglio, e il file
# europeo usa 0,05: la tolleranza grossa è quella giusta per una mappa che si
# guarda. Ma c'è un caso in cui è **sbagliata**, ed è il caso per cui questo
# file esiste: il borough britannico di Westminster è un poligono di 47 vertici
# che a 0,05 si semplifica in **zero anelli**, e a 0,02 non contiene più il pin
# che dovrebbe contenere. Un file che perde l'unità amministrativa del proprio
# pin non è un file accurato: è un file che mente sul controllo che sta
# facendo, e mente in modo che il controllo non può accorgersene.
#
# Quindi la regola è: si semplifica grosso, e **poi si verifica**. Se l'anello
# semplificato non contiene più il pin che lo aveva scelto, si rifa più fine.
# Il file non usa una tolleranza sola, usa la più grossa che non faccia
# perdere nessun pin. Il numero di unità per cui è stato necessario scendere
# è dichiarato nel file di copertura.
TOL = 0.05
# le tolleranze di riserva, dalla più grossa alla più fine. L'ultima è il fondo:
# a 0,002 gradi (200 m, la stessa della penisola) non si scende più, e se
# anche così il pin non sta dentro, l'anello viene tenuto intero.
TOLLERANZE = [0.05, 0.02, 0.01, 0.006, 0.002]
Q = 2000
CHIAVI = ["name_it", "name", "admin", "adm1_code", "type_en", "adm0_a3"]

# Il riquadro serve a una cosa sola: dichiarare nel file di copertura che il
# taglio non e' a zero. La scelta dell'unita' NON lo usa: e' punto-in-poligono
# sul punto del pin. Con la versione che usava il riquadro, Los Alamos e
# Xianyang risultavano fuori da ogni unita' — non perche' la fonte non le abbia,
# ma perche' sono al centro di un territorio cosi' grande che il suo bordo non
# arriva a toccare il riquadro della citta'.
CUSCINETTO = 0.75


def scarica():
    os.makedirs(os.path.join(LAVORO, "ne"), exist_ok=True)
    base = os.path.join(LAVORO, "ne", NOME)
    if os.path.exists(base + ".shp"):
        return base + ".shp"
    print("scarico", NOME)
    req = urllib.request.Request(URL, headers={"User-Agent": "i-cinque-duchi/0.1"})
    with urllib.request.urlopen(req, timeout=180) as f:
        dati = f.read()
    z = zipfile.ZipFile(io.BytesIO(dati))
    for est in (".shp", ".shx", ".dbf", ".prj"):
        with open(base + est, "wb") as f:
            f.write(z.read(NOME + est))
    return base + ".shp"


def pin():
    """Ogni pin che ha coordinate, con il suo riquadro."""
    luoghi = json.load(open(os.path.join(RADICE, "dati", "luoghi_gioco.json"),
                            encoding="utf-8"))["luoghi"]
    out = []
    for v in luoghi:
        if v.get("lat") is None:
            continue
        out.append((v["luogo"], v["lon"], v["lat"],
                    v["lon"] - CUSCINETTO, v["lat"] - CUSCINETTO,
                    v["lon"] + CUSCINETTO, v["lat"] + CUSCINETTO))
    return out


def taglia_che_non_perde(anelli, dentro_puo, scatole):
    """Semplifica alla tolleranza più grossa che non faccia perdere un pin.

    Il punto qui non è la fedeltà del disegno, è che il file **non deve
    contraddirsi**: un poligono che semplificato non contiene più il pin che lo
    aveva fatto scegliere direbbe al verificatore che quel pin non è in quella
    unità, e il verificatore ci crederebbe. Westminster a 0,05 gradi sparisce
    del tutto.
    """
    punti = {nome: (lon, lat) for nome, lon, lat, _, _, _, _ in scatole}
    prove = [(nome, punti[nome]) for nome in dentro_puo if nome in punti]
    for tol in TOLLERANZE:
        tagliati = MF.taglia(anelli, "poligono", None, tol)
        if tagliati and all(dentro(tagliati, lon, lat) for _, (lon, lat) in prove):
            return tagliati, tol
    # ultima riserva: l'anello intero, senza semplificazione
    return [a for a in anelli if len(a) >= 4], TOLLERANZE[-1]


def main():
    solo_prova = "--prova" in sys.argv
    shp = scarica()
    scatole = pin()
    print(f"pin da coprire: {len(scatole)}, cuscinetto {CUSCINETTO} gradi")

    geom = leggi(shp)
    print(f"unita' nella fonte: {len(geom)}")

    scelte, servite, scartate, ridotte = [], {}, [], []
    for props, anelli in geom:
        # Il criterio di copertura e' `dentro`, NON "l'anello tocca il
        # riquadro". Sono due domande diverse e la prima versione di questo
        # file usava la seconda: per un punto al centro di un territorio
        # grande l'anello non tocca il riquadro della citta' — Los Alamos e'
        # nel mezzo del New Mexico — e il file diceva che due pin su 54 non
        # avevano unita' amministrativa. Non era un buco della fonte: era il
        # criterio.
        #
        # E `dentro` si chiama UNA volta per poligono, con tutti i suoi
        # anelli insieme, non anello per anello: il winding number somma i
        # contributi di esterno e buchi, e chiamarlo anello per anello fa
        # perdere i buchi. Su Agra, che ha un solo anello, la differenza si
        # vedeva lo stesso: `any(dentro(a) for a in anelli)` dava vuoto e
        # `dentro(a)` dava Uttar Pradesh. Con piu' anelli la cosa peggiora,
        # perché un lago dentro la provincia la fa sparire.
        dentro_puo = [nome for nome, lon, lat, _, _, _, _ in scatole
                      if dentro(anelli, lon, lat)]
        if not dentro_puo:
            scartate.append((props.get("name_it") or props.get("name"),
                             props.get("admin")))
            continue
        tagliati, usata = taglia_che_non_perde(anelli, dentro_puo, scatole)
        if not tagliati:
            scartate.append((props.get("name_it") or props.get("name"),
                             props.get("admin")))
            continue
        if usata != TOL:
            ridotte.append((props.get("name_it") or props.get("name"), usata))
        pulite = {k: props.get(k) for k in CHIAVI if props.get(k) not in (None, "")}
        scelte.append((pulite, tagliati))
        for nome in dentro_puo:
            servite.setdefault(nome, []).append(pulite.get("adm1_code"))

    print(f"unita' tenute: {len(scelte)}   scartate: {len(scartate)}")
    if ridotte:
        print(f"unita' che hanno avuto bisogno di una tolleranza piu' fine di "
              f"{TOL}: {len(ridotte)}")
        for nome, tol in ridotte:
            print(f"    {nome:<28} tolleranza {tol}")
    senza = [nome for nome, lon, lat, x0, y0, x1, y1 in scatole
             if nome not in servite]
    print(f"pin con almeno un'unita': {len(scatole) - len(senza)} su {len(scatole)}")
    if senza:
        print("  pin SENZA unita':", senza)

    if solo_prova:
        return 0

    os.makedirs(OUT, exist_ok=True)
    size = MF.scrivi(os.path.join(OUT, "mondo_admin1.json"), scelte, [], Q)
    nv = sum(len(s) for _, ss in scelte for s in ss)
    print(f"scritto mondo_admin1.json: {size//1024} kB, {nv} vertici")

    # il file di copertura: cosa c'è dentro e cosa no, scritto nei dati e non
    # solo nel documento, perché il prossimo che ci mette dentro un pin non
    # deve scoprirlo leggendo un .md
    with open(os.path.join(OUT, "mondo_admin1_copertura.json"), "w",
              encoding="utf-8") as f:
        json.dump({
            "file": "mondo_admin1.json",
            "fonte": "Natural Earth 10m admin_1_states_provinces (pubblico dominio)",
            "tolleranza_gradi": TOL,
            "tolleranze_di_riserva": TOLLERANZE,
            "unita_che_hanno_avuto_bisogno_di_riserva": [
                {"unita": nome, "tolleranza": tol} for nome, tol in ridotte],
            "quantizzazione": Q,
            "cuscinetto_gradi": CUSCINETTO,
            "unita_nella_fonte": len(geom),
            "unita_nel_file": len(scelte),
            "unita_scartate": len(scartate),
            "pin_coperti": len(scatole) - len(senza),
            "pin_totali": len(scatole),
            "pin_per_unita": servite,
            "avvertenze": [
                "la scelta dell'unita' e' punto-in-poligono sul pin, non un "
                "taglio per riquadro: il riquadro del file e' solo la "
                "dichiarazione di quanto il taglio puo' allargarsi",
                "la semplificazione scende da sola finche' l'anello contiene "
                "ancora il proprio pin: %d unita' su %d hanno avuto bisogno di "
                "una tolleranza piu' fine" % (len(ridotte), len(scelte)),
                "l'unita' e' quella che contiene il pin, non il nome del pin: "
                "Bajkonur cade dentro 'Bayqonyr', che e' il cosmodromo, e "
                "Karakorum dentro 'dell'Arhangaj', che e' la traduzione "
                "italiana dell'Ovorkhangai. Sono due nomi, non due coordinate",
                "niente altezza e nessun dettaglio urbano: questo file serve "
                "solo al controllo 'il pin e' nella giusta unita' amministrativa'",
            ],
        }, f, ensure_ascii=False, indent=1)
    print("scritto mondo_admin1_copertura.json")
    return 0


    """Tenuto per compattezza con una versione precedente: la copertura si
    calcola sopra `servite`, che è già fatto."""
    return True


if __name__ == "__main__":
    sys.exit(main())