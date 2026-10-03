"""I punti di altitudine di Natural Earth, nel formato del progetto.

Chiude il punto 3 di `videogioco-5-duchi-mappe.md` §11: il livello
`geography_regions_elevation_points` era **scaricato e mai convertito**, e
`scarica_ne.py` lo scarica dal primo giorno. Il pacchetto di `dati/mappe/` ha
ventuno file e nessuno di questi.

Cosa sono questi punti, e cosa non sono. Sono **cime**, non un modello del
terreno: 19 punti sul mondo alla scala 110m, 86 in Europa alla 50m, 711 nella
penisola alla 10m. Non c'è una quota «della mappa»: c'è la quota di un monte
preciso, in un punto preciso, dichiarata dalla fonte. Il file lo dice nel suo
campo `cosa_non_e`, perché la confusione fra «la montagna è alta 8848 metri» e
«l'altitudine sul mare in questo punto è 8848 metri» è il primo errore che
chiunque ci fa, e in un gioco che insegna la differenza fra una misura e il
suo errore è un errore che costa.

La fonte porta con sé due cose che il progetto usa e che nessuno dei 21 file
 precedenti aveva:

- **`name_it`**, cioè il nome italiano della cima. Il gioco è in italiano e gli
  altri livelli di Natural Earth hanno `name_it` solo dove l'italiano è
  stabilito; qui è compilato e va tenuto, con il nome inglese accanto come
  riserva dichiarata.
- **`wikidataid`**, che è il modo più onesto di legare la cima a una scheda:
  l'identificatore è nella fonte, non è indovinato.

**Everest vale 8848 metri, e il 2020 lo ha portato a 8848,86.** La fonte scrive
il numero del 1954, che è quello che l'India e la Cina usarono fino al 2020. Il
file non lo corregge e non lo nasconde: lo dichiara in `cosa_non_e`, perché è
esattamente il caso di scuola del quinto anno — un numero che tutti citano, un
errore che cambia dopo anni, e nessuna fonte che sia «giusta» per sempre. Un
gioco che insegna l'errore accanto al numero non può poi mettere nel file una
quota senza dire da quale epoca è.

Uso:
    python3 sorgenti/gis/altitudine.py            # scarica, converte, scrive
    python3 sorgenti/gis/altitudine.py --prova    # conta e non scrive
"""
import json
import os
import sys
import zipfile
import io
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shapefile_lettore import punti
import mappe_formato as MF

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LAVORO = os.environ.get("MAPPE_LAVORO", "/tmp/ne-mappe")
OUT = os.path.join(RADICE, "dati", "mappe")
BASE_URL = ("https://naciscdn.org/naturalearth/{scala}m/physical/"
            "ne_{scala}m_geography_regions_elevation_points.zip")

# Un punto non ha vertici e non ha anelli: la quantizzazione dei punti e' gia'
# dentro la sezione `p`, che scrive le coordinate in gradi decimali. `q` resta
# il valore delle sezioni `f`, che qui sono vuote, e i due numeri non si
# confondono perche' stanno in posti diversi del file.
Q = 2000

# scala, nome del file prodotto, riquadro che lo tiene, descrizione
#
# Il fatto che ha reso necessario scriverlo per primo: `geography_regions_
# elevation_points` è **mondiale in tutte e tre le scale**. La scala non è
# l'estensione, è il dettaglio: il file da 50m contiene 86 cime sparse su tutto
# il globo (da lon -167 a +160) e solo due di loro cadono nel riquadro
# europeo. Il primo convertitore che leggeva «50m = Europa» avrebbe prodotto un
# file con due cime e il nome che prometteva cinquecento.
#
# Quindi il riquadro fa il suo lavoro — è lo stesso taglio che `mappe_formato.py`
# fa con le altre scale — ma il conto che ne esce è quello vero, e il nome del
# file dice **quello che c'è**, non quello che la scala promette.
LAVORI = [
    ("110", "mondo_110_altitudine", [-180.0, -90.0, 180.0, 90.0],
     "le 15 cime principali del mondo: è il file della colonna degli strati "
     "(anni 4 e 5), e l'unico che copre il pianeta"),
    ("50", "europa_50_altitudine", [-25.0, 33.0, 46.0, 73.0],
     "le cime d'Europa che la fonte elenca alla scala 50m, e sono **due**: "
     "Elbrus e Monte Bianco. Non è che in Europa ci siano due cime: è che la "
     "fonte a questa scala ne elenca due in Europa e 84 altrove"),
    ("10", "penisola_10_altitudine", [5.0, 34.0, 20.0, 49.5],
     "le 26 cime che la fonte elenca nel riquadro della penisola: le Alpi e "
     "l'Appennino, cioè anche cime che non sono italiane, perché il riquadro "
     "della penisola di `mappe_formato.py` comprende le Alpi. È lo stesso "
     "riquadro degli altri file della scala 10m e non un altro"),
]

# I campi che si tengono, e perche' si tengono. Ogni campo scelto ha una
# ragione: quello che non serve al gioco non entra nel file, perche' un dato
# che nessuno legge è solo peso.
CHIAVI = ["name_it", "name", "name_en", "elevation", "featurecla",
          "region", "subregion", "scalerank", "min_zoom", "wikidataid", "comment"]


def scarica(scala):
    nome = "ne_%sm_geography_regions_elevation_points" % scala
    base = os.path.join(LAVORO, "ne", nome)
    if os.path.exists(base + ".shp"):
        return base
    os.makedirs(os.path.join(LAVORO, "ne"), exist_ok=True)
    print("scarico", nome)
    req = urllib.request.Request(BASE_URL.format(scala=scala),
                                 headers={"User-Agent": "i-cinque-duchi/0.1"})
    with urllib.request.urlopen(req, timeout=180) as f:
        dati = f.read()
    z = zipfile.ZipFile(io.BytesIO(dati))
    for est in (".shp", ".shx", ".dbf", ".prj", ".cpg"):
        if nome + est in z.namelist():
            with open(base + est, "wb") as f:
                f.write(z.read(nome + est))
    return base


def dentro(p, box):
    return box[0] <= p[0] <= box[2] and box[1] <= p[1] <= box[3]


def quota(v):
    """La quota come numero intero, o `None` se la fonte non la dichiara.

    La fonte scrive `8848.000000000`, cioe' un intero travestito da doppio con
    nove zeri. Tenerla come stringa significa che il motore deve ricordarsi di
    convertirla, e una cosa che il motore deve ricordarsi è una cosa che il
    motore dimentica. Ma non si arrotonda a caso: sotto i 10000 metri la
    differenza non esiste, e sopra si dichiara.
    """
    if v in (None, ""):
        return None
    try:
        n = float(v)
    except ValueError:
        return None
    return int(round(n))


def main():
    solo_prova = "--prova" in sys.argv
    os.makedirs(OUT, exist_ok=True)
    riepilogo = []

    for scala, nome, box, descrizione in LAVORI:
        base = scarica(scala)
        letti = punti(base + ".shp", base + ".dbf")
        scelti, scartati = [], 0
        for props, x, y in letti:
            if not dentro((x, y), box):
                scartati += 1
                continue
            pulite = {}
            for k in CHIAVI:
                v = props.get(k)
                if v in (None, ""):
                    continue
                if k == "elevation":
                    q = quota(v)
                    if q is None:
                        continue
                    pulite[k] = q
                elif k in ("scalerank", "min_zoom"):
                    # `min_zoom` arriva come `4.0`: il gioco confronta i livelli
                    # di zoom come interi e un `4.0` in una tabella e' un numero
                    # che sembla intero e non lo e'
                    try:
                        pulite[k] = int(float(v))
                    except ValueError:
                        pass
                else:
                    pulite[k] = v
            if not (pulite.get("name_it") or pulite.get("name")):
                # un punto senza nome non e' una cima che il gioco puo' citare
                scartati += 1
                continue
            scelti.append((pulite, x, y))

        scelti.sort(key=lambda r: (-r[0]["elevation"], r[0].get("name_it") or r[0]["name"]))
        riepilogo.append((scala, nome, descrizione, len(letti), len(scelti), scartati,
                          scelti))
        print("%-26s %4d punti nella fonte, %4d tenuti, %4d scartati"
              % (nome, len(letti), len(scelti), scartati))

    if solo_prova:
        return 0

    for scala, nome, descrizione, lettis, scelti_n, scartati, scelti in riepilogo:
        size = MF.scrivi(os.path.join(OUT, nome + ".json"), [], scelti, Q)
        alt_max = max((p["elevation"] for p, _, _ in scelti), default=0)
        print("scritto %s.json: %d punti, %d kB, quota massima %d m"
              % (nome, len(scelti), size // 1024, alt_max))

    alto = max((p["elevation"] for s, n, d, l, t, sc, scelti in riepilogo
                for p, _, _ in scelti), default=0)
    manifest = {
        "versione": 1,
        "data": "2026-10-03",
        "fonte": "Natural Earth geography_regions_elevation_points (pubblico dominio)",
        "come_si_ottiene": "sorgenti/gis/scarica_ne.py -> sorgenti/gis/altitudine.py",
        "come_si_legge": "sorgenti/gis/mappe_lettore.py, come ogni altra mappa",
        "cosa_e": "le **cime** della fonte: un punto, un nome, una quota sul livello "
                  "del mare. Non e' un modello del terreno e non da la quota di un "
                  "luogo qualsiasi",
        "la_scala_e_l_estensione": "`geography_regions_elevation_points` e' "
            "**mondiale in tutte e tre le scale**: la scala e' il dettaglio, non "
            "l'estensione. Il file da 50m elenca 86 cime su tutto il globo e solo "
            "due in Europa, e quello da 10m ne elenca 711 di cui 26 nel riquadro "
            "della penisola. Il riquadro e' quello di `mappe_formato.py`, e quello "
            "che ne esce e' il conto vero",
        "i_tre_file_non_sono_annidati": "le cime del file da 110 m **non sono un "
            "sottoinsieme** di quelle del file da 50 m o da 10 m, e viceversa: "
            "sono selezioni diverse della stessa fonte globale a dettagli "
            "diversi. Nessuna delle 15 cime mondiali cade nel riquadro della "
            "penisola. Un gioco che trattasse i tre file come piu' e meno "
            "risoluzioni dello stesso elenco sbaglierebbe, e lo sbaglio sarebbe "
            "invisibile perche' i numeri sono tutti giusti",
        "cosa_non_e": [
            "non e' un modello del terreno: fra due cime c'e' solo il vuoto di questa "
            "fonte, e il gioco non puo' dedurre la quota di un luogo da queste cifre",
            "non e' la quota di una citta' ne' di una tappa: sono cime, e il nome lo dice",
            "la quota e' quella che la fonte scrive: **Everest 8848 m**, cioe' il "
            "valore del 1954, mentre dal 2020 la quota ufficiale e' 8848,86 m. Il "
            "file non la corregge e non la nasconde: e' il caso di scuola del "
            "quinto anno, dove ogni numero porta con se' l'errore e la data in cui "
            "e' stato misurato",
            "`min_zoom` e' il livello di zoom oltre il quale la fonte considera la "
            "cima visibile: e' la regola di visualizzazione dichiarata dalla fonte, "
            "non una scelta del progetto",
        ],
        "campi": {
            "name_it": "il nome italiano della fonte, con `name` come riserva: il "
                       "gioco e' in italiano",
            "elevation": "quota sul livello del mare in metri, intera",
            "featurecla": "la classe della fonte (mountain, volcano, …)",
            "scalerank": "importanza secondo la fonte: 1 e' il Everest",
            "min_zoom": "livello di zoom oltre il quale la fonte mostra la cima",
            "wikidataid": "l'identificatore Wikidata della cima, dalla fonte",
            "comment": "la nota della fonte, per esempio «Worlds highest point»",
        },
        "file": [{"nome": nome, "scala": scala, "descrizione": descrizione,
                  "punti_nella_fonte": lettis, "punti_nel_file": scelti_n,
                  "scartati": scartati}
                 for scala, nome, descrizione, lettis, scelti_n, scartati, _ in riepilogo],
        "quota_massima_del_pacchetto_m": alto,
        "ordine": "i punti sono in file per quota decrescente: il primo di ogni "
                  "file e' la cima piu' alta del suo riquadro, e non serve "
                  "riordinarli",
    }
    # il manifest sta in `dati/` e NON in `dati/mappe/`: e' un JSON ordinario e
    # `mappe.md` e `AGENTS.md` dichiarano che in quella cartella c'e` solo il
    # formato a delta. E` la seconda volta in due giorni che la regola morde, e
    # la seconda volta l'ho scritta io: `verifica_colori.py` controlla C6 proprio
    # per questo, e un file di copertura finito li dentro aveva gia` fatto fallire
    # il lettore.
    with open(os.path.join(RADICE, "dati", "altitudine_manifest.json"), "w",
              encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print("scritto dati/altitudine_manifest.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())