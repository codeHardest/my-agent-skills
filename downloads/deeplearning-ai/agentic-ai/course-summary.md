# Agentic AI (课程总结)

**课程来源**: DeepLearning.AI
**课程名称**: Agentic AI
**课程链接**: https://learn.deeplearning.ai/courses/agentic-ai

---

## 课程概述

本课程由 Andrew Ng 教授讲解，介绍 Agentic AI 的核心概念、设计模式和最佳实践。Agentic AI 工作流通过将复杂任务分解为多个步骤，比传统提示更加高效。课程涵盖五大模块，包括反射模式、工具使用、评估与错误分析、规划模式和 multi-agent 系统。

---

## Module 1: Introduction to Agentic Workflows

### 模块概述

本模块介绍 Agentic AI 的基本概念、优势和设计模式。通过多个实际案例，讲解如何将复杂任务分解为离散的步骤，以及如何使用评估驱动开发过程。

### 视频 1: Welcome!
**时长**: ~2 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/pu5xbv/welcome
**视频 ID**: 10079010

### 内容总结

Andrew Ng 首次提出"agentic"一词来描述当时迅速发展的 AI 应用构建趋势。尽管市场上出现了大量炒作，但真正有价值的 Agentic AI 应用也在快速增长。课程将分享构建 Agentic AI 应用的最佳实践，掌握这项技能将是 AI 时代最重要且最有价值的能力之一。掌握评估和错误分析的驱动开发过程是区分优秀开发者和普通开发者的关键。

---

### 视频 2: What is agentic AI?
**时长**: ~5 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/nae3i1/what-is-agentic-ai
**视频 ID**: 10079011

### 内容总结

Agentic AI 工作流比标准提示更强大，因为它将复杂任务分解为多个步骤，类似于人类实际工作的方式。以写论文为例，传统方式是直接让 LLM 一次性生成整篇文章（如同打字时从不用退格键），而 agentic 工作流可以先创建大纲、进行网络搜索、写草稿、审查找漏洞、修改，甚至可以让人类进行关键审查。这种迭代过程虽然耗时更长，但能产生更好的结果。关键技能是学会将任务分解为更小、可管理的步骤，由 AI 逐一执行。一个实际例子是构建一个研究智能体，可以接受"如何建立一家与 SpaceX 竞争的火箭公司"这样的主题，然后计划研究、搜索网页、下载资源、综合发现、起草大纲、让编辑审查连贯性，最终生成综合的 markdown 报告。

---

### 视频 3: Degrees of autonomy
**时长**: ~5 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/zqs9ty/degrees-of-autonomy
**视频 ID**: 10079052

### 内容总结

AI 系统可以具有不同程度的自主性。使用"agentic"作为形容词而非二元术语（是或否 agent），承认系统可以在不同程度上具有 agentic 特性。较少自主性的 agent 示例：写一篇关于黑洞的论文，可以设计一个相对简单的 agent，提出一些网页搜索词，硬编码调用网页搜索引擎，获取一些网页，然后用它来写论文。这是较少自主性的 agent，具有完全确定性的步骤序列。较自主的 agent：给定写关于黑洞的论文的请求，可以让 LLM 决定是否要进行网页搜索、搜索新闻来源还是搜索研究论文档案，然后由 LLM（而非人类工程师）决定调用哪个网页搜索引擎，以及获取多少个网页。自主性光谱：一端是较少自主性的系统，通常所有步骤都是预先确定的，任何函数调用（如网页搜索）都是由人类工程师硬编码的；另一端是高度自主的 agent，agent 可以做出许多决定，包括决定执行任务的步骤序列。高度自主的 agent 甚至可以编写新函数或创建新工具。在这两个极端之间是半自主 agent，可以做出一些决定，选择工具，但工具通常更加预定义。

---

### 视频 4: Benefits of agentic AI
**时长**: ~4 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/k2vehc/benefits-of-agentic-ai
**视频 ID**: 10079013

### 内容总结

agentic 工作流的主要好处是：能够完成许多之前根本无法完成的任务。其他好处包括并行性（让某些事情更快完成）和模块化（可以从多个不同地方组合最佳组件来构建有效的工作流）。在编码基准测试中，GPT-3.5 直接提示只能得到 40% 的正确率，GPT-4 是 67%，但通过 agentic 工作流包装 GPT-3.5 可以获得更高性能，甚至超过下一代模型的性能。agentic 工作流还可以并行化某些任务，例如在研究 agent 中，可以并行下载多个网页，然后将所有内容汇总给 LLM 来写论文。模块化设计允许添加或更新工具，有时也可以交换模型。

---

### 视频 5: Agentic AI applications
**时长**: ~7 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/bvuwkr/agentic-ai-applications
**视频 ID**: 10079014

### 内容总结

多种 Agentic AI 应用示例：
- **发票处理**：提取账单、地址、应付金额、到期日期等字段并记录到数据库
- **客户订单查询**：提取关键信息、查找客户记录、起草回复供人工审核
- **高级客服 agent**：处理更复杂的查询，如库存查询（黑 jeans、蓝 jeans）、退货处理等，需要规划数据库查询序列
- **计算机使用 agent**：尝试使用网页浏览器完成复杂任务，如检查航班可用性

容易实现的应用特点：有明确的分步骤流程、已有标准操作程序、使用纯文本资产。较难实现的应用特点：步骤事先不知道（需要规划）、需要处理多模态输入（声音、图像、音频）。

---

### 视频 6: Task decomposition: Identifying the steps in a workflow
**时长**: ~8 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/moivygo8/task-decomposition-identifying-the-steps-in-a-workflow
**视频 ID**: 10079015

### 内容总结

任务分解的关键技能：观察某人做的事情，并识别可以实现的离散步骤。在查看各个离散步骤时，始终问自己：这一步是否可以用 LLM、或用一小段代码、或用函数调用、或用工具来实现？如果答案是"否"，那么问自己：作为人类，我会如何完成这一步？是否可以进一步分解为更小的步骤，使其更适合用 LLM 或软件工具实现。构建 agentic 工作流时使用的模块/组件：LLM/大型多模态模型、用于 PDF 转文本或文本转语音或图像分析的专用 AI 模型、各种 API（语音搜索、获取实时天气数据、发送电子邮件、检查日历等）、RAG 检索工具、代码执行工具。在开发过程中，通常需要多次迭代和改进 agentic 工作流，直到达到所需的性能水平。评估驱动开发过程非常重要。

---

### 视频 7: Evaluating agentic AI (evals)
**时长**: ~5 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/46yh5j/evaluating-agentic-ai-evals
**视频 ID**: 10079016

### 内容总结

构建 agentic 工作流后，很难提前知道可能会出现什么问题。最佳实践是先构建它，然后检查它在哪里还不满意，找到评估和改进系统的方法来消除不满意的方面。评估类型：
- **客观指标**：可以编写代码检查的错误（如是否提到了竞争对手），这类指标可以自动计算频率
- **LLM as a judge**：用于更主观的标准，可以使用另一个 LLM 来评估输出质量（如给论文打 1-5 分）

两大主要评估类型：
- **端到端评估**：测量整个 agent 的输出质量
- **组件级评估**：测量 agentic 工作流中单个步骤的输出质量

这些评估驱动不同部分的开发过程。错误分析（阅读每个步骤的中间输出以寻找改进机会）是另一个关键技能。

---

### 视频 8: Agentic design patterns
**时长**: ~7 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/rm9bg7/agentic-design-patterns
**视频 ID**: 10079017

### 内容总结

四个关键设计模式：
1. **Reflection（反射）**：让 LLM 检查自己的输出并提出改进建议，可以引入外部反馈（如运行代码看输出或错误信息）来增强效果。也可以用专门的 critique agent 来审查
2. **Tool use（工具使用）**：给 LLM 提供函数调用能力，如网页搜索、代码执行、数据库查询、日历/邮件集成、处理图像等
3. **Planning（规划）**：LLM 自动决定完成任务的步骤序列（如 HuggingGPT 示例：确定姿势、生成图像、描述图像）
4. **Multi-agent collaboration（多智能体协作）**：多个 agent 具有不同角色（如 CEO、程序员、测试员、设计师）协作完成复杂任务（如 ChatDev 软件开发框架、营销 brochure 生成）

---

## Module 2: Reflection Design Pattern

### 模块概述

反射设计模式是一个简单但有效的技术，可以让系统性能获得显著提升。通过让 LLM 审查自己的输出或引入外部反馈，可以迭代改进生成内容。

### 视频 1: Reflection to improve outputs of a task
**时长**: ~4 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/shknq1/reflection-to-improve-outputs-of-a-task
**视频 ID**: 10079018

### 内容总结

人类有时会反思自己的输出并找到改进方法，LLM 也可以做同样的事情。例如，可以先让 LLM 写第一版邮件，然后让同一个或不同的 LLM 反思并写出改进的第二版。反思可以应用于各种输出：代码（如检查 bug）、邮件、HTML 表格、JSON 数据结构、指令集、域名生成等。写反思提示的建议：
- 明确指出要审查或反思第一版输出
- 指定清晰的标准（如域名是否易读、是否有负面含义；邮件则检查语气、验证事实）
- 多读别人的提示来学习好的写法

有时不同的 LLM 适合不同的任务，例如用推理模型（thinking models）来检查 bug 比普通模型效果更好。

---

### 视频 2: Why not just direct generation?
**时长**: ~5 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/uz37v2/why-not-just-direct-generation
**视频 ID**: 10079019

### 内容总结

直接生成（zero-shot prompting）是直接提示 LLM 生成答案一次完成。反射则是在生成第一次后，让 LLM 审查并改进输出。多项研究表明，反射在各种任务上都能改善直接生成的性能。反射可以帮助的场景：
- 生成结构化数据（如复杂 HTML、嵌套 JSON）时的格式错误
- 生成指令集（如泡茶步骤）时可能遗漏步骤
- 生成域名时可能有意外含义或难以发音

使用外部反馈（如执行代码看输出或错误信息）比仅靠 LLM 自身反思要强大得多。

---

### 视频 3: Chart generation workflow
**时长**: ~4 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/moivym/chart-generation-workflow
**视频 ID**: 10079020

### 内容总结

在图表生成工作流中，反射可以显著改善输出质量。例如，生成咖啡销售数据可视化时：
- v1 代码生成的堆叠条形图不够清晰
- 让多模态 LLM 审查图像并提出改进建议，可以生成更好的条形图

实践经验：可以用不同的 LLM 做初始生成和反思；用推理模型做反思通常效果更好；可以通过修改初始生成提示或反思提示来优化结果。

---

### 视频 4: Evaluating the impact of reflection
**时长**: ~8 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/vtzr25/evaluating-the-impact-of-reflection
**视频 ID**: 10079021

### 内容总结

评估反射工作流的方法：
- **客观评估**：收集一组问题和标准答案，测量无反射和有反射的正确率（如 SQL 查询生成：无反射 87%，有反射 95%）
- **主观评估**：用 LLM 作为 judge 评估图像质量，但比比较两个图像，用 rubric 对单个图像评分更可靠（如 5 个二元标准：是否有清晰标题、是否有轴标签、图表类型是否合适等）

使用二进制标准比 1-5 评分量表更一致。评估后可以不断调整初始生成提示或反思提示来优化性能。

---

### 视频 5: Using external feedback
**时长**: ~5 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/txqmf0/using-external-feedback
**视频 ID**: 10079022

### 内容总结

外部反馈比仅靠 LLM 自身反思要强大得多。外部反馈示例：
- **代码执行**：运行代码看输出或错误信息，反馈给 LLM 改进
- **竞争对手名称检测**：用正则表达式检测输出中是否提到竞争对手名称
- **网络搜索事实核查**：如验证 Taj Mahal 建造时间，获取准确历史信息
- **字数统计工具**：如果输出超过字数限制，将精确字数反馈给 LLM 重新生成

外部反馈提供了新的信息源，让反射过程更有效。工具创建的额外信息可以帮助 LLM 更准确地改进输出。

---

## Module 3: Tool use

### 模块概述

本模块介绍如何让 LLM 使用工具（函数）来扩展其能力。工具使用让 LLM 可以执行网页搜索、数据库查询、代码执行等各种操作，大大增强应用能力。

### 视频 1: What are tools?
**时长**: ~6 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/3s0czq/what-are-tools
**视频 ID**: 10079023

### 内容总结

工具（Tool use）是指让 LLM 决定何时请求调用函数来执行操作、收集信息或完成其他任务。就像人类用工具比空手能做更多事情一样，LLM 有工具访问权限也能做更多事情。工具使用的工作流程：
1. 输入提示
2. LLM 查看可用工具列表，决定是否调用工具
3. 工具执行函数并返回值
4. 值反馈给 LLM
5. LLM 生成最终输出

关键特点：可以让 LLM 决定是否使用工具。例如问"What time is it?"会调用 getCurrentTime，而问咖啡因含量则直接生成答案。工具可以是网页搜索、数据库查询、日历、邮件等。

---

### 视频 2: Creating a tool
**时长**: ~6 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/79cpry/creating-a-tool
**视频 ID**: 10079024

### 内容总结

创建工具的过程：实现一个函数，然后告诉 LLM 该工具可用。较旧的方式是用 all-caps FUNCTION 和函数名来指示要调用哪个函数，然后用代码搜索这个格式、执行函数、结果反馈给 LLM。现代 LLM 已经训练原生使用工具，不需要这种笨拙的语法。例如，使用 AI Suite 库可以自动将函数签名和文档字符串转换为 LLM 能理解的 JSON schema。工具创建后，LLM 可以根据用户问题决定是否调用、调用哪些工具、传递什么参数。

---

### 视频 3: Tool syntax
**时长**: ~6 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/154qpw/tool-syntax
**视频 ID**: 10079025

### 内容总结

使用 AI Suite 库的代码执行工具语法示例。AI Suite 是开源库，可以方便地调用多个 LLM 提供商。语法类似 OpenAI 的聊天补全 API，但通过 tools 参数提供工具列表给 LLM。使用 AISuite 时，函数会自动带有 docstring 描述工具，使 LLM 知道何时调用。对于复杂函数（如带时区参数的 getCurrentTime），AI Suite 会自动创建更复杂的 JSON schema，包含参数信息。client.chat.completions.create() 会自动处理工具调用循环（max_turns 参数控制最大调用次数）。通过提供工具，LLM 决定调用工具、执行函数、获取结果、反馈给 LLM，最终生成响应。

---

### 视频 4: Code execution
**时长**: ~6 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/a4gs14/code-execution
**视频 ID**: 10079026

### 内容总结

代码执行是一个特殊的强大工具。给 LLM 写代码和执行代码的能力，可以让它完成数学计算等各种任务。用 prompt 让 LLM 在 execute Python 标签中返回代码，然后用正则表达式提取代码并执行。可以使用 Python 的 exec 函数或沙箱环境（如 Docker、E2B）来执行代码。安全考虑：LLM 可能生成删除文件等有害代码，建议在沙箱环境中执行。代码执行如此重要，以至于很多 LLM 提供商都会特别优化这个功能。

---

### 视频 5: MCP
**时长**: ~5 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/x7jowg/mcp
**视频 ID**: 10079027

### 内容总结

MCP（Model Context Protocol）是由 Anthropic 提出但已被许多公司采用的标准，用于给 LLM 提供更多上下文和工具。解决的核心问题：如果 M 个应用要各自集成 N 个工具（如 Slack、Google Drive、GitHub、Postgres），传统方式需要 M×N 的工作量；MCP 将其减少到 M+N。MCP 提供两种资源：data（资源）和 functions（函数）。MCP 生态系统包括 MCP clients（消费工具的应用）和 MCP services（提供工具的服务，如 Slack、GitHub、Google Drive）。快速发展的 MCP 标准让开发者更容易构建强大的 AI 应用。

---

## Module 4: Practical Tips for Building Agentic AI

### 模块概述

本模块是课程最重要的部分之一，讲解如何通过评估和错误分析来驱动开发过程，找到最值得改进的方向，提高开发效率。

### 视频 1: Evaluations (evals)
**时长**: ~15 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/pu5xbl/evaluations-evals
**视频 ID**: 10079028

### 内容总结

构建 agentic 工作流的建议：先专注于获得高质量输出，之后再优化成本和延迟。评估方法：
- **2x2 评估框架**：客观代码评估 vs LLM-as-judge，以及是否有每条目的标准答案
- **快速粗糙评估**：从 10-20 个例子开始，然后迭代改进
- **关注性能低于专家水平的领域**

评估让开发过程系统化，帮助选择不同提示版本、组件配置等。

---

### 视频 2: Error analysis and prioritizing next steps
**时长**: ~9 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/2ftglp/error-analysis-and-prioritizing-next-steps
**视频 ID**: 10079029

### 内容总结

构建快速粗糙系统后，通过查看 traces（中间输出）来发现问题和改进机会。错误分析过程：
1. 找出系统表现不佳的例子（忽略表现好的）
2. 检查每个组件的 traces
3. 统计每个组件导致错误的频率
4. 优先处理错误率高且有改进想法的组件

研究 agent 示例：检查搜索词、搜索结果、最佳来源选择等各步骤的输出质量。如果搜索结果错误率高（45% 不满意），而搜索词本身没问题（5% 不满意），则应专注于改进搜索工具或参数，而非其他组件。

---

### 视频 3: More error analysis examples
**时长**: ~5 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/0kbds1/more-error-analysis-examples
**视频 ID**: 10079030

### 内容总结

更多错误分析示例：
- **发票处理**：分析 PDF 转文本或 LLM 提取日期的错误，找到主要问题来源是 LLM 数据提取而非 PDF 转文本
- **客户邮件回复**：分析数据库查询错误、数据库数据错误、邮件生成错误的发生频率，确定最需要改进的方向

错误分析帮助避免浪费数周或数月时间在不是主要问题源的组件上。

---

### 视频 4: Component-level evaluations
**时长**: ~3 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/fwxyds/component-level-evaluations
**视频 ID**: 10079031

### 内容总结

组件级评估补充端到端评估。对于单个组件（如 web search），创建 gold standard 资源列表，计算信息检索指标（如 F1 score）来衡量组件质量。好处：
- 更清晰的信号来评估特定组件改进
- 避免端到端评估中的噪声
- 不同团队可以专注于各自组件的优化
- 比每次改变参数都运行完整端到端更高效

---

### 视频 5: How to address problems you identify
**时长**: ~10 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/ldf4ci/how-to-address-problems-you-identify
**视频 ID**: 10079032

### 内容总结

改进不同组件的方法：
- **非 LLM 组件**（web search、RAG、代码执行等）：调整超参数（结果数量、日期范围、相似度阈值、chunk 大小等）或替换组件
- **LLM 组件**：改进提示、添加 few-shot 示例、尝试不同 LLM、分解复杂任务为更小步骤、考虑微调（最后手段）

选择 LLM 时，较大的前沿模型通常更擅长遵循指令，而较小的模型在简单问答上表现不错但指令遵循较差。通过尝试不同模型、阅读他人提示、构建个人评估集来培养直觉。

---

### 视频 6: Latency, cost optimization
**时长**: ~4 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/154qpa/latency-cost-optimization
**视频 ID**: 10079033

### 内容总结

优化延迟和成本的方法：
- **延迟优化**：计时每个步骤（如 research agent 中 LLM 生成搜索词 7 秒、网页搜索 5 秒等），找出最大瓶颈，考虑并行化操作或尝试更快的 LLM 提供商
- **成本优化**：计算每个步骤的 token 成本和 API 调用成本，识别最大的成本来源，考虑使用更便宜的组件或 LLM

基准测试帮助识别哪些组件最值得优化，避免在不重要的地方浪费时间。

---

### 视频 7: Development process summary
**时长**: ~4 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/hl2aj7/development-process-summary
**视频 ID**: 10079034

### 内容总结

开发 agentic 系统的过程是迭代的来回过程：
1. 快速构建初始端到端系统
2. 手动检查输出和 traces，初步了解组件性能
3. 收集更多例子构建评估集，计算端到端指标
4. 进行更严格的错误分析，统计各组件错误频率
5. 组件成熟后建立组件级评估
6. 在端到端系统和组件级评估之间来回迭代

新手团队常花大量时间构建而很少分析。分析和评估帮助真正聚焦构建工作。现有工具（监控、trace logging、成本计算等）可以帮助，但大多数工作流最终需要自定义评估来捕获特定问题。

---

## Module 5: Patterns for Highly Autonomous Agents

### 模块概述

本模块介绍构建高度自主 agent 的高级设计模式，包括规划（planning）和多智能体协作（multi-agent systems）。

### 视频 1: Planning workflows
**时长**: ~7 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/jcl177/planning-workflows
**视频 ID**: 10079035

### 内容总结

规划设计模式让 agent 可以自己决定完成任务的步骤序列，无需开发者预先硬编码。示例：太阳镜零售商的客服 agent 可以回答"你们有 100 美元以下的圆形太阳镜吗？"这类复杂问题。LLM 被提供一套工具（获取商品描述、检查库存、获取价格等），然后被要求返回分步骤计划执行用户请求。工作流：LLM 写出计划（如步骤1：获取圆形太阳镜描述，步骤2：检查哪些有库存，步骤3：检查价格是否低于 100），然后逐步执行每个步骤，每次都带着相关上下文调用 LLM。规划已在高度自主的代码生成系统中成功使用，但在其他应用中仍处于实验阶段。

---

### 视频 2: Creating and executing LLM plans
**时长**: ~3 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/wr78er/creating-and-executing-llm-plans
**视频 ID**: 10079036

### 内容总结

LLM 生成计划的格式：通常用 JSON 或 XML，让下游代码能清晰解析步骤。示例 JSON 格式包含每个步骤的描述、使用的工具和参数。也可以用 XML 或 Markdown，但 JSON 和 XML 最清晰。规划使得系统能处理更广泛的任务，因为不需要预先指定确切的工具调用顺序。

---

### 视频 3: Planning with code execution
**时长**: ~7 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/egr0a8/planning-with-code-execution
**视频 ID**: 10079037

### 内容总结

规划与代码执行结合：不让 LLM 输出 JSON 格式的计划，而是让它直接编写代码来表达计划，代码可以表达多个步骤（如调用这个函数，然后调用那个函数）。示例：处理咖啡机销售数据的查询问题，LLM 可以编写 Python 代码（使用 pandas 库）来加载数据、解析日期、筛选行、计算统计量。Python 有数百个内置函数，LLM 训练时见过大量如何调用这些函数的数据，因此可以组合出复杂计划来回答各种查询。研究表明，代码作为动作（code as action）优于 JSON 计划优于纯文本计划。规划在高度自主的代码生成系统中效果很好，但在其他应用中仍在发展。

---

### 视频 4: Multi-agentic workflows
**时长**: ~9 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/608l3n/multi-agentic-workflows
**视频 ID**: 10079038

### 内容总结

多智能体系统：多个 agent 具有不同角色协作完成复杂任务。示例：营销团队中 researcher、graphic designer、writer 线性协作。通信模式：
- **线性通信**：researcher → graphic designer → writer
- **层级通信**：manager 与多个 team member 协调工作
- **深层层级**：manager 下有多个 agent，其中某些 agent 又有自己的 sub-agent
- **全对全通信**：任何 agent 可以随时与任何其他 agent 通信（最难预测和控制的模式）

多智能体系统可以产生更好的结果，但也更难控制。

---

### 视频 5: Communication patterns for multi-agent systems
**时长**: ~4 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/gymk4l/communication-patterns-for-multi-agent-systems
**视频 ID**: 10079039

### 内容总结

多智能体系统中的通信模式设计：
- **线性通信**：适合简单工作流，输出依次传递
- **层级通信**：一个 manager agent 协调多个 worker agents，更常见和推荐
- **深层层级**：某些 agent 可以调用 sub-agents，更复杂但有时用于高级应用
- **全对全通信**：任何 agent 可以与任何其他 agent 通信，结果难以预测，适用于可以容忍一定混乱的应用

各种软件框架支持构建多智能体系统，使实现这些通信模式相对容易。

---

### 视频 6: Conclusion
**时长**: ~2 min
**链接**: https://learn.deeplearning.ai/courses/agentic-ai/lesson/qjhixk/conclusion
**视频 ID**: 10079040

### 内容总结

课程总结：学习了构建 Agentic AI 应用的核心技能：
- 反射设计模式：简单有效的性能提升方法
- 工具使用/函数调用：扩展 LLM 应用能力
- 代码执行：强大的工具
- 评估与错误分析：驱动高效开发过程的关键技能
- 规划与多智能体系统：构建更强大但更难控制的应用

这些技能让你能够构建各种令人兴奋的 Agentic AI 应用。掌握这些技能不仅有助于构建更好的应用，也能开启新的职业机会。

---

## 完整视频列表

| 序号 | 模块 | 视频标题 | 时长 | 链接 | 视频 ID |
|------|------|---------|------|------|---------|
| 1 | M1 | Welcome! | ~2 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/pu5xbv/welcome | 10079010 |
| 2 | M1 | What is agentic AI? | ~5 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/nae3i1/what-is-agentic-ai | 10079011 |
| 3 | M1 | Degrees of autonomy | ~5 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/zqs9ty/degrees-of-autonomy | 10079052 |
| 4 | M1 | Benefits of agentic AI | ~4 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/k2vehc/benefits-of-agentic-ai | 10079013 |
| 5 | M1 | Agentic AI applications | ~7 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/bvuwkr/agentic-ai-applications | 10079014 |
| 6 | M1 | Task decomposition: Identifying the steps in a workflow | ~8 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/moivygo8/task-decomposition-identifying-the-steps-in-a-workflow | 10079015 |
| 7 | M1 | Evaluating agentic AI (evals) | ~5 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/46yh5j/evaluating-agentic-ai-evals | 10079016 |
| 8 | M1 | Agentic design patterns | ~7 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/rm9bg7/agentic-design-patterns | 10079017 |
| 9 | M2 | Reflection to improve outputs of a task | ~4 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/shknq1/reflection-to-improve-outputs-of-a-task | 10079018 |
| 10 | M2 | Why not just direct generation? | ~5 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/uz37v2/why-not-just-direct-generation | 10079019 |
| 11 | M2 | Chart generation workflow | ~4 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/moivym/chart-generation-workflow | 10079020 |
| 12 | M2 | Evaluating the impact of reflection | ~8 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/vtzr25/evaluating-the-impact-of-reflection | 10079021 |
| 13 | M2 | Using external feedback | ~5 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/txqmf0/using-external-feedback | 10079022 |
| 14 | M3 | What are tools? | ~6 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/3s0czq/what-are-tools | 10079023 |
| 15 | M3 | Creating a tool | ~6 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/79cpry/creating-a-tool | 10079024 |
| 16 | M3 | Tool syntax | ~6 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/154qpw/tool-syntax | 10079025 |
| 17 | M3 | Code execution | ~6 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/a4gs14/code-execution | 10079026 |
| 18 | M3 | MCP | ~5 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/x7jowg/mcp | 10079027 |
| 19 | M4 | Evaluations (evals) | ~15 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/pu5xbl/evaluations-evals | 10079028 |
| 20 | M4 | Error analysis and prioritizing next steps | ~9 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/2ftglp/error-analysis-and-prioritizing-next-steps | 10079029 |
| 21 | M4 | More error analysis examples | ~5 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/0kbds1/more-error-analysis-examples | 10079030 |
| 22 | M4 | Component-level evaluations | ~3 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/fwxyds/component-level-evaluations | 10079031 |
| 23 | M4 | How to address problems you identify | ~10 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/ldf4ci/how-to-address-problems-you-identify | 10079032 |
| 24 | M4 | Latency, cost optimization | ~4 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/154qpa/latency-cost-optimization | 10079033 |
| 25 | M4 | Development process summary | ~4 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/hl2aj7/development-process-summary | 10079034 |
| 26 | M5 | Planning workflows | ~7 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/jcl177/planning-workflows | 10079035 |
| 27 | M5 | Creating and executing LLM plans | ~3 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/wr78er/creating-and-executing-llm-plans | 10079036 |
| 28 | M5 | Planning with code execution | ~7 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/egr0a8/planning-with-code-execution | 10079037 |
| 29 | M5 | Multi-agentic workflows | ~9 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/608l3n/multi-agentic-workflows | 10079038 |
| 30 | M5 | Communication patterns for multi-agent systems | ~4 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/gymk4l/communication-patterns-for-multi-agent-systems | 10079039 |
| 31 | M5 | Conclusion | ~2 min | https://learn.deeplearning.ai/courses/agentic-ai/lesson/qjhixk/conclusion | 10079040 |

---

## 关键概念总结

### 核心设计模式
1. **Reflection（反射）**：让 LLM 审查并改进自己的输出，外部反馈可增强效果
2. **Tool use（工具使用）**：给 LLM 提供函数调用能力，扩展其操作范围
3. **Planning（规划）**：LLM 自动决定完成任务的步骤序列
4. **Multi-agent（多智能体）**：多个 agent 协作完成复杂任务

### 关键技能
- **任务分解**：将复杂任务拆分为可执行的离散步骤
- **评估驱动开发**：通过 evals 和 error analysis 聚焦改进方向
- **组件级评估**：隔离测试单个组件以获得更清晰的改进信号

### MCP (Model Context Protocol)
- Anthropic 提出的标准，已被广泛采用
- 大幅减少 M×N 的集成工作量为 M+N
- 连接各种数据源和工具的生态系统

### 评估类型
- **端到端评估**：测量整个系统性能
- **组件级评估**：测量单个步骤的性能
- **客观评估**：可编程检查的指标
- **主观评估**：需要 LLM-as-judge 或人工判断

---

*此总结由 AI 自动生成，仅供学习参考使用*