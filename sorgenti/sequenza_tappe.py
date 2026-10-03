#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mette in sequenza le trenta tappe degli anni 2, 3 e 4: luogo, voce, mezzo, distanza.

Il progetto ha gia' tutto, ma in tre pezzi separati: la tabella delle trenta
tappe sta nel documento dell'anno, le coordinate stanno in `dati/luoghi_gioco.json`
e le tappe che il registro non puo' verificare stanno in `dati/ipotesi_luoghi.json`.
Nessuno dei tre dice **in che ordine** il duca incontra le persone. Questo file
unisce i tre pezzi e produce due cose: `dati/sequenza_tappe.json`, che e' il dato,
e le tre tabelle dentro `docs/videogioco-5-duchi-sequenza.md`, che sono la sua
lettura. Il documento non si scrive a mano: se il generatore non lo aggiorna, la
tabella mente e nessuno se ne accorge.

**Le voci obbligatorie vengono dai documenti, non da qui.** Il generatore legge la
colonna `Voce` delle trenta righe di ogni anno e mette in sequenza quelle, che sono
le trenta persone che il giocatore incontra per forza. Le facoltative stanno nella
colonna apposita e vengono tenute **fuori** dalla sequenza: sono facoltative per
definizione, e una sequenza che le include mente sul suo percorso.

Uso:
    python3 sorgenti/sequenza_tappe.py            # scrive il JSON e le tabelle
    python3 sorgenti/sequenza_tappe.py --anno 3   # solo un anno, in chiaro
"""
import io
import json
import os
import re
import sys

RADICE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS = os.path.join(RADICE, "docs")
LUOGHI = os.path.join(RADICE, "dati", "luoghi_gioco.json")
IPOTESI = os.path.join(RADICE, "dati", "ipotesi_luoghi.json")
JSON_OUT = os.path.join(RADICE, "dati", "sequenza_tappe.json")
DOC_OUT = os.path.join(DOCS, "videogioco-5-duchi-sequenza.md")

INIZIO = "<!-- SEQUENZA:INIZIO -->"
FINE = "<!-- SEQUENZA:FINE -->"

DOCUMENTI = {2: "videogioco-5-duchi-anno2-penisola.md",
             3: "videogioco-5-duchi-anno3-europa.md",
             4: "videogioco-5-duchi-anno4-mondo.md"}

# Chilometri al giorno, dal file che gia' li dichiara (`percorsi_calcola.py`).
# Non si ricavano qui: un percorso che usa velocita' diverse da quelle dichiarate
# nel documento dei percorsi darebbe due numeri per la stessa strada.
KM_GIORNO = {2: ("cavallo", 45), 3: ("cavallo", 45), 4: ("barca", 60)}

# Le tappe per le quali il registro dei luoghi e il documento d'anno non dicono
# la stessa cosa. Una che c'e' qui e' una domanda dichiarata; una che il
# confronto trova e non c'e' qui e' un difetto, ed e' quello che si vuole.
DICHIARATE = {
    "3-28": "Manchester nel registro, Torino nel documento. Il livello e' JavaScript e "
            "Manchester e' il luogo del calcolatore (il 3-28 e' il primo dei livelli del "
            "Novecento); Primo Levi, aggiunto il 02/10/2026, e' torinese. Il documento ha "
            "scelto la persona e il luogo della persona, il registro ha quello del livello. "
            "**La scelta e' di Pietro e non e' presa qui**: finche' non e' decisa, la tappa "
            "ha due luoghi e il dato li dichiara entrambi",
}
RAGGIO = 6371.0


def leggi(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def haversine(lat1, lon1, lat2, lon2):
    import math
    f1, f2 = math.radians(lat1), math.radians(lat2)
    dlat = f2 - f1
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(f1) * math.cos(f2) * math.sin(dlon / 2) ** 2
    return 2 * RAGGIO * math.asin(math.sqrt(a))


def normalizza(nome):
    import unicodedata
    s = unicodedata.normalize("NFKD", nome.lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def indice_colonne(riga):
    """Le colonne cambiano fra gli anni: il quarto anno ha anche la porta e il
    confronto. Si legge l'intestazione, non si contano le barre."""
    celle = [c.strip() for c in riga.strip().strip("|").split("|")]
    out = {}
    for i, nome in enumerate(celle):
        if nome == "Livello":
            out["livello"] = i
        elif nome.startswith("Luogo (pin)") or nome == "Pin":
            out["luogo"] = i
        elif nome == "Voce":
            out["voce"] = i
        elif nome == "Forza":
            out["forza"] = i
        elif nome == "Porta":
            out["porta"] = i
        elif nome.startswith("Facoltativi"):
            out["facoltativi"] = i
        elif nome == "Argomento":
            out["argomento"] = i
        elif nome == "Strato":
            out["strato"] = i
    return out


def tabella_tappe(testo):
    """Le trenta righe della tabella delle tappe, con l'intestazione."""
    righe = testo.split("\n")
    for i, riga in enumerate(righe):
        if riga.startswith("| Livello |"):
            cols = indice_colonne(riga)
            out = []
            for r in righe[i + 2:]:
                if not r.startswith("|"):
                    if out:
                        break
                    continue
                celle = [c.strip() for c in r.strip().strip("|").split("|")]
                if len(celle) < len(cols) or not re.match(r"^\*\*\d+-\d+\*\*$", celle[cols["livello"]]):
                    continue
                out.append(celle)
            return cols, out
    return None, []


def voce(cella):
    """`Ötzi` (Q01) -> nome e codice; `un collettivo` -> nome e nessun codice."""
    m = re.match(r"^\*\*(.+?)\*\*\s*\((\w+)\)\s*$", cella)
    if m:
        return m.group(1).strip(), m.group(2)
    return cella.replace("**", "").strip(), None


def facoltativi(cella):
    """`A; B (facoltativa)` -> due nomi. La colonna puo' essere troncata nei
    documenti, e cio' si dichiara: quello che c'e' si mette, quello che manca no."""
    if not cella:
        return [], True
    out = []
    for pezzo in cella.split(";"):
        nome = re.sub(r"\(facoltativ[ao]\)?", "", pezzo, flags=re.I)
        nome = re.sub(r"\(.*?\)", "", nome).replace("**", "").strip(" .")
        if nome:
            out.append(nome)
    return out, False


def main():
    solo = None
    if "--anno" in sys.argv:
        solo = int(sys.argv[sys.argv.index("--anno") + 1])

    luoghi = json.loads(leggi(LUOGHI))
    ipotesi = {h["tappa"]: h for h in json.loads(leggi(IPOTESI))["ipotesi"]}

    # coordinate: prima il registro, poi l'ipotesi dichiarata
    coords = {}
    for l in luoghi.get("luoghi", []):
        if l.get("lat") is not None and l.get("lon") is not None:
            coords[normalizza(l["luogo"])] = (l["lat"], l["lon"], "registro")
    for h in ipotesi.values():
        if h.get("lat") is not None:
            coords[normalizza(h["luogo"])] = (h["lat"], h["lon"],
                                              "ipotesi_%s" % h["grado"])

    # tappa -> luogo, secondo il registro: serve a confrontare le due fonti
    per_tappa = {}
    stato_per_tappa = {}
    for l in luoghi.get("luoghi", []):
        for tp in l.get("tappe", []):
            per_tappa.setdefault(tp, l["luogo"])
            stato_per_tappa.setdefault(tp, l.get("coord_stato"))

    anni = {}
    for anno, nome_doc in sorted(DOCUMENTI.items()):
        if solo and anno != solo:
            continue
        testo = leggi(os.path.join(DOCS, nome_doc))
        cols, righe = tabella_tappe(testo)
        # un documento d'anno puo' citare le tappe di un altro anno (l'anno 3
        # riprende l'anno 2): qui si tiene solo l'anno che si sta costruendo
        righe = [r for r in righe
                 if re.match(r"^\*\*%d-\d+\*\*$" % anno, r[cols["livello"]])]
        if not righe:
            print("anno %d: nessuna tabella delle tappe trovata" % anno)
            return 2
        mezzo, km_giorno = KM_GIORNO[anno]
        tappe = []
        for celle in righe:
            # `**3-13**` e' anno 3, tappa 13: togliere i caratteri non numerici
            # darebbe 313, che e' un tappa che non esiste
            m = re.match(r"^\*\*(\d+)-(\d+)\*\*$", celle[cols["livello"]])
            if not m:
                continue
            numero = int(m.group(2))
            nome, codice = voce(celle[cols["voce"]])
            fac, troncata = facoltativi(celle[cols["facoltativi"]])
            luogo = celle[cols["luogo"]]
            punto = coords.get(normalizza(luogo))
            tappe.append({
                "ordine": numero,
                "tappa": "%d-%d" % (anno, numero),
                "argomento": celle[cols["argomento"]],
                "strato": celle[cols["strato"]].strip("`"),
                "luogo": luogo,
                "voce": nome,
                "voce_id": codice,
                "forza": celle[cols["forza"]],
                "porta": celle[cols["porta"]].strip("`") if "porta" in cols else None,
                "facoltativi": fac,
                "facoltativi_troncate": troncata,
                "luogo_registro": None,
                "punto_stato": stato_per_tappa.get("%d-%d" % (anno, numero)),
                "punto": None if punto is None else {"lat": punto[0], "lon": punto[1],
                                                     "fonte": punto[2]},
                "km_dalla_precedente": None,
                "giorni": None,
                "km_cumulativi": None,
                "giorni_cumulativi": None,
            })
        tappe.sort(key=lambda t: t["ordine"])
        for t in tappe:
            del_registro = per_tappa.get(t["tappa"])
            if del_registro and normalizza(del_registro) != normalizza(t["luogo"]):
                t["luogo_registro"] = del_registro
        for i, t in enumerate(tappe):
            if i == 0 or not t["punto"] or not tappe[i - 1]["punto"]:
                continue
            km = haversine(tappe[i - 1]["punto"]["lat"], tappe[i - 1]["punto"]["lon"],
                           t["punto"]["lat"], t["punto"]["lon"])
            t["km_dalla_precedente"] = round(km, 1)
            t["giorni"] = max(1, int(round(km / km_giorno)))
        tot_km = tot_gg = 0.0
        for t in tappe:
            if t["km_dalla_precedente"] is not None:
                tot_km += t["km_dalla_precedente"]
                tot_gg += t["giorni"]
            t["km_cumulativi"] = round(tot_km)
            t["giorni_cumulativi"] = int(tot_gg)
        con_punto = sum(1 for t in tappe if t["punto"])
        senza_punto = [t["tappa"] for t in tappe if not t["punto"]]
        anni[anno] = {
            "mezzo": mezzo,
            "km_al_giorno": km_giorno,
            "tappe": tappe,
            "riepilogo": {
                "tappe": len(tappe),
                "con_punto": con_punto,
                "senza_punto": senza_punto,
                "km_totali": round(tot_km),
                "giorni_totali": int(tot_gg),
                "voci_obbligatorie": len({t["voce"] for t in tappe}),
                "facoltative_dichiarate": sum(len(t["facoltativi"]) for t in tappe),
            },
        }
        r = anni[anno]["riepilogo"]
        print("anno %d: %d tappe, %d voci obbligatorie, %d facoltative dichiarate, %s"
              % (anno, r["tappe"], r["voci_obbligatorie"], r["facoltative_dichiarate"], mezzo))
        print("   percorso in linea d'aria: %d km in %d giorni; %d tappe senza punto%s"
              % (r["km_totali"], r["giorni_totali"], len(senza_punto),
                 (": " + ", ".join(senza_punto)) if senza_punto else ""))

    if solo:
        return 0

    out = {
        "versione": "v1",
        "data": "2026-10-03",
        "scopo": "la sequenza delle trenta tappe degli anni 2, 3 e 4: in che ordine il "
                 "duca incontra le trenta voci obbligatorie, e dove. Le facoltative sono "
                 "tenute fuori dalla sequenza e stanno nella colonna apposita di ogni tappa",
        "da_chei_dati": {
            "tappe": "la tabella delle trenta tappe di ciascun documento d'anno, "
                     "legguta per intestazione e non per numero di colonna, perche' il "
                     "quarto anno ha due colonne in piu' (la porta e il confronto)",
            "coordinate": "dati/luoghi_gioco.json prima, dati/ipotesi_luoghi.json poi: "
                          "il campo `fonte` di ogni punto dice da quale dei due viene",
            "velocita": "sorgenti/percorsi_calcola.py, gli stessi km al giorno che il "
                        "documento dei percorsi dichiara: due numeri per la stessa "
                        "strada sarebbero due bugie",
        },
        "che_cosa_non_e": "non e' il percorso del duca di percorsi.md: quello segue i soli "
                          "pin che avevano coordinate (9, 22 e 13), questo segue tutte e "
                          "trenta le tappe. Le due cose si confrontano e non coincidono, "
                          "e il conto della differenza e' in `verifica_sequenza.py`",
        "divergenze_nota": (
            "le tappe per le quali il registro dei luoghi e il documento d'anno non "
            "dicono la stessa cosa. Una divergenza con `dichiarazione` e' una domanda "
            "dichiarata; una divergenza senza dichiarazione e' un difetto, ed e' quello "
            "che verifica_sequenza.py segnala"
        ),
        "divergenze": [
            {"tappa": t["tappa"], "luogo_documento": t["luogo"],
             "luogo_registro": t["luogo_registro"],
             "dichiarazione": DICHIARATE.get(t["tappa"])}
            for anno in sorted(anni)
            for t in anni[anno]["tappe"] if t["luogo_registro"]
        ],
        "anni": anni,
    }
    with io.open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("\ndivergenze fra registro e documento: %d" % len(out["divergenze"]))
    for d in out["divergenze"]:
        print("   %s: documento %r, registro %r — %s"
              % (d["tappa"], d["luogo_documento"], d["luogo_registro"],
                 "dichiarata" if d["dichiarazione"] else "NON DICHIARATA"))
    print("scritto %s" % JSON_OUT)
    if os.path.exists(DOC_OUT):
        aggiorna_documento(out)
        print("aggiornate le tabelle di %s" % os.path.basename(DOC_OUT))
    else:
        print("documento non ancora scritto: le tabelle si generano quando esiste")
    return 0


def tabella(anno, anni):
    d = anni[anno]
    righe = ["| # | Tappa | Luogo (pin) | Voce obbligatoria | Forza | Facoltative (2) | "
             "| km dalla precedente | giorni | km cumulati |",
             "|---|---|---|---|---|---|---|---|---|"]
    for t in d["tappe"]:
        km = "" if t["km_dalla_precedente"] is None else "%.0f" % t["km_dalla_precedente"]
        gg = "" if t["giorni"] is None else "%d" % t["giorni"]
        cum = "" if t["km_cumulativi"] is None else "%d" % t["km_cumulativi"]
        nome = t["voce"] + (" `%s`" % t["voce_id"] if t["voce_id"] else "")
        righe.append("| %d | **%s** | %s | %s | %s | %s | %s | %s | %s |"
                     % (t["ordine"], t["tappa"], t["luogo"], nome, t["forza"],
                        "; ".join(t["facoltativi"]) or "—", km, gg, cum))
    return "\n".join(righe)


def aggiorna_documento(out):
    testo = leggi(DOC_OUT)
    i = testo.index(INIZIO)
    j = testo.index(FINE)
    parti = [INIZIO]
    nomi = {2: "Anno 2 — la penisola", 3: "Anno 3 — l'Europa",
            4: "Anno 4 — il mondo"}
    for anno in sorted(out["anni"]):
        d = out["anni"][anno]
        r = d["riepilogo"]
        parti.append("\n### %s\n" % nomi[anno])
        parti.append("\n*%s, %d km al giorno. Percorso in linea d'aria: **%d km in %d giorni**. "
                     "Voci obbligatorie distinte: **%d**. Facoltative dichiarate in tabella: **%d**. "
                     "Tappe senza punto: %s.*\n"
                     % (d["mezzo"], d["km_al_giorno"], r["km_totali"], r["giorni_totali"],
                        r["voci_obbligatorie"], r["facoltative_dichiarate"],
                        ", ".join(r["senza_punto"]) if r["senza_punto"] else "nessuna"))
        parti.append("\n" + tabella(anno, out["anni"]) + "\n")
    parti.append("\n")
    parti.append(FINE)
    with io.open(DOC_OUT, "w", encoding="utf-8") as f:
        f.write(testo[:i] + "".join(parti) + testo[j + len(FINE):])
    return True


if __name__ == "__main__":
    sys.exit(main())