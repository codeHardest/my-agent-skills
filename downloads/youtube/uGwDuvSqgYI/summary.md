# 视频摘要：Claude Cowork Fundamentals In 22 Minutes

## 基本信息
- **来源**: YouTube
- **URL**: https://www.youtube.com/watch?v=uGwDuvSqgYI
- **时长**: 1371秒 (约22分钟)
- **语言**: 英文
- **发布时间**: 2026-05-10
- **下载时间**: 2026-08-12 16:43:00

## 原始元数据
- **作者/UP主**: Tina Huang

## 输出文件
- video.mp4 - 原始视频文件
- audio.mp3 - 音频文件
- subtitle.vtt - 带时间戳的字幕文件
- subtitle_ai-zh.json - 原始AI字幕JSON
- transcript.txt - 纯文本转录
- summary.md - 本摘要文件

## 内容概述
本视频由Tina Huang主讲，系统介绍了Anthropic的本地AI代理产品Claude Cowork（字幕中多处被语音识别为Claude Colleague/Cohere/Cowerk/Coda等）的核心功能与实操方法。视频从基础安装、设置出发，逐步演示了文件整理、信用卡消费分析仪表板、品牌手册制作、技能（Skills）、连接器（Connectors）、插件（Plugins）、计划任务（Scheduled Tasks）以及项目（Projects）等高级功能，最后展示了如何将Claude Cowork与Claude Code结合，构建更复杂的软件应用。全程强调无需编程知识即可上手，并穿插了Manas（AI室内设计助手）的赞助演示。

## 核心要点
1. Claude Cowork属于“本地AI代理”（local AI agent）类别，可直接操作本地文件、应用和工具，比传统聊天机器人更强大。
2. 可通过 claude.com/products/colleague 下载安装，安装后拥有Chat、Colleague、Claude Code三个主要标签页。
3. 初始配置需要打开Capabilities中的Artifacts、AI-powered artifacts、Inline visualizations；Claude Code中可开启Dispatch（手机远程控制）、全局指令（Global Instructions）和Chrome集成。
4. 文件整理演示：Claude Cowork成功识别并整理了桌面376个文件，还发现了暴露的API密钥并建议安全删除，展示了它与普通聊天机器人的本质差异。
5. 信用卡分析演示：使用Opus模型分析24个月（2024-2026）的信用卡账单，通过多轮对话确定需求，生成本地HTML交互式仪表板，包含消费趋势、订阅、费用和兴趣洞察。
6. 品牌手册技能：从品牌资产截图生成PDF品牌手册，并将其转化为可复用的“技能”（Skill），之后通过“apply brand”指令即可将品牌风格应用到任意视觉产物。
7. 技能（Skills）可以自定义、从社区安装，也可以共享；常用技能包括Canvas Design、Doc Authoring、External Comms等。
8. 连接器（Connectors）支持连接Gmail、Google Drive、Google Calendar、Microsoft 365等第三方服务，也可通过MCP自行扩展。
9. 插件（Plugins）是技能+连接器的组合，例如Anthropic官方的Finance插件可生成财务报告、P&L、交易明细等。
10. 计划任务（Scheduled Tasks）支持定时执行，例如每天早上7:00将日程和邮件简报发送到Apple Notes。
11. 项目（Projects）是持久化、自包含的工作区，包含独立指令、记忆文件和连接，可跨会话记忆上下文。
12. 使用Productivity插件可以自动建立记忆系统（memory.md / CLOW.md），通过 `/update` 命令更新记忆，免去手动维护。
13. 投资组合项目演示：创建“stock portfolio”项目，设置投资哲学指令，生成每日投资摘要。
14. 可以构建“Mission Control”式综合仪表板，集成投资追踪、每日摘要、机会研究等功能。
15. 进阶技巧：将Claude Cowork与Claude Code结合，可大幅提升编程能力，例如为现有仪表板添加“创建技术交易机器人”的新标签页。

## 详细内容（保留所有原始信息）

### 1. 什么是Claude Cowork？
Claude Cowork属于当前热门的“本地AI代理”（local AI agent）产品类别。本地AI代理是生活在用户自己的电脑上的AI，可以自主操作文件、应用和工具。如果用户曾用过OpenClaude，可以将Claude Cowork理解为Anthropic的官方更安全版本，它完全基于Claude生态构建，且更面向非技术人群。视频中也提到本地AI代理是一个很酷的AI产品类别，但此视频更注重动手实践。

### 2. 安装与初始设置
- 安装步骤：访问 claude.com/products/colleague，点击“Download Claude”并安装在电脑上，完成后该应用成为“本地中枢”（local hub）。
- 主界面有三个标签：
  - **Chat**：与 claude.ai 网页版完全相同的聊天机器人，包含历史对话线程。
  - **Colleague**

---

## 附：Claude Cowork 系统配置与项目看板全景文档

> 由视频作者 Tina Huang 的四张配置截图整理，涵盖 Skills、Connectors、Plugins、Projects 四大部分。

### 一、核心技能（My Favourite Claude Cowork Skills）

通过斜杠命令（/）快速触发的自动化快捷原子技能。

| 斜杠命令 | 类型标签 | 功能描述 (中英双语) |
|---|---|---|
| /today | TINA | 将隔夜的投资组合变动、收件箱亮点、Slack 提醒以及今天的日历整理成一份摘要。替代你清晨刷手机的习惯。 Pulls overnight portfolio moves, inbox highlights, Slack pings, and today's calendar into one digest. Replace your morning scroll. |
| /data:build-dashboard | DATA PLUGIN | 从任何数据源（投资组合、指标、运营）构建交互式仪表盘。将图表、过滤器和实时数据整合到一个可分享的文件中。 Build interactive dashboards from any data source — portfolio, metrics, ops. Charts, filters, and live data in one shareable file. |
| /prep [meeting] | TINA | 在任何电话会议之前，Claude 会扫描 Gmail 和 Slack 以获取历史记录、背景和行动项。再也不用毫无准备地去开会了。 Before any call, Claude scans Gmail + Slack for history, context, and action items. Never walk into a meeting cold again. |
| /start + /update | PRODUCTIVITY | 引导启动你的任务列表并保持同步 —— Claude 会扫描电子邮件、日历和 Slack，自动找出被埋没的行动项。 Bootstrap your task list, then keep it synced — Claude scans email, calendar, and Slack to surface buried action items automatically. |
| /review-contract | LEGAL PLUGIN | 放入任何合同，Claude 会立即标记出偏差、风险区域和需要谈判的关键条款。瞬间完成律师的第一轮初审。 Drop in any contract and Claude flags deviations, risk areas, and key clauses to negotiate. A lawyer's first pass, instantly. |
| /postiz | POSTIZ PLUGIN | 写下你的帖子，选择你的渠道，设置一个时间 —— Claude 可以帮你排程发布到包括 LinkedIn、X、Instagram 和 TikTok 在内的 28 多个平台。 Write your post, pick your channels, set a time — Claude schedules to 28+ platforms including LinkedIn, X, Instagram, and TikTok. |
| /fill-form | PDF PLUGIN | 在查看器中打开任何 PDF，交互式填写字段、签名和批注 —— 完全不需要离开 Cowork。 Open any PDF in the viewer, fill fields interactively, sign, and annotate — without ever leaving Cowork. |
| /build | TINA | 睡觉前放下一页简报。Claude 会构建好工作和脚本 —— 第二天早上它就在那等你了。 Drop a one-page brief before you sleep. Claude builds the work... script... — and it's waiting in the morning. |
| /search [query] | ENTERPRISE | 一次查询即可同时搜索 Gmail、Slack、Notion 和 Google 云端硬盘。瞬间在所有工具中找到任何内容。 One query searches Gmail, Slack, Notion, and Google Drive simultaneously. Find anything across all your tools instantly. |

### 二、外部生态连接器（My Favourite Claude Cowork Connectors）

打通底层数据资产、沟通软件与云存储的第三方连接通道。

1. **Gmail (Email inbox)**
   - 功能描述：定时每日摘要 —— 每天早晨呈现收件箱亮点、行动项以及赞助相关的邮件线索。
   - Scheduled daily digest — surfaces inbox highlights, action items, and sponsorship threads every morning

2. **Google Calendar (Calendar)**
   - 功能描述：为 /today 和 /prep 命令提供数据支持 —— Cowork 会读取我的日程表来规划一天，并在每次电话会议前为我提供背景简报。
   - Feeds /today and /prep — Cowork reads my schedule to plan the day and brief me before every call

3. **Slack (Team messaging)**
   - 功能描述：Cowork 会将投资组合警报推送到这里，并将团队亮点与关键讨论拉取到每日摘要中。
   - Cowork pushes portfolio alerts here and pulls team highlights into the daily digest

4. **Notion (Docs + ops)**
   - 功能描述：Cowork 会读取团队工作区 —— 自动提取学习小组（Cohort）笔记和会议记录，以获取长远的上下文背景。
   - Cowork reads our team workspace — cohort notes and meeting logs for LO context

5. **Google Drive (Cloud storage)**
   - 功能描述：Cowork 会按需拉取文档和内容资产，用于深度研究、脚本编写和会议准备。
   - Cowork pulls docs and content assets for research, scripting, and meeting prep

6. **Bigdata.com (Financial data)**
   - 功能描述：为投资仪表盘提供底层支持 —— 包含实时数据、预览以及公司层面的深度研究。
   - Powers the investment dashboard — live... and... previews, company research

7. **Canva (Design tool)**
   - 功能描述：Cowork 负责撰写设计简报和文案，并直接无缝输入到 Canva 中，用于设计生成与自动化工作流程。
   - Cowork drafts briefs and copy that feed straight into Canva for... and workflows.

8. **Apple Notes (Notes)**
   - 功能描述：任务列表管理 —— Cowork 会持续扫描备忘录中被埋没的行动项，并将它们自动同步到本地的 TASKS.md 文件中。
   - Task list — Cowork scans for buried action items and syncs them into TASKS.md

### 三、业务领域插件（My Favourite Claude Cowork Plugins）

封装了特定垂直领域 Prompt、上下文记忆和执行逻辑的专家级插件。

- **🛠️ Productivity（任务管理与记忆）** / Task management + memory
  - 引导启动任务列表，扫描电子邮件/Slack/日历以查找被埋没的行动项，并记住不同对话之间的背景上下文。
- **🔍 Enterprise Search（跨工具搜索）** / Cross-tool search
  - 无需切换标签页，即可在 Gmail、Slack、Notion 和网盘中查找任何内容 —— 一次查询即可搜索所有地方。
- **⚖️ Legal（合同与合规）** / Contracts + compliance
  - 审查赞助合同，分流处理品牌合作的保密协议（NDA），并为承包商起草合规合同。
- **📊 Finance（财务报告）** / Financial reporting
  - 为 Lonely Octopus 提供财务报告和分析 —— 包含财务报表、差异分析和日记账分录。
- **📈 Bigdata（投资研究）** / Investment research
  - 投资研究专家 —— 为投资组合仪表盘提供数据支持，并对单个持仓进行深入剖析。
- **🎨 Data（仪表盘与可视化）** / Dashboards + visualizations
  - 从任何数据源构建交互式仪表盘 —— 将图表、过滤器和实时数据整合到一个可分享的文件中。
- **📢 Marketing（内容与营销活动）** / Content + campaigns
  - 为 Lonely Octopus 的内容和新品发布起草时事通讯（Newsletters）、社交媒体文案和营销活动简报。
- **🗺️ Product Management（路线图与规划）** / Roadmap + planning
  - 编写功能需求、产品需求文档（PRD）等，确保团队在业务优先级上保持高度一致。
- **🗣️ Brand Voice（内容一致性）** / Content consistency
  - 自动确保每篇 LO 产出的内容 —— 帖子、电子邮件等，听起来风格一致并高度符合品牌形象。

### 四、项目看板管理（Projects I'm Building with Claude Cowork）

使用上述技能和生态组合而成的一站式工作/生活全生命周期看板。

**🟢 Built（已构建 - 6 个）**

1. **YouTube topic → script tool** [WORK]
   - 将任何选题灵感转化为结构化的脚本大纲，随时可以用于拍摄。
2. **Daily digest** [WORK] [PERSONAL]
   - 早间简报：包含投资组合变动、收件箱亮点、Slack 以及日历。
3. **Investment dashboard** [PERSONAL]
   - 带有研究和警报功能的实时投资组合追踪器。
4. **Personal productivity skills** [WORK] [PERSONAL]
   - 集成 /today、/prep、/build 等功能，用于日常运营的自定义技能集合。
5. **Autonomous overnight builder** [WORK] [PERSONAL]
   - 睡前放下一份简报，醒来时工作（脚本/代码）已经由 AI 自动构建完成。
6. **Accounting** [WORK]
   - 负责 LO 的财务报表生成、日记账分录自动填写和预算差异分析。

**🟠 In Progress（进行中 - 2 个）**

1. **Trading bots** [PERSONAL]
   - 基于价格阈值和外部研究信号的自动化仓位触发/交易机器人。
2. **LO Student Dashboard**
   - 追踪每个学员的学习小组进度、参与度和课程完成率 —— 供团队使用的实时全局视图。

**🔵 Pending（待办中 - 4 个）**

1. **Health tracker** [PERSONAL] [FUN]
   - 将健身数据、饮食、睡眠和习惯整合到同一个综合健康仪表盘中。
2. **Team OKR tracker** [WORK]
   - 负责 LO 团队目标的管理、每周打卡检查，以及进度与阶段性目标的动态对比。
3. **Budgeting tool** [PERSONAL]
   - 个人以及 LO 的整体现金流管理、储蓄率核算和净资产追踪工具。
4. **RPG Habit Tracker** [PERSONAL] [FUN]
   - 引入经验值（XP）、等级和连击（Streaks）机制，将日常任务、习惯和目标全面游戏化。