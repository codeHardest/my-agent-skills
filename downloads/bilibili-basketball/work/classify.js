const fs = require('fs');
const W = 'P:/c2-workspace/trunk/server/downloads/bilibili-basketball/work';

const raw = fs.readFileSync(W + '/favdata.json', 'utf8').replace(/^\uFEFF/, '');
const obj = JSON.parse(JSON.parse(raw));
const all = [];
for (const k of Object.keys(obj)) {
  for (const it of obj[k].items) all.push({ fav: obj[k].title, ...it });
}

const cats = {
  '投篮': [12,14,15,18,21,24,28,37,40,45,52,54,64,72,98,137,138,143,153,154,155,156,157,158,159,160,161,164,166,168,169,170,171,172,174,175,176,177,180,185,186,191,193,195,196,199,200,208,218,219,220,222,226,227,228,231,232,233,237,242,243,244,249,251,255,261,275,277,289,292,294,295,296,298,304,305,306,316],
  '脚步': [5,9,10,23,35,36,39,46,48,51,83,94,95,120,122,136,145,147,183,194,198,202,205,212,214,235,253,264,271,299],
  '三威胁': [32,43,287,311],
  '胯下': [2,6,7,8,22,146,173,179,203,206,221,229,246,263,285],
  '弱侧手': [77,90,91,239],
  '节奏感': [30,50,53,150,247,268,278,297],
  '控球': [0,1,4,11,13,19,20,25,29,34,62,63,67,70,80,88,89,100,101,139,142,144,148,151,152,163,178,181,182,184,188,201,207,209,216,217,225,230,236,238,241,245,248,250,252,257,258,259,265,266,267,269,270,273,274,276,279,282,283,286,293],
  '基本功': [16,17,31,49,55,66,85,86,102,128,129,140,141,149,165,189,192,197,204,210,211,213,215,223,224,234,240,262,272]
};

const used = new Set();
const included = [];
for (const [cat, idxs] of Object.entries(cats)) {
  for (const i of idxs) {
    if (used.has(i)) { console.error('DUP', i); continue; }
    used.add(i);
    const v = all[i];
    included.push({ cat, idx: i, bv: v.bv, title: v.title, up: v.up, dur: v.dur, fav: v.fav });
  }
}
const excluded = all.map((v, i) => ({ idx: i, ...v })).filter(v => !used.has(v.idx));
fs.writeFileSync(W + '/included.json', JSON.stringify(included, null, 1), 'utf8');
fs.writeFileSync(W + '/excluded.json', JSON.stringify(excluded, null, 1), 'utf8');
const counts = {};
for (const x of included) counts[x.cat] = (counts[x.cat] || 0) + 1;
console.log('included', included.length, 'excluded', excluded.length, JSON.stringify(counts));
