"""Verifica gli ambienti dei centocinquanta livelli.

Un ambiente e' una promessa: dice al motore che cosa disegnare e dice alla scheda
che cosa non si sa. Il pericolo di una promessa cosi' non e' che sia falsa, e' che
diventi **dimenticata**: il motore smette di chiedere, la scheda mostra un vuoto
che nessuno ha piu' controllato, e il difetto sparisce senza che nessuno lo dica.

I controlli sono sei, e l'ultimo e' quello per cui il file esiste.

  B1  i livelli sono esattamente 5 x 30, e nessuno due volte
  B2  ogni ambiente porta i campi che il motore legge, e nessuno e' vuoto
      dove non puo' esserlo
  B3  il luogo dichiarato e' quello del registro: l'ambiente non puo' dire una
      citta' diversa da `luoghi_gioco.json`
  B4  le coordinate dell'ambiente sono quelle del registro, e il loro stato
      e' quello del registro
  B5  ogni tipo ha detto da dove viene (`tipo_da`), e ogni griglia esiste nel
      progetto: nessuna tessera che il motore non sappia leggere
  B6  **ogni vuoto dichiarato e' un vuoto reale**, e ogni vuoto reale e'
      dichiarato
  B7  **ogni ambiente ha un punto da disegnare, o dichiara che non ne ha**: il
      punto viene dal registro quando la coordinata e' verificata e dall'ipotesi
      quando non lo e', e in entrambi i casi l'ambiente dice quale dei due ha
      usato

B6 e' il controllo che vale: un ambiente che dichiara `senza_coordinate` e poi ha
le coordinate e' un ambiente che mente, e un ambiente che ha i vuoti ma non li
dichiara e' un ambiente che mente nel modo opposto. Per elencarli tutti e' una
riga di logica, ma e' la riga che rende gli altri cinquecento utili.

**B8 e' nato il 03/10/2026 da un difetto vero.** Gli altri sette confrontano il
dato con gli altri dati, e nessuno confrontava il dato con **quello che i
documenti scrivono**: `fonti-visive.md` §3.6 dichiarava 99 ambienti con
coordinate, 69 con sagome OSM, `citta_antica` 11 e `percorso` 11, mentre il dato
diceva 100, 68, 12 e 10. Tutte le verifiche passavano, perche' B1-B7 non
guardano i numeri scritti nelle righe. B8 legge la sezione e confronta ogni
numero con il conto: il documento non può piu' dire una cifra che il dato non
conferma, ed e' l'unico modo perche' un documento resti vero quando il dato
cambia sotto di lui.

**B7 e' nato con le ipotesi di coordinata** (`dati/ipotesi_luoghi.json`, il 03/10/2026),
e controlla una cosa che sembra ovvia e non lo e'. Il motore ha due fonti di
coordinate, e scegliere sempre la prima produce un gioco con 99 ambienti su 150
posizionati **senza che nessuno lo dichieda**. B7 vuole che ogni ambiente
dichiari `pin_da_disegnare` con la fonte del punto, e che l'unica riga accettata
senza punto sia quella che porta il vuoto `nessun_luogo_dichiarato`: un posto che
il progetto ha deciso che non esiste. Un vuoto cosi' non e' una mancanza, e' una
risposta, ed e' l'unica cosa che il controllo accetta senza punto.

Uso:  python3 sorgenti/verifica_ambienti.py
"""
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AMBIENTI = os.path.join(RADICE, "dati", "ambienti_livelli.json")
LUOGHI = os.path.join(RADICE, "dati", "luoghi_gioco.json")
TAVOLAZZA = os.path.join(RADICE, "dati", "fonti_visive", "tavolozza.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ambienti_livelli as al                                # noqa: E402

OBBLIGATORI = ["livello", "anno", "numero", "argomento", "luogo", "coord_stato",
               "ambiente", "vuoti"]

# `pin_da_disegnare` e' obbligatorio ma puo' valere `None`: e' il campo che
# dichiara «qui non c'e' niente da mettere sulla carta». Un campo obbligatorio
# che rifiuta `None` direbbe che la risposta alla Q6.2 non e' ammessa, e il
# controllo deve invece esigerla. Se la chiave manca, B7 lo segnala; se vale
# `None`, lo accetta solo con il vuoto `nessun_luogo_dichiarato` dichiarato.
OBBLIGATORI_MA_NON_NULL = ["pin_da_disegnare"]

IPOTESI = os.path.join(RADICE, "dati", "ipotesi_luoghi.json")
_IPOTESI = {}
if os.path.exists(IPOTESI):
    with open(IPOTESI, encoding="utf-8") as f:
        for _r in json.load(f)["ipotesi"]:
            _IPOTESI[_r["tappa"]] = (_r["lat"], _r["lon"])


def ipotesi_coord(lid):
    """La coordinata che il file delle ipotesi dichiara per la tappa."""
    return _IPOTESI.get(lid)


DOC = os.path.join(RADICE, "docs", "videogioco-5-duchi-fonti-visive.md")

# I numeri di §3.6, e come si chiamano dentro il dato. La chiave e' la frase che
# il documento usa, e `None` vuol dire «presente ma senza numero»: si controlla
# solo che ci sia.
QUOTE = [
    ("Con coordinate", None, lambda a: sum(1 for x in a if x["lat"] is not None)),
    ("Con sagome OSM", None,
     lambda a: sum(1 for x in a if x["ambiente"]["edifici"]["n"])),
    ("Già costruiti", None,
     lambda a: sum(1 for x in a if x["ambiente"]["stato"] == "costruito")),
]


def _numero_dopo(testo, etichetta):
    """Il numero che segue un'etichetta in una riga della tabella di §3.6.

    La riga e' fatta cosi': `| Etichetta | **99** |`. Si prende il primo numero
    che segue l'etichetta, e si restituisce `None` se non c'e': l'assenza e' un
    difetto suo, e va detto, non aggirato.
    """
    for riga in testo.split("\n"):
        if not riga.startswith("|") or etichetta not in riga:
            continue
        dopo = riga.split(etichetta, 1)[1]
        m = re.search(r"(\d+)", dopo)
        return int(m.group(1)) if m else None
    return None


def confronta_documento(ambiente):
    """B8: nessun numero scritto in §3.6 puo' contraddire il dato."""
    if not os.path.exists(DOC):
        return ["B8  non trovo %s" % os.path.relpath(DOC, RADICE)]
    testo = open(DOC, encoding="utf-8").read()
    # la sezione da confrontare: da §3.6 fino alla successiva
    inizio = testo.find("### 3.6")
    fine = testo.find("### 3.7", inizio)
    sezione = testo[inizio:fine if fine > inizio else len(testo)]

    problemi = []
    for etichetta, _, conto in QUOTE:
        dichiarato = _numero_dopo(sezione, etichetta)
        reale = conto(ambiente)
        if dichiarato is None:
            problemi.append("B8  la riga '%s' di §3.6 non ha un numero" % etichetta)
        elif dichiarato != reale:
            problemi.append("B8  §3.6 dichiara %d per '%s', il dato dice %d"
                            % (dichiarato, etichetta, reale))

    # i tipi: `citta_antica` 12 nella riga dei nove tipi
    riga_tipi = ""
    for riga in sezione.split("\n"):
        if "`citta`" in riga:
            riga_tipi = riga
            break
    if not riga_tipi:
        problemi.append("B8  non trovo la riga dei nove tipi in §3.6")
    else:
        per_tipo = {}
        for x in ambiente:
            t_ = x["ambiente"]["tipo"]
            per_tipo[t_] = per_tipo.get(t_, 0) + 1
        for t_, n in sorted(per_tipo.items()):
            m = re.search(r"`%s` (\d+)" % re.escape(t_), riga_tipi)
            if not m:
                problemi.append("B8  §3.6 non dichiara il tipo `%s`" % t_)
            elif int(m.group(1)) != n:
                problemi.append("B8  §3.6 dichiara `%s` %s, il dato dice %d"
                                % (t_, m.group(1), n))

    # i vuoti dichiarati: ogni vuoto del dato deve comparire con il suo numero
    vuoti = {}
    for x in ambiente:
        for v in x["vuoti"]:
            vuoti[v] = vuoti.get(v, 0) + 1
    for v, n in sorted(vuoti.items()):
        if not re.search(r"`%s`\s*\*?\*?%d" % (re.escape(v), n), sezione):
            problemi.append("B8  §3.6 non dichiara `%s` con il conto %d "
                            "(o lo dichiara con un altro numero)" % (v, n))
    return problemi


def main():
    con = json.load(open(AMBIENTI, encoding="utf-8"))
    gj = json.load(open(LUOGHI, encoding="utf-8"))
    ambiente = con["ambienti"]
    problemi = []

    # B1: il conto
    attesi = ["%d-%d" % (a, n) for a in range(1, 6) for n in range(1, 31)]
    ids = [a["livello"] for a in ambiente]
    for lid in sorted(set(ids)):
        if ids.count(lid) > 1:
            problemi.append("B1  livello ripetuto: %s" % lid)
    mancanti = [t for t in attesi if t not in ids]
    inpiu = [t for t in ids if t not in attesi]
    if mancanti:
        problemi.append("B1  %d livelli mancanti: %s"
                        % (len(mancanti), ", ".join(mancanti[:12])))
    if inpiu:
        problemi.append("B1  %d livelli fuori schema: %s"
                        % (len(inpiu), ", ".join(inpiu[:12])))

    # il registro, per i confronti
    per_tappa = {}
    for l in gj["luoghi"]:
        for t in (l.get("tappe") or []):
            per_tappa[t] = l

    tavolozza = json.load(open(TAVOLAZZA, encoding="utf-8"))
    colori = {v["chiave"] for v in tavolozza["voci"]}

    for a in ambiente:
        lid = a["livello"]
        # B2: i campi
        for k in OBBLIGATORI:
            if k not in a or a[k] is None:
                problemi.append("B2  %s: campo mancante %s" % (lid, k))
        for k in OBBLIGATORI_MA_NON_NULL:
            if k not in a:
                problemi.append("B2  %s: campo mancante %s" % (lid, k))
        if not a.get("argomento"):
            problemi.append("B2  %s: argomento vuoto" % lid)
        if not a.get("voce"):
            problemi.append("B2  %s: nessuna voce" % lid)

        # B3 e B4: il luogo e le coordinate contro il registro
        reg = per_tappa.get(lid)
        if a["anno"] > 1:
            if reg is None:
                problemi.append("B3  %s: nessun luogo nel registro" % lid)
            elif a["luogo"] != reg["luogo"]:
                problemi.append("B3  %s: l'ambiente dice '%s', il registro dice "
                                "'%s'" % (lid, a["luogo"], reg["luogo"]))
            else:
                if a["lat"] != reg.get("lat") or a["lon"] != reg.get("lon"):
                    problemi.append("B4  %s: coordinate diverse dal registro"
                                    % lid)
                if a["coord_stato"] != reg.get("coord_stato"):
                    problemi.append("B4  %s: stato coordinate '%s' invece di "
                                    "'%s'" % (lid, a["coord_stato"],
                                              reg.get("coord_stato")))

        # B5: il tipo dichiara la sua fonte, la griglia esiste, i colori esistono
        amb = a["ambiente"]
        if not amb.get("tipo_da"):
            problemi.append("B5  %s: il tipo non dice da dove viene" % lid)
        if amb.get("griglia") != al.GRIGLIE.get(amb.get("tipo")):
            problemi.append("B5  %s: griglia %s che non corrisponde al tipo %s"
                            % (lid, amb.get("griglia"), amb.get("tipo")))
        for c in amb.get("paleta", []):
            if c not in colori:
                problemi.append("B5  %s: il colore '%s' non e' in tavolozza.json"
                                % (lid, c))
        if a["anno"] == 1 and amb.get("fondo") is None:
            problemi.append("B5  %s: anno 1 senza fondo di Ferrara" % lid)
        if a["anno"] > 1 and amb.get("fondo"):
            problemi.append("B5  %s: fondo di Ferrara fuori dall'anno 1" % lid)

        # B6: i vuoti dichiarati sono veri, e i vuoti veri sono dichiarati
        attesi_vuoti = set()
        if a["lat"] is None:
            attesi_vuoti.add("senza_coordinate"
                             if a["anno"] == 1
                             else "coordinate_" + str(a["coord_stato"]))
        if a["coord_stato"] not in ("verificata", None) and a["lat"] is not None:
            attesi_vuoti.add("coordinate_" + str(a["coord_stato"]))
        ed = amb["edifici"]
        if not ed["n"]:
            attesi_vuoti.add("senza_sagome_osm")
        elif ed["senza_altezza"] == ed["n"]:
            attesi_vuoti.add("sole_sagome_senza_altezza")
        if amb.get("orientamento") is None:
            attesi_vuoti.add("orientamento_non_dichiarato")
        if a["anno"] == 1 and amb.get("fondo") is None:
            attesi_vuoti.add("senza_fondo_ferrara")
        # il vuoto dell'immaginata: lo aggiunge il generatore, e B6 lo accetta
        # solo se l'ambiente porta davvero il grado `immaginata`
        ip = a.get("ipotesi")
        if ip and ip["grado"] == "immaginata":
            attesi_vuoti.add("nessun_luogo_dichiarato")

        dichiarati = set(a["vuoti"])
        for v in sorted(dichiarati - attesi_vuoti):
            problemi.append("B6  %s: dichiara il vuoto '%s' ma non e' un vuoto"
                            % (lid, v))
        for v in sorted(attesi_vuoti - dichiarati):
            problemi.append("B6  %s: il vuoto '%s' c'e' ma non e' dichiarato"
                            % (lid, v))

        # B7: il punto da disegnare c'e', e dice da quale dei due file viene
        dis = a.get("pin_da_disegnare")
        if dis is None:
            if not ip or ip["grado"] != "immaginata":
                problemi.append("B7  %s: nessun punto da disegnare e nessuna "
                                "ipotesi che lo dichiari" % lid)
        else:
            if dis.get("fonte") not in ("dati/luoghi_gioco.json",
                                         "dati/ipotesi_luoghi.json"):
                problemi.append("B7  %s: la fonte del punto e' '%s', che non e' "
                                "uno dei due file" % (lid, dis.get("fonte")))
            if a["lat"] is not None and dis.get("fonte") != \
                    "dati/luoghi_gioco.json":
                problemi.append("B7  %s: ha una coordinata verificata e un punto "
                                "preso dall'ipotesi" % lid)
            if ip and dis.get("fonte") == "dati/ipotesi_luoghi.json":
                if dis.get("grado") != ip["grado"]:
                    problemi.append("B7  %s: il punto e' di grado '%s' e l'ambiente "
                                    "dichiara '%s'"
                                    % (lid, dis.get("grado"), ip["grado"]))
                if (dis.get("lat"), dis.get("lon")) != ipotesi_coord(lid):
                    problemi.append("B7  %s: il punto non e' quello dell'ipotesi"
                                    % lid)

    # B8: i numeri che il documento dichiara sono quelli del dato
    problemi += confronta_documento(ambiente)

    # il riepilogo
    print("ambienti: %s" % os.path.relpath(AMBIENTI, RADICE))
    print("  %d ambienti su %d attesi" % (len(ambiente), len(attesi)))
    print("  con coordinate verificate: %d"
          % sum(1 for a in ambiente if a["lat"]))
    print("  con ipotesi: %d" % sum(1 for a in ambiente if a.get("ipotesi")))
    print("  con un punto da disegnare: %d su %d"
          % (sum(1 for a in ambiente if a.get("pin_da_disegnare")),
             len(ambiente)))
    print("  con sagome: %d" % sum(1 for a in ambiente
                                  if a["ambiente"]["edifici"]["n"]))
    print("  costruiti: %s" % ", ".join(con["riepilogo"]["costruiti"]) or "nessuno")
    vuoti = {}
    for a in ambiente:
        for v in a["vuoti"]:
            vuoti[v] = vuoti.get(v, 0) + 1
    print("  vuoti dichiarati: %s"
          % ", ".join("%s %d" % kv for kv in sorted(vuoti.items())))
    if problemi:
        print("\nPROBLEMI: %d" % len(problemi))
        for p in problemi[:60]:
            print("  " + p)
        if len(problemi) > 60:
            print("  ... e altri %d" % (len(problemi) - 60))
        return 1
    print("\nOK: nessun problema")
    return 0


if __name__ == "__main__":
    sys.exit(main())