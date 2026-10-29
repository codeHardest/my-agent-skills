(async () => {
  const bvs = window.__bvs;
  const out = {};
  for (const bv of bvs) {
    const v = await (await fetch(`https://api.bilibili.com/x/web-interface/view?bvid=${bv}`, { credentials: 'include' })).json();
    if (v.code === 0 && v.data) out[bv] = { title: v.data.title, desc: (v.data.desc || '').slice(0, 500), up: v.data.owner.name, dur: v.data.duration };
    await new Promise(r => setTimeout(r, 200));
  }
  window.__descs = out;
  return JSON.stringify({ n: Object.keys(out).length });
})()
