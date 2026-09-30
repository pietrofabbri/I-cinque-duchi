"""Ritratti per i dialoghi (48 x 54 px, 16 colori circa).
- Borso: ricavato dal ritratto di profilo (Vicino da Ferrara / Baldassarre d'Este, 1469-71, pubblico dominio),
  ridotto a 48x54 e 16 colori nel browser (media k-means); dati in ritratti_raw.json.
- Maurelio: disegnato a mano, ispirato ai colori dei tondi di Cosme Tura (1480): manto azzurro, tunica rosa;
  qui con mitra e pastorale da vescovo. Non e' un ritratto: e' una figura della tradizione.
- San Giorgio (visione): cavaliere di pietra, tono seppia, ispirato alla lunetta di Nicholaus (1135).
"""
import json
from PIL import Image, ImageDraw

def from_raw(d):
    im = Image.new('RGBA', (d['w'], d['h']))
    for y, r in enumerate(d['rows']):
        for x, c in enumerate(r):
            im.putpixel((x, y), tuple(bytes.fromhex(d['hex'][int(c, 36)])) + (255,))
    return im

raw = json.load(open('ritratti_raw.json'))
borso = from_raw(raw['borso'])
borso.save('out/ritratto_borso.png')

# --- Maurelio ---
W, H = 48, 54
m = Image.new('RGBA', (W, H), (46, 58, 92, 255)); g = ImageDraw.Draw(m)
# sfondo: arco rosso come nei tondi di Tura
g.ellipse((-6, 4, 54, 64), fill=(176, 72, 52)); g.ellipse((0, 10, 48, 70), fill=(58, 92, 70))
# manto azzurro
g.polygon([(4, 54), (8, 38), (16, 32), (32, 32), (40, 38), (44, 54)], fill=(70, 110, 190))
g.polygon([(8, 54), (11, 41), (16, 36), (18, 54)], fill=(110, 150, 220))
g.polygon([(34, 54), (37, 41), (40, 44), (42, 54)], fill=(44, 76, 140))
# stolone d'oro e tunica rosa
g.polygon([(18, 54), (20, 36), (28, 36), (30, 54)], fill=(214, 140, 150))
g.line((19, 36, 17, 54), fill=(214, 168, 64), width=2); g.line((29, 36, 31, 54), fill=(214, 168, 64), width=2)
# collo e viso
g.rectangle((20, 30, 28, 36), fill=(200, 150, 118))
g.ellipse((15, 15, 33, 35), fill=(218, 172, 136))
g.ellipse((15, 15, 33, 35), outline=(150, 104, 80))
# barba grigia
g.polygon([(15, 26), (18, 34), (24, 38), (30, 34), (33, 26), (30, 30), (24, 32), (18, 30)], fill=(206, 202, 194))
g.line((20, 33, 24, 36), fill=(160, 156, 150)); g.line((28, 33, 24, 36), fill=(160, 156, 150))
# occhi, naso, bocca
for x in (20, 27):
    g.rectangle((x, 23, x + 1, 23), fill=(40, 36, 44)); g.line((x - 1, 21, x + 2, 21), fill=(150, 130, 120))
g.line((24, 24, 23, 28), fill=(170, 120, 96)); g.line((22, 30, 26, 30), fill=(140, 90, 80))
# mitra
g.polygon([(15, 18), (17, 4), (24, 0), (31, 4), (33, 18)], fill=(244, 240, 228))
g.line((24, 1, 24, 18), fill=(214, 168, 64), width=2); g.line((16, 17, 32, 17), fill=(214, 168, 64), width=2)
g.polygon([(15, 18), (17, 4), (24, 0), (31, 4), (33, 18)], outline=(170, 160, 140))
# pastorale
g.line((42, 8, 42, 54), fill=(214, 168, 64), width=2)
g.arc((36, 2, 46, 12), 180, 90, fill=(214, 168, 64), width=2)
m.save('out/ritratto_maurelio.png')

# --- San Giorgio (visione, seppia) ---
gi = Image.new('RGBA', (W, H), (120, 96, 64, 255)); g = ImageDraw.Draw(gi)
g.ellipse((-10, 6, 58, 80), fill=(150, 124, 88))
s = Image.open('out/giorgio.png').resize((48, 48), Image.NEAREST)
gi.alpha_composite(s, (0, 6))
gi.save('out/ritratto_giorgio.png')

pv = Image.new('RGBA', (W * 3 + 20, H), (30, 30, 30, 255))
for i, im in enumerate((borso, m, gi)):
    pv.alpha_composite(im, (i * (W + 10), 0))
pv.resize((pv.width * 4, pv.height * 4), Image.NEAREST).save('out/_preview_ritratti.png')
