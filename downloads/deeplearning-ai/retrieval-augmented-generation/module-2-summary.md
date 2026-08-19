# Module 2: Retrieval 检索器 (课程总结)

**课程来源**: DeepLearning.AI
**课程名称**: Retrieval-Augmented Generation (RAG)
**课程链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation
**Module 2**: Retrieval (检索器)

---

## Module 2 概述

本模块深入探讨了RAG系统中检索器（Retriever）的核心原理与技术。检索器的工作是在知识库中找到能帮助LLM响应用户提示的相关文档。这是一个极具挑战性的任务：用户以自然语言与系统对话，而非提交结构化的SQL查询；同时知识库中的文档格式多样，包括个人邮件、公司备忘录、医学期刊等多种来源。Module 2系统介绍了三种主要检索技术——关键词搜索、语义搜索和元数据过滤，以及如何通过混合搜索（Hybrid Search）将它们组合使用，最后还介绍了评估检索器性能的常用指标。

---

## 视频列表

| 序号 | 视频标题 | 时长 | 链接 | 视频 ID |
|------|---------|------|------|---------|
| 1 | Module 2 introduction | ~1 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/77dri/module-2-introduction | 1199196 |
| 2 | Retriever architecture overview | ~3 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/jjf72/retriever-architecture-overview | 1199197 |
| 3 | Metadata filtering | ~4 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/bb3k6/metadata-filtering | 1199198 |
| 4 | Keyword search - TF-IDF | ~7 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/rrngg/keyword-search-tf-idf | 1199199 |
| 5 | Keyword search - BM25 | ~4 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/66p34/keyword-search-bm25 | 1199200 |
| 6 | Semantic search - introduction | ~7 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/aam1t/semantic-search-introduction | 1199201 |
| 7 | Semantic search - embedding model deepdive | ~6 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/00us3/semantic-search-embedding-model-deepdive | 1199202 |
| 8 | Hybrid search | ~7 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/77dro/hybrid-search | 1199203 |
| 9 | Evaluating retrieval | ~8 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/558u1/evaluating-retrieval | 1199204 |
| 10 | Module 2 conclusion | ~2 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/nnrir/module-2-conclusion | 1199205 |

---

## 视频 1: Module 2 introduction

**时长**: ~1 分钟 (85秒)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/77dri/module-2-introduction
**视频 ID**: 1199196

### 内容总结

本视频是Module 2的导论，主要介绍检索器在RAG系统中的核心作用及其面临的挑战。检索器的工作看似简单——找到能帮助LLM响应提示的文档，但实际上极具挑战性。用户以自然对话方式与LLM交流，而非提交结构化查询；知识库文档格式多样（邮件、备忘录、期刊等），信息丰富但为人类阅读设计而非计算机搜索优化。检索器必须在极短时间内处理这些混乱的非结构化信息并返回最相关结果。

**核心要点**:
- 检索器基本任务：在知识库中找到能帮助LLM响应提示的文档
- 用户输入是非结构化自然语言，而非SQL查询
- 知识库文档格式多样，为人类阅读设计
- 必须在极短时间内（几分之一秒）处理并返回结果

---

## 视频 2: Retriever architecture overview

**时长**: ~3 分钟 (209秒)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/jjf72/retriever-architecture-overview
**视频 ID**: 1199197

### 内容总结

本视频从高层架构角度介绍检索器的工作原理。现代检索器采用两种主要搜索技术：**关键词搜索**（匹配prompt中的确切词汇）和**语义搜索**（理解文档含义，即使不包含确切词汇也能匹配）。每种技术返回20-50个文档组成的列表。元数据过滤允许根据用户属性（如所属部门）筛选文档。两个列表被合并形成最终排名，这种方式被称为"混合搜索"（Hybrid Search）。

**核心要点**:
- 检索器访问知识库，快速判断哪些文档与prompt最相关
- 关键词搜索：匹配确切词汇，数十年为信息检索系统提供动力
- 语义搜索：基于含义匹配，不依赖确切词汇
- 元数据过滤：根据用户属性（如部门）筛选文档
- 混合搜索结合多种技术的优势

---

## 视频 3: Metadata filtering

**时长**: ~4 分钟 (264秒)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/bb3k6/metadata-filtering
**视频 ID**: 1199198

### 内容总结

本视频介绍元数据过滤技术。元数据过滤使用刚性标准根据文档的元数据（标题、作者、日期、访问权限等）来缩小检索返回的文档范围。在典型RAG系统中，元数据过滤不用于执行检索，而是帮助缩小其他检索技术返回的结果范围。过滤器通常由用户属性（订阅状态、地理位置等）决定，而非用户提示内容。

**优势**:
- 概念简单，易于理解和调试
- 快速、成熟、经过良好优化
- 是唯一能基于刚性标准决定文档是否被检索的方法

**局限性**:
- 本质上不是搜索技术，而是细化工具
- 过度刚性，忽略文档内容
- 缺乏文档排名机制
- 必须与其他搜索技术配合使用

---

## 视频 4: Keyword search - TF-IDF

**时长**: ~7 分钟 (427秒)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/rrngg/keyword-search-tf-idf
**视频 ID**: 1199199

### 内容总结

本视频深入讲解TF-IDF关键词搜索技术。TF-IDF通过词袋模型将提示词和文档转换为稀疏向量，基于词汇出现频率评估文档相关性。视频介绍了词袋模型、稀疏向量、倒排索引、评分机制等核心概念，并详细讲解了TF-IDF算法如何结合词频（TF）和逆文档频率（IDF）来评估文档相关性。

**核心要点**:
- 词袋模型：忽略词序，只关注词汇及其出现频率
- 稀疏向量：高维向量，大多数位置为零
- 倒排索引：从词汇快速查找包含它的文档
- TF-IDF：同时考虑词在单个文档中的频率和在整体语料库中的罕见性
- TF-IDF分数是关键词检索性能的标准基准

---

## 视频 5: Keyword search - BM25

**时长**: ~4 分钟 (288秒)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/66p34/keyword-search-bm25
**视频 ID**: 1199200

### 内容总结

本视频介绍BM25（Best Matching 25）算法，这是大多数生产环境检索器使用的标准关键词搜索算法。BM25在TF-IDF基础上进行了两项重要改进：**词频饱和**（对关键词重复次数实施递减回报）和**文档长度归一化**（对长文档的惩罚也是递减的）。BM25包含两个可调超参数，允许控制词频饱和程度和文档长度归一化程度。

**核心要点**:
- BM25是当前大多数检索系统的标准关键词搜索算法
- 词频饱和：关键词出现20次的文档不会比出现10次的文档相关度高一倍
- 文档长度归一化：长文档只要关键词频率足够高仍可获得高分
- 可调超参数允许针对数据集进行调整
- 关键词搜索优势：简单、精确匹配保证；局限：依赖精确词汇匹配

---

## 视频 6: Semantic search - introduction

**时长**: ~7 分钟 (450秒)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/aam1t/semantic-search-introduction
**视频 ID**: 1199201

### 内容总结

本视频介绍语义搜索的基本概念和实现原理。语义搜索通过嵌入模型将文档和提示词映射到向量空间，基于向量距离（而非词汇匹配）来评估相关性。视频详细讲解了嵌入模型的工作机制、向量空间概念、三种常见距离度量方法（欧几里得距离、余弦相似度、点积），以及语义搜索的完整工作流程。

**核心要点**:
- 语义搜索能捕捉同义词和一词多义的细微差别
- 嵌入模型将文本映射为向量，语义相似的文本在向量空间中相近
- 高维向量空间（数百到数千维度）提供极大灵活性
- 余弦相似度是最常用的高维空间距离度量方法
- 语义搜索流程：文档向量化 → 提示词向量化 → 计算距离 → 排序返回

---

## 视频 7: Semantic search - embedding model deepdive

**时长**: ~6 分钟 (372秒)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/00us3/semantic-search-embedding-model-deepdive
**视频 ID**: 1199202

### 内容总结

本视频深入探讨嵌入模型的训练原理，重点介绍对比训练（contrastive training）技术。嵌入模型通过正样本对（语义相似的文本）和负样本对（语义不相似的文本）进行训练，迭代优化使正样本对距离缩短、负样本对距离增大。训练后，相似词汇被"拉"到向量空间的相近区域形成语义聚类。视频强调只能比较同一嵌入模型生成的向量。

**核心要点**:
- 正样本对：语义相似的文本，应在向量空间中靠近
- 负样本对：语义不相似的文本，应在向量空间中远离
- 对比训练：利用正负样本对比信息迭代优化模型参数
- 高维空间：为算法提供充足方向来反映细微语义关系
- 语义向量是抽象的且在一定程度上是随机的
- 只能比较同一嵌入模型生成的向量

---

## 视频 8: Hybrid search

**时长**: ~7 分钟 (459秒)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/77dro/hybrid-search
**视频 ID**: 1199203

### 内容总结

本视频介绍混合搜索技术，展示如何将元数据过滤、关键词搜索和语义搜索组合使用。混合搜索流程：接收提示词 → 同时执行关键词和语义搜索 → 使用元数据过滤筛选 → 通过倒数排名融合（Reciprocal Rank Fusion, RRF）算法合并排名 → 返回最终结果。RRF算法基于文档在每个排名列表中的位置分配分数，支持通过beta参数调整语义搜索和关键词搜索的权重比例。

**核心要点**:
- 混合搜索充分利用三种技术的各自优势
- RRF算法奖励在任一列表中排名高的文档
- K参数控制排名首位文档的影响力
- Beta参数允许调整语义搜索与关键词搜索的权重（推荐70%:30%）
- Top K参数决定最终返回的文档数量

---

## 视频 9: Evaluating retrieval

**时长**: ~8 分钟 (504秒)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/558u1/evaluating-retrieval
**视频 ID**: 1199204

### 内容总结

本视频探讨如何评估检索器的搜索质量。介绍了精确率（Precision）、召回率（Recall）、Top K指标、平均精确率（MAP）和平均倒数排名（MRR）等核心评估指标。精确率反映结果可信度，召回率反映检索全面性，两者之间存在权衡关系。MAP奖励将相关文档排在高位，MRR衡量平均能在多早找到相关文档。

**核心要点**:
- 精确率 = 相关文档数 ÷ 检索返回的文档总数
- 召回率 = 相关文档数 ÷ 知识库中的相关文档总数
- Top K指标标准化评估，常用范围是5到15
- MAP@K：奖励相关文档排在高位
- MRR：衡量平均能在多早找到相关文档
- 所有指标都需要人工标注的ground truth数据

---

## 视频 10: Module 2 conclusion

**时长**: ~2 分钟 (126秒)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/nnrir/module-2-conclusion
**视频 ID**: 1199205

### 内容总结

本视频是Module 2的总结课程，快速回顾了本模块探索的主要概念。检索器通常使用三种搜索技术的混合方式进行文档搜索：关键词搜索（成熟、精确匹配）、语义搜索（灵活、基于含义）和元数据过滤（严格标准）。混合搜索通过RRF算法将多种技术组合，评估指标用于判断调整超参数后检索质量的变化。学员现已具备典型RAG系统中信息检索概念的坚实基础。

**核心要点**:
- 检索器使用三种技术的混合搜索：关键词搜索、语义搜索、元数据过滤
- 关键词搜索：基于关键词频率排名，成熟且确保精确匹配
- 语义搜索：基于向量嵌入的相似度，提供关键词搜索不具备的灵活性
- 元数据过滤：基于严格标准排除文档
- 混合搜索：组合多种技术，通过RRF算法合并排名
- 评估指标用于监控和优化检索性能

---

## Module 2 关键概念总结

### 三种检索技术

| 技术 | 原理 | 优势 | 局限 |
|------|------|------|------|
| 元数据过滤 | 基于文档元数据的严格标准筛选 | 快速、成熟、刚性控制 | 非搜索技术，需与其他技术配合 |
| 关键词搜索 | 基于词汇频率匹配（TF-IDF/BM25） | 成熟、精确匹配保证 | 依赖精确词汇，无法语义匹配 |
| 语义搜索 | 基于向量嵌入的语义相似度 | 灵活、捕捉同义词/一词多义 | 较慢、计算密集 |

### 混合搜索流程

1. 接收用户prompt
2. 并行执行关键词搜索和语义搜索
3. 使用元数据过滤器筛选
4. 通过RRF算法合并两个排名列表
5. 返回Top K个最相关文档

### 评估指标

- **Recall@K**：最基础指标，衡量找到相关文档的能力
- **Precision@K**：衡量返回结果的可信度
- **MAP@K**：奖励相关文档排在高位
- **MRR**：衡量平均能在多早找到相关文档

---

## 核心概念速查

- **Retriever（检索器）**：在知识库中找到能帮助LLM响应提示的文档
- **Hybrid Search（混合搜索）**：结合关键词搜索、语义搜索和元数据过滤
- **TF-IDF**：词频-逆文档频率，关键词检索标准基准
- **BM25**：最佳匹配25，生产环境标准关键词搜索算法
- **Embedding Model（嵌入模型）**：将文本映射为向量的深度学习模型
- **Contrastive Training（对比训练）**：使用正负样本对训练嵌入模型
- **Reciprocal Rank Fusion（倒数排名融合）**：合并多个排名列表的算法
- **Cosine Similarity（余弦相似度）**：衡量向量方向相似性的度量

---

*此总结由 AI 自动生成，仅供学习参考使用*
