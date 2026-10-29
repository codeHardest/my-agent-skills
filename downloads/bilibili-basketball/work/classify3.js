const fs = require('fs');
const W = 'P:/AI/my-agent-skills/downloads/bilibili-basketball/work';
const uniq = JSON.parse(fs.readFileSync(W + '/unique.json', 'utf8'));
const byBv = new Map(uniq.map(v => [v.bv, v]));

const inc = JSON.parse(fs.readFileSync(W + '/included.json', 'utf8'));

// 现有分类（按 BV）
const cats = {};
for (const x of inc) (cats[x.cat] = cats[x.cat] || []).push(x.bv);

// 1) 补充遗漏的三威胁视频
cats['三威胁'].push('BV1Vg4y1574J');

// 2) 从基本功移出到对抗
const moveTo = (from, to, bv) => {
  cats[from] = cats[from].filter(b => b !== bv);
  cats[to] = cats[to] || [];
  if (!cats[to].includes(bv)) cats[to].push(bv);
};
moveTo('基本功', '对抗', 'BV16N4y127qe');
moveTo('基本功', '对抗', 'BV18s4y1R7Tx');
moveTo('基本功', '对抗', 'BV1CDpqzpECv');

// 3) 新分类
cats['对抗'] = [
  'BV1wN4y1w7yi', // 打球为什么一定要会对抗
  'BV1CDpqzpECv', // 篮球对抗必修课 第6集
  'BV16N4y127qe', // 五种对抗上篮
  'BV18s4y1R7Tx'  // 小打大：轻松对抗大个子
];

cats['防守'] = [
  'BV1WP411H7Sy'  // 西班牙一盯四联防守分析
];

cats['战术&经验'] = [
  'BV11R4y1D7Jn', // 3条重要球场经验
  'BV1er4y1N7UY', // 1打1根据防守站位选择进攻(2)
  'BV1YK4y1S7md', // 一对一根据防守站位选择进攻(1)
  'BV12p4y1n799', // 破解收缩防守及贴防
  'BV1q5411X7wQ', // 挡拆后单手传球
  'BV1EP4y1m7uw', // 幽灵掩护
  'BV1at4y1s7z8', // 不会打挡拆
  'BV1ny4y1z7CA', // 阅读防守：眼睛该往哪看
  'BV1r5411X7iV', // 如何进攻2-3联防
  'BV1BW4y1b7X5', // 5种基础战术
  'BV1fY411X7Gb', // 打全场比赛效率翻倍
  'BV1DT411T7si', // 专业救治半场龙全场虫
  'BV1EHifY8EBH', // 走步/携带球违例
  'BV1z1ttzYEZt'  // 青少年引导（青训经验）
];

const ORDER = ['投篮', '控球', '弱侧手', '三威胁', '胯下', '节奏感', '脚步', '基本功', '对抗', '防守', '战术&经验'];

const used = new Set();
const out = [];
for (const cat of ORDER) {
  for (const bv of cats[cat] || []) {
    if (used.has(bv)) { console.error('DUP', bv); continue; }
    used.add(bv);
    const v = byBv.get(bv);
    if (!v) { console.error('MISSING META', bv); continue; }
    out.push({ cat, bv: v.bv, title: v.title, up: v.up, dur: v.dur, fav: v.favs ? v.favs[0] : v.fav });
  }
}
const exc = uniq.filter(v => !used.has(v.bv)).map(v => ({ bv: v.bv, title: v.title, up: v.up, dur: v.dur, fav: v.favs ? v.favs[0] : v.fav }));

fs.writeFileSync(W + '/included3.json', JSON.stringify(out, null, 1), 'utf8');
fs.writeFileSync(W + '/excluded3.json', JSON.stringify(exc, null, 1), 'utf8');
const counts = {};
for (const x of out) counts[x.cat] = (counts[x.cat] || 0) + 1;
console.log('included', out.length, 'excluded', exc.length);
console.log(JSON.stringify(counts, null, 1));
console.log('\nnewly added:', out.filter(x => !inc.some(i => i.bv === x.bv)).map(x => x.cat + ':' + x.bv + ' ' + x.title.slice(0, 30)).join('\n'));
