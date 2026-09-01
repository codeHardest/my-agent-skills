// 进度初始化脚本：基于字库生成 progress.json
// 用法: node tools/init_progress.js [日期]   （日期可选，默认今天）
// 规则:
//   - 字库前 LEARNED_COUNT 个字标记为「已学」（复习池），到期日错开
//   - 其余字标记为「新」（新字储备池，每日取3个引入）
//   - 已学字按 index/45 错开到期日 → 第一天起就有完整复习池

const fs = require('fs');
const path = require('path');

const LEARNED_COUNT = 332;      // 已学字数（对应大班毕业识字量，后续随洪恩导入调整）
const STAGGER = 45;             // 每批错开天数
const argDate = process.argv[2];

function todayStr() {
  if (argDate) return argDate;
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
}
function addDays(dateStr, n) {
  const d = new Date(dateStr + 'T00:00:00');
  d.setDate(d.getDate() + n);
  return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
}

const lib = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data', 'char_library.json'), 'utf8'));
const today = todayStr();

const chars = {};
lib.forEach((e, i) => {
  if (i < LEARNED_COUNT) {
    chars[e.char] = {
      status: 'review',
      interval_days: 1,
      due_date: addDays(today, Math.floor(i / STAGGER)),
      reviews: 0,
      consecutive_correct: 0,
      last_result: null
    };
  } else {
    chars[e.char] = {
      status: 'new',
      interval_days: 0,
      due_date: null,
      reviews: 0,
      consecutive_correct: 0,
      last_result: null
    };
  }
});

const progress = {
  schema_version: 1,
  subject: 'chinese',
  updated: today,
  daily_target: { review: 20, new: 3 },
  curriculum_index: LEARNED_COUNT,
  chars: chars,
  logs: [],
  stats: {
    start_date: today,
    total_reviews: 0,
    total_new: 0,
    total_stars: 0,
    sessions_done: 0
  }
};

const out = path.join(__dirname, '..', 'data', 'progress.json');
fs.writeFileSync(out, JSON.stringify(progress, null, 2) + '\n');
const dueToday = Object.values(chars).filter(c => c.status === 'review' && c.due_date === today).length;
const newPool = Object.values(chars).filter(c => c.status === 'new').length;
console.log('✓ 进度已初始化 →', out);
console.log(`  已学(复习池): ${LEARNED_COUNT} 字 | 今日到期: ${dueToday} 字 | 新字储备: ${newPool} 字`);
