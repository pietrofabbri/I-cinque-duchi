"""Verifica che la parte orale del gioco sia dichiarata con i numeri giusti.

Il documento `videogioco-5-duchi-parlato.md` porta un numero per lingua, e quel
numero viene da una ricerca che cambia nel tempo: Commons cresce, e un domani il
ferrarese potrebbe avere trenta registrazioni. Un numero scritto a mano nella
tabella del documento è quindi una fotografia che invecchia, e il controllo che
manca è quello che dice se la fotografia e' ancora quella.

Quattro controlli, tutti morroni (provati con difetti iniettati):

  A1  il documento porta, per ogni lingua, il numero che il dato conta
  A2  ogni lingua è dichiarata una volta sola: sei righe, sei lingue
  A3  la Web Speech API e' esclusa **per la ragione giusta** (manda l'audio fuori),
      e non per una vaghezza
  A4  nessun livello della parte orale promette il riconoscimento della voce:
      quello che il gioco non sa fare si dichiara, non si simula

Uso:  python3 sorgenti/verifica_parlato.py
"""
import json
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(RADICE, "docs", "videogioco-5-duchi-parlato.md")
DATI = os.path.join(RADICE, "dati", "lingue", "audio_disponibili.json")
LINGUE_DOC = os.path.join(RADICE, "docs", "videogioco-5-duchi-lingue.md")

problemi = []


def esito(ok, messaggio):
    print("  " + ("OK  " if ok else "KO  ") + messaggio)
    if not ok:
        problemi.append(messaggio)


def numero_italiano(n):
    return "{:,}".format(n).replace(",", " ")


def main():
    doc = open(DOC, encoding="utf-8").read()
    dati = json.load(open(DATI, encoding="utf-8"))

    # ------------------------------------------------------------- A1
    print("== A1. il documento porta il numero che il dato conta ==")
    per_voce = dati["lingue"]
    for r in per_voce:
        n = r["registrazioni"]
        if r["esito"] != "contato":
            esito(False, "%s: il dato e' '%s' e il documento non puo' dichiararlo"
                  % (r["nome"], r["esito"]))
            continue
        scritto = numero_italiano(n)
        # il numero del documento porta il separatore delle migliaia o la parola
        # «zero»: i due modi sono entrambi accettati perche' il documento e'
        # scritto per essere letto
        trovato = (scritto in doc) or (n == 0 and re.search(
            r"\|\s*\*\*0\*\*", doc) is not None and re.search(
            r"\*\*" + re.escape(r["nome"].split()[0].lower()) + r"\*\*", doc) is not None)
        esito(trovato, "%-26s %s" % (r["nome"], scritto))

    # ------------------------------------------------------------- A2
    print("\n== A2. sei lingue, sei righe, nessuna due volte ==")
    # la tabella di 2.3: sei righe di lingua. Si prendono per il primo campo
    # grassetto, non per il secondo: il secondo porta il numero in forme diverse
    # («89 381», «**0**, e non è un buco») e un formato che cambia è un formato che
    # si rompe.
    sezione = doc[doc.index("### 2.3"):doc.index("## 3.")] if "### 2.3" in doc else ""
    righe = re.findall(r"^\| \*\*([^*]+)\*\* \|", sezione, re.M)
    nomi = righe
    esito(len(righe) == 6, "la tabella delle lingue ha %d righe, non 6" % len(righe))
    esito(len(set(nomi)) == len(nomi), "nessuna lingua e' dichiarata due volte")
    lingue_codici = {r["lingua"] for r in dati["lingue"]}
    esito(len(lingue_codici) == 6, "il dato copre %d lingue" % len(lingue_codici))

    # ------------------------------------------------------------- A3
    print("\n== A3. la Web Speech API e' esclusa per la ragione giusta ==")
    sez = doc[doc.index("### 2.2"):doc.index("### 2.3")] if "### 2.2" in doc else ""
    esito("server di Google" in sez,
          "la sezione 2.2 dice che Chrome manda l'audio ai server di Google")
    esito("non funziona offline" in sez,
          "la sezione 2.2 dice che non funziona offline")
    esito("esclusa" in sez, "la sezione 2.2 dichiara l'esclusione e non la evita")

    # ------------------------------------------------------------- A4
    print("\n== A4. nessun livello promette il riconoscimento della voce ==")
    # i cinque livelli: il quinto e' quello dichiarato non fatto
    livelli = re.findall(r"^### (L\d) ", doc, re.M)
    esito(livelli == ["L1", "L2", "L3", "L4", "L5"],
          "i livelli sono %s" % ", ".join(livelli))
    sez5 = doc[doc.index("### L5"):doc.index("## 4.")] if "### L5" in doc else ""
    esito("non fatto" in sez5, "L5 e' dichiarato come non fatto")
    esito("deve poter funzionare **senza** L5" in sez5,
          "il gioco deve funzionare anche se L5 non arriva mai")
    # anche il titolo conta: un livello chiamato «Riconoscimento automatico:
    # funziona» promette il riconoscimento, per quanto sia vago il corpo
    titolo = re.search(r"^### L5 .*$", doc, re.M)
    esito(titolo is not None and "non fatto" in titolo.group(0),
          "il titolo di L5 dichiara che non e' fatto")
    # la parte scritta non cambia: nessuna componente nuova, nessuna famiglia nuova
    lingue = open(LINGUE_DOC, encoding="utf-8").read()
    esito("| # | Componente" in lingue and "| 9 |" in lingue,
          "lingue.md resta a nove componenti: la parte orale non ne aggiunge una")
    if "famiglie di esercizi" in doc:
        esito("non è un sistema a sé" in doc,
              "il documento dichiara che la parte orale non e' un sistema separato")

    print("\n" + "=" * 62)
    if problemi:
        print("PROBLEMI: %d" % len(problemi))
        for p in problemi:
            print("  - " + p)
        return 1
    print("nessun difetto: la parte orale e' dichiarata con i numeri del dato, e "
          "quello che il gioco non sa fare resta dichiarato")
    return 0


if __name__ == "__main__":
    sys.exit(main())