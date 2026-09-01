// 每日学习页生成器（技能 kid-learn 的确定性参考实现）
// 用法:
//   node tools/generate_session.js               生成今日页面（复习20字+新字3个）
//   node tools/generate_session.js --date 2026-08-19   指定日期
//   node tools/generate_session.js --merge       仅合并 results/ 到 progress，不生成页面
//
// 规则与 SKILL.md 一致：遗忘曲线选字 + 题型配额(14识字+3同音相似+2拼音+1发音)
// 所有干扰项均取自已学字库，不超纲。

const fs = require('fs');
const path = require('path');
const ROOT = path.join(__dirname, '..');
const DATA = path.join(ROOT, 'data');
const LIB = JSON.parse(fs.readFileSync(path.join(DATA, 'char_library.json'), 'utf8'));
const PROG = JSON.parse(fs.readFileSync(path.join(DATA, 'progress.json'), 'utf8'));

const LADDER = [1, 3, 7, 15, 30, 60];

// 已学字（复习池）：progress 里 status != new 的字
function learnedPool() {
  return LIB.filter(e => PROG.chars[e.char] && PROG.chars[e.char].status !== 'new');
}

/* ---------- 工具 ---------- */
function shuffle(a) {
  const arr = a.slice();
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}
function todayStr(date) {
  if (date) return date;
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
}
function addDays(dateStr, n) {
  const d = new Date(dateStr + 'T00:00:00');
  d.setDate(d.getDate() + n);
  return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
}
function charByChar(ch) { return LIB.find(e => e.char === ch); }
function progressOf(ch) { return PROG.chars[ch]; }
function isLearned(ch) { return progressOf(ch) && progressOf(ch).status !== 'new'; }

// 从已学池中抽 n 个干扰字，排除 exclude 集合
function distractChars(n, exclude = new Set()) {
  const pool = shuffle(learnedPool()).filter(e => !exclude.has(e.char));
  return pool.slice(0, n).map(e => e.char);
}

/* ---------- 遗忘曲线选字 ---------- */
function selectReview(today, targetN) {
  const due = LIB
    .filter(e => {
      const p = progressOf(e.char);
      return p && p.status !== 'new' && p.due_date && p.due_date <= today;
    })
    .map(e => ({ e, p: progressOf(e.char), order: LIB.indexOf(e) }));
  due.sort((a, b) => {
    if (a.p.due_date !== b.p.due_date) return a.p.due_date < b.p.due_date ? -1 : 1;
    const aw = a.p.last_result === 'wrong' || a.p.last_result === null ? 0 : 1;
    const bw = b.p.last_result === 'wrong' || b.p.last_result === null ? 0 : 1;
    if (aw !== bw) return aw - bw;
    return a.order - b.order;
  });
  return due.slice(0, targetN).map(d => d.e);
}
function selectNew(today, targetN) {
  return LIB.filter(e => progressOf(e.char) && progressOf(e.char).status === 'new').slice(0, targetN);
}

/* ---------- 同音/相似兄弟 ---------- */
function homophoneSibling(e) {
  // 同组内已学的另一个字
  return learnedPool().find(o => o.char !== e.char && o.phonetic_group === e.phonetic_group);
}
function similarSibling(e) {
  return e.similar.find(ch => isLearned(ch) && ch !== e.char);
}

/* ---------- 生成选择题步骤 ---------- */
function choiceStep(e, mode) {
  const target = e.char;
  const exclude = new Set([target]);
  let big, big_tag, prompt, options, answer;

  if (mode === 'pick_char') {
    big = e.pinyin; big_tag = '🔊 拼音';
    prompt = `哪个字读 ${e.pinyin}？`;
    const distract = distractChars(3, exclude);
    options = shuffle([target, ...distract]);
    answer = options.indexOf(target);
  } else if (mode === 'pick_word') {
    // 题干用拼音表达目标字（不直接显示字形，避免答案泄露）
    big = e.pinyin;
    big_tag = '🔊 拼音';
    prompt = `哪个词里有读「${e.pinyin}」的字？`;
    const correctWord = e.words[0];
    const others = [];
    const seenWords = new Set([correctWord]);
    // 干扰词集合内部不能有共同字符：防「一千/千万/千秋」「火车/灯火/大火」这类
    // 扎堆模式——干扰词全体共有某个字（而答案没有）时，孩子按“另类”即可蒙对
    let sharedChars = null;   // 已选干扰词全体共同包含的字符
    const pick = (w) => { others.push(w); seenWords.add(w); };
    for (const d of distractChars(8, exclude)) {
      const entry = charByChar(d);
      if (!entry) continue;
      for (const w of entry.words) {
        if (others.length >= 3) break;
        if (seenWords.has(w) || w.includes(target)) continue;
        if (others.length >= 2 && sharedChars && [...w].some(c => sharedChars.has(c))) continue;
        pick(w);
        if (others.length === 1) sharedChars = new Set([...w]);
        else if (others.length === 2) sharedChars = new Set([...others[0]].filter(c => w.includes(c)));
        else sharedChars = new Set([...sharedChars].filter(c => w.includes(c)));
      }
      if (others.length >= 3) break;
    }
    // 兜底：词池不够时放宽，保证凑满 3 个（罕见时允许）
    if (others.length < 3) {
      for (const d of distractChars(8, exclude)) {
        const entry = charByChar(d);
        if (!entry) continue;
        for (const w of entry.words) {
          if (others.length >= 3) break;
          if (!seenWords.has(w) && !w.includes(target)) pick(w);
        }
      }
    }
    options = shuffle([correctWord, ...others]);
    answer = options.indexOf(correctWord);
  } else if (mode === 'pick_pinyin') {
    big = target; big_tag = '汉字';
    prompt = `「${target}」的拼音是哪个？`;
    const others = [];
    const seen = new Set([e.pinyin]);
    for (const d of distractChars(8, exclude)) {
      const entry = charByChar(d);
      if (!entry) continue;
      if (!seen.has(entry.pinyin) && others.length < 3) { others.push(entry.pinyin); seen.add(entry.pinyin); }
    }
    options = shuffle([e.pinyin, ...others]);
    answer = options.indexOf(e.pinyin);
  } else if (mode === 'pick_homophone') {
    const sib = homophoneSibling(e);
    if (!sib) return choiceStep(e, 'pick_char');
    big = target;
    prompt = `哪个字和「${target}」读音一样？`;
    const distract = distractChars(3, new Set([target, sib.char]));
    options = shuffle([sib.char, ...distract]);
    answer = options.indexOf(sib.char);
  } else if (mode === 'pick_similar') {
    const sib = similarSibling(e);
    if (!sib) return choiceStep(e, 'pick_char');
    big = target;
    prompt = `哪个字和「${target}」长得像？`;
    const distract = distractChars(3, new Set([target, sib]));
    options = shuffle([sib, ...distract]);
    answer = options.indexOf(sib);
  }

  return {
    kind: 'choice', char: target, phase: 'review', mode,
    big, big_tag, prompt, options, answer,
    words: e.words.slice(0, 3), phonetic: e.pinyin
  };
}

/* ---------- 新字步骤 ---------- */
const STROKES_MAP = {
  '王': ['横','横','竖','横'], '全': ['撇','捺','横','横','竖'],
  '公': ['撇','捺','撇折','点'], '主': ['点','横','横','竖','横'],
  '迎': ['撇','竖提','横折钩','竖','点','横折折撇','捺'],
  '住': ['撇','竖','点','横','横','竖','横'],
  '居': ['横折','横','撇','横','竖','竖','横折','横'],
  '圆': ['竖','横折','竖','横折','横','竖','横折','撇','点','横'],
  '尾': ['横折','横','撇','撇','横折钩','横','横','竖弯钩'],
  '巴': ['横折','竖','横','竖弯钩']
};
function learnSteps(e, today) {
  const strokes = STROKES_MAP[e.char] || e.strokes || [];
  const base = { kind: 'learn', char: e.char, phase: 'new', pinyin: e.pinyin, words: e.words.slice(0,3), strokes };
  const c1 = choiceStep({ ...e, phase: 'new' }, 'pick_char'); c1.phase = 'new'; c1.prompt = `刚学的字是哪个？`;
  const c2 = choiceStep({ ...e, phase: 'new' }, 'pick_word'); c2.phase = 'new';
  const c3 = choiceStep({ ...e, phase: 'new' }, 'pick_pinyin'); c3.phase = 'new'; c3.prompt = `「${e.char}」的拼音是哪个？`;
  const trace = { kind: 'trace', char: e.char, phase: 'new', stroke_count: strokes.length || 1, phonetic: e.pinyin };
  const pron = { kind: 'pronounce', char: e.char, phase: 'new', phonetic: e.pinyin, text: e.words[0], prompt: '跟着读「' + e.words[0] + '」' };
  return [base, c1, c2, c3, trace, pron];
}

/* ---------- 组装 steps ---------- */
function buildSteps(reviewChars, newChars, today) {
  const steps = [];
  steps.push({ kind: 'section', label: '复习 · 怪兽军团', subtitle: `${reviewChars.length} 只怪兽等你消灭！`, emoji: '👾' });

  // 题型配额：3 同音/相似（优先有兄弟的字）、2 拼音、1 发音，其余 14 识字
  const qualified = reviewChars.map(e => ({ e, hom: homophoneSibling(e), sim: similarSibling(e) }));
  const homSimPool = qualified.filter(q => q.hom || q.sim);
  const used = new Set();
  let homSim = 0, pinyin = 0;
  reviewChars.forEach((e, i) => {
    if (i === 15) { steps.push({ kind: 'pronounce', char: e.char, phase: 'review', phonetic: e.pinyin, text: e.char, prompt: '跟着读「' + e.char + '」' }); used.add(i); return; }
    const q = qualified[i];
    let mode;
    if (homSim < 3 && (q.hom || q.sim)) {
      mode = q.hom ? 'pick_homophone' : 'pick_similar';
      homSim++;
    } else if (pinyin < 2) {
      mode = 'pick_pinyin'; pinyin++;
    } else {
      mode = (i % 2 === 0) ? 'pick_char' : 'pick_word';
    }
    steps.push(choiceStep(e, mode));
  });

  steps.push({ kind: 'section', label: '新技能解锁', subtitle: `学习 ${newChars.length} 个新字`, emoji: '🦸' });
  for (const e of newChars) steps.push(...learnSteps(e, today));

  steps.push({ kind: 'section', label: '最终决战', subtitle: '新字混战！', emoji: '⚡' });
  for (const e of newChars) {
    steps.push({ ...choiceStep({ ...e }, (['pick_char','pick_word','pick_pinyin'])[newChars.indexOf(e)]), phase: 'new' });
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
function mergeResults() {
  const resultsDir = path.join(DATA, 'results');
  const processedDir = path.join(resultsDir, 'processed');
  const files = fs.readdirSync(resultsDir).filter(f => f.startsWith('result-') && f.endsWith('.json'));
  let merged = 0;
  for (const f of files) {
    const r = JSON.parse(fs.readFileSync(path.join(resultsDir, f), 'utf8'));
    if (r.subject !== 'chinese') { console.log('跳过非语文结果:', f); continue; }
    // 复习结果（模板输出键为 id，兼容旧 char 键）
    for (const item of (r.review || [])) {
      const p = PROG.chars[item.id || item.char];
      if (!p) continue;
      p.reviews++;
      if (item.correct) {
        p.consecutive_correct++;
        const ci = LADDER.indexOf(p.interval_days);
        p.interval_days = LADDER[Math.min(ci + 1, LADDER.length - 1)];
        p.due_date = addDays(today, p.interval_days);
        p.last_result = 'correct';
        if (p.interval_days === 60 && p.consecutive_correct >= 3) p.status = 'mastered';
      } else {
        p.consecutive_correct = 0;
        p.interval_days = 1;
        p.due_date = addDays(today, 1);
        p.last_result = 'wrong';
        p.status = 'review';
      }
    }
    // 新字（模板输出 new_items，兼容旧 new_chars）
    for (const ch of (r.new_items || r.new_chars || [])) {
      const p = PROG.chars[ch];
      if (p && p.status === 'new') {
        p.status = 'review'; p.interval_days = 1; p.due_date = addDays(today, 1);
        p.reviews = (p.reviews || 0) + 1; p.last_result = null;
      }
    }
    // 更新 curriculum_index
    for (let i = 0; i < LIB.length; i++) {
      if (PROG.chars[LIB[i].char] && PROG.chars[LIB[i].char].status === 'new') {
        PROG.curriculum_index = i; break;
      }
    }
    // 统计
    PROG.stats.total_reviews += (r.review || []).length;
    PROG.stats.total_new += (r.new_items || r.new_chars || []).length;
    PROG.stats.total_stars += (r.stats && r.stats.stars) || 0;
    PROG.stats.sessions_done++;
    PROG.logs.push({
      date: r.date,
      reviewed: (r.review || []).map(x => x.id || x.char),
      wrong: (r.review || []).filter(x => !x.correct).map(x => x.id || x.char),
      new: r.new_items || r.new_chars || [],
      stars: (r.stats && r.stats.stars) || 0
    });
    fs.renameSync(path.join(resultsDir, f), path.join(processedDir, f));
    merged++;
  }
  PROG.updated = today;
  fs.writeFileSync(path.join(DATA, 'progress.json'), JSON.stringify(PROG, null, 2) + '\n');
  return merged;
}

/* ---------- 主流程 ---------- */
const args = process.argv.slice(2);
const today = args.includes('--merge') ? todayStr() : todayStr(args[args.indexOf('--date') + 1]);

if (args.includes('--merge')) {
  const n = mergeResults();
  console.log(n ? `✓ 已合并 ${n} 份结果` : '无待合并结果');
  process.exit(0);
}

// 1) 先合并历史（保证遗忘曲线准确）
const mergedN = mergeResults();

// 2) 选字
const reviewChars = selectReview(today, PROG.daily_target.review);
const newChars = selectNew(today, PROG.daily_target.new);

if (!reviewChars.length && !newChars.length) {
  console.log('今日无任务（无到期字、无新字）');
  process.exit(0);
}

// 3) 组装并注入
const steps = buildSteps(reviewChars, newChars, today);
const data = { date: today, subject: 'chinese', title: `奥特识字战 · ${today}`, steps };
const tpl = fs.readFileSync(path.join(ROOT, 'templates', 'lesson-app.html'), 'utf8');
const html = inject(tpl, data);
const outFile = path.join(ROOT, 'sessions', today + '.html');
fs.writeFileSync(outFile, html);

// 4) 汇报
console.log(`✓ 已生成今日学习页 → sessions\\${today}.html`);
console.log(`  复习 ${reviewChars.length} 字: ${reviewChars.map(e=>e.char).join('')}`);
console.log(`  新学 ${newChars.length} 字: ${newChars.map(e=>e.char).join('')}`);
console.log(mergedN ? `  顺带合并了 ${mergedN} 份历史结果` : '');
console.log('  用 Chrome 打开（建议 http://localhost 以获得语音识别）');
