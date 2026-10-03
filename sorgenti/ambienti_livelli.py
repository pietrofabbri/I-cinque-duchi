"""Costruisce gli ambienti dei centocinquanta livelli: uno per livello, tutti.

`videogioco-5-duchi-tappa-1-01.md` §3 descrive **una** zona percorribile, quella
della piazza della Cattedrale, e la chiama «il modello per le altre 29». Questo
file costruisce le altre 149, e le costruisce tutte allo stesso modo: non disegna
niente, ma fissa **che cosa serve** a ogni livello e **che cosa si sa davvero**,
perche' il motore non abbia da indovinare.

**Perche' tutti e non uno.** La tappa 1-1 e' l'unica che ha una zona percorribile
costruita, e per questo il progetto rischiava di fermarsi li'. Ma gli ambienti non
sono un extra: sono cio' che distingue il gioco da una scheda. Senza ambiente un
livello e' una domanda con un'immagine accanto; con l'ambiente e' un posto dove
si sta. E la parte difficile non e' disegnarli: e' sapere, per ognuno, se il
posto esiste, dove sta e che cosa si sa delle sue case. Quel conto si fa una
volta sola, in un file, e da li' in poi e' un dato.

**Le fonti, e da dove viene ogni cosa.** Il file non sceglie i luoghi: li legge
dai documenti che il progetto ha gia' scritti e verificati.

  il livello       dalla tabella «Le 30 tappe» di ciascun anno: `anno1-mappa.md`
                   2 e `anno2..5` 4. Cinque tavole di trenta righe: 150 livelli,
                   e non uno di piu' o di meno, perche' il conto e' verificabile
  il luogo         anno 1 dalla tabella delle coordinate di `anno1-mappa.md` 3,
                   che sono gia' verificate sul dataset dei numeri civici del
                   Comune; anni 2-5 da `luoghi_gioco.json`, campo `tappe`, che
                   collega ogni livello al suo luogo senza dover confrontare i
                   nomi a mano
  le sagome        da `edifici_footprint.json`, per i luoghi che ne hanno
  il fondo         da `ferrara_fondo.json`, solo per l'anno 1, che e' l'unico
                   anno che si gioca dentro Ferrara

**Il confronto dei nomi e' evitato apposta.** Il primo tentativo di questo file
ha provato ad abbinare «Bolzano, Museo archeologico altoatesino» della tabella
del secondo anno con «Bolzano» di `luoghi_gioco.json` confrontando le stringhe.
Sarebbe finito bene per caso: la parola che distingue due luoghi e' spesso
l'articolo, e il confronto fallisce su «il Cairo e le carovane». Il campo `tappe`
esiste gia' e fa il lavoro per relazione esplicita.

**Il tipo di ambiente e' una parola chiave, e lo dichiara.** `piazza`, `citta`,
`edificio`, `porta`, `area`, `percorso`, `situazione` vengono dal campo `tipo` di
`luoghi_gioco.json` o da una parola del nome. E' una euristica, non un
rilevamento: il campo `tipo_da` dice sempre donde viene, cosi' chi legge sa che
una parola ha deciso e non un architetto.

**Cosa resta vuoto, e resta dichiarato.** Un ambiente senza coordinate non si
posiziona, e un ambiente senza sagome non ha case. Il file non riempie: elenca i
vuoti di ogni livello in `vuoti`, cosi' il motore sa cosa non disegnare e la
scheda sa cosa dire.

Uso:  python3 sorgenti/ambienti_livelli.py
      python3 sorgenti/ambienti_livelli.py --prova        # non scrive
"""
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(RADICE, "docs")
LUOGHI = os.path.join(RADICE, "dati", "luoghi_gioco.json")
FOOTPRINT = os.path.join(RADICE, "dati", "edifici_footprint.json")
FONDO = os.path.join(RADICE, "dati", "ferrara_fondo.json")
USCITA = os.path.join(RADICE, "dati", "ambienti_livelli.json")

# Le cinque tabelle dei livelli. Il numero e' la posizione della sezione dentro il
# documento: cambiare l'ordine delle sezioni romperebbe il file, e va detto.
TABELLE = [
    {"anno": 1, "file": "videogioco-5-duchi-anno1-mappa.md",
     "sezione": "## 2. Le 30 tappe",
     "colonne": {"livello": 0, "luogo": 1, "voce": 2, "argomento": 3,
                 "forza": 5}},
    {"anno": 2, "file": "videogioco-5-duchi-anno2-penisola.md",
     "sezione": "## 4. Le 30 tappe",
     "colonne": {"livello": 0, "argomento": 1, "strato": 2, "luogo": 3,
                 "voce": 4, "forza": 6}},
    {"anno": 3, "file": "videogioco-5-duchi-anno3-europa.md",
     "sezione": "## 4. Le 30 tappe",
     "colonne": {"livello": 0, "argomento": 1, "strato": 2, "luogo": 3,
                 "voce": 4, "forza": 6}},
    {"anno": 4, "file": "videogioco-5-duchi-anno4-mondo.md",
     "sezione": "## 4. Le 30 tappe",
     "colonne": {"livello": 0, "argomento": 1, "strato": 2, "luogo": 3,
                 "voce": 4, "porta": 5, "forza": 7}},
    {"anno": 5, "file": "videogioco-5-duchi-anno5-mondo.md",
     "sezione": "## 4. Le 30 tappe",
     "colonne": {"livello": 0, "argomento": 1, "strato": 2, "luogo": 3,
                 "stanza": 4, "voce": 5, "porta": 6, "forza": 8}},
]

# La griglia di ogni tipo di ambiente. I numeri sono una scelta di progetto, non
# un dato: vengono dalla zona della tappa 1-1 (22 x 14 tessere da 1,25 m) per il
# tipo `piazza`, e gli altri tipi sono scalati da li' secondo quanto e' grande il
# posto. Sono dichiarati qui e nel file prodotto, e sono i numeri che il progetto
# puo' cambiare da un giorno all'altro senza toccare il codice.
GRIGLIE = {
    "piazza":       {"colonne": 22, "righe": 14, "scala_m_per_tessera": 1.25},
    "citta":        {"colonne": 30, "righe": 22, "scala_m_per_tessera": 1.5},
    "edificio":     {"colonne": 16, "righe": 12, "scala_m_per_tessera": 1.25},
    "porta":        {"colonne": 18, "righe": 14, "scala_m_per_tessera": 1.25},
    "percorso":     {"colonne": 34, "righe": 10, "scala_m_per_tessera": 1.5},
    "area":         {"colonne": 34, "righe": 26, "scala_m_per_tessera": 2.0},
    "citta_antica": {"colonne": 30, "righe": 22, "scala_m_per_tessera": 1.5},
    "situazione":   {"colonne": 24, "righe": 18, "scala_m_per_tessera": 1.5},
    "paesaggio":    {"colonne": 40, "righe": 30, "scala_m_per_tessera": 2.0},
}
GRIGLIA_DI_DEFAULT = GRIGLIE["paesaggio"]

# La parola che decide il tipo, quando il campo `tipo` non c'e'. E' un'euristica e
# il file lo dichiara: se domani un posto si chiama «Piazza del Campo» ma e' una
# citta', questa tabella lo mette fra le piazze, e nessuno se ne accorge senza
# guardare `tipo_da`.
PAROLE = [
    ("piazza", "piazza"), ("campo", "piazza"), ("platz", "piazza"),
    ("cattedrale", "edificio"), ("duomo", "edificio"), ("basilica", "edificio"),
    ("chiesa", "edificio"), ("moschea", "edificio"), ("tempio", "edificio"),
    ("santuario", "edificio"), ("castello", "edificio"), ("palazzo", "edificio"),
    ("biblioteca", "edificio"), ("museo", "edificio"), ("universita", "edificio"),
    ("ospedale", "edificio"), ("monastero", "edificio"), ("abbazia", "edificio"),
    ("porta", "porta"), ("gate", "porta"),
    ("strada", "percorso"), ("via", "percorso"), ("ponte", "percorso"),
    ("stazione", "percorso"), ("porto", "percorso"), ("canale", "percorso"),
    ("addizione", "area"), ("parco", "area"), ("orto", "area"),
    ("giardino", "area"), ("cimitero", "area"), ("certosa", "area"),
    ("rovina", "citta_antica"), ("tell", "citta_antica"), ("mohenjo", "citta_antica"),
    ("sepolto", "citta_antica"), ("acropoli", "citta_antica"),
    ("canale", "percorso"), ("fiume", "percorso"), ("lago", "paesaggio"),
    ("deserto", "paesaggio"), ("foresta", "paesaggio"), ("vulcano", "paesaggio"),
    ("marina", "paesaggio"), ("isola", "paesaggio"),
]


def testo_tabella(percorso, sezione):
    with open(percorso, encoding="utf-8") as f:
        testo = f.read()
    if sezione not in testo:
        return []
    corpo = testo.split(sezione, 1)[1]
    corpo = re.split(r"\n## ", corpo, 1)[0]
    out = []
    for riga in corpo.splitlines():
        if not re.match(r"^\|\s*\*?\*?\d-\d+", riga):
            continue
        celle = [c.strip() for c in riga.strip().strip("|").split("|")]
        if len(celle) < 3:
            continue
        out.append(celle)
    return out


def pulisci(testo):
    """Togli il grassimo e il codice dalle celle delle tabelle."""
    testo = (testo or "").strip()
    testo = re.sub(r"\*\*(.+?)\*\*", r"\1", testo)
    testo = re.sub(r"`(.+?)`", r"\1", testo)
    testo = re.sub(r"\[(.+?)\]\(.*?\)", r"\1", testo)
    return testo.strip()


def tipo_ambiente(nome, tipo_registrato):
    """Il tipo di ambiente, e da dove viene. Sempre entrambi."""
    if tipo_registrato:
        return tipo_registrato, "luoghi_gioco.tipo"
    basso = (nome or "").lower()
    for parola, tipo in PAROLE:
        if parola in basso:
            return tipo, "parola_chiave:" + parola
    return "paesaggio", "nessuna_parola_chiave"


def main():
    solo_prova = "--prova" in sys.argv

    # --- i 150 livelli, dalle cinque tabelle dei documenti
    livelli = {}
    for t in TABELLE:
        righe = testo_tabella(os.path.join(DOCS, t["file"]), t["sezione"])
        for celle in righe:
            col = t["colonne"]
            lid = pulisci(celle[col["livello"]])
            if not re.match(r"^\d-\d+$", lid):
                continue
            livelli[lid] = {
                "livello": lid,
                "anno": t["anno"],
                "numero": int(lid.split("-")[1]),
                "argomento": pulisci(celle[col["argomento"]]) if "argomento" in col else "",
                "luogo_testo": pulisci(celle[col["luogo"]]),
                "voce": pulisci(celle[col["voce"]]) if "voce" in col else "",
                "forza": pulisci(celle[col["forza"]]) if "forza" in col else "",
                "strato": pulisci(celle[col["strato"]]) if "strato" in col else None,
                "porta": pulisci(celle[col["porta"]]) if "porta" in col else None,
                "stanza": pulisci(celle[col["stanza"]]) if "stanza" in col else None,
            }
    print("livelli letti dalle tabelle: %d" % len(livelli))

    # --- il luogo di ogni livello
    with open(LUOGHI, encoding="utf-8") as f:
        gj = json.load(f)
    per_tappa = {}
    for l in gj["luoghi"]:
        for t in (l.get("tappe") or []):
            per_tappa[t] = l
    stanze = {t["tappa"]: t for t in gj.get("tappe", []) if "tappa" in t}

    # --- l'anno 1 ha le coordinate in anno1-mappa.md 3, non in luoghi_gioco.json
    percorso_anno1 = os.path.join(DOCS, "videogioco-5-duchi-anno1-mappa.md")
    coord_anno1 = {}
    with open(percorso_anno1, encoding="utf-8") as f:
        testo = f.read().split("## 3. Posizione precisa dei punti", 1)[1]
    for riga in testo.split("## 4.")[0].splitlines():
        if not re.match(r"^\|\s*\d-\d+", riga):
            continue
        c = [x.strip() for x in riga.strip().strip("|").split("|")]
        if len(c) < 5:
            continue
        try:
            coord_anno1[c[0]] = {"luogo": c[1], "lat": float(c[3]),
                                 "lon": float(c[4])}
        except ValueError:
            continue
    print("tappe dell'anno 1 con coordinate: %d" % len(coord_anno1))

    # --- sagome e fondo
    sagome = {}
    if os.path.exists(FOOTPRINT):
        with open(FOOTPRINT, encoding="utf-8") as f:
            fp = json.load(f)
        for e in fp["edifici"]:
            sagome.setdefault(e["luogo"], []).append(e)
    fondo = None
    if os.path.exists(FONDO):
        with open(FONDO, encoding="utf-8") as f:
            fondo = json.load(f)
    print("luoghi con sagome: %d" % len(sagome))

    ambienti, problemi = [], []
    for lid in sorted(livelli, key=lambda x: (int(x.split("-")[0]),
                                              int(x.split("-")[1]))):
        v = livelli[lid]
        luogo = per_tappa.get(lid)
        vuoti = []
        nome = v["luogo_testo"]

        if v["anno"] == 1:
            c = coord_anno1.get(lid)
            if c:
                nome, lat, lon = c["luogo"], c["lat"], c["lon"]
                stato, fonte = "verificata", "anno1-mappa.md 3 (civici Comune)"
            else:
                lat = lon = None
                stato, fonte = "assente", "nessuna fonte"
                vuoti.append("senza_coordinate")
        elif luogo:
            nome = luogo["luogo"]
            lat, lon = luogo.get("lat"), luogo.get("lon")
            stato = luogo.get("coord_stato")
            fonte = luogo.get("fonte_coord")
            if stato != "verificata":
                vuoti.append("coordinate_" + str(stato))
        else:
            lat = lon = None
            stato, fonte = "assente", "nessuna fonte"
            vuoti.append("senza_luogo_in_luoghi_gioco")

        tipo, tipo_da = tipo_ambiente(nome, luogo.get("tipo") if luogo else None)

        # le sagome: per chiave di luogo, che e' il nome in luoghi_gioco.json
        ed = sagome.get(nome if luogo else "", [])
        edifici = {"fonte": "dati/edifici_footprint.json",
                   "n": len(ed),
                   "con_altezza": sum(1 for e in ed
                                      if e["fonte_altezza"] == "osm_height"),
                   "da_piani": sum(1 for e in ed
                                   if e["fonte_altezza"] == "osm_levels"),
                   "senza_altezza": sum(1 for e in ed
                                        if e["fonte_altezza"] == "assente")}
        if not ed:
            vuoti.append("senza_sagome_osm")
        if edifici["n"] and edifici["senza_altezza"] == edifici["n"]:
            vuoti.append("sole_sagome_senza_altezza")

        griglia = GRIGLIE.get(tipo, GRIGLIA_DI_DEFAULT)
        se_stanza = stanze.get(lid)
        amb = {
            "tipo": tipo,
            "tipo_da": tipo_da,
            "griglia": griglia,
            "griglia_da": "GRIGLIE di sorgenti/ambienti_livelli.py: scelta di "
                          "progetto, non un dato della fonte",
            "edifici": edifici,
            "fondo": ("dati/ferrara_fondo.json" if (v["anno"] == 1 and fondo)
                      else None),
            "orientamento": None,
            "nomi_edifici": sorted({e["nome"] for e in ed if e.get("nome")})[:12],
            "stato": ("costruito" if lid == "1-1" else "da_costruire"),
            "costruito_in": ("videogioco-5-duchi-tappa-1-01.md 3" if lid == "1-1"
                             else None),
            "paleta": ["sfondo", "inchiostro", "terra_gialla", "terra_rossa",
                       "azzurro_oltremare", "oro"],
            "paleta_fonte": "dati/fonti_visive/tavolozza.json",
        }
        if v["anno"] == 1 and not amb["fondo"]:
            vuoti.append("senza_fondo_ferrara")
        if amb["orientamento"] is None:
            vuoti.append("orientamento_non_dichiarato")

        ambienti.append({
            "livello": lid, "anno": v["anno"], "numero": v["numero"],
            "argomento": v["argomento"], "voce": v["voce"],
            "forza": v["forza"], "strato": v["strato"], "porta": v["porta"],
            "stanza": v["stanza"],
            "stanza_dettaglio": (se_stanza or {}).get("stanza"),
            "luogo": nome, "lat": lat, "lon": lon,
            "coord_stato": stato, "fonte_coord": fonte,
            "terreno": (luogo or {}).get("terreno"),
            "ambiente": amb, "vuoti": sorted(set(vuoti)),
        })

    # --- il conto, che e' la parte che serve
    attesi = ["%d-%d" % (a, n) for a in range(1, 6) for n in range(1, 31)]
    mancanti = [t for t in attesi if t not in livelli]
    con_coord = [a for a in ambienti if a["lat"] is not None]
    con_sagome = [a for a in ambienti if a["ambiente"]["edifici"]["n"] > 0]
    per_tipo = {}
    for a in ambienti:
        per_tipo[a["ambiente"]["tipo"]] = per_tipo.get(
            a["ambiente"]["tipo"], 0) + 1

    print("\nambienti: %d (attesi %d)" % (len(ambienti), len(attesi)))
    if mancanti:
        print("  LIVELLI MANCANTI: %s" % ", ".join(mancanti))
    print("  con coordinate: %d su %d" % (len(con_coord), len(ambienti)))
    print("  con sagome OSM: %d" % len(con_sagome))
    print("  per tipo: %s" % ", ".join("%s %d" % kv for kv in
                                      sorted(per_tipo.items())))
    if solo_prova:
        return 0

    doc = {
        "versione": 1,
        "data": "2026-10-03",
        "scopo": "un ambiente per ogni livello: che cosa serve a ciascuno e che "
                 "cosa si sa davvero. Il file non disegna e non sceglie i "
                 "luoghi: li legge dai documenti del progetto e dichiara i "
                 "vuoti",
        "il_modello": "videogioco-5-duchi-tappa-1-01.md 3 (piazza della "
                      "Cattedrale), l'unica zona gia' costruita: e' il modello, "
                      "e tutti gli altri centoquarantanove ambienti hanno la sua "
                      "stessa forma",
        "come_sono_costruiti": [
            "il livello dalla tabella «Le 30 tappe» del suo anno",
            "il luogo dell'anno 1 da anno1-mappa.md 3, che ha le coordinate "
            "verificate sui numeri civici del Comune; degli anni 2-5 da "
            "luoghi_gioco.json campo `tappe`, che collega per relazione "
            "esplicita e non per confronto di nomi",
            "le sagome da edifici_footprint.json, per il nome che li ha nel "
            "registro dei luoghi",
            "il fondo da ferrara_fondo.json, e solo per l'anno 1, che e' "
            "l'unico anno che si gioca dentro Ferrara",
        ],
        "griglie": GRIGLIE,
        "griglie_nota": "colonne, righe e scala sono una scelta di progetto, non "
                        "un dato di una fonte: stanno tutte qui perche' il "
                        "motore le legga e nessuno le riscriva nel codice",
        "parole_tipo": {p: t for p, t in PAROLE},
        "parole_tipo_nota": "euristica dichiarata: quando il campo `tipo` del "
                            "registro dei luoghi c'e' ha la precedenza, e "
                            "ogni ambiente dice in `tipo_da` quale delle due "
                            "strade ha preso",
        "riepilogo": {
            "ambienti": len(ambienti),
            "attesi": len(attesi),
            "mancanti": mancanti,
            "con_coordinate": len(con_coord),
            "senza_coordinate": [a["livello"] for a in ambienti
                                 if a["lat"] is None],
            "con_sagome": len(con_sagome),
            "per_tipo": per_tipo,
            "costruiti": [a["livello"] for a in ambienti
                          if a["ambiente"]["stato"] == "costruito"],
        },
        "vuoti_dichiarati": {
            "orientamento": "ogni ambiente ha l'orientamento a null e il vuoto in "
                            "`vuoti`: la tappa 1-1 ha un orientamento dichiarato "
                            "(la facciata guarda verso chi gioca) e gli altri "
                            "149 no. Dichiararlo vuol dire che il motore non "
                            "deve sceglierlo da solo",
            "edifici": "i luoghi senza sagome sono quelli che OSM non copre o "
                       "che non sono un luogo reale: si vede da `vuoti`",
            "anno_1": "1-27 e 1-30 non hanno coordinate nella tabella di "
                      "anno1-mappa.md 3 e non si possono posizionare",
        },
        "ambienti": ambienti,
    }
    with open(USCITA, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print("scritto %s (%.0f kB)"
          % (os.path.relpath(USCITA, RADICE), os.path.getsize(USCITA) / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main())