const { chromium, devices } = require('playwright');
(async()=>{const b=await chromium.launch();const c=await b.newContext({...devices['iPhone 13']});const p=await c.newPage();
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+require('path').resolve(__dirname,'../../prototipo/index.html'));await p.waitForTimeout(2500);await p.screenshot({path:'m1.png'});
await p.evaluate(()=>document.getElementById('bott').click()); await p.waitForTimeout(2500); await p.screenshot({path:'m2.png'});
console.log(errs.join('\n')||'no errors'); await b.close()})();
