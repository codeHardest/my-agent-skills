const fs = require('fs');
const path = require('path');
const W = 'P:/c2-workspace/trunk/server/downloads/bilibili-basketball/work';
const BASE = 'P:/c2-workspace/trunk/server/downloads/bilibili-basketball';

const raw = fs.readFileSync(W + '/subs2.json', 'utf8').replace(/^\uFEFF/, '');
const subs = JSON.parse(JSON.parse(raw));
const inc = JSON.parse(fs.readFileSync(W + '/included.json', 'utf8'));

const todo = inc.filter(x => subs[x.bv] && subs[x.bv].has && subs[x.bv].url);

function parseSub(j) { return (j.body || []).map(b => ({ from: b.from, to: b.to, text: (b.content || '').trim() })); }

async function dl(x) {
  const dir = path.join(BASE, 'raw', x.bv);
  fs.mkdirSync(dir, { recursive: true });
  const r = await fetch(subs[x.bv].url);
  if (!r.ok) throw new Error('HTTP ' + r.status);
  const j = await r.json();
  fs.writeFileSync(path.join(dir, 'subtitle.json'), JSON.stringify(j, null, 1), 'utf8');
  const lines = parseSub(j);
  fs.writeFileSync(path.join(dir, 'transcript.txt'), lines.map(l => l.text).filter(Boolean).join('\n'), 'utf8');
  const vtt = ['WEBVTT', ''];
  const ft = (t) => {
    const h = String(Math.floor(t / 3600)).padStart(2, '0');
    const m = String(Math.floor(t % 3600 / 60)).padStart(2, '0');
    const s = String(Math.floor(t % 60)).padStart(2, '0');
    const ms = String(Math.round((t % 1) * 1000)).padStart(3, '0');
    return `${h}:${m}:${s}.${ms}`;
  };
  for (const l of lines) { if (!l.text) continue; vtt.push(`${ft(l.from)} --> ${ft(l.to)}`, l.text, ''); }
  fs.writeFileSync(path.join(dir, 'subtitle.vtt'), vtt.join('\n'), 'utf8');
  return lines.length;
}

(async () => {
  let i = 0, ok = 0; const fail = [];
  await Promise.all(Array.from({ length: 5 }, async () => {
    while (i < todo.length) {
      const x = todo[i++];
      try { await dl(x); ok++; } catch (e) { fail.push(x.bv + ':' + e.message); }
    }
  }));
  console.log('downloaded', ok, 'failed', fail.length);
  if (fail.length) console.log(fail.slice(0, 10).join('\n'));
})();
