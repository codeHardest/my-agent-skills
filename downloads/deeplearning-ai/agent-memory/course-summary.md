# Agent Memory: Building Memory-Aware Agents
## 课程总结 | Course Summary

**课程来源**: DeepLearning.AI
**合作方**: Oracle
**讲师**: Richmond Alake & Nacho Martínez
**课程链接**: https://learn.deeplearning.ai/courses/agent-memory-building-memory-aware-agents

---

## 课程概述

本课程教授如何构建记忆系统，使无状态的 LLM 智能体转变为具有持久性、连续性和自主学习能力的 Memory-Aware Agents。课程采用 Oracle AI 数据库作为记忆存储的基础设施层，结合 LangChain 和 LLM 驱动的管道实现记忆增强、记忆提取和工具检索。

---

## 第一章：Introduction（课程介绍）

**时长**: 约 2 分钟

### 内容要点：
- 课程由 DeepLearning.AI 与 Oracle 联合开发
- **核心问题**: 基于 LLM 的智能体在单次会话中表现良好，但会话结束后会丢失所有学到的内容
- **Memory（记忆）** 能将无状态智能体转变为能克服这一挑战的智能体
- 课程涵盖使用 Oracle AI 数据库作为基础设施层进行记忆存储和检索
- **范式转变**: 从"提示工程"和"上下文工程"转向"记忆工程"——将长期记忆作为第一性基础设施，独立于模型之外，持久化且结构化
- 课程提供真实可工作的代码，可适配到生产级智能体

---

## 第二章：Why AI Agents Need Memory（为什么 AI 智能体需要记忆）

**时长**: 约 18 分钟

### 内容要点：

#### 1. AI 智能体的定义
AI 智能体是一个计算实体，具有以下特征：
- **Perception（感知）**: 通过输入感知环境
- **Action（行动）**: 通过工具执行操作
- **Reasoning（推理）**: 由 LLM 驱动的推理能力
- **Memory（记忆）**: 能够跨会话存储、检索和应用知识

#### 2. 无状态智能体（Stateless Agent）的问题
- **无法完成长期任务（Long-horizon Tasks）**: 需要运行数分钟到数天的任务
- **无跨会话上下文感知**: 用户离开后重新回来，信息丢失
- **缺乏适应能力**: 新信息无法更新到后续交互中
- **高运营成本**: 每次轮次都需要将大量信息塞入上下文窗口

#### 3. 记忆增强型智能体（Memory-Augmented Agent）
- 与无状态智能体相同的感知、推理和行动能力
- 额外增加外部数据库存储和检索信息
- 能够在多轮交互中保持连续性

#### 4. 对话历史（Conversational Memory）的局限性
- **上下文窗口是有限的，但用户关系不是**
- 对话历史只是交互记录，不包含实体信息（如人名、地点、组织关系）
- 需要结构化的、可查询的知识，而非仅仅聊天记录
- 需要超越对话记忆，提取跨会话的有用信息

#### 5. 智能体记忆的类型

**短期记忆（Short-term Memory）**:
- **Semantic Cache（语义缓存）**: 利用向量搜索和之前的响应来回答相似查询
- **Working Memory（工作记忆）**: LLM 的上下文窗口和基于会话的记忆，相当于"草稿板"

**长期记忆（Long-term Memory）**:
- **Procedural Memory → Workflow Memory（工作流记忆）**: 记录智能体完成任务所采取的步骤和工具调用
- **Semantic Memory → Knowledge Base（知识库）**: 智能体需要知道的外部领域知识
- **Episodic Memory → Conversational Memory（情景记忆）**: 带时间戳的对话历史

#### 6. Agent Memory Core（智能体记忆核心）
智能体系统中有三个主要的记忆所在：
- **LLM**: 包含参数记忆（训练数据）
- **Embedding Model**: 生成嵌入时提取语义和上下文信息
- **Database（数据库）**: 数据流量最大，是真正的 Agent Memory Core

Agent Memory Core 定义：系统中数据流量最大的主要基础设施，能够处理信息的存储、检索和优化。

---

## 第三章：Constructing The Memory Manager（构建记忆管理器）

**时长**: 约 22 分钟

### 内容要点：

#### 1. Memory Manager 概述
Memory Manager 是软件工具（harness），它：
- 抽象了访问记忆的复杂性
- 提供统一的接口来读写不同类型的记忆存储
- 将记忆存储实现为 Oracle 数据库中的表

#### 2. 核心组件

**Memory Store（记忆存储）**:
- 每种记忆类型的计算表示
- 例如：Conversational Memory Store、Entity Memory Store、Workflow Memory Store、Knowledge Base Memory Store、Summary Memory Store

**Store Manager（存储管理器）**:
- 记忆存储的高级编排器
- 负责创建、更新、删除和读取不同的记忆存储

#### 3. 数据库表的设计

**Conversational Memory Store（SQL 表）**:
- 存储对话历史，保持对话序列和时间顺序检索
- 字段：message_id（主键）、thread_id（会话ID）、role（user/assistant）、message_content、timestamp、metadata（标记消息是否已摘要等）

**Vector-based Memory Stores（向量存储）**:
- Knowledge Base、Entity、Workflow、Summary 使用 Oracle AI Vector Search
- 需要指定向量维度（使用 paraphrase-mpnet-base-v2 模型，768 维）
- 字段：ID、content、embedding、metadata

**Tool Log Store（工具日志）**:
- 存储工具执行日志，用于追踪智能体在工作流中采取的步骤

#### 4. MemoryManager 类
主要接口，包含各种记忆类型的读写方法：
- `write_conversational_memory` / `read_conversational_memory`
- `write_entity_memory` / `read_entity_memory`
- `write_knowledge_base` / `read_knowledge_base`
- `write_workflow_memory` / `read_workflow_memory`
- `write_summary_memory` / `read_summary_memory`

---

## 第四章：Scaling Agent Tool Use with Semantic Tool Memory（使用语义工具记忆扩展智能体工具使用）

**时长**: 约 17 分钟

### 内容要点：

#### 1. 工具调用（Tool Calling）概述
- LLM 不直接执行代码，而是输出结构化请求
- 环境执行代码并返回结果给 LLM

#### 2. 工具过多时的问题
当智能体能访问大量工具时：
- **Context Confusion & Context Bloat**: 上下文被工具信息淹没
- **Tool Selection Degradation**: 模型选择工具的能力下降
- **延迟和 Token 成本增加**: 处理所有工具定义需要更长时间

#### 3. Toolbox Pattern（工具箱模式）
**核心思想**: 将工具视为可检索的来源，而非全部塞入上下文
- 将所有工具的名称、描述、参数编码为向量
- 存入向量数据库
- 用户查询时，通过语义搜索（similarity search）只检索最相关的工具

#### 4. Memory Unit Augmentation（记忆单元增强）
- 将工具定义通过 LLM 增强描述
- 用增强后的描述创建嵌入
- **优势**: 在嵌入空间中工具之间有更高的分离度、更高的召回率和更高信号的嵌入文本

#### 5. 实践代码
- **Tavily 工具**: 网络搜索服务，将结果存入知识库
- **本地工具**: 使用 datetime 库等本地 Python 代码
- **ArXiv 工具**: 使用 langchain_community 的 ArxivRetriever 检索学术论文
- **Deep Ingestion**: 使用 RecursiveCharacterTextSplitter 进行文档分块，然后存入向量存储

---

## 第五章：Memory Operations: Extraction, Consolidation, and Self-Updating Memory（记忆操作：提取、整合和自我更新）

**时长**: 约 23 分钟

### 内容要点：

#### 1. 上下文工程（Context Engineering）
定义：一种优化选择进入 LLM 上下文窗口的信息量的技术，通过塑造放入其中的信息量来使 LLM 响应更高效。

#### 2. 上下文窗口缩减技术（Context Window Reduction）

**Context Summarization（上下文摘要）**:
- 通过 LLM 处理整个上下文
- 保留最高信号信息、保留关键关系、移除冗余部分
- **缺点**: 有损技术，总会丢失一些信息

**Context Compaction（上下文压缩）**:
- 将信息转移到数据库
- 使用数据库作为 LLM 的外部扩展
- 只在 ID 和描述中存储上下文概要
- LLM 可以通过 ID 检索完整信息
- **优势**: 无信息丢失

#### 3. Workflow Memory（工作流记忆）
- 保存智能体完成任务所采取的步骤序列
- 例如：获取天气需要 → 获取用户位置 → 访问天气 API → 传递经纬度 → 返回天气信息
- **优势**: 一次执行后，后续相同任务可复用步骤，无需每次重新规划

#### 4. 关键实现
- **calculate_context_usage**: 估算上下文使用的 token 数量
- **summarize_conversation**: 摘要对话并标记已摘要的消息
- **expand_summary**: 根据摘要 ID 展开还原原始对话
- **compact_context**: 将上下文压缩存入数据库，保留 ID 和描述
- **monitor_context_window**: 监控上下文利用率（绿色/警告/危急）

---

## 第六章：Memory Aware Agent（记忆感知智能体）

**时长**: 约 20 分钟

### 内容要点：

#### 1. Agent Loop（智能体循环）概述
Agent Loop 是一个循环迭代环境：
1. **组装上下文（Assemble Context）**: 从各种记忆存储中收集信息
2. **调用 LLM（Invoke LLM）**: 将上下文传递给 LLM 进行推理
3. **执行行动（Act）**: LLM 决定响应、调用工具或请求用户输入
4. 重复直到满足停止条件

**停止条件**:
- LLM 给出最终答案（目标完成）
- 错误或超时

#### 2. 智能体循环内外的记忆操作

**循环外的记忆操作**:
- 在进入 Agent Loop 前从记忆读取（构建初始上下文）
- 构建对话记忆、知识库、工作流、实体和摘要记忆
- 检查上下文使用率（超过 80% 时触发摘要）
- 检索与查询相关的工具

**循环内的记忆操作**:
- 智能体可以调用工具（如搜索互联网、扩展摘要、总结对话）
- 程序化执行摘要（当上下文窗口超过 80% 时自动触发）
- 将工具日志写入数据库（上下文卸载）

#### 3. Agent Harness（智能体工具）
- 记忆操作和循环内外操作的组合构成 Agent Harness
- 是使 AI 智能体能够可靠执行的编程脚手架

#### 4. Memory Aware Agent 实现
- **启动时**: 从长期记忆加载先前上下文
- **运行中**: 递归推理循环 + 中间记忆检查点
- **会话间**: 持久化保存

#### 5. 演示案例
1. **第一轮**: 请求获取 MemGPT 论文 → 智能体调用 arXiv 搜索工具 → 返回论文信息
2. **第二轮**: 请求保存论文内容 → 智能体使用 fetch_and_save_paper 工具 → 保存到知识库
3. **第三轮**: 请求提取论文要点 → 智能体从对话记忆中获取上下文 → 生成要点总结
4. **第四轮**: 上下文窗口超过 80% → 自动触发摘要 → 对话记忆被压缩，摘要存入 Summary Memory
5. **第五轮**: 询问第一个问题是什么 → 智能体展开摘要 → 从摘要中恢复信息 → 回答问题

---

## 第七章：Conclusion（课程总结）

**时长**: 约 1 分钟

### 课程回顾与收获：
1. **理解了为什么没有记忆的智能体会失败**
2. **构建了带有持久存储的 Memory Manager**，支持不同记忆类型
3. **使用语义工具记忆扩展了工具使用**
4. **构建了提取和整合管道**，将原始对话转换为持久知识
5. **构建了自我更新智能体循环**，让智能体能够自主完善自身知识
6. **整合为完整的全状态 Memory Aware Agent**

### 核心设计模式：
- **Memory Modeling（记忆建模）**
- **Semantic Retrieval（语义检索）**
- **Extraction（提取）**
- **Consolidation（整合）**
- **Write-back（写回）**

### 核心理念：
> "构建不仅能响应，还能记住、改进、并感知自身记忆能力的智能体"

---

## 文件清单

| 文件名 | 描述 |
|--------|------|
| `01-introduction.json` | 第一课：课程介绍 完整字幕 |
| `02-why-ai-agents-need-memory.json` | 第二课：为什么 AI 智能体需要记忆 完整字幕 |
| `03-constructing-the-memory-manager.json` | 第三课：构建记忆管理器 完整字幕 |
| `04-scaling-agent-tool-use-with-semantic-tool-memory.json` | 第四课：使用语义工具记忆扩展工具使用 完整字幕 |
| `05-memory-operations-extraction-consolidation-self-updating-memory.json` | 第五课：记忆操作 完整字幕 |
| `06-memory-aware-agent.json` | 第六课：记忆感知智能体 完整字幕 |
| `07-conclusion.json` | 第七课：课程总结 完整字幕 |
| `course-summary.md` | 本文件：全课程中文总结 |
