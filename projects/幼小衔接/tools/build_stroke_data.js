/**
 * build_stroke_data.js — 从 hanzi-writer-data 源提取笔顺矢量数据，打包成浏览器可直接引用的单文件。
 *
 * 输入:   data/char_library.json（字表）
 * 数据源: 仓库内 node_modules/hanzi-writer-data/（已加入 .gitignore，不提交）；
 *         缺失时首次运行自动从 npm registry 下载指定版本 tgz 解压到该目录（安装后无需重复下载）；
 *         兜底复用父级 node_modules 的既有安装。
 * 输出:   data/stroke_data.js  →  window.STROKE_DATA = { "字": {strokes:[...], medians:[...]}, ... }
 *
 * 用法:   node tools/build_stroke_data.js
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const ROOT = path.join(__dirname, '..');
const DATA = path.join(ROOT, 'data');
const LIB_FILE = path.join(DATA, 'char_library.json');
const OUT_FILE = path.join(DATA, 'stroke_data.js');

const HW_DATA_VERSION = '2.0.1';

/** 确保 hanzi-writer-data 源目录存在（含每字一个 json 的根目录），缺失时自动下载到仓库内 node_modules */
function ensureSourceDir() {
  // 1) 仓库内 node_modules（已被 .gitignore 忽略，装好后常驻）
  const nmDir = path.join(ROOT, 'node_modules');
  const local = path.join(nmDir, 'hanzi-writer-data');
  if (fs.existsSync(local) && fs.existsSync(path.join(local, '一.json'))) return local;
  // 2) 复用父级 node_modules 的既有安装，避免重复下载
  const globalCandidates = [
    path.join(ROOT, '..', 'node_modules', 'hanzi-writer-data'),
  ];
  for (const g of globalCandidates) {
    if (fs.existsSync(g) && fs.existsSync(path.join(g, '一.json'))) return g;
  }
  // 3) 下载 tgz 到仓库内 node_modules 并解压（首次运行自动安装，目录已 gitignore 不入库）
  const tarball = `https://registry.npmjs.org/hanzi-writer-data/-/hanzi-writer-data-${HW_DATA_VERSION}.tgz`;
  const tgz = path.join(nmDir, `hanzi-writer-data-${HW_DATA_VERSION}.tgz`);
  console.log(`字库缺失，自动下载 ${tarball}\n  解压到 node_modules/hanzi-writer-data（已 gitignore，仅首次运行）`);
  fs.mkdirSync(nmDir, { recursive: true });
  execSync(`curl -sL "${tarball}" -o "${tgz}"`, { stdio: 'inherit' });
  if (fs.existsSync(local)) fs.rmSync(local, { recursive: true, force: true });
  fs.mkdirSync(local, { recursive: true });
  execSync(`tar -xzf "${unixPath(tgz)}" --force-local -C "${unixPath(local)}" --strip-components=1`, { stdio: 'inherit' });
  fs.rmSync(tgz, { force: true });
  if (!fs.existsSync(path.join(local, '一.json'))) {
    throw new Error('下载解压后未找到 一.json，数据源校验失败');
  }
  return local;
}

/** Windows 反斜杠路径转正斜杠（tar 在 Git Bash/MSYS 下会把 \ 当转义符处理） */
function unixPath(p) { return p.replace(/\\/g, '/'); }

function main() {
  const lib = JSON.parse(fs.readFileSync(LIB_FILE, 'utf8'));
  if (!Array.isArray(lib)) throw new Error('char_library.json 应为数组');
  const srcDir = ensureSourceDir();

  const out = {};
  const missing = [];
  for (const entry of lib) {
    const ch = entry.char;
    if (!ch) continue;
    const f = path.join(srcDir, ch + '.json');
    if (!fs.existsSync(f)) { missing.push(ch); continue; }
    const d = JSON.parse(fs.readFileSync(f, 'utf8'));
    out[ch] = { strokes: d.strokes || [], medians: d.medians || [] };
  }

  const body = 'window.STROKE_DATA = ' + JSON.stringify(out) + ';';
  fs.writeFileSync(OUT_FILE, body, 'utf8');
  console.log(`✓ 已生成 ${OUT_FILE}`);
  console.log(`  字数: ${Object.keys(out).length} / ${lib.length}`);
  console.log(`  体积: ${(Buffer.byteLength(body) / 1024).toFixed(1)} KB`);
  if (missing.length) {
    console.warn(`⚠️ 缺 ${missing.length} 字数据: ${missing.join(' ')}`);
    process.exitCode = 1;
  } else {
    console.log('  全部字均有笔顺数据 ✅');
  }
}

main();
