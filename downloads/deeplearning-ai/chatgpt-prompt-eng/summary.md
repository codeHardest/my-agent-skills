# ChatGPT Prompt Engineering for Developers
## 课程总结

**课程来源**: DeepLearning.AI
**课程链接**: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng

---

## 视频 1: Introduction
**时长**: ~6.5 min
**链接**: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/dfbds/introduction
**视频 ID**: 20

### 内容总结

本课程由 Andrew Ng 和 OpenAI 技术团队的 Isa Fulford 共同授课。

**两种 LLM 类型**:
- **Base LLM (基础 LLM)**: 基于互联网文本训练，预测下一个最可能出现的词。例如输入"从前有一只独角兽"，它会续写关于独角兽的故事；输入"法国的首都是什么"，可能会续写成关于法国城市列表的问题。
- **Instruction-Tuned LLM (指令微调 LLM)**: 经过训练能够遵循指令，回答问题时更可能给出"法国首都是巴黎"这样的直接答案。训练方式包括在大量文本数据上预训练，然后使用指令和示例进行微调，并常用 RLHF（人类反馈强化学习）技术进一步优化。

**Prompt Engineering 最佳实践**:
1. **清晰具体的指令 (Clear and Specific Instructions)**: 像对待一位聪明但不了解你具体任务的大学毕业生一样提供指令。例如，写关于 Alan Turing 的内容时，应指定是聚焦他的科学工作、个人生活还是历史角色，以及期望的语气（专业记者风格还是给朋友的随意便签）。
2. **给模型时间思考 (Give the Model Time to Think)**: 如果任务复杂，应要求模型逐步推理，而不是快速得出可能错误的结论。

课程涵盖：Prompt 最佳实践、常见用例（总结、推理、转换、扩展）、构建聊天机器人。

---

## 视频 2: Guidelines
**时长**: ~17 min
**链接**: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/zi9lz/guidelines
**视频 ID**: 21

### 内容总结

**原则一：编写清晰具体的指令**

四个策略：

1. **使用分隔符 (Delimiters)**：使用明确的分隔符（如 triple backticks、XML 标签等）分隔输入的不同部分，防止提示注入（prompt injection）。例如：
   ```
   总结以下文本 delimited by triple backticks...
   ```

2. **要求结构化输出 (Structured Output)**：要求模型以 JSON 或 HTML 等格式输出，便于程序解析。

3. **要求模型检查条件是否满足 (Check Conditions)**：如果任务有假设条件，先让模型检查这些条件，不满足时指出问题。

4. **Few-shot Prompting (少样本提示)**：先提供成功执行的示例，再要求模型执行类似任务。

**原则二：给模型时间思考**

两个策略：

1. **指定完成任务所需的步骤 (Specify Steps)**：将任务分解为明确的步骤序列。

2. **让模型先自行解决再比较 (Self-Comparison)**：要求模型先独立计算/推理，再将结果与提供的答案比较。

**模型局限性 - 幻觉 (Hallucinations)**:
- LLM 不会完美记忆训练信息，可能对不熟悉的主题编造看似合理但实际错误的内容（幻觉）。
- 减少幻觉的方法：先让模型从文本中查找相关引用，再基于引用回答问题。

---

## 视频 3: Iterative
**时长**: ~13 min
**链接**: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/so7ui/iterative
**视频 ID**: 22

### 内容总结

**迭代式 Prompt 开发**

关键观点：第一次写出的 prompt 很少能直接用于最终应用。重要的是拥有一个迭代优化的流程。

**迭代循环**：
1. 有一个想法/任务
2. 编写第一次尝试的 prompt
3. 运行并检查结果
4. 分析为什么效果不好
5. 优化指令或给模型更多思考时间
6. 重复直到满意

**实践示例**：
将椅子规格表（fact sheet）转化为营销描述。

迭代过程：
- **第一次尝试**：生成了详细描述，但太长
- **加词数限制**：使用"最多 50 词"控制长度
- **调整目标受众**：改为面向家具零售商的 기술性描述
- **添加产品 ID**：在末尾加入产品编号 SWC 110、SWC 100
- **更复杂格式**：加入尺寸表格并输出为 HTML

**更成熟应用的做法**：
- 初期：用单个示例迭代开发 prompt
- 成熟期：用多个示例（如 10-50+ 个案例）评估 prompt 的平均/最坏情况表现

---

## 视频 4: Summarizing
**时长**: ~7.5 min
**链接**: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/px4pd/summarizing
**视频 ID**: 23

### 内容总结

**文本总结的应用场景**：
- 快速浏览大量文章/产品评论
- 电子商务网站评论汇总

**基础总结**：
- 指定字数限制（如"最多 30 词"）
- 指定句子数量（如"最多 3 句"）

**针对特定部门的总结**：
- **运输部门**：关注物流和配送
- **定价部门**：关注价格和感知价值
- 通过调整 prompt 聚焦特定信息

**提取 vs 总结**：
- 总结：保留主要内容
- 提取：只保留与特定用途相关的信息

**批量处理多条评论**：
- 将多条评论放入列表
- 循环调用 API 生成简短摘要
- 可用于构建评论仪表板，快速了解客户反馈

---

## 视频 5: Inferring
**时长**: ~12 min
**链接**: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/tyucw/inferring
**视频 ID**: 24

### 内容总结

**推理任务**：从文本中提取标签、情感、实体等信息。传统机器学习需要收集标注数据集、训练模型、部署，周期长。每个任务需要单独训练模型。

LLM 的优势：写一个 prompt 即可立即生成结果，一个 API 调用可完成多种任务。

**情感分类**：
- 可输出完整句子或简洁词汇（positive/negative）

**情绪识别**：
- 识别评论者表达的情绪（不超过 5 项）
- 可用于了解客户对产品的感受

**愤怒检测**：
- 判断评论者是否表达愤怒（对客户支持很重要）

**信息提取**：
- 提取购买商品、品牌等信息
- 输出为 JSON 格式，便于程序处理
- 一次 prompt 可提取多个字段

**主题识别 (Zero-Shot Learning)**：
- 给定一篇新闻文章，判断其涉及哪些主题
- 无需训练数据，直接通过 prompt 实现

**构建新闻提醒系统**：
- 追踪特定主题（如 NASA）
- 文章涉及目标主题时触发提醒

---

## 视频 6: Transforming
**时长**: ~12.5 min
**链接**: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/ycefn/transforming
**视频 ID**: 25

### 内容总结

**转换类型**：

1. **翻译**：
   - 单语言翻译
   - 多语言批量翻译
   - 正式/非正式语气区分
   - 构建多语言客服统一翻译器

2. **语气转换**：
   - 不同受众使用不同语气（如朋友间 vs 正式商务信函）

3. **格式转换**：
   - JSON ↔ HTML ↔ Markdown 等
   - 指定输入输出格式描述

4. **拼写/语法检查**：
   - 纠正常见语法错误
   - 支持多语言文本校对
   - 可对比原文与修正后的差异（使用 redlines 包）

5. **文本优化**：
   - 使文章更专业
   - 按特定风格（APA 等）重写
   - 针对特定读者群体调整

---

## 视频 7: Expanding
**时长**: ~6.5 min
**链接**: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/imsux/expanding
**视频 ID**: 26

### 内容总结

**扩展任务**：将短文本（如指令列表）生成为更长的文本（如电子邮件或文章）。

**应用场景**：
- 作为头脑风暴伙伴
- 生成个性化客户回复邮件

**负责任使用**：
- 避免用于生成垃圾邮件等有害用途

**温度参数 (Temperature)**：
- 控制输出的随机性和创意性
- **Temperature = 0**：总是选择最可能的下一个词，结果确定可预测
- **Temperature 越高**：越可能选择不太可能的词，输出更多样化但更不可预测
- 使用场景：
  - 需要可靠、可预测输出 → 用 temperature 0
  - 需要创意、多样化输出 → 用更高 temperature

---

## 视频 8: Chatbot
**时长**: ~12 min
**链接**: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/jtmdv/chatbot
**视频 ID**: 27

### 内容总结

**Chat Completions 格式**：
- 输入：消息列表（system、user、assistant 角色）
- 输出：模型生成的消息

**消息角色**：
- **System Message**：设定助手整体行为和角色，用户不可见
- **User Message**：用户输入
- **Assistant Message**：模型回复

**对话的独立性**：
- 每次对话是独立交互
- 必须提供所有相关上下文消息

**构建 OrderBot 示例**：
- 系统消息定义菜单和对话流程
- 上下文（context）包含累积的对话历史
- 模型根据完整上下文生成回复
- 可生成 JSON 格式订单摘要提交给后端系统

---

## 视频 9: Conclusion
**时长**: ~2.5 min
**链接**: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/fam6w/conclusion
**视频 ID**: 28

### 内容总结

**课程回顾**：
- 学习了两个核心 Prompt 原则：编写清晰具体的指令、给模型时间思考
- 迭代式 Prompt 开发流程
- 大语言模型的实用能力：总结、推理、转换、扩展
- 构建自定义聊天机器人

**建议**：
- 先从小型项目开始尝试
- 从第一个项目积累经验，逐步构建更好的项目
- 负责任地使用这些强大的 AI 工具，只构建积极影响的应用程序

---

## 完整视频列表

| 序号 | 视频标题 | 时长 | 链接 | 视频 ID |
|------|---------|------|------|---------|
| 1 | Introduction | ~6.5 min | [Link](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/dfbds/introduction) | 20 |
| 2 | Guidelines | ~17 min | [Link](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/zi9lz/guidelines) | 21 |
| 3 | Iterative | ~13 min | [Link](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/so7ui/iterative) | 22 |
| 4 | Summarizing | ~7.5 min | [Link](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/px4pd/summarizing) | 23 |
| 5 | Inferring | ~12 min | [Link](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/tyucw/inferring) | 24 |
| 6 | Transforming | ~12.5 min | [Link](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/ycefn/transforming) | 25 |
| 7 | Expanding | ~6.5 min | [Link](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/imsux/expanding) | 26 |
| 8 | Chatbot | ~12 min | [Link](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/jtmdv/chatbot) | 27 |
| 9 | Conclusion | ~2.5 min | [Link](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/fam6w/conclusion) | 28 |

---

## 核心概念总结

### Prompt Engineering 两大原则
1. **清晰具体的指令 (Clear and Specific Instructions)**
   - 使用分隔符
   - 要求结构化输出
   - 检查条件
   - Few-shot 示例

2. **给模型时间思考 (Give the Model Time to Think)**
   - 指定完成步骤
   - 让模型先独立解决再比较

### LLM 能力
- **总结 (Summarizing)**：多角度、按用途聚焦
- **推理 (Inferring)**：情感、情绪、实体、主题识别
- **转换 (Transforming)**：翻译、格式转换、语法纠正
- **扩展 (Expanding)**：生成更长文本，温度参数控制创意性

### 构建聊天机器人
- System Message 设定角色
- 累积上下文实现多轮对话
- 高可靠性任务用低 temperature

---

*此总结由 AI 自动生成，仅供学习参考使用*