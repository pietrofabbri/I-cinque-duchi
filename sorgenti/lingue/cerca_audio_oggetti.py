"""Conta che cosa si può ascoltare davvero, per lingua, su Wikimedia Commons.

Il documento `videogioco-5-duchi-parlato.md` §2.3 porta un numero che il progetto
non aveva: quante registrazioni libere esistono per ciascuna delle sei lingue. Il
numero che conta fra tutti è **zero per il ferrarese**, e quel numero è la ragione
per cui il progetto del ferrarese è un progetto di ascolto.

**Perché un contatore e non una ricerca.** Le 180 immagini degli oggetti sono state
cercate una per una (`cerca_immagini_oggetti.py`), perché un'immagine la si sceglie.
Un audio non si sceglie così: o esiste per quella lingua o non esiste, e la domanda
utile è **quanta parte del percorso si può coprire**. Il contatore risponde a
quella e produce il primo dato su cui scrivere i livelli; scegliere i file è un
secondo passo, e va fatto per voce, non per lingua.

**Le regole che vengono dal progetto, non da qui.**

- **Il `429` non è una risposta.** Il progetto l'ha già scritto nella regola dei
  fondi: un errore di rete lascia la scheda `da_rifare` e non chiude niente. Qui la
  conseguenza è che un numero di esiti contati può essere **minore** del vero, e il
  file lo dichiara con il campo `esito`: `contato` oppure `fallito`. Un `fallito`
  non è uno zero.
- **Il `Retry-After` si ascolta**, e le richieste hanno una pausa: novantasei query
  di fila hanno già fatto prendere un `429` a questo progetto durante la ricerca
  delle immagini.
- **Il conteggio è un dato con la sua data e la sua query**, non una verità: il
  file scrive entrambe, perché un numero senza la query che l'ha prodotto non è
  riproducibile.

Uso:
    python3 sorgenti/lingue/cerca_audio_oggetti.py            # tutte e sei
    python3 sorgenti/lingue/cerca_audio_oggetti.py --ferrarese # una lingua
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
USCITA = os.path.join(RADICE, "dati", "lingue", "audio_disponibili.json")

UA = "i-cinque-duchi/0.1 (progetto didattico per liceo; pietrofabbri)"
PAUSA = 4.0

# Le sei lingue del gioco, con il codice Wikidata della lingua. Il codice serve
# per la query: e' l'unico modo di chiedere «registrazioni **di questa** lingua»
# senza dover distinguere un file italiano da un file che parla d'italiano.
LINGUE = [
    ("it", "Italiano", "Q652"),
    ("en", "Inglese", "Q1860"),
    ("fe", "Ferrarese", "Q33224"),
    ("la", "Latino", "Q397"),
    ("el", "Greco", "Q9129"),
    ("si", "Lingua dei segni italiana", "Q12867462"),
]

# La query che conta: i file audio di Commons che portano il marchio di Lingua
# Libre (il progetto Wikimedia delle pronunciazioni, che dichiara registratore e
# licenza) e che hanno la lingua come dichiarazione. Il `filetype:audio` e' la
# parte che rende il numero confrontabile con quello delle immagini.
QUERY = ('"Lingua Libre" haswbstatement:P407=%s filetype:audio')


def get(host, params, tentativi=5):
    """Una richiesta, che ascolta il 429 e che non confonde la rete con una risposta."""
    for k in range(tentativi):
        url = "https://%s/w/api.php?" % host + urllib.parse.urlencode(params)
        try:
            r = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept": "application/json"})
            with urllib.request.urlopen(r, timeout=60) as f:
                return json.load(f)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 10.0 * (k + 1)
                time.sleep(att)
                continue
            # un altro errore HTTP e' una risposta del server, non la rete: la
            # scheda resta da rifare e il motivo si scrive
            return {"_errore": "HTTP %d" % e.code}
        except Exception as e:                       # noqa: BLE001 - rete
            if k == tentativi - 1:
                return {"_errore": str(e)[:70]}
            time.sleep(6.0 * (k + 1))
    return {"_errore": "insuccesso dopo i tentativi"}


def conta(host, query):
    """Il numero di file che la query trova, o None se non si e' potuto sapere."""
    d = get(host, {"action": "query", "format": "json", "list": "search",
                   "srsearch": query, "srnamespace": "6", "srlimit": "1"})
    if "_errore" in d:
        return None, d["_errore"]
    q = d.get("query")
    if q is None:
        return None, "risposta senza query"
    return q.get("searchinfo", {}).get("totalhits"), None


def main():
    lingue = LINGUE
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        scelto = sys.argv[1]
        lingue = [l for l in LINGUE if l[0] == scelto]
        if not lingue:
            raise SystemExit("lingua sconosciuta: %s" % scelto)

    record = []
    for i, (codice, nome, qid) in enumerate(lingue, 1):
        sys.stdout.write("  %d/%d  %-26s " % (i, len(lingue), nome))
        sys.stdout.flush()
        n, errore = conta("commons.wikimedia.org", QUERY % qid)
        if n is None:
            print("fallito (%s)" % errore)
        else:
            print("%s" % "{:,}".format(n).replace(",", " "))
        record.append({
            "lingua": codice,
            "nome": nome,
            "wikidata": qid,
            "registrazioni": n,
            "esito": "fallito" if n is None else "contato",
            "motivo_se_fallito": errore,
        })
        if i < len(lingue):
            time.sleep(PAUSA)

    # Il controllo che conta: lo zero del ferrarese non e' un numero, e' una
    # assenza verificata. Un fallimento e' diverso da uno zero, e i due non si
    # sommano.
    ferrarese = next((r for r in record if r["lingua"] == "fe"), None)
    verdetto = None
    if ferrarese and ferrarese["esito"] == "contato" and ferrarese["registrazioni"] == 0:
        verdetto = ("nessuna registrazione libera esiste per il ferrarese: l'ascolto di "
                    "questa lingua si produce, non si cerca")

    out = {
        "versione": 1,
        "data": "2026-10-03",
        "nota": ("Il numero di registrazioni libere che si possono usare come ascolto per ciascuna "
                 "lingua. Non e' un inventario di file scelti: e' la domanda «esiste materiale per "
                 "questa lingua?», e la risposta decide se l'ascolto si compra, si cerca o si "
                 "produce. Ogni numero porta la query che lo ha prodotto, perche' un numero senza "
                 "la sua query non e' riproducibile."),
        "query": QUERY % "<QID>",
        "fonte": "Wikimedia Commons, API, ricerca nel namespace File (6)",
        "nota_sul_risultato": ("Un `fallito` non e' uno zero: la richiesta e' stata interrotta dalla rete "
                              "o dal server e il numero resta ignoto. Il progetto lo chiama "
                              "`da_rifare` e non lo chiude."),
        "lingue": record,
        "verdetto_ferrarese": verdetto,
    }
    with open(USCITA, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    contati = [r for r in record if r["esito"] == "contato"]
    print("\ncontate %d lingue su %d; fallite %d"
          % (len(contati), len(record), len(record) - len(contati)))
    if verdetto:
        print("ferrarese: %s" % verdetto)
    print("scritto %s" % USCITA)


if __name__ == "__main__":
    main()