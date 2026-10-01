"""Genera provino_furioso.html: la stanza del filone, in una pagina e senza rete.

Perché il provino è generato e non scritto a mano: i dati dentro la pagina
sono gli stessi di dati/furioso/citazioni.json, e se la pagina li ripetesse a
mano accaderebbe quello che è già successo una volta in questo progetto — una
citazione copiata due volte, e due versioni che divergono. Qui la pagina si
ricostruisce ogni volta dal file, e il HTML è un prodotto, non una fonte.

La pagina è **una sola**, si apre dal filesystem, non chiede niente a nessuno:
il progetto ha deciso che il prototipo deve funzionare anche sulla lavagna di
una scuola senza rete, e un provino che funziona solo online non l'ha mai
verificato.

Uso:  python3 provino_html.py            -> scrive ../provino_furioso.html
      python3 provino_html.py --apri     -> lo apre nel browser
"""
import json
import os
import sys
import webbrowser

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSON = os.path.join(RADICE, "dati", "furioso", "citazioni.json")
HTML = os.path.join(RADICE, "provino_furioso.html")

# Le quattro tappe del provino: una del primo anno-sesto (l'errore), una sui
# dati, una sulla città del duca, una sulla prova finale.
TAPPE = ["5-1", "5-11", "5-20", "5-30"]

# I tre sentimenti dati come distractor per ogni tappa, con il motivo per cui
# sono sbagliati: un gioco didattico che sbaglia per indovinare non insegna.
DISTRACTOR = {
    "5-1": [("orgoglio", "non è orgoglio: è qualcuno che grida a chi non può ascoltarlo"),
            ("paura", "non c'è paura: c'è un uomo che si arrabbia con un animale")],
    "5-11": [("terrore", "non è terrore: l'isola è bella, e il pericolo non si vede"),
             ("noia", "nessuno si annoia davanti a un campione storto: è un problema")],
    "5-20": [("entusiasmo", "non è entusiasmo: il duca sa che l'acqua non basta mai"),
             ("indifferenza", "una città senza acqua non è indifferenza, è una faccenda")],
    "5-30": [("soddisfazione", "a metà dell'opera non si è soddisfatti: si è in carico"),
             ("nostalgia", "qui la domanda è in avanti, non indietro")],
}

TESTO = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>I cinque duchi — la stanza del filone (provino del 5º anno)</title>
<style>
  :root {{
    --inchiostro: #1b1a17;  -- carta: #f3ede1;   -- carta2: #eae1d0;
    --estero: #7a2e1e;      -- verde: #3f5d3a;   --ottone: #9a7b2f;
    --filo: #cfc3aa;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--carta); color: var(--inchiostro);
    font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
    font-size: 17px; line-height: 1.55;
  }}
  .fuori {{ max-width: 780px; margin: 0 auto; padding: 28px 20px 80px; }}
  h1 {{ font-size: 1.5rem; margin: 0 0 .2em; letter-spacing: .01em; }}
  h2 {{ font-size: 1.12rem; margin: 2em 0 .4em; }}
  .sotto {{ color: #6b6154; font-size: .92rem; margin: 0 0 1.6em; }}
  .avviso {{
    border-left: 3px solid var(--estero); background: #f7ece6; padding: 10px 14px;
    font-size: .92rem; margin: 0 0 2em;
  }}
  .scheda {{
    background: #fffdf7; border: 1px solid var(--filo); border-radius: 3px;
    padding: 18px 20px; margin: 0 0 26px;
  }}
  .riga {{ display: flex; flex-wrap: wrap; gap: 6px 10px; align-items: baseline;
           font-size: .84rem; color: #6b6154; margin: 0 0 10px; }}
  .tasta {{ border: 1px solid var(--filo); border-radius: 999px; padding: 1px 9px;
           background: var(--carta2); color: #4a4438; }}
  .tasta.filone {{ border-color: var(--verde); color: var(--verde); }}
  .citazione {{
    font-size: 1.16rem; margin: 0 0 .1em; padding-left: 14px;
    border-left: 2px solid var(--ottone);
  }}
  .rif {{ font-size: .82rem; color: #6b6154; margin: 0 0 18px 16px; }}
  .prompt {{ font-size: .95rem; margin: 0 0 8px; }}
  .scelte {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 12px; }}
  button {{
    font: inherit; font-size: .92rem; cursor: pointer; background: #fff;
    border: 1px solid var(--filo); border-radius: 3px; padding: 6px 12px; color: var(--inchiostro);
  }}
  button:hover {{ border-color: var(--estero); }}
  button[aria-pressed="true"] {{ background: var(--estero); border-color: var(--estero); color: #fff; }}
  .risposta {{ font-size: .95rem; min-height: 1.6em; }}
  .risposta.ok {{ color: var(--verde); }}
  .risposta.no {{ color: var(--estero); }}
  .parafrasi {{
    display: none; background: #f2f6f0; border: 1px solid #cddcc7; border-radius: 3px;
    padding: 14px 16px; margin: 14px 0 0;
  }}
  .parafrasi.aperta {{ display: block; }}
  .parafrasi p {{ margin: 0 0 .6em; }}
  .parafrasi p:last-child {{ margin: 0; }}
  .targa {{
    display: inline-block; background: var(--verde); color: #fff; border-radius: 2px;
    padding: 2px 9px; font-size: .86rem; margin: 0 0 10px;
  }}
  footer {{ margin-top: 3em; font-size: .84rem; color: #6b6154;
            border-top: 1px solid var(--filo); padding-top: 12px; }}
</style>
</head>
<body>
<div class="fuori">
  <h1>La stanza del filone</h1>
  <p class="sotto">Quinto anno, quattro tappe su trenta. È un provino: serve a vedere come si comporta
     una tappa quando dentro c'è una citazione del <i>Furioso</i>, e non a giocare.</p>

  <p class="avviso"><b>La regola della stanza.</b> Il <b>pin</b> — dove il gioco si ferma — resta il luogo
     reale del personaggio, verificato. La <b>stanza</b> invece è quella del filone: può essere un luogo
     che non esiste, e in quel caso si dichiara con il tipo <code>I</code>. Le citazioni sono state tutte
     verificate riestraendole dal testo (canto e ottava); nessuna è a memoria.</p>

  <h2>Le tappe</h2>
  <div id="tappe"></div>

  <footer>
    Testo: Ludovico Ariosto, <i>Orlando furioso</i>, edizione 1928 (Biblioteca BEIC), trascrizione di
    Wikisource, in pubblico dominio. Parafrasi e temi sono di questo progetto.
    Generato da <code>sorgenti/furioso/provino_html.py</code>: non modificarlo a mano.
  </footer>
</div>
<script id="dati" type="application/json">
{DATI}
</script>
<script>
(function () {{
  "use strict";
  var D = JSON.parse(document.getElementById("dati").textContent);
  var DIZ = {{
    "5-1":  {{ stanza: "Il bosco, la strada della fuga. Fuori, la disperazione; e tu hai una stima sbagliata.",
              moti:  ["sdegno"] }},
    "5-11": {{ stanza: "La spiaggia dell'isola. Fuori, il mare; e tu hai un campione storto.",
              moti:  ["inganno"] }},
    "5-20": {{ stanza: "Ferrara, l'oficina del duca. Fuori, il cantiere; e tu devi portare l'acqua dove serve.",
              moti:  ["preoccupazione"] }},
    "5-30": {{ stanza: "La sala di progetto, le sei fasce bianche sulla colonna.",
              moti:  ["impegno"] }}
  }};

  function testoVersi(r) {{
    return r.versi.map(function (v) {{ return "<div class='citazione'>" + v + "</div>"; }}).join("");
  }}

  function parafrasi(r) {{
    var p = DIZ[r.tappa] || {{}};
    return "<div class='parafrasi' id='pa-" + r.tappa + "'>" +
      "<p>" + (p.stanza || "") + "</p>" +
      "<p>" + r.parafrasi + "</p>" +
      "<span class='targa'>" + r.tema + "</span>" +
      "</div>";
  }}

  function scelte(r) {{
    var out = "<div class='prompt'>Che cosa prova, in quei versi, chi li sta vivendo?</div><div class='scelte'>";
    out += "<button data-t='" + r.tappa + "' data-v='" + r.moto + "'>" + r.moto + "</button>";
    (DIZ[r.tappa].distractor || []).forEach(function (d) {{
      out += "<button data-t='" + r.tappa + "' data-v='" + d[0] + "'>" + d[0] + "</button>";
    }});
    return out + "</div><div class='risposta' id='ri-" + r.tappa + "'></div>";
  }}

  function rispondi(t, v, giusto, perchè) {{
    var r = document.getElementById("ri-" + t);
    r.className = "risposta " + (v === giusto ? "ok" : "no");
    r.innerHTML = (v === giusto
      ? "Esatto. " + perchè.giusto
      : "Non quello. " + perchè.no);
    Array.prototype.slice.call(document.querySelectorAll("button[data-t='" + t + "']")).forEach(function (b) {{
      b.setAttribute("aria-pressed", String(b.dataset.v === giusto));
    }});
    document.getElementById("pa-" + t).classList.add("aperta");
  }}

  var PERCHE = {{
    "5-1":  {{ giusto: "Rinaldo grida e il cavallo non si ferma: è la stima sbagliata che non ti avvisa.",
              no:    "Il cavallo non è sordo per cattiveria: è che non è lì dove tu lo stai cercando." }},
    "5-11": {{ giusto: "Sull'isola sono tutti belli perché non c'è mai stato nessun altro: è il campione, non la vista.",
              no:    "L'inganno non è dell'isola: è di chi ha scelto le persone da mostrare." }},
    "5-20": {{ giusto: "Il duca non è entusiasta: è preoccupato, perché un quartiere senza acqua è un quartiere senza persone.",
              no:    "Il progetto non è un problema di entusiasmo: è un problema di tubi, e i tubi si contano." }},
    "5-30": {{ giusto: "Ariosto non promette niente: elenca. Alla fine del gioco farai lo stesso.",
              no:    "Qui non è ancora finito niente: è una lista, e le liste si onorano." }}
  }};

  var DIZ_DIST = {dict_distrattori};

  var scelta = {{}};
  function disegna() {{
    var host = document.getElementById("tappe");
    host.innerHTML = D.tappe.map(function (r) {{
      DIZ[r.tappa].distractor = DIZ_DIST[r.tappa];
      return "<section class='scheda'>" +
        "<div class='riga'>" +
          "<span class='tasta'>" + r.tappa + "</span>" +
          "<span class='tasta filone'>" + r.filone + " — " + r.filone_titolo + "</span>" +
          "<span class='tasta'>" + r.riferimento + "</span>" +
          "<span class='tasta'>legame " + r.legame + "</span>" +
          "<span>" + r.luogo + "</span>" +
        "</div>" + testoVersi(r) +
        "<p class='rif'>moto: " + r.moto + " · emozione: " + r.emozione + "</p>" +
        scelte(r) + parafrasi(r) + "</section>";
    }}).join("");
    Array.prototype.slice.call(host.querySelectorAll("button")).forEach(function (b) {{
      b.addEventListener("click", function () {{
        var r = D.tappe.find(function (x) {{ return x.tappa === b.dataset.t; }});
        scelta[b.dataset.t] = b.dataset.v;
        rispondi(b.dataset.t, b.dataset.v, r.moto, PERCHE[b.dataset.t]);
      }});
    }});
  }}
  disegna();
}})();
</script>
</body>
</html>
"""


def costruisci():
    with open(JSON, encoding="utf-8") as f:
        documento = json.load(f)
    per_tappa = {r["tappa"]: r for r in documento["citazioni"]}
    scelte = [per_tappa[t] for t in TAPPE]
    distrattori = {t: DIZ_DISTRACTOR[t] for t in TAPPE}
    dati = {"tappe": scelte}
    # DIFETTO CORRETTO IN QUESTA STESSA FUNZIONE: il modello è scritto con le
    # graffe raddoppiate ({{ }}), che sono la forma giusta per `str.format`,
    # ma la sostituzione era fatta con `str.replace`. Le graffe raddoppiate
    # restavano nel file e il JavaScript non partiva: la pagina mostrava il
    # titolo e le quattro tappe mancanti, senza un solo messaggio d'errore in
    # evidenza. Due sintassi per una cosa sola, e il risultato è una pagina
    # muta — che è il difetto peggiore che questo progetto sappia fare.
    return TESTO.format(DATI=json.dumps(dati, ensure_ascii=False, indent=1),
                        dict_distrattori=json.dumps(distrattori, ensure_ascii=False))


# I distrattori stanno qui e non dentro l'HTML: se fossero nel modello, il
# provino mostrerebbe i suoi stessi errori come se fossero del progetto.
DIZ_DISTRACTOR = DISTRACTOR

if __name__ == "__main__":
    with open(HTML, "w", encoding="utf-8") as f:
        f.write(costruisci())
    print("scritto %s (%d tappe)" % (HTML, len(TAPPE)))
    if "--apri" in sys.argv:
        webbrowser.open("file://" + HTML)