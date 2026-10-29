(async () => {
  const bv = 'BV1eG411E7dA';
  const v = await (await fetch(`https://api.bilibili.com/x/web-interface/view?bvid=${bv}`, { credentials: 'include' })).json();
  const d = v.data;
  const p = await (await fetch(`https://api.bilibili.com/x/player/v2?aid=${d.aid}&cid=${d.cid}&bvid=${bv}`, { credentials: 'include' })).json();
  const list = (p.data && p.data.subtitle && p.data.subtitle.subtitles) || [];
  const url = list[0] && ('https:' + list[0].subtitle_url);
  let head = null;
  if (url) {
    const j = await (await fetch(url)).json();
    head = (j.body || []).slice(0, 3).map(b => b.content).join(' | ');
  }
  return JSON.stringify({ title: d.title, aid: d.aid, cid: d.cid, url, head });
})()
