const fs = require('fs');
const W = 'P:/AI/my-agent-skills/downloads/bilibili-basketball/work';
const raw = fs.readFileSync(W + '/favdata.json', 'utf8').replace(/^\uFEFF/, '');
const obj = JSON.parse(JSON.parse(raw));
const all = [];
for (const k of Object.keys(obj)) for (const it of obj[k].items) all.push({ fav: obj[k].title, ...it });

const byBv = new Map();
for (const it of all) {
  if (!byBv.has(it.bv)) byBv.set(it.bv, { ...it, favs: [it.fav] });
  else byBv.get(it.bv).favs.push(it.fav);
}
const dups = [...byBv.values()].filter(v => v.favs.length > 1);
console.log('entries', all.length, 'unique', byBv.size, 'dups', dups.length);
console.log(dups.slice(0, 10).map(d => d.bv + ':' + d.favs.join('+')).join('\n'));

const kws = ['防守', '防', '断', '帽', '抢', '卡位', '篮板', '对抗', '战术', '挡拆', '联防', '包夹', '换防', '脚步', '阅读'];
const uniq = [...byBv.values()];
console.log('\n--- keyword matches ---');
for (const kw of kws) {
  const m = uniq.filter(v => v.title.includes(kw));
  console.log(`\n[${kw}] ${m.length}`);
  for (const v of m) console.log('  ' + v.bv + ' | ' + v.title.slice(0, 50) + ' | ' + v.up);
}
fs.writeFileSync(W + '/unique.json', JSON.stringify(uniq, null, 1), 'utf8');
