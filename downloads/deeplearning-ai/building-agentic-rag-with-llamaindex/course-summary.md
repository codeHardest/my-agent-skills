# Building Agentic RAG with Llamaindex
# 使用LlamaIndex构建Agentic RAG

**课程来源**: DeepLearning.AI
**课程链接**: https://learn.deeplearning.ai/courses/building-agentic-rag-with-llamaindex
**导师**: Jerry Liu (LlamaIndex联合创始人兼CEO)
**合作方**: LlamaIndex
**总时长**: 约43分钟
**课程形式**: 视频 + 代码示例

---

## 课程概述

本课程由Andrew Ng主持，Jerry Liu（LlamaIndex联合创始人兼CEO）主讲，介绍了**Agentic RAG**——一种构建自主研究智能体的框架。与标准的RAG流水线（适合简单问题、单次检索调用）不同，Agentic RAG能够处理复杂问题，涉及多步骤处理、推理和决策。

课程将逐步教授从**路由（Routing）**到**工具调用（Tool Calling）**再到**多文档Agent**的完整技术栈。

---

## 第一课：路由查询引擎（Router Query Engine）
**时长**: 约9分钟
**代码示例**: 有

### 核心概念

**路由（Router）**是最简单的Agentic RAG形式。根据用户查询，路由器选择多个查询引擎中的一个来执行，而不是简单地做单次检索。

### 实现要点

1. **加载文档**: 使用LlamaIndex的`SimpleDirectoryReader`读取PDF文档（如MetaGPT论文）
2. **文本分块**: 使用`SentenceSplitter`将文档分割成1024大小的块（nodes）
3. **构建索引**: 创建两种索引
   - **向量索引（Vector Index）**: 基于嵌入相似度检索相关上下文
   - **摘要索引（Summary Index）**: 返回索引中的所有节点，适用于摘要类查询

```python
# 设置全局配置
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding()
```

4. **定义查询工具（Query Tools）**: 每个查询引擎附加元数据描述，说明该工具适合哪类问题

```python
summary_tool = QueryEngineTool(
    summary_query_engine,
    description="用于MetaGPT相关摘要问题"
)
vector_tool = QueryEngineTool(
    vector_query_engine,
    description="用于从MetaGPT论文检索特定上下文"
)
```

5. **路由器选择器**: 
   - `LLMSingleSelector`: 通过LLM提示选择单一工具
   - `PydanticSelector`: 使用OpenAI等模型的函数调用API输出结构化选择对象

### 示例演示

- **摘要查询**（"what is a summary of the document?"）→ 路由器选择摘要工具，返回所有34个文档块
- **具体问题**（"How do agents share information?"）→ 路由器选择向量搜索工具，精确定位相关段落

---

## 第二课：工具调用（Tool Calling）
**时长**: 约10分钟
**代码示例**: 有

### 核心概念

标准RAG中LLM仅用于综合（synthesis）。本课展示如何让LLM不仅**选择工具**，还能**推断参数**传递给工具。

### 实现要点

1. **FunctionTool抽象**: LlamaIndex的`FunctionTool`包装任意Python函数，自动从函数签名和文档字符串生成LLM提示

```python
from llamaIndex.core.tools import FunctionTool

def add(x: int, y: int) -> int:
    """Add two numbers"""
    return x + y

add_tool = FunctionTool.from_defaults(add)
```

2. **predict_and_call**: LLM通过函数调用API决定调用哪个工具以及传递什么参数

```python
response = llm.predict_and_call(
    [add_tool, mystery_tool],
    "What is 2 + 9 and also calculate x * y where x=2,y=9"
)
```

3. **元数据过滤器**: 扩展向量搜索，支持结构化过滤条件（如页码）

```python
from llamaIndex.core.vector_stores import MetadataFilters

filters = MetadataFilters(
    filters=[ExactMatchFilter(key="page_label", value="2")]
)
query_engine = vector_index.as_query_engine(filters=filters)
```

4. **Tool Calling Agent**: 将向量工具和摘要工具组合成多工具系统，LLM可动态选择

---

## 第三课：构建Agent推理循环（Building an Agent Reasoning Loop）
**时长**: 约11分钟
**代码示例**: 有

### 核心概念

前述方法仍是单次前向传递。对于复杂问题（多步骤、模糊问题需澄清），需要一个**完整的Agent推理循环**——多步骤推理+记忆保持。

### 实现要点

1. **Agent双组件架构**:
   - **AgentWorker（工作者）**: 负责执行下一步
   - **AgentRunner（运行器）**: 任务调度器，创建任务、协调运行、返回最终响应

2. **FunctionCallingAgentWorker**: 原生集成LLM函数调用能力

```python
from llamaIndex.core.agent import FunctionCallingAgentWorker, AgentRunner

agent_worker = FunctionCallingAgentWorker.from_tools(
    [vector_tool, summary_tool],
    llm=OpenAI(model="gpt-3.5-turbo"),
    verbose=True
)
agent = AgentRunner(agent_worker)
```

3. **单次查询vs对话保持**:
   - `agent.query()`: 单次查询，不保持状态
   - `agent.chat()`: 保持对话历史（rolling buffer）

4. **低级调试接口**:
   - 创建任务: `agent.create_task(user_input)`
   - 执行单步: `agent.run_step(task_id)`
   - 检查待办步骤: `agent.get_upcoming_steps(task_id)`
   - 注入用户反馈: 在执行过程中可注入用户输入修改Agent行为
   - 获取最终响应: `agent.finalize_response(task_id)`

### 关键能力

- **调试能力**: 追踪每步执行，发现失败点
- **可操控性**: 用户可在Agent运行中途注入反馈（如"搜索另一个文档"）

---

## 第四课：构建多文档Agent（Building a Multi-Document Agent）
**时长**: 约10分钟
**代码示例**: 有

### 核心概念

将Agent能力扩展到多文档场景。初始方法：为每个文档配置向量工具+摘要工具（3文档=6工具，11文档=22工具）。

### 挑战与解决方案

**问题**: 工具数量过多导致：
1. 上下文窗口溢出
2. 成本和延迟增加
3. LLM选择准确率下降

**解决方案**: **工具检索（Tool Retrieval）**——在工具层面进行RAG，而非文本层面

```python
from llamaIndex.core.objects import ObjectIndex, ObjectRetriever

# 将工具索引为对象
object_index = ObjectIndex.from_objects(
    all_tools,  # 所有向量工具+摘要工具
    index=VectorStoreIndex,
    retriever=VectorRetriever
)
object_retriever = object_index.as_retriever()
```

### 实现要点

1. **ObjectIndex抽象**: 将Python工具对象序列化为字符串表示并建立索引
2. **工具检索流程**:
   - 用户查询 → 检索最相关的K个工具（如top-3）→ 仅将相关工具传给Agent
3. **扩展到11篇论文**: 演示了完整的11篇Ilya 2024论文处理流程

### 示例演示

- **跨文档摘要**: "Give me a summary of both SelfRAG and LongLora" → Agent依次调用两篇论文的摘要工具
- **对比查询**: "Tell me about eval datasets in MetaGPT and compare with SWE-bench" → Agent检索相关工具并综合回答

---

## 第五课：总结与资源（Conclusion）
**时长**: 约1分钟

课程回顾：
1. **路由Agent**: 构建路由器动态选择查询引擎
2. **工具调用**: LLM选择工具并推断参数
3. **Agent推理循环**: 多步骤推理+记忆
4. **多文档Agent**: Tool Retrieval解决扩展性问题

**资源推荐**: 
- 自定义Agent实现
- 社区模板提交
- 高级文档解析服务

---

## 关键架构总结

| 组件 | 用途 |
|------|------|
| **Router** | 动态选择查询引擎（单步决策） |
| **FunctionTool** | 封装Python函数为LLM可调用工具 |
| **QueryEngine** | 封装索引+检索+综合逻辑 |
| **AgentWorker** | 执行下一步决策 |
| **AgentRunner** | 任务调度和状态管理 |
| **ObjectIndex** | 工具层面的RAG索引 |
| **ToolRetriever** | 基于查询检索相关工具子集 |

---

## 文件清单

| 文件 | 描述 |
|------|------|
| `01-introduction.vtt` | 课程介绍字幕 |
| `02-router-query-engine.vtt` | 第一课字幕 |
| `03-tool-calling.vtt` | 第二课字幕 |
| `04-building-agent-reasoning-loop.vtt` | 第三课字幕 |
| `05-multi-document-agent.vtt` | 第四课字幕 |
| `06-conclusion.vtt` | 总结课字幕 |

---

## 技术栈

- **LLM**: OpenAI GPT-3.5-turbo / GPT-4
- **框架**: LlamaIndex
- **文档**: PDF research papers (MetaGPT, LongLora, LoftQ, SWE-bench, SelfRAG等)
- **环境**: Jupyter notebooks, nest_asyncio

---

## 学习路径

```
基础RAG (单次检索)
    ↓
Router (动态选择工具)
    ↓
Tool Calling (选择+参数推断)
    ↓
Agent Reasoning Loop (多步骤+记忆)
    ↓
Multi-Document Agent (工具检索扩展)
```

---

*本笔记由Claude Code视频摘要技能生成，仅供个人学习使用*