(async () => {
  const ids = [4113946126, 4020163726];
  const out = {};
  for (const id of ids) {
    const items = [];
    let info = null;
    for (let pn = 1; pn <= 60; pn++) {
      const r = await fetch(`https://api.bilibili.com/x/v3/fav/resource/list?media_id=${id}&pn=${pn}&ps=20&platform=web&order=mtime&type=0&tid=0`, { credentials: 'include' });
      const j = await r.json();
      if (j.code !== 0 || !j.data) break;
      if (!info) info = j.data.info;
      const medias = j.data.medias || [];
      if (!medias.length) break;
      for (const m of medias) {
        items.push({ bv: m.bvid, title: m.title, up: m.upper && m.upper.name, dur: m.duration });
      }
      if (!j.data.has_more) break;
    }
    out[id] = { title: info && info.title, count: info && info.media_count, items };
  }
  window.__favdata = out;
  return JSON.stringify({ ok: true, summary: Object.fromEntries(Object.entries(out).map(([k, v]) => [k, { title: v.title, got: v.items.length }])) });
})()
