# How Transformer LLMs Work (课程总结)

**课程来源**: DeepLearning.AI
**课程名称**: How Transformer LLMs Work
**课程链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work
**Module 1**: How Transformer LLMs Work
**发布时间**: 2024
**下载时间**: 2026-06-04

---

## Module 1 概述

本课程由 Jay Alammar 和 Maarten Grootendorst 讲授，基于他们的著作《Hands-On Large Language Models》。课程介绍了 LLM Transformer 架构的主要组件，这些组件彻底改变了语言处理领域。课程涵盖从词袋模型到 Word2Vec、再到 Transformer 的语言表示数值化演进过程。

**视频列表**:

---

## 视频 1: Introduction
**时长**: ~5 min (307秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/nfshb/introduction
**视频 ID**: 601

### 内容总结

欢迎参加《How Transformer LLMs Work》课程。本课程由 Jay Alammar 和 Maarten Grootendorst 讲授，他们在其著作《Hands-On Large Language Models》中精美地阐释了 LLM 的底层架构。

Transformer 架构最初在 2017 年论文《Attention is All You Need》中被提出，用于机器翻译任务。原始架构由两个主要部分组成：编码器（encoder）和解码器（decoder）。编码器模型（如 BERT）提供丰富的上下文敏感表示，用于 RAG 应用；解码器模型（如 GPT）执行文本生成任务，是大多数流行 LLM 的基础。

课程内容包括：深入探讨 LLMs 的最新发展；学习 tokenization（将文本分解为 token）；理解 Transformer 网络的工作原理，聚焦于仅解码器模型；学习生成过程如何一次生成一个 token。

---

## 视频 2: Understanding Language Models: Language as a Bag-of-Words
**时长**: ~5 min (337秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/oo4d8/understanding-language-models-language-as-a-bag-of-words
**视频 ID**: 602

### 内容总结

语言对计算机来说是棘手的概念。文本是非结构化的，当用零和一或单个字符表示时会失去意义。

**Bag-of-Words（词袋模型）**：最早的表示方法之一。过程包括：
1. 将输入文本通过空格分割成单词（tokenization）
2. 创建词汇表（vocabulary），包含所有唯一单词
3. 计算每个单词在输入中出现的次数
4. 生成数值向量表示

例如，"My cat is cute" 的表示是 [0,1,0,1,0,1,1] 这样的稀疏向量，每个位置对应词汇表中的一个词。

这种方法简单但忽略了语义——"My cat is cute" 和 "That is a cute cat" 虽然意思相同，但向量表示可能不同。Bag-of-words 无法捕捉词序和语境信息。

---

## 视频 3: Understanding Language Models: (Word) Embeddings
**时长**: ~5 min (300秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/ch1aa/understanding-language-models-word-embeddings
**视频 ID**: 604

### 内容总结

**Word2Vec（2013年）**：捕获词语语义的早期成功尝试。通过在大规模文本数据（如整个 Wikipedia）上训练神经网络来生成语义表示。

工作原理：
1. 为词汇表中的每个词分配随机向量嵌入（通常5-100+维）
2. 在每个训练步骤中，取一对词，模型预测它们是否可能在句子中相邻
3. 训练过程中学习词之间的关系，并将这些信息浓缩到嵌入中

**嵌入表示含义**：例如 "cats" 在属性上可能 newborn 低、human 低、fruits 低，但 animal 高、plural 高。嵌入将这些属性值编码在向量中。

**多类型嵌入**：词嵌入（word embeddings）、句子嵌入（sentence embeddings）、文档嵌入（document embeddings）等。

嵌入的核心价值在于：语义相似的词在向量空间中彼此接近，可以通过向量运算比较词语之间的关系。

---

## 视频 4: Understanding Language Models: Encoding and Decoding Context with Attention
**时长**: ~6 min (345秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/lbu6s/understanding-language-models-encoding-and-decoding-context-with-attention
**视频 ID**: 605

### 内容总结

Word2Vec 创建的是**静态嵌入**——同一个词无论在什么语境下，嵌入都相同。例如 "bank" 可以指银行或河岸，但嵌入不变。

**RNN（循环神经网络）**的编码-解码架构：
- 编码器（Encoder）：将整个输入序列处理成一个上下文嵌入
- 解码器（Decoder）：利用这个上下文嵌入生成输出语言

**自回归生成**：每个步骤依赖之前生成的所有词。例如翻译 "I love llamas" 为荷兰语 "Ik hou van lama's" 时，逐步生成每个 token。

**问题**：单个上下文嵌入难以捕捉长而复杂序列的全部信息。

**Attention（注意力机制，2014年）**：
- 允许模型关注输入序列中彼此相关的部分
- 词之间相关性越高，注意力权重越大
- 不再传递单个上下文嵌入，而是传递所有输入词的隐藏状态给解码器
- 大幅提升了长距离依赖的处理能力

---

## 视频 5: Understanding Language Models: Transformers
**时长**: ~8 min (457秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/hrpcy/understanding-language-models-transformers
**视频 ID**: 606

### 内容总结

**Transformer 架构**基于注意力机制，不使用循环神经网络，允许并行训练。

**编码器（Encoder）**：
- 输入通过自注意力（self-attention）处理，生成上下文感知的嵌入
- 再通过前馈神经网络（feedforward neural network）
- 适合表示语言任务（如 BERT）

**解码器（Decoder）**：
- 使用 masked self-attention（掩码自注意力），防止看到未来位置
- 结合编码器的输出和已生成的内容
- 适合生成任务（如 GPT）

**BERT（2018年）**：仅编码器架构，使用遮蔽语言建模（masked language modeling）进行预训练。

**GPT（Generative Pre-Trained Transformer）**：仅解码器架构，2018年推出，从 GPT-1（1亿参数）到 GPT-2（15亿）再到 GPT-3（1750亿），能力随规模增长。

**上下文长度（Context Length）**：模型一次能处理的 token 数量，包括输入和已生成的 token。

---

## 视频 6: Architectural Overview
**时长**: ~6 min (387秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/g7roa/architectural-overview
**视频 ID**: 608

### 内容总结

Transformer 三个主要组件：

1. **Tokenizer（分词器）**：将文本分解为 token，词汇表通常约 50,000 个 token
2. **Transformer Block 堆栈**：神经网络执行大部分计算的地方
3. **Language Modeling Head（语言建模头）**：输出 token 概率分布

**生成过程**：
- 模型一次生成一个 token
- 每个 token 的生成都会加入输入序列，重新通过模型

**并行处理**：Transformer 同时处理所有输入 token，与 RNN 的顺序处理不同，这种并行化大大提高了效率。

**解码策略**：
- 贪心解码（Greedy Decoding）：始终选择最高概率 token
- Top P 采样：随机选择，允许更多多样性
- Temperature 参数控制随机性

**KV 缓存**：缓存计算结果以加速后续 token 的生成。

**时间指标**：
- Time to First Token：首次处理所有输入的时间
- 生成后续 token 是不同的过程

---

## 视频 7: The Transformer Block
**时长**: ~7 min (409秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/nbrpv/the-transformer-block
**视频 ID**: 609

### 内容总结

**Token 流程**：
1. Tokenizer 将文本分成 token
2. 查找对应的嵌入向量
3. 通过 transformer block 堆栈
4. 最终 token 的向量送入语言建模头
5. 输出下一个 token 的概率分布

**Transformer Block 两个主要组件**：

1. **前馈神经网络（Feedforward Neural Network）**：
   - 扩展→收缩的密集层结构
   - 存储"下一个词可能是什么"的统计信息
   - 例如：处理 "the Shawshank" 后，可能输出 "redemption"

2. **自注意力（Self-Attention）**：
   - 允许模型关注前面的 token
   - 将相关 token 的信息融入当前 token 的表示
   - 处理共指解析（coreference resolution）等任务

**高层次理解**：
- 自注意力 = 相关性评分 + 信息组合
- 对当前 token 进行评分，确定哪些其他 token 与之最相关
- 将相关 token 的信息整合到当前表示中

---

## 视频 8: Self-Attention
**时长**: ~10 min (626秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/bpx95/self-attention
**视频 ID**: 610

### 内容总结

**自注意力的两个步骤**：
1. **相关性评分（Relevance Scoring）**：计算当前 token 与其他 token 的相关性
2. **信息组合（Combining Information）**：根据评分加权组合相关信息

**Query、Key、Value 矩阵**：
- 每个 token 有三个向量：query、key、value
- 通过矩阵乘法计算相关性分数：query · key^T
- softmax 归一化得到注意力权重

**多头注意力（Multi-Head Attention）**：
- 多个注意力头并行工作
- 每个头有独立的 Q、K、V 权重矩阵
- 输出被拼接并投影

**效率优化**：

1. **多查询注意力（Multi-Query Attention）**：
   - 所有注意力头共享同一个 K 和 V 矩阵
   - 减少参数量，加速计算

2. **分组查询注意力（Grouped Query Attention，GQA）**：
   - 使用多个 K、V 组（少于注意力头数）
   - Llama 3.1 使用 32 个注意力头但只有 8 个 key-value 头

3. **稀疏注意力（Sparse Attention）**：
   - 不是每层都允许全注意力
   - 某些层只关注最近的 token（如最后 4/16/32 个）
   - 降低计算成本

**Ring Attention**：用于处理 100K-1M token 超长上下文的技术。

---

## 视频 9: Recent Improvements
**时长**: ~11 min (638秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/od9s5/recent-improvements
**视频 ID**: 603

### 内容总结

**2024年 Transformer Block 的变化**：

1. **位置编码（Positional Encoding）**：
   - 早期：静态位置编码（学习或正弦/余弦）
   - 现代：Rotary Embeddings（RoPE），在自注意力层内添加位置信息

2. **层归一化（Layer Normalization）**：
   - 从残差连接内部移到前面（Pre-LN）
   - 提高训练稳定性

3. **分组查询注意力（GQA）**：替代多查询注意力

4. **残差连接（Residual Connections）**：信息从层开始处传递到结束处

**训练数据打包**：
- 朴素方法：用 padding 填充短文档到固定长度
- 高效方法：将多个短文档打包成一行，减少 padding

**Mixture of Experts（专家混合）**：
- 每个前馈网络层有多个"专家"网络
- 路由器决定使用哪个专家
- 不是领域专家，而是 token 级别的句法专家

---

## 视频 10: Mixture of Experts (MoE)
**时长**: ~10 min (567秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/ktp7u/mixture-of-experts-moe
**视频 ID**: 683

### 内容总结

**MoE 的两个主要组件**：

1. **Experts（专家）**：
   - 不是领域专家（如心理学、生物学）
   - 而是 token 级别的句法专家（标点、动词、连词等）
   - 每个专家是一个前馈神经网络
   - 只激活部分专家（稀疏模型）

2. **Router（路由器）**：
   - 一个小型的 FFN
   - 为每个专家生成概率分数
   - 选择最合适的专家处理当前输入

**Mixtral 8x7B 示例**：
- 8 个专家，每个约 5.6B 参数（不是精确的 7B）
- 共享参数约 1B
- 总稀疏参数 46B
- 但推理时只用 2 个专家，所以活跃参数少得多

**优缺点**：
- 优点：推理成本低（只用部分专家）、性能高、减少冗余计算
- 缺点：需要大量内存加载所有专家（即使不用）、训练复杂、可能过拟合单个专家

**应用**：MoE 层只影响前馈网络，不影响注意力机制，因此非 Transformer 模型（如 Mamba、Jamba）也可以使用。

---

## 视频 11: Conclusion
**时长**: ~20 sec (19秒)
**链接**: https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/newqc/conclusion
**视频 ID**: 600

### 内容总结

恭喜！你现在对大型语言模型和 Transformer 有了扎实的理解。希望你能将 LLM 视为一个可解释的系统，而不是黑盒子，这将帮助你更有效地使用它们。

---

## Module 1 完整视频列表

| 序号 | 视频标题 | 时长 | 链接 | 视频 ID |
|------|---------|------|------|---------|
| 1 | Introduction | ~5 min | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/nfshb/introduction | 601 |
| 2 | Language as a Bag-of-Words | ~5 min | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/oo4d8/understanding-language-models-language-as-a-bag-of-words | 602 |
| 3 | Word Embeddings | ~5 min | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/ch1aa/understanding-language-models-word-embeddings | 604 |
| 4 | Encoding and Decoding Context with Attention | ~6 min | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/lbu6s/understanding-language-models-encoding-and-decoding-context-with-attention | 605 |
| 5 | Transformers | ~8 min | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/hrpcy/understanding-language-models-transformers | 606 |
| 6 | Architectural Overview | ~6 min | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/g7roa/architectural-overview | 608 |
| 7 | The Transformer Block | ~7 min | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/nbrpv/the-transformer-block | 609 |
| 8 | Self-Attention | ~10 min | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/bpx95/self-attention | 610 |
| 9 | Recent Improvements | ~11 min | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/od9s5/recent-improvements | 603 |
| 10 | Mixture of Experts (MoE) | ~10 min | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/ktp7u/mixture-of-experts-moe | 683 |
| 11 | Conclusion | ~20 sec | https://learn.deeplearning.ai/courses/how-transformer-llms-work/lesson/newqc/conclusion | 600 |

---

## Module 1 关键概念总结

### 核心概念

- **Tokenization**：将文本分解为 token，词汇表大小通常约 50,000
- **Word Embeddings**：将词映射到语义向量空间，语义相近的词向量接近
- **Bag-of-Words**：简单的词频统计表示，忽略语序和上下文
- **Attention Mechanism**：允许模型关注输入中相关的部分
- **Self-Attention**：同一序列内 token 之间的注意力
- **Transformer**：基于注意力机制无 RNN 的架构，可并行训练
- **Encoder/Decoder**：编码器生成嵌入表示，解码器生成文本
- **Positional Encoding**：为 token 添加位置信息（RoPE 是现代方法）
- **Multi-Head Attention**：多个注意力头并行工作
- **Grouped Query Attention**：高效注意力变体
- **Mixture of Experts**：稀疏激活的前馈网络专家

### 架构演进

1. **Bag-of-Words** → 简单词频，忽略语义
2. **Word2Vec** → 语义嵌入，但仍是静态
3. **RNN + Attention** → 上下文感知，但仍难以并行
4. **Transformer** → 全注意力机制，可并行
5. **Modern Transformers** → RoPE、GQA、MoE 等优化

### 三种架构类型

| 类型 | 特点 | 代表模型 |
|------|------|---------|
| Encoder-only | 表示语言，生成嵌入 | BERT |
| Decoder-only | 生成文本 | GPT 系列 |
| Encoder-Decoder | 兼顾两者 | T5 |

---

*此总结由 AI 自动生成，仅供学习参考使用*