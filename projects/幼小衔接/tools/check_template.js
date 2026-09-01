// 模板引用完整性检查
const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join(__dirname, '..', 'templates', 'lesson-app.html'), 'utf8');

// 提取 $('xxx') 引用 与 id="xxx" 定义
const refs = new Set();
const refRe = /\$\(\s*'([\w-]+)'\s*\)/g;
let m;
while ((m = refRe.exec(html))) refs.add(m[1]);

const ids = new Set();
const idRe = /id="([\w-]+)"/g;
while ((m = idRe.exec(html))) ids.add(m[1]);

const missing = [...refs].filter(r => !ids.has(r));
console.log('DOM 引用数:', refs.size, '| 已定义 id 数:', ids.size);
if (missing.length) {
  console.error('✗ 未定义引用: ' + missing.join(', '));
  process.exit(1);
}
console.log('✓ 所有 DOM 引用都有对应元素');

// 检查样例页数据注入完整性
const sample = fs.readFileSync(path.join(__dirname, '..', 'sessions', '_sample.html'), 'utf8');
const dm = sample.match(/<script id="lesson-data" type="application\/json">([\s\S]*?)<\/script>/);
if (!dm) { console.error('✗ 未找到数据注入块'); process.exit(1); }
const data = JSON.parse(dm[1]);
console.log('✓ 数据注入可解析, steps:', data.steps.length);
