# Bilibili 双语字幕浏览器插件

在 Bilibili 视频页面右侧显示 30 行滚动字幕框，支持中英双语，自动保持当前字幕居中。

## 功能特性

- **30 行滚动字幕**：视频右侧显示字幕列表
- **自动居中**：当前播放字幕始终保持在窗口中央
- **双语支持**：同时显示中文和英文字幕（格式：中文 | English）
- **多 P 支持**：自动识别当前播放的分 P 视频
- **可拖动**：点击顶部把手可拖动调整位置
- **可调整大小**：拖动右下角可调整窗口大小
- **半透明背景**：50% 透明度，不遮挡视频

## 安装方法

1. 打开 Chrome 浏览器，访问 `chrome://extensions/`
2. 开启右上角的「开发者模式」
3. 点击「加载已解压的扩展程序」
4. 选择项目中的 `plugin/bilibili` 文件夹
5. 插件安装完成

## 使用方法

1. 打开任意 Bilibili 视频页面（如 `https://www.bilibili.com/video/BVxxx`）
2. 等待 2-3 秒，字幕窗口会自动出现在视频右侧
3. 播放视频，字幕会自动同步显示

### 注意事项

- 某些视频可能没有字幕
- 部分视频的字幕需要登录后才能获取
- 如遇问题，按 F12 打开控制台查看日志（以 `[Bilibili Subtitle]` 开头）

## 项目结构

```
plugin/bilibili/
├── manifest.json    # 插件配置文件
├── content.js      # 核心逻辑脚本
└── styles.css     # 样式文件
```

### manifest.json

插件配置文件，定义了：
- 插件名称和版本
- 权限（activeTab, scripting）
- 内容脚本匹配规则（`*://*.bilibili.com/video/*`）

### content.js

核心逻辑包括：
- `init()` - 初始化插件
- `getVideoInfo()` - 获取视频 AID 和 CID
- `loadSubtitles()` - 从 Bilibili API 获取字幕
- `downloadAndParseSubtitles()` - 下载并解析字幕文件
- `mergeSubtitles()` - 合并中英双语字幕
- `createSubtitleContainer()` - 创建字幕 DOM 容器
- `makeDraggable()` - 实现拖动功能
- `startSubtitleSync()` - 同步字幕显示

### styles.css

样式定义：
- 位置：视频右侧，垂直居中
- 尺寸：320px × 600px（可调整）
- 背景：半透明黑色（50% 透明度）
- 交互：可拖动、可调整大小

## 技术实现

### 字幕获取

使用 Bilibili Web API 获取字幕：
```
https://api.bilibili.com/x/player/wbi/v2?aid={aid}&cid={cid}
```

需要从页面提取：
- `aid`：视频 AID
- `cid`：当前分 P 的 CID

### 字幕同步

监听 video 元素的 `timeupdate` 事件，根据当前播放时间查找对应字幕，并通过 `scrollTo` 实现自动滚动到中央。

### 多 P 视频处理

从 URL 中提取当前分 P 编号（`?p=2`），请求 API 时获取对应分 P 的 CID。

## 常见问题

**Q: 字幕窗口不显示？**
A: 检查控制台是否有错误日志，确认视频是否有字幕


**Q: 无法调整大小？**
A: 拖动右下角即可调整大小

## 更新日志

### v1.0
- 初始版本
- 支持 30 行滚动字幕
- 支持中英双语
- 支持拖动和调整大小
- 支持多 P 视频

## 许可证

仅供个人学习使用，请尊重视频创作者的版权。
