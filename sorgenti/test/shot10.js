const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:800}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+require('path').resolve(__dirname,'../../prototipo/index.html'));
await p.waitForTimeout(400); await p.screenshot({path:'c1.png'});
await p.waitForTimeout(2200); await p.screenshot({path:'c2.png'});
await p.evaluate(()=>{st.done=[0,1,2,3,4];st.cur=5;needCache=true;render();flyTo(S[3].x,S[3].y,0.5)}); await p.waitForTimeout(2200); await p.screenshot({path:'c3.png'});
const t0=Date.now();await p.evaluate(()=>{for(let i=0;i<30;i++)draw()});console.log('30 draws ms',Date.now()-t0);
console.log(errs.join('\n')||'no errors'); await b.close()})();
