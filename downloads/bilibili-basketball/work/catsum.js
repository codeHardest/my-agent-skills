const fs = require('fs');
const path = require('path');

const BASE = 'P:/AI/my-agent-skills/downloads/bilibili-basketball';
const key = process.env.OPENROUTER_API_KEY;
const MODEL = 'deepseek/deepseek-chat-v3.1';

const inc = JSON.parse(fs.readFileSync(BASE + '/work/included.json', 'utf8'));
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

function summariesOf(cat) {
  const out = [];
  for (const x of inc.filter(v => v.cat === cat)) {
    const p = path.join(BASE, 'raw', x.bv, 'summary.md');
    if (!fs.existsSync(p)) continue;
    const s = fs.readFileSync(p, 'utf8').trim();
    if (!s || s.startsWith('MISMATCH')) continue;
    out.push({ ...x, summary: s });
  }
  return out;
}

function buildPrompt(cat, list) {
  const body = list.map((x, i) => `【${i + 1}】${x.title}（UP：${x.up}）\n${x.summary}`).join('\n\n');
  return `你是篮球训练知识库编辑。下面是 ${list.length} 个「${cat}」类篮球教学视频的独立总结，内容大量重复。

请把它们合并成一份**去重后**的知识总结，要求：
1. 相同或高度相似的观点只保留一次，合并表述；只保留真正有价值、可执行的内容。
2. 不要编造字幕里没有的内容；不要罗列视频标题。
3. 结构如下（Markdown，不要用一级标题）：
## 一、核心原理
（3-6 条，说明这一类技术的底层逻辑）
## 二、动作要领
（按主题分小节，每个小节 3-6 条要点；用「**主题名**」作为加粗小标题）
## 三、常见错误与纠正
（每条格式：错误表现 → 原因 → 纠正方法，6-12 条）
## 四、训练方法与进阶
（可执行的练习，注明组数/次数或时长，若有）
## 五、关键心法
（3-5 条短句）

要求：总字数 1200-2000 字；去重彻底；语言精炼、可直接用于训练。

各视频总结如下：

${body}`;
}

async function callApi(cat, list, attempt = 0) {
  try {
    const r = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: MODEL,
        messages: [{ role: 'user', content: buildPrompt(cat, list) }],
        temperature: 0.2,
        max_tokens: 4000
      })
    });
    if (!r.ok) throw new Error('HTTP ' + r.status + ' ' + (await r.text()).slice(0, 200));
    const j = await r.json();
    const out = j.choices && j.choices[0] && j.choices[0].message && j.choices[0].message.content;
    if (!out) throw new Error('empty');
    return out.trim();
  } catch (e) {
    if (attempt < 3) {
      await new Promise(r => setTimeout(r, 3000 * (attempt + 1)));
      return callApi(cat, list, attempt + 1);
    }
    throw e;
  }
}

const FILE = { '投篮': '01-投篮.md', '控球': '02-控球.md', '弱侧手': '03-弱侧手.md', '三威胁': '04-三威胁.md', '胯下': '05-胯下.md', '节奏感': '06-节奏感.md', '脚步': '07-脚步.md', '基本功': '08-基本功.md', '阅读防守': '09-阅读防守.md', '战术经验': '10-战术经验.md' };

(async () => {
  const outDir = path.join(BASE, '分类总结');
  fs.mkdirSync(outDir, { recursive: true });
  for (const cat of ORDER) {
    const list = summariesOf(cat);
    if (!list.length) { console.log(cat, 'no data'); continue; }
    const res = await callApi(cat, list);
    const header = `# ${cat} · 分类总结\n\n> 基于 ${list.length} 个视频的字幕总结去重合并 ｜ ${DESC[cat]}\n\n`;
    fs.writeFileSync(path.join(outDir, FILE[cat]), header + res + '\n', 'utf8');
    console.log(cat, 'videos', list.length, 'chars', res.length);
  }
})();
