# 幼小衔接学习台 · 家长使用说明

一套给大班→一年级孩子用的每日识字系统。主题：**奥特曼打怪兽 / 拳皇对战**。
每天自动按**遗忘曲线**安排复习（20字）+ 学习新字（3个），全程交互式选择题，配发音跟读和描红。

## 每天怎么用

```
1. 在 Claude Code 里运行：
      /kid-learn
   → Claude 会：先自动合并昨天学习结果 → 计算今日任务 → 生成今日学习页
   → 完成后会告诉你页面路径，例如 sessions\2026-08-20.html

2. 用 Chrome 打开那个页面，交给孩子学（家长在旁边陪发音部分）

3. 孩子学完，页面自动生成「今日结果」文件：
   · 弹窗选保存文件夹 → 选 data\results\ 目录（之后每天自动写入）
   · 或自动下载 result-日期.json，家长手动存到 data\results\

4. 次日再运行 /kid-learn，结果会自动合并、遗忘曲线自动更新
```

> **提示**：直接双击 HTML 用 `file://` 打开时，Chrome 语音识别不可用，发音题会
> 自动降级为「家长判断」（孩子跟读后家长点 👍/👎）。
> 想要语音自动识别，把目录用本地服务器打开即可，例如：
> ```
> cd P:\AI\my-agent-skills\projects\幼小衔接
> python -m http.server 8000
> ```
> 然后 Chrome 打开 `http://localhost:8000/sessions/2026-08-20.html`。

## 目录结构

```
幼小衔接\
├── data\
│   ├── char_library.json       字库（拼音/组词/同音相似标记/笔顺）
│   ├── progress.json           学习进度 + 遗忘曲线状态（不要手动改）
│   ├── results\                每日结果文件（页面写入，自动合并）
│   └── subjects_progress.md    进度周报（家长浏览用）
├── templates\lesson-app.html   学习台 UI 模板（一般不用动）
├── sessions\                   每日生成的学习页（按日期）
├── tools\
│   ├── build_library.js        重建字库（改了 tools 里的字表后运行）
│   ├── init_progress.js        初始化进度（重置时运行）
│   ├── generate_session.js     每日页面生成器（技能调用）
│   └── test_template.js / check_template.js   模板验证
└── subjects\                   数学/英语（预留）
```

## 想调整学习内容？

- **加字 / 改组词**：编辑 `tools\build_library.js` 里的字表，然后运行
  `node tools\build_library.js` 重建字库。
- **改每日题量**：编辑 `data\progress.json` 的 `daily_target`（如 `review` 改 15）。
- **导入洪恩字表**：把洪恩识字已学字列表发给我，我帮你批量导入并校准进度。
- **重置从头开始**：运行 `node tools\init_progress.js`。

## 遗忘曲线怎么工作的

每个字独立记间隔：答对 → 间隔 1→3→7→15→30→60 天放大；答错 → 重置为 1 天，
明天立刻再考。每天优先复习「到期最久 + 上次答错」的字。

## 数学 / 英语

框架已预留（`subjects\math`、`subjects\english`），后续迭代接入。有需要时告诉我。
