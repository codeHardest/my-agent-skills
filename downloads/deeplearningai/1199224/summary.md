# 视频摘要：Agentic RAG

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/aam1f5/agentic-rag
- **时长**: 375秒 (约6分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:18:47

## 原始元数据
- (无额外元数据)

## 输出文件
- video.mp4 - 原始视频文件
- audio.mp3 - 音频文件
- subtitle.vtt - 带时间戳的字幕文件
- subtitle_ai-zh.json - 原始AI字幕JSON
- transcript.txt - 纯文本转录
- summary.md - 本摘要文件

## 内容概述
本视频介绍了如何通过引入Agentic工作流来提升RAG（检索增强生成）系统的性能。视频详细解释了Agentic RAG的核心概念，包括使用多个LLM分别负责不同步骤的设计模式，并展示了顺序、条件、迭代和并行四种常见的工作流模式。此外，视频还强调了构建Agentic系统时需要转变的思维方式——将LLM视为模块化组件而非独立解决方案。

## 核心要点
1. **Agentic工作流定义**：在RAG系统中使用多个LLM，每个LLM负责整体过程中的单一步骤，从而实现任务分解和专业化。
2. **两种主要变化**：一是将任务视为一系列步骤和决策，每个步骤由不同的LLM调用完成；二是为LLM提供更广泛的工具访问能力，如代码解释器、网页浏览器或向量数据库。
3. **路由器LLM（Router LLM）**：专门调优的小型LLM，负责判断用户提示是否需要调用向量数据库，仅输出"是"或"否"。
4. **评估器LLM（Evaluator LLM）**：判断检索到的文档是否足够回答问题，可根据需要请求额外的检索。
5. **Agentic系统设计思维**：将设计视为绘制流程图，每个LLM仍然只是接受文本输入并生成文本输出。
6. **模型选择灵活性**：不同步骤可以使用不同规模和专长的模型，轻量级模型用于简单任务，大型模型用于复杂任务。
6. **顺序工作流（Sequential Workflow）**：将输出线性地通过一系列LLM，每个LLM专注于单一步骤并专业化。
7. **条件工作流（Conditional Workflow）**：使用LLM决定提示应遵循多条路径中的哪一条。
8. **迭代工作流（Iterative Workflow）**：类似条件工作流，但将提示路由到系统中较早的位置，形成循环。
9. **并行工作流（Parallel Workflow）**：编排LLM将提示分解为多个独立任务分配给不同LLM，合成器LLM重新组合工作结果。
10. **工具和平台支持**：有多种工具、库和平台可帮助构建和管理Agentic系统。
11. **思维方式转变**：LLM从独立解决方案转变为工作流中可组合的模块化组件。
12. **小型模型的可行性**：由于能力与工作流部分高度匹配，使用小型模型或专注于少数任务的模型变得可行。

## 详细内容（保留所有原始信息）

### 一、Agentic RAG的核心概念

随着RAG系统日趋成熟，引入Agentic工作流是提升其性能的一种强大方式。Agentic工作流意味着在整个RAG系统中使用多个LLM，每个LLM负责整体过程中的单一步骤。这一理念读者此前已有所了解——LLM被用于执行查询扩展、提示重写或引用生成等任务。可以构建的复合系统种类繁多，接下来将深入探讨如何以Agentic方式构建RAG系统来进一步提升其质量。

### 二、传统LLM使用与Agentic系统的区别

通常使用语言模型的方式是向其输入提示，然后它输出响应——简单直接。在Agentic系统中，对这一模式有两项主要变革：

**第一项变革**：任务现在被视为一系列步骤和决策，每个步骤都可以通过调用不同的LLM来完成。

**第二项变革**：LLM被赋予访问更广泛工具的能力，如代码解释器、网页浏览器，或者在RAG场景下的信息参考向量数据库。

### 三、示例Agentic RAG工作流

以下是一种可能的Agentic RAG工作流：

1. **用户提交提示**：用户向系统提交一个提示。

2. **路由器LLM处理**：提示首先由一个小型路由器LLM处理。该LLM的工作是判断提示是否实际上需要调用向量数据库。它经过专门调优，只能输出"是"（表示提示需要从数据库检索）或"否"（表示提示无需检索即可回答）。

3. **条件路由**：
   - 如果路由器LLM输出"否"，提示直接发送给单独的LLM生成响应。
   - 如果路由器LLM输出"是"，则将提示发送到向量数据库进行检索。

4. **评估器LLM判断**：如果执行了检索步骤，则使用单独的评估器LLM判断检索到的文档是否足够回答问题。

5. **迭代检索**：根据评估器LLM的判断，可能从向量数据库请求额外的检索。

6. **生成增强提示**：一旦检索到足够的信息，就构建一个增强提示并交给LLM生成响应。

7. **引用生成**：此时，最终LLM遍历响应并添加引用。

### 四、Agentic系统的关键设计原则

这个示例Agentic RAG系统突出了对任何Agentic系统都适用的几个关键点：

**第一点**：可以将设计Agentic系统本质上视为绘制流程图。流程图中的每个LLM仍然只是接受文本输入并生成文本输出，但系统的设置使得每个LLM在提示穿越RAG系统的过程中完成一项任务。

**第二点**：不需要在工作流的每个步骤使用相同的LLM。该Agentic系统中的路由器LLM和评估器LLM可以是轻量级模型，运行速度快且成本低，因为它们的任务单一且相对简单。然后可以使用更大的模型来生成草稿响应，选择专门从事引用生成的模型来完成该步骤。

### 五、四种常见Agentic工作流模式

在为RAG应用程序添加Agentic工作流时，需要考虑以下几种常见模式：

#### 1. 顺序工作流（Sequential Workflow）

顺序工作流只是以线性方式将输出通过一系列LLM移动。这意味着发送给系统的每个提示都可能经过基于LLM的查询解析器、查询重写器和引用生成器作为生成过程的一部分。每个LLM只专注于整体过程中的一个步骤，因此可以在该步骤上专业化。

#### 2. 条件工作流（Conditional Workflow）

条件工作流使用LLM来决定提示应遵循多条路径中的哪一条。前面看到的路由器LLM就是实现此工作流的例子，用于决定是否需要检索来回答提示。也可以使用路由器来确定应该使用多个具有不同优势和专长的LLM中的哪一个来生成响应。

#### 3. 迭代工作流（Iterative Workflow）

迭代工作流类似于条件工作流，但它将提示路由到系统中较早的位置，形成循环。例如，如果RAG系统被设计用于生成与现有代码库集成的代码，系统可能需要多次尝试才能写出可工作的代码。评估器LLM可用于评估每个草稿（可能借助代码解释器的帮助），并提供反馈直到认为解决方案合适。

#### 4. 并行工作流（Parallel Workflow）

并行工作流中，一个编排语言模型将提示分解为多个独立任务，并将每个任务分配给单独的LLM。在另一端，一个合成器语言模型重新组合它们的工作。如果应用程序需要比较两篇研究论文的关键洞察，可能需要两个不同的LLM分别总结和评估每篇论文，然后让编排器结合它们的发现。

### 六、工具和实现方式

对于简单的Agentic系统，可以自己实现所需工作流的逻辑。然而，随着事情变得更加复杂，有各种各样的工具、库和平台旨在帮助构建和管理Agentic系统。构建Agentic系统时的创意可能性确实是无穷无尽的。

### 七、思维方式的重要转变

这里还涉及到一种重要的思维方式转变。LLM开始看起来不那么像独立解决方案，而更像是融入更大工作流的模块化组件。突然之间，使用小型模型或只在少数任务上表现出色的模型变得更加令人愉悦，因为它们的能力与它们负责的工作流部分高度匹配。添加Agentic组件可以提供灵活性来构建更加高效的RAG系统。

## 完整字幕原文
```
As your RAG system matures, a powerful way to improve its performance is to start introducing agentic workflows. An agentic workflow means using several LLMs throughout your RAG system, each one responsible for a single step in the overall process. You've already seen this idea, with LLMs used to perform tasks like query expansion, prompt rewriting, or citation generation. There's a huge array of compound systems like this you could build. So let's look into how you can further improve the quality of your RAG system by building it in an agentic way. Typically, the way you use a language model is to feed it a prompt, and it spits out a response. Simple. In an agentic system, there's two main changes to this model. First, tasks are now treated as a series of steps and decisions, each of which can be completed by a call to a different LLM. Second, LLMs are given access to a wider array of tools like a code interpreter, web browser, or in the case of RAG, a vector database of information to reference. Here's one possible agentic workflow for a RAG system. A user submits a prompt to the system, and it is first processed by a small router LLM. This LLM's job is to determine if the prompt actually requires a call to the vector database. It's been specially tuned for this task, and will only output either yes, meaning the prompt does justify retrieval from the database, or no, meaning the prompt can be answered without retrieval. Based on the router LLM's decision, the prompt is either sent to the vector database for retrieval, or skips that step. If no retrieval is completed, the prompt is sent directly to a separate LLM to generate a response. If a retrieval step was requested, a separate evaluator LLM is used to determine if the retrieved documents are sufficient to answer the question. Based on this evaluator LLM's decision, additional retrievals from the vector database may be requested. Once sufficient information has been retrieved, an augmented prompt is constructed and given to the LLM to generate a response. At this point, a final LLM goes through this response and adds citations. This is just one possible agentic RAG system, but it highlights a few key points that are true for any agentic system. First, you can think of designing an agentic system essentially as drawing a flowchart. Each LLM in the diagram is still just taking text input and generating text output, but the system is set up so that each LLM is completing one task on the prompt's journey through the RAG system. Second, you don't need to use the same LLM for each step in the workflow. The router and evaluator LLM in this agentic system could be lightweight models that are fast and cheap to run since they have a single and relatively simple task. You could then use a larger model to generate the draft response and pick a model that specializes in citation generation for that step. As you think about adding agentic workflows to your RAG application, here's a few common patterns to consider. A sequential workflow just moves output in a linear fashion through a series of LLMs. This might mean that every prompt sent to your system moves through an LLM-based query parser, query rewriter, and citation generator as part of the generation process. Each LLM just focuses on one step of the overall process and can therefore specialize at that step. A conditional workflow uses an LLM to decide which of many paths a prompt should follow. You just saw a router LLM implement this workflow to decide if a retrieval is necessary to respond to a prompt. You could also use a router to determine which of several LLMs with different strengths and specializations should be used to generate a response. An iterative workflow works similarly to a conditional workflow, but it routes the prompt to an earlier point in the overall system, forming a loop. For example, if your RAG system is designed to generate code that integrates with an existing code base, it's possible the system would need multiple attempts to write working code. An evaluator LLM could be used to assess each draft, perhaps with the assistance of a code interpreter, and provide feedback until it deems the solution suitable. Finally, you can create parallel workflows in which an orchestrator language model breaks a prompt into multiple distinct tasks and assigns each task to separate LLMs. On the other end, a synthesizer language model recombines their work. If your application is, say, comparing the key insights from two research papers, you might want two different LLMs to summarize and evaluate each one and then have the orchestrator combine their findings. For simple agentic systems, you can just implement the logic of your desired workflow yourself. As things get more complicated, however, there's a wide variety of tools, libraries, and platforms designed to help you build and manage an agentic system. The creative possibilities when building agentic systems are truly endless. There's also an important mindset shift at play here. LLMs start to look a little less like standalone solutions and more like modular pieces that fit inside a larger workflow. Suddenly, you're more than happy to use smaller models or models that only excel at a few tasks because their capabilities are well aligned with the portions of the workflow they're responsible for. Adding agentic components can give you the flexibility to build even more capable rack systems.
```

## 关键引述/重要观点

> "An agentic workflow means using several LLMs throughout your RAG system, each one responsible for a single step in the overall process."

> "In an agentic system, there's two main changes to this model. First, tasks are now treated as a series of steps and decisions, each of which can be completed by a call to a different LLM. Second, LLMs are given access to a wider array of tools like a code interpreter, web browser, or in the case of RAG, a vector database of information to reference."

> "You can think of designing an agentic system essentially as drawing a flowchart."

> "You don't need to use the same LLM for each step in the workflow."

> "LLMs start to look a little less like standalone solutions and more like modular pieces that fit inside a larger workflow."

> "Adding agentic components can give you the flexibility to build even more capable RAG systems."

## 相关话题/关键词
- Agentic RAG（代理式RAG）
- Agentic Workflow（代理式工作流）
- Large Language Model (LLM)（大型语言模型）
- Router LLM（路由器LLM）
- Evaluator LLM（评估器LLM）
- Vector Database（向量数据库）
- Retrieval-Augmented Generation (RAG)（检索增强生成）
- Sequential Workflow（顺序工作流）
- Conditional Workflow（条件工作流）
- Iterative Workflow（迭代工作流）
- Parallel Workflow（并行工作流）
- Orchestrator（编排器）
- Synthesizer（合成器）
- Query Expansion（查询扩展）
- Prompt Rewriting（提示重写）
- Citation Generation（引用生成）
- Code Interpreter（代码解释器）
- Web Browser（网页浏览器）
- Query Parser（查询解析器）
- Flowchart（流程图）
- Modular Components（模块化组件）

## 技术信息
- 字幕字数: 5450
- 字幕字符数: 5450
- 时间戳条目数: 0
- 处理时间: 2026-05-28 14:18:47