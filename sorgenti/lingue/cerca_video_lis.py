"""Conta che cosa si può **vedere** in lingua dei segni, e con quale testo accanto.

Il documento `videogioco-5-duchi-lingue.md` Q4 dichiara che i trenta livelli della
lingua dei segni sono i più difficili da scrivere di tutti i novecento, perché non
si può scrivere una lingua dei segni a tavolino, e `videogioco-5-duchi-premi.md`
§2.1 chiude la domanda con una frase che sembra definitiva: **«il gioco non sa
disegnare la propria lingua dei segni»**.

Questo script non smentisce quella frase e non prova a forzarla: mette sul tavolo
il numero che manca, cioè **quanti video liberi di LIS esistono al mondo e quanti
di quelli hanno, scritto accanto, il testo italiano corrispondente**. È il numero
che decide se la LIS entra nel gioco come qualcosa da guardare (che è legittimo) o
come qualcosa da decodificare (che è un'altra domanda, più difficile e ancora aperta).

**Perché un contatore e non una ricerca.** Come per l'audio (`cerca_audio_oggetti.py`):
un video di LIS non si sceglie voce per voce, si conta prima e si sceglie dopo. Il
conto che conta è però **due numeri e non uno**, perché sono due cose diverse:

- i **video in LIS** che esistono e sono liberi;
- i video che hanno **il testo italiano parallelo già dichiarato**, cioè quelli in
  cui il nome del file o la descrizione porta l'articolo, il periodo o la frase che
  il video traduce.

Il secondo numero è il primo con cui si può lavorare, perché è l'unico che permette
al gioco di mostrare il segno **e** la sua traduzione senza che nessuno debba
inventare la traduzione. È la stessa regola delle 180 immagini degli oggetti: la
prova 1 è la fonte, e una traduzione scritta dal progetto non è una fonte.

**Le regole che vengono dal progetto, non da qui.**

- **`ZERO` non è un numero, è un'assenza verificata.** Se la ricerca fallisce, la
  scheda dice `fallito` e non `zero`, e i due non si sommano mai.
- **Il `429` non è una risposta.** Si ascolta il `Retry-After` e si lascia la pausa:
  novantasei query di fila hanno già fatto prendere un `429` a questo progetto.
- **Ogni numero porta la sua data e la sua query**, perché un numero senza la query
  che l'ha prodotto non è riproducibile.
- **La licenza si guarda, non si presume.** Ogni file porta la sua, e il file
  elenca le licenze trovate: una sola licenza non libera fra i video escluderebbe
  l'uso nel gioco, e va detto prima di costruirci sopra.

Uso:
    python3 sorgenti/lingue/cerca_video_lis.py            # conta e scrive il file
    python3 sorgenti/lingue/cerca_video_lis.py --prova    # dice, non scrive
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
USCITA = os.path.join(RADICE, "dati", "lingue", "video_lis_disponibili.json")

UA = "i-cinque-duchi/0.1 (progetto didattico per liceo; pietrofabbri)"
PAUSA = 4.0

# La categoria di Commons che raccoglie i video in lingua dei segni italiana. Il
# codice Wikidata della lingua serve solo per la scheda: la categoria e' la fonte
# del numero, e va detto nel file che e' una categoria, non un elenco di tutto.
LINGUA_QID = "Q12867462"
CATEGORIA = "Category:Videos in Italian_Sign_Language"

# Le tre domande che il gioco deve poter fare, e che hanno risposte diverse.
DOMANDE = {
    "quanti_video": {
        "action": "query", "format": "json", "list": "categorymembers",
        "cmtitle": CATEGORIA, "cmlimit": "500", "cmtype": "file|subcat",
    },
    "quanti_video_con_testo": {
        "action": "query", "format": "json", "list": "categorymembers",
        "cmtitle": CATEGORIA, "cmlimit": "500", "cmtype": "file",
    },
}

# Il nome del file di una parte di questi video porta gia' l'articolo e il suo
# titolo in italiano: e' il testo parallelo, non una descrizione. Il confronto e'
# fatto per pattern e non per elenco, perche' l'elenco si invecchia con i dati.
PARALLELO = [
    ("convenzione_crpd", r"Articolo\s+\d+\s*-\s*.+"),
    ("titolo_in_italiano", r"[Dd]attilologia|alfabeto|[Ss]corpio"),
]


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
            return {"_errore": "HTTP %d" % e.code}
        except Exception as e:                       # noqa: BLE001 - rete
            if k == tentativi - 1:
                return {"_errore": str(e)[:70]}
            time.sleep(6.0 * (k + 1))
    return {"_errore": "insuccesso dopo i tentativi"}


def elenca(host):
    """I membri della categoria, o None se non si e' potuto sapere."""
    d = get(host, DOMANDE["quanti_video"])
    if "_errore" in d:
        return None, d["_errore"]
    q = d.get("query")
    if q is None:
        return None, "risposta senza query"
    return q.get("categorymembers", []), None


def metadati(host, titoli):
    """Licenza e peso di ogni file, a lotti di cinquanta (il massimo della API)."""
    out = {}
    for i in range(0, len(titoli), 50):
        blocco = titoli[i:i + 50]
        d = get(host, {
            "action": "query", "format": "json", "generator": "categorymembers",
            "gcmtitle": CATEGORIA, "gcmlimit": "500", "gcmtype": "file",
            "prop": "imageinfo", "iiprop": "url|extmetadata|size|mime",
            "titles": "|".join(t["title"] for t in blocco),
        })
        if "_errore" in d:
            return None, d["_errore"]
        for k, v in d.get("query", {}).get("pages", {}).items():
            ii = (v.get("imageinfo") or [{}])[0]
            em = ii.get("extmetadata", {})
            out[v["title"]] = {
                "licenza": em.get("LicenseShortName", {}).get("value", "dichiarata"),
                "byte": ii.get("size", 0),
                "mime": ii.get("mime", ""),
                "fonte": em.get("Artist", {}).get("value", ""),
            }
        time.sleep(PAUSA)
    return out, None


def main():
    prova = "--prova" in sys.argv
    host = "commons.wikimedia.org"

    membri, errore = elenca(host)
    if membri is None:
        print("  contatore fallito: %s" % errore)
        return 1

    video = [m for m in membri if not m["title"].lower().endswith((".jpg", ".jpeg",
                                                                  ".png", ".gif"))]
    sottocategorie = [m for m in membri if m["title"].lower().startswith("category:")]

    print("  video nella categoria: %d" % len(video))
    if sottocategorie:
        print("  attenzione: %d sottocategorie, il numero non le contiene"
              % len(sottocategorie))

    meta, errore2 = metadati(host, video)
    if meta is None:
        print("  metadati falliti: %s" % errore2)
        return 1

    licenze, pesi, con_testo = {}, {}, {}
    for t in video:
        m = meta.get(t["title"], {})
        licenze[m.get("licenza", "dichiarata")] = licenze.get(
            m.get("licenza", "dichiarata"), 0) + 1
        pesi[m.get("byte", 0)] = pesi.get(m.get("byte", 0), 0) + 1
        nome = t["title"].split(":", 1)[-1]
        for chiave, pattern in PARALLELO:
            if re.search(pattern, nome):
                con_testo[chiave] = con_testo.get(chiave, 0) + 1

    totale_mb = sum(meta.get(t["title"], {}).get("byte", 0)
                    for t in video) / 1e6
    liberi = sum(v for k, v in licenze.items()
                 if k.upper().startswith("CC BY") or "PUBLIC" in k.upper())
    non_liberi = len(video) - liberi

    # Il numero che decide: quanti video si possono mostrare **con la traduzione
    # scritta accanto**. E' la differenza fra guardare la LIS e poterla usare in
    # un gioco che deve anche spiegare, in italiano, che cosa sta dicendo.
    con_articolo = con_testo.get("convenzione_crpd", 0)
    verdetto = (
        "%d video su %d hanno il testo italiano parallelo gia' dichiarato nel nome "
        "del file: sono i soli su cui il gioco puo' mostrare il segno e la sua "
        "traduzione senza scrivere la traduzione lui"
        % (con_articolo, len(video)) if con_articolo else
        "nessun video ha il testo italiano parallelo dichiarato: mostrare la LIS "
        "nel gioco richiederebbe che il progetto scriva le traduzioni, e una "
        "traduzione scritta dal progetto non e' una fonte")

    out = {
        "versione": 1,
        "data": time.strftime("%Y-%m-%d"),
        "scopo": "quanti video liberi di lingua dei segni italiana esistono su "
                 "Wikimedia Commons, e quanti hanno gia' il testo italiano "
                 "parallelo dichiarato",
        "fonte": "Wikimedia Commons, categoria %s" % CATEGORIA,
        "wikidata_lingua": LINGUA_QID,
        "come_si_conta": "API list=categorymembers sulla categoria, poi "
                         "prop=imageinfo per licenza e peso; il testo parallelo "
                         "si riconosce dal nome del file, perche' e' l'articolo "
                         "della convenzione tradotto in italiano",
        "avvertenza_sulla_fonte": "una categoria non e' tutto quello che esiste: "
                                  "il numero e' quello che la categoria contiene, "
                                  "e va detto con la sua data",
        "video": len(video),
        "sottocategorie_non_conteggiate": len(sottocategorie),
        "con_testo_parallelo": con_testo,
        "licenze": licenze,
        "non_liberi": non_liberi,
        "peso_totale_mb": round(totale_mb, 1),
        "peso_medio_mb": round(totale_mb / len(video), 1) if video else 0,
        "esito": "contato",
        "verdetto": verdetto,
    }

    print("  con testo parallelo: %s" % (con_testo or "nessuno"))
    print("  licenze: %s" % ", ".join("%s %d" % kv for kv in sorted(licenze.items())))
    print("  non liberi: %d" % non_liberi)
    print("  peso: %.0f MB in tutto, %.1f MB l'uno" % (totale_mb,
                                                        out["peso_medio_mb"]))
    print("\n  verdetto: %s" % verdetto)

    if prova:
        print("--prova: non scrivo")
        return 0
    with open(USCITA, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("scritto %s" % os.path.relpath(USCITA, RADICE))
    return 0


if __name__ == "__main__":
    sys.exit(main())