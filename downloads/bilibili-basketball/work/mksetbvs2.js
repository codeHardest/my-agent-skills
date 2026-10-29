const fs = require('fs');
const W = 'P:/c2-workspace/trunk/server/downloads/bilibili-basketball/work';
const inc = JSON.parse(fs.readFileSync(W + '/included.json', 'utf8'));
const bvs = inc.map(x => x.bv);
fs.writeFileSync(W + '/setbvs2.js',
  'window.__bvs=' + JSON.stringify(bvs) + ';window.__cursor2=0;window.__subs2={};"ok"', 'utf8');
console.log('bvs', bvs.length);
