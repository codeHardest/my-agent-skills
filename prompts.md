* @.claude/skills/video-summarizer/SKILL.md **For Bilibili** part中提供了如何获取bilibili subtitles 的方法
* 需要实现一个浏览器插件，能在观看bilibili视频时，显示一个30行的滚动字幕框，通过滚动始终保持当前字幕在正中；
* 如果有中英双语字幕，则每一行都需要包含中英双语
* 安装该插件到 chrome 浏览器中，并打开一个bilibili视频，查看插件效果
* 这是一个全新的功能

* 使用这个视频进行测试 https://www.bilibili.com/video/BV1DfrdByE2H?spm_id_from=333.788.videopod.episodes&vd_source=d31feea0f4c7fcfbd00ace0a32a9b420&p=2，
./download/bilibili/bilibili-cookies.txt 中保存了该网站的cookies，你可以这个cookies进行测试
* 我正在观看p2, 这里显示的字幕是p1

* 透明度调整为50%
* 字幕窗口可拖动和调整长宽

* 问题未修复， 且点击右下方和上面的按钮， 字幕窗口会往下反瞬移
* 