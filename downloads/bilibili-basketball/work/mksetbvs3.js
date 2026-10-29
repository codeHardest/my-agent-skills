const fs = require('fs');
const W = 'P:/AI/my-agent-skills/downloads/bilibili-basketball/work/';
const inc3 = JSON.parse(fs.readFileSync(W + 'included3.json', 'utf8'));
const inc1 = JSON.parse(fs.readFileSync(W + 'included.json', 'utf8'));
const old = new Set(inc1.map(x => x.bv));
const nw = inc3.filter(x => !old.has(x.bv));
fs.writeFileSync(W + 'setbvs3.js',
  'window.__bvs=' + JSON.stringify(nw.map(x => x.bv)) + ';window.__cursor2=0;window.__subs2={};"ok"', 'utf8');
console.log('new', nw.length, nw.map(x => x.bv).join(','));
