"""Sprite dei personaggi (pixel art disegnata a mano, 16x24 per fotogramma).
Riferimenti visivi (solo per forme e colori, nessuna copia di pixel):
- Borso: ritratto di profilo attribuito a Vicino da Ferrara / Baldassarre d'Este (1469-71): berretta rossa alta,
  capelli grigio-castani a caschetto, veste rossa con broccato d'oro e collare di perle.
- Maurelio: tondi di Cosme Tura (1480, Pinacoteca di Ferrara): manto azzurro su tunica rosa; qui come vescovo con mitra.
Uscita: art/out/<nome>.png (fogli: righe = giu, sinistra, destra, su; colonne = fermo, passo A, passo B).
"""
from PIL import Image
import os
os.makedirs('out', exist_ok=True)

def img_from(rows, pal):
    h = len(rows); w = len(rows[0])
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    for y, r in enumerate(rows):
        assert len(r) == w, (y, r, len(r))
        for x, c in enumerate(r):
            if c != '.':
                v = pal[c]
                im.putpixel((x, y), tuple(bytes.fromhex(v)) + (255,))
    return im

# ---------- BORSO ----------
PB = {'k': '2a1e1c', 'R': 'c23a2b', 'r': '8e2a20', 'h': 'e0634f',  # berretta
      'H': '6b5d50', 'j': '4a3f36',                                # capelli
      's': 'e0b48a', 'S': 'b98763', 'e': '2a1e1c', 'm': '9a5a48',  # viso
      'P': 'f2ead0', 'G': 'd9a441', 'g': 'a8762a', 'B': 'b0342a', 'b': '7c2219',  # veste
      'L': '5a2320', 'F': '2a1e1c'}                                  # calze, scarpe

B_DOWN = [
    "....kkkkkkkk....",
    "...khRRRRRRRk...",
    "...khRRRRRRrk...",
    "...khRRRRRRrk...",
    "...khRRRRRRrk...",
    "...krrrrrrrrk...",
    "..kjHHHHHHHHjk..",
    "..kHHssssssHHk..",
    "..kHHseSSesHHk..",
    "..kHHssSSssHHk..",
    "..kjHsSmmSsHjk..",
    "...kjSssssSjk...",
    "....kkSSSSkk....",
    "..kPGPGPGPGPGk..",
    ".kbBBGBBBBGBBbk.",
    ".kbBGGGBBGGGBbk.",
    ".kbBBGBBBBGBBbk.",
    ".kbBGGGBBGGGBbk.",
    ".ksBBGBBBBGBBsk.",
    "..kBBBBBBBBBBk..",
    "..kgGgGgGgGgGk..",
]
B_UP = [
    "....kkkkkkkk....",
    "...kRRRRRRRRk...",
    "...kRRRRRRRRk...",
    "...kRRRRRRRRk...",
    "...kRRRRRRRRk...",
    "...krrrrrrrrk...",
    "..kjHHHHHHHHjk..",
    "..kHHHHHHHHHHk..",
    "..kHHHHjjHHHHk..",
    "..kHHHHHHHHHHk..",
    "..kjHHHjjHHHjk..",
    "...kjHHHHHHjk...",
    "....kkSSSSkk....",
    "..kPGPGPGPGPGk..",
    ".kbBBBBBBBBBBbk.",
    ".kbBBGBBBBGBBbk.",
    ".kbBBBBBBBBBBbk.",
    ".kbBBGBBBBGBBbk.",
    ".ksBBBBBBBBBBsk.",
    "..kBBBBBBBBBBk..",
    "..kgGgGgGgGgGk..",
]
B_RIGHT = [  # di profilo verso destra, come nel ritratto
    "....kkkkkkkk....",
    "...kRRRRRRRhk...",
    "...kRRRRRRRhk...",
    "...kRRRRRRRhk...",
    "...kRRRRRRRhk...",
    "...krrrrrrrrk...",
    "..kjHHHHHHssk...",
    "..kHHHHHHsssk...",
    "..kHHHHHssesk...",
    "..kHHHHHsssssk..",
    "..kjHHHHSsssk...",
    "...kjHHHSmSk....",
    "....kkkSSSSk....",
    "...kPGPGPGPk....",
    "..kbBBGBBGBBk...",
    "..kbBGGGBGGBk...",
    "..kbBBGBsBBBk...",
    "..kbBGGGBGGBk...",
    "..kbBBGBBBBBk...",
    "..kBBBBBBBBBk...",
    "..kgGgGgGgGgk...",
]

def legs(frame, side=False):
    if side:
        L = {0: ["....kLLLk.......", "....kLLLk.......", "....kFFFFk......"],
             1: ["...kLLk.kLk.....", "..kLLk...kLk....", "..kFFk...kFFk..."],
             2: ["....kLLkLk......", ".....kLLLk......", ".....kFFFFk....."]}
        return L[frame]
    L = {0: ["....kLLkkLLk....", "....kLLkkLLk....", "...kFFFkkFFFk..."],
         1: ["....kLLkkLLk....", "....kLLk.kkk....", "...kFFFk........"],
         2: ["....kLLkkLLk....", "....kkk.kLLk....", "........kFFFk..."]}
    return L[frame]

def sheet(views, pal, name):
    W, H = 16, 24
    sh = Image.new('RGBA', (W * 3, H * 4), (0, 0, 0, 0))
    down, up, right = views
    for f in range(3):
        sh.paste(img_from(down + legs(f), pal), (f * W, 0))
        r = img_from(right + legs(f, True), pal)
        sh.paste(r.transpose(Image.FLIP_LEFT_RIGHT), (f * W, H))
        sh.paste(r, (f * W, 2 * H))
        sh.paste(img_from(up + legs(f), pal), (f * W, 3 * H))
    sh.save(f'out/{name}.png')
    return sh

sheet((B_DOWN, B_UP, B_RIGHT), PB, 'borso')

# ---------- MAURELIO (vescovo: mitra bianca, piviale azzurro, tunica rosa, barba grigia, pastorale) ----------
PM = {'k': '1f2233', 'W': 'f4f1e6', 'w': 'c9c3b0', 'Y': 'd9a441',
      's': 'd9ab86', 'S': 'a97c5c', 'e': '1f2233', 'A': 'd8d4cc', 'a': 'a39e94',  # viso, barba
      'U': '4f79c4', 'u': '2f4f8f', 'V': '8fb0e6', 'P': 'd98c95', 'p': 'a85e68',
      'C': 'd9a441', 'c': '8a6420', 'F': '3a2a22'}
M_DOWN = [
    "......kWk.......",
    ".....kWYWk......",
    "....kWWYWWk.....",
    "....kWWYWWk.C...",
    "....kwYYYwk.CC..",
    "...kAssssSAk.C..",
    "...kAseSSeAk.c..",
    "...kAsssssAk.c..",
    "...kaAAmAAak.c..",
    "....kaAAAak..c..",
    "..kUUkPPPkUUkc..",
    ".kUVUUPYPUUUUc..",
    ".kUVUUPYPUUUsc..",
    ".kUVUUPYPUUUuc..",
    ".kUVUUPYPUUuuc..",
    ".kUVUUPYPUUuuc..",
    ".kUVUUPYPUUuuc..",
    ".kUVUUPYPUUuuc..",
    ".kuUUUPPPUUuukc.",
    "..kuuuPPPuuuk.c.",
    "..kkkkPpPkkkk.c.",
    "....kpPPPpk...c.",
    "....kFFkFFk.....",
    "................",
]
PM['m'] = '8a6a5a'

def static_sheet(rows, pal, name, frames=2):
    im = img_from(rows, pal)
    W, H = im.size
    sh = Image.new('RGBA', (W * frames, H), (0, 0, 0, 0))
    sh.paste(im, (0, 0))
    if frames > 1:  # respiro: il busto si abbassa di un pixel
        b = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        b.paste(im.crop((0, 0, W, 12)), (0, 1))
        b.paste(im.crop((0, 12, W, H)), (0, 12))
        sh.paste(b, (W, 0))
    sh.save(f'out/{name}.png')

static_sheet(M_DOWN, PM, 'maurelio')

# ---------- SAN GIORGIO (visione: cavaliere di pietra, tono seppia) 32x32 ----------
PG = {'k': '3b2a1a', 'W': 'efe0c2', 'w': 'cdb58e', 'd': 'a88a60', 'D': '7d6343', 'L': 'b99a6a'}
G = [
    "................................",
    "............kkk.................",
    "...........kWWWk................",
    "...........kWwWk................",
    "...........kkWkk................",
    "..........kWWWWWk...............",
    ".........kdkWWWWdk......kk......",
    ".........kdkWWWWdk.....kWWk.....",
    ".........kdkWWwWLLk...kWWWWk....",
    "..........kkWWWWkkLk.kWWWkWk....",
    "...........kWWWWk..LkWWWWWWWk...",
    ".....kkk..kWwwwWk..kLWWWWkkWWk..",
    "....kWWWkkWWWWWWWkkWWLWWk..kk...",
    "...kWWWWWWWWWWWWWWWWWWLk........",
    "..kWWwWWWWWWWWWWWWWWWWkLk.......",
    "..kWwWWWWWWWWWWWWWWWWWk.kLk.....",
    ".kWwkWWWWWWWWWWWWWWWWdk..kLk....",
    ".kWk.kWWWWWWWWWWWWWWddk...kLk...",
    ".kWk..kWWwwwwwwwwWWWdk.....kLk..",
    "..k...kWwkkkkkkkkkWWwk......kLk.",
    "......kWwk.......kWwWk.......kk.",
    ".....kWwk.......kWwkWwk.........",
    ".....kWk........kWk.kWk.........",
    "....kWk.........kWk..kWk....kk..",
    "....kdk........kWk....kdk..kLLk.",
    "...kddk........kdk....kddkkLddLk",
    "...kkk........kddk.....kkLLddLk.",
    "..............kkk.....kLLdkkLk..",
    "......................kLk..kk...",
    ".......................k........",
    "................................",
    "................................",
]
img_from(G, PG).save('out/giorgio.png')

# ---------- LAPIDE 16x16 ----------
PL = {'k': '3a3530', 'W': 'd8d2c6', 'w': 'b3ab9c', 'd': '8a8174', 'g': '6f8a4a'}
LAP = [
    "................",
    "....kkkkkkkk....",
    "...kWWWWWWWWk...",
    "..kWWwWWWWwWWk..",
    "..kWdWdWddWdWk..",
    "..kWWWWWWWWWwk..",
    "..kWdddWdWddWk..",
    "..kWWWWWWWWWwk..",
    "..kWdWddWdWdwk..",
    "..kWWWWWWWWwwk..",
    "..kWddWdWddwwk..",
    "..kWWWWWWWwwwk..",
    "..kwwwwwwwwwwk..",
    ".gkkkkkkkkkkkkg.",
    "gggggggggggggggg",
    "................",
]
img_from(LAP, PL).save('out/lapide.png')

def preview():
    names = ['borso', 'maurelio', 'giorgio', 'lapide']
    ims = [Image.open(f'out/{n}.png') for n in names]
    W = sum(i.width for i in ims) + 10 * len(ims); H = max(i.height for i in ims)
    pv = Image.new('RGBA', (W, H), (120, 140, 110, 255))
    x = 0
    for i in ims:
        pv.alpha_composite(i, (x, 0)); x += i.width + 10
    pv.resize((W * 4, H * 4), Image.NEAREST).save('out/_preview_sprites.png')
preview()

# ---------- STATUE DEL VOLTO DEL CAVALLO (bronzo, copie del 1927) e CARTELLO ----------
PS = {'k': '1e2a24', 'B': '4f6b5a', 'b': '34493d', 'l': '7d9a86', 'M': 'e8e0d2', 'm': 'bdb2a2', 'd': '8f8475'}
STATUA_BORSO = [  # Borso seduto, sopra la colonna
    "......kkkk......",
    ".....kBBBBk.....",
    ".....kBlBBk.....",
    ".....kBBBBk.....",
    "......kBBk......",
    "....kkBBBBkk....",
    "...kBBlBBBBBk...",
    "...kBlBBBBBbk.k.",
    "...kBBBBBBBbkBk.",
    "...kkBBBBBBkkBk.",
    "..kBBBBBBBBBbBk.",
    "..kBlBBBBBBBbk..",
    "..kkkkBkkBkkkk..",
    "....kBk..kBk....",
    "...kkkk..kkkk...",
    "..kmmmmmmmmmmk..",
    "...kMMMMMMMMk...",
] + ["....kMMMmmdk...."] * 22 + ["...kMMMMmmmdk...", "..kMMMMMmmmmdk..", "..kkkkkkkkkkkk.."]
STATUA_NICCOLO = [  # Niccolo III a cavallo, sopra l'arco
    "..........kk....................",
    ".........kBBk...................",
    ".........kBlk...................",
    "........kBBBBk..................",
    "........kBlBBk.............kk...",
    ".........kBBk.............kBBk..",
    "..kkkkkkkBBBBkkkkkkkkkkkkkBBlBk.",
    ".kBBBBBBBBBBBBBBBBBBBBBBBBBBkkk.",
    "kBlBBBBBBBBBBBBBBBBBBBBBBBBk....",
    "kBBBBBBBBBBBBBBBBBBBBBBBBBk.....",
    ".kbBBBBBBBBBBBBBBBBBBBBBBbk.....",
    "..kbkbk..........kbk..kbk.......",
    "..kbkbk..........kbk..kbk.......",
    "..kkkkk..........kkk..kkk.......",
    ".kmmmmmmmmmmmmmmmmmmmmmmmmmmk...",
    "..kMMMMMMMMMMMMMMMMMMMMMMMMk....",
] + ["......kMMMmmdk........kMMmdk...."] * 20 + ["....kMMMMMmmmdk.....kMMMMmmdk...", "....kkkkkkkkkkk.....kkkkkkkkk..."]
img_from(STATUA_BORSO, PS).save('out/statua_borso.png')
img_from(STATUA_NICCOLO, PS).save('out/statua_niccolo.png')
PC = {'k': '2a2a2a', 'W': 'f4f1e6', 'w': 'c9c3b0', 'G': '2f6e3a', 'g': '1f4a26', 't': '555555'}
CARTELLO = [
    "kkkkkkkkkkkkkkkk",
    "kGGGGGGGGGGGGGGk",
    "kGWWWWWWWWWWWWGk",
    "kGWttWtttWttWWGk",
    "kGWWWWWWWWWWWWGk",
    "kGWtttWttWtttWGk",
    "kGWWWWWWWWWWWWGk",
    "kGWttWttttWttWGk",
    "kGWWWWWWWWWWWWGk",
    "kGGGGGGGGGGGGGGk",
    "kkkkkkkkkkkkkkkk",
    "......kggk......",
    "......kggk......",
    "......kggk......",
    "......kggk......",
    ".....kggggk.....",
]
img_from(CARTELLO, PC).save('out/cartello.png')
