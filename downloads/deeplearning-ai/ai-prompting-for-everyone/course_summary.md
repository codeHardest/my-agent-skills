# AI Prompting for Everyone - 课程总结

**课程来源**: DeepLearning.AI
**课程链接**: https://learn.deeplearning.ai/courses/ai-prompting-for-everyone
**课程简介**: Learn to communicate with AI effectively, from basic queries to advanced techniques used by power users.

---

## 模块 1: Finding Information

### 视频 1: The AI novice and the AI power user

**时长**: 9m
**链接**: https://learn.deeplearning.ai/courses/ai-prompting-for-everyone/lesson/de11nq6r/the-ai-novice-and-the-ai-power-user

#### 内容总结

本视频对比了AI新手与AI高级用户在prompt方式上的核心差异。通过具体案例展示了高级用户如何通过提供充足上下文、给AI思考时间、迭代式写作等方式获得更好的AI输出质量。

#### 核心知识点

- **上下文至关重要**：高级用户会提供详细的背景信息，而非简单的Google式查询
- **给AI思考时间**：对于复杂任务（如购车分析），允许AI花费更多处理时间来生成详细报告
- **对AI保持同理心**：将AI视为一个知识渊博但缺乏上下文背景的助理，需要足够信息才能准确完成任务
- **避免谄媚效应**：不要暗示期望的答案，使用中性的问题或提供评分标准来获取客观反馈
- **迭代式写作**：不要直接让AI写文章，而是先Outline（大纲）→ Critique（批评）→ Iterate（迭代）→ Expand（扩展）
- **AI的错误被夸大**：AI犯的错误比人们想象的少，病毒式传播的错误案例并不具有代表性
- **AI的真正价值**：深度研究、写作研究综述、分析个人数据（如健康数据）等任务

---

### 视频 2: Pretrained Knowledge

**时长**: 6m
**链接**: https://learn.deeplearning.ai/courses/ai-prompting-for-everyone/lesson/53ttu2p0/pretrained-knowledge

#### 内容总结

本视频解释了AI模型如何从互联网上的大量文本中学习知识（预训练知识），以及这些知识来源的特点和局限性。帮助学习者理解AI为什么会给出某些答案，以及如何预测AI在特定问题上的表现。

#### 核心知识点

- **预训练知识来源**：AI从互联网上的多种来源学习，包括社交媒体（Reddit）、书籍、Wikipedia、新闻网站、研究论文等
- **知识频率反映**：互联网上常见主题（烹饪、名人、电影）的信息更丰富，专业主题（天体物理学中的类星体）信息较少
- **多语言数据**：虽然大部分互联网是英语，但AI也学习了其他语言的数据（如粤语约占0.1%）
- **私有数据不存在**：AI模型不知道您公司的专有数据，因为它不在公开互联网上
- **错别字容忍**：AI能很好地理解错别字，因为它从包含错别字的来源学习过
- **知识局限性**：AI的知识有截止日期，且可能包含误解和过时信息
- **可靠性判断**：思考数据在互联网上的出现频率可以帮助判断AI回答的可靠程度

---

### 视频 3: Web Search

**时长**: 5m
**链接**: https://learn.deeplearning.ai/courses/ai-prompting-for-everyone/lesson/fwaadejr/web-search

#### 内容总结

本视频介绍了AI如何使用Web Search来获取最新信息，包括其工作原理、局限性以及如何引导AI使用更可靠的来源。还解释了AI搜索网页时的底层机制——用户面向的AI模型会调用辅助AI模型来执行搜索。

#### 核心知识点

- **Web Search的局限**：AI搜索倾向于使用流行来源（Reddit、Wikipedia、YouTube等），其中一些来源的可靠性不如其他来源
- **引导使用可靠来源**：可以要求AI使用官方组织（WHO、FDA、欧洲药品管理局）的来源
- **信息可能过时**：网页内容可能已过时，导致AI给出不准确的建议
- **AI搜索的工作流程**：用户面向的AI模型（客服）→ 调用辅助AI模型 → 执行Web Search → 汇总相关网页 → 返回结果给用户
- **AI只看摘要**：用户面向的AI模型并没有完整读取所有网页，只看到了摘要，因此可能误解网页内容
- **何时用AI vs 传统搜索引擎**：想要快速扫描多个来源或导航到特定网站用传统搜索引擎；想要综合多个来源、获取利弊分析时用AI
- **常见Google习惯适用于AI**：寻找可靠来源、核实来源等习惯在AI搜索时同样适用

---

### 视频 4: Web Search Sources

**时长**: 8m
**链接**: https://learn.deeplearning.ai/courses/ai-prompting-for-everyone/lesson/vtdd22pz/web-search-sources

#### 内容总结

本视频深入讲解了为什么AI在执行Web Search时可能会给出不可靠答案，以及如何通过特定prompt技巧来引导AI优先使用官方和权威来源。还解释了AI搜索结果背后的多步骤流程。

#### 核心知识点

- **知识截止日期**：AI模型的训练有截止日期，之后发生的事情需要通过Web Search获取
- **自动触发搜索**：当问题涉及当前事件、地点特定信息或利基知识时，AI可能自动触发Web Search
- **手动触发搜索**：可以通过点击按钮或在prompt中写"请执行Web Search"来明确触发
- **搜索触发条件**：当前事件、位置特定查询、利基信息等会触发Web Search
- **不是所有AI都有搜索功能**：最流行的AI模型提供商（ChatGPT、Gemini、Claude）大多支持此功能
- **坏来源问题**：Web Search可能返回不可靠来源，需要引导AI使用更权威的来源

---

### 视频 5: Using Deep Research

**时长**: 8m
**链接**: https://learn.deeplearning.ai/courses/ai-prompting-for-everyone/lesson/ldiicy7i/using-deep-research

#### 内容总结

本视频介绍了Deep Research（深度研究）功能，这是一种比普通Web Search更强大的AI研究能力。它可以同时发起多个网络搜索，阅读数十个来源，然后综合成一份详细的研究报告。视频还解释了何时应该使用深度研究而非普通搜索。

#### 核心知识点

- **Deep Research定义**：AI可以同时搜索和阅读数十个甚至更多来源，进行深入思考后生成最佳答案
- **工作流程**：制定研究计划 → 同时发起多个Web Search → 评估来源相关性 → 决定是否需要更多搜索 → 汇总所有内容生成报告
- **代理式AI示例**：深度研究是代理式AI（agentic AI）的典型例子，AI有灵活性自行决定下一步做什么
- **与普通Web Search的区别**：
  - 普通搜索：回答简单问题，下载少量来源，耗时数秒
  - 深度研究：回答复杂问题，下载数十个来源，耗时数分钟甚至更长
- **何时使用Deep Research**：需要综合多个视角、需要最近科学文献支持、需要深入思考而非简单搜索的主题
- **Google Gemini的额外功能**：可以将深度研究结果直接转换为网页或信息图
- **典型用例**：医疗健康影响、旅游影响分析等需要综合多个来源的复杂问题

---

### 视频 6: Lab Overview: AI Model Prompt Comparison

**时长**: 4m
**链接**: https://learn.deeplearning.ai/courses/ai-prompting-for-everyone/lesson/46zz5oii/lab-overview%3A-ai-model-prompt-comparison

#### 内容总结

本视频是实践实验的概述，介绍了如何比较有无Web Search时AI输出的差异，以及Deep Research与普通搜索的区别。鼓励学习者亲自尝试各种示例来理解不同prompt技术的效果。

#### 核心知识点

- **实验对比功能**：可以比较有无Web Search的答案差异
- **Deep Research对比**：可以比较Web Search与Deep Research的结果差异
- **文件上传功能**：可以上传自己的文件（如租约协议）让AI结合上下文给出更有针对性的答案
- **错别字容忍**：AI系统能够很好地回答有错别字的问题
- **实验目的**：帮助学习者建立对何时使用何种AI工具的直觉

---

### 视频 7: Brainstorming with AI

**时长**: -
**链接**: https://learn.deeplearning.ai/courses/ai-prompting-for-everyone/lesson/uzffvb/brainstorming-with-ai

#### 内容总结

本视频介绍了如何将AI作为思维伙伴进行头脑风暴。视频指出仅仅让AI生成想法列表并不是最高效的方式，展示了如何通过提供更多上下文、给AI反馈、迭代多轮来获得更有创意的想法。

#### 核心知识点

- **AI作为思维伙伴**：当人类专家不可用时，AI是一个很好的思维伙伴资源
- **创意生成能力**：AI可以生成200个潜在用户这样的长列表想法
- **基本vs创意响应**：AI更可能给出常识性回应而非高度创意的回应，因为它基于互联网文本训练
- **提供上下文的艺术**：给AI更多背景（如年龄、器材、限制条件）可以获得更相关和创意的响应
- **迭代反馈法**：不直接要求一个方案，而是让AI给出多个选项 → 反馈喜欢/不喜欢 → AI生成新选项 → 循环迭代
- **常见创意问题**：如果问AI"帮我制定锻炼计划"而不提供背景，AI会给出通用的俯卧撑、深蹲等常识性回答
- **高效获取创意**：提供上下文 + 要求多个选项 + 迭代反馈 = 更有创意的想法
- **ChatGPT使用统计**：创意构思占所有聊天约4%，写作和实用指导占约50%

---

### 视频 8: Working with Multimedia Data

**时长**: -
**链接**: https://learn.deeplearning.ai/courses/ai-prompting-for-everyone/lesson/2fnnlk/working-with-multimedia-data

#### 内容总结

本视频介绍了AI的多模态能力，包括生成图像、视频、语音、音乐、代码等。讲解了不同模态输出的时间和成本差异，以及如何将多模态输入（如上传图片）用于prompt中。

#### 核心知识点

- **多模态输出类型**：图像、视频、语音、音乐、代码等
- **生成成本/时间差异**：
  - 文本：最低成本、最快
  - 语音：中等成本
  - 图像：较高成本
  - 视频：最高成本、最慢
- **多模态输入**：可以输入图像、音频给AI，让AI基于这些内容生成输出
- **实用案例**：
  - 用AI生成蛋糕设计图像 → 给烘焙师制作真实蛋糕
  - 用AI生成视频（特效）
  - 用AI克隆声音朗读
  - 用AI编写代码（如打字游戏）
- **图像生成示例**：为女儿生日用AI生成猫咪蛋糕设计
- **语音克隆技术**：语音克隆越来越逼真，可以用来修正播客中的小错误或为游戏角色生成声音
- **代码生成**：用AI生成打字游戏——正确按键时显示猫咪被喂食的动画
- **迭代挑战**：多模态生成耗时更长、成本更高，因此难以像文本那样快速迭代
- **负责任使用**：语音克隆可用于正当用途（修正音频），但也存在欺诈风险（如AI声音冒充他人）
- **伦理考量**：AI语音生成对配音演员生计的影响与让更多人能够创作娱乐内容之间的平衡

---

## 模块 2: AI as a Thought Partner

> 注：模块2"AI as a Thought Partner"的详细内容已在上述视频7（Brainstorming with AI）中包含，该模块仅有一个视频。

---

## 模块 3: Working with Multimedia & Code

> 注：模块3"Working with Multimedia & Code"的详细内容已在上述视频8（Working with multimedia data）中包含，该模块仅有一个视频。

---

*课程总结制作时间: 2026-05-27*