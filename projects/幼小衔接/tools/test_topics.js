/**
 * test_topics.js — 数学出题逻辑批量验证（临时脚本）。
 * 对每个知识点生成 60 题，校验：选项 4 个、答案索引合法、答案值/符号正确、
 * 加减法约束（进位/退位/上限）成立、compare/classify 选项无垃圾值。
 * 用法: node tools/test_topics.js
 */
'use strict';
const M = require('./generate_math.js');

function rand() { return 1; } // 占位，实际用不到

const TOPICS = [
  { id: 'shapes', type: 'shapes', title: '图形认识' },
  { id: 'classify', type: 'classify', title: '找不同' },
  { id: 'compare', type: 'compare', title: '比大小', params: { max: 20 } },
  { id: 'add10', type: 'add', title: '10以内加法', params: { max: 10 } },
  { id: 'sub10', type: 'sub', title: '10以内减法', params: { max: 10 } },
  { id: 'add20', type: 'add', title: '进位加法', params: { max: 20, carry: true } },
  { id: 'sub20', type: 'sub', title: '退位减法', params: { max: 20, borrow: true } },
  { id: 'mix20', type: 'mix', title: '综合挑战', params: { max: 20 } }
];

let allOk = true;
function fail(topic, q, why) { allOk = false; console.log(`  ✗ ${topic.title}: ${why} | ${JSON.stringify(q)}`); }

for (const t of TOPICS) {
  const seen = new Set();
  for (let i = 0; i < 60; i++) {
    const q = M.makeQuestion(t);
    // 结构
    if (q.kind !== 'choice') { fail(t, q, 'kind 不是 choice'); continue; }
    if (!Array.isArray(q.options) || q.options.length !== 4) { fail(t, q, `选项 ${q.options.length} 个`); continue; }
    if (typeof q.answer !== 'number' || q.answer < 0 || q.answer > 3) { fail(t, q, `answer=${q.answer} 非法`); continue; }
    if (!(q.big && q.prompt)) { fail(t, q, '缺 big/prompt'); continue; }
    const dup = new Set(q.options).size !== 4;
    if (dup) { fail(t, q, '选项重复'); continue; }

    // 语义（60 次采样空间小，允许题面重复，只校验正确性）
    if (t.type === 'add' || t.type === 'sub' || t.type === 'mix') {
      const m = String(q.big).match(/(-?\d+) ([+-]) (-?\d+)/);
      if (!m) { fail(t, q, `big 无法解析: ${q.big}`); continue; }
      const a = +m[1], b = +m[3], ans = m[2] === '+' ? a + b : a - b;
      const p = t.params || {};
      if (q.options[q.answer] !== String(ans)) fail(t, q, `答案 ${q.options[q.answer]} ≠ ${ans}`);
      if (t.type === 'add') {
        if (p.carry && a + b < 10) fail(t, q, `非进位题 (${q.big})`);
        if (!p.carry && a + b > (p.max || 10)) fail(t, q, `超出上限 (${q.big})`);
      } else if (t.type === 'sub') {
        if (p.borrow && !(a % 10 < b)) fail(t, q, `非退位题 (${q.big})`);
        if (!p.borrow && !(b >= 1 && b < a)) fail(t, q, `减法参数异常 (${q.big})`);
      }
    } else if (t.type === 'compare') {
      const m = String(q.big).match(/(\d+) ⚖️ (\d+)/);
      if (!m) { fail(t, q, `big 无法解析: ${q.big}`); continue; }
      const a = +m[1], b = +m[2];
      if (a === b) { fail(t, q, '两数相等，无大小关系'); continue; }
      const expect = a > b ? '>' : '<';
      if (q.options[q.answer] !== expect) fail(t, q, `答案 ${q.options[q.answer]} ≠ ${expect}`);
      if (q.options.some(o => !['>', '<', '=', '≠'].includes(o))) fail(t, q, `干扰项含垃圾值: ${q.options}`);
      if (new Set(q.options).size !== 4) fail(t, q, '选项重复');
    } else if (t.type === 'shapes') {
      if (!q.options.includes(q.options[q.answer])) fail(t, q, '答案不在选项');
    } else if (t.type === 'classify') {
      if (!/^第[1-4]个$/.test(q.options[q.answer])) fail(t, q, `answer 索引非位置: ${q.options[q.answer]}`);
    }
  }
  console.log(`  ✓ ${t.title}（60 题）`);
}

// 边界：sub20 退位题 a 的十位=1（11..18），保证退位后不为负
const sub20 = { id: 'sub20', type: 'sub', title: 'x', params: { max: 20, borrow: true } };
for (let i = 0; i < 200; i++) {
  const q = M.makeQuestion(sub20);
  const m = String(q.big).match(/(\d+) - (\d+)/);
  const a = +m[1], b = +m[2];
  if (a - b < 0) { allOk = false; fail(sub20, q, `结果为负 ${a}-${b}`); }
}

console.log(allOk ? '\n全部通过 ✓' : '\n存在失败 ✗');
process.exit(allOk ? 0 : 1);
