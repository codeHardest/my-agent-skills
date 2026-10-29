const fs = require('fs');
const W = 'P:/AI/my-agent-skills/downloads/bilibili-basketball/work/';
const inc3 = JSON.parse(fs.readFileSync(W + 'included3.json', 'utf8'));
const need = inc3.filter(x => ['对抗', '防守', '战术&经验'].includes(x.cat)).map(x => x.bv);
fs.writeFileSync(W + 'setbvs4.js',
  'window.__bvs=' + JSON.stringify(need) + ';"ok"', 'utf8');
console.log('need', need.length);
