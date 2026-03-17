// Bilibili 双语字幕插件 - 内容脚本

(function() {
    'use strict';

    const CONTAINER_ID = 'bilibili-subtitle-container';
    let subtitles = [];
    let currentSubtitleIndex = -1;
    let isEnabled = true;
    let initialized = false;
    let currentCid = null;
    let currentAid = null;

    // 等待页面加载完成后初始化
    function init() {
        if (initialized) return;
        initialized = true;

        console.log('[Bilibili Subtitle] Starting init...');

        // 等待页面基本加载后再检查
        setTimeout(() => {
            checkAndLoadSubtitles();
        }, 2000);
    }

    // 检查并加载字幕
    async function checkAndLoadSubtitles() {
        const video = document.querySelector('video');
        if (!video) {
            console.log('[Bilibili Subtitle] No video found, retrying...');
            setTimeout(checkAndLoadSubtitles, 2000);
            return;
        }

        console.log('[Bilibili Subtitle] Video found');

        // 获取当前分P的视频信息
        const videoInfo = await getVideoInfo();
        if (!videoInfo) {
            console.log('[Bilibili Subtitle] Cannot get video info, retrying...');
            setTimeout(checkAndLoadSubtitles, 2000);
            return;
        }

        console.log('[Bilibili Subtitle] Got video info:', videoInfo);

        // 检查是否需要重新加载字幕（切换分P时）
        if (currentCid !== videoInfo.cid) {
            console.log('[Bilibili Subtitle] CID changed, reloading subtitles');
            currentCid = videoInfo.cid;
            currentAid = videoInfo.aid;
            loadSubtitles(videoInfo.aid, videoInfo.cid);
        }
    }

    // 获取视频信息（AID和CID）
    async function getVideoInfo() {
        // 方法1: 从 __playinfo__ 获取当前播放的CID（这是最准确的方式）
        try {
            // 尝试从window中获取playInfo
            const keys = Object.keys(window).filter(k => k.includes('playinfo') || k.includes('playInfo'));
            for (const key of keys) {
                const playInfo = window[key];
                if (playInfo && playInfo.cid) {
                    console.log('[Bilibili Subtitle] Got CID from', key, ':', playInfo.cid);
                    // 尝试获取aid
                    let aid = playInfo.aid;
                    if (!aid) {
                        // 从URL获取
                        const info = await getAidFromApi();
                        aid = info?.aid;
                    }
                    if (aid && playInfo.cid) {
                        return { aid: aid, cid: playInfo.cid };
                    }
                }
            }
        } catch (e) {
            console.log('[Bilibili Subtitle] playinfo error:', e);
        }

        // 方法2: 从 __INITIAL_STATE__ 获取
        try {
            if (window.__INITIAL_STATE__) {
                const state = window.__INITIAL_STATE__;

                // 获取当前分P的cid
                let cid = null;
                let aid = null;

                // 从视频信息中获取
                if (state.videoInfo) {
                    aid = state.videoInfo.aid;
                    cid = state.videoInfo.cid;
                }

                // 如果有分P信息，获取当前分P的cid
                if (state.videoData && state.videoData.pages) {
                    const currentP = state.videoData.p;
                    const pages = state.videoData.pages;
                    if (pages && pages.length > 0) {
                        // 获取当前分P
                        const pageInfo = pages[currentP - 1] || pages[0];
                        cid = pageInfo.cid;
                        aid = aid || state.videoData.aid;
                    }
                }

                if (aid && cid) {
                    console.log('[Bilibili Subtitle] Got from __INITIAL_STATE__:', { aid, cid });
                    return { aid, cid };
                }
            }
        } catch (e) {
            console.log('[Bilibili Subtitle] __INITIAL_STATE__ error:', e);
        }

        // 方法3: 从URL参数获取当前分P并请求API
        return await getAidFromApi();
    }

    // 从API获取aid和cid
    async function getAidFromApi() {
        const bvidMatch = window.location.href.match(/BV[\w]+/);
        if (!bvidMatch) return null;

        // 获取当前分P
        const pMatch = window.location.href.match(/[?&]p=(\d+)/);
        const currentP = pMatch ? parseInt(pMatch[1]) : 1;

        try {
            console.log('[Bilibili Subtitle] Fetching from API with bvid:', bvidMatch[0], 'p:', currentP);
            const response = await fetch(`https://api.bilibili.com/x/web-interface/view?bvid=${bvidMatch[0]}`);
            const data = await response.json();

            if (data.code === 0 && data.data) {
                const pages = data.data.pages;
                // 获取当前分P的信息
                const pageInfo = pages[currentP - 1] || pages[0];
                console.log('[Bilibili Subtitle] Got from API:', {
                    aid: data.data.aid,
                    cid: pageInfo.cid,
                    p: currentP,
                    title: data.data.title
                });
                return {
                    aid: data.data.aid,
                    cid: pageInfo.cid
                };
            }
        } catch (e) {
            console.error('[Bilibili Subtitle] API error:', e);
        }

        return null;
    }

    // 加载字幕
    async function loadSubtitles(aid, cid) {
        if (!aid || !cid) {
            console.log('[Bilibili Subtitle] Invalid aid or cid');
            showNoSubtitleMessage('无法获取视频信息');
            return;
        }

        try {
            console.log('[Bilibili Subtitle] Loading subtitles for AID:', aid, 'CID:', cid);

            // 使用Bilibili API获取字幕列表
            const response = await fetch(`https://api.bilibili.com/x/player/wbi/v2?aid=${aid}&cid=${cid}`, {
                credentials: 'include',
                headers: {
                    'Referer': 'https://www.bilibili.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
            });
            const data = await response.json();

            console.log('[Bilibili Subtitle] API response:', data);

            if (data.code === 0 && data.data && data.data.subtitle) {
                const subtitleList = data.data.subtitle.subtitles;
                if (subtitleList && subtitleList.length > 0) {
                    console.log('[Bilibili Subtitle] Found subtitles:', subtitleList);
                    await downloadAndParseSubtitles(subtitleList);
                } else {
                    console.log('[Bilibili Subtitle] No subtitles available');
                    showNoSubtitleMessage('该视频没有字幕');
                }
            } else {
                console.log('[Bilibili Subtitle] API error:', data.message);
                showNoSubtitleMessage(data.message || '无法获取字幕');
            }
        } catch (e) {
            console.error('[Bilibili Subtitle] Failed to load subtitles:', e);
            showNoSubtitleMessage('加载字幕失败: ' + e.message);
        }
    }

    // 下载并解析字幕
    async function downloadAndParseSubtitles(subtitleList) {
        console.log('[Bilibili Subtitle] Processing subtitles:', subtitleList);

        // 优先获取中文和英文字幕
        const zhSub = subtitleList.find(s => s.lan === 'ai-zh' || s.lan.includes('zh'));
        const enSub = subtitleList.find(s => s.lan === 'en' || s.lan === 'english');

        console.log('[Bilibili Subtitle] Found zh:', zhSub, 'en:', enSub);

        const promises = [];
        if (zhSub) promises.push(downloadSubtitle(zhSub.subtitle_url, 'zh'));
        else promises.push(Promise.resolve(null));

        if (enSub) promises.push(downloadSubtitle(enSub.subtitle_url, 'en'));
        else promises.push(Promise.resolve(null));

        const results = await Promise.all(promises);
        const zhData = results[0];
        const enData = results[1];

        console.log('[Bilibili Subtitle] Downloaded zh:', zhData ? zhData.length : 0, 'en:', enData ? enData.length : 0);

        // 合并字幕
        if (zhData) {
            subtitles = mergeSubtitles(zhData, enData);
            console.log('[Bilibili Subtitle] Merged subtitles:', subtitles.length);
            createSubtitleContainer();
            startSubtitleSync();
        } else if (enData) {
            subtitles = enData.map(e => ({
                start: e.from,
                end: e.to,
                text: e.content
            }));
            createSubtitleContainer();
            startSubtitleSync();
        } else {
            showNoSubtitleMessage('无法解析字幕数据');
        }
    }

    // 下载单个字幕文件
    async function downloadSubtitle(url, lang) {
        try {
            const fullUrl = url.startsWith('http') ? url : 'https:' + url;
            console.log('[Bilibili Subtitle] Downloading subtitle from:', fullUrl);
            const response = await fetch(fullUrl);
            const data = await response.json();
            console.log('[Bilibili Subtitle] Downloaded', lang, 'subtitle, length:', data.body ? data.body.length : 0);
            return data.body || data;
        } catch (e) {
            console.error(`[Bilibili Subtitle] Failed to download ${lang} subtitle:`, e);
            return null;
        }
    }

    // 合并中英字幕
    function mergeSubtitles(zhData, enData) {
        if (!zhData) return [];

        return zhData.map((zhCue, index) => {
            // 尝试找到匹配的英文字幕
            let enCue = null;
            if (enData) {
                enCue = enData.find(e =>
                    Math.abs(e.from - zhCue.from) < 1 && Math.abs(e.to - zhCue.to) < 1
                );
            }

            let text = zhCue.content;
            if (enCue) {
                text = `${zhCue.content} | ${enCue.content}`;
            }

            return {
                start: zhCue.from,
                end: zhCue.to,
                text: text,
                zh: zhCue.content,
                en: enCue ? enCue.content : null
            };
        });
    }

    // 创建字幕容器
    function createSubtitleContainer() {
        // 移除已存在的容器
        const existing = document.getElementById(CONTAINER_ID);
        if (existing) {
            existing.remove();
        }

        const container = document.createElement('div');
        container.id = CONTAINER_ID;
        container.innerHTML = '<div class="subtitle-list"></div>';

        // 尝试找到视频容器
        const playerArea = document.querySelector('.bpx-player-primary');
        const videoContainer = document.querySelector('.bpx-player-container') ||
                              document.querySelector('.bilibili-player-video') ||
                              document.querySelector('#bilibiliPlayer') ||
                              playerArea;

        if (videoContainer) {
            // 找到播放器容器，尝试在其父元素添加
            const parent = videoContainer.parentElement;
            if (parent) {
                parent.style.position = 'relative';
                parent.appendChild(container);
                console.log('[Bilibili Subtitle] Container added to video parent');
            }
        }

        if (!document.getElementById(CONTAINER_ID)) {
            // 如果没添加成功，添加到body
            document.body.appendChild(container);
            console.log('[Bilibili Subtitle] Container added to body');
        }

        // 渲染字幕列表
        renderSubtitleList();

        // 添加拖动功能（拖动顶部把手）
        makeDraggable(container);
    }

    // 拖动功能
    function makeDraggable(el) {
        const handle = el;
        let isDragging = false;
        let startX, startY, startRight, startTop;

        handle.addEventListener('mousedown', function(e) {
            // 如果点击的是字幕项，不拖动
            if (e.target.classList.contains('subtitle-item')) return;

            // 如果鼠标在右下角resize区域，不拖动（让CSS resize处理）
            const rect = el.getBoundingClientRect();
            const resizeThreshold = 20; // resize区域大小
            const isInResizeArea = (
                e.clientX >= rect.right - resizeThreshold &&
                e.clientY >= rect.bottom - resizeThreshold
            );
            if (isInResizeArea) return;

            isDragging = true;
            startX = e.clientX;
            startY = e.clientY;

            // 获取当前 right 和 top 值
            const style = window.getComputedStyle(el);
            startRight = parseFloat(style.right) || 0;
            startTop = parseFloat(style.top) || 50;

            // 如果 top 是百分比，转换为像素
            if (style.top.includes('%')) {
                const parent = el.parentElement;
                if (parent) {
                    startTop = (parseFloat(style.top) / 100) * parent.clientHeight;
                }
            }

            el.style.transition = 'none';
            el.style.transform = 'none'; // 移除 transform 避免干扰
            e.preventDefault();
        });

        document.addEventListener('mousemove', function(e) {
            if (!isDragging) return;

            const dx = e.clientX - startX;
            const dy = e.clientY - startY;

            // 保持使用 right 和 top
            el.style.right = (startRight - dx) + 'px';
            el.style.top = (startTop + dy) + 'px';
        });

        document.addEventListener('mouseup', function() {
            isDragging = false;
            el.style.transition = '';
        });
    }

    // 渲染字幕列表
    function renderSubtitleList() {
        const listContainer = document.querySelector(`#${CONTAINER_ID} .subtitle-list`);
        if (!listContainer) {
            console.log('[Bilibili Subtitle] List container not found');
            return;
        }

        console.log('[Bilibili Subtitle] Rendering', subtitles.length, 'subtitles');

        listContainer.innerHTML = subtitles.map((sub, index) =>
            `<div class="subtitle-item" data-index="${index}">${escapeHtml(sub.text)}</div>`
        ).join('');

        console.log('[Bilibili Subtitle] Rendered subtitles');
    }

    // 开始字幕同步
    function startSubtitleSync() {
        const video = document.querySelector('video');
        if (!video) {
            console.log('[Bilibili Subtitle] No video for sync');
            return;
        }

        console.log('[Bilibili Subtitle] Starting subtitle sync');

        const updateSubtitle = () => {
            if (!isEnabled || subtitles.length === 0) return;

            const currentTime = video.currentTime;
            const index = findSubtitleIndex(currentTime);

            if (index !== currentSubtitleIndex) {
                currentSubtitleIndex = index;
                highlightCurrentSubtitle(index);
            }
        };

        video.addEventListener('timeupdate', updateSubtitle);
        video.addEventListener('play', updateSubtitle);

        // 初始更新
        updateSubtitle();
    }

    // 查找当前时间对应的字幕索引
    function findSubtitleIndex(time) {
        for (let i = 0; i < subtitles.length; i++) {
            if (time >= subtitles[i].start && time <= subtitles[i].end) {
                return i;
            }
        }
        return -1;
    }

    // 高亮当前字幕并滚动到中央
    function highlightCurrentSubtitle(index) {
        const items = document.querySelectorAll(`#${CONTAINER_ID} .subtitle-item`);
        const container = document.querySelector(`#${CONTAINER_ID} .subtitle-list`);

        items.forEach((item, i) => {
            item.classList.toggle('active', i === index);
        });

        if (index >= 0 && items[index] && container) {
            // 滚动到中央
            const containerHeight = container.clientHeight;
            const itemTop = items[index].offsetTop;
            const itemHeight = items[index].clientHeight;

            container.scrollTo({
                top: itemTop - containerHeight / 2 + itemHeight / 2,
                behavior: 'smooth'
            });
        }
    }

    // 显示消息
    function showNoSubtitleMessage(msg) {
        console.log('[Bilibili Subtitle] Showing message:', msg);

        // 移除已存在的容器
        const existing = document.getElementById(CONTAINER_ID);
        if (existing) {
            existing.remove();
        }

        const container = document.createElement('div');
        container.id = CONTAINER_ID;
        container.innerHTML = `<div class="no-subtitle">${msg}</div>`;

        // 尝试添加到页面
        const playerArea = document.querySelector('.bpx-player-primary');
        const videoContainer = document.querySelector('.bpx-player-container') ||
                              playerArea;

        if (videoContainer && videoContainer.parentElement) {
            videoContainer.parentElement.style.position = 'relative';
            videoContainer.parentElement.appendChild(container);
        } else {
            document.body.appendChild(container);
        }
    }

    // HTML转义
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // 启动
    init();
})();
