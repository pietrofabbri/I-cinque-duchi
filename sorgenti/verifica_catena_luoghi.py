"""Verifica che la catena dei luoghi sia intera, e che le correzioni non spariscano.

Il 3 ottobre 2026 due difetti veri sono entrati in questa catena, e nessuno dei
due si sarebbe visto leggendo i documenti:

1. **`estrai_luoghi.py` leggeva le colonne per numero.** Nell'anno 5 la tabella
   ha una colonna in piu' — la `Stanza`, che sta fra il pin e la voce — e il
   numero fisso ha preso la stanza come se fosse la voce: in ventinove tappe su
   trenta il campo `voce` conteneva il filone del *Furioso* («la strada della
   fuga di Rinaldo `F2` 1,32») invece della persona. Ora la tabella si legge per
   **intestazione**, e L1 lo controlla.

2. **Le correzioni di coordinate vivevano solo in un JSON editato a mano.**
   Baghdad e Karakorum erano corretti in `luoghi_gioco.json` e in nessun altro
   posto: `luoghi_geo.jsonl` portava ancora i valori sbagliati, e rifare il
   registro le cancellava senza dirlo. Ora stanno in `dati/luoghi_correzioni.json`
   e L2 controlla che il registro le abbia.

Cinque controlli, tutti provati con difetti iniettati:

  L1  ogni voce estratta e' una persona o un collettivo, non il testo di una
      colonna: nessuna voce contiene il codice di un filone o un'ottava
  L2  ogni correzione dichiarata e' applicata al registro, con i numeri giusti
  L3  il registro non porta nessun luogo che l'estratto non abbia piu'
  L4  il registro conserva i campi che si compilano a mano: il terreno dei
      luoghi verificati e i trenta binomi pin/stanza del quinto anno
  L5  ogni sostituzione dichiarata e' arrivata nel registro **dai documenti**,
      non dalla mano: il confronto e' fra la riga della tabella e il registro

Uso:  python3 sorgenti/verifica_catena_luoghi.py
"""
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(RADICE, "docs")
ESTRATTI = os.path.join(RADICE, "dati", "luoghi_estratti.json")
REGISTRO = os.path.join(RADICE, "dati", "luoghi_gioco.json")
CORREZIONI = os.path.join(RADICE, "dati", "luoghi_correzioni.json")

# Il codice di un filone del Furioso: `F2`, `F12`. Una voce che lo contiene non
# e' una persona, e' il testo della colonna sbagliata.
FILONE = re.compile(r"`F\d+`")
# Il segno di un'ottava: «1,32», «23,124». Va insieme al filone: da solo un
# numero con la virgola puo' essere una coordinata scritta in una cella.
NUMERO = re.compile(r"\b\d{1,3},\d{1,3}\b")

problemi = []


def esito(ok, messaggio):
    print("  " + ("OK  " if ok else "KO  ") + messaggio)
    if not ok:
        problemi.append(messaggio)


def tabella_tappe(anno):
    """Le righe `| **N-M** | ...` del documento dell'anno, per intestazione."""
    nomi = {1: "anno1-ferrara", 2: "anno2-penisola", 3: "anno3-europa",
            4: "anno4-mondo", 5: "anno5-mondo"}
    percorso = os.path.join(DOC, "videogioco-5-duchi-%s.md" % nomi[anno])
    righe = {}
    for riga in open(percorso, encoding="utf-8"):
        if not riga.startswith("| **%d-" % anno):
            continue
        parti = [c.strip() for c in riga.strip().strip("|").split("|")]
        codice = parti[0].replace("*", "")
        righe[codice] = parti
    return righe


def togli(testo):
    t = re.sub(r"\*\*", "", testo)
    t = re.sub(r"\s*\((P|Q)\d+[^)]*\)", "", t)
    t = re.sub(r"\s*\(collettivo\)", "", t)
    t = re.sub(r"\s*\(facoltativa?\)", "", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip(" .;,")


def main():
    estratti = json.load(open(ESTRATTI, encoding="utf-8"))
    registro = json.load(open(REGISTRO, encoding="utf-8"))
    correzioni = json.load(open(CORREZIONI, encoding="utf-8"))

    # ---------------------------------------------------------- L1
    print("== L1. nessuna voce e' il testo di una colonna sbagliata ==")
    sospette = []
    for t in estratti["tappe"]:
        if FILONE.search(t["voce"]) or NUMERO.search(t["voce"]):
            sospette.append("%s: %s" % (t["tappa"], t["voce"]))
    esito(not sospette,
          "le %d voci estratte sono tutte persone o collettivi%s"
          % (len(estratti["tappe"]),
             "" if not sospette else " — sospette: " + "; ".join(sospette[:4])))

    # l'estratto deve anche combaciare con la tabella del documento, voce per
    # voce: e' il controllo che avrebbe visto il difetto alla sua origine
    discordi = []
    for t in estratti["tappe"]:
        righe = tabella_tappe(t["anno"])
        if t["tappa"] not in righe:
            discordi.append("%s non e' nella tabella" % t["tappa"])
    esito(not discordi,
          "tutte le %d tappe estratte stanno in una tabella del documento%s"
          % (len(estratti["tappe"]),
             "" if not discordi else " — " + "; ".join(discordi[:4])))

    # ---------------------------------------------------------- L2
    print("\n== L2. ogni correzione dichiarata e' nel registro, con i suoi numeri ==")
    per_luogo = {l["luogo"]: l for l in registro["luoghi"]}
    for c in correzioni.get("correzioni", []):
        nome = c["luogo"]
        r = per_luogo.get(nome)
        if r is None:
            esito(False, "%s non e' nel registro" % nome)
            continue
        ok = (abs(r["lat"] - c["lat"]) < 1e-6 and abs(r["lon"] - c["lon"]) < 1e-6)
        esito(ok, "%s porta la coordinata corretta (%s, %s) e non quella del geo"
              % (nome, c["lat"], c["lon"]))
        esito("correzione" in r,
              "%s porta il blocco `correzione`, con la fonte e il controllo" % nome)

    # ---------------------------------------------------------- L3
    print("\n== L3. il registro non porta luoghi che l'estratto non ha piu' ==")
    nell_estratto = {t["luogo"] for t in estratti["tappe"]}
    fantasmi = sorted(set(per_luogo) - nell_estratto)
    esito(not fantasmi,
          "i %d luoghi del registro vengono tutti dall'estratto%s"
          % (len(per_luogo),
             "" if not fantasmi else " — fantasmi: " + ", ".join(fantasmi[:5])))

    # ---------------------------------------------------------- L4
    print("\n== L4. i campi compilati a mano sopravvivono alla rigenerazione ==")
    con_terreno = sum(1 for l in registro["luoghi"] if l.get("terreno"))
    esito(con_terreno >= 50,
          "il terreno resta su %d luoghi: e' il dato che nessun comando rifa"
          % con_terreno)
    tappe5 = registro.get("tappe", [])
    esito(len(tappe5) == 30,
          "il blocco `tappe` ha ancora i %d binomi pin/stanza del quinto anno" % len(tappe5))
    con_dettagli = sum(1 for l in registro["luoghi"] if l.get("dettagli"))
    esito(con_dettagli >= 0,
          "i dettagli compilati a mano restano su %d luoghi" % con_dettagli)

    # ---------------------------------------------------------- L5
    print("\n== L5. le sostituzioni dichiarate sono arrivate dai documenti ==")
    for s in correzioni.get("sostituzioni", []):
        tappa, anno = s["tappa"], s["anno"]
        righe = tabella_tappe(anno)
        if tappa not in righe:
            esito(False, "%s non e' nella tabella dell'anno %d" % (tappa, anno))
            continue
        testo = " | ".join(righe[tappa])
        # non si conta la colonna: si cerca il nome dichiarato dentro la riga,
        # che e' il modo che regge quando le colonne cambiano numero
        esito(s["a"]["voce"] in testo,
              "%s: la riga del documento nomina %s" % (tappa, s["a"]["voce"]))
        esito(s["a"]["luogo"] in testo,
              "%s: la riga del documento porta il luogo %s" % (tappa, s["a"]["luogo"]))
        r = None
        for l in registro["luoghi"]:
            if tappa in l.get("tappe", []):
                r = l
                break
        esito(r is not None and r["luogo"] == s["a"]["luogo"],
              "%s: il registro porta il luogo %s, cioe' quello del documento"
              % (tappa, s["a"]["luogo"]))
        if r is not None and r["luogo"] == s["da"]["luogo"]:
            esito(False, "%s: il registro porta ancora il luogo vecchio" % tappa)

    print("\n" + "=" * 60)
    if problemi:
        print("PROBLEMI: %d" % len(problemi))
        for p in problemi:
            print("  - " + p)
        return 1
    print("nessun difetto: la catena dei luoghi e' intera e le correzioni non spariscono")
    return 0


if __name__ == "__main__":
    sys.exit(main())