// ===== Tappa 1-1 · San Maurelio · Dato, informazione, conoscenza =====
// Motore a pool: per ogni gradino servono NEED risposte giuste; la pool ha 5×NEED esercizi equivalenti (20), estratti a caso senza ripetizioni.
const NEED=4, POOL=NEED*5;
function rng(seed){return function(){seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
const cap=s=>s.charAt(0).toUpperCase()+s.slice(1);
function shuffle(a,r){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
const esc1=t=>String(t).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

// --- banche dati (fatti verificati; contesti quotidiani) ---
const FATTI=[["la Cattedrale",1135,"fu consacrata"],["il Castello Estense",1385,"fu iniziato"],["l'Università",1391,"fu fondata"],["Borso d'Este",1471,"divenne duca di Ferrara"],["l'Addizione Erculea",1492,"fu avviata"],["Copernico",1503,"si laureò a Ferrara"],["l'Orlando furioso",1516,"uscì in prima edizione"],["la Devoluzione",1598,"portò Ferrara al Papa"],["Ferrara",1995,"diventò Patrimonio UNESCO"]];
const TIPI={anno:"un anno",orario:"un orario",temp:"una temperatura",cap:"un codice postale",km:"una distanza",pref:"un prefisso telefonico",conto:"un numero di cose"};
const DATI=[
 {v:"1135",t:"anno",s:["La Cattedrale","fu consacrata","nel 1135"]},
 {v:"1492",t:"anno",s:["L'Addizione Erculea","fu avviata","nel 1492"]},
 {v:"15:40",t:"orario",s:["Il treno per Bologna","parte","alle 15:40"]},
 {v:"08:05",t:"orario",s:["La prima ora di lezione","comincia","alle 08:05"]},
 {v:"37,8 °C",t:"temp",s:["Il termometro di Marco","segna","37,8 °C"]},
 {v:"21 °C",t:"temp",s:["Nell'aula di informatica","ci sono","21 °C"]},
 {v:"44121",t:"cap",s:["Il codice postale","del centro di Ferrara","è 44121"]},
 {v:"9 km",t:"km",s:["Le mura di Ferrara","sono lunghe","più di 9 km"]},
 {v:"0532",t:"pref",s:["Il prefisso telefonico","di Ferrara","è 0532"]},
 {v:"12",t:"conto",s:["Nel Salone dei Mesi","sono dipinti","12 mesi"]}];
const ICONE={anno:"calendario",orario:"orologio",temp:"termometro",cap:"busta",km:"righello",pref:"telefono",conto:"pallottoliere"};
const VF=[["Un numero da solo è già un'informazione.",0],["Lo stesso dato può voler dire cose diverse.",1],["Un'informazione può anche essere falsa.",1],["Collegando informazioni nasce conoscenza.",1],["Più una frase è lunga, più è conoscenza.",0],["«44121», senza altro, è un dato.",1],["«°C» aggiunge un contesto a un numero.",1],["Se una data è incisa nella pietra, è per forza vera.",0],["Due persone possono leggere lo stesso dato in modi diversi.",1],["Informazione e conoscenza sono la stessa cosa.",0],["Il computer conserva dati: il significato lo diamo noi.",1],["Un orario senza sapere di che cosa, è un dato.",1]];

function info(d){return d.s.join(" ")+"."}
function tripla(r){let i=Math.floor(r()*FATTI.length),j;do{j=Math.floor(r()*FATTI.length)}while(j===i);let a=FATTI[i],b=FATTI[j];if(a[1]>b[1])[a,b]=[b,a];
 return {a,b,dato:String(a[1]),info:`${cap(a[0])} ${a[2]} nel ${a[1]}.`,con:`${cap(a[0])} ${a[2]} nel ${a[1]}, ${b[0]} ${b[2]} nel ${b[1]}: quindi il primo fatto viene ${b[1]-a[1]} anni prima.`}}

// --- generatori di esercizi (ogni tipo è un meccanismo diverso) ---
const GEN={
 smista(r){const T=tripla(r);const pick=["dato","info","con"][Math.floor(r()*3)];const txt={dato:T.dato,info:T.info,con:T.con}[pick];
   return {m:"smista",q:"In quale cesto va?",card:txt,ok:{dato:"dato",info:"informazione",con:"conoscenza"}[pick],steps:1}},
 vf(r){const x=VF[Math.floor(r()*VF.length)];return {m:"vf",q:"Vero o falso?",s:x[0],ok:x[1]?"vero":"falso",steps:1}},
 intruso(r){const ds=shuffle(DATI,r);const odd=r()<.5;const cards=odd?[ds[0].v,ds[1].v,ds[2].v,info(ds[3])]:[info(ds[0]),info(ds[1]),info(ds[2]),ds[3].v];
   return {m:"intruso",q:"Tocca l'intruso",cards:shuffle(cards.map((c,i)=>({c,ok:i===3})),r),steps:1}},
 vesti(r){const ds=shuffle(DATI,r);const d=ds[0];const others=shuffle(Object.keys(TIPI).filter(t=>t!==d.t),r).slice(0,3);
   return {m:"vesti",q:"Che cosa può essere?",v:d.v,opts:shuffle([{t:TIPI[d.t],ok:1},...others.map(t=>({t:TIPI[t],ok:0}))],r),steps:1}},
 icona(r){const d=DATI[Math.floor(r()*DATI.length)];const others=shuffle(Object.keys(ICONE).filter(t=>t!==d.t),r).slice(0,3);
   return {m:"icona",q:"Quale strumento dà senso a questo dato?",v:d.v,opts:shuffle([{k:d.t,ok:1},...others.map(t=>({k:t,ok:0}))],r),steps:1}},
 costruisci(r){const d=DATI[Math.floor(r()*DATI.length)];return {m:"costruisci",q:"Metti in ordine i pezzi",parts:d.s.slice(),tiles:shuffle(d.s.map((p,i)=>({p,i})),r),steps:1}},
 conclusione(r){const T=tripla(r);const a=T.a,b=T.b;
   return {m:"conclusione",q:"Quale conclusione è corretta?",i1:`${cap(a[0])} ${a[2]} nel ${a[1]}.`,i2:`${cap(b[0])} ${b[2]} nel ${b[1]}.`,
     opts:shuffle([{t:`${cap(a[0])} viene prima: ${b[1]-a[1]} anni prima.`,ok:1},{t:`${cap(b[0])} viene prima.`,ok:0},{t:`Le due date sono uguali.`,ok:0}],r),
     why:shuffle([{t:"Collego due informazioni e ne ricavo una nuova.",ok:1},{t:"Perché ci sono dei numeri.",ok:0},{t:"Perché la frase è lunga.",ok:0}],r),steps:2}},
 scala(r){const T=tripla(r);return {m:"scala",q:"Ordina: dal dato alla conoscenza",cards:shuffle([{c:T.dato,k:0},{c:T.info,k:1},{c:T.con,k:2}],r),steps:3}},
 tripla(r){const T=tripla(r);return {m:"tripla",q:"Dai un'etichetta a ogni traccia",cards:shuffle([{c:T.dato,k:"dato"},{c:T.info,k:"informazione"},{c:T.con,k:"conoscenza"}],r),steps:3}}
};
const GRADINI=[
 null,
 {nome:"Riconosci",tipi:["smista","vf","intruso"]},
 {nome:"Trasforma",tipi:["vesti","icona","costruisci"]},
 {nome:"Collega",tipi:["conclusione","scala","tripla"]}];
function buildPool(g,seed){const r=rng(seed*7919+g);const tipi=GRADINI[g].tipi;const out=[],seen=new Set();let k=0,tries=0;
 while(out.length<POOL&&tries<2000){tries++;const it=GEN[tipi[k%tipi.length]](r);const key=it.m+'|'+(it.card||it.s||it.v||it.i1||'')+'|'+(it.cards?it.cards.map(c=>c.c).join('/'):'')+'|'+(it.parts?it.parts.join(' '):'');if(seen.has(key)&&tries<1500)continue;seen.add(key);out.push(it);k++}
 return shuffle(out,r)}

// --- disegni SVG semplici per le icone ---
const SVG={
 calendario:'<rect x="6" y="10" width="36" height="30" rx="4" fill="#fff" stroke="currentColor" stroke-width="3"/><rect x="6" y="10" width="36" height="9" fill="currentColor"/><circle cx="16" cy="28" r="3"/><circle cx="26" cy="28" r="3"/><circle cx="34" cy="28" r="3"/>',
 orologio:'<circle cx="24" cy="24" r="17" fill="#fff" stroke="currentColor" stroke-width="3"/><path d="M24 13v11l8 5" stroke="currentColor" stroke-width="3" fill="none"/>',
 termometro:'<rect x="20" y="6" width="8" height="26" rx="4" fill="#fff" stroke="currentColor" stroke-width="3"/><circle cx="24" cy="36" r="7" fill="currentColor"/>',
 busta:'<rect x="6" y="12" width="36" height="24" rx="3" fill="#fff" stroke="currentColor" stroke-width="3"/><path d="M6 14l18 13 18-13" stroke="currentColor" stroke-width="3" fill="none"/>',
 righello:'<rect x="4" y="18" width="40" height="12" rx="2" fill="#fff" stroke="currentColor" stroke-width="3"/><path d="M11 18v6M18 18v4M25 18v6M32 18v4M39 18v6" stroke="currentColor" stroke-width="2"/>',
 telefono:'<rect x="15" y="5" width="18" height="38" rx="4" fill="#fff" stroke="currentColor" stroke-width="3"/><circle cx="24" cy="37" r="2.5"/>',
 pallottoliere:'<path d="M8 14h32M8 24h32M8 34h32" stroke="currentColor" stroke-width="2"/><circle cx="14" cy="14" r="4"/><circle cx="22" cy="14" r="4"/><circle cx="18" cy="24" r="4"/><circle cx="30" cy="34" r="4"/><circle cx="38" cy="34" r="4"/>'};
const ico=k=>`<svg viewBox="0 0 48 48" width="56" height="56" aria-label="${k}" fill="currentColor">${SVG[k]}</svg>`;

// --- motore della bottega ---
function openBottega(ctx){ // ctx: {box, onDone, stato}
 const st=ctx.stato;const box=ctx.box;
 if(!st.pools){st.pools={};st.ok={1:0,2:0,3:0};st.err=0;st.hist=[];st.g=0;st.seed=st.seed||((Date.now()%97003)+11)}
 const head=()=>`<div class="ovh"><span>Cattedrale · <b>San Maurelio</b></span><span class="dots">${[1,2,3].map(g=>`<i class="${st.g>g?'full':st.g===g?'cur':''}"></i>`).join('')}</span><button class="sec x" id="x">Chiudi</button></div>`;
 const bindX=()=>{box.querySelector('#x').onclick=ctx.onClose};
 function g0(step=0){const T=tripla(rng(st.seed));
  const scr=[
   ["Guarda questo numero.",`<div class="stone">${T.dato}</div>`],
   ["Con un contesto, il numero parla.",`<div class="stone small">${T.dato}</div><div class="arrow">↓</div><div class="tag c2">${esc1(T.info)}</div>`],
   ["Collegando due informazioni, capisci qualcosa di nuovo.",`<div class="tag c3">${esc1(T.con)}</div>`],
   ["Dato → informazione → conoscenza.",`<div class="trio"><span class="b1">dato</span><span class="b2">informazione</span><span class="b3">conoscenza</span></div>`]];
  const [t,v]=scr[step];box.innerHTML=head()+`<h2>${t}</h2><div class="stage">${v}</div><button id="nx">${step<3?'Avanti':'Proviamo'}</button>`;bindX();
  box.querySelector('#nx').onclick=()=>{if(step<3)g0(step+1);else{st.g=1;next()}}}
 function next(){if(st.g>3){ctx.onDone();return}
  if(!st.pools[st.g]||!st.pools[st.g].length)st.pools[st.g]=buildPool(st.g,st.seed+st.hist.length);
  const E=st.pools[st.g].pop();E.t0=performance.now();show(E)}
 function finish(E,right,steps){const dt=(performance.now()-E.t0)/1000;const C=steps.length?steps.filter(x=>x).length/steps.length:(right?1:0);
  const good=right&&(st.g<3||C>=0.7);st.hist.push({g:st.g,m:E.m,E:right?1:0,C:+C.toFixed(2),t:+dt.toFixed(1)});
  let msg;if(good){st.ok[st.g]++;st.err=0;msg=["Sì!","Giusto!","Esatto!","Ottimo!"][st.ok[st.g]%4]}else{st.err++;msg=right?"Risultato giusto, passaggi incerti.":"Non ancora."}
  let back=false;if(!good&&st.err>=2){st.err=0;if(st.g>1){st.g--;back=true}pausa(back);return}
  const done=st.ok[st.g]>=NEED;const fb=box.querySelector('.fb');
  fb.className='fb '+(good?'yes':'no');fb.innerHTML=`${msg}${back?' Torniamo un gradino indietro.':''} <span class="cnt">${Math.min(st.ok[st.g],NEED)}/${NEED}</span> <button id="go">${done?'Gradino superato →':'Avanti'}</button>`;
  box.querySelectorAll('button.o').forEach(b=>b.disabled=true);
  box.querySelector('#go').onclick=()=>{if(done){st.g++;st.err=0;if(st.g<=3)levelUp();else ctx.onDone()}else next()}}
 function pausa(back){box.innerHTML=head()+`<h2>Fermati un momento.</h2><div class="stage"><div class="breath"></div><p class="small">Inspira mentre il cerchio cresce, espira mentre si stringe.<br>Che cosa provi adesso? Puoi sentirlo, e poi scegliere come ripartire.</p></div><button id="go" disabled>Riparto</button>`;bindX();
  setTimeout(()=>{const g=box.querySelector('#go');if(g){g.disabled=false;g.onclick=()=>{back?levelUp():next()}}},4000)}
 function levelUp(){box.innerHTML=head()+`<h2>Gradino ${st.g}: ${GRADINI[st.g].nome}</h2><div class="stage"><div class="big">${['','🔍','🔧','🔗'][st.g]}</div></div><button id="go">Via</button>`;bindX();box.querySelector('#go').onclick=next}
 function show(E){window.__E=E;let h=head()+`<h2 class="q m-${E.m}">${E.q}</h2><div class="stage m-${E.m}">`;
  if(E.m==="smista")h+=`<div class="tag c0">${esc1(E.card)}</div><div class="baskets">${["dato","informazione","conoscenza"].map((k,i)=>`<button class="o basket b${i+1}" data-v="${k}">${k}</button>`).join('')}</div>`;
  if(E.m==="vf")h+=`<div class="bubble">${esc1(E.s)}</div><div class="row"><button class="o vf vt" data-v="vero">Vero</button><button class="o vf vfx" data-v="falso">Falso</button></div>`;
  if(E.m==="intruso")h+=`<div class="grid4">${E.cards.map((c,i)=>`<button class="o card4" data-v="${i}">${esc1(c.c)}</button>`).join('')}</div>`;
  if(E.m==="vesti")h+=`<div class="stone">${esc1(E.v)}</div><div class="row wrap">${E.opts.map((o,i)=>`<button class="o pill" data-v="${i}">${o.t}</button>`).join('')}</div>`;
  if(E.m==="icona")h+=`<div class="stone">${esc1(E.v)}</div><div class="row">${E.opts.map((o,i)=>`<button class="o icon" data-v="${i}">${ico(ICONE[o.k])}</button>`).join('')}</div>`;
  if(E.m==="costruisci")h+=`<div class="slots" id="slots"></div><div class="row wrap" id="tiles">${E.tiles.map((t,i)=>`<button class="o tile2" data-v="${i}">${esc1(t.p)}</button>`).join('')}</div>`;
  if(E.m==="conclusione")h+=`<div class="tag c2">${esc1(E.i1)}</div><div class="tag c2">${esc1(E.i2)}</div><div class="col" id="p1">${E.opts.map((o,i)=>`<button class="o pill wide" data-v="${i}">${esc1(o.t)}</button>`).join('')}</div><div class="col hidden" id="p2"><p class="small">Perché è conoscenza?</p>${E.why.map((o,i)=>`<button class="o pill wide" data-w="${i}">${esc1(o.t)}</button>`).join('')}</div>`;
  if(E.m==="scala")h+=`<div class="ladder" id="lad"></div><div class="col" id="src">${E.cards.map((c,i)=>`<button class="o pill wide" data-v="${i}">${esc1(c.c)}</button>`).join('')}</div>`;
  if(E.m==="tripla")h+=E.cards.map((c,i)=>`<div class="tag c0">${esc1(c.c)}<div class="row">${["dato","informazione","conoscenza"].map((k,j)=>`<button class="o mini b${j+1}" data-r="${i}" data-v="${k}">${k}</button>`).join('')}</div></div>`).join('')+`<button id="chk">Verifica</button>`;
  h+=`</div><div class="fb"></div>`;box.innerHTML=h;bindX();
  const B=sel=>box.querySelectorAll(sel);
  const mark=(b,ok)=>b.classList.add(ok?'right':'wrong');
  if(E.m==="smista"||E.m==="vf")B('button.o').forEach(b=>b.onclick=()=>{const ok=b.dataset.v===E.ok;mark(b,ok);finish(E,ok,[])});
  if(E.m==="intruso")B('button.o').forEach(b=>b.onclick=()=>{const ok=E.cards[+b.dataset.v].ok;mark(b,ok);finish(E,ok,[])});
  if(E.m==="vesti"||E.m==="icona")B('button.o').forEach(b=>b.onclick=()=>{const ok=!!E.opts[+b.dataset.v].ok;mark(b,ok);finish(E,ok,[])});
  if(E.m==="costruisci"){const seq=[];B('#tiles button').forEach(b=>b.onclick=()=>{b.disabled=true;seq.push(E.tiles[+b.dataset.v].i);box.querySelector('#slots').innerHTML+=`<span class="slot">${esc1(E.tiles[+b.dataset.v].p)}</span>`;
    if(seq.length===3){const ok=seq.every((v,k)=>v===k);finish(E,ok,[])}})}
  if(E.m==="conclusione"){let s1=null;B('#p1 button').forEach(b=>b.onclick=()=>{s1=!!E.opts[+b.dataset.v].ok;mark(b,s1);B('#p1 button').forEach(x=>x.disabled=true);box.querySelector('#p2').classList.remove('hidden')});
    B('#p2 button').forEach(b=>b.onclick=()=>{const s2=!!E.why[+b.dataset.w].ok;mark(b,s2);finish(E,s1,[s1,s2])})}
  if(E.m==="scala"){const seq=[];B('#src button').forEach(b=>b.onclick=()=>{b.disabled=true;const c=E.cards[+b.dataset.v];seq.push(c.k);box.querySelector('#lad').innerHTML+=`<div class="rung r${seq.length}">${esc1(c.c)}</div>`;
    if(seq.length===3){const steps=seq.map((k,i)=>k===i);finish(E,steps.every(x=>x),steps)}})}
  if(E.m==="tripla"){const pick={};B('[data-r]').forEach(b=>b.onclick=()=>{B(`[data-r="${b.dataset.r}"]`).forEach(x=>x.classList.remove('sel'));b.classList.add('sel');pick[b.dataset.r]=b.dataset.v});
    box.querySelector('#chk').onclick=()=>{if(Object.keys(pick).length<3)return;const steps=E.cards.map((c,i)=>pick[i]===c.k);
      E.cards.forEach((c,i)=>B(`[data-r="${i}"]`).forEach(x=>{if(x.dataset.v===c.k)x.classList.add('right');else if(x.classList.contains('sel'))x.classList.add('wrong')}));
      box.querySelector('#chk').disabled=true;finish(E,steps.every(x=>x),steps)}}
 }
 if(st.g===0)g0();else if(st.g>3)ctx.onDone();else next();
}
