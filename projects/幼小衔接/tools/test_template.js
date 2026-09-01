// 模板验证脚本：注入样例数据生成测试页 + 引擎脚本语法检查
// 用法: node tools/test_template.js

const fs = require('fs');
const path = require('path');

const tpl = fs.readFileSync(path.join(__dirname, '..', 'templates', 'lesson-app.html'), 'utf8');

// 1) 提取引擎脚本（最后一个 <script> 块，非 JSON 数据块）做语法检查
const scripts = [...tpl.matchAll(/<script(?![^>]*type="application\/json")[^>]*>([\s\S]*?)<\/script>/g)];
if (!scripts.length) { console.error('✗ 未找到引擎脚本'); process.exit(1); }
for (const [, body] of scripts) {
  try {
    new Function(body); // 仅解析，不执行（浏览器 API 不可用）
    console.log('✓ 引擎脚本语法正确');
  } catch (e) {
    console.error('✗ 引擎脚本语法错误:', e.message);
    process.exit(1);
  }
}

// 2) 样例数据
const sample = {
  date: '2026-08-19',
  subject: 'chinese',
  title: '奥特识字战 · 样例',
  steps: [
    { kind: 'section', label: '复习 · 怪兽军团', subtitle: '2 只怪兽等你消灭！', emoji: '👾👾' },
    { kind: 'choice', char: '日', phase: 'review', big: 'rì', big_tag: '拼音', prompt: '哪个字读 rì，能组成「日出」？', options: ['日','目','白','田'], answer: 0, words: ['日出','日月','日子'] },
    { kind: 'choice', char: '月', phase: 'review', big: '越', big_tag: '同音字', prompt: '哪个字和「越」读音一样？', options: ['月','明','朋','用'], answer: 0 },
    { kind: 'pronounce', char: '日', phase: 'review', phonetic: 'rì', text: '日', prompt: '跟着读「日」' },
    { kind: 'trace', char: '日', phase: 'review', stroke_count: 4 },
    { kind: 'section', label: '新技能解锁', subtitle: '学习 1 个新字', emoji: '🦸' },
    { kind: 'learn', char: '王', phase: 'new', pinyin: 'wáng', words: ['大王','国王','王子'], strokes: ['横','横','竖','横'] },
    { kind: 'choice', char: '王', phase: 'new', big: 'wáng', big_tag: '拼音', prompt: '刚学的字是哪个？', options: ['王','玉','主','全'], answer: 0 },
    { kind: 'pronounce', char: '王', phase: 'new', phonetic: 'wáng', text: '大王', prompt: '跟着读「大王」' },
    { kind: 'section', label: '最终决战', subtitle: '混战！', emoji: '⚡' },
    { kind: 'choice', char: '日', phase: 'review', big: '日', prompt: '哪个字读 rì？', options: ['日','目','白','田'], answer: 0 }
  ]
};

// 3) 注入数据生成测试页
const injected = tpl.replace('<script id="lesson-data" type="application/json">{}</script>',
  `<script id="lesson-data" type="application/json">${JSON.stringify(sample)}</script>`);
const out = path.join(__dirname, '..', 'sessions', '_sample.html');
fs.writeFileSync(out, injected);
console.log('✓ 已生成测试页 →', out);
