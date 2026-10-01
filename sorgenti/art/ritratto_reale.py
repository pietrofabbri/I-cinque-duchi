"""Ritratto_reale.py — scarica i ritratti autentici e li riduce per i dialoghi.

Fa la stessa cosa che `ritratti.py` fa per Borso, ma su 148 immagini vere
invece che su una: scarica il file da Wikimedia, **taglia la testa**, riduce a
48x54 px e riduce i colori.

Il taglio della testa e' la parte difficile, e qui e' approssimato. Non si puo'
chiedere a una libreria di riconoscere i volti senza dipendenze che il progetto
non vuole, quindi si usa una regola: il ritratto e' normalmente un busto o una
mezza figura, e il viso sta nella meta' superiore. Si prende la finestra piu'
alta possibile che abbia le proporzioni del riquadro e il centro non troppo in
basso, e poi si centra.

Il risultato va guardato: `prepara_fogli.py` produce un foglio di prova con tutti
i 148 ritratti, da aprire per controllare i tagli sbagliati.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error

from PIL import Image, ImageFilter

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ELENCO = os.path.join(RADICE, "sorgenti", "art", "ritratti_disponibili.json")
GREZZI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ritratti_grezzi")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
LATO = 48
ALTEZZA = 54
UA = "i-cinque-duchi/0.2 (progetto didattico per liceo; pietrofabbri)"


def scarica(nome_file, destino):
    """Scarica una versione ridotta del file di Commons.

    600 px e non 400: il viso viene ritagliato e poi ridotto a 48, e con 400 px
    di partenza l'occhio, che occupa forse un sesto dell'altezza, si ritrova
    con 13 pixel di altezza da cui ricavare 20: si vede che e' sfocato.
    """
    url = ("https://commons.wikimedia.org/wiki/Special:FilePath/"
           + urllib.parse.quote(nome_file) + "?width=600")
    for k in range(5):
        try:
            r = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(r, timeout=60) as f:
                dati = f.read()
            with open(destino, "wb") as g:
                g.write(dati)
            return True
        except urllib.error.HTTPError as e:
            # Commons risponde 429 a raffica. Tre tentativi ravvicinati non
            # bastano: sei immagini su centosessanta restavano fuori perche'
            # il ciclo di tentativi non ascoltava il 429 e il fallimento
            # finiva in 'download fallito', che sembrava un file rotto.
            if e.code in (429, 503):
                att = float(e.headers.get("Retry-After") or 0) or 6 * (k + 1)
                time.sleep(att)
                continue
            time.sleep(2 * (k + 1))
        except Exception:
            time.sleep(2 * (k + 1))
    return False


def taglia_testa(im, larghezza=LATO, altezza=ALTEZZA):
    """Finestra del viso: alta, non troppo in basso, centrata sul ritratto,
    e **ridotta davvero** a 48x54.

    DIFETTO CORRETTO: la prima versione ritagliava con le proporzioni giuste ma
    non ridimensionava, e restituiva un'immagine di 400x450 o 500x562. Il
    risultato era un file da 97 kB al posto di 2, e un riquadro del gioco con
    dentro un'immagine trent volte piu' grande: che il motore non riduce a
    schermo, perche' il motore lavora gia' su 48x54 e si limita a quantizzare
    i colori. Le immagini sembravano sfocate e i file pesavano 14 MB.
    """
    w, h = im.size
    rapp = larghezza / altezza            # 0,889
    # finestra più alta compatibile con le proporzioni del riquadro
    fh = min(h, w / rapp)
    fw = min(w, fh * rapp)
    # in un ritratto il viso sta in alto: si parte dal bordo superiore
    fy = 0.0
    # ma se l'immagine è molto alta (figura intera), si scende un poco
    if h > w * 1.6:
        fy = (h - fh) * 0.22
    elif h > w * 1.2:
        fy = (h - fh) * 0.10
    fx = (w - fw) / 2
    # nei quadri il soggetto è spesso leggermente a sinistra o a destra:
    # si centra sul contenuto non vuoto, non sull'immagine
    grigi = im.convert("L")
    bbox = grigi.point(lambda v: 255 if v > 22 else 0).getbbox()
    if bbox:
        cx = (bbox[0] + bbox[2]) / 2
        fx = max(0, min(w - fw, cx - fw / 2))
    box = (int(fx), int(fy), int(fx + fw), int(fy + fh))
    rit = im.crop(box)
    # Lanczos tiene i dettagli fini meglio di un ridimensionamento per corrispondenza
    # dei pixel, che a questa scala lascia solo dei blocchi
    rit = rit.resize((larghezza, altezza), Image.LANCZOS)
    # e un maschera di contrasto, perche' a 48 pixel di lato la riduzione
    # ammorbidisce tutto e i lineamenti del viso scompaiono
    return rit.filter(ImageFilter.UnsharpMask(radius=1.2, percent=90, threshold=2))


def riduci(im, colori=16):
    """Riduce a `colori` colori, come la media usata per il ritratto di Borso."""
    q = im.convert("RGB").quantize(colors=colori, method=Image.MEDIANCUT)
    # `info` eredita dal file originale può contenere una chiave `transparency`
    # con dentro una tupla RGBA: Pillow la passa al salvataggio come se fosse un
    # singolo valore e il salvataggio fallisce. La pulizia evita di dover
    # ricontrollare ogni formato di partenza.
    q.info.clear()
    return q


if __name__ == "__main__":
    os.makedirs(GREZZI, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    elenco = json.load(open(ELENCO, encoding="utf-8"))
    utili = [e for e in elenco if e["motivo"] == "ok"]
    print(f"da scaricare: {len(utili)}")

    fatti = saltati = 0
    for n, e in enumerate(utili, 1):
        grezzo = os.path.join(GREZZI, e["codice"] + ".img")
        # `immagine_reale` e' il nome vero del file: quello in `immagine` puo'
        # essere il nome della miniatura, con il prefisso di dimensione, e quel
        # nome su Commons non porta a nessuna scheda
        sorgente = e.get("immagine_reale") or e["immagine"]
        if not os.path.exists(grezzo):
            if not scarica(sorgente, grezzo):
                e["motivo"] = "download fallito"
                saltati += 1
                continue
            time.sleep(0.15)
        try:
            im = Image.open(grezzo)
            im.load()
        except Exception:
            e["motivo"] = "immagine non apribile"
            saltati += 1
            continue
        if im.mode in ("RGBA", "LA", "P"):
            # il fondo trasparente diventa il color pergamena del progetto
            im = im.convert("RGBA")
            fondo = Image.new("RGBA", im.size, (236, 228, 210, 255))
            fondo.alpha_composite(im)
            im = fondo.convert("RGB")
        else:
            im = im.convert("RGB")
        ridotto = riduci(taglia_testa(im))
        # il controllo e' qui dentro e non affidato a un occhio: se un'immagine
        # esce di misura, il file non e' quello che il motore si aspetta, e
        # finisce copiato in tutti i dialoghi
        if ridotto.size != (LATO, ALTEZZA):
            ridotto = ridotto.resize((LATO, ALTEZZA), Image.LANCZOS)
        ridotto.save(os.path.join(OUT, f"ritratto_{e['codice']}.png"),
                     optimize=True)
        fatti += 1
        if n % 20 == 0:
            print(f"  {n}/{len(utili)}", flush=True)

    with open(ELENCO, "w", encoding="utf-8") as f:
        json.dump(elenco, f, ensure_ascii=False, indent=1)
    print(f"\nritratti prodotti: {fatti}   saltati: {saltati}")
    print(f"in {OUT}")