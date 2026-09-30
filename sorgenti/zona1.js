// ===== Zona percorribile della tappa 1 (piazza della Cattedrale) — v0.2 =====
// Borso è il personaggio giocante. Vista dall'alto 3/4 in stile GBA, motore canvas scritto a mano.
// Geometria reale: sagome e altezze degli edifici dagli open data del Comune di Ferrara (vedi gis/zona1_build.py).
// Dati e grafica: Z1DATA e Z1ART (zona1_dati.js). Esercizi: openBottega (esercizi1.js).
const ZPX = 12.8;   // pixel per metro al suolo (1 tessera = 1,25 m = 16 px)
const ZHP = 10;     // pixel per metro di altezza (vista 3/4)
const Z1NPC = {
  maurelio: { u: -3.4, v: 2.4, n: 'San Maurelio', spr: 'maurelio', por: 'r_maurelio' },
  giorgio:  { u: 3.6,  v: 2.6, n: 'San Giorgio (visione)', spr: 'giorgio', por: 'r_giorgio', vis: true },
  lapide:   { u: -13.0, v: 1.6, n: 'La lapide', spr: 'lapide', por: null },
  cartello: { u: -12.5, v: 17.0, n: 'Cartello', spr: 'cartello', por: null },
};
const Z1START = { u: 4, v: 15 };
// arredo: biciclette (Ferrara, città delle biciclette), lampioni, piccioni
const Z1PROPS = [
  ...[0, 1, 2, 3, 4, 5].map(i => ({ t: 'bici', u: 9 + i * 1.1, v: 22.5, c: ['#8c2d19', '#2f5d8c', '#3f7d4e', '#222', '#d4a017', '#6b4f2e'][i] })),
  ...[0, 1, 2, 3].map(i => ({ t: 'bici', u: -20 + i * 1.1, v: 11, c: ['#2f5d8c', '#8c2d19', '#222', '#3f7d4e'][i] })),
  { t: 'lamp', u: -16, v: 5 }, { t: 'lamp', u: 16, v: 5 }, { t: 'lamp', u: -8, v: 24 }, { t: 'lamp', u: 18, v: 20 },
];
const Z1ART_PROPS = {
  bici: ['.....kk....kk...', '......c....c....', '......cccccc....', '.....c.c..c.c...', '..kkkc...cc.kkk.', '.k...k...c.k...k', 'k..c..k..ck..c.k', '.k...k....k...k.', '..kkk......kkk..'],
  lamp: ['..kkkk..', '.kyyyyk.', '.kyWWyk.', '.kyyyyk.', '..kkkk..', '...kk...', ...Array(20).fill('...kk...'), '..kkkk..', '.kkkkkk.'],
  pic: ['..gg..', '.gkgg.', 'wggggg', '.gggg.', '..y.y.'],
};
function z1propImg(rows, col) { const pal = { k: '#2b2b2b', c: col || '#8c2d19', y: '#e8c45a', W: '#fff8d8', g: '#8d8f96', w: '#c8cad0' };
  const c = document.createElement('canvas'); c.width = rows[0].length; c.height = rows.length; const x = c.getContext('2d');
  rows.forEach((r, j) => [...r].forEach((ch, i) => { if (ch !== '.') { x.fillStyle = pal[ch]; x.fillRect(i, j, 1, 1); } })); return c; }

function z1img(src) { const i = new Image(); i.src = src; return i; }

function z1prepare() {
  if (window.__Z1) return window.__Z1;
  const D = Z1DATA, [U0, U1, V0, V1] = D.r;
  const GW = Math.round((U1 - U0) * ZPX), GH = Math.round((V1 - V0) * ZPX);
  const X = u => (u - U0) * ZPX, Y = v => (v - V0) * ZPX;
  const IMG = {}; for (const k in Z1ART) IMG[k] = z1img(Z1ART[k]);
  const rnd = s => { s = Math.sin(s * 99991.7) * 43758.5453; return s - Math.floor(s); };
  const path = (c, ring, dy = 0) => { ring.forEach((p, i) => i ? c.lineTo(X(p[0]), Y(p[1]) + dy) : c.moveTo(X(p[0]), Y(p[1]) + dy)); c.closePath(); };

  // ---------- suolo ----------
  const ground = document.createElement('canvas'); ground.width = GW; ground.height = GH;
  const g = ground.getContext('2d');
  function patt(w, h, fn) { const c = document.createElement('canvas'); c.width = w; c.height = h; fn(c.getContext('2d')); return g.createPattern(c, 'repeat'); }
  const cobble = patt(16, 16, c => { c.fillStyle = '#a99a82'; c.fillRect(0, 0, 16, 16);
    for (let y = 0; y < 16; y += 4) for (let x = (y / 4) % 2 * 2; x < 16; x += 4) { c.fillStyle = ['#b7a88f', '#b0a189', '#bcae96'][(x + y) % 3]; c.fillRect(x, y, 3, 3); } });
  const slabs = patt(48, 48, c => { const id = c.createImageData(48, 48);
    for (let y = 0; y < 48; y++) for (let x = 0; x < 48; x++) { const row = Math.floor(y / 6), off = (row % 2) * 5, col = Math.floor((x + off) / 10);
      const edge = y % 6 === 0 || (x + off) % 10 === 0; const base = 196 + Math.floor(rnd(row * 31 + col * 7) * 14) - 7, n = Math.floor(rnd(x * 13 + y * 71) * 8) - 4;
      const v = edge ? base - 22 : base + n; const q = (y * 48 + x) * 4; id.data[q] = v + 6; id.data[q + 1] = v + 1; id.data[q + 2] = v - 10; id.data[q + 3] = 255; }
    c.putImageData(id, 0, 0); });
  g.fillStyle = cobble; g.fillRect(0, 0, GW, GH);
  g.fillStyle = slabs; D.ped.forEach(r => { g.beginPath(); path(g, r); g.fill(); });
  // fasce chiare di pietra d'Istria che disegnano la pavimentazione (griglia di 6 m)
  g.save(); g.beginPath(); D.ped.forEach(r => path(g, r)); g.clip(); g.fillStyle = 'rgba(236,232,222,.55)';
  for (let u = Math.ceil(U0 / 6) * 6; u < U1; u += 6) g.fillRect(X(u), 0, 3, GH);
  for (let v = Math.ceil(V0 / 6) * 6; v < V1; v += 6) g.fillRect(0, Y(v), GW, 3);
  g.restore();
  // tombini e macchie: piccoli dettagli sparsi
  for (let i = 0; i < 260; i++) { const x = rnd(i * 3.1) * GW, y = rnd(i * 7.7) * GH; g.fillStyle = i % 5 ? 'rgba(90,80,70,.10)' : 'rgba(255,255,255,.18)'; g.fillRect(x | 0, y | 0, 2 + (i % 3), 1 + (i % 2)); }
  // ombre portate (luce da sinistra in alto)
  g.fillStyle = 'rgba(50,38,30,.10)';
  D.ed.forEach(b => { for (let s = 1; s <= 6; s++) { const k = s / 6; g.beginPath(); path(g, b.p.map(p => [p[0] + b.h * .32 * k, p[1] + b.h * .06 * k])); g.fill(); } });

  // ---------- edifici: sprite pre-disegnati (muri visibili + tetto) ----------
  const WALLS = ['#b5563c', '#c98f5a', '#d9b27a', '#c46a4f', '#d8a78f', '#a9493a', '#e0c28f', '#b97a55'];
  const ROOFS = ['#a8472f', '#b4563a', '#9c4330', '#b8603f'];
  const shade = (hex, k) => { const n = parseInt(hex.slice(1), 16); const f = v => Math.max(0, Math.min(255, Math.round(v * k)));
    return `rgb(${f(n >> 16)},${f(n >> 8 & 255)},${f(n & 255)})`; };
  const area = r => r.reduce((s, p, i) => { const q = r[(i + 1) % r.length]; return s + p[0] * q[1] - q[0] * p[1]; }, 0) / 2;
  const B = D.ed.map(b => {
    const H = b.h * ZHP, cat = b.k === 'cattedrale';
    const xs = b.p.map(p => X(p[0])), ys = b.p.map(p => Y(p[1]));
    let x0 = Math.floor(Math.min(...xs)) - 2, x1 = Math.ceil(Math.max(...xs)) + 2;
    let y0 = Math.floor(Math.min(...ys) - H) - 2, y1 = Math.ceil(Math.max(...ys)) + 2;
    if (cat) y0 = Math.min(y0, Math.floor(Y(0) - 330));
    const c = document.createElement('canvas'); c.width = x1 - x0; c.height = y1 - y0;
    const k = c.getContext('2d'); k.translate(-x0, -y0);
    const wall = cat ? '#e8ddd0' : WALLS[Math.floor(rnd(b.id) * WALLS.length)];
    const roof = ROOFS[Math.floor(rnd(b.id + 7) * ROOFS.length)];
    // muri: lati la cui normale (verso l'esterno del volume) guarda verso chi gioca
    const rings = [[b.p, true], ...b.ho.map(h => [h, false])];
    const faces = [];
    rings.forEach(([r, outer]) => { const cw = area(r) < 0; // in coordinate (u,v) con v verso il basso
      for (let i = 0; i < r.length; i++) { const p = r[i], q = r[(i + 1) % r.length];
        const du = q[0] - p[0], dv = q[1] - p[1], L = Math.hypot(du, dv); if (L < .3) continue;
        let nu = dv / L, nv = -du / L; if (cw === outer) { nu = -nu; nv = -nv; }
        // (anello esterno: normale verso fuori; buco: normale verso il cortile)
        if (nv > 0.08) faces.push({ p, q, L, nu, nv, top: Math.max(Y(p[1]), Y(q[1])) }); } });
    faces.sort((a, b2) => a.top - b2.top);
    faces.forEach(f => {
      const lit = .78 + .22 * f.nv - .10 * f.nu;
      k.fillStyle = shade(wall, lit);
      k.beginPath(); k.moveTo(X(f.p[0]), Y(f.p[1])); k.lineTo(X(f.q[0]), Y(f.q[1]));
      k.lineTo(X(f.q[0]), Y(f.q[1]) - H); k.lineTo(X(f.p[0]), Y(f.p[1]) - H); k.closePath(); k.fill();
      k.fillStyle = shade(wall, lit * .8); // zoccolo
      k.beginPath(); k.moveTo(X(f.p[0]), Y(f.p[1])); k.lineTo(X(f.q[0]), Y(f.q[1]));
      k.lineTo(X(f.q[0]), Y(f.q[1]) - 7); k.lineTo(X(f.p[0]), Y(f.p[1]) - 7); k.closePath(); k.fill();
      if (cat) return;
      // finestre e porte, piano per piano
      const nwin = Math.floor(f.L / 3.1), floors = Math.floor((b.h - 1) / 3.4);
      const ww = Math.max(2, Math.round(Math.abs(f.q[0] - f.p[0]) / f.L * .95 * ZPX));
      for (let i = 0; i < nwin; i++) {
        const t = (i + .5) / nwin, gx = X(f.p[0] + (f.q[0] - f.p[0]) * t), gy = Y(f.p[1] + (f.q[1] - f.p[1]) * t);
        for (let fl = 0; fl < floors; fl++) {
          const top = gy - (fl * 3.4 + (fl ? 2.6 : 2.4)) * ZHP, hh = (fl ? 1.7 : 2.1) * ZHP;
          if (fl === 0 && rnd(b.id + i) < .5) { k.fillStyle = '#3b2c26'; k.fillRect(gx - ww / 2, gy - 2.3 * ZHP, ww, 2.3 * ZHP); continue; }
          k.fillStyle = shade(wall, lit * .62); k.fillRect(gx - ww / 2 - 1, top - 1, ww + 2, hh + 2);
          k.fillStyle = fl ? '#4a5560' : '#3b3430'; k.fillRect(gx - ww / 2, top, ww, hh);
          k.fillStyle = 'rgba(255,255,255,.25)'; k.fillRect(gx - ww / 2, top, Math.max(1, ww / 3), hh);
          k.fillStyle = shade(wall, 1.15); k.fillRect(gx - ww / 2 - 1, top + hh, ww + 2, 1);
        }
      }
      // cornicione
      k.strokeStyle = shade(wall, .6); k.lineWidth = 1; k.beginPath(); k.moveTo(X(f.p[0]), Y(f.p[1]) - H + .5); k.lineTo(X(f.q[0]), Y(f.q[1]) - H + .5); k.stroke();
    });
    // tetto
    k.save(); k.beginPath(); path(k, b.p, -H); b.ho.forEach(h => path(k, h, -H));
    k.fillStyle = cat ? '#b0503a' : roof; k.fill('evenodd'); k.clip('evenodd');
    b.f.forEach(([o, s, pp]) => { const lit = 1 + .16 * o[1] - .12 * o[0] - .05 * (s > 25);
      k.beginPath(); path(k, pp, -H); k.fillStyle = shade(cat ? '#b0503a' : roof, lit); k.fill();
      k.strokeStyle = shade(roof, .72); k.stroke(); });
    k.globalAlpha = .18; k.fillStyle = '#3a1a10';
    for (let yy = y0; yy < y1; yy += 3) k.fillRect(x0, yy, x1 - x0, 1); // file di coppi
    k.restore();
    k.strokeStyle = 'rgba(40,20,14,.55)'; k.beginPath(); path(k, b.p, -H); k.stroke();
    b.ho.forEach(h => { k.beginPath(); path(k, h, -H); k.stroke(); });
    // bottom al suolo per colonna (serve per capire chi sta davanti)
    const bottomAt = (u) => { let best = -1e9;
      for (let i = 0; i < b.p.length; i++) { const p = b.p[i], q = b.p[(i + 1) % b.p.length];
        if ((p[0] - u) * (q[0] - u) <= 0 && p[0] !== q[0]) { const t = (u - p[0]) / (q[0] - p[0]); best = Math.max(best, p[1] + t * (q[1] - p[1])); } }
      return best; };
    const cu = b.p.reduce((a, p) => a + p[0], 0) / b.p.length, cvv = b.p.reduce((a, p) => a + p[1], 0) / b.p.length;
    const inZone = cat || z1pip(cu, cvv, D.zona);
    let cf = c; if (!inZone) { cf = document.createElement('canvas'); cf.width = c.width; cf.height = c.height; const q = cf.getContext('2d');
      q.drawImage(c, 0, 0); q.globalCompositeOperation = 'source-atop'; q.fillStyle = 'rgba(236,234,230,.74)'; q.fillRect(0, 0, c.width, c.height); }
    return { id: b.id, cat, c: cf, x0, y0, x1, y1, depth: Math.max(...ys), bottomAt, h: b.h, inZone };
  });
  const CAT = B.find(b => b.cat);

  // ---------- maschera percorribile (4 celle per metro) ----------
  const MR = 4; const mw = Math.round((U1 - U0) * MR), mh = Math.round((V1 - V0) * MR);
  const mc = document.createElement('canvas'); mc.width = mw; mc.height = mh; const m = mc.getContext('2d');
  const mp = (ring) => { m.beginPath(); ring.forEach((p, i) => i ? m.lineTo((p[0] - U0) * MR, (p[1] - V0) * MR) : m.moveTo((p[0] - U0) * MR, (p[1] - V0) * MR)); m.closePath(); };
  m.fillStyle = '#000'; m.fillRect(0, 0, mw, mh);
  m.fillStyle = '#fff'; mp(D.zona); m.fill();
  m.fillStyle = '#000'; D.ed.forEach(b => { mp(b.p); m.fill(); m.lineWidth = 1.2; m.strokeStyle = '#000'; m.stroke(); });
  m.fillRect((-20 - U0) * MR, (-0.2 - V0) * MR, 40 * MR, 1.3 * MR); // gradini della facciata
  const md = m.getImageData(0, 0, mw, mh).data;
  const walk = (u, v) => { const i = Math.floor((u - U0) * MR), j = Math.floor((v - V0) * MR);
    if (i < 0 || j < 0 || i >= mw || j >= mh) return false; return md[(j * mw + i) * 4] > 128; };
  // al suolo, fuori dalla zona (serve per l'uscita verso la tappa 2)
  const walkAny = (u, v) => { for (const b of D.ed) { if (z1pip(u, v, b.p)) return false; } return u > U0 && u < U1 && v > V0 && v < V1; };

  // ---------- nebbia: maschera statica (1 px ogni 2 px di mappa) ----------
  const FS = 2, fw = Math.ceil(GW / FS), fh = Math.ceil(GH / FS);
  const fog = document.createElement('canvas'); fog.width = fw; fog.height = fh; const f = fog.getContext('2d');
  const fpath = () => { f.beginPath(); D.zona.forEach((p, i) => i ? f.lineTo(X(p[0]) / FS, Y(p[1]) / FS) : f.moveTo(X(p[0]) / FS, Y(p[1]) / FS)); f.closePath(); };
  f.fillStyle = 'rgba(238,236,232,.86)'; f.fillRect(0, 0, fw, fh);
  f.globalCompositeOperation = 'destination-out';
  fpath(); f.fillStyle = '#000'; f.fill();
  for (let i = 10; i >= 1; i--) { fpath(); f.lineJoin = 'round'; f.lineWidth = i * 3.2; f.strokeStyle = 'rgba(0,0,0,.14)'; f.stroke(); }
  f.globalCompositeOperation = 'source-over';
  // nuvole (rumore morbido e ripetibile)
  const cl = document.createElement('canvas'); cl.width = cl.height = 128; const cc = cl.getContext('2d');
  const id = cc.createImageData(128, 128); const val = (x, y) => rnd((x & 15) * 57 + (y & 15) * 131 + 7);
  const sm = t => t * t * (3 - 2 * t);
  for (let y = 0; y < 128; y++) for (let x = 0; x < 128; x++) { let a = 0, amp = .55, fr = 8;
    for (let o = 0; o < 3; o++) { const gx = x / (128 / fr), gy = y / (128 / fr), ix = Math.floor(gx), iy = Math.floor(gy), tx = sm(gx - ix), ty = sm(gy - iy);
      const w = (xx, yy) => val(((xx % fr) + fr) % fr * (16 / fr), ((yy % fr) + fr) % fr * (16 / fr));
      a += amp * ((w(ix, iy) * (1 - tx) + w(ix + 1, iy) * tx) * (1 - ty) + (w(ix, iy + 1) * (1 - tx) + w(ix + 1, iy + 1) * tx) * ty); amp *= .5; fr = Math.min(16, fr * 2); }
    const q = (y * 128 + x) * 4; id.data[q] = id.data[q + 1] = id.data[q + 2] = 255; id.data[q + 3] = Math.max(0, Math.min(255, (a - .35) * 420)); }
  cc.putImageData(id, 0, 0);

  window.__Z1 = { D, U0, U1, V0, V1, GW, GH, X, Y, IMG, ground, B, CAT, walk, walkAny, fog, FS, clouds: cl };
  return window.__Z1;
}
function z1pip(x, y, r) { let ins = false; for (let i = 0, j = r.length - 1; i < r.length; j = i++) { const [xi, yi] = r[i], [xj, yj] = r[j];
  if ((yi > y) !== (yj > y) && x < (xj - xi) * (y - yi) / (yj - yi) + xi) ins = !ins; } return ins; }

function openZona1(opts) { // opts: {stato, onExit}
  const Z = z1prepare(), st = opts.stato;
  st.z = st.z && st.z.v2 ? st.z : { v2: true, pos: { ...Z1START, d: 'up' }, done: false, a1: false, a2: false, parlato: false };
  const Zs = st.z;
  if (!document.getElementById('z1css')) { const s = document.createElement('style'); s.id = 'z1css'; s.textContent = `
  .z1{position:fixed;inset:0;z-index:10;background:#1e1a17;user-select:none;-webkit-user-select:none;touch-action:none;overflow:hidden}
  .z1 canvas.scr{position:absolute;inset:0;width:100%;height:100%;image-rendering:pixelated;image-rendering:crisp-edges}
  .z1 .top{position:absolute;left:10px;right:10px;top:8px;display:flex;justify-content:space-between;align-items:center;gap:8px;pointer-events:none}
  .z1 .top .tag{background:rgba(255,250,240,.92);color:#2b2118;border:2px solid #2b2118;border-radius:8px;padding:4px 10px;font:600 13px/1.3 system-ui,sans-serif}
  .z1 .top button{pointer-events:auto;margin:0;background:#fffaf0;color:#2b2118;border:2px solid #2b2118;border-radius:8px;padding:5px 12px;font:600 13px system-ui,sans-serif;cursor:pointer}
  .z1 .banner{position:absolute;left:50%;top:18%;transform:translate(-50%,-20px);opacity:0;transition:.6s;background:#fffaf0;border:3px solid #2b2118;border-radius:10px;padding:10px 22px;font:700 20px Georgia,serif;color:#2b2118;box-shadow:0 4px 0 #2b2118;pointer-events:none;text-align:center}
  .z1 .banner small{display:block;font:500 12px system-ui,sans-serif;color:#8c2d19;letter-spacing:.08em;text-transform:uppercase}
  .z1 .banner.on{opacity:1;transform:translate(-50%,0)}
  .z1 .say{position:absolute;left:50%;bottom:14px;transform:translateX(-50%);width:min(760px,calc(100% - 20px));display:flex;gap:12px;align-items:stretch;background:#fffaf0;color:#2b2118;border:4px solid #2b2118;border-radius:12px;box-shadow:0 5px 0 #2b2118;padding:10px 14px;font:18px/1.4 Georgia,serif;cursor:pointer}
  .z1 .say.vis{background:#f3e6cc;color:#4a3620;border-color:#6b4f2e;box-shadow:0 5px 0 #6b4f2e}
  .z1 .say img{width:96px;height:108px;image-rendering:pixelated;border:3px solid #2b2118;border-radius:6px;background:#2b2118;flex:none}
  .z1 .say .who{font:700 12px system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#8c2d19;margin-bottom:4px}
  .z1 .say .tx{min-height:3.2em}
  .z1 .say .opt{display:flex;gap:8px;justify-content:flex-end;flex-wrap:wrap;margin-top:6px}
  .z1 .say .opt button{margin:0;background:#8c2d19;color:#fff;border:0;border-radius:8px;padding:6px 14px;font:600 14px system-ui,sans-serif;cursor:pointer}
  .z1 .say .opt button.sec{background:#e9dfcb;color:#2b2118}
  .z1 .say .more{position:absolute;right:14px;bottom:8px;animation:z1b 1s steps(2) infinite;font-size:14px}
  @keyframes z1b{50%{opacity:0}}
  .z1 .stick{position:absolute;left:18px;bottom:18px;width:120px;height:120px;border-radius:50%;background:rgba(255,250,240,.18);border:2px solid rgba(255,250,240,.5);display:none}
  .z1 .stick i{position:absolute;left:38px;top:38px;width:44px;height:44px;border-radius:50%;background:rgba(255,250,240,.7)}
  .z1 .abtn{position:absolute;right:22px;bottom:34px;width:72px;height:72px;border-radius:50%;background:#8c2d19;color:#fff;border:3px solid #fffaf0;font:700 26px system-ui,sans-serif;display:none}
  .z1.touch .stick,.z1.touch .abtn{display:block}
  .z1.talking .stick,.z1.talking .abtn{display:none!important}
  @media (max-width:560px){.z1 .top .tag{font-size:11px;padding:3px 8px}.z1 .say{font-size:16px}.z1 .say img{width:64px;height:72px}}
  .z1 .help{position:absolute;right:10px;bottom:8px;color:#fffaf0;opacity:.75;font:12px system-ui,sans-serif;text-shadow:0 1px 2px #000;pointer-events:none}
  .z1.touch .help{display:none}
  .z1 .box2{position:fixed;inset:0;background:rgba(40,30,20,.45);z-index:12;overflow:auto;padding-top:10px}
  .z1 .wm{position:fixed;right:12px;top:48px;font-size:11px;color:#fffaf0;opacity:.45;pointer-events:none}`; document.head.appendChild(s); }

  const ov = document.createElement('div'); ov.className = 'z1' + (matchMedia('(pointer:coarse)').matches ? ' touch' : '');
  ov.innerHTML = `<canvas class="scr"></canvas>
   <div class="top"><span class="tag">Tappa 1 · Piazza della Cattedrale · sei <b>Borso</b></span><button id="zx">Mappa</button></div>
   <div class="banner" id="ban"><small>Ferrara · tappa 1</small>Piazza della Cattedrale</div>
   <div class="say hidden" id="say"><img id="por" alt=""><div style="flex:1"><div class="who" id="who"></div><div class="tx" id="tx"></div><div class="opt" id="opt"></div></div><span class="more" id="more">▼</span></div>
   <div class="stick" id="stick"><i></i></div><button class="abtn" id="ab">A</button>
   <div class="help">Frecce o WASD: cammina · Maiusc: corri · Spazio: parla</div>
   <div class="box2 hidden" id="box2"><div class="ovin" id="bin"></div></div><div class="wm" id="wm"></div>`;
  document.body.appendChild(ov);
  ['copy', 'cut', 'contextmenu', 'dragstart'].forEach(ev => ov.addEventListener(ev, e => e.preventDefault()));
  ov.querySelector('#wm').textContent = `${st.nome || 'giocatore'} · istanza ${st.seed || '-'} · ${new Date().toLocaleString('it-IT')}`;
  const scr = ov.querySelector('canvas.scr'), sc = scr.getContext('2d');
  const buf = document.createElement('canvas'), bc = buf.getContext('2d');
  const tmp = document.createElement('canvas'), tc = tmp.getContext('2d');
  let S = 3, VW = 0, VH = 0;
  function resize() { const w = ov.clientWidth, h = ov.clientHeight;
    const s0 = Math.min(w / 640, h / 400); S = s0 >= 2 ? Math.min(4, Math.floor(s0)) : Math.max(1.25, Math.min(2, Math.min(w / 280, h / 330))); VW = Math.ceil(w / S); VH = Math.ceil(h / S);
    buf.width = tmp.width = VW; buf.height = tmp.height = VH; scr.width = VW * S; scr.height = VH * S;
    scr.style.width = VW * S + 'px'; scr.style.height = VH * S + 'px'; }
  resize(); addEventListener('resize', resize);

  // ---------- stato del giocatore ----------
  const P = { u: Zs.pos.u, v: Zs.pos.v, d: Zs.pos.d || 'up', vu: 0, vv: 0, t: 0 };
  const cam = { x: Z.X(P.u) - VW / 2, y: Z.Y(P.v) - VH * .64 };
  const keys = {}; let stick = { x: 0, y: 0 };
  let dlg = null, modalOn = false, ended = false, closedAt = 0;
  const npcs = () => Object.entries(Z1NPC).filter(([k, n]) => !n.vis || Zs.done);

  const solid = (u, v) => { if (!Z.walk(u, v)) return true;
    for (const [k, n] of npcs()) if (Math.hypot(u - n.u, (v - n.v) * 1.6) < .55) return true;
    for (const p of Z1PROPS) if (p.t === 'lamp' ? Math.hypot(u - p.u, (v - p.v) * 1.6) < .35 : Math.abs(u - p.u) < .55 && Math.abs(v - p.v) < .25) return true; return false; };
  const PI = {}; Z1PROPS.forEach(p => { const key = p.t + (p.c || ''); if (!PI[key]) PI[key] = z1propImg(Z1ART_PROPS[p.t], p.c); p.img = PI[key]; });
  const PIG = z1propImg(Z1ART_PROPS.pic); const pig = [...Array(7)].map((_, i) => ({ u: -6 + i * 1.7, v: 16 + (i % 3) * 1.3, hu: -6 + i * 1.7, hv: 16 + (i % 3) * 1.3, fly: 0, t: i }));
  const blocked = (u, v) => solid(u - .3, v) || solid(u + .3, v) || solid(u, v - .15) || solid(u - .3, v - .15) || solid(u + .3, v - .15);
  // uscita verso la tappa 2 (lato destro della zona, lungo il fianco della Cattedrale) dopo la soglia
  const exitZone = (u, v) => Zs.done && u > 27.2 && v > -2 && v < 14;

  function update(dt) {
    if (dlg || modalOn || ended) { P.vu = P.vv = 0; return; }
    let ax = (keys.right ? 1 : 0) - (keys.left ? 1 : 0) + stick.x, ay = (keys.down ? 1 : 0) - (keys.up ? 1 : 0) + stick.y;
    const L = Math.hypot(ax, ay); if (L > 1) { ax /= L; ay /= L; }
    const sp = (keys.run ? 7.5 : 4.6) * (L > .15 ? 1 : 0);
    const k = 1 - Math.exp(-dt * 14);
    P.vu += (ax * sp - P.vu) * k; P.vv += (ay * sp - P.vv) * k;
    if (L > .15) P.d = Math.abs(ax) > Math.abs(ay) ? (ax > 0 ? 'right' : 'left') : (ay > 0 ? 'down' : 'up');
    const nu = P.u + P.vu * dt, nv = P.v + P.vv * dt;
    if (Zs.done && (exitZone(nu, P.v) || exitZone(P.u, nv))) { exit(); return; }
    if (!blocked(nu, P.v) || (Zs.done && nu > 26 && P.v < 14 && Z.walkAny(nu, P.v))) P.u = nu; else P.vu = 0;
    if (!blocked(P.u, nv) || (Zs.done && P.u > 26 && nv < 14 && Z.walkAny(P.u, nv))) P.v = nv; else P.vv = 0;
    P.t += Math.hypot(P.vu, P.vv) * dt;
    pig.forEach(b => { const d = Math.hypot(P.u - b.u, P.v - b.v);
      if (d < 2.2 && !b.fly) b.fly = .01;
      if (b.fly) { b.fly = Math.min(1, b.fly + dt * 1.5); b.u += (b.u - P.u) * dt * 1.2; b.dir = Math.sign(b.u - P.u);
        if (b.fly >= 1 && d > 6) { b.fly = 0; b.u = b.hu + (Math.random() - .5) * 4; b.v = b.hv + (Math.random() - .5) * 3; } }
      else if (Math.random() < dt * .6) { b.dir = Math.random() < .5 ? -1 : 1; b.u += b.dir * .25; } });
    Zs.pos = { u: P.u, v: P.v, d: P.d };
    // chicche: avvicinandosi ai leoni o alla facciata compare un segno
  }

  function near() { let best = null, bd = 2.3;
    for (const [k, n] of npcs()) { const d = Math.hypot(P.u - n.u, P.v - n.v); if (d < bd) { bd = d; best = k; } }
    if (!best && P.v < 3.2 && Math.abs(P.u) < 20) { if (Math.abs(Math.abs(P.u) - 2.4) < 1.3) return 'leoni'; return 'facciata'; }
    return best; }

  // ---------- disegno ----------
  const FR = { down: 0, left: 1, right: 2, up: 3 };
  function sprite(img, u, v, frame, row, alpha = 1, w = 16, h = 24) { const x = Math.round(Z.X(u) - w / 2 - cam.x), y = Math.round(Z.Y(v) - h + 2 - cam.y);
    bc.globalAlpha = alpha; bc.drawImage(img, frame * w, row * h, w, h, x, y, w, h); bc.globalAlpha = 1; return [x, y, w, h]; }
  function shadow(u, v, r = 6) { bc.fillStyle = 'rgba(30,20,15,.28)'; bc.beginPath(); bc.ellipse(Math.round(Z.X(u) - cam.x), Math.round(Z.Y(v) - cam.y), r, r * .45, 0, 0, 7); bc.fill(); }
  function drawBuilding(b, clip) { const x = b.x0 - cam.x, y = b.y0 - cam.y;
    if (x > VW || y > VH || x + b.c.width < 0 || y + b.c.height < 0) return;
    if (clip) { bc.save(); bc.beginPath(); bc.rect(...clip); bc.clip(); }
    bc.drawImage(b.c, Math.round(x), Math.round(y));
    if (b.cat) { const fx = Z.X(-19.9) - cam.x, fy = Z.Y(1.0) - Z.IMG.facciata.height - cam.y; bc.drawImage(Z.IMG.facciata, Math.round(fx), Math.round(fy)); }
    if (clip) bc.restore(); }
  function marker(u, v, t, col = '#d4a017') { const x = Math.round(Z.X(u) - cam.x), y = Math.round(Z.Y(v) - 34 - cam.y + Math.sin(t * 4) * 2);
    bc.fillStyle = '#2b2118'; bc.fillRect(x - 4, y - 5, 9, 11); bc.fillStyle = col; bc.fillRect(x - 3, y - 4, 7, 9);
    bc.fillStyle = '#2b2118'; bc.fillRect(x, y - 3, 1, 4); bc.fillRect(x, y + 3, 1, 1); }
  function label(txt, u, v, col = '#2b2118', bg = 'rgba(255,250,240,.9)') { bc.font = '8px system-ui,sans-serif'; const w = bc.measureText(txt).width + 8;
    const x = Math.round(Z.X(u) - cam.x - w / 2), y = Math.round(Z.Y(v) - cam.y);
    bc.fillStyle = bg; bc.fillRect(x, y - 9, w, 12); bc.strokeStyle = col; bc.strokeRect(x + .5, y - 8.5, w - 1, 11); bc.fillStyle = col; bc.fillText(txt, x + 4, y); }

  let T = 0;
  function draw() {
    // telecamera morbida
    const tx = Z.X(P.u) - VW / 2, ty = Z.Y(P.v) - VH * (VH > VW ? .74 : .64);
    cam.x += (tx - cam.x) * .12; cam.y += (ty - cam.y) * .12;
    cam.x = Math.max(0, Math.min(Z.GW - VW, cam.x)); cam.y = Math.max(0, Math.min(Z.GH - VH, cam.y));
    const cx = Math.round(cam.x), cy = Math.round(cam.y);
    bc.imageSmoothingEnabled = false; bc.fillStyle = '#8f8270'; bc.fillRect(0, 0, VW, VH);
    bc.drawImage(Z.ground, cx, cy, VW, VH, 0, 0, VW, VH);
    // nebbia con nuvole in movimento
    tc.clearRect(0, 0, VW, VH); tc.globalCompositeOperation = 'source-over'; tc.imageSmoothingEnabled = true;
    tc.drawImage(Z.fog, cx / Z.FS, cy / Z.FS, VW / Z.FS, VH / Z.FS, 0, 0, VW, VH);
    tc.globalCompositeOperation = 'source-atop'; tc.globalAlpha = .55;
    const pat = tc.createPattern(Z.clouds, 'repeat'); const ox = (T * 6 + cx * .9) % 128, oy = (T * 2.5 + cy * .9) % 128;
    tc.save(); tc.translate(-ox, -oy); tc.fillStyle = pat; tc.fillRect(0, 0, VW + 128, VH + 128); tc.restore();
    tc.globalAlpha = 1; tc.globalCompositeOperation = 'source-over';
    bc.drawImage(tmp, 0, 0);
    // confine della zona (tratteggio dorato) e nomi delle zone vicine nella nebbia
    bc.save(); bc.translate(-cx, -cy); bc.setLineDash([3, 3]); bc.lineDashOffset = -T * 8; bc.strokeStyle = 'rgba(212,160,23,.9)'; bc.lineWidth = 1;
    bc.beginPath(); Z.D.zona.forEach((p, i) => i ? bc.lineTo(Z.X(p[0]), Z.Y(p[1])) : bc.moveTo(Z.X(p[0]), Z.Y(p[1]))); bc.closePath(); bc.stroke(); bc.restore();
    // edifici in ordine di profondità
    const bs = Z.B.slice().sort((a, b) => a.depth - b.depth);
    bs.forEach(b => drawBuilding(b));
    // personaggi e oggetti, dall'alto in basso
    const ents = [];
    for (const [k, n] of npcs()) ents.push({ v: n.v, f: () => {
      const img = Z.IMG[n.spr], vis = n.vis;
      if (k === 'lapide') { shadow(n.u, n.v, 7); return sprite(img, n.u, n.v, 0, 0, Zs.a1 ? 1 : .6, 16, 16); }
      if (k === 'cartello') { shadow(n.u, n.v, 6); return sprite(img, n.u, n.v, 0, 0, 1, 16, 16); }
      if (k === 'giorgio') { const a = .55 + .2 * Math.sin(T * 2); return sprite(img, n.u, n.v + .6, 0, 0, a, 32, 32); }
      shadow(n.u, n.v); return sprite(img, n.u, n.v, Math.floor(T * 1.5) % 2, 0); } });
    Z1PROPS.forEach(p => ents.push({ v: p.v, f: () => { const w = p.img.width, h = p.img.height; if (p.t === 'lamp') shadow(p.u, p.v, 3);
      const x = Math.round(Z.X(p.u) - w / 2 - cam.x), y = Math.round(Z.Y(p.v) - h + 1 - cam.y); bc.drawImage(p.img, x, y); return [x, y, w, h]; } }));
    pig.forEach(b => ents.push({ v: b.v, f: () => { const x = Math.round(Z.X(b.u) - 3 - cam.x), y = Math.round(Z.Y(b.v) - 5 - cam.y - b.fly * 30);
      if (b.fly < .2) { bc.fillStyle = 'rgba(30,20,15,.2)'; bc.fillRect(x + 1, y + 4, 4, 1); }
      bc.save(); if (b.dir < 0) { bc.translate(x * 2 + 6, 0); bc.scale(-1, 1); } bc.drawImage(PIG, x, y - (Math.sin(T * 12 + b.t) > .9 && !b.fly ? 1 : 0)); bc.restore(); return [x, y, 6, 5]; } }));
    const moving = Math.hypot(P.vu, P.vv) > .4, fr = moving ? [1, 0, 2, 0][Math.floor(P.t * 1.6) % 4] : 0;
    ents.push({ v: P.v, me: true, f: () => { shadow(P.u, P.v); return sprite(Z.IMG.borso, P.u, P.v, fr, FR[P.d]); } });
    ents.sort((a, b) => a.v - b.v);
    const rects = [];
    ents.forEach(e => { const r = e.f(); rects.push([r, e]); });
    // chi sta dietro un edificio viene coperto
    rects.forEach(([r, e]) => { const u = e.me ? P.u : null; const [x, y, w, h] = r; const wx = x + cam.x, wy = y + cam.y;
      bs.forEach(b => { if (wx + w < b.x0 || wx > b.x1 || wy + h < b.y0 || wy > b.y1) return;
        const uu = (wx + w / 2) / ZPX + Z.U0, bot = b.bottomAt(uu); const vv = (wy + h) / ZPX + Z.V0;
        if (bot > vv - .1 && bot > -1e8) { bc.globalAlpha = e.me ? .5 : 1; drawBuilding(b, [x, y, w, h]); bc.globalAlpha = 1; } }); });
    // indicatori
    const nb0 = !dlg && !modalOn && near();
    if (!Zs.done && nb0 !== 'maurelio') marker(Z1NPC.maurelio.u, Z1NPC.maurelio.v, T);
    else if (Zs.done && !Zs.a1 && nb0 !== 'giorgio') marker(Z1NPC.giorgio.u, Z1NPC.giorgio.v, T, '#c9a36b');
    else if (Zs.a1 && !Zs.a2 && nb0 !== 'lapide') marker(Z1NPC.lapide.u, Z1NPC.lapide.v + .2, T, '#c9a36b');
    const nb = !dlg && !modalOn && near();
    if (nb) { const n = Z1NPC[nb] || { u: P.u, v: P.v - 1.2 }; const x = Math.round(Z.X(nb in Z1NPC ? n.u : P.u) - cam.x), y = Math.round(Z.Y(nb in Z1NPC ? n.v : P.v) - 44 - cam.y);
      bc.fillStyle = '#fffaf0'; bc.fillRect(x - 6, y - 7, 13, 12); bc.strokeStyle = '#2b2118'; bc.strokeRect(x - 5.5, y - 6.5, 12, 11); bc.fillStyle = '#2b2118'; bc.font = 'bold 9px system-ui'; bc.fillText('A', x - 3, y + 2); }
    Z.D.tv.forEach(t => { if (t.livello === '1-1') return; const next = t.livello === '1-2';
      label((next && Zs.done ? '→ ' : '🔒 ') + 'Tappa ' + t.livello.split('-')[1] + (next ? ' · Loggia dei Merciai' : ''), t.uv[0], t.uv[1], next && Zs.done ? '#8c2d19' : '#6b6259'); });
    if (Zs.done) { const x = Math.round(Z.X(26.5) - cam.x), y = Math.round(Z.Y(6) - cam.y) + Math.round(Math.sin(T * 5) * 2);
      bc.fillStyle = '#8c2d19'; bc.beginPath(); bc.moveTo(x + 10, y); bc.lineTo(x, y - 7); bc.lineTo(x, y + 7); bc.fill(); }
    sc.imageSmoothingEnabled = false; sc.drawImage(buf, 0, 0, VW, VH, 0, 0, VW * S, VH * S);
  }

  let last = performance.now(), raf = 0;
  function loop(now) { const dt = Math.min(.05, (now - last) / 1000); last = now; T += dt; update(dt); if (ended) return; draw(); raf = requestAnimationFrame(loop); }

  // ---------- dialoghi ----------
  const SAY = ov.querySelector('#say');
  function say(name, lines, opt, por, vis) { dlg = { name, lines, i: 0, opt, por, vis, shown: 0 }; showD(); }
  function showD() { SAY.classList.remove('hidden'); ov.classList.add('talking'); SAY.classList.toggle('vis', !!dlg.vis);
    const im = ov.querySelector('#por'); if (dlg.por) { im.src = Z1ART[dlg.por]; im.style.display = ''; } else im.style.display = 'none';
    ov.querySelector('#who').textContent = dlg.name; const tx = ov.querySelector('#tx'); const full = dlg.lines[dlg.i]; dlg.shown = 0;
    const O = ov.querySelector('#opt'); O.innerHTML = ''; ov.querySelector('#more').style.display = 'none';
    clearInterval(dlg.tm); dlg.tm = setInterval(() => { dlg.shown += 2; tx.textContent = full.slice(0, dlg.shown); if (dlg.shown >= full.length) { clearInterval(dlg.tm); endLine(); } }, 16); }
  function endLine() { const O = ov.querySelector('#opt'); const lastL = dlg.i === dlg.lines.length - 1; ov.querySelector('#tx').textContent = dlg.lines[dlg.i];
    if (lastL && dlg.opt) dlg.opt.forEach(([t, fn], j) => { const b = document.createElement('button'); b.textContent = t; if (j) b.className = 'sec';
      b.onclick = e => { e.stopPropagation(); closeD(); fn(); }; O.appendChild(b); });
    else ov.querySelector('#more').style.display = ''; dlg.ready = true; }
  function advance() { if (!dlg) return; if (!dlg.ready) { clearInterval(dlg.tm); dlg.shown = 1e9; endLine(); return; }
    if (dlg.i < dlg.lines.length - 1) { dlg.i++; dlg.ready = false; showD(); } else if (!dlg.opt) closeD(); }
  function closeD() { if (dlg) clearInterval(dlg.tm); dlg = null; SAY.classList.add('hidden'); ov.classList.remove('talking'); closedAt = performance.now(); }

  function act() { if (modalOn) return; if (dlg) { if (dlg.ready && dlg.opt && dlg.i === dlg.lines.length - 1) return; advance(); return; }
    if (performance.now() - closedAt < 250) return;
    const k = near(); if (!k) return;
    if (k === 'leoni') return say('Borso', ['Due leoni di marmo rosso reggono le colonne del portale.', 'Sono lì da quasi novecento anni.'], null, 'r_borso');
    if (k === 'facciata') return say('Borso', ['La facciata ha tre parti e tre punte.', 'Sotto è romanica, sopra è gotica: due epoche in un solo muro.', 'Anche un edificio è un messaggio, se sai leggerlo.'], null, 'r_borso');
    talk(k); }
  function talk(k) {
    if (k === 'maurelio') {
      if (!Zs.done) say('San Maurelio', ['La tradizione dice che fui vescovo qui, più di mille anni fa.', 'Allora questa era terra di confine, tra acque e paludi.', 'Di me restano poche tracce: un nome, qualche data, dei racconti.', 'Una traccia, da sola, non parla. Vuoi imparare a farla parlare?'], [['Sì, proviamo', () => bottega()], ['Non ancora', () => {}]], 'r_maurelio');
      else say('San Maurelio', ['Le tracce passano di mano in mano.', 'Lungo il fianco della chiesa si commercia da secoli. Vai a destra, verso la Loggia.'], null, 'r_maurelio');
    }
    if (k === 'giorgio') { if (!Zs.a1) say('San Giorgio (visione)', ['Borso guarda la lunetta sopra il portale e immagina il santo a cavallo.', '«Ogni opera ha una scheda: chi, quando, dove, che cosa.»', '«Me la compili?»'], [['Sì', () => visA1()], ['Dopo', () => {}]], 'r_giorgio', true);
      else say('San Giorgio (visione)', ['«Una scheda di dati sui dati: si chiamano metadati.»'], null, 'r_giorgio', true); }
    if (k === 'lapide') { if (!Zs.done || !Zs.a1) return say('La lapide', ['Una pietra consumata. Si leggono solo alcune lettere.'], null);
      if (!Zs.a2) say('La lapide', ['Borso immagina chi la incise, chi la lesse, chi la capì.', 'Metti in ordine i quattro piani della piramide.'], [['Proviamo', () => visA2()], ['Dopo', () => {}]], null, true);
      else say('La lapide', ['Dati, informazioni, conoscenza, saggezza.'], null, null, true); }
    if (k === 'cartello') say('Cartello', ['Costituzione, articolo 9.', '«La Repubblica tutela il paesaggio e il patrimonio storico e artistico della Nazione.»', 'Questa piazza è una traccia: la legge la protegge.'], null);
  }
  // ---------- bottega, carta e visioni (come nella v0.1) ----------
  const B2 = ov.querySelector('#box2');
  function modal() { B2.classList.remove('hidden'); modalOn = true; return ov.querySelector('#bin'); }
  function unmodal() { B2.classList.add('hidden'); modalOn = false; }
  function bottega() { const box = modal(); openBottega({ box, stato: st, onClose: unmodal, onDone: () => { Zs.done = true; card(box); } }); }
  function card(box) { box.innerHTML = `<h2>Hai una carta nuova</h2><div class="cardx"><img src="${Z1ART.r_maurelio}" width="96" height="108" style="image-rendering:pixelated;border:3px solid #2b2118;border-radius:6px" alt="San Maurelio (disegno)">
    <div><div class="name">San Maurelio</div><div class="meta">VII secolo · tradizione · attendibilità D + M</div><div class="topic"><b>Dato, informazione, conoscenza</b></div><div class="quote">«Il numero da solo tace; con un contesto parla; collegato ad altro, ragiona.»</div><div class="meta">Bronzo · primo ripasso domani</div></div></div><button id="ok">Torna in piazza</button>`;
    box.querySelector('#ok').onclick = () => { unmodal(); say('San Maurelio', ['Le tracce passano di mano in mano.', 'Lungo il fianco della chiesa si commercia da secoli. Vai a destra, verso la Loggia.', '(Sono comparse due visioni: puoi seguirle, se vuoi.)'], null, 'r_maurelio'); }; }
  function visA1() { const box = modal(); const F = [['Autore', 'Nicholaus, scultore'], ['Data', '1135'], ['Luogo', 'Portale della Cattedrale'], ['Soggetto', 'San Giorgio e il drago']];
    const vals = F.map(f => f[1]).sort(() => Math.random() - .5); let sel = null, ok = 0;
    box.innerHTML = `<h2 class="sepia">Visione · La scheda dell'opera</h2><p class="small">Tocca un campo, poi il suo valore.</p><div class="pairs"><div class="col">${F.map((f, i) => `<button class="pill fld" data-i="${i}">${f[0]}</button>`).join('')}</div><div class="col">${vals.map(v => `<button class="pill val" data-v="${esc1(v)}">${esc1(v)}</button>`).join('')}</div></div><div class="fb"></div>`;
    box.querySelectorAll('.fld').forEach(b => b.onclick = () => { box.querySelectorAll('.fld').forEach(x => x.classList.remove('sel')); b.classList.add('sel'); sel = +b.dataset.i; });
    box.querySelectorAll('.val').forEach(b => b.onclick = () => { if (sel === null) return; const f = box.querySelector(`.fld[data-i="${sel}"]`);
      if (F[sel][1] === b.dataset.v) { f.classList.add('right'); b.classList.add('right'); f.disabled = b.disabled = true; ok++; sel = null;
        if (ok === 4) { box.querySelector('.fb').innerHTML = `Scheda completa: sono <b>metadati</b>, dati che descrivono altri dati. <button id="ok">Chiudi la visione</button>`; box.querySelector('#ok').onclick = () => { Zs.a1 = true; unmodal(); }; } }
      else { b.classList.add('wrong'); setTimeout(() => b.classList.remove('wrong'), 500); } }); }
  function visA2() { const box = modal(); const L = ['Dati', 'Informazioni', 'Conoscenza', 'Saggezza']; const DD = { Dati: 'segni e numeri', Informazioni: 'dati con un contesto', Conoscenza: 'informazioni collegate', Saggezza: 'sapere come usarle bene' };
    const sh = L.slice().sort(() => Math.random() - .5); let k = 0;
    box.innerHTML = `<h2 class="sepia">Visione · La piramide</h2><p class="small">Costruisci dal basso: tocca i blocchi nell'ordine giusto.</p><div class="pyr" id="pyr"></div><div class="row wrap">${sh.map(l => `<button class="pill blk" data-l="${l}">${l}</button>`).join('')}</div><div class="fb"></div>`;
    box.querySelectorAll('.blk').forEach(b => b.onclick = () => { if (b.dataset.l === L[k]) { b.disabled = true; box.querySelector('#pyr').insertAdjacentHTML('afterbegin', `<div class="lv lv${k}">${L[k]} <span>· ${DD[L[k]]}</span></div>`); k++;
        if (k === 4) { box.querySelector('.fb').innerHTML = `È la piramide DIKW. <button id="ok">Chiudi la visione</button>`; box.querySelector('#ok').onclick = () => { Zs.a2 = true; unmodal(); }; } }
      else { b.classList.add('wrong'); setTimeout(() => b.classList.remove('wrong'), 500); } }); }

  // ---------- ingresso, comandi, uscita ----------
  function exit() { if (ended) return; ended = true; cancelAnimationFrame(raf); removeEventListener('resize', resize);
    document.removeEventListener('keydown', kd); document.removeEventListener('keyup', ku); ov.remove(); opts.onExit(Zs.done); }
  const KM = { ArrowUp: 'up', ArrowDown: 'down', ArrowLeft: 'left', ArrowRight: 'right', w: 'up', s: 'down', a: 'left', d: 'right', W: 'up', S: 'down', A: 'left', D: 'right', Shift: 'run' };
  function kd(e) { if (modalOn) return; if (KM[e.key]) { e.preventDefault(); keys[KM[e.key]] = true; } else if (e.key === ' ' || e.key === 'Enter' || e.key === 'e') { e.preventDefault(); act(); } }
  function ku(e) { if (KM[e.key]) keys[KM[e.key]] = false; }
  document.addEventListener('keydown', kd); document.addEventListener('keyup', ku);
  SAY.onclick = () => act(); ov.querySelector('#ab').onclick = e => { e.stopPropagation(); act(); };
  ov.querySelector('#zx').onclick = () => exit();
  // levetta virtuale (telefono e tablet)
  const stk = ov.querySelector('#stick'), knob = stk.querySelector('i'); let sid = null;
  const sMove = t => { const r = stk.getBoundingClientRect(); let x = (t.clientX - r.left - 60) / 50, y = (t.clientY - r.top - 60) / 50; const L = Math.hypot(x, y); if (L > 1) { x /= L; y /= L; }
    stick = { x, y }; knob.style.transform = `translate(${x * 38}px,${y * 38}px)`; };
  stk.addEventListener('pointerdown', e => { sid = e.pointerId; stk.setPointerCapture(sid); sMove(e); });
  stk.addEventListener('pointermove', e => { if (e.pointerId === sid) sMove(e); });
  const sEnd = () => { sid = null; stick = { x: 0, y: 0 }; knob.style.transform = ''; };
  stk.addEventListener('pointerup', sEnd); stk.addEventListener('pointercancel', sEnd);
  ov.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') ov.classList.add('touch'); }, { capture: true });

  const ban = ov.querySelector('#ban'); setTimeout(() => ban.classList.add('on'), 200); setTimeout(() => ban.classList.remove('on'), 2600);
  const start = () => { raf = requestAnimationFrame(loop);
    if (!Zs.parlato) { Zs.parlato = true; setTimeout(() => say('Borso', ['Ferrara. Piazza della Cattedrale.', 'Davanti al portale c\'è qualcuno.'], null, 'r_borso'), 900); } };
  const imgs = Object.values(Z.IMG); Promise.all(imgs.map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; }))).then(start);
  window.__Z1S = { P, Zs, act, near, say: (...a) => say(...a), get dlg() { return dlg; }, keys, exit };
}
