const fs = require('fs');
const path = require('path');

const BASE = 'P:/c2-workspace/trunk/server/downloads/bilibili-basketball';
const key = process.env.OPENROUTER_API_KEY;
const MODEL = 'deepseek/deepseek-chat-v3.1';
const included = JSON.parse(fs.readFileSync(BASE + '/work/included.json', 'utf8'));

const todo = included.filter(x => fs.existsSync(path.join(BASE, 'raw', x.bv, 'transcript.txt')));

function prompt(x, txt) {
  return `你是篮球训练内容编辑。下面是一段从视频自动语音识别得到的字幕，可能存在歌曲、广告、闲聊等无关片段和识别错误。

视频标题：${x.title}
UP主：${x.up}
分类：${x.cat}
时长：${x.dur}秒

请按以下规则处理：
1. 忽略歌曲、BGM 歌词、广告、无关闲聊等片段。
2. 若字幕中几乎没有任何与这个篮球教学视频相关的内容（例如整段只有歌曲/广告/游戏解说），只输出一行：
MISMATCH: <一句话说明字幕实际内容，不超过30字>
3. 否则只用相关部分写中文 Markdown 总结，包含：
**一句话概括**（不超过40字）
**核心要点**（3-5条，每条不超过35字）
**训练方法/动作步骤**（若无具体步骤则写“字幕未具体讲解步骤”）
**常见错误或关键细节**（2-3条，若无则写“无”）
如果字幕识别质量差，可在末尾补一行“> 注：字幕为自动识别，存在错漏”。

要求：只依据字幕，不要编造；总字数 200-350 字；不要输出标题层级。

字幕内容：
${txt.slice(0, 8000)}`;
}

async function callApi(x, txt, attempt = 0) {
  try {
    const r = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json' },
      body: JSON.stringify({ model: MODEL, messages: [{ role: 'user', content: prompt(x, txt) }], temperature: 0.2, max_tokens: 900 })
    });
    if (!r.ok) throw new Error('HTTP ' + r.status + ' ' + (await r.text()).slice(0, 150));
    const j = await r.json();
    const out = j.choices && j.choices[0] && j.choices[0].message && j.choices[0].message.content;
    if (!out) throw new Error('empty');
    return out.trim();
  } catch (e) {
    if (attempt < 3) { await new Promise(r => setTimeout(r, 2000 * (attempt + 1))); return callApi(x, txt, attempt + 1); }
    throw e;
  }
}

(async () => {
  let i = 0, ok = 0, mismatch = 0;
  const fail = [];
  await Promise.all(Array.from({ length: 5 }, async () => {
    while (i < todo.length) {
      const x = todo[i++];
      const dir = path.join(BASE, 'raw', x.bv);
      const txt = fs.readFileSync(path.join(dir, 'transcript.txt'), 'utf8');
      try {
        const s = await callApi(x, txt);
        fs.writeFileSync(path.join(dir, 'summary.md'), s + '\n', 'utf8');
        if (s.startsWith('MISMATCH')) mismatch++; else ok++;
      } catch (e) { fail.push(x.bv + ':' + e.message.slice(0, 100)); }
    }
  }));
  console.log('ok', ok, 'mismatch', mismatch, 'failed', fail.length);
  if (fail.length) console.log(fail.join('\n'));
})();
