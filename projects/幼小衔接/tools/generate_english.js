/**
 * generate_english.js — 英语课程（字母探险队）每日生成器 + 结果合并。
 *
 * 与语文链路完全独立：读 data/english_library.json + data/progress_english.json，
 * 输出 sessions/YYYY-MM-DD-en.html；--merge 合并英语结果进 progress_english.json。
 *
 * 用法:
 *   node tools/generate_english.js                 生成今日页面（顺带合并历史结果）
 *   node tools/generate_english.js --date 2026-08-20   指定日期生成
 *   node tools/generate_english.js --merge         只合并结果，不生成页面
 *
 * 流程: 遗忘曲线选复习词(10) → 新词(5) → 复习题(听音/看图/选义轮换) →
 *       新词三件套(学习卡+巩固+跟读) → 单词大闯关 → 注入模板。
 */
'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DATA = path.join(ROOT, 'data');
const LIB_FILE = path.join(DATA, 'english_library.json');
const PROG_FILE = path.join(DATA, 'progress_english.json');
const TPL_FILE = path.join(ROOT, 'templates', 'lesson-app.html');

const LADDER = [1, 3, 7, 15, 30, 60];

function todayStr(offsetDays = 0) {
  const d = new Date();
  d.setDate(d.getDate() + offsetDays);
  return d.toISOString().slice(0, 10);
}
const args = process.argv.slice(2);
const dateIdx = args.indexOf('--date');
const today = dateIdx > -1 ? args[dateIdx + 1] : todayStr();
const TOMORROW = todayStr(1);

function shuffle(arr) { const a = [...arr]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
function rand(n) { return Math.floor(Math.random() * n); }

const LIB = JSON.parse(fs.readFileSync(LIB_FILE, 'utf8'));
const LIB_INDEX = Object.fromEntries(LIB.map((e, i) => [e.id, i]));

/* ---------- 进度（不存在则初始化） ---------- */
let PROG = null;
function save() { fs.writeFileSync(PROG_FILE, JSON.stringify(PROG, null, 2) + '\n'); }
function loadProgress() {
  if (fs.existsSync(PROG_FILE)) { PROG = JSON.parse(fs.readFileSync(PROG_FILE, 'utf8')); return; }
  PROG = {
    schema_version: 1, subject: 'english', updated: today,
    daily_target: { review: 10, new: 5 }, curriculum_index: 0,
    items: {},
    logs: [],
    stats: { start_date: today, total_reviews: 0, total_new: 0, total_stars: 0, sessions_done: 0 }
  };
  for (const e of LIB) PROG.items[e.id] = { status: 'new', interval_days: 1, due_date: today, reviews: 0, consecutive_correct: 0, last_result: null };
  save();
}

/* ---------- 选词 ---------- */
function selectReview(n) {
  const due = LIB.filter(e => {
    const p = PROG.items[e.id];
    return p && p.status !== 'new' && p.due_date <= today;
  });
  due.sort((a, b) => {
    const pa = PROG.items[a.id], pb = PROG.items[b.id];
    if (pa.due_date !== pb.due_date) return pa.due_date < pb.due_date ? -1 : 1;
    const ra = pa.last_result === 'correct' ? 1 : 0, rb = pb.last_result === 'correct' ? 1 : 0;
    if (ra !== rb) return ra - rb;
    return LIB_INDEX[a.id] - LIB_INDEX[b.id];
  });
  return due.slice(0, n);
}
function selectNew(n) {
  return LIB.slice(PROG.curriculum_index).filter(e => PROG.items[e.id] && PROG.items[e.id].status === 'new').slice(0, n);
}

/* 干扰项：同类别已学词优先 → 同类别未学词 → 已学池 → 词库随机（首日无已学词时保证仍有干扰项） */
function distract(target, n) {
  const exclude = new Set([target.id]);
  const learned = LIB.filter(e => !exclude.has(e.id) && PROG.items[e.id] && PROG.items[e.id].status !== 'new');
  const cat = LIB.filter(e => !exclude.has(e.id) && e.category === target.category);
  const catLearned = cat.filter(e => learned.includes(e));
  const pool = [
    ...shuffle(catLearned),
    ...shuffle(cat.filter(e => !learned.includes(e))),
    ...shuffle(learned),
    ...shuffle(LIB.filter(e => !exclude.has(e.id)))
  ];
  const seen = new Set(); const out = [];
  for (const e of pool) { if (out.length >= n) break; if (seen.has(e.id)) continue; seen.add(e.id); out.push(e); }
  return out.slice(0, n);
}

/* ---------- 题型 ---------- */
const MODES = ['pick_audio', 'pick_image', 'pick_meaning'];

function choiceStep(e, mode) {
  const ds = distract(e, 3);
  const opts = shuffle([e, ...ds]);
  const s = {
    kind: 'choice', id: e.id, phase: 'review', mode,
    options: opts.map(x => x.word), answer: opts.indexOf(e)
  };
  if (mode === 'pick_audio')   { s.big = '🔊'; s.prompt = '听一听，选出你听到的单词'; s.phonetic = e.word; s.words = [e.meaning]; }
  if (mode === 'pick_image')   { s.big = e.emoji; s.prompt = `哪个单词是「${e.meaning}」？`; s.words = [e.word]; }
  if (mode === 'pick_meaning') { s.big = e.meaning; s.prompt = '选出和中文意思对应的单词'; s.words = [e.word]; }
  return s;
}

function learnSteps(e, seed) {
  const review = choiceStep(e, MODES[(seed + 1) % 3]);   // 巩固题避开当天复习题型
  review.phase = 'new'; review.prompt = '刚学的单词是哪个？';
  return [
    { kind: 'learn', id: e.id, phase: 'new', big: e.word, subtitle: e.phonetic, emoji: e.emoji,
      detail: e.meaning, speak: e.word, okLabel: '我会啦！' },
    review,
    { kind: 'pronounce', id: e.id, phase: 'new', text: e.word, phonetic: e.phonetic, emoji: e.emoji,
      prompt: `跟着读「${e.word}」` }
  ];
}

function buildSteps(review, news) {
  const steps = [];
  if (review.length) {
    steps.push({ kind: 'section', label: '复习 · 单词巡逻', subtitle: `${review.length} 个单词等你认领！`, emoji: '🦁' });
    review.forEach((e, i) => steps.push(choiceStep(e, MODES[i % 3])));
  }
  steps.push({ kind: 'section', label: '新词汇解锁', subtitle: `学 ${news.length} 个新单词`, emoji: '🎈' });
  news.forEach((e, i) => steps.push(...learnSteps(e, i)));
  steps.push({ kind: 'section', label: '单词大闯关', subtitle: `${news.length} 词混战`, emoji: '⚡' });
  news.forEach((e, i) => {
    const c = choiceStep(e, MODES[(i + review.length) % 3]);
    c.phase = 'new'; c.prompt = c.prompt + '（刚学的哦）';
    steps.push(c);
  });
  return steps;
}

/* ---------- 注入模板 ---------- */
function inject(tpl, data) {
  const json = JSON.stringify(data).replace(/</g, '\\u003c').replace(/>/g, '\\u003e');
  return tpl.replace('<script id="lesson-data" type="application/json">{}</script>',
    '<script id="lesson-data" type="application/json">' + json + '</script>');
}

/* ---------- 结果合并 ---------- */
function mergeResults() {
  const resultsDir = path.join(DATA, 'results');
  const processedDir = path.join(resultsDir, 'processed');
  if (!fs.existsSync(resultsDir)) return 0;
  const files = fs.readdirSync(resultsDir).filter(f => f.startsWith('result-') && f.endsWith('.json'));
  let merged = 0;
  for (const f of files) {
    const r = JSON.parse(fs.readFileSync(path.join(resultsDir, f), 'utf8'));
    if (r.subject !== 'english') continue;   // 只合并英语结果，其他科目留给各自生成器
    // 复习
    for (const item of (r.review || [])) {
      const p = PROG.items[item.id];
      if (!p) continue;
      p.reviews++;
      if (item.correct) {
        p.consecutive_correct++;
        const ci = LADDER.indexOf(p.interval_days);
        p.interval_days = LADDER[Math.min(ci + 1, LADDER.length - 1)];
        p.due_date = todayStr(p.interval_days);
        p.last_result = 'correct';
        if (p.interval_days === 60 && p.consecutive_correct >= 3) p.status = 'mastered';
      } else {
        p.consecutive_correct = 0; p.interval_days = 1; p.due_date = TOMORROW;
        p.last_result = 'wrong'; p.status = 'review';
      }
    }
    // 新词
    for (const id of (r.new_items || [])) {
      const p = PROG.items[id];
      if (p && p.status === 'new') {
        p.status = 'review'; p.interval_days = 1; p.due_date = TOMORROW;
        p.reviews = (p.reviews || 0) + 1; p.last_result = null;
      }
    }
    // curriculum_index：第一个仍为 new 的词
    for (let i = 0; i < LIB.length; i++) {
      if (PROG.items[LIB[i].id].status === 'new') { PROG.curriculum_index = i; break; }
    }
    // 统计 + 日志
    PROG.stats.total_reviews += (r.review || []).length;
    PROG.stats.total_new += (r.new_items || []).length;
    PROG.stats.total_stars += (r.stats && r.stats.stars) || 0;
    PROG.stats.sessions_done++;
    PROG.logs.push({
      date: r.date,
      reviewed: (r.review || []).map(x => x.id),
      wrong: (r.review || []).filter(x => !x.correct).map(x => x.id),
      new: r.new_items || [],
      stars: (r.stats && r.stats.stars) || 0
    });
    fs.renameSync(path.join(resultsDir, f), path.join(processedDir, f));
    merged++;
  }
  if (merged) { PROG.updated = today; save(); }
  return merged;
}

/* ---------- 主题（扁平单强调色：丛林绿） ---------- */
const THEME = {
  lang: 'en-US',
  logo: '🦁 字母探险队',
  title: `字母探险队 · ${today}`,
  accent: '#43A047', accentLight: '#81C784', accentDark: '#2E7D32',
  accentText: '#1B5E20', accentSoft: '#E8F5E9', accentBorder: 'rgba(67,160,71,.35)',
  bg: '#F4FAF4',
  encourage: ['Great! 🎉', 'Awesome! ⭐', 'Well done! 🌟', 'Super! 💪', 'You rock! 🚀',
    'Nice! 🎈', 'Perfect! 🏆', 'Amazing! ✨', 'Fantastic! 🦁', 'Keep going! 🌈'],
  encBad: ['Try again! 💪', 'Almost! 😊', 'You can do it! 🌟', 'One more time! 🎯'],
  progIcon: '🦁', heroEmoji: '🦁', unlockLabel: '新单词',
  newLabel: '新词', reportTitle: '🦁 字母探险队 · 今日战报',
  praiseHigh: "Amazing! You're a word star! 🌟",
  praiseMid: 'Great job! Keep exploring! 🧭',
  praiseLow: 'Good effort! Practice makes perfect! 💪'
};

/* ---------- 主流程 ---------- */
function main() {
  loadProgress();
  if (args.includes('--merge')) {
    const n = mergeResults();
    console.log(n ? `✓ 已合并 ${n} 份英语结果` : '无待合并的英语结果');
    return;
  }
  const mergedN = mergeResults();   // 先消化昨天的数据
  const review = selectReview(PROG.daily_target.review);
  const news = selectNew(PROG.daily_target.new);
  if (!review.length && !news.length) {
    console.log('今日无任务（无到期单词、词库已学完）');
    return;
  }
  const steps = buildSteps(review, news);
  const data = { date: today, subject: 'english', title: `字母探险队 · ${today}`, theme: THEME, steps };
  const tpl = fs.readFileSync(TPL_FILE, 'utf8');
  const html = inject(tpl, data);
  const outFile = path.join(ROOT, 'sessions', today + '-en.html');
  fs.writeFileSync(outFile, html);
  console.log(`✓ 已生成今日英语页 → sessions\\${today}-en.html`);
  console.log(`  复习 ${review.length} 词: ${review.map(e => e.word).join(' ')}`);
  console.log(`  新学 ${news.length} 词: ${news.map(e => e.word).join(' ')}`);
  console.log(mergedN ? `  顺带合并了 ${mergedN} 份历史结果` : '');
  console.log('  用 Chrome 打开（建议 http://localhost 以获得语音识别）');
}
main();
