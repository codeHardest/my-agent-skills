# Agentic Knowledge Graph Construction (课程总结)

**课程来源**: DeepLearning.AI
**课程名称**: Agentic Knowledge Graph Construction
**课程链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction
**合作机构**: Neo4j
**课程级别**: Intermediate
**发布于**: 2025-08-27

---

## 课程概述

本课程教授如何构建一个多智能体系统（Multi-Agent System），将结构化和非结构化数据转换为知识图谱。课程使用 Google ADK（Agent Development Kit）和 Neo4j 图数据库，通过多个专业智能体协作完成从用户意图理解到知识图谱构建的完整流程。

**核心技能**:
- 使用 Google ADK 构建智能体
- 知识图谱设计与实现
- Neo4j 图数据库操作
- 多智能体系统架构
- 使用 Cypher 查询语言

**适用场景**:
- 社交网络分析
- 物流优化
- 推荐系统
- 欺诈检测
- 产品数据分析
- 根因分析（Root Cause Analysis）

---

## 视频列表

| 序号 | 视频标题 | 时长 | 链接 | 视频 ID |
|------|---------|------|------|---------|
| 1 | Introduction | ~3 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/hhqjv/introduction | 1215001 |
| 2 | What is a Knowledge Graph? | ~11 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/8860g/what-is-a-knowledge-graph | 1215002 |
| 3 | Architecture of the Multi-Agent System | ~10 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/ddcnq/architecture-of-the-multi-agent-system | 1215003 |
| 4 | Introduction to Google's ADK - Part I | ~22 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/77wrh/introduction-to-google-s-adk-part-i | 1215004 |
| 5 | Introduction to Google's ADK – Part II | ~20 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/jjx7p/introduction-to-google-s-adk-part-ii | 1215005 |
| 6 | Understanding User Intent | ~17 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/vvk22/understanding-user-intent | 1215006 |
| 7 | File Suggestions | ~13 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/55puk/file-suggestions | 1215007 |
| 8 | Schema Proposal for Structured Data | ~29 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/jjx7m/schema-proposal-for-structured-data | 1215008 |
| 9 | Schema Proposal for UnStructured Data | ~16 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/wwdel/schema-proposal-for-unstructured-data | 1215009 |
| 10 | Knowledge Graph Construction - Part I | ~13 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/lljch/knowledge-graph-construction-part-i | 1215010 |
| 11 | Knowledge Graph Construction – Part II | ~33 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/33uzg/knowledge-graph-construction-part-ii | 1215011 |
| 12 | Conclusion | <1 min | https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/cc79j/conclusion | 1215012 |

---

## 视频内容详细总结

---

## 视频 1: Introduction

**时长**: ~3 min (191 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/hhqjv/introduction
**视频 ID**: 1215001

### 内容总结

本课程由 Andrew Ng 与 Neo4j 开发者关系专家 Andreas Kollegger 合作开设。课程目标是构建一个多智能体系统，将结构化和非结构化数据转换为知识图谱。

**知识图谱的核心优势**：
- 类似于 RAG（检索增强生成），知识图谱将文档分块并存储在向量数据库中
- 额外优势：将分块放入图结构中，每个分块链接到从中提取的实体
- 例如，产品评论可包含产品订单、配送问题、产品缺陷等实体
- 通过边（Edge）连接分块和实体，每条边代表一种关系
- 实体与分块一起检索，为 LLM 提供更精确的上下文

**多智能体系统的工作流程**：
1. 首先确定图谱模式（Schema）——定义可提取的实体类型和它们之间的关系
2. 根据模式构建实际图谱并存储到图数据库
3. 使用 Google ADK（Agent Development Kit）设计多智能体系统

**三个主要工作流程**：
1. **Structured Data Agent**（结构化数据智能体）：处理 CSV 文件等结构化数据
2. **Unstructured Data Agent**（非结构化数据智能体）：处理 Markdown 文件等非结构化文本
3. **GraphRAG Agent**：使用构建好的图谱回答用户问题

---

## 视频 2: What is a Knowledge Graph?

**时长**: ~11 min (656 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/8860g/what-is-a-knowledge-graph
**视频 ID**: 1215002

### 内容总结

本课深入解释知识图谱的概念及其与关系数据库的区别。

**关系数据库到知识图谱的转换**：
- 传统关系数据库使用表和连接表（Join Tables）来表示多对多关系
- 通过多个 JOIN 操作（如 Person → Person_Product → Product）回答复杂查询
- 知识图谱将这种多跳查询简化为直接的模式匹配

**图数据库的特点**：
- **节点（Nodes）**：代表事物（人、产品、博客等），具有多个标签
- **关系（Relationships）**：是一等公民，是数据库中的实际数据记录，具有方向和单一类型
- **属性（Properties）**：节点和关系都有键值对属性
- 使用 Cypher 查询语言，支持模式匹配

**Cypher 查询示例**：
```cypher
MATCH (abk:Person {name: 'abk'})-[:PURCHASED]->(abkProducts)
RETURN abkProducts
```

**知识图谱的优势**：
1. 非常适合组合非结构化数据和结构化数据
2. 可以结合向量相似性搜索和模式匹配
3. 自然语言友好，便于与 LLM/GenAI 结合

**典型应用场景：根因分析（Root Cause Analysis）**：
- 家具制造商分析客户投诉
- 问题：哪些产品问题最多？产品哪个部位有问题？
- 是否是设计问题（交给设计团队）或制造问题（可采取纠正措施）

**数据模型的三层图结构**：
1. **Domain Graph（域图）**：来自 CSV 等结构化数据
2. **Lexical Graph（词汇图）**：来自分块的文本和向量嵌入
3. **Subject Graph（主题图）**：从文本中提取的实体，通过 SPO（三元组）连接

---

## 视频 3: Architecture of the Multi-Agent System

**时长**: ~10 min (594 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/ddcnq/architecture-of-the-multi-agent-system
**视频 ID**: 1215003

### 内容总结

本课详细介绍多智能体系统的架构设计。

**智能体的定义**：
- 从工程角度看，智能体是一个新型控制流运算符
- 基本结构：循环中调用 LLM，LLM 决定要执行的操作，然后传递给计算机端执行
- 通过 switch 语句执行潜在操作

**智能体的优势**：
- 强大：LLM 可调用任何代码能做的工具
- 自适应：LLM 被赋予记忆，可从对话或保存的记忆中学习
- 易于上手：使用自然语言描述prompts

**智能体的劣势**：
- 慢：远程 LLM 调用成本高、速度慢
- 非确定性：LLM 本身的特性
- 成本：token 成本随时间累积

**多智能体系统的优势**：
- 改善单智能体的速度和成本问题
- 多个智能体协同工作完成单一目标

**多智能体系统的架构**：
- **层次结构**：顶层智能体管理整体流程，子智能体执行具体任务
- **两种交互方式**：
  1. 智能体之间相互委托（Delegation）
  2. 一个智能体作为工具被另一个智能体调用

**本课程构建的多智能体系统**：

```
Knowledge Graph Agent (顶层协调器)
├── Structured Data Agent（结构化数据工作流）
│   ├── User Intent Agent → 理解用户目标
│   ├── File Suggestion Agent → 推荐相关文件
│   └── Schema Proposal Agent → 提出图谱模式（Critic Pattern）
│
├── Unstructured Data Agent（非结构化数据工作流）
│   ├── User Intent Agent → 理解用户意图
│   ├── File Suggestion Agent → 推荐相关文件
│   └── Entity and Fact Type Proposal Agent → 提取实体和事实类型
│
└── GraphRAG Agent（使用图谱回答问题）
```

**Critic Pattern（批评模式）**：
- Schema Proposal Agent：提出模式建议
- Schema Critic Agent：审查并批评建议
- CheckStatusAndEscalate Agent：决定是否继续循环

---

## 视频 4: Introduction to Google's ADK - Part I

**时长**: ~22 min (1325 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/77wrh/introduction-to-google-s-adk-part-i
**视频 ID**: 1215004

### 内容总结

本课介绍 Google ADK 的基本使用方法。

**ADK 核心组件**：
- `Agent` 类：定义智能体
- `LiteLLM`：与 OpenAI 等 LLM 交互的封装
- `InMemorySessionService`：提供记忆功能
- `Runner`：管理智能体的执行环境

**工具定义**：
```python
def say_hello(person_name: str) -> dict:
    """格式化的欢迎消息"""
    return tool_success(
        message=f"Hello to you, {person_name}",
        db_response=graph_db.query(
            "RETURN 'Hello to you, ' + $person_name AS message",
            {"person_name": person_name}
        )
    )
```

**智能体创建**：
```python
hello_agent = Agent(
    name="hello_agent_v1",
    model=llm,
    description="A friendly chat agent",
    instruction="You are a helpful assistant...",
    tools=[say_hello]
)
```

**智能体运行机制**：
- Runner 管理事件循环
- 通过异步调用执行智能体
- 事件循环处理消息、工具调用、响应

**执行环境设置**：
- `SessionService`：管理会话状态
- `Runner`：协调智能体执行
- `AgentCaller`：便捷的封装类

**Query 参数防注入**：
- 使用 `$variable` 语法传递查询参数
- 避免字符串拼接带来的安全风险

---

## 视频 5: Introduction to Google's ADK – Part II

**时长**: ~20 min (1206 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/jjx7p/introduction-to-google-s-adk-part-ii
**视频 ID**: 1215005

### 内容总结

本课继续讲解 ADK，介绍多智能体系统的构建。

**多智能体系统的构建**：
1. **Sub-Agents（子智能体）**：
   - `greeting_agent`：处理问候
   - `farewell_agent`：处理告别

2. **Root Agent（根智能体/协调器）**：
   - 负责任务分配和协调
   - 根据描述决定何时委托给子智能体

**智能体委托（Agent Delegation）**：
```python
root_agent = Agent(
    name="root_agent_v1",
    model=llm,
    description="Coordinates a team of sub-agents",
    instruction="Your job is to coordinate...",
    sub_agents=[greeting_agent, farewell_agent]
)
```

**委托流程**：
1. 用户发送消息
2. 根智能体分析消息类型
3. 通过 `transfer_to_agent` 将控制权转移给适当的子智能体
4. 子智能体执行任务（可能调用工具）
5. 返回最终响应

**记忆（Memory）和状态管理**：
- 使用 `ToolContext` 访问状态
- 通过 `state` 字典在智能体之间共享信息
- 状态更新会被 ADK 自动追踪和传播

**状态更新示例**：
```python
def say_hello_stateful(person_name: str, tool_context: ToolContext) -> dict:
    tool_context.state["user_name"] = person_name
    # ... 执行逻辑
```

---

## 视频 6: Understanding User Intent

**时长**: ~17 min (1030 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/vvk22/understanding-user-intent
**视频 ID**: 1215006

### 内容总结

本课介绍如何构建 User Intent Agent。

**User Intent Agent 的作用**：
- 帮助用户头脑风暴，了解他们想要构建的知识图谱类型
- 确定用户希望通过图谱回答什么问题
- 最终输出：`approved_user_goal`

**用户目标的两部分**：
1. **Kind of Graph（图类型）**：最多三个词描述图谱类型（如 "USA freight logistics"）
2. **Description（描述）**：几句话说明图谱的意图（如 "A dynamic routing and delivery system for cargo"）

**Agent 提示结构**：
- **Role & Goal**：定义角色和目标
- **Conversational Hints**：对话提示，提供示例
- **Chain of Thought**：思维链方向

**关键工具**：
- `set_perceived_user_goal`：记录智能体理解的用户目标
- `approve_perceived_user_goal`：用户确认后，将目标设为批准状态

**检查点机制**：
- 用户必须明确批准目标后才能继续
- 防止智能体过早进入下一阶段

**工具定义示例**：
```python
def set_perceived_user_goal(kind_of_graph: str, graph_description: str, tool_context: ToolContext) -> dict:
    user_goal_data = {
        "kind_of_graph": kind_of_graph,
        "graph_description": graph_description
    }
    tool_context.state["PERCEIVED_USER_GOAL"] = user_goal_data
    return tool_success("Perceived user goal has been set")
```

---

## 视频 7: File Suggestions

**时长**: ~13 min (764 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/55puk/file-suggestions
**视频 ID**: 1215007

### 内容总结

本课介绍 File Suggestion Agent，用于推荐与用户目标相关的文件。

**File Suggestion Agent 的作用**：
- 根据用户目标，从可用文件中筛选出相关的文件
- 主要处理结构化数据文件（如 CSV、JSON）
- 输出：`approved_files`

**Agent 的工具**：
- `list_import_files`：列出 Neo4j 导入目录中的所有文件
- `sample_file`：读取文件的前 100 行内容
- `set_suggested_files`：记录建议的文件列表
- `approve_suggested_files`：用户批准后，将建议文件转为批准文件

**文件访问限制**：
- Neo4j 有导入目录限制，只能访问特定目录下的文件
- 使用 `get_neo4j_import_dir()` 获取正确的路径

**工具安全性检查**：
- 检查文件路径是否为相对路径（防止绝对路径访问）
- 验证文件是否存在

**输出示例**：
- 建议的文件：`assemblies.csv`, `components.csv`, `part_supplier_mapping.csv`, `products.csv`, `suppliers.csv`, `parts.csv`
- 忽略的文件：所有 Markdown 文件（因为当前任务是处理结构化数据）

---

## 视频 8: Schema Proposal for Structured Data

**时长**: ~29 min (1758 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/jjx7m/schema-proposal-for-structured-data
**视频 ID**: 1215008

### 内容总结

本课介绍如何使用 Critic Pattern 构建 Schema Proposal Agent。

**Schema Proposal Agent 的作用**：
- 根据已批准的文件和用户目标，设计图谱模式（Schema）
- 输出：`graph_construction_plan`

**Critic Pattern（批评模式）**：
- **Schema Proposal Agent**：提出图谱模式建议
- **Schema Critic Agent**：审查并批评建议
- **CheckStatusAndEscalate Agent**：决定循环是否继续

**图谱模式设计原则**：
1. 每个 CSV 文件都应该成为图的一部分
2. 寻找唯一标识符列
3. 单个唯一标识符 → 节点
4. 多个唯一标识符（外键关系）→ 关系
5. 确保最终图是连通图

**关系类型区分**：
1. **Full Relationship（完全关系）**：源文件直接描述两个实体之间的关系
2. **Reference Relationship（引用关系）**：源文件引用其他文件的标识符

**构建规则（Construction Rules）**：
- **节点构建规则**：指定标签、唯一列名、属性列表
- **关系构建规则**：指定关系类型、起始节点标签、结束节点标签

**工具定义**：
- `propose_node_construction`：提议节点构建规则
- `propose_relationship_construction`：提议关系构建规则
- `remove_construction_rule`：移除构建规则
- `get_proposed_construction_plan`：获取当前构建计划
- `approve_proposed_construction_plan`：批准构建计划

**循环限制**：
- 设置 `max_iterations=2`，防止无限循环
- 如果批评者不满意，将反馈传递给提议者重新修改

---

## 视频 9: Schema Proposal for UnStructured Data

**时长**: ~16 min (969 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/wwdel/schema-proposal-for-unstructured-data
**视频 ID**: 1215009

### 内容总结

本课介绍如何处理非结构化数据（Markdown 文件）。

**非结构化数据工作流**：
1. 类似结构化数据，先经过 User Intent Agent 和 File Suggestion Agent
2. 重点是 **Entity and Fact Type Proposal Agent**

**两个专业智能体**：
1. **Named Entity Recognition (NER) Schema Agent**：
   - 读取 Markdown 文件
   - 识别人名、地名、事物等命名实体
   - 区分「知名实体」（在结构化数据中已定义）和「发现实体」（新发现的）

2. **Fact Type Extraction Agent**：
   - 识别关于实体的陈述
   - 输出事实类型（Subject-Predicate-Object 三元组）
   - 例如：`product has_issue "某产品有问题"`

**输出不是提取本身，而是提取计划**：
- 实体类型列表
- 事实类型列表
- 这为后续的实际提取提供了规范

**工具定义**：
- `propose_entities` / `approve_proposed_entities`：实体的提议和批准
- `propose_facts` / `approve_proposed_facts`：事实的提议和批准
- `get_well_known_types`：从结构化数据的模式中获取已知的节点类型

---

## 视频 10: Knowledge Graph Construction - Part I

**时长**: ~13 min (785 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/lljch/knowledge-graph-construction-part-i
**视频 ID**: 1215010

### 内容总结

本课介绍如何构建用于构建域图的核心工具。

**知识图谱构建工具（Knowledge Graph Construction Tool）**：
- 可以称为「神经符号智能体」（Neuro-symbolic Agent）
- 是 LLM 和基于规则的系统的混合体

**从构建计划到实际图谱**：
- **Graph Construction Plan**：从 CSV 文件加载数据 → 生成域图
- **Knowledge Extraction Plan**：处理 Markdown 文件 → 生成词汇图和主题图

**核心工具函数**：

1. **create_uniqueness_constraint**：
   - 在数据库上创建唯一约束
   - 确保节点 ID 的唯一性

2. **load_nodes_from_csv**：
   - 使用 `LOAD CSV` 从 Neo4j 导入目录加载数据
   - 使用 `MERGE` 创建节点（存在则匹配，不存在则创建）
   - 使用 `FOREACH` 设置属性
   - 批量处理：`IN TRANSACTIONS OF 1000 ROWS`

3. **load_relationships_from_csv**：
   - 匹配 FROM 和 TO 节点
   - 使用 `MERGE` 创建关系

**Construct Domain Graph 函数**：
- 首先按顺序导入所有节点（利用唯一约束）
- 然后导入所有关系（节点已存在）

**Cypher 示例**：
```cypher
LOAD CSV WITH HEADERS FROM 'file:///' + source_file AS ROW
MATCH (from_node:LABEL {unique_column: ROW.from_column})
MATCH (to_node:LABEL {unique_column: ROW.to_column})
MERGE (from_node)-[r:RELATIONSHIP_TYPE]->(to_node)
SET r += {property: ROW.property}
```

---

## 视频 11: Knowledge Graph Construction – Part II

**时长**: ~33 min (1984 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/33uzg/knowledge-graph-construction-part-ii
**视频 ID**: 1215011

### 内容总结

本课继续讲解知识图谱构建，重点处理 Markdown 文件和实体解析。

**处理 Markdown 文件的流程**：
1. **加载文档**：使用自定义 MarkdownDataLoader
2. **分块（Chunking）**：使用正则表达式分割文本
3. **生成嵌入**：为每个分块生成向量嵌入
4. **实体提取**：使用 LLM 根据模式提取实体
5. **写入 Neo4j**：使用 KGWriter 保存图谱

**neo4j_graphrag 的 SimpleKGPipeline**：
```python
pipeline = SimpleKGPipeline(
    llm=llm,
    driver=driver,
    embedder=embedder,
    pdf_loader=markdown_loader,
    text_splitter=regex_splitter,
    schema=entity_schema,
    prompt=custom_prompt
)
```

**实体模式（Entity Schema）**：
- `node_types`：节点类型列表（如 Product, Issue, Feature）
- `relationship_types`：关系类型列表
- `patterns`：事实模式（如 `Product - HAS_ISSUE -> Issue`）

**实体解析（Entity Resolution）**：
- 将主题图中的实体与域图中的对应节点关联
- 使用 **Jaro-Winkler 距离** 计算字符串相似度
- 相似度阈值（如 < 0.1）判断是否为同一实体

**属性键关联**：
- 使用 rapidfuzz 库计算字符串相似度
- 找到匹配的键对（如 `name` ↔ `product_name`）
- 基于匹配的属性值进行实体解析

**最终步骤**：
- 执行 Cypher 查询创建 `CORRESPONDS_TO` 关系
- 连接主题图节点和域图节点
- 最终形成一个完全连通的知识图谱

---

## 视频 12: Conclusion

**时长**: <1 min (24 秒)
**链接**: https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/lesson/cc79j/conclusion
**视频 ID**: 1215012

### 内容总结

课程完成总结。

**学习成果**：
- 构建了一个多智能体系统
- 将结构化和非结构化数据转换为知识图谱
- 学会了设置每个专业智能体、设计提示、定义工具
- 掌握了智能体之间共享上下文的方法

---

## 核心概念总结

### 多智能体架构模式

| 模式 | 说明 |
|------|------|
| **协调器模式** | 顶层智能体管理整体流程，委托给子智能体 |
| **Critic Pattern** | 提议智能体和批评智能体配对，迭代优化结果 |
| **工具模式** | 智能体通过调用工具与外部系统交互 |
| **记忆模式** | 通过 ToolContext 在智能体之间共享状态 |

### 知识图谱三层结构

| 层次 | 来源 | 说明 |
|------|------|------|
| **Domain Graph** | CSV 等结构化数据 | 已知实体和关系 |
| **Lexical Graph** | 分块的 Markdown 文本 | 原始文本和向量嵌入 |
| **Subject Graph** | 提取的实体和事实 | SPO 三元组 |

### 关键技术栈

- **Google ADK**：智能体开发框架
- **Neo4j**：图数据库
- **Cypher**：图查询语言
- **LiteLLM**：LLM 接口封装
- **neo4j_graphrag**：知识图谱检索增强生成库

---

*此总结由 AI 自动生成，仅供学习参考使用*