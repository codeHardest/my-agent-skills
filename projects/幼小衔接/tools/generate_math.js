/**
 * generate_math.js — 数学课程（数字星球）每日生成器 + 结果合并。
 *
 * 与语文/英语链路独立：读 data/math_curriculum.json + data/progress_math.json，
 * 输出 sessions/YYYY-MM-DD-math.html；--merge 合并数学结果进 progress_math.json。
 *
 * 数学是技能训练：知识点线性推进（答对当前知识点全部题 → 次日推进），
 * 不用遗忘曲线；错题存 wrong_queue 次日优先重做；已学知识点滚动复习。
 *
 * 用法:
 *   node tools/generate_math.js                 生成今日页面（顺带合并历史结果）
 *   node tools/generate_math.js --date 2026-08-20   指定日期生成
 *   node tools/generate_math.js --merge         只合并结果，不生成页面
 */
'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DATA = path.join(ROOT, 'data');
const CURR_FILE = path.join(DATA, 'math_curriculum.json');
const PROG_FILE = path.join(DATA, 'progress_math.json');
const TPL_FILE = path.join(ROOT, 'templates', 'lesson-app.html');

function todayStr(offsetDays = 0) {
  const d = new Date();
  d.setDate(d.getDate() + offsetDays);
  return d.toISOString().slice(0, 10);
}
const args = process.argv.slice(2);
const dateIdx = args.indexOf('--date');
const today = dateIdx > -1 ? args[dateIdx + 1] : todayStr();

function shuffle(arr) { const a = [...arr]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
function rand(n) { return Math.floor(Math.random() * n); }

const CURR = JSON.parse(fs.readFileSync(CURR_FILE, 'utf8'));

/* ---------- 进度（不存在则初始化） ---------- */
let PROG = null;
function save() { fs.writeFileSync(PROG_FILE, JSON.stringify(PROG, null, 2) + '\n'); }
function loadProgress() {
  if (fs.existsSync(PROG_FILE)) { PROG = JSON.parse(fs.readFileSync(PROG_FILE, 'utf8')); return; }
  PROG = {
    schema_version: 1, subject: 'math', updated: today,
    curriculum_index: 0,
    learned: [],
    wrong_queue: [],
    stats: { start_date: today, total_questions: 0, total_correct: 0, sessions_done: 0 }
  };
  save();
}

/* ---------- 出题 ---------- */
const SHAPES = [
  { name: '圆形', emoji: '⭕' },
  { name: '三角形', emoji: '🔺' },
  { name: '正方形', emoji: '🟩' },
  { name: '长方形', emoji: '🟨' },
  { name: '五角星', emoji: '⭐' },
  { name: '心形', emoji: '❤️' },
  { name: '菱形', emoji: '🔶' }
];
const CMP_OPTS = ['>', '<', '=', '≠'];

let qNo = 0;
const qid = topic => `${topic.id}#${++qNo}`;

/* 加减法：params.max 控结果上限；carry 个位和≥10；borrow 个位不够减 */
function arithQuestion(topic) {
  const p = topic.params || {};
  const max = p.max || 10;
  let a, b, ans;
  if (topic.type === 'add') {
    do { a = rand(9) + 1; b = rand(9) + 1; } while (p.carry ? (a + b < 10) : (a + b > max));
    ans = a + b;
    return { big: `${a} + ${b}`, prompt: '等于多少？', ans };
  }
  if (p.borrow) {
    do { a = rand(8) + 11; b = rand(9) + 1; } while (a % 10 >= b);   // a ∈ 11..18，个位 < b
  } else {
    a = rand(9) + 2; b = rand(a - 1) + 1;                              // a ∈ 2..10，b ∈ 1..a-1
  }
  ans = a - b;
  return { big: `${a} - ${b}`, prompt: '等于多少？', ans };
}

function compareQuestion() {
  let a = rand(20) + 1, b = rand(20) + 1;
  while (a === b) b = rand(20) + 1;
  const ans = a > b ? CMP_OPTS[0] : CMP_OPTS[1];
  // 答案与干扰项同为符号（'<' '>' '=' '≠'），不能用数值干扰项生成器
  return { big: `${a} ⚖️ ${b}`, prompt: '比一比，填上正确的符号', ans, opts: shuffle([ans, ...CMP_OPTS.filter(o => o !== ans)]) };
}

function shapesQuestion() {
  const target = SHAPES[rand(SHAPES.length)];
  const ds = shuffle(SHAPES.filter(s => s !== target)).slice(0, 3);
  const opts = shuffle([target, ...ds]);
  return { big: target.emoji.repeat(3), prompt: '这些图形是什么形状？', opts: opts.map(s => s.name), ans: target.name };
}

function classifyQuestion() {
  const target = SHAPES[rand(SHAPES.length)];
  const other = shuffle(SHAPES.filter(s => s !== target))[0];
  const line = shuffle([target, target, target, other]);
  return { big: line.map(s => s.emoji).join('  '), prompt: '哪个图形不一样？', opts: ['第1个', '第2个', '第3个', '第4个'], ansIdx: line.indexOf(other) };
}

/* 干扰数字：正确值 ±1~3，保证非负且互不相同 */
function distractNumbers(ans, n) {
  const out = [];
  for (const d of shuffle([1, -1, 2, -2, 3, -3])) {
    if (out.length >= n) break;
    const v = ans + d;
    if (v >= 0 && v !== ans && !out.includes(v)) out.push(v);
  }
  let c = 0;
  while (out.length < n && c < 80) { const v = rand(ans + 8); if (v !== ans && !out.includes(v)) out.push(v); c++; }
  return out;
}

function choiceFrom(topic, q) {
  const opts = q.opts || shuffle([q.ans, ...distractNumbers(q.ans, 3)]);
  // ansIdx 优先（分类题答案为位置索引）；否则按答案值定位
  const ansIdx = q.ansIdx !== undefined ? q.ansIdx : opts.indexOf(q.ans);
  return {
    kind: 'choice', id: qid(topic), phase: 'review',
    big: q.big, prompt: q.prompt,
    options: opts.map(String), answer: ansIdx
  };
}

/* 学习卡示例 */
function example(topic) {
  if (topic.type === 'add' || topic.type === 'sub') {
    const q = arithQuestion(topic);
    return `例：${q.big} = ${q.ans}`;
  }
  if (topic.type === 'compare') {
    const q = compareQuestion();
    return `例：${q.big} 填 ${q.ans}`;
  }
  if (topic.type === 'shapes') return '例：⭕⭕⭕ 是 圆形';
  if (topic.type === 'classify') return '例：🔺🔺🟩🔺 → 第 3 个不一样';
  const q = arithQuestion({ type: rand(2) ? 'add' : 'sub', params: topic.params });
  return `例：${q.big} = ${q.ans}`;
}

function makeQuestion(topic) {
  // mix：先落定具体题型再出题，避免递归后 choiceFrom 套 choiceFrom（ans/opts 丢失）
  if (topic.type === 'mix') topic = { ...topic, type: rand(2) ? 'add' : 'sub' };
  let q;
  if (topic.type === 'add' || topic.type === 'sub') q = arithQuestion(topic);
  else if (topic.type === 'compare') q = compareQuestion();
  else if (topic.type === 'shapes') q = shapesQuestion();
  else q = classifyQuestion();
  return choiceFrom(topic, q);
}

/* ---------- 步骤组装 ---------- */
function buildSteps() {
  const steps = [];
  const current = CURR[Math.min(PROG.curriculum_index, CURR.length - 1)];
  const isNewTopic = !PROG.learned.some(l => l.id === current.id);

  // 1) 错题重做（保留原始 id，重做答对后从队列移除）
  if (PROG.wrong_queue.length) {
    const wrongs = PROG.wrong_queue.slice(0, 3);
    steps.push({ kind: 'section', label: '错题重做', subtitle: `上次做错的 ${wrongs.length} 道题，再来一次！`, emoji: '💪' });
    for (const w of wrongs) {
      steps.push({ kind: 'choice', id: w.id, phase: 'review', big: w.big, prompt: w.prompt, options: w.options, answer: w.answer, words: ['上次做错了，这次赢回来！'] });
    }
  }

  // 2) 学习卡（仅新知识点首次出现）
  if (isNewTopic) {
    steps.push({ kind: 'section', label: `新知识 · ${current.title}`, subtitle: current.desc, emoji: current.emoji });
    steps.push({
      kind: 'learn', id: current.id, phase: 'new', big: current.emoji, subtitle: current.title,
      prompt: current.desc, detail: example(current), speak: current.title, okLabel: '明白啦！'
    });
  }

  // 3) 当前知识点 5 题（当天批次内题面不重复）
  steps.push({ kind: 'section', label: `${current.title} 练习`, subtitle: '练一练，全对就升级！', emoji: current.emoji });
  const seenBig = new Set();
  for (let i = 0; i < 5; i++) {
    let s, tries = 0;
    do { s = makeQuestion(current); } while (seenBig.has(s.big) && ++tries < 30);
    seenBig.add(s.big);
    steps.push(s);
  }

  // 4) 已学知识点滚动 1-2 题
  const learned = PROG.learned.filter(l => l.id !== current.id);
  if (learned.length) {
    steps.push({ kind: 'section', label: '复习 · 已学本领', subtitle: '学过的本领可别忘啦！', emoji: '🔁' });
    for (const l of shuffle(learned).slice(0, 2)) {
      const t = CURR.find(c => c.id === l.id);
      if (t) steps.push(makeQuestion(t));
    }
  }
  return steps;
}

/* ---------- 注入模板 ---------- */
function inject(tpl, data) {
  const json = JSON.stringify(data).replace(/</g, '\\u003c').replace(/>/g, '\\u003e');
  return tpl.replace('<script id="lesson-data" type="application/json">{}</script>',
    '<script id="lesson-data" type="application/json">' + json + '</script>');
}

/* ---------- 结果合并 ---------- */
/* 入队/出队按 (id + 题面) 组合判断：qNo 每次生成从 0 重启，跨天 id 会撞号（如队列有 add10#1，
   次日新题也生成 add10#1），只按 id 会误删/误跳，必须连同题目内容一起匹配 */
function sameQuestion(a, b) {
  return a.id === b.id && a.big === b.big &&
    (!a.options || !b.options || a.options.join() === b.options.join());
}
function pushWrongQueue(w) {
  if (PROG.wrong_queue.some(x => sameQuestion(x, w))) return;
  PROG.wrong_queue.push(w);
  if (PROG.wrong_queue.length > 10) PROG.wrong_queue.shift();
}
function removeFromWrongQueue(item) {
  PROG.wrong_queue = PROG.wrong_queue.filter(x => {
    if (x.id !== item.id) return true;
    if (!item.step) return false;                       // 无题干明细 → 按 id 出队（旧格式结果）
    return !sameQuestion(x, { id: item.id, big: item.step.big, options: item.step.options });
  });
}

function mergeResults() {
  const resultsDir = path.join(DATA, 'results');
  const processedDir = path.join(resultsDir, 'processed');
  if (!fs.existsSync(resultsDir)) return 0;
  const files = fs.readdirSync(resultsDir).filter(f => f.startsWith('result-') && f.endsWith('.json'));
  let merged = 0;
  for (const f of files) {
    const r = JSON.parse(fs.readFileSync(path.join(resultsDir, f), 'utf8'));
    if (r.subject !== 'math') continue;
    // 每题明细（数学题 id 唯一，不聚合）→ 按知识点聚合状态
    const perTopic = {};
    for (const item of (r.review || [])) {
      const topic = String(item.id || '').split('#')[0];
      if (!topic) continue;
      perTopic[topic] = perTopic[topic] || { anyWrong: false, wrongItems: [] };
      if (item.correct) { removeFromWrongQueue(item); }            // 错题重做答对 → 出队
      else { perTopic[topic].anyWrong = true; if (item.step) perTopic[topic].wrongItems.push({ id: item.id, topic, ...item.step }); }
    }
    for (const [topic, info] of Object.entries(perTopic)) {
      let l = PROG.learned.find(x => x.id === topic);
      if (!l) { l = { id: topic, streak: 0, last_result: null }; PROG.learned.push(l); }
      if (info.anyWrong) {
        l.streak = 0; l.last_result = 'wrong';
        for (const w of info.wrongItems) pushWrongQueue(w);
      } else {
        l.streak = (l.streak || 0) + 1; l.last_result = 'correct';
      }
    }
    // 新知识点（学习卡）
    for (const id of (r.new_items || [])) {
      if (!PROG.learned.some(x => x.id === id)) PROG.learned.push({ id, streak: 0, last_result: null });
    }
    // 推进：当前知识点当日全对 → 学下一个
    const cur = CURR[Math.min(PROG.curriculum_index, CURR.length - 1)];
    const info = perTopic[cur.id];
    if (info && !info.anyWrong && PROG.curriculum_index < CURR.length - 1) PROG.curriculum_index++;
    // 统计
    PROG.stats.total_questions += (r.review || []).length;
    PROG.stats.total_correct += (r.stats && r.stats.correct) || 0;
    PROG.stats.sessions_done++;
    fs.renameSync(path.join(resultsDir, f), path.join(processedDir, f));
    merged++;
  }
  if (merged) { PROG.updated = today; save(); }
  return merged;
}

/* ---------- 主题（扁平单强调色：太空蓝） ---------- */
const THEME = {
  lang: 'zh-CN',
  logo: '🚀 数字星球',
  title: `数字星球 · ${today}`,
  accent: '#1E88E5', accentLight: '#64B5F6', accentDark: '#1565C0',
  accentText: '#0D47A1', accentSoft: '#E3F2FD', accentBorder: 'rgba(30,136,229,.35)',
  bg: '#F4F8FC',
  encourage: ['太棒了！', '好厉害！', '又算对一题！', '火箭加速！', '记牢啦！',
    '真聪明！', '继续加油！', '这一题漂亮！', '超厉害的！', '数字小天才！'],
  encBad: ['没关系，再想想！', '火箭在打转，修好它！', '不着急，慢慢算！', '下一题一定行！'],
  progIcon: '🚀', heroEmoji: '🚀', unlockLabel: '新知识',
  newLabel: '新知识', reportTitle: '🚀 数字星球 · 今日战报',
  praiseHigh: '超级厉害！数字小天才！',
  praiseMid: '很棒！火箭又前进一步！',
  praiseLow: '不错！多练几次会更棒！'
};

/* ---------- 主流程 ---------- */
function main() {
  loadProgress();
  if (args.includes('--merge')) {
    const n = mergeResults();
    console.log(n ? `✓ 已合并 ${n} 份数学结果` : '无待合并的数学结果');
    return;
  }
  const mergedN = mergeResults();   // 先消化昨天的数据
  const steps = buildSteps();
  const data = { date: today, subject: 'math', title: `数字星球 · ${today}`, theme: THEME, steps };
  const tpl = fs.readFileSync(TPL_FILE, 'utf8');
  const html = inject(tpl, data);
  const outFile = path.join(ROOT, 'sessions', today + '-math.html');
  fs.writeFileSync(outFile, html);
  const qCount = steps.filter(s => s.kind === 'choice').length;
  const cur = CURR[Math.min(PROG.curriculum_index, CURR.length - 1)];
  console.log(`✓ 已生成今日数学页 → sessions\\${today}-math.html`);
  console.log(`  当前知识点: ${cur.title}（${cur.desc}）`);
  console.log(`  题量 ${qCount} 道，错题重做 ${Math.min(PROG.wrong_queue.length, 3)} 道`);
  console.log(mergedN ? `  顺带合并了 ${mergedN} 份历史结果` : '');
  console.log('  用 Chrome 打开（建议 http://localhost）');
}
if (require.main === module) main();   // 供测试脚本 require 复用出题函数
module.exports = { makeQuestion };
