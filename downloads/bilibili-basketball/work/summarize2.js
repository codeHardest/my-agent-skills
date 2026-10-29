const fs = require('fs');
const path = require('path');

const BASE = 'P:/c2-workspace/trunk/server/downloads/bilibili-basketball';
const key = process.env.OPENROUTER_API_KEY;
const MODEL = 'deepseek/deepseek-chat-v3.1';
const included = JSON.parse(fs.readFileSync(BASE + '/work/included.json', 'utf8'));

const todo = included.filter(x => fs.existsSync(path.join(BASE, 'raw', x.bv, 'transcript.txt')));

function prompt(x, txt) {
  return `你的任务是校验字幕并总结篮球教学视频。

视频标题：${x.title}
UP主：${x.up}
分类：${x.cat}
时长：${x.dur}秒

第一步：判断下面这段字幕是否真的在讲这个篮球教学视频的内容。
如果字幕内容与该视频主题明显无关（例如是别的节目、歌曲、手机评测、游戏解说、广告），
请只输出：
MISMATCH: <一句话说明字幕实际内容，不超过30字>

第二步：如果相关，输出中文 Markdown 总结，包含：
**一句话概括**（不超过40字）
**核心要点**（3-5条，每条不超过35字）
**训练方法/动作步骤**（若无则写“字幕未具体讲解步骤”）
**常见错误或关键细节**（2-3条，若无则写“无”）

要求：只依据字幕，不要编造；总字数 200-350 字；不要输出标题层级。

字幕内容：
${txt.slice(0, 7000)}`;
}

async function callApi(x, txt, attempt = 0) {
  try {
    const r = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: MODEL,
        messages: [{ role: 'user', content: prompt(x, txt) }],
        temperature: 0.2,
        max_tokens: 900
      })
    });
    if (!r.ok) throw new Error('HTTP ' + r.status + ' ' + (await r.text()).slice(0, 150));
    const j = await r.json();
    const out = j.choices && j.choices[0] && j.choices[0].message && j.choices[0].message.content;
    if (!out) throw new Error('empty');
    return out.trim();
  } catch (e) {
    if (attempt < 3) {
      await new Promise(r => setTimeout(r, 2000 * (attempt + 1)));
      return callApi(x, txt, attempt + 1);
    }
    throw e;
  }
}

(async () => {
  let i = 0, ok = 0, mismatch = 0;
  const fail = [];
  const workers = Array.from({ length: 5 }, async () => {
    while (i < todo.length) {
      const x = todo[i++];
      const dir = path.join(BASE, 'raw', x.bv);
      const txt = fs.readFileSync(path.join(dir, 'transcript.txt'), 'utf8');
      if (txt.trim().length < 40) {
        fs.writeFileSync(path.join(dir, 'summary.md'), 'MISMATCH: 字幕内容过少（纯音乐或无讲解）\n', 'utf8');
        mismatch++;
        continue;
      }
      try {
        const s = await callApi(x, txt);
        fs.writeFileSync(path.join(dir, 'summary.md'), s + '\n', 'utf8');
        if (s.startsWith('MISMATCH')) mismatch++; else ok++;
      } catch (e) {
        fail.push(x.bv + ':' + e.message.slice(0, 100));
      }
    }
  });
  await Promise.all(workers);
  console.log('ok', ok, 'mismatch', mismatch, 'failed', fail.length);
  if (fail.length) console.log(fail.join('\n'));
})();
