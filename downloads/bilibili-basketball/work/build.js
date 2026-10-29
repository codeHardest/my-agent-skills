const fs = require('fs');
const path = require('path');

const BASE = 'P:/c2-workspace/trunk/server/downloads/bilibili-basketball';
const inc = JSON.parse(fs.readFileSync(BASE + '/work/included.json', 'utf8'));
const exc = JSON.parse(fs.readFileSync(BASE + '/work/excluded.json', 'utf8'));

const ORDER = ['投篮', '控球', '弱侧手', '三威胁', '胯下', '节奏感', '脚步', '基本功', '阅读防守', '战术经验'];
const DESC = {
  '投篮': '投篮手型、发力、射程、后撤步/后仰/急停跳投等',
  '控球': '运球基本功、变向、悬浮球、护球、控运组合',
  '弱侧手': '非惯用手（左手）专项训练',
  '三威胁': '试探步、三威胁姿势与进攻选择',
  '胯下': '胯下运球/胯下变向/胯下衔接',
  '节奏感': '运球与突破的节奏、快慢变化',
  '脚步': '转身、欧洲步、合球步、试探步、上篮步法等',
  '基本功': '综合基础训练、上篮终结、热身、体系化训练',
  '阅读防守': '观察防守站位、重心、核心和手部动作，选择进攻方式',
  '战术经验': '挡拆、掩护、联防、全场比赛经验与篮球规则'
};

const fmt = (s) => {
  s = Math.round(s || 0);
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
};

const groups = {};
for (const cat of ORDER) groups[cat] = inc.filter(x => x.cat === cat);

const hasSummary = (bv) => {
  const p = path.join(BASE, 'raw', bv, 'summary.md');
  if (!fs.existsSync(p)) return null;
  const s = fs.readFileSync(p, 'utf8').trim();
  if (s.startsWith('MISMATCH')) return null;
  return s;
};

let totalWith = 0, totalWithout = 0;
const stat = {};

for (const cat of ORDER) {
  const withS = groups[cat].filter(x => hasSummary(x.bv)).length;
  stat[cat] = { total: groups[cat].length, withS, without: groups[cat].length - withS };
  totalWith += withS;
  totalWithout += groups[cat].length - withS;
}

function videoBlock(x, idx) {
  const sum = hasSummary(x.bv);
  const lines = [];
  lines.push(`### ${idx}. [${x.title}](https://www.bilibili.com/video/${x.bv})`);
  lines.push('');
  lines.push(`- UP主：${x.up} ｜ 时长：${fmt(x.dur)} ｜ 收藏夹：${x.fav} ｜ BV：${x.bv}`);
  lines.push(`- 字幕/总结：${sum ? '✅ 已有字幕并生成总结' : '⚪ 无可用字幕，仅列目录'}`);
  if (sum) {
    lines.push('');
    lines.push(sum.split('\n').map(l => l.trim() ? '  ' + l : '').join('\n'));
  }
  lines.push('');
  return lines.join('\n');
}

// 主文档
const main = [];
main.push('# B 站篮球训练视频分类与总结');
main.push('');
main.push(`- 收藏夹来源：**体育训练**（262 个）+ **篮球专项训练**（56 个），共 ${inc.length + exc.length} 个视频`);
main.push(`- 筛选出篮球训练相关视频：**${inc.length}** 个；排除（比赛集锦/花絮/新闻/球鞋/其它运动等）：**${exc.length}** 个`);
main.push(`- 有字幕并生成总结：**${totalWith}** 个；无可用字幕（仅列目录）：**${totalWithout}** 个`);
main.push('');
main.push('> 分类规则：一个视频只归入一个分类，优先落到更具体的分类（如「胯下」优先于「控球」，「脚步」优先于「投篮」）。');
main.push('');
main.push('## 分类总览');
main.push('');
main.push('| 分类 | 数量 | 有总结 | 仅目录 | 说明 |');
main.push('| --- | --- | --- | --- | --- |');
for (const cat of ORDER) {
  main.push(`| ${cat} | ${stat[cat].total} | ${stat[cat].withS} | ${stat[cat].without} | ${DESC[cat]} |`);
}
main.push('');
main.push('---');
main.push('');

for (const cat of ORDER) {
  main.push(`## ${cat}（${groups[cat].length} 个）`);
  main.push('');
  // 目录表
  main.push('| # | 视频 | UP主 | 时长 | 字幕 |');
  main.push('| --- | --- | --- | --- | --- |');
  groups[cat].forEach((x, i) => {
    main.push(`| ${i + 1} | [${x.title.replace(/\|/g, '\\|')}](https://www.bilibili.com/video/${x.bv}) | ${x.up.replace(/\|/g, '\\|')} | ${fmt(x.dur)} | ${hasSummary(x.bv) ? '✅' : '—'} |`);
  });
  main.push('');
  groups[cat].forEach((x, i) => { main.push(videoBlock(x, i + 1)); });
  main.push('---');
  main.push('');
}

fs.writeFileSync(path.join(BASE, '篮球训练视频分类与总结.md'), main.join('\n'), 'utf8');

// 分类单独文件
const fileMap = { '投篮': '01-投篮.md', '控球': '02-控球.md', '弱侧手': '03-弱侧手.md', '三威胁': '04-三威胁.md', '胯下': '05-胯下.md', '节奏感': '06-节奏感.md', '脚步': '07-脚步.md', '基本功': '08-基本功.md', '阅读防守': '09-阅读防守.md', '战术经验': '10-战术经验.md' };
for (const cat of ORDER) {
  const out = [];
  out.push(`# ${cat}（${groups[cat].length} 个）`);
  out.push('');
  out.push(`> ${DESC[cat]}`);
  out.push('');
  groups[cat].forEach((x, i) => out.push(videoBlock(x, i + 1)));
  fs.writeFileSync(path.join(BASE, '分类', fileMap[cat]), out.join('\n'), 'utf8');
}

// 已排除清单
const ex = [];
ex.push(`# 已排除的视频（${exc.length} 个）`);
ex.push('');
ex.push('以下视频不属于篮球训练教学（比赛集锦、单挑实录、新闻、球鞋评测、其它运动、生活类等），未纳入分类。');
ex.push('');
ex.push('| # | 视频 | UP主 | 时长 | 原收藏夹 |');
ex.push('| --- | --- | --- | --- | --- |');
exc.forEach((x, i) => ex.push(`| ${i + 1} | [${x.title.replace(/\|/g, '\\|')}](https://www.bilibili.com/video/${x.bv}) | ${x.up.replace(/\|/g, '\\|')} | ${fmt(x.dur)} | ${x.fav} |`));
fs.writeFileSync(path.join(BASE, '分类', '已排除.md'), ex.join('\n'), 'utf8');

console.log('main doc written;', JSON.stringify(stat), 'withS', totalWith, 'without', totalWithout);
