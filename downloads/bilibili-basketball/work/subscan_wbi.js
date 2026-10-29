(async () => {
  function md5cycle(x,k){let a=x[0],b=x[1],c=x[2],d=x[3];a=ff(a,b,c,d,k[0],7,-680876936);d=ff(d,a,b,c,k[1],12,-389564586);c=ff(c,d,a,b,k[2],17,606105819);b=ff(b,c,d,a,k[3],22,-1044525330);a=ff(a,b,c,d,k[4],7,-176418897);d=ff(d,a,b,c,k[5],12,1200080426);c=ff(c,d,a,b,k[6],17,-1473231341);b=ff(b,c,d,a,k[7],22,-45705983);a=ff(a,b,c,d,k[8],7,1770035416);d=ff(d,a,b,c,k[9],12,-1958414417);c=ff(c,d,a,b,k[10],17,-42063);b=ff(b,c,d,a,k[11],22,-1990404162);a=ff(a,b,c,d,k[12],7,1804603682);d=ff(d,a,b,c,k[13],12,-40341101);c=ff(c,d,a,b,k[14],17,-1502002290);b=ff(b,c,d,a,k[15],22,1236535329);a=gg(a,b,c,d,k[1],5,-165796510);d=gg(d,a,b,c,k[6],9,-1069501632);c=gg(c,d,a,b,k[11],14,643717713);b=gg(b,c,d,a,k[0],20,-373897302);a=gg(a,b,c,d,k[5],5,-701558691);d=gg(d,a,b,c,k[10],9,38016083);c=gg(c,d,a,b,k[15],14,-660478335);b=gg(b,c,d,a,k[4],20,-405537848);a=gg(a,b,c,d,k[9],5,568446438);d=gg(d,a,b,c,k[14],9,-1019803690);c=gg(c,d,a,b,k[3],14,-187363961);b=gg(b,c,d,a,k[8],20,1163531501);a=gg(a,b,c,d,k[13],5,-1444681467);d=gg(d,a,b,c,k[2],9,-51403784);c=gg(c,d,a,b,k[7],14,1735328473);b=gg(b,c,d,a,k[12],20,-1926607734);a=hh(a,b,c,d,k[5],4,-378558);d=hh(d,a,b,c,k[8],11,-2022574463);c=hh(c,d,a,b,k[11],16,1839030562);b=hh(b,c,d,a,k[14],23,-35309556);a=hh(a,b,c,d,k[1],4,-1530992060);d=hh(d,a,b,c,k[4],11,1272893353);c=hh(c,d,a,b,k[7],16,-155497632);b=hh(b,c,d,a,k[10],23,-1094730640);a=hh(a,b,c,d,k[13],4,681279174);d=hh(d,a,b,c,k[0],11,-358537222);c=hh(c,d,a,b,k[3],16,-722521979);b=hh(b,c,d,a,k[6],23,76029189);a=hh(a,b,c,d,k[9],4,-640364487);d=hh(d,a,b,c,k[12],11,-421815835);c=hh(c,d,a,b,k[15],16,530742520);b=hh(b,c,d,a,k[2],23,-995338651);a=ii(a,b,c,d,k[0],6,-198630844);d=ii(d,a,b,c,k[7],10,1126891415);c=ii(c,d,a,b,k[14],15,-1416354905);b=ii(b,c,d,a,k[5],21,-57434055);a=ii(a,b,c,d,k[12],6,1700485571);d=ii(d,a,b,c,k[3],10,-1894986606);c=ii(c,d,a,b,k[10],15,-1051523);b=ii(b,c,d,a,k[1],21,-2054922799);a=ii(a,b,c,d,k[8],6,1873313359);d=ii(d,a,b,c,k[15],10,-30611744);c=ii(c,d,a,b,k[6],15,-1560198380);b=ii(b,c,d,a,k[13],21,1309151649);a=ii(a,b,c,d,k[4],6,-145523070);d=ii(d,a,b,c,k[11],10,-1120210379);c=ii(c,d,a,b,k[2],15,718787259);b=ii(b,c,d,a,k[9],21,-343485551);x[0]=add32(a,x[0]);x[1]=add32(b,x[1]);x[2]=add32(c,x[2]);x[3]=add32(d,x[3]);}
  function cmn(q,a,b,x,s,t){a=add32(add32(a,q),add32(x,t));return add32((a<<s)|(a>>>(32-s)),b);} function ff(a,b,c,d,x,s,t){return cmn((b&c)|((~b)&d),a,b,x,s,t);} function gg(a,b,c,d,x,s,t){return cmn((b&d)|(c&(~d)),a,b,x,s,t);} function hh(a,b,c,d,x,s,t){return cmn(b^c^d,a,b,x,s,t);} function ii(a,b,c,d,x,s,t){return cmn(c^(b|(~d)),a,b,x,s,t);} function md5blk(s){const md5blks=[];for(let i=0;i<64;i+=4){md5blks[i>>2]=s.charCodeAt(i)+(s.charCodeAt(i+1)<<8)+(s.charCodeAt(i+2)<<16)+(s.charCodeAt(i+3)<<24);}return md5blks;} function add32(a,b){return (a+b)&0xFFFFFFFF;} function rhex(n){const s='0123456789abcdef';let str='';for(let j=0;j<4;j++){str+=s.charAt((n>>(j*8+4))&0x0F)+s.charAt((n>>(j*8))&0x0F);}return str;}
  const MD5 = (s) => { let i,n=s.length*8; s=s.replace(/\r\n/g,'\n'); const state=[1732584193,-271733879,-1732584194,271733878]; for(i=64;i<=s.length;i+=64){md5cycle(state,md5blk(s.substring(i-64,i)));} s=s.substring(i-64); const tail=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]; for(i=0;i<s.length;i++)tail[i>>2]|=s.charCodeAt(i)<<((i%4)<<3); tail[i>>2]|=0x80<<((i%4)<<3); if(i>55){md5cycle(state,tail);for(i=0;i<16;i++)tail[i]=0;} tail[14]=n; md5cycle(state,tail); return rhex(state[0])+rhex(state[1])+rhex(state[2])+rhex(state[3]); };

  const mixinKeyEncTab = [46,47,18,2,53,8,23,32,15,50,10,31,58,3,45,35,27,43,5,49,33,9,42,19,29,28,14,39,12,38,41,13,37,48,7,16,24,55,40,61,26,17,0,1,60,51,30,4,22,25,54,21,56,59,6,63,57,62,11,36,20,34,44,52];
  const nav = await (await fetch('https://api.bilibili.com/x/web-interface/nav', { credentials: 'include' })).json();
  const img = nav.data.wbi_img.img_url.split('/').pop().split('.')[0];
  const sub = nav.data.wbi_img.sub_url.split('/').pop().split('.')[0];
  const orig = img + sub;
  const mixin = mixinKeyEncTab.map(n => orig[n]).join('').slice(0, 32);

  async function getSub(bv) {
    const v = await (await fetch(`https://api.bilibili.com/x/web-interface/view?bvid=${bv}`, { credentials: 'include' })).json();
    if (v.code !== 0 || !v.data) return { has: false, err: 'view:' + v.code };
    const params = { aid: v.data.aid, cid: v.data.cid, wts: Math.round(Date.now() / 1000) };
    const q = Object.keys(params).sort().map(k => `${encodeURIComponent(k)}=${encodeURIComponent(String(params[k]).replace(/[!'()*]/g, ''))}`).join('&');
    const wid = MD5(q + mixin);
    const p = await (await fetch(`https://api.bilibili.com/x/player/wbi/v2?${q}&w_rid=${wid}`, { credentials: 'include' })).json();
    const list = (p.data && p.data.subtitle && p.data.subtitle.subtitles) || [];
    const zh = list.find(s => s.lan === 'ai-zh') || list.find(s => String(s.lan).startsWith('zh')) || null;
    return { has: !!(zh && zh.subtitle_url), lan: zh && zh.lan, url: zh && zh.subtitle_url ? 'https:' + zh.subtitle_url : null, dur: v.data.duration, aid: v.data.aid, cid: v.data.cid, lans: list.map(s => s.lan) };
  }

  window.__subs2 = window.__subs2 || {};
  const bvs = window.__bvs;
  const start = window.__cursor2 || 0;
  const end = Math.min(bvs.length, start + 20);
  let n = 0;
  for (let i = start; i < end; i++) {
    const bv = bvs[i];
    try { window.__subs2[bv] = await getSub(bv); n++; }
    catch (e) { window.__subs2[bv] = { has: false, err: String(e) }; }
    await new Promise(r => setTimeout(r, 250));
  }
  window.__cursor2 = end;
  const vals = Object.values(window.__subs2);
  return JSON.stringify({ start, end, total: bvs.length, scanned: vals.length, has: vals.filter(x => x.has).length });
})()
