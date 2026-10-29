# CODEBUDDY.md 本文件为 CodeBuddy 在此仓库中处理代码时提供指引。

## 本仓库是什么

这是一个个人的 **AI-agent「技能」仓库**，而非传统应用程序。其核心内容是一组 **技能**（`.claude/skills/*`）：每个技能都是这样一个文件夹——其中的 `SKILL.md` 教会 agent 如何完成一项可重复任务，外加该技能依赖的 Python/Node 脚本、参考资料与评测（evals）。技能通过在 agent 中调用（例如 `/video-summarizer`、`/kid-learn`、`/income-expenditure-analysis`）或在对话中按名称引用来使用。

这里没有构建系统、测试运行器或 lint 配置。本仓库的「开发闭环」是：编写/修改某个技能的 `SKILL.md` 及其 `scripts/`，然后运行该技能的具体命令工作流来验证它。请把下文中的可执行示例当作本仓库等同于 build/test 命令的东西。

## 环境（Windows —— 运行任何命令前请先阅读）

- 操作系统为 Windows；shell 是 PowerShell。脚本引用 Windows 路径和 PowerShell 语法。
- **Python**：多个技能工作流需要真实的解释器，因为 `uv run python` 可能报「No Python」失败。可选用其一：
  - `C:\Users\chandlernie\AppData\Local\Programs\Python\Python313\python.exe`（整个 `video-summarizer` 技能中都简称为 `python313`）
  - 仓库虚拟环境：`.\venv\Scripts\python.exe`（装有 `yt_dlp`、`requests`、`anthropic`、`faster-whisper`、`openpyxl`、`cryptography`；`venv/` 已被 gitignore）。
- 打印中文的脚本请设置 `PYTHONIOENCODING=utf-8` / `PYTHONUTF8=1`；控制台输出可能乱码，但 Python 能正确读取 UTF-8 文件。
- **路径**：为避免 Windows 反斜杠转义问题，请使用正斜杠或双引号。
- **Bilibili cookies** 位于 `downloads/bilibili/bilibili-cookies*.txt`（Netscape 格式；出于安全，`bilibili-cookies.txt` 已被 gitignore）。它们会定期过期——当字幕下载失败时需从浏览器重新导出。
- Git：仓库为 `git@github.com:codeHardest/my-agent-skills.git`，分支 `master`。媒体文件和 venv 已被 gitignore，但 `downloads/` 下的字幕文本/摘要/目录（catalogs）会被跟踪。

## 命令与验证工作流（按领域分）

### 一般性地编辑技能
技能遵循 `CLAUDE.md` 中的格式：一个文件夹，其 `SKILL.md` 带 YAML frontmatter，包含必需的 `name`（小写、连字符分隔）和 `description`（agent 应在何时使用该技能）。当修改某个技能的脚本或行为时，也要同步更新其 `SKILL.md`。技能规范参考：https://agentskills.io/specification。

### video-summarizer 技能
工作流位于 `.claude/skills/video-summarizer/`。输出写入 `./downloads/<website>/<video_id>/`（B 站为 `downloads/bilibili/BVxxx/`）。每个视频的文件固定为 `subtitle_ai-zh.json`、`subtitle.vtt`、`transcript.txt`、`summary.md`；每条生成的摘要都会追加到 `downloads/bilibili/catalog.md`（按发布日期排序，而非下载日期）。

```
# 创建每个视频的目录（BVID = 12 位 B 站 id）
mkdir -p ./downloads/bilibili/BV1qv6eBZErD

# 抓取两条 AI 字幕（AID/CID 来自 bilibili view API，经 yt-dlp --dump-json 获得）
& python313 .claude/skills/video-summarizer/scripts/get_bilibili_subtitle.py <AID> <CID> ./downloads/bilibili/BV1qv6eBZErD/ ./downloads/bilibili/bilibili-cookies.txt

# 将 JSON 字幕转换为 subtitle.vtt + transcript.txt
& python313 .claude/skills/video-summarizer/scripts/convert_subtitle.py ./downloads/bilibili/BV1qv6eBZErD/subtitle_ai-zh.json ./downloads/bilibili/BV1qv6eBZErD/

# 若无字幕：先抽取音频再转写
& python313 -m yt_dlp -x --audio-format mp3 -o "./downloads/bilibili/BV1qv6eBZErD/audio.%(ext)s" <URL>
& python313 .claude/skills/video-summarizer/scripts/parallel_transcribe.py --input ./downloads/bilibili/BV1qv6eBZErD/audio.mp3 --output-dir ./downloads/bilibili/BV1qv6eBZErD/ --model small

# 生成 AI 摘要（--pubdate 传视频发布日期，而非下载日期）
& python313 .claude/skills/video-summarizer/scripts/generate_summary.py ./downloads/bilibili/BV1qv6eBZErD/transcript.txt ./downloads/bilibili/BV1qv6eBZErD/summary.md --title "<标题>" --url "https://www.bilibili.com/video/BV1qv6eBZErD" --duration <秒> --pubdate YYYY-MM-DD

# 登记到 catalog（对已收录的视频不要重跑；改为手动编辑那一行）
& python313 .claude/skills/video-summarizer/scripts/update_catalog.py ./downloads/bilibili/BV1qv6eBZErD/summary.md ./downloads/bilibili/catalog.md

# 查看任一脚本的选项
& python313 .claude/skills/video-summarizer/scripts/generate_summary.py --help
```

技能中记录的关键坑：`generate_summary.py` 绝不能硬编码模型 ID——它先读环境变量 `ANTHROPIC_MODEL`，再回退到 `deepseek-v4-flash` / `deepseek-v4-pro`（网关会以 401 拒绝 `claude-*` ID，而某些已配置模型会返回空 400）。当存在 `CLAUDE_CODE_SESSION_ID` 时它从中读取 `x-opencode-session`，否则网关返回 400 `MissingSessionID`。当摘要被截断时它会逐级调大 `max_tokens`（4096→8192→16384→32768）（需确认摘要确实结束在一个真实章节上，而不是一个孤零零的数字）。每个视频只运行一次 `update_catalog.py`——它没有去重。

### income-expenditure-analysis 技能
核心逻辑：真实的银行/微信/支付宝流水在消费发生点（微信/支付宝，显示商户名）和结算点（银行，显示为「财付通/支付宝/信用卡还款」）都有同一条消费记录。只在发生点统计一次消费；剔除银行的结算行。在某个原始流水文件夹上运行参数化的参考实现：

```
# 分析 + 全部交付报表，输出写入 <dir>/output/（绝不写进技能文件夹）
FAMILY_TRANSFER_KEY=<key> PYTHONUTF8=1 py -3.13 .claude/skills/income-expenditure-analysis/scripts/analyze_expenses.py --input-dir "P:/AI/my-agent-skills/projects/income-expenditure-analysis"

# 重新生成用于冒烟测试的合成夹具数据
py -3.13 .claude/skills/income-expenditure-analysis/evals/make_fixtures.py
```

该技能要求分析*在包含源流水的文件夹内*运行并在那里输出（`<源目录>/output/`）；技能自身文件夹是只读参考。分类关键词位于 `references/category-rules.md`（含优先级表），解析配方与陷阱位于 `references/source-parsing.md`。敏感清单（如家庭转账姓名、`transfers_family.enc`）与部分规则在 `SKILL.md` 及脚本配置中做了 base64 混淆；用 `...analyze_expenses.py --decode` 解码。在归类前，各来源的预期分类总计必须对照每个文件自身的页脚合计进行人工核对。

### kid-learn 技能（projects/幼小衔接/）
一个面向学龄前儿童的每日中文/英文/数学学习应用。数据区根目录为 `projects/幼小衔接/`（Node.js 生成器把 HTML 写入 `sessions/`；个人进度文件已被 gitignore）。每日流程：先合并昨天的 `result-*.json` 文件，再生成今天的三个科目页面。

```
# 生成某个科目的页面（chinese / english / math）；每个生成器也会合并自己的结果
node "P:\AI\my-agent-skills\projects\幼小衔接\tools\generate_session.js" --date YYYY-MM-DD
node "P:\AI\my-agent-skills\projects\幼小衔接\tools\generate_math.js" --date YYYY-MM-DD

# 首次初始化汉字库 / 进度状态
node "P:\AI\my-agent-skills\projects\幼小衔接\tools\build_library.js"
node "P:\AI\my-agent-skills\projects\幼小衔接\tools\init_progress.js"

# 向字库新增汉字后重建笔画矢量数据
node "P:\AI\my-agent-skills\projects\幼小衔接\tools\build_stroke_data.js"

# 验证模板 / 主题（快速健全性检查）
node "P:\AI\my-agent-skills\projects\幼小衔接\tools\test_template.js"
node "P:\AI\my-agent-skills\projects\幼小衔接\tools\check_template.js"

# 提供服务页面以便 Web Speech 识别可用（file:// 会禁用），再在 Chrome 打开
python -m http.server 8000 --directory "P:\AI\my-agent-skills\projects\幼小衔接"
Start-Process chrome.exe -ArgumentList 'http://localhost:8000/sessions/YYYY-MM-DD.html'
```

`data/` 布局与遗忘曲线规则记录在 `.claude/skills/kid-learn/SKILL.md` 中。关键运维规则：结果 JSON 文件必须放在 `data/results/`（根目录，绝不能放进 `data/results/processed/`），否则合并会被静默跳过，导致次日题目完全重复。

### bilibili-plugin（projects/bilibili-plugin/）
一个 Manifest V3 Chrome 扩展（文件：`manifest.json`、`content.js`、`styles.css`），在视频旁显示一个可拖拽、可调整大小、50% 透明、30 行的双语滚动字幕框。无构建步骤——编辑文件后，在 Chrome 中加载未打包的 `plugin/bilibili` 文件夹（`chrome://extensions/` → 开发者模式 →「加载已解压的扩展程序」）。针对某个 B 站视频 URL 测试；在控制台中查看以 `[Bilibili Subtitle]` 为前缀的日志。它从 `https://api.bilibili.com/x/player/wbi/v2?aid=...&cid=...` 拉取字幕；注意：多 P（分P）视频必须使用当前分P的 CID（已知 bug 是 P2 会显示 P1 的字幕）。

## 架构总览

本仓库围绕三个角色组织：技能（可复用能力）、downloads（技能产出的数据）和 projects（由技能驱动的真实用户工作）。理解各类内容位于何处、以及同一技能如何被多个地方引用，是需要最多文件阅读的「大局」。

### 1. 技能树 —— 自研 vs 镜像 vs 已安装

这里唯一的技能*编写*位置是面向 Claude Code 使用的 `.claude/skills/`，以及 `.agents/skills/` 下适配 CodeBuddy 的副本。对比二者：`.claude/skills/` 与 `.agents/skills/` 当前都含 `book-to-skill`、`hallmark`、`youdaonote`，但 `.claude/skills/` 树的条目要多得多。把 `.claude/skills/` 当作你拥有技能的正式工作副本，`.agents/skills/` 当作面向你要支持的某个 agent 前端而保持同步的镜像——当你新增一个本地自研技能时，可能需要在两处都添加，两个 agent 才能加载它。

在 `.claude/skills/` 内部，要区分第三方安装的技能与本地自研的技能。`skills-lock.json` 将每个*下载*的技能映射到其上源（多为 GitHub，例如 `anthropics/skills` 对应 `docx`/`pdf`/`pptx`/`xlsx`/`mcp-builder`/`skill-creator`，`vercel-labs/skills` 对应 `find-skills`，`nutlope/hallmark` 对应 `hallmark`，`virgiliojr94/book-to-skill`，以及本地临时安装的 `youdaonote`）。凡是不在 `skills-lock.json` 中的都是本地自研、需要你维护的：`video-summarizer`、`income-expenditure-analysis`、`cb-forecasting`、`graham-intelligent-investor`、`kid-learn`。技能大致按领域分组：
- **文档/办公生成**（已下载）：`docx`、`pdf`、`pptx`、`xlsx`，外加 `skill-creator`（用于技能的创作/评测的元技能）、`find-skills`、`mcp-builder`、`hallmark`、`book-to-skill`、`youdaonote`。
- **媒体/学习管线**（本地自研）：`video-summarizer`。
- **个人财务 / 投资知识**（本地自研）：`income-expenditure-analysis`、`cb-forecasting`、`graham-intelligent-investor`。
- **儿童学习应用**（本地自研）：`kid-learn`。

每个本地自研技能都有相似的内部分层，切勿与之对抗：`SKILL.md`（面向 agent 的说明，含触发描述 + 工作流 + 已记录的报错处理）、`scripts/`（具体的参考实现或生成器）、`references/`（解析配方、分类规则、各平台方法文档）、`evals/`（JSON 评测元数据，以及在适用时的 `make_fixtures.py` 用来重新生成合成输入文件），偶尔还有机密/辅助文件（如 `transfers_family.enc`）。部分技能会在 `SKILL.md` 底部以 HTML 注释追加不断演进的评论（`<!-- Evolution: date | source | skill | reason -->`），描述真实运行中习得的模式——务必阅读这些注释，它们编码了来之不易的运维规则（模型回退链、网关请求头、catalog 去重警告）。

### 2. 共享运行时与「downloads」输出约定

多个技能共享同一个概念上的输出约定，即使它们位于不同子文件夹：**总是把生成的产物保存到 `downloads/<source>/...` 下的按条目录**，原始形式与派生形式放在一起，并在每个 downloads 区顶部维护一个 `catalog.md` 索引。这并非偶然——下游用户会浏览这些目录，所以命名与排序规则很重要（B 站文件夹 = `BV{12 位}`；多 P = `BVxxx_p{N}`；摘要追加到 `catalog.md` 并按视频真实发布日期排序，这正是为何必须贯穿传递 `--pubdate`、也是为何重跑目录更新器会重复行）。

因此 `downloads/bilibili/` 与 `downloads/deeplearning-ai/` 树包含*被跟踪的*、由 `video-summarizer` 技能及其参考文档（`bilibili-method.md`、`deeplearning-ai-course-method.md`）生成的字幕文本、摘要和目录。DeepLearning.AI 课程工作流与 B 站不同：它访问 `https://platform-api.dlai.link/courses/{course-slug}` 获取课时元数据，以及 `.../videos/{数字 videoId}/caption.json` 获取字幕（用数字 id，而非课时 slug——用 slug 会得到 422）。课程输出遵循按课程划分的布局（`NN-slug.vtt`、`NNNNNNNN_summary.md`、`module-N-summary.md` 或 `course-summary.md`）。

### 3. 运行时环境耦合（Python + 工具）

这些技能在运行时以影响实际行为的方式与 Windows 绑定。规范解释器是 `python313`，即 `C:\Users\chandlernie\AppData\Local\Programs\Python\Python313\python.exe`（贯穿 `video-summarizer` 引用）。此外还有一个仓库级虚拟环境 `venv/`，脚本曾用它来装 `yt_dlp`、`requests`、`anthropic`、`faster-whisper`、`openpyxl`、`cryptography`。工作流所需的外部 CLI 工具：`yt-dlp`（下载 + 元数据）、`ffmpeg`（转码/抽取音频）、`faster-whisper`（转写兜底）、`uv`（依赖/驱动管理；避免使用 `uv run python`，它可能失败）。因为安装/运行命令已针对权限与路径故障反复打磨，技能文档及 `CLAUDE.md`/`.claude/settings.local.json` 中的确切调用才是事实来源——请照搬而非临时发挥新写法。

### 4.「projects」区及其作用

`projects/` 存放三个真实应用，每个都*是某个本地自研技能的具体应用*，且通常会重新实现或导入该技能的逻辑：
- `bilibili-plugin/`——`video-summarizer` 的 Chrome（Manifest V3）扩展伴侣，用于实时双语字幕观看；无构建步骤。
- `income-expenditure-analysis/`——经 `income-expenditure-analysis` 技能跑过的真实 2025 年流水集；其 `analyze_expenses.py` 项目脚本镜像了技能的参考脚本，`build_ledger.py` 以模块方式复用技能脚本，组装出一个自包含的交互式 HTML 账本。
- `幼小衔接/`——`kid-learn` 技能的实时数据区（字/词/数学库、各科进度 JSON、生成器 Node 脚本、`templates/lesson-app.html`、`sessions/`）。其中敏感的个人数据已被 gitignore。

不要把这些 projects 文件当作草稿：它们是进行中的技能驱动工作流的实际数据/来源，当对某个技能的参考实现做修改且存在对应项目脚本时，应与该脚本协调一致。

### 5. 根目录的草稿/笔记文件

`inbox.md`、`product.md` 与 `prompt.md` 是个人草稿笔记（功能想法、一份产品简报、一份旧的 bilibili-plugin 开发提示）。`video_info.json`、`youdaonote-skill-latest.zip`，以及 `income-expenditure-analysis.zip` / `video-summarizer.zip`（位于 `.claude/skills/` 下）是零散产物。它们不是架构；只有当任务提到它们时才去读。权威起点是 `CLAUDE.md`（技能格式规范）、每个技能的 `SKILL.md` 以及本文件。

## 值得牢记的非显性规则

- **不要随意重新生成/重跑那些「幂等但有状态」的步骤**——例如 `update_catalog.py` 没有去重；重新生成摘要后再跑它会新增一条重复的目录行。更倾向于编辑已有行。
- **绝不要把输出写进技能自身文件夹**（`income-expenditure-analysis` 明确禁止；其工作目录是用户源文件所在处）。
- **结果文件的放置位置至关重要**（`kid-learn` 中为 `data/results/` 根目录，而非 `processed/`）。
- **任何摘要生成脚本都不要硬编码模型 ID**；读取 `ANTHROPIC_MODEL` 并沿 `deepseek-v4-*` 回退，存在 `x-opencode-session` 时予以转发。
- **无论控制台是否乱码都要保证中文内容的 UTF-8 正确性**，并让 bilibili cookie 文件留在 git 之外。
- 从零新增技能时，遵循 `CLAUDE.md` 指向的格式/规范（frontmatter `name` + `description`，然后是正文），并把它加到应当加载它的那个(些) agent 树中；描述要具体到触发时机。
