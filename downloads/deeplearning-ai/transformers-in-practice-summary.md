# Transformers in Practice - 课程完整总结

**课程来源**: [DeepLearning.AI](https://learn.deeplearning.ai/)
**课程讲师**: Sharon Zhou (AMD VP of Engineering and AI)
**课程链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice>
**课程合作**: AMD
**课程难度**: Intermediate
**课程主题**: Transformers
**发布日期**: 2026-05-12

> 课程简介：超越单纯"使用"LLM，真正"理解"它们。本课程由 Sharon Zhou 主讲，帮助你建立推理模型行为、调试真实问题以及对基于 Transformer 的模型做出更明智的部署决策所需的直觉。

---

## 课程结构概览

本课程包含 **3 个 Module，共 19 个视频**：

- **Module 1: Observed behavior（观察到的行为）** — 9 个视频，将 LLM 视为黑盒，关注输入/输出与行为
- **Module 2: LLM internals and attention（LLM 内部机制与注意力）** — 4 个视频，打开黑盒，研究注意力、位置编码、模型层和解码
- **Module 3: Scaling and deploying（扩展与部署）** — 6 个视频，研究在 GPU 上的运行与优化（量化、KV 缓存、Flash Attention、推测解码等）

---

# Module 1: Observed behavior（观察到的行为）

**Module 概述**：本模块将 LLM 视为黑盒，关注其输入和输出。核心观点：LLM 所做的一切（写代码、产生幻觉等）都源于同一个过程——**从整个词汇表的概率分布中一次选择一个 token**。本模块解释了许多 LLM 行为如何从这一过程中涌现，并展示了结构化输出、RAG、推理等技术如何基于这一循环构建。

---

## 视频 1: Conversation between Sharon Zhou and Andrew Ng（Sharon Zhou 与 Andrew Ng 的对话）
**时长**: ~4.5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/y8sw6w/conversation-between-sharon-zhou-and-andrew-ng>
**视频 ID**: 10169010

### 内容总结

这是由 Andrew Ng 主持的课程导言对话。Andrew 介绍了讲师 Sharon Zhou（曾在 Stanford，现任 AMD 副总裁）。课程的目标是帮助学习者在使用 LLM 时获得更深入的直觉，从而能调试问题，而不是仅仅说"LLM 不工作"。

**核心要点**：

1. **课程定位**：市面上已有很多优秀资源讲解 Transformer 的工作原理（从零构建课程、注意力机制的复杂解释、理论深度剖析）。但这些解释往往与实际使用 Transformer 时遇到的问题脱节。本课程连接所有关键环节，建立连贯的图景。

2. **课程覆盖范围**：
   - 训练好的 Transformer 如何生成文本
   - 前向传播过程中发生了什么
   - 如何优化该过程以在 GPU 上运行

3. **关键概念**：一旦理解了这些模型的核心——**从概率分布中一次生成一个 token**，其他一切都顺理成章。

4. **架构演变**：原始 Google Brain 的 Transformer 论文讲的是 encoder-decoder 架构。但最重要的演变之一是，现在所有前沿实验室几乎都使用 **decoder-only 架构**。本课程专注于 decoder-only Transformers，因为这是当今几乎所有前沿模型背后的架构。

5. **互动可视化**：课程包含有趣、信息丰富的交互式可视化，你可以实际观察这些过程：观察 token 被采样、注意分数形成、GPU 内部发生什么。具体的例子对理解非常重要，因为 Transformer 中常常"眼所见非全貌"。

6. **三个 Module 内容**：
   - **Module 1**：学习 LLM 所做的一切——无论是写代码还是为什么产生幻觉——都源于从词汇表概率分布中一次挑选一个 token 的同一过程。这解释了从该过程涌现的许多 LLM 行为，并展示了结构化输出、RAG、推理等技术如何基于同一循环构建。
   - **Module 2**：那个概率分布从哪里来？打开模型，研究注意力机制、位置信息如何被编码和包含、层与层之间如何构建以产生该分布的数学运算。这涉及大量矩阵运算。
   - **Module 3**：理解单次前向传播涉及的数学后，就能开始理解整个 LLM 系统中发生了什么，不仅仅是语言模型本身。研究这些数学如何在 GPU 上运行，以及 KV caching、flash attention、量化等优化。

7. **课程目标**：如果你已经在使用 LLM，你可能对其行为有实际经验，但不一定总是理解为什么它们以那种方式行为。完成本课程后，你将拥有 Andrew 描述的连贯图景，帮助你在部署中做出更好的决策，或帮助你跟进新的研究。

---

## 视频 2: Transformers in practice（实践中的 Transformers）
**时长**: ~2.5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/ldi0cw7i/transformers-in-practice>
**视频 ID**: 10169011

### 内容总结

Sharon Zhou 正式开课，介绍课程的整体目标。

**核心要点**：

1. **课程目标**：本课程旨在让你**实际理解** Transformer 模型的工作方式，这样当出现问题或需要做出部署/配置决策时，你拥有正确的心理模型来推理，而不是盲目猜测。

2. **架构现状**：这是当前所有前沿 LLM（Claude、Gemini、ChatGPT 以及开源的 Qwen、DeepSeek）背后的架构。原始 Transformer 论文讲的是 encoder-decoder 架构，但最新的生成式模型使用 **decoder-only Transformer**，已成为主流架构，这也是本课程的重点。

3. **为什么会得到好坏参半的结果**：你可能经历过模型超级有用的时刻，给出惊人答案；但也有得到糟糕答案的时候，即使问题看起来很简单。本课程帮助你建立这些概念性理解，配合互动可视化让想法更具体。

4. **三个 Module 的预览**：
   - **Module 1 - 模型行为（Model Behavior）**：将 LLM 视为黑盒，专注于输入和输出是如何从输入产生的（概念性直觉）。
   - **Module 2 - 打开黑盒**：查看架构内部的表示和过程，如注意力或 MLP（多层感知机）。
   - **Module 3 - 扩展与部署（Scaling and Deploying）**：理解完整 LLM 系统。有大量的东西围绕着它，以获得你看到和期待的速度、成本、质量。

5. **学完收获**：到课程结束时，你将完整理解这些模型如何行为、架构如何产生该行为，以及实际运行它们需要什么。从你可以观察到的东西开始——模型如何一次生成一个 token。

---

## 视频 3: The autoregressive loop（自回归循环）
**时长**: ~4.5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/79yzruak/the-autoregressive-loop>
**视频 ID**: 10169030

### 内容总结

本视频将 Transformer 视为黑盒，观察其外部行为。

**核心要点**：

1. **自回归生成（Autoregressive Generation）**：当你向 LLM 输入提示时，会得到完整的响应——句子或段落作为输出。但这个响应是一次构建一个片段、**一个 token 一个 token** 通过称为自回归生成的过程构建的。这一过程的具体细节影响了你会看到模型生成新文本的行为。

2. **什么是自回归**：意味着 LLM 通过循环**一次生成一个 token**。每个新 token 依赖于前一个生成的 token，循环不断进行。

3. **输入的处理**：
   - 输入首先被分解为 token
   - Token 可以是单词、片段，常见词通常是单个 token
   - 模型不仅从你的提示中获取 token，还会获取**模板 token**
   - 包括：系统提示（如"你是一个乐于助人的助手"）、`/no_think` 标签（不使用任何思维/推理 token）、LLM 结束/开始标签等助手标签
   - 所有这些 token 加在一起构成**上下文窗口（context window）**

4. **上下文窗口的关键性**：
   - 模型没有静态记忆或上下文窗口之外的记忆
   - 它仅查看这个包含你提示的上下文窗口，并从中产生一个 token
   - 上下文窗口的大小是 LLM 在任何时刻能"看到"的最大文本量
   - 不能超过这个最大上下文窗口

5. **生成循环的步骤**：
   - **步骤 1**：输入被分解为 token，这些 token 位于上下文窗口中
   - **步骤 2**：模型计算概率，输出整个词汇表上的 token 概率分布
   - **步骤 3**：选择一个 token 作为下一个 token
   - **步骤 4**：所选 token 被附加到输入 token
   - **步骤 5**：再次进行整个过程
   - 重复直到满足停止条件

6. **选择下一个 token 的方法**：
   - **贪婪选择（Greedy Selection）**：选择概率最高的 token（这里是 "the"）
   - 也可以进行**随机采样（sampling）**：从这些 token 中随机选择
   - 有许多参数可以控制可以选择的 token
   - 这就是为什么同一提示每次都能给出不同响应的原因

7. **停止条件**：
   - 模型已学会这些**停止 token**（stop tokens），用作明确的停止条件
   - 可能有最大 token 限制（输出数量）
   - 上下文窗口达到最大大小时也会停止

**核心洞见**：每次循环迭代产生整个词汇表上下一个可能 token 的概率分布。但单个 token 如何从所有这些可能性中被挑选出来？这个选择如何塑造模型产生的内容？这是下一视频的内容。

---

## 视频 4: Visualization tutorial（可视化教程）
**时长**: ~3.5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/de1knw6r/visualization-tutorial>
**视频 ID**: 10169029

### 内容总结

本视频是关于课程中交互式可视化的使用教程。

**核心要点**：

1. **可视化的目的**：给你另一个机会建立 Transformer 概念的直觉。本课程提供一系列关键主题的交互式可视化。

2. **第一个可视化**：走查文本生成循环的步骤。
   - 由 **Qwen3-0.6B 参数模型**驱动（一个小巧的 LLM，能在 Deep Learning AI 平台上运行）
   - 让你看到 LLM 的真实输出
   - 其他一些可视化也由该模型驱动，其他只使用预先计算的数据

3. **使用建议**：
   - 第一次加载可能需要一分钟
   - 点击课程大纲旁边的小菜单图标以折叠菜单，让可视化占据更多浏览器宽度
   - 可以使用浏览器菜单中的缩放控件调整可视化大小

4. **操作步骤**：
   - 在框中输入提示或用图标选择预写提示
   - 推荐选择一个示例：情感分析示例（"analyze the sentiment of this review"）
   - 输入 token 在下方显示：灰色 token 是 Qwen 模型期望的聊天模板，蓝色提示是系统提示
   - 可以点击 "system" 查看系统提示（例如"return exactly one word"）

5. **逐步循环**：
   - 点击 "step" 按钮启动模型的前向传播
   - 整个左侧输入 token 集通过模型
   - 输出是词汇表上的下一个 token 预测概率集
   - 概率和 token 在此处显示（例如情感分析中所有概率都集中在 "positive"）
   - 再次点击 step，选择 top token 出现在第三列
   - 在此可视化中，始终选择最可能的 token，称为**贪婪采样（greedy sampling）/贪婪解码（greedy decoding）**

6. **停止条件**：循环可以以三种方式退出：
   - 满足指定的 max new tokens
   - 填满上下文窗口
   - 选择停止 token

7. **进一步操作**：
   - 点击 step 多次，或点击 play 让步骤自动播放
   - 可以点击 faster 加速
   - 点击任何信息按钮（如 select token 部分的）以获取更多信息
   - 遇到任何问题，寻找 reset 按钮或刷新页面
   - 尝试预写提示（如音乐按钮查看有趣的 Taylor Swift 问题），或输入自己的提示

---

## 视频 5: Token sampling（Token 采样）
**时长**: ~5.5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/sh74qlbh/token-sampling>
**视频 ID**: 10169013

### 内容总结

本视频深入探讨从概率分布中选择单个 token 的各种方法。

**核心要点**：

1. **回顾**：你有自回归循环，输入 token → 计算概率 → 获得下一个 token 概率 → 采样一个 → 在循环中重复直到停止。本视频聚焦于那个 token 的选择。

2. **采样策略**：

   - **贪婪解码（Greedy Decoding）**：
     - 选择概率最高的下一个 token
     - 使用语言模型解码的完整过程称为贪婪解码
     - 几乎确定性的——每次都选择最高概率 token
     - **问题**：LLM 有时听起来有点无聊和模板化（boilerplate）
     - 历史上有时会陷入**重复循环**
   
   - **随机采样（Random Sampling）**：
     - 不是总选择最可能的 token，更随机地选择
     - 像旋转一个轮盘，由概率加权
     - 有点随机性
     - **注意**：如果从所有可能 token（包括超低概率的）采样，可能选出毫无意义的稀有 token
   
3. **采样参数**：

   - **温度（Temperature）**：
     - 改变这些概率，改变分布，使你更可能或更不可能选择某些 token 作为下一个 token
     - 借自物理学，与物理中的温度（温暖或寒冷）相同
     - 当温度较大时，跨可能下一个 token 概率的分布更大
     - 这使得选择最高概率 token 的可能性降低，并将分布分散
     - 当温度非常低（设为零）时，类似于贪婪采样，只选择最可能的 token
   
   - **Top K**：
     - 选择 top K token，并从这些 top K 中选择
     - Top K = 1，仍选择 top 下一个 token 概率
     - Top K = 2，从两个最高概率 token 中选择
     - **问题**：并不总是最优
     - 例如有些情况下前两个 token 概率很高，但后续 token 概率很低（0.2%, 0.1%），可能将模型引向奇怪的空间
   
   - **Top P**：
     - P 代表概率
     - 提供从 0 到 100% 的百分比
     - 0% 是贪婪解码
     - 100% 选择所有 token 的累积概率 100%
     - 99% 是累积概率 99% 的概率质量
     - 例如 90% 时总累积概率为 94.7%
     - 80% 时选择更少的 token
   
4. **温度与 Top P 的组合**：
   - 较低温度下，分布更尖锐
   - Top P 为 90% 仅保留少数 token
   - 较高温度下，分布更分散，Top P 90% 捕获更多 token
   - 实际前沿模型在内部组合使用这些参数
   - **注意**：OpenAI 不暴露 Top K，建议改变温度或 Top P，但不要同时改变两者

5. **核心要点总结**：
   - 模型始终基于**概率**而非正确性进行选择
   - 基于训练中学习的模式，这是概率性的
   - 这意味着许多有趣的模型行为正是从这些性质中涌现

---

## 视频 6: Autoregressive dynamics（自回归动态）
**时长**: ~4 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/opk78jc1/autoregressive-dynamics>
**视频 ID**: 10169015

### 内容总结

本视频分析自回归过程导致的各种行为和问题。

**核心要点**：

1. **回顾**：模型有输入 token，计算概率，基于采样参数选择下一个 token，在循环中重复直到停止条件。

2. **多种路径（Many Paths）**：
   - 自回归生成可以导致许多不同路径
   - 例如，要求模型编写 Python 函数验证用户邮箱
   - 可能采样 "def" 开始定义 Python 函数
   - 也可能预测并采样下一个 token 为 "import"，导入 regex 包，仍然在写有效的 Python 函数并完成任务，但看起来不同

3. **问题性场景**：
   - 如果第一个 token 是 "function"——不是 Python 函数的开始方式，而是 JavaScript 函数
   - 模型开始写 JavaScript 函数，**无法回溯**
   - 数学中也存在这种情况，因为数字是一个数字一个数字生成的
   - 这就是为什么人们用计算器工具代替 LLM，因为 LLM 在这里可能做一些有问题的事情
   - 一开始是好的，但到达错误的数字（如 0），然后继续，无法回溯
   - 询问某数字是否为质数，正确答案是 yes，但如果采样到 "no"，后续一切都会错，可能继续编造事实

4. **常见问题**：
   - **幻觉（Hallucination）**：选择糟糕 token 后，模型可能自信地编造
   - **任务漂移（Task Drift）**：要求 Python 函数，但产生 JavaScript 函数
   - **重复（Repetition）**：模型可能进入自我强化的循环，反复生成相同序列的 token
   - 较旧或较小的模型更容易出现重复

5. **著名案例**：
   - 用户问模型如何将模型上传到 Hugging Face
   - 模型建议一个虚假包，因为人们问的是"如何将模型上传到 hugging face"
   - 一位安全研究员创建了 fake PyPy 包，三个月内下载量达 30,000 次

6. **训练模式的默认值**：
   - 摄氏度转华氏度：乘以 9，除以 5，加 32
   - 模型在这上面表现很好
   - 但稍微扰动一下，模型可能仍然默认为温度转换（因为更可能）
   - 研究人员发现这种情况，因为模型习惯了

7. **知识缺乏导致的幻觉**：模型可能不知道你询问的包，可能开始编造，因为它想要给出概率高的东西而不是说不知道

8. **自回归动态导致多条路径**：可以分支到许多正确路径，但也许多错误路径。语言模型**不一定看到真相，看到的是概率**。最可能的 token 可能不是最正确的 token。

9. **训练后的解决方案**：研究人员试图通过后训练（post-training）解决这个问题——确保模型更可能选择正确的 token，使最可能的 token 成为最正确的 token。

---

## 视频 7: Structured outputs（结构化输出）
**时长**: ~5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/8bhr0z/structured-outputs>
**视频 ID**: 10170010

### 内容总结

本视频探讨如何控制模型输出的格式，使其符合特定结构。

**核心要点**：

1. **问题背景**：你不能严格强制模型提供特定答案。模型可能选择许多概率 token。你可以使用不同技术采样下一个 token，但总会有许多不同的可能性。但当你必须遵循某种结构时怎么办？

2. **需要结构的场景**：
   - **JSON 输出**：你想要结构化数据提取作为输出，然后用于下游任务
   - **代码生成**：要遵循某个模式、某些语法规则
   - **函数调用**：需要生成具有正确参数的有效 API
   - **SQL 生成**：需要与数据库中的内容匹配

3. **LLM 的困境**：在训练时，它想平衡结构化与有用性（说"当然，我可以帮你"），这导致潜在的不一致输出。例如，它可能说"sure"或"here"，或输出花括号产生结构。

4. **后处理问题**：模型可能输出额外的礼貌语句（如"sure, here's the JSON output..."）或 JSON 标签，导致大量后处理。

5. **约束解码（Constrained Decoding）解决方案**：
   - 给模型一个模式（schema）
   - 例如 JSON 模式：输出以花括号开始和结束，必填字段、字符串字段（"yes" 或 "no"）等
   - **有限状态机（FSM）**：因为模式有结构，解码器需要一种方式跟踪在该结构中的位置。例如：是否已开始 JSON 对象？是否在键名中？是否在冒号后值应出现的位置？
   - **关键思想**：FSM 跟踪所需结构中的当前位置。每个 token 生成后，它移动到下一个状态。该状态告诉解码器哪些 token 是有效的下一个
   - **掩码机制**：你**掩盖（mask）**下一个 token 概率中无效的 token，只允许模型从有效的 token 中采样
   - 必须先采样开括号，然后是开引号等

6. **改进效果（来自论文数据）**：
   - 2024 年没有约束时 GPT-4o 能获得 40% 成功率
   - 有约束时达到 100%
   - **代价是准确性**：模型可能正确遵循模式，但可能更容易产生错误答案

7. **API 提供**：
   - OpenAI：只需将 Pydantic 模型或原始 JSON 模式传入 response format
   - Anthropic：同样可以放入 JSON 模式或 Pydantic 模型
   - 自托管模型：不同的推理引擎使用底层库帮助约束解码

8. **下一步**：可以控制模型输出的格式。但实际内容呢？模型只能借鉴训练数据中的模式。如果你询问私有数据或训练后发生的事情，那些 token 根本不会是最可能的。如何让模型基于从未训练过的信息产生结果？这是下一个视频。

---

## 视频 8: Grounding in context（上下文中的基础）
**时长**: ~7.5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/pu29b7sl/grounding-in-context>
**视频 ID**: 10169017

### 内容总结

本视频探讨如何让模型基于训练数据之外的信息产生结果。

**核心要点**：

1. **问题根源**：模型只能借鉴训练中学到的东西。如果所需答案在训练数据中没有很好表示，模型将输出最可能的——可能是错的。模型的知识在训练日期被冻结。

2. **三种自动失败的提示**：
   - 没有来自 Acme Corp 的内部信息
   - 训练前发生的事件（如 2026 FIFA Women's Champion Cup）
   - 训练期间没有访问的药物信息

3. **模型没有"I don't know" token**：在这种情况下模型被训练没有这个 token，所以它会编造听起来对的东西。

4. **手动注入上下文**：
   - 用户可以手动注入上下文（粘贴代码或文件以调试）
   - 当代码太大、文档太多或文档不断变化时，手动注入不合适

5. **基础（Grounding）解决方案**：一组在输入上下文层用有用信息"基础"模型并自动执行的方法。

6. **四种主要方法**：
   - **RAG（Retrieval Augmented Generation）**：从存储在数据库中的相关文档块中抓取（最流行）
   - **搜索（Search）**：进行实时搜索以获取网上最新相关信息
   - **工具使用（Tool Use）**：让模型调用不同工具和 API
   - **知识图谱（Knowledge Graphs）**：用结构化信息基础模型

7. **RAG 管道详解**：
   - 文档被**分块（chunked）**和**嵌入（embedded）**，存储在向量数据库中
   - 用户提交查询
   - 该查询针对向量数据库搜索
   - 选择 top K 最相似的块（K=3 等）
   - 这些块被拼接到 LLM 的上下文窗口中
   - LLM 能够基于查询和检索到的上下文做出更好的响应

8. **RAG 的有效性**：
   - 2020 至 2025 年 5 月的系统综述确认，RAG 确实持续帮助减少幻觉，特别是过时的知识
   - **但 RAG 不是万能的**：
     - 它只是向上下文窗口注入额外的字符串
     - 检索到糟糕文档、矛盾文档或分块不当会导致问题
     - 模型将使用不正确信息产生错误结果

9. **RAG 失败案例**：
   - **矛盾文档**：例如询问如何认证内部 API 请求，检索到 V1（2021 修改）和 V2（2023 修改）两个文档，模型说两种格式都支持（实际不是）
   - **分块不当**：例如错误代码列表文件，分块可能将永久禁令错误与 30 秒恢复方法分到不同块。结果只检索到第一个块，模型认为不能从错误中恢复
   - **Loss-in-the-middle 现象**：模型倾向于关注上下文窗口的开头和结尾，放在中间的重要内容可能被忽略

10. **上下文工程（Context Engineering）**：
    - 工程师设计确保模型获得所需信息以产生准确结果的方法
    - 几个好的文档而不是许多好坏参半的文档
    - 语义或结构感知的方式分块
    - 将文档放在最容易被关注的位置（开头和结尾）
    - **RAG 不是硬性强制，是软性条件**：模型可以忽略检索到的上下文（例如用户问 OpenAI 最新模型，模型可能回退到训练中的旧信息）
    - **最终目标**：让 RAG 更可靠，但并非完全无错
    - 在医学、法律、金融等领域，人们会在 RAG 之外放置额外的验证步骤

11. **下一步**：你已经看到提示中的内容直接塑造了模型产生的内容。正确的上下文使正确的 token 更可能。但如果模型能为自身生成有用的上下文呢？如果它自己中间输出（通过逐步解决问题）能改善后续答案？这就是下一个视频的内容。

---

## 视频 9: Thinking and reasoning（思维与推理）
**时长**: ~6 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/k2cyh3/thinking-and-reasoning>
**视频 ID**: 10169018

### 内容总结

本视频探讨利用循环本身的特性来改进模型输出——让模型通过生成中间步骤（推理）来获得更好的答案。

**核心要点**：

1. **影响模型行为的不同点**：
   - **基础（Grounding）** 在输入阶段工作
   - **采样参数**（温度、Top P、Top K）和**约束解码** 在概率分布计算处工作（选择下一个 token 时）
   - **推理（Reasoning）** 来自循环本身

2. **核心思想**：模型生成的每个 token 都成为下一个 token 输入的一部分。所以如果模型利用这一点，生成有助于获得更好答案的中间步骤。

3. **需要推理的问题类型**：
   - **数学问题**：例如苹果问题，如果不推理可能直接猜错（如"five apples"）
   - **调试**：模型可能受益于迭代可能的结果，而不是一次性猜测

4. **思维链（Chain of Thought）发现**：最初只是要求模型在提示中"think step by step"。模型逐步思考，从五个苹果开始，给 Sarah 两个等，将数学问题分解，能给出正确的最终答案（两个苹果）。

5. **推理（Reasoning）作为技术术语**：
   - 模型给出不同步骤，产生通常对用户不可见的思维链
   - 通常封装在 `<think>` 标签中
   - 也可称为"思维（thinking）"作为技术术语
   - 模型实际上可能没有在思考，只是被称为"思考"
   - **Claude 示例**：你可能看到灰色文本，那是隐藏的"思考"过程。可以点击查看这些逐步发生的情况。但最终结果是暴露给用户的。

6. **自校正（Self-Correction）**：
   - 模型可以尝试某些东西，自校正，反思并意识到"那不对，让我尝试别的"
   - 例如 trace function，发现 bug 不在该逻辑，而在该窗口。然后意识到这是一个众所周知的解决方案，是正确的
   - 会经历所有可能性才达到最终结果，类似于一个人思考问题

7. **不完美的推理**：
   - 模型可能陷入错误的推理步骤
   - 例如模型决定代码是某种标准实现，导致不同结果
   - 如果模型无法通过该过程自我校正，它将遵循完全不同的思维链
   - 可能得出错误结论（例如用户有过时的 Python 版本）

8. **多轮对话中的推理**：
   - 在上下文窗口中，问一个问题，模型产生答案附加到上下文，再问下一个问题
   - 推理区域（带 think 标签的）是作为输出产生的
   - **问题**：如果只是不断追加，推理区域会填满上下文窗口
   - **解决方案**：通常**每轮都丢弃推理区域**，不附加到上下文窗口
   - 仍然使用该"草稿空间"进行思考，但不附加到上下文窗口
   - 只有答案附加到上下文窗口
   - **Claude 的处理方式**：推理被丢弃
   - **一些最新模型**：某些提供商至少保留思维过程的摘要，而非全部丢弃，因为其中有模型之前尝试过的内容，可以防止模型再次尝试该错误解决方案

9. **Module 1 总结**：
   - LLM 作为自回归循环工作
   - 自回归行为不完全可预测，可以有许多不同路径
   - 有一组策略可以在不同阶段改进模型行为：
     - **基础** 在输入处工作
     - **采样参数** 和 **约束解码** 在计算概率处工作
     - **推理** 通过生成改进模型上下文的中间结果工作
   - 所有这些方法都有注意事项，谨慎使用并结合使用
   - 一切（从自回归循环到采样、幻觉、基础、推理）都来自同一过程：模型输出概率分布并一次选择一个 token
   - 你一直在从外部观察、影响和改进该过程
   - 但你还没看过该概率分布实际上是如何产生的。这就是 Module 2 的内容

---

# Module 2: LLM internals and attention（LLM 内部机制与注意力）

**Module 概述**：你已经看到了模型如何行为——循环、采样、从该过程涌现的行为。但到目前为止一切都是关于模型做什么，而不是如何做。到目前为止你将 LLM 视为黑盒——token 进，token 出。本模块打开黑盒，从最重要的部分开始——**注意力（attention）**。注意力是使得下一个 token 预测从输入中具有上下文感知能力的机制。

---

## 视频 10: Attention（注意力）
**时长**: ~9 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/79yzr2/attention>
**视频 ID**: 10170020

### 内容总结

本视频深入讲解 Transformer 中最关键的机制——注意力（attention）。

**核心要点**：

1. **为什么需要注意力**：模型需要理解单词在上下文中的含义，就像你我一样。例如上下文"the dog bit"中，bit 是"咬"；如果是"a little bit"，bit 是"少量"；如果是"set the bit"，bit 是"一位数据"。单词 bit 可能有这么多不同含义，**上下文对理解含义至关重要**。

2. **输入序列的准备**：
   - 每个序列被分解为 token
   - 每个 token 获得一个 ID（在整个词汇表中的 ID）
   - "bit" 的 token ID 是 2699
   - token ID 被转换为**独热向量（one-hot vector）**：整个词汇表中除了 2699 槽是 1 外，其他都是 0
   - **嵌入矩阵（embedding matrix）**：该矩阵表示词汇表中每个 token 的语义含义
   - 将独热向量与嵌入矩阵相乘，得到该 token 的嵌入

3. **嵌入的局限性**：
   - "bit" 在"a little bit"或"set the bit"中是与"the dog bit"中相同的单词，因此会得到**相同的 token 嵌入**，即使它们有不同的含义
   - 在这个阶段，**没有周围上下文影响这个表示**
   - 这对于模型预测下一个 token 是问题，因为它不能区分上下文含义

4. **注意力的作用**：使该 token 能够关注它之前的其他 token，以获得其含义的更好表示。

5. **多头注意力（Multi-Head Attention）**：
   - 注意力不是单一流程，**并行发生**
   - 有许多注意力头（attention heads），这些头被设计为学习不同的事物
   - 例如，一个头可能学习动词如何连接到主语；另一个可能学习代词如何指回它们引用的名词
   - 这些方式并不严格，是模型学习表示本身的不同方式
   - 然后它们的输出被组合成单一表示
   - 输入向量已被原始 token 序列中其他 token 以多种方式（跨头）塑造，然后拼接在一起作为输出
   - 输出是**非常上下文感知的**

6. **单注意力头的工作机制**：
   
   - **三个权重矩阵**：
     - **Query（查询）**：表示 token（如 "bit"）试图找出"谁与句子中的我相关，谁咬的，谁被咬"
     - **Key（键）**：试图广告自己，"作为 token bit，我能提供什么"
     - **Value（值）**：表示 token 的语义内容
   
   - **维度信息**：
     - 在此模型中，嵌入是 1024 维
     - 有 16 个注意力头
     - 完整嵌入维度跨头拆分，每个头处理 64 维 query、key 和 value 向量
   
   - **因果掩码（Causal Mask）**：
     - token 可以关注自身，但不应关注 "dog" 或 "bit"（未来）
     - "bit" 可以关注 "the" 和 "dog"
     - "dog" 可以关注 "the" 和自身
     - "the" 只能关注自身
   
   - **计算过程**：
     - **分数矩阵（Score Matrix）**：将不同的 query 向量与 key 向量做**点积（dot product）**
     - 高数字意味着 query 和 key 向量在同一位置有大值，意味着应关注那里
     - 低数字意味着不要过多关注
     - 缩放后，正负值都有
     - 应用因果掩码，将上三角设为负无穷，只看下三角
     - **Softmax**：通过 softmax 函数得到概率分布
     - 得到注意力权重（0-1 之间的数字）
     - 决定 token 应该多大程度上关注序列中每个其他 token 和过去的 token
   
   - **最终输出**：使用 value 向量（表示 "bit" 的语义内容）更新 "bit" 的表示，基于它应关注 "the" 和 "dog" 的位置。最后得到**上下文感知的输出嵌入**。

7. **多头拼接**：
   - 几个注意力头并行运行，每个有不同学习权重，产生自己的输出
   - 将所有这些头的输出**拼接（concatenate）**，回到原始 token 嵌入大小
   - 那是一个注意力层的输出
   - "bit" 在"the dog bit"中现在有不同的表示，因为关注了不同的 token，有不同的权重

8. **核心要点总结**：
   - 每个注意力头创建 query、key 和 value 向量
   - 可以取 query 和 key 的**缩放点积（scaled dot product）**得到注意力分数
   - 可以使用 **softmax** 将其转换为概率分布，作为权重
   - 然后乘以 value 向量得到一个头的输出
   - 最后可以拼接所有头的输出，得到注意力层的最终输出

9. **下一步**：注意力给每个 token 一个由周围 token 塑造的新嵌入。但模型实际上知道 token 在序列中的位置吗？例如"the dog bit the man"和"the man bit the dog"有相同的输入 token，但词序明显重要。模型能区分吗？如何处理位置信息？这是下一个视频。

---

## 视频 11: Positional encoding（位置编码）
**时长**: ~5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/2fn8lb/positional-encoding>
**视频 ID**: 10169020

### 内容总结

本视频探讨模型如何处理位置信息，因为注意力本身对词序不敏感。

**核心要点**：

1. **问题**：注意力已能让 "the dog bit" 中的 "bit" 与 "a little bit" 中的 "bit" 有不同表示（关注不同 token）。但"the dog bit the man"和"the man bit the dog"呢？

2. **注意力的局限**：
   - 相同的词汇，词序不同，意义完全不同
   - 如果用相同的学习权重运行这两个通过注意力，输出嵌入会不同吗？答案是**不会**
   - "man" 的输出嵌入与 "dog" 和 "bit" 看起来一样
   - 能区分 "the dog bit" 中 "bit" 含义的模型，**实际上不能区分** "the dog bit the man" 和 "the man bit the dog"
   - 因为注意力在没有额外信息的情况下，看到这两个是相同的，因为序列包含完全相同的 token。**不是词序敏感的**

3. **解决方案：位置编码（Positional Encoding）**：
   - 给每个 token 关于它所在序列位置的信息，在进入 Transformer 之前
   - 当 query 和 key 被比较时，嵌入已经携带该位置信息
   - **加性位置嵌入**：你可能有第 0、第 1、第 2 token 的位置嵌入，然后加上输入嵌入 "the dog bit"，得到最终位置感知嵌入
   - "the dog bit the man" 和 "the man bit the dog" 现在有不同的最终嵌入

4. **位置向量的来源**：
   - **固定数字**：简单的固定位置编码
   - **学习位置嵌入（Learned Positional Embeddings）**：类似于你学习不同 token 的嵌入矩阵
     - 有独热向量代替 token ID，索引是该位置（如第 10 位）
     - 然后映射到学习嵌入矩阵
     - 模型学习数字，然后获得该位置的最终嵌入
   - **问题**：使用学习位置嵌入时，存在最大序列大小（如 512）。不能有第 513 位位置
   - **问题**：嵌入也编码绝对位置，编码的是确切的绝对位置，而不是不同 token 之间的**相对距离**

5. **为什么相对位置重要**：
   - 对于语言，许多情况下 token 的相对位置更重要（至少在英语中）
   - 例如 "neither" "nor"：可以在不同长度间隔下仍然合理
   - 动词 "is" 必须与主语 "cat" 一致，而不是更近的名词 "mat"
   - 这些 token 的相对距离对语言语义理解真正重要

6. **RoPE（Rotary Positional Embeddings）**：
   - 更现代的技术，被当今大多数 LLM 使用
   - **关键差异**：RoPE **不添加到输入嵌入本身**，而是对 query 和 key 进行操作
   - 使用**旋转（rotation）**根据 token 的位置旋转 query 和 key 向量
   - **关键性质**：当你对两个旋转后的向量取点积时，结果取决于它们**角度的差异**，而不是确切的绝对角度
   - 这就是相对位置部分自然地从 RoPE 的数学中涌现，无需额外计算
   - **重要优点**：RoPE 不限制在训练时的最大序列长度。它能够**扩展上下文**

7. **NoPE（无位置编码）**：
   - 一篇论文探讨在某些条件下，模型可以学习从因果掩码本身推断词序
   - 这是非常隐式的位置信息，无需添加任何额外位置信息
   - 这是一个有趣的开问：模型需要多少位置信息 vs 从输入结构本身能推断多少

8. **下一步**：现在你知道模型如何通过注意力机制处理位置信息。但注意力不是全部，**它只是 Transformer 层内发生的一部分**。还有更多事情发生，最终必须将所有这些转化为你在 Module 1 中看到的概率分布。

---

## 视频 12: Model layers（模型层）
**时长**: ~7 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/y8sw6e/model-layers>
**视频 ID**: 10169021

### 内容总结

本视频探讨 Transformer 层内除了注意力之外的其他组件。

**核心要点**：

1. **Transformer 层的完整组成**：
   - 不只是注意力，还有 **MLP 层（multi-layer perceptron layer，多层感知机层）**
   - 也不是只有一个 Transformer 层，可以**堆叠多个 Transformer 层**
   - 通过堆叠层，模型可以构建丰富的表示，导致更好的预测
   - **参考**：Qwen3-0.6B（驱动本课程交互式可视化的小模型）有 28 个 Transformer 层。更大的模型可以有大约 100 个

2. **Transformer 层内的两部分**：
   - **注意力**：信息在 token 位置之间**混合**
   - **MLP**：**不**在 token 位置之间混合信息，使用自己的学习权重**独立转换**每个位置的向量

3. **MLP 的工作原理**：
   - 简单的**前馈层（feed-forward layer）**
   - **三个主要步骤**：
     - **步骤 1**：将向量投影到更高的**隐藏维度大小**。扩展网络给它更多工作空间
     - **步骤 2**：应用**非线性激活函数**。现代的是 SwiGLU（你可能学过 ReLU），本质上是某种非线性
       - 非线性很重要，因为没有它，堆叠层变换实际上只是塌缩为一种线性变换
       - 非线性允许每层捕获前一层无法捕获的不同模式
     - **步骤 3**：投影回原始维度或你需要的维度
   
4. **MLP 的重要性**：
   - 虽然注意力获得大量关注，但在许多模型中，**大部分参数位于 MLP 层**
   - 模型学到的很多东西实际上反映在这些层如何转换表示，然后将表示传递到下一层
   - 尽管这些层扮演着巨大角色，但很难精确解释这些转换在做什么
   - **有趣的研究结果**：研究人员编辑 MLP 层中的权重，使通常将埃菲尔铁塔与巴黎关联的模型改为将其视为在罗马。这种变化在不同的提示中显现出来，包括旅行问题和关于附近地方的问题
   - 其他研究表明**层与层之间相互构建**：早期层通常获取更**表面**的模式，后期层倾向于获取更**基于含义**的模式

5. **残差连接（Residual Connections）**：
   - 在堆叠层之间，通常有**残差连接**——短路不同层的额外连接
   - 帮助训练这些模型更加稳定，使其能够达到极大深度
   - 更深的网络能够学习更复杂的表示
   - 除了在训练稳定中扮演最大角色，它们在推理期间仍然是计算的一部分
   - 因为模型是用这些残差路径学习的，每层将其更新添加到从早期层传递的表示中

6. **Logit Lens**（研究工具）：
   - 你可以使用语言模型头在第一层之后或某个中间层之后查看概率分布的样子
   - 可以看到概率分布的结构如何涌现
   - **重要提示**：这是研究工具，可能不是该模型实际表示的真实表示
   - 但它给出了它可能是什么样的视图
   - **有趣观察**：随着层数加深，预测从几乎均匀分布在词汇表上（有点噪声）变为国家或欧洲国家、重要城市，最后是巴黎因为提示是"法国的首都是什么"

7. **整合所有内容**：
   - 从表示为 token 嵌入的输入序列开始，相同 token 之间的向量相同，与上下文无关
   - **注意力层**：通过与周围 token 混合信息以及通过 RoPE 编码的位置信息来塑造它
   - **MLP 层**：进一步丰富该表示
   - 经过许多这些 Transformer 层（注意力、MLP 和残差连接），每层都将其贡献添加到之前的内容，token 具有全新的表示，可以区分 "the dog bit" 与 "a little bit" 或 "the dog bit the man" 与 "the man bit the dog"
   - 这些新表示导致模型对序列中接下来是什么的预测
   - 通过自回归循环一次又一次地这样做

8. **下一步**：这些仍然是嵌入，是模型内部的向量。必须有东西将它们转换为整个词汇表上的概率分布。这是下一个视频要看的。

---

## 视频 13: Decoding（解码）
**时长**: ~4.5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/bvlmk183/decoding>
**视频 ID**: 10169022

### 内容总结

本视频讲解 Transformer 最后一个组件——语言模型头（language model head）。

**核心要点**：

1. **语言模型头（Language Model Head）**：
   - 在所有这些层的末端坐着最后一个组件——语言模型头
   - 它的任务是接受 Transformer 的输出，为词汇表中的**每个 token 产生一个分数**
   - 最终导致在该自回归循环中选择下一个 token 的概率分布

2. **完整流程回顾**：
   - Transformer 接受原始 token
   - 通过嵌入层
   - 经过若干 Transformer 层的注意力和 MLP
   - 然后在所有这些层的末端，是语言模型头
   - 产生整个词汇表 token 的分数，最终产生概率分布

3. **具体示例（"the dog bit"）**：
   - Transformer 在每个 token 位置产生一个隐藏状态（"the"、"dog"、"bit" 各一个）
   - 为了进行预测，**只有最后一个"bit"是重要的**
   - "bit" 是这里唯一看到前面 token 的，其最终隐藏状态受所有其他 token 影响
   - 模型的整个预测归结为这个**单一向量**

4. **Unembedding 矩阵**：
   - 取最后 token 嵌入（在 Transformer 层之后）
   - 放入称为 **unembedding 矩阵**的东西
   - 名字如其意：取消嵌入，放回词汇分数
   - 通常 unembedding 矩阵如何工作：我们做**权重绑定（weight tying）**
   - 与开头的嵌入矩阵绑定，相同权重
   - 减少推理和训练期间的内存
   - 输出是**词汇分数**，这些原始分数称为 **logits**
   - 每个词汇表 token 都有一个 logit，有些为正，有些为负
   - 本身还不是概率

5. **Softmax**：
   - 在这一点上，模型使用与之前在注意力中看到的**相同的 softmax 操作**
   - 但现在它应用于不同的分数集
   - 在注意力中，softmax 将注意力分数转换为注意力权重
   - 在这里，它将词汇 logits 转换为下一个 token 概率

6. **采样控制的连接**：
   - 这就是一些之前看到的采样控制与模型原始输出连接的地方
   - **温度（Temperature）**：通过在 softmax 之前缩放这些 logits 来工作，使最终分布更尖锐或更平坦
   - **Top K**：也可以在 logit 阶段应用，因为它仅取决于哪些 token 具有最高分数

7. **完整流程总结**：
   - 语言模型头有 unembedding 矩阵和 softmax
   - 接受最后 token 的隐藏 token 嵌入
   - 确实获得每个 token 的输出概率分布
   - 不仅最后一个 token，所以每个 token 都有
   - 训练时用于预测下一个 token（因为已掩码后续 token）
   - 推理时通常只使用最后位置的 logits 预测下一个 token

8. **训练 vs 推理**：
   - 在训练中，所有这些预测都用于计算损失
   - "dog" 看不到 "bit" 的原因是因果掩码
   - 在推理时，通常只使用最后位置的 logits 预测下一个 token
   - 这种在每个位置产生预测的能力以后会很有用
   - 在 Module 3 中，你会看到它如何通过称为**推测解码（speculative decoding）**的技术帮助加速生成

9. **下一步**：这就是前向传播。现在你可以开始理解涉及多少计算。记住，自回归循环为每个生成的 token 运行。在 Module 3 中，你会看到让它在真实硬件上工作需要什么，使其快到足以实际服务用户。

---

# Module 3: Scaling and deploying（扩展与部署）

**Module 概述**：你已经看到了前向传播，所有跨注意力头、跨层的矩阵乘法。在本模块中，你将研究当你尝试在真实硬件上运行此模型时会发生什么。研究这些数学如何在 GPU 上运行，以及诸如 KV caching、flash attention、量化等优化。这些是使这些更大的前沿模型快到足以实际服务用户的技术。

---

## 视频 14: Putting the model in production（将模型投入生产）
**时长**: ~4 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/bvlmka/putting-the-model-in-production>
**视频 ID**: 10169023

### 内容总结

本视频介绍 Module 3，讨论在真实硬件上运行模型的挑战。

**核心要点**：

1. **已学内容回顾**：
   - 前向传播，所有跨注意力头、跨层的矩阵乘法
   - 嵌入层接受输入 token
   - Transformer 层（每个内部有注意力层和 MLP 层）
   - 所有这些进入语言模型头，产生词汇表 token 上的概率分布

2. **规模有多大**：
   - 以中型 700 亿参数模型为例（700 亿权重）
   - 会占用**大量空间**并需要**大量计算**
   - 占用 **280 GB 内存**
   - 单次前向传播涉及数十亿次单独乘法
   - 自回归循环为模型生成的每个 token 运行整个过程一次
   - 生成仅 500 个输出 token 意味着通过它**所有 500 次**

3. **为什么这对你很重要**：
   - 从模型获取响应可能**非常慢**
   - 系统无法处理负载，没有足够的容量
   - 成本**非常高**，硬件非常昂贵

4. **数学实际发生在哪里**：
   - 数学在 **GPU** 上运行
   - GPU 加速该数学，使其能非常快速地完成
   - GPU 有两个最重要的组件，有真实的限制：
     - **计算单元（compute unit）**：实际进行矩阵乘法的工作。**数千个**这样的小计算单元**并行工作**
     - **内存（memory）**：存储模型权重以及其他东西的空间。GPU 有固定数量的此内存，称为 **VRAM**
   - 280 GB 模型甚至无法单独放在 GPU 上。必须**分片（shard）**，将模型拆分跨多个 GPU

5. **具体数字**：
   - 高端 GPU 有 288 GB VRAM，可以适合 280 GB 模型
   - 即使模型确实适合内存，还有另一个约束
   - 内存和计算单元在芯片内**物理上是分开的**
   - 数据必须**在它们之间传输**
   - 该通道有**有限的速度**，就是**内存带宽（memory bandwidth）**
   - 每次前向传播基本上需要从 VRAM 读取所有权重矩阵到计算单元进行该数学运算
   - 当你有数十亿权重时，那是大量数据来回移动
   - **该移动的速度**通常决定 GPU 工作多快，即使计算单元本身可以更快

6. **三个核心约束**：
   - **有限内存**：是否有足够的空间存储一切？权重、中间计算、激活、输入 token、缓存一些计算
   - **有限带宽**：有限的内存带宽。能否避免不必要地移动东西？
   - **计算成本**：是否优化了正在进行的计算？能否通过存储/缓存一些结果来避免重复自己？

7. **下一步**：所有不同的计算、模型中的所有矩阵乘法都必须在 GPU 上运行以加速。GPU 可以计算所有这些矩阵乘法，但也需要存储你的模型。该存储空间、内存是**有限的**。处理该有限内存的一种方法是**缩小模型**并以**更低精度**表示它。这称为**量化（quantization）**，下一个视频将探讨。

---

## 视频 15: Quantization（量化）
**时长**: ~5.5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/pu29ba/quantization>
**视频 ID**: 10170019

### 内容总结

本视频深入探讨量化技术——用更少的位表示权重。

**核心要点**：

1. **内存计算**：
   - 700 亿参数模型需要约 280 GB 内存作为标准精度
   - 700 亿参数权重以 **FP32**（32 位浮点数）存储
   - 8 位在一字节中，所以 32 位是每个权重 4 字节
   - 乘以 700 亿得到约 280 GB
   - 如果你的 GPU 只有 192 GB VRAM，它无法存储它

2. **量化的作用**：
   - 通过用**更少的位、更低的精度**表示每个权重来**缩小模型**
   - 仍然相同数量的权重，相同数量的参数，但每个权重用更少的位表示
   - **FP32 → FP16**：16 位，模型减半（140 GB）
   - **FP32 → INT8**：8 位，更小（70 GB）
   - **FP32 → 4 位**：更小（35 GB），可以适合单个 192 GB GPU

3. **小模型 vs 量化模型**：
   - 小模型：参数数量较少的模型。可以是全精度或量化
   - 量化模型：关于模型权重的精度。可能是被量化为较小表示的巨大模型

4. **具体例子**：
   - 从 32 位浮点数到 8 位整数
   - 通过取该数字的近似值加一些缩放因子来量化，并单独存储缩放因子
   - 例如缩放因子为 0.01031
   - **5 个数字示例**：
     - FP32: 5 × 32 位 = 160 位（20 字节）
     - INT8: 5 × 8 位 = 40 位
     - 加缩放因子（32 位）= 72 位（9 字节）
   - 显著减少内存

5. **Qwen3 示例**：
   - 140 亿参数变体
   - 在 BF16（16 位）下占用约 30 GB RAM
   - 降低精度后可以很小
   - 较小的一些可以放在消费级 GPU 上
   - 可以服务在边缘，例如机器人

6. **其他好处**：
   - 除空间外，更小的数字可以**更快地通过内存带宽移动**
   - 减少 RAM 和计算单元之间的内存带宽开销
   - **更快的推理**有两个原因：
     - 数字以低精度表示移动更快
     - 如果硬件针对它优化，计算也可能更快

7. **权衡 - 精度降低**：
   - FP32 可以表示比 INT8 大得多的值范围
   - 在权衡精度
   - 精度可能导致模型输出不同，可能导致**准确性退化**
   - 来自单个权重只有少量偏差可能不大，但会与数十亿计算复合
   - 舍入误差将改变从模型采样的概率分布

8. **混合精度实践**：
   - 实际上，**一切都是混合精度**
   - 不是将所有内容都量化到小精度
   - 模型中有些操作对微小变化**超敏感**：softmax 操作、归一化层、MLP 中的非线性激活函数
   - 真实实现将是混合精度
   - 大部分计算可能在低精度上运行，但需要在某些地方**反量化**
   - 例如：在激活函数之前反量化。然后可以重新量化进行下一组操作

9. **应用场景建议**：
   - **聊天机器人**：量化可以相当激进
   - **编码应用**：在准确性上非常重要，可能更难以接受量化模型
   - 准确性、速度和成本之间的权衡是**测试出来的**，像所有 AI 应用一样，高度经验性

10. **量化总结**：
    - **优点**：更小的整体内存占用，可能更快的推理
    - **缺点**：通过舍入有效获得性能退化
    - 量化解决了最直接的问题，让模型适合 GPU 内存
    - 作为奖励，还通过使每条数据更小来减少带宽瓶颈
    - 但适合模型在内存中只是**第一个约束**
    - 即使有量化模型加载，自回归循环仍为每个 token 重复大量计算
    - 其中很多计算是**冗余的**
    - 下一个视频探讨该问题

---

## 视频 16: KV cache（KV 缓存）
**时长**: ~4 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/fwabdc/kv-cache>
**视频 ID**: 10169025

### 内容总结

本视频讲解 KV 缓存——消除自回归循环中的冗余计算。

**核心要点**：

1. **冗余计算的来源**：
   - 量化解决了第一个问题，模型现在适合 GPU 内存
   - 但自回归循环中仍有冗余计算
   - 模型生成下一个 token 时，**重新计算**许多它已经用于第一个 token 的 key 和 value 投影
   - 这些是相同的结果
   - 重新计算相同的东西时怎么办？**缓存它**

2. **为什么只需要缓存 K 和 V**：
   - 深入到数学：query 向量与 key 向量相乘，得到注意力权重，然后乘以 value 投影得到输出
   - 当模型生成下一个 token 时，**所有这些都无关紧要当新 query 到来时，只是该 query 自身，而不是之前 token 的 query**
   - **Query 向量不必缓存**：
     - Query 代表新 token 寻找什么
     - 对当前正在处理的该新 token 是特定的
     - 缓存它无益
   - 当新 token 到来时，只需计算它自己的 key、value 和 query
   - 需要每个新 token 的**新 query**，计算它在整个序列上的注意力
   - **Key 和 Value 不同**：当新 token 到来时它们不变，可以存储并重用它们，这就是 **KV Cache**

3. **KV 缓存的构建**：
   - 对每个 Transformer 层，KV Cache 应用于模型中的每个注意力层
   - 给出提示时构建 KV Cache，有两个阶段：
     - **Prefill（预填充）**：所有提示 token 通过所有 Transformer 层，构建 KV Cache。可以并行完成
     - **Decode（解码）**：一次获得下一个 token。对于每个新生成的 token，KV Cache 不断构建

4. **KV 缓存的作用**：
   - 移除自回归循环中的冗余计算
   - 通过存储和重用来自之前 token 的 key 和 value 向量
   - **计算从二次变为线性**

5. **KV 缓存的代价 - 内存**：
   - 缓存占用空间，占用内存
   - 节省计算，但需要存储
   - 随着对话增长，缓存本身会增长
   - 与模型竞争 RAM/内存空间
   - 如果 KV Cache 巨大，它将占用更多空间，意味着新请求的 VRAM 更少，实际上**降低吞吐量**
   - 像存储在内存中的任何东西一样，需要在某些时刻访问，所以内存带宽也重要

6. **KV 缓存的影响因素**：
   - 不只是模型权重，还有与模型的对话长度
   - 提示和输出的长度
   - 影响 GPU 选择
   - 影响量化思考方式
   - 影响限制最大上下文长度
   - 使用模型 API 时，读取和写入 KV Cache 的成本有时会显现出来

7. **下一步**：
   - 已解决两个约束：适合模型和避免冗余计算
   - 但仍有 GPU 内部那些计算期间数据如何移动的问题
   - 即使有 KV Cache，注意力计算涉及构建大型中间结果并在内存和计算之间来回移动
   - 下一个视频看一种减少该移动的技术

---

## 视频 17: Flash attention（Flash 注意力）
**时长**: ~6 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/mo0xyj/flash-attention>
**视频 ID**: 10169026

### 内容总结

本视频讲解 Flash Attention——优化 GPU 内部数据移动的技术。

**核心要点**：

1. **未解决的问题**：
   - KV Cache 消除了冗余计算，模型不再重新处理之前的 token
   - 但即使对于单 token 的注意力计算，GPU 内部仍有大量数据来回移动
   - 在内存和计算之间移动数据可能**非常慢**

2. **GPU 内存层次结构**：
   - GPU 有大型主内存部分（VRAM），存储模型权重和 KV Cache
   - 还有计算单元内部较小的内存部分，计算单元在计算期间使用它来快速移动
   - 不适合那里的东西（大多数东西）必须从 VRAM 加载然后写回
   - 当数据量大需要在 VRAM 和计算单元内内存之间传输时，那些**读写往返可能成为相当大的瓶颈**

3. **内存带宽**：
   - 计算单元可能闲置，等待数据从 VRAM 到来
   - 这不好，希望充分利用 GPU

4. **标准注意力的数据流**：
   - 从 VRAM 加载 query 和 key 矩阵到计算单元内存区域
   - 将它们相乘产生分数矩阵（**序列长度的平方**，很大）
   - 将分数矩阵从 VRAM 加载到工作区，应用 softmax 得到注意力权重矩阵
   - 将其写回 VRAM
   - 从 VRAM 加载注意力权重矩阵加上 value 矩阵，将它们相乘得到最终注意力输出
   - 将最终输出写回 VRAM
   - **两个完整的读写往返**。对于长序列，这变得巨大。**内存带宽而非计算成为瓶颈**

5. **问题**：如果它已经在计算单元中，为什么必须写回 VRAM？
   - 主要由于 **softmax**
   - 要计算任何位置的注意力权重，softmax 需要在单行中所有分数之间**归一化**
   - 需要为该行计算所有分数，然后才能进行 softmax
   - 不能在首先有该行所有分数的情况下计算任何 token 对的最终注意力权重

6. **Flash Attention 解决方案**：
   - 不计算所有分数、所有权重然后输出，而是工作在**更小的块（blocks）**中
   - 加载小块的 query 和小块的 key、value 到更快的计算单元工作区
   - 计算该块的**部分结果**，然后**累积**向最终输出
   - 然后移动到下一个块
   - **处理 softmax 部分**：softmax 的分母仍需要该完整行。Flash Attention 通过维护 softmax 的**运行修正（running correction）**来处理。当新块分数到达时，更新部分结果以考虑该新信息
   - 分数矩阵和 softmax 权重**永远不会作为完整矩阵存在于 VRAM 中**
   - 计算直接从那些 QKV 块到部分输出，全部在快速计算单元工作区内
   - 唯一写回 VRAM 的是最终注意力输出
   - **最终结果在数学上仍然与标准注意力相同**，不是近似

7. **Flash Attention 的好处**：
   - 内存使用显著降低：标准注意力需要 O(n²) 内存（n 为序列长度）。Flash Attention 不需要那么多
   - 释放内存用于其他用途（如 KV Cache）
   - VRAM 和计算单元工作区之间的往返次数更少
   - 注意力计算更快，特别是对于更长的序列长度
   - **token 数量很重要**，因为它与 token 数量成二次方缩放
   - 较长的序列长度获得更大的收益

8. **需要注意的事项**：
   - Flash Attention 在前向传播和推理中获得巨大的内存带宽收益
   - 但在反向传播和训练中，Flash Attention 确实使用**比标准注意力更多的 flops**
   - 这真的是关于何时是**内存受限**而不是计算受限

9. **应用现状**：
   - Flash Attention 是每个现代推理框架和库的标准
   - 如果你使用 API 或像 VLLM 这样的服务框架的最近模型，Flash Attention 可能在底层运行

10. **总结 - 三个优化技术**：
    - **量化（Quantization）**：使数据更小，更低精度，所以适合内存，移动更快
    - **KV Cache**：避免重新计算未更改的 key 和 value 向量
    - **Flash Attention**：避免在注意力期间来回移动这些大型中间结果
    - 综合起来，它们使每次前向传播极其高效
    - 但即使是大模型的优化前向传播也需要时间。仍有数十亿参数要处理，数十亿计算要执行

11. **下一步**：
    - 自回归循环对每个 token 运行这次昂贵的前向传播
    - 如果生成 500 个 token，就是 500 次
    - 如果能用**更少的大模型前向传播**获得相同结果呢？接下来

---

## 视频 18: Speculative decoding（推测解码）
**时长**: ~7 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/9i8qmm/speculative-decoding>
**视频 ID**: 10169027

### 内容总结

本视频讲解推测解码——通过小模型预测、大模型并行验证来加速推理。

**核心要点**：

1. **未解决的问题**：
   - 即使是优化的大模型前向传播仍然昂贵
   - 仍有数十亿权重要读取，数十亿计算要执行
   - 每个生成的 token 都是如此

2. **核心洞见**：
   - 对许多 token（常见词、语法事物如标点、可预测短语），实际上**更小的模型可以产生与大模型相同的预测**
   - 仅运行更大的模型来预测逗号就像用超级计算机做基本数学
   - 它会得到正确答案，但有更便宜、可能更快的方法可以使用

3. **推测解码（Speculative Decoding）**：
   - 不使用巨型模型（target 模型，如 700 亿参数）
   - 而是对于大多数事情可以使用**更小的模型**（draft 模型，可能 10 亿参数）
   - 更小的模型更快、**不太准确**，但更大的模型有所有这些额外参数，所以更好但更慢

4. **工作流程**：
   - 使用 draft 模型解码并生成**候选 token**
   - 然后 target 模型可以**并行**检查该工作
   - **关键洞见**：检查工作比生成和解码**效率高得多**
   - 当模型**同意**时，可以保留 draft 模型的 token
   - 当它们**不同意**时，必须重新采样（例如使用 target 模型）

5. **为什么更快**：
   - 你可能想：如果 target 模型必须检查 draft 模型 token 的工作，那怎么可能更快？
   - 那不是意味着每个 draft token 需要运行 target 模型一次，这与前向传播次数相同？
   - **Module 2 知识**：模型可以处理多个 token，并在每个位置同时产生下一个 token 概率
   - 通常自回归循环仅使用最后位置选择下一个 token，但推测解码利用**其他位置**
   - 不是为每个提议的 token 运行 target 模型一次，可以将当前上下文加上提议的 token 一起给出，在**一次前向传播**中产生并行检查它们所需的概率

6. **惊人特性 - 数学等价**：
   - 推测解码可以使其**在数学上相同**
   - 输出分布**数学上等同于** target 模型自己产生的结果
   - 不是近似，以 target 模型的质量获得一小部分成本

7. **draft 模型选择的关键**：
   - 推测解码在 draft 模型不仅更小，而且**与 target 模型匹配**时效果最好
   - 例如，如果 target 模型是较大的 Qwen 模型，通常希望 draft 模型是较小的 Qwen 模型，而不是完全不同的模型家族
   - 因为如果模型更相似，draft 模型更可能提议 target 模型接受的 token
   - 如果模型差异太大，太多提议的 token 可能被拒绝，生成和检查它们的时间可能不值得

8. **具体过程**：
   - **步骤 1**：draft 模型提议候选 token
   - **步骤 2**：target 模型检查那些 token 并接受或拒绝
   - **示例**："The capital of France is" 作为提示
   - draft 模型开始预测，保存采样的 token 和下一个 token 概率分布
   - 继续："capital of France is" ".", "which", "is"，让 draft 模型跑 4 个额外 token

9. **验证 token**：
   - 输入整个 token 序列直到此点
   - 查看 target 模型的下一个 token 概率分布和给定直到现在的序列的下一个 token 概率
   - 与保存的下一个 token draft 概率分布比较
   - 如果预测该下一个 token 的概率（在 target 模型中）高于 draft 模型，则**接受**该 token
   - 如果不是，进行**有偏硬币投掷**（biased coin toss）
     - 硬币每边的概率看起来像接受与拒绝的概率
     - 如果 target 模型对该下一个 token 采样概率远小于 draft 模型，拒绝的概率应该相当高
     - 这只是重新加权分布，使其匹配如何从 target 分布采样

10. **并行验证**：
    - "Paris", ".", "which", "is"，所有这些可以**同时**通过 target 模型
    - 接受-拒绝可以通过匹配那些分布**并行发生**
    - 由于自回归生成，要拒绝**第一个拒绝之后的所有内容**，即使它们之后被接受

11. **处理拒绝**：
    - 仍可以从概率分布中采样，从 target 模型的下一个 token 概率分布和 draft 模型分布中
    - 创建新分布，考虑 target 模型的下一个 token 概率分布和已拒绝下一个 token 预测的事实
    - 从这个新概率分布采样获得下一个 token
    - 然后继续运行 draft 模型获得越来越多的下一组 token

12. **效益与代价**：
    - **大速度提升**：理想情况下如果 draft 模型接近 target 模型
    - 数据来自 Google 的 T5 transformer 模型家族
    - **代价**：使用更多内存因为运行 draft 模型
    - 可以将 draft 模型放在与 target 模型不同的硬件上以获得某些速度提升，因为它小得多
    - **关键条件**：推测解码只在 draft 模型真的在大多数时候与 target 模型一致时才有效

13. **下一步**：
    - 让模型使用这些优化运行只是开始
    - 在生产中，会面临额外挑战，如大规模管理硬件、处理不可预测的用户行为、监控系统在实际条件下的表现
    - 下一个视频涵盖一些这些实际问题

---

## 视频 19: Issues that arise in production（生产中出现的问题）
**时长**: ~5.5 分钟
**链接**: <https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/sh74q6/issues-that-arise-in-production>
**视频 ID**: 10169028

### 内容总结

本视频探讨将模型部署到生产环境时的实际挑战。

**核心要点**：

1. **已掌握的优化工具包**：
   - 量化（Quantization）
   - KV 缓存（KV cache）
   - Flash 注意力（Flash attention）
   - 推测解码（Speculative decoding）
   - 综合起来，使运行大模型快到足以服务用户

2. **生产 vs 单 GPU 优化**：
   - 优化单 GPU 的模型与在生产中运行它非常不同
   - 在生产中，有**数千用户**发送不可预测的请求
   - 会有很多用户**同时**发送请求（并发）
   - 需要能够处理该并发性的方法

3. **三种主要方法**：

   - **数据并行（Data Parallelism）**：
     - 在多个 GPU 上运行模型的**副本（replicas）**
     - 负载均衡器可以将传入请求路由到它们
     - 更多副本意味着可以处理更多并发请求
     - 所有这些提示进来，它们会被路由到不同的 GPU 并从模型并发获得响应
   
   - **动态批处理（Dynamic Batching）**：
     - 不按顺序处理这些请求
     - 系统可以将多个请求分组在单个批处理中
     - 更好地利用 GPU 的并行能力
     - 否则只运行批处理大小为 1
   
   - **数据并行 + 动态批处理**：
     - 动态批处理节点可以将请求批处理在一起
     - 然后负载均衡器能够将它们分发到进行数据并行的不同 GPU
     - 当独立请求从用户进来时，可以在它们同时进来时动态批处理它们，然后路由到正确的 GPU 全部并行进行
   
   - **模型并行（Model Parallelism）**：
     - 当模型巨大且不适合单个 GPU，或想将其分片跨许多 GPU 时
     - 许多推理服务框架（如 vLLM）会为你处理很多这些
     - 对于大多数从业者，关键只是知道这些概念存在，以便能正确配置该框架，不必从头实现

4. **常见差距 - 实验室 vs 真实世界**：

   - **不是失败，总是会有这个差距**，能越能在内部缩小它越好
   
   - **问题 1：失败分布不同**：
     - 模型可能有相似的平均基准分数，但其失败的分布非常不同
     - 模型 A 可能偶尔在许多任务上失败，但模型 B 在大多数任务上表现良好，但在少数任务上灾难性地失败
     - 平均值可能看起来一样，而用户体验不同
     - 要看分布的尾部
   
   - **问题 2：基准温度是 0**：
     - 基准通常在温度为零下运行，意味着相当确定性的输出
     - 每次得到相同答案
     - 但在生产中，人们使用更高温度以获得更自然或更多样的响应
     - 更高温度将扩大采样分布
     - 应该仍然在该更高温度下运行和测试，但无法在实验室中涵盖一切
   
   - **问题 3：基准提示通常更干净**：
     - 良好形式的
     - 真实用户查询**更混乱**：错别字、模糊措辞、可能漂移的多轮对话或与早期消息矛盾的指令
     - 越能将那种混乱纳入内部基准，越好

5. **真实案例**：
   
   - **纽约时报报道**：
     - 模型在被暴露于非常长的上下文（包括个人话题）时只在短用户查询上被评估过
     - 输出变得无用甚至可能有害
     - 主题漂移到未测试的不同领域
   
   - **Amazon Rufus**：
     - 嵌入到 Amazon 购物应用中的模型
     - 用户意识到它实际上只是 Claude 在幕后，一个通用模型
     - 用户只是提示它忽略关于购物的指令，并将其用于任何任务
     - 能够获得本应付费的模型的免费访问
   
   - **Klarna 客服**：
     - 付款平台，不是设计用于编写代码
     - 用户询问如何展平 Python 中的列表列表
     - 模型被用于设计之外的用途

6. **实验室练习**：
   - 将获得动手实践测量关键 LLM 性能指标的练习
   - 包括**延迟、内存使用和吞吐量**
   - 更好地理解服务真实模型涉及的权衡

7. **Module 3 总结**：
   - 学到了运行完整 Transformer 模型真正需要什么
   - 在这里建立的直觉应该有助于推理你工作的系统
   - 当新技术在 AI 领域出现时，你将能够更好地理解和利用它们

8. **课程总结**：
   - 跨越本课程，你已完成 Transformer 实践的导览：
     - 它们如何一次生成一个 token
     - 注意力和层如何将输入 token 转化为预测
     - 像量化、KV caching、flash attention 和推测解码这样的技术如何使这些模型在生产中更快、更高效
   - **恭喜**，期待看到你构建的东西

---

# 完整视频索引

## Module 1: Observed behavior（9 个视频）

| 序号 | 视频标题 | 时长 | 链接 | 视频 ID |
|------|---------|------|------|---------|
| 1 | Conversation between Sharon Zhou and Andrew Ng | ~4.5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/y8sw6w/conversation-between-sharon-zhou-and-andrew-ng) | 10169010 |
| 2 | Transformers in practice | ~2.5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/ldi0cw7i/transformers-in-practice) | 10169011 |
| 3 | The autoregressive loop | ~4.5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/79yzruak/the-autoregressive-loop) | 10169030 |
| 4 | Visualization tutorial | ~3.5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/de1knw6r/visualization-tutorial) | 10169029 |
| 5 | Token sampling | ~5.5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/sh74qlbh/token-sampling) | 10169013 |
| 6 | Autoregressive dynamics | ~4 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/opk78jc1/autoregressive-dynamics) | 10169015 |
| 7 | Structured outputs | ~5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/8bhr0z/structured-outputs) | 10170010 |
| 8 | Grounding in context | ~7.5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/pu29b7sl/grounding-in-context) | 10169017 |
| 9 | Thinking and reasoning | ~6 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/k2cyh3/thinking-and-reasoning) | 10169018 |

## Module 2: LLM internals and attention（4 个视频）

| 序号 | 视频标题 | 时长 | 链接 | 视频 ID |
|------|---------|------|------|---------|
| 10 | Attention | ~9 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/79yzr2/attention) | 10170020 |
| 11 | Positional encoding | ~5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/2fn8lb/positional-encoding) | 10169020 |
| 12 | Model layers | ~7 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/y8sw6e/model-layers) | 10169021 |
| 13 | Decoding | ~4.5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/bvlmk183/decoding) | 10169022 |

## Module 3: Scaling and deploying（6 个视频）

| 序号 | 视频标题 | 时长 | 链接 | 视频 ID |
|------|---------|------|------|---------|
| 14 | Putting the model in production | ~4 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/bvlmka/putting-the-model-in-production) | 10169023 |
| 15 | Quantization | ~5.5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/pu29ba/quantization) | 10170019 |
| 16 | KV cache | ~4 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/fwabdc/kv-cache) | 10169025 |
| 17 | Flash attention | ~6 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/mo0xyj/flash-attention) | 10169026 |
| 18 | Speculative decoding | ~7 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/9i8qmm/speculative-decoding) | 10169027 |
| 19 | Issues that arise in production | ~5.5 min | [链接](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/sh74q6/issues-that-arise-in-production) | 10169028 |

---

# 关键概念总结

## Module 1 核心概念

- **自回归循环（Autoregressive Loop）**：LLM 一次生成一个 token 的循环过程
- **上下文窗口（Context Window）**：模型在任意时刻能"看到"的最大文本量
- **停止条件（Stopping Conditions）**：停止 token、最大 token 限制、上下文窗口大小
- **贪婪采样（Greedy Sampling）**：选择概率最高的 token
- **温度（Temperature）**：改变概率分布的尖锐度
- **Top K / Top P**：限制候选 token 范围的参数
- **自回归动态（Autoregressive Dynamics）**：自回归过程导致的各种行为（幻觉、任务漂移、重复）
- **结构化输出（Structured Outputs）**：使用有限状态机（FSM）约束解码
- **基础（Grounding）**：在输入层加入有用信息（RAG、搜索、工具使用、知识图谱）
- **推理（Reasoning）/思维链（Chain of Thought）**：生成中间步骤改进最终答案

## Module 2 核心概念

- **嵌入矩阵（Embedding Matrix）**：将 token ID 转换为向量的矩阵
- **多头注意力（Multi-Head Attention）**：并行运行的多个注意力头
- **Query/Key/Value**：注意力的三个权重矩阵
- **缩放点积注意力（Scaled Dot-Product Attention）**：Query 与 Key 的点积得到注意力分数
- **Softmax**：将分数转换为概率分布
- **因果掩码（Causal Mask）**：防止 token 看到未来
- **位置编码（Positional Encoding）**：注入位置信息
- **RoPE（Rotary Positional Embeddings）**：旋转位置编码，自然编码相对位置
- **MLP 层**：独立转换每个位置向量的前馈层
- **残差连接（Residual Connections）**：跨层短路连接
- **语言模型头（Language Model Head）**：最终产生概率分布的组件
- **Unembedding 矩阵**：将隐藏状态映射回词汇分数
- **Logits**：原始词汇分数
- **权重绑定（Weight Tying）**：嵌入矩阵与 unembedding 矩阵共享权重

## Module 3 核心概念

- **GPU 内存与计算单元**：内存受限与计算受限
- **VRAM**：GPU 上的内存
- **内存带宽（Memory Bandwidth）**：在内存和计算之间移动数据的速度
- **量化（Quantization）**：用更少的位表示权重（FP32 → FP16 → INT8 → 4-bit）
- **混合精度（Mixed Precision）**：不同操作使用不同精度
- **KV 缓存（KV Cache）**：存储之前的 key 和 value 向量避免重算
- **Prefill 和 Decode**：KV 缓存构建的两个阶段
- **Flash Attention**：通过分块避免在 VRAM 和 SRAM 之间移动大型中间矩阵
- **推测解码（Speculative Decoding）**：用小模型提议、大模型并行验证
- **Draft 模型与 Target 模型**：推测解码的两个模型
- **数据并行（Data Parallelism）**：跨多 GPU 复制模型
- **模型并行（Model Parallelism）**：将单个模型分片跨多 GPU
- **动态批处理（Dynamic Batching）**：将多个请求分组为单个批次

---

*此总结由 AI 根据课程视频 Transcript 自动生成，仅供学习参考使用*
*生成日期: 2026-07-16*