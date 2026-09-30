const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:800}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+require('path').resolve(__dirname,'../../prototipo/index.html'));
await p.click('#bott'); await p.waitForTimeout(2200);
const key=async(k,n=1)=>{for(let i=0;i<n;i++){await p.keyboard.press(k);await p.waitForTimeout(40)}};
const clr=async()=>{for(let i=0;i<20;i++){if(!(await p.evaluate(()=>!!__Z1S.dlg)))break;await p.keyboard.press('Space');await p.waitForTimeout(80);}};
const walkTo=async(u,v)=>{for(let i=0;i<400;i++){await clr();const P=await p.evaluate(()=>({u:__Z1S.P.u,v:__Z1S.P.v}));const du=u-P.u,dv=v-P.v;if(Math.hypot(du,dv)<.35)break;
 const k=Math.abs(du)>Math.abs(dv)?(du>0?'ArrowRight':'ArrowLeft'):(dv>0?'ArrowDown':'ArrowUp');await p.keyboard.down(k);await p.waitForTimeout(60);await p.keyboard.up(k);}
 for(const k of ['ArrowRight','ArrowLeft','ArrowUp','ArrowDown'])await p.keyboard.up(k);};
await key('Space',3);
await walkTo(-3.4,4.2); await p.waitForTimeout(300); console.log('near',await p.evaluate(()=>[__Z1S.near(),__Z1S.P.u,__Z1S.P.v,!!__Z1S.dlg]));
await key('Space',1);await p.waitForTimeout(300);await key('Space',6); await p.waitForTimeout(800); await p.screenshot({path:'w1.png'});
await p.click('text=Sì, proviamo'); for(let i=0;i<4;i++) await p.click('#nx');
for(let k=0;k<80;k++){
  if(await p.$('text=Hai una carta nuova')) break;
  if(await p.$('.fb.yes, .fb.no')){ await p.click('#go'); continue; }
  if(await p.$('h2 >> text=Gradino')){ await p.click('#go'); continue; }
  const E=await p.evaluate(()=>window.__E);
  if(E.m==='smista'||E.m==='vf') await p.click(`button.o[data-v="${E.ok}"]`);
  else if(E.m==='intruso') await p.click(`button.o[data-v="${E.cards.findIndex(c=>c.ok)}"]`);
  else if(E.m==='vesti'||E.m==='icona') await p.click(`button.o[data-v="${E.opts.findIndex(o=>o.ok)}"]`);
  else if(E.m==='costruisci'){for(let i=0;i<3;i++){const idx=E.tiles.findIndex(t=>t.i===i); await p.click(`#tiles button[data-v="${idx}"]`);}}
  else if(E.m==='conclusione'){await p.click(`#p1 button[data-v="${E.opts.findIndex(o=>o.ok)}"]`);await p.click(`#p2 button[data-w="${E.why.findIndex(o=>o.ok)}"]`);}
  else if(E.m==='scala'){for(let i=0;i<3;i++){await p.click(`#src button[data-v="${E.cards.findIndex(c=>c.k===i)}"]`);}}
  else if(E.m==='tripla'){for(let i=0;i<3;i++) await p.click(`[data-r="${i}"][data-v="${E.cards[i].k}"]`); await p.click('#chk');}
}
await p.screenshot({path:'w2.png'}); await p.click('#ok'); await p.waitForTimeout(300); await key('Space',8);
await walkTo(3.6,4.4); await key('Space',1); await p.waitForTimeout(300); await key('Space',5); await p.waitForTimeout(600); await p.screenshot({path:'w3.png'});
await p.click('text=Sì');
const F={"Autore":"Nicholaus, scultore","Data":"1135","Luogo":"Portale della Cattedrale","Soggetto":"San Giorgio e il drago"};
for(const [f,v] of Object.entries(F)){await p.click(`.fld >> text=${f}`); await p.click(`.val[data-v="${v}"]`);}
await p.click('#ok');
await walkTo(-13,3.2); await key('Space',1); await p.waitForTimeout(200); await key('Space',4); await p.waitForTimeout(400); await p.click('text=Proviamo');
for(const l of ["Dati","Informazioni","Conoscenza","Saggezza"]) await p.click(`.blk[data-l="${l}"]`);
await p.click('#ok'); await p.waitForTimeout(300);
await walkTo(20,6); await p.screenshot({path:'w4.png'});
await p.keyboard.down('ArrowRight'); await p.waitForTimeout(2500); await p.keyboard.up('ArrowRight');
console.log('zona chiusa:', !(await p.$('.z1')), 'tappa1 fatta:', await p.evaluate(()=>st.done));
await p.screenshot({path:'w5.png'});
console.log(errs.join('\n')||'no errors'); await b.close()})();
