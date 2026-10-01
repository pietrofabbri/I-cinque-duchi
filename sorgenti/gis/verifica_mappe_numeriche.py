"""Verifica numerica delle mappe: non basta guardarle.

Un disegno puo' sembrare giusto anche se un anello e' capovolto, se un punto e'
spostato di mezzo grado o se un anello si auto-interseca. Qui si controllano fatti
che si possono sbagliare:

 1. le quattro estremita' d'Italia, con la tolleranza della scala 10m;
 2. i capoluoghi dentro la propria provincia (il layer contiene le province, non
    le regioni: e' il controllo piu' severo, perche' ce ne sono 574);
 3. citta' europee dentro il proprio Paese, e citta' fuori dall'Europa assenti;
 4. nessun vertice fuori dal mondo e nessun anello con meno di due punti.

Tre cose che la prima versione di questo file sbagliava, e che sono segnate
qui perche' sono errori facili da rifare:

- l'estremo sud dell'Italia NON e' Portopalo (36,65 N) ma **Lampedusa**
  (35,49 N), che e' italiana. Il dato del file era giusto, l'aspettativa no;
- **Citta' del Vaticano** cade dentro il poligono dell'Italia: e' un'enclave e
  deve cadere. Non e' un errore;
- il punto-in-poligono va calcolato col **winding number** (`punto_in_poligono.py`),
  non con la regola pari-dispari: coi buchi, la pari-dispari diceva che Venezia
  era dentro la Baviera.
"""
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mappe_lettore import leggi
from punto_in_poligono import dentro

MAPPE = os.path.join(RADICE, "dati", "mappe")
GUARDIA = []


def carica(nome):
    return leggi(f"{MAPPE}/{nome}")


def esito(ok, testo):
    print(f"  {'OK ' if ok else 'KO '} {testo}")
    GUARDIA.append(bool(ok))


# ---------------------------------------------------------------- 1
print("== 1. estremita' d'Italia (scala 10m, quantizzazione 0,5 m) ==")
PAESI = carica("penisola_10_paesi.json")[0]
italia = [(p, a) for p, a in PAESI if p.get("ADM0_A3") == "ITA"]
xs = [q[0] for _, a in italia for an in a for q in an]
ys = [q[1] for _, a in italia for an in a for q in an]

# ovest Val d'Aosta 6,63 E · est Capo d'Otranto 18,52 E
# sud Lampedusa 35,49 N · nord Ortler-Cevedale 47,08 N
for nome, val, atteso in [("ovest, Val d'Aosta", min(xs), 6.63),
                          ("est, Capo d'Otranto", max(xs), 18.52),
                          ("sud, Lampedusa", min(ys), 35.49),
                          ("nord, Ortler-Cevedale", max(ys), 47.08)]:
    scarto = abs(val - atteso)
    esito(scarto < 0.12, f"{nome:<22} calcolato {val:8.3f}  atteso {atteso:8.3f}  "
                         f"scarto {scarto:.3f}")
print(f"       bbox Italia: lon {min(xs):.2f}..{max(xs):.2f}  "
      f"lat {min(ys):.2f}..{max(ys):.2f}  anelli {sum(len(a) for _, a in italia)}")

# ---------------------------------------------------------------- 2
print("\n== 2. capoluoghi dentro la propria provincia (574 province) ==")
REGIONI = carica("penisola_10_regioni.json")[0]
for nome, lon, lat, attesa in [
        ("Roma", 12.496, 41.903, "Roma"), ("Milano", 9.190, 45.464, "Milano"),
        ("Napoli", 14.268, 40.852, "Napoli"), ("Palermo", 13.361, 38.116, "Palermo"),
        ("Cagliari", 9.120, 39.224, "Cagliari"), ("Venezia", 12.326, 45.440, "Venezia"),
        ("Bari", 16.872, 41.118, "Bari"), ("Torino", 7.691, 45.070, "Torino"),
        ("Ferrara", 11.621, 44.837, "Ferrara"), ("Bologna", 11.343, 44.494, "Bologna"),
        ("Firenze", 11.256, 43.770, "Firenze"),
        # Natural Earth chiama questa unita' "Liguria" nel campo italiano e
        # "Genova" nel campo inglese: non e' un errore, e' la fonte.
        ("Genova", 8.946, 44.405, "Liguria"),
        ("L'Aquila", 13.396, 42.351, "dell'Aquila"), ("Catanzaro", 16.578, 38.905, "Catanzaro"),
        ("Ancona", 13.515, 43.616, "Ancona"), ("Campobasso", 14.663, 41.560, "Campobasso")]:
    trovate = [p.get("name_it") or p.get("name")
               for p, a in REGIONI if p.get("admin") == "Italy" and dentro(a, lon, lat)]
    esito(attesa in trovate,
          f"{nome:<11} ({lon:7.3f},{lat:6.3f}) -> {trovate or 'NESSUNA'}")

print("\n== 2b. la stessa citta' non deve cadere in province sbagliate ==")
for nome, lon, lat, esclusa in [("Ferrara", 11.621, 44.837, "Roma"),
                                ("Roma", 12.496, 41.903, "Milano"),
                                ("Milano", 9.190, 45.464, "Napoli")]:
    trovate = [p.get("name_it") for p, a in REGIONI
               if p.get("admin") == "Italy" and dentro(a, lon, lat)]
    esito(len(trovate) == 1 and esclusa not in trovate,
          f"{nome:<11} province trovate: {trovate} (non deve contenere {esclusa})")

# ---------------------------------------------------------------- 3
print("\n== 3. citta' dentro il Paese giusto ==")
EU = carica("europa_50_paesi.json")[0]
for nome, lon, lat, iso in [("Roma", 12.496, 41.903, "ITA"),
                            ("Parigi", 2.352, 48.857, "FRA"),
                            ("Vienna", 16.373, 48.208, "AUT"),
                            ("Monaco", 11.582, 48.135, "DEU"),
                            ("Londra", -0.128, 51.507, "GBR"),
                            ("Madrid", -3.704, 40.417, "ESP"),
                            ("Atene", 23.727, 37.984, "GRC")]:
    src = PAESI if iso == "ITA" else EU
    ok = any(p.get("ADM0_A3") == iso and dentro(a, lon, lat) for p, a in src)
    esito(ok, f"{nome:<9} dentro {iso}: {ok}")

print("\n== 3b. citta' fuori dall'Europa non devono esserci ==")
for nome, lon, lat in [("New York", -74.0, 40.7), ("Tokyo", 139.7, 35.7),
                       ("Il Cairo", 31.2, 30.0), ("Brasilia", -47.9, -15.8),
                       ("Sydney", 151.2, -33.9), ("Cape Town", 18.4, -33.9)]:
    f = any(dentro(a, lon, lat) for _, a in EU)
    esito(not f, f"{nome:<11} dentro l'Europa: {f}")

# ---------------------------------------------------------------- 4
print("\n== 4. le citta' archiviate sono dove dicono di essere ==")
CITTA_IT = carica("penisola_10_citta.json")[1]
IT_E = {"Italy", "France", "Switzerland", "Austria", "Slovenia",
        "Vatican", "San Marino"}
problemi = []
for props, x, y in CITTA_IT:
    paese = props.get("ADM0NAME")
    if paese in IT_E:
        continue
    # un Paese non confinante che pretende una citta' dentro l'Italia e' un bug
    if any(dentro(a, x, y) for _, a in italia):
        problemi.append((props.get("NAME_IT"), paese, round(x, 2), round(y, 2)))
esito(not problemi,
      f"nessuna citta' di un Paese lontano cade dentro l'Italia "
      f"({len(CITTA_IT)} controllate){': ' + str(problemi[:3]) if problemi else ''}")

print("\n== 4b. le citta' archiviate sono dentro il proprio Paese ==")
ITALIANI = {"Italy"}
mismatch = []
enclave = []
for props, x, y in CITTA_IT:
    paese = props.get("ADM0NAME")
    if paese not in ITALIANI:
        # Vaticano e San Marino: il poligono dell'Italia di Natural Earth NON ha
        # un buco per le enclave, quindi ci cadono dentro. Non e' un difetto dei
        # dati ma una scelta della fonte, e va registrata perche' un controllo
        # futuro la deve sapere: non va trattata come se fosse un errore.
        if paese in ("Vatican", "San Marino") and \
                any(dentro(a, x, y) for p, a in PAESI if p.get("ADM0_A3") == "ITA"):
            enclave.append(props.get("NAME_IT"))
        continue
    if not any(dentro(a, x, y) for p, a in PAESI if p.get("ADM0_A3") == "ITA"):
        mismatch.append((props.get("NAME_IT"), paese, "fuori dall'Italia"))
esito(not mismatch,
      f"ogni citta' italiana dichiarata cade nel poligono dell'Italia "
      f"({len(mismatch)} problemi){': ' + str(mismatch[:3]) if mismatch else ''}")
print(f"  nota  enclave che cadono dentro l'Italia perche' la fonte non le "
      f"ritaglia: {enclave or 'nessuna'}")

# ---------------------------------------------------------------- 5
print("\n== 5. sanita' dei file ==")
for nome in sorted(os.listdir(MAPPE)):
    geom, punti = carica(nome)
    cattivi = 0
    for p, an in geom:
        for a in an:
            if len(a) < 2:
                cattivi += 1
            for lon, lat in a:
                if not (-180.01 <= lon <= 180.01 and -90.01 <= lat <= 90.01):
                    cattivi += 1
                    break
    for p, x, y in punti:
        if not (-180.01 <= x <= 180.01 and -90.01 <= y <= 90.01):
            cattivi += 1
    esito(cattivi == 0, f"{nome:<36} vertici/anelli fuori dal mondo: {cattivi}")

print(f"\n==== controlli superati: {sum(GUARDIA)}/{len(GUARDIA)} ====")