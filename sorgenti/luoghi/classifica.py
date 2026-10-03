"""Unisce l'inventario dei luoghi, le coordinate e la classificazione in un solo
record che il motore grafico può leggere.

La classificazione è la parte che conta. I 41 luoghi che Wikipedia non risolve
non sono 41 errori: sono cinque tipi diversi di cosa, e ognuno si disegna in un
modo diverso.

| `tipo` | Che cos'è | Quanti | Come si disegna |
|---|---|---|---|
| `citta` | una città | 44 | mappa, edifici per tipologia ed epoca |
| `edificio` | un palazzo, una basilica, una cattedrale | 7 | sagoma singola, con la sua cronologia |
| `area` | una zona urbana con un nome proprio (Addizione Erculea, Villa dei Gracchi) | 5 | polilinea d'area, edifici dentro |
| `percorso` | due o più luoghi insieme: «Il Cairo e le caravane» | 13 | strada che unisce, con i due capi |
| `porta` | una porta di gioco: `PT-COL` (Ferrara) | 4 | non si disegna: è un'uscita dal nodo |
| `situazione` | il luogo è un contesto, non un posto: «una sala di riunione, 1983» | 8 | non si disegna: il 5º anno non si sposta sulla mappa |

Le ultime due righe sono una scoperta, non una difficoltà: in quarantuno casi su
centoventi, la casella «Luogo (pin)» **non contiene un luogo**. Nel quinto anno
per costruzione, e in quattro anni per le porte. Il motore deve saperlo, e deve
sapere che in quei casi non deve cercare coordinate.
"""
import json
import os
import re

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ESTRATTI = os.path.join(RADICE, "dati", "luoghi_estratti.json")
GEO = os.path.join(RADICE, "dati", "luoghi_geo.jsonl")
CORREZIONI = os.path.join(RADICE, "dati", "luoghi_correzioni.json")
USCITA = os.path.join(RADICE, "dati", "luoghi_gioco.json")


def le_correzioni():
    """Le correzioni di coordinate che i controlli hanno trovato.

    Vivono in `dati/luoghi_correzioni.json` e non dentro `luoghi_geo.jsonl` di
    proposito: quel file e' la fotografia di quello che il geocodificatore aveva
    trovato, e riscriverlo a mano avrebbe cancellato la traccia dell'errore. Il
    02/10/2026 due coordinate corrette vivevano solo in un JSON editato a mano
    e in nessun altro posto, cosi' che rifare il registro le cancellava.
    """
    if not os.path.exists(CORREZIONI):
        return {}
    archivio = json.load(open(CORREZIONI, encoding="utf-8"))
    return {c["luogo"]: c for c in archivio.get("correzioni", [])}


def applica_correzione(g, c):
    """Mette i numeri corretti dentro il record, e li prende come numeri.

    Non dalla frase: un valore scritto dentro una stringa da smontare e' un
    valore che un giorno non viene smontato e resta sbagliato in silenzio.
    """
    if not isinstance(c.get("lat"), (int, float)) or not isinstance(c.get("lon"), (int, float)):
        return False
    g["lat"], g["lon"] = c["lat"], c["lon"]
    if c.get("titolo_risolto"):
        g["titolo_risolto"] = c["titolo_risolto"]
    elif not g.get("titolo_risolto"):
        g["titolo_risolto"] = c["luogo"]
    g["wiki"] = c.get("wiki", g.get("wiki", "it"))
    return True

# nomi che sono un percorso: due o piu' toponimi uniti da una congiunzione.
# Si riconoscono dalla forma, non da una lista scritta a parte, cosi' un tappa
# nuova che usa la stessa forma viene classificata bene senza toccare nulla.
PERCORSO = re.compile(r"\be\b.*\be\b|^\S+\s+e\s+\S+", re.I)
# un luogo con una data fra parentesi o dopo virgola e' un contesto
CONTESTO = re.compile(r",\s*(1[89]\d\d|20\d\d)\b|^(un|una|il|lo)\s", re.I)
PORTA = re.compile(r"^Porta\s+`PT-[A-Z]{3}`")

# dentro «Citta', cosa», la seconda parte dice che genere di cosa e'. Senza questa
# regola tredici schede finivano classificate come citta': sono un palazzo, una
# villa, un convento e un'area urbana, e si disegnano in tre modi diversi.
# La prima versione le chiamava tutte «citta'» ed e' stata vista dal fatto che
# nessuna di esse ha coordinate su Wikipedia, mentre tutte hanno coordinate nel
# WFS del loro Comune.
EDIFICI = re.compile(
    r"\b(corte|archivio|cappella|fonderia|sala|palazzo|basilica|cattedrale|duomo|"
    r"curia|villa|monastero|monastero|convento|abbazia|museo|sinagoga|teatro|"
    r"castello|borgo|broad street|mausoleo)\b", re.I)
AREA = re.compile(r"\b(zona|area|quartiere|contrada|campidoglio|addizione|"
                  r"perimetro|delta|valle)\b", re.I)


def che_tipo(nome):
    """(tipo, perche') — il perche' spiega la classificazione, non la scusa."""
    if PORTA.match(nome):
        return "porta", "porta di gioco, non e' un luogo: e' un'uscita dal nodo"
    if CONTESTO.search(nome):
        return ("situazione",
                "la casella non contiene un luogo ma una situazione: nel quinto "
                "anno la tappa e' un metodo, non un posto")
    parti = [p.strip() for p in re.split(r"\be\b", nome) if p.strip()]
    if len(parti) > 1:
        return "percorso", "due o piu' luoghi nella stessa casella: e' una strada, non un punto"
    if "," in nome:
        secondo = nome.split(",", 1)[1]
        if EDIFICI.search(secondo):
            return "edificio", "un edificio dentro la citta': ha una sagoma e una cronologia sue"
        if AREA.search(secondo):
            return "area", "una zona urbana con un nome proprio: si disegna come un'area, non come un punto"
    if nome in ("Tebe", "Babilonia", "Elea (Velia)", "Uruk", "Agra", "Karakorum",
                "Uppsala", "Hannover", "Bethesda", "Pataliputra"):
        return "citta_antica", "citta' antica, scomparsa o spostata: il rilievo moderno non dice niente"
    return "citta", None


def stato_di(nome, tipo, geo, presente):
    """Lo stato della coordinata, in un posto solo.

    La funzione era dentro il `main` di questo file e una copia ne faceva
    `aggiorna_registro.py`: due copie di una regola che assegna quattro stati
    a novantacinque luoghi divergono appena una delle due viene toccata, ed e'
    successo (le sette ferraresi finivano `non_e_un_luogo` da una parte e
    `da_geocodificare_wfs` dall'altra). Ora c'e' una sola definizione e gli
    altri script la importano.

    `presente` dice se il nome e' passato dal geocodificatore. Un luogo che
    non e' mai stata cercata non e' una richiesta fallita, e non si chiama
    `da_rifare` — si chiama `da_geocodificare_a_mano`, perche' il lavoro da
    fare e' un altro e si sa quale.
    """
    if geo.get("titolo_risolto"):
        stato = "verificata"
    elif tipo in ("porta", "situazione", "percorso"):
        stato = "non_e_un_luogo"
    elif geo.get("stato") == "senza_articolo" or not presente:
        stato = "da_geocodificare_a_mano"
    else:
        stato = "da_rifare"
    # dentro Ferrara la fonte non e' Wikipedia ma il WFS del Comune, ed esiste
    if nome.startswith("Ferrara") and stato != "verificata":
        stato = "da_geocodificare_wfs"
    return stato


if __name__ == "__main__":
    estratti = json.load(open(ESTRATTI, encoding="utf-8"))
    geo = {}
    for riga in open(GEO, encoding="utf-8"):
        riga = riga.strip()
        if not riga:
            continue
        d = json.loads(riga)
        if d.get("stato") == "da_rifare":
            continue
        geo[d["luogo"]] = d
    corretti = le_correzioni()
    applicate = []

    # tappe per luogo
    tappe = {}
    anno = {}
    for t in estratti["tappe"]:
        tappe.setdefault(t["luogo"], []).append(t["tappa"])
        anno.setdefault(t["luogo"], set()).add(t["anno"])

    record = []
    import collections
    conta = collections.Counter()
    stati = collections.Counter()
    for nome in sorted(tappe):
        tipo, nota = che_tipo(nome)
        conta[tipo] += 1
        g = dict(geo.get(nome, {}))
        presente = nome in geo
        stato = stato_di(nome, tipo, g, presente)
        # le correzioni che i controlli hanno trovato vengono applicate qui, e
        # non nel file delle risoluzioni: quel file resta la fotografia di
        # quello che il geocodificatore aveva trovato il 02/10/2026.
        c = corretti.get(nome)
        if c:
            applicata = applica_correzione(g, c)
            if applicata:
                applicate.append(nome)
                stato = "verificata"
                nota = (nota + " " if nota else "") + (
                    "Correzione del %s: %s" % (c["data"], c["difetto"].rstrip(".")))
        stati[stato] += 1
        r = {
            "luogo": nome,
            "tipo": tipo,
            "tappe": sorted(tappe[nome]),
            "anni": sorted(anno[nome]),
            "pin": len(tappe[nome]),
            "lat": g.get("lat"),
            "lon": g.get("lon"),
            "articolo": g.get("titolo_risolto"),
            "fonte_coord": ("wikipedia:" + g["wiki"]) if g.get("titolo_risolto") else None,
            "coord_stato": stato,
            "perche": nota,
            "dettagli": [],      # si compila a mano, con la fonte: vedi il documento
        }
        if c:
            r["correzione"] = {
                "dall_articolo": c["dall_articolo"],
                "correzione": c["correzione"],
                "fonte": c["fonte"],
                "controllo": c["controllo"],
            }
        record.append(r)

    with open(USCITA, "w", encoding="utf-8") as f:
        json.dump({"luoghi": record}, f, ensure_ascii=False, indent=1)

    con_coord = sum(1 for r in record if r["lat"] is not None)
    if applicate:
        print("\ncorrezioni applicate: %d (%s)"
              % (len(applicate), ", ".join(applicate)))
    print("luoghi: %d" % len(record))
    print("\nper tipo:")
    for t, n in conta.most_common():
        print("  %-14s %3d" % (t, n))
    print("\nper stato della coordinata:")
    for s, n in stati.most_common():
        print("  %-30s %3d" % (s, n))
    print("\ncon coordinate verificate: %d su %d" % (con_coord, len(record)))
    print("scritto %s" % USCITA)
