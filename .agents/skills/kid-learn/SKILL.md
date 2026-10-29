---
name: kid-learn
description: 幼小衔接每日学习台（语文奥特识字战/英语字母探险队/数学数字星球）。每次调用生成三科今日学习页（语文20复习+3新字、英语10复习+5新词、数学8-10题），并自动把学习结果合并回各科进度。用法：/kid-learn（生成三科今日页面并顺带合并昨日结果）；/kid-learn 语文|英语|数学（只生成单科）；/kid-learn 合并（仅合并，不生成页面）。
---

# 幼小衔接学习台 · kid-learn

<!-- Evolution: 2026-08-20 | source: ep-2026-08-20-001 | skill: kid-learn | reason: 结果误放 processed\ 导致合并被跳过、题目多日不变 -->
<!-- Evolution: 2026-08-20 | source: user-request + 浏览器验证 | skill: kid-learn | reason: 引入 hanzi-writer 笔顺书写动画，描红改为严格逐笔校验（用户确认：不设跳过） -->
<!-- Evolution: 2026-08-20 | source: user-request + 设计文档 | skill: kid-learn | reason: 新增英语/数学课程，模板参数化（语言/主题/字段泛化），生成器按科目独立 -->

给即将升小学的孩子（大班）使用的每日学习系统，三科各一页：

| 科目 | 主题 | 页面 | 生成器 |
|---|---|---|---|
| 语文 | 🦸 奥特识字战（橙） | `sessions\YYYY-MM-DD.html` | `tools\generate_session.js` |
| 英语 | 🦁 字母探险队（绿） | `sessions\YYYY-MM-DD-en.html` | `tools\generate_english.js` |
| 数学 | 🚀 数字星球（蓝） | `sessions\YYYY-MM-DD-math.html` | `tools\generate_math.js` |

## 路径

- 数据区根目录：`P:\AI\my-agent-skills\projects\幼小衔接\`
- 结果：`data\results\`（**家长把页面保存按钮下载的 `result-*.json` 手动放进来**，合并后归档到 `data\results\processed\`）
  - ⚠️ 结果文件**必须放 `data\results\` 根目录**，绝不能直接放进 `processed\`——合并程序只扫描根目录，误放会整份跳过，遗忘曲线不推进，导致每天题目不变。详见第 0 步。
- 模板：`templates\lesson-app.html`（三科通用学习台 UI，数据注入点：`<script id="lesson-data" type="application/json">{}</script>`；主题/语言由 `DATA.theme`/`DATA.lang` 驱动，渲染层科目无关）
- 战报 K.O. 特效：完成任务后的战报页顶部显示拳皇 97 风格「K.O.」主视觉（图 + 标题叠加压暗渐变）。每次结算从图池随机选一张：`KO_POOL` = `assets\ko97.svg` + `ko-alt-1..6.*`（在模板 `finish()` 前的数组里维护，新增图片需同步加进池子）；`THEME.koImage` 可指定固定图 / `''` 关闭 / 未设则随机
- 语文：字库 `data\char_library.json`、进度 `data\progress.json`、生成器 `tools\generate_session.js`
- 英语：词库 `data\english_library.json`、进度 `data\progress_english.json`、生成器 `tools\generate_english.js`
- 数学：知识点 `data\math_curriculum.json`、进度 `data\progress_math.json`、生成器 `tools\generate_math.js`
- 笔顺动画引擎：`vendor\hanzi-writer.min.js`（离线库，37KB）+ 矢量数据 `data\stroke_data.js`（`window.STROKE_DATA`，413字全覆盖，~900KB，语文专用）
- 输出：`sessions\YYYY-MM-DD.html` / `-en.html` / `-math.html`
- 周报：`data\subjects_progress.md`

**笔顺动画说明**：learn 学习卡与 trace 描红用 hanzi-writer 渲染。模板通过 `../data/stroke_data.js` + `../vendor/hanzi-writer.min.js` 相对路径引入（页面在 sessions/ 下，`file://` 与 `http://localhost` 均可用）。描红为**严格逐笔校验**：先循环演示笔顺，点「开始写！」进入 quiz，每笔写对才进下一笔、写错提示重写、无跳过按钮，全部写完自动过关。若新增字不在字库，运行 `node tools/build_stroke_data.js` 重建数据——该脚本在 `node_modules\hanzi-writer-data` 字库缺失时**首次运行自动下载**（npm registry tgz 解压到仓库内该目录，已 .gitignore 不入库，之后常驻复用）。

## 每日流程（每次调用都执行）

### 第 0 步：合并历史结果（自动）

**结果文件从哪来**：页面「保存结果」按钮用浏览器下载 `result-YYYY-MM-DD-{subject}.json`（chinese/en/math 后缀）到**系统下载目录**，家长需要手动把它移动到 `data\results\` **根目录**（不是 `processed\`）。保存流程没有自动化，Claude 只负责读取+合并。

1. 读取 `data\results\` 下所有 `result-*.json`（排除 `processed\`）。
2. 逐个按「结果合并规范」按内容 `subject` 字段路由合并进对应科目进度（`progress.json` / `progress_english.json` / `progress_math.json`）。
3. 合并后把文件移动到 `data\results\processed\`。
4. 若本次合并了任何结果，向家长打印一句摘要（三科分开），例如：
   `📊 已合并 8/19 结果：语文复习20字错2个（天、地）、新字3个（王、全、主）；英语复习10词错1个（cat）；数学8题错2题（已入错题队列）。`
   合并发生在生成新页面之前——先消化昨天的数据，遗忘曲线才准确。
5. **误放检查**：若 `data\results\processed\` 里有 `result-*.json`，且对应科目进度的 `stats` 未更新（如 `total_reviews` 仍是旧值），说明结果被误放进了 `processed\` 被跳过——先把文件**移回 `data\results\` 根目录**再重新合并，并向家长说明为何要放根目录。此问题典型症状：**连续几天题目一模一样**。

### 第 1 步：读取数据

- 读取 `progress.json` 与 `char_library.json`。若 `progress.json` 不存在，先运行初始化：
  `node "P:\AI\my-agent-skills\projects\幼小衔接\tools\init_progress.js"`（以及 `build_library.js`）。

### 第 2 步：计算今日任务

**复习集（20字）**：从已学字中选出所有 `due_date <= 今天` 的字，按以下优先级排序，取前 20：

1. `due_date` 升序（越逾期越优先）
2. `last_result` 为 `wrong` 或 `null` 的排在 `correct` 前
3. 字库索引（order）升序（同优先级取更基础的字）

**新字（3个）**：取 `progress.chars` 中 `status == "new"` 的字，按字库顺序取前 3 个。

### 第 3 步：生成今日页面

**首选：运行确定性生成器**（推荐，结果可复现、可验证）。默认三科全部生成；`/kid-learn 语文|英语|数学` 只生成指定科：

```powershell
node "P:\AI\my-agent-skills\projects\幼小衔接\tools\generate_session.js" --date YYYY-MM-DD   # 语文
node "P:\AI\my-agent-skills\projects\幼小衔接\tools\generate_english.js" --date YYYY-MM-DD   # 英语
node "P:\AI\my-agent-skills\projects\幼小衔接\tools\generate_math.js" --date YYYY-MM-DD      # 数学
```

- **语文**：遗忘曲线选字、题型配额（14识字+3同音相似+2拼音+1发音）、干扰项取自已学字库、新字学习卡+巩固题+描红+跟读。
- **英语**：遗忘曲线选词（10 复习 + 5 新词，字母阶段前 6 天学完 26 字母）、听音/看图/选义题型轮换、干扰项同类别优先、新词学习卡+巩固+跟读（en-US 语音）。
- **数学**：错题重做（wrong_queue 前 3 道）→ 当前知识点学习卡（首次）→ 5 题 → 已学滚动 2 题；加减法算法化随机出题，干扰项为答案 ±1~3；知识点线性推进（当日全对 → 次日推进）。

每个生成器都顺带合并自己科目的历史结果。生成完打印复习/新学清单。

**兜底（生成器报错或需个性化时）**：按「题目生成规范」手工构建 `steps`：

1. 复习在前、新字在后，复习环节绝不可跳过。
2. 组装 lesson-data JSON：`{ date, subject: "chinese"|"english"|"math", title, steps, theme? }`（英语/数学需带 `theme`，见各生成器内 THEME 常量；语文不带动主题时模板回退默认奥特曼）。
3. 读模板 `templates\lesson-app.html`，把 `<script id="lesson-data" type="application/json">{}</script>` 中的 `{}` 替换为组装好的 JSON（`JSON.stringify` 并转义 `<`/`>` 为 `\u003c`/`\u003e`）。
4. 写入 `sessions\YYYY-MM-DD.html`（语文）/ `-en.html`（英语）/ `-math.html`（数学）。
5. 向家长汇报：三科今日内容，并**直接启动本地 HTTP 服务 + Chrome 打开三个标签页**（用户偏好，见下）。

**页面打开方式（默认）**：生成后默认通过本地 HTTP 服务访问，因为 `file://` 下语音识别不可用（降级为家长判断），`http://localhost` 下语音识别可用。

```powershell
# 1) 在数据区根目录起服务（后台运行）
python -m http.server 8000 --directory "P:\AI\my-agent-skills\projects\幼小衔接"
# 2) 用 Chrome 打开（三科三个标签页）
Start-Process chrome.exe -ArgumentList '"http://localhost:8000/sessions/YYYY-MM-DD.html","http://localhost:8000/sessions/YYYY-MM-DD-en.html","http://localhost:8000/sessions/YYYY-MM-DD-math.html"'
```

### 第 4 步（可选）：`/kid-learn 合并`

只执行第 0 步（三科结果都合并），不生成页面。

## 遗忘曲线规则

每个字在 `progress.json` 中：

```json
{
  "日": {
    "status": "review",          // new | review | mastered
    "interval_days": 1,
    "due_date": "2026-08-19",
    "reviews": 0,
    "consecutive_correct": 0,
    "last_result": null          // null | correct | wrong
  }
}
```

间隔阶梯：`[1, 3, 7, 15, 30, 60]`。

- **答对** → `interval_days` 移到下一级；`due_date = 今天 + interval_days`；`consecutive_correct++`。
- **答错** → `interval_days` 重置为 1；`due_date = 明天`；`consecutive_correct = 0`。
- `status == "mastered"`：间隔到 60 且连续答对 ≥ 3 次 → 升级为 mastered，`interval_days` 保持 60（几乎不占用每日名额）。
- `interval_days` 已到 60 且答错 → 降回 review，间隔重置 1。

## 题目生成规范

目标：20 个复习字 → 20 题（14 识字选择 + 3 同音/相似 + 2 拼音 + 1 发音跟读）。题型在 20 字间尽量轮换，不重复。**所有干扰项必须来自已学字库**（不超纲）。

### 复习选择题（choice，phase: "review"）

| 模式 mode | big 显示 | options 内容 | prompt 示例 |
|---|---|---|---|
| `pick_char` | 拼音 | 4 个字 | 哪个字读 rì，能组成「日出」？ |
| `pick_word` | 字 | 4 个词（仅1个含目标字） | 哪个词里有「日」？ |
| `pick_pinyin` | 字 | 4 个拼音 | 「日」的拼音是哪个？ |
| `pick_similar` | 字 | 4 个字（1个与目标形近） | 哪个字和「日」长得像？ |
| `pick_homophone` | 字 | 4 个字（1个与目标同音） | 哪个字和「越」读音一样？ |

**干扰项选取规则**（核心质量要求）：
- 从 `status != "new"` 的已学字中选，绝不能把目标字本字放进干扰项。
- `pick_char`：优先选 1 个同 `phonetic_group` 的字、1 个 `similar` 里的字、1 个随机已学字。
- `pick_word`：其他 3 个词取自另外 3 个已学字的 `words`，保证词里都不含目标字；且 3 个干扰词**全体不能有共同字符**（防「一千/千万/千秋」「火车/灯火/大火」扎堆——干扰项共有某个字而答案没有时，孩子按“另类”即可蒙对，2026-08-20 修复）。
- `pick_homophone`：先看目标字 `phonetic_group` 在库中是否还有别的字（如 月/越）；有则用，无则改用其它模式。
- `pick_similar`：目标字 `similar` 非空才用此模式；干扰项为不相似的字。
- 每个 choice 步骤都带上 `words: [目标字的前3个词]`（页面展示组词联想）。
- 若某个字无同音兄弟也无相似字，就不给它分同音/相似题，配额让给有条件的字。

**同音/相似题配额**：3 题里优先分配给「库中确有同音兄弟或形近字」的复习字；若当天复习集里凑不足 3 个，允许复用其他复习字并换成 pick_char。

**拼音题配额**：2 题，用 `pick_pinyin`。

**发音跟读**：1 题，`kind: "pronounce"`，`text` 为目标字（或一个含它的词），`phonetic` 为拼音。

### 新字学习步骤（每新字一套，phase: "new"）

按顺序生成：

1. `learn` 学习卡：`char`、`pinyin`、`words`（≥3）、`strokes`（笔顺序列，形如 `["横","横","竖","横"]`）。
2. `choice`（`pick_char`）：big 显示拼音选字。
3. `choice`（`pick_word`）：选含该字的词。
4. `choice`（`pick_pinyin`）：选该字的拼音。
5. `trace` 描红：`char` + `stroke_count`。
6. `pronounce` 跟读：读该字或一个组词。

**笔顺数据**：新字在库中的 `strokes` 为空时，由你补全并**同时写回 `char_library.json`** 对应条目的 `strokes` 与 `stroke_count`（一次性丰富字库）。笔顺名称用标准称谓：横、竖、撇、捺、点、横折、横撇、竖钩、弯钩、竖折、撇点、提、横钩、卧钩、斜钩、竖弯钩、横折钩、横折弯钩、竖折折钩、横折提。

### 章节与主题（steps 结构）

```json
{ "kind":"section", "label":"复习 · 怪兽军团", "subtitle":"20 只怪兽等你消灭！", "emoji":"👾" }
{ "kind":"section", "label":"新技能解锁", "subtitle":"学 3 个新字", "emoji":"🦸" }
{ "kind":"section", "label":"最终决战", "subtitle":"3 字混战", "emoji":"⚡" }
```

最终决战：从 3 个新字中抽 3 道混合 choice（phase 仍为 "new"，不计入复习结果）。

### 页面数据 schema（必须与模板一致）

```json
{
  "date": "2026-08-19",
  "subject": "chinese",
  "title": "奥特识字战 · 8月19日",
  "steps": [ ... ]
}
```

- choice：`{ kind, char, phase, mode, big, big_tag?, prompt, options[], answer, words[]?, phonetic? }`
- pronounce：`{ kind, char, phase, phonetic, text, prompt? }`
- trace：`{ kind, char, phase, stroke_count, phonetic? }`
- learn：`{ kind, char, phase:"new", pinyin, words[], strokes[] }`
- section：`{ kind, label, subtitle?, emoji? }`

## 结果合并规范

**路由**：三个生成器的合并器都扫描 `data\results\` 根目录所有 `result-*.json`，按文件**内容里的 `subject` 字段**路由到各自科目（英语只合并 `subject:"english"`，依此类推），合并后移入 `processed\`。文件名带科目后缀由模板生成，但路由只看内容、与文件名无关。

页面写回的结果结构（模板统一输出：复习元素键 `id`、新学字段 `new_items`；语文合并器兼容旧 `char`/`new_chars` 键）：

```json
{
  "date": "2026-08-19",
  "subject": "chinese",              // chinese | english | math
  "review": [ { "id": "天", "correct": true, "tries": 1,
                "step": { "big": "...", "prompt": "...", "options": ["..."], "answer": 0 } } ],
  "new_items": ["王", "全", "主"],
  "stats": { "stars": 35, "combo_max": 8, "correct": 18, "total": 21 }
}
```

- `review[].step`：选择题题干明细，数学错题队列靠它存题重放；语文/英语合并器忽略。
- 数学题 id 带序号（如 `add10#3`），合并器按 `#` 前缀聚合到知识点；同知识点多题时语文式聚合（全对才算对）**不适用**——每题独立判断。

合并步骤（语文）：

1. **review 每字**：按遗忘曲线规则更新该字状态（答对进级、答错重置）。
2. **new_items**：把库中对应字标为已学——`progress.chars[char].status = "review"`、`interval_days = 1`、`due_date = 明天`、`reviews +1`；同时更新 `curriculum_index` 为最新已引入位置（库中第一个仍为 new 的索引）。
3. **统计**：`stats.total_reviews += review.length`、`stats.total_new += new_items.length`、`stats.total_stars += stats.stars`、`stats.sessions_done++`、`updated = 今天`。
4. **日志**：向 `logs` 追加 `{ date, reviewed: [字], new: [字], wrong: [错的字] }`。
5. **周报**：在 `data\subjects_progress.md` 追加当日一行（日期、复习数、错字、新字、星星），并刷新本周汇总。

**英语差异**：遗忘曲线与语文完全一致，按词 `id` 更新 `progress_english.json` 的 `items`；`curriculum_index` 推进到第一个仍为 `new` 的词。首日无已学词时复习 0 题、干扰项从同类别未学词补（字母互相做干扰是合理的）。

**数学差异**（`progress_math.json`，不用遗忘曲线）：

- 每题独立记录 → 按知识点聚合：全对 → `streak++`；有错 → `streak = 0`，且错题（含题干）进 `wrong_queue`（去重，最多 10 道，`shift` 淘汰最旧）。
- 错题重做答对（id 匹配队列条目）→ 从 `wrong_queue` 移除。
- `curriculum_index`：当日当前知识点全对 → 推进一格；综合挑战知识点不推进。
- 学习卡计入 `new_items`（对应新知识点，合并进 `learned`）。

## 质量要求

- 复习环节顺序在 steps 数组里必须在最前，页面没有跳过按钮，**当日先复习、再学新字**。
- 所有题干、干扰项、组词对孩子友好，不出现生僻词或成人词汇。
- 同一天内同一字不重复出现两个 review 题。
- 生成的页面必须能在 Chrome 直接打开跑通（模板已验证）。
- 保留已生成的历史页面（`sessions\`），不要覆盖已合并过结果的当天页面以外的文件。
