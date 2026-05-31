# Module 4: LLMs and Text Generation (课程总结)

**课程来源**: DeepLearning.AI
**课程名称**: Retrieval-Augmented Generation
**课程链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation
**Module 4**: LLMs and Text Generation

---

## Module 4 概述

Module 4 专注于 LLM（大型语言模型）的核心概念，包括 Transformer 架构、采样策略、模型选择、以及如何通过 Prompt Engineering 增强 RAG 系统。还涵盖了幻觉处理、性能评估、Agentic RAG 和微调与 RAG 的对比。

**视频列表**:

---

## 视频 1: Module 4 introduction
**时长**: ~1 min (71s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/ffjd0g/module-4-introduction
**视频 ID**: 1199215

# 视频摘要：Module 4 introduction

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/ffjd0g/module-4-introduction
- **时长**: 71秒 (约1分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:12:08

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
本视频是RAG（检索增强生成）课程的Module 4课程介绍。视频主要介绍了本模块的核心主题——大语言模型（LLM），强调尽管检索器是RAG系统的关键组件，但LLM才是真正的核心大脑，负责利用检索到的信息生成高质量响应。课程将涵盖Transformer架构、LLM调用与编码实践、高级性能优化技术等内容，最终通过编程实践任务帮助学习者构建完整的RAG系统。

## 核心要点
1. **LLM的核心地位**：在RAG系统中，检索器负责查找和准备有用信息，但最终使用这些信息生成高质量响应的任务由LLM承担
2. **Transformer架构深入**：本模块将深入探讨LLM所基于的Transformer架构
3. **LLM调用与编码**：学习如何构建LLM调用和代码，实现基础工作流程
4. **迭代优化**：通过迭代添加组件，完善工作流程确保LLM提供高质量、基于检索信息的响应
5. **高级技术探索**：展示突破LLM性能极限的高级技术
6. **实践指导**：提供针对典型RAG项目的实用方法和建议
7. **编程实践任务**：模块结尾提供动手编程作业，基于模块主题构建RAG系统
8. **理论与实践结合**：强调动手实践的重要性，邀请学习者亲自动手操作LLM
9. **课程衔接**：作为Module 4的引入视频，为后续深入学习做铺垫
10. **系统整体视角**：帮助学习者从系统层面理解LLM在RAG架构中的作用

## 详细内容（保留所有原始信息）

### 1. RAG系统中LLM的核心作用

视频开篇即强调LLM在RAG系统中的核心地位。讲师明确指出，虽然检索器（retriever）是RAG系统的关键组成部分，但LLM才是真正的"大脑"（the real brains of the operation）。这一比喻清晰地阐明了两者的关系：检索器负责信息检索和准备，但最终需要LLM来实际使用这些信息生成高质量响应。

### 2. 本模块的学习内容

本模块的核心教学目标是帮助学习者全面理解大语言模型，包括：
- **LLM工作原理**：深入了解大语言模型如何处理和生成文本
- **性能优化技术**：学习在RAG系统中提升LLM性能的具体技术
- **Transformer架构**：深入研究支撑LLM的Transformer架构
- **LLM调用实践**：学习如何编写代码构建LLM调用

### 3. 学习路径与方法论

课程采用循序渐进的教学方法：
- **基础构建**：首先学习构建基础的LLM工作流程和代码实现
- **迭代完善**：在此基础上迭代添加组件，不断优化系统
- **质量保障**：确保LLM生成的响应高质量且基于检索器提供的信息
- **高级技术**：介绍突破LLM性能极限的前沿技术
- **实践验证**：提供针对典型RAG项目的实用建议

### 4. 实践环节

每个模块都设计了实践项目，本模块末尾的学习任务包括：
- 基于模块涵盖的主题构建RAG系统
- 动手编程实践
- 实际动手操作大语言模型

### 5. 课程互动邀请

视频最后，讲师表达了对学习者动手实践的期待，并邀请学习者进入下一视频开始学习。

## 完整字幕原文
```
The retriever is a critical part of your RAG system, but the LLM is the real brains of the operation. The retriever can find and prepare useful information, but at the end of the day, it's the LLM that needs to actually use that information to generate a high-quality response. In this module, you'll learn all about large language models, how they work, as well as specific techniques that you can use to improve their performance within a RAG system. You'll dive deep on the transformer architecture that LLMs are built on, learn how to construct LLM calls and code, and then iteratively add to that basic workflow to ensure the LLM provides high-quality responses that are grounded in the information provided by the retriever. You'll see some advanced techniques that push the limits of LLM performance, but also get practical advice for what approaches tend to work for a typical RAG project. As always, at the end of the module, you'll find a hands-on programming assignment where you'll get to build out a RAG system based on the topics covered in the module. I hope you enjoy getting hands-on with large language models. Join me in the next video and let's get started.
```

## 关键引述/重要观点

> "The retriever is a critical part of your RAG system, but the LLM is the real brains of the operation." [无时间戳信息]

> "The retriever can find and prepare useful information, but at the end of the day, it's the LLM that needs to actually use that information to generate a high-quality response." [无时间戳信息]

> "You'll dive deep on the transformer architecture that LLMs are built on, learn how to construct LLM calls and code, and then iteratively add to that basic workflow to ensure the LLM provides high-quality responses that are grounded in the information provided by the retriever." [无时间戳信息]

> "You'll see some advanced techniques that push the limits of LLM performance, but also get practical advice for what approaches tend to work for a typical RAG project." [无时间戳信息]

> "At the end of the module, you'll find a hands-on programming assignment where you'll get to build out a RAG system based on the topics covered in the module." [无时间戳信息]

> "I hope you enjoy getting hands-on with large language models. Join me in the next video and let's get started." [无时间戳信息]

## 相关话题/关键词
- 大语言模型 (LLM)
- RAG系统 (Retrieval-Augmented Generation)
- 检索器 (Retriever)
- Transformer架构
- LLM调用
- 代码构建
- 工作流程优化
- 响应质量
- 高级技术
- 性能优化
- 编程实践
- 动手实践
- 迭代开发
- 信息检索
- 检索增强生成

## 技术信息
- 字幕字数: 1177
- 字幕字符数: 1177
- 时间戳条目数: 0
- 处理时间: 2026-05-28 14:12:08

---

## 视频 2: Transformer architecture
**时长**: ~8 min (539s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/yy164k/transformer-architecture
**视频 ID**: 1199217

# 视频摘要：Transformer architecture

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/yy164k/transformer-architecture
- **时长**: 539秒 (约8分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:12:18

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
本视频深入探讨了支撑大型语言模型(LLM)的Transformer架构，解释了RAG系统为何有效工作的底层原理。视频详细介绍了Transformer的核心组件（编码器和解码器）、token处理流程、注意力机制、前馈神经网络的工作原理，以及这些技术如何影响RAG系统的设计决策。

## 核心要点
1. Transformer架构起源于2017年的开创性论文"Attention is All You Need"，最初用于解决机器翻译问题
2. Transformer包含两大核心组件：编码器(Encoder)和解码器(Decoder)
3. 大多数LLM仅包含解码器组件，因为它们只关注文本生成任务
4. 编码器通常用于嵌入模型，因为其目标是开发丰富的文本语义表示
5. Prompt首先被分割成tokens，每个token被分配初始密集向量表示（首次猜测）
6. 每个token还会获得一个位置向量，用于捕获其在prompt中的位置信息
7. 注意力机制允许每个token查看所有其他token的意义和位置，决定关注哪些token
8. 注意力头(Attention Heads)用于分配注意力权重，不同注意力头专门处理不同类型的词语关系
9. 较小的模型可能使用8到16个注意力头，较大的模型可能使用超过100个
10. 前馈阶段是LLM中最大的部分，包含最多的参数
11. LLM会通过注意力层和前馈层重复处理8到64次，逐步细化理解
12. 基于精细化的向量嵌入，模型计算词汇表中所有tokens的概率分布
13. LLM从概率分布中选择下一个tokenprobable tokens被选择频率更高
14. 生成完整回复需要重复整个过程，直到达到token限制或生成特殊的结束token
15. Transformer架构的设计动机解释了RAG系统的多个方面：为何有效、本质随机性、计算成本高

## 详细内容（保留所有原始信息）

### 一、Transformer架构的历史与背景

Transformer架构最初是在2017年一篇名为"Attention is All You Need"的开创性论文中提出的，该论文专注于解决机器翻译问题。Transformer架构有两个主要组件：编码器（Encoder）和解码器（Decoder）。编码器负责处理原始文本（例如一段德语文本）， develops a deep contextual understanding of the paragraph's meaning（Developing a deep contextual understanding of the paragraph's meaning）。解码器随后使用对德语文段的深入理解来生成新的英文版本。

大多数大型语言模型（LLM）只包含第二个组件——解码器，因为它们只关心文本生成任务。编码器则通常用于嵌入模型（embedding models）中，因为它们的目标是开发丰富的文本语义表示。

### 二、Prompt在LLM中的旅程——Tokenization阶段

让我们追踪一个prompt在LLM中的旅程，也就是在Transformer解码器组件中的旅程。发生的第一件事是：你的prompt被分割成tokens。一旦文本被tokenized（分词），每个token被分配一个初始密集向量表示（initial dense vector representation）。这个向量基本上是这个token含义的首次猜测（first guess）。这些猜测是静态的，所以每次你向LLM输入相同的token，它都会被分配相同的首次猜测向量。

接下来，每个token被分配一个位置向量（positional vector），用于捕获它在prompt中的位置。一旦这些首次猜测嵌入向量和位置向量被创建，它们就会被发送进行进一步处理。

### 三、注意力机制（Attention Mechanism）

Tokens现在进入Transformer的注意力机制。每个token基本上会查看prompt中的所有其他token，并且能够看到它们的含义和位置。每个token然后决定它应该最关注哪些其他token。

注意力本质上是一种花哨的说法，表示哪些其他tokens应该对我的含义产生最大的影响。以一个句子为例："the brown dog sat next to the red fox"，单词"dog"可能会最关注"brown"和"sat"，因为这些词与"dog"直接相关。你可以将dog视为将其注意力的70%分配给brown，20%分配给sat，其余10%分布在所有其他tokens上。

用于分配这种注意力的机制被称为注意力头（attention head），大多数模型实际上包含许多注意力头，这些注意力头专门处理词语之间不同类型的关系。你可以将此想象为一个专门处理物体及其描述之间关系的注意力头，因此单词"fox"可能将其所有注意力集中在"brown"上。另一个注意力头可能专门处理物体之间的空间关系，因此在该注意力头中，"fox"可能会更关注"sat"和"next"。

实际上，每个注意力头捕获的关系并不是人类分配的一组整齐的关系，而是在模型训练过程中学到的复杂而抽象的关系集。较小的模型可能使用8到16个注意力头，但较大的模型可能使用超过100个。

这很重要的原因是：不仅每个token在跟踪它与文本中每个其他token的关系，而且它们会以稍微不同的视角或关注点多次重复这样做。结果是，注意力机制 develop a very detailed representation of the relationships between all the tokens in the text（Develops a very detailed representation of the relationships between all the tokens in the text）。

### 四、前馈阶段（Feedforward Phase）

一旦每个token分配了所有注意力分数，信息就进入前馈阶段。这是LLM迄今为止最大的部分，意味着它包含最多的参数。基于每个token的原始嵌入、位置和注意力，它为每个token分配更新的向量嵌入。这些新向量基本上是每个token真正含义的第二次猜测，但现在由文本中其他tokens的上下文所 informing（Informing）。

然后大多数LLM重复整个过程。第二次猜测的向量被反馈到注意力和前馈机制中，生成每个token含义的新而更精细的第三次猜测向量。一个典型的LLM实际上可能会将这些向量通过这些层传递8到64次，在每个阶段逐渐细化其理解。

### 五、Token生成过程

现在，LLM准备好开始生成。基于它生成的高度精细化的向量嵌入，模型会问：根据我的训练数据，哪些tokens接下来可能出现？这被计算为模型词汇表中所有tokens的概率分布。通常，少量tokens有很高的概率出现在下一个，但如果你的模型识别100,000个tokens，每个token都会被分配一个概率，即使绝大多数基本上为零。

最后，LLM从这个分布中选择一个token，根据每个token分配的概率加权选择。Probable tokens are chosen more often, but in theory, any token has at least a tiny chance of being picked（Probable tokens are chosen more often, but in theory, any token has at least a tiny chance of being picked）。所选的token被附加到prompt的末尾，经过所有这些工作，LLM又生成了一个token。

如果你想生成第二个token，模型必须重复整个过程，但这次要考虑原始tokens和它附加的那个token。这确保新的tokens在原始tokens和它生成的tokens的上下文中都有意义。这意味着早期的随机token选择也将影响稍后选择哪个token。

为了生成完整的回复，模型一遍又一遍地执行这个过程，直到它达到你为该回复设置的token限制，或者它选择生成一个特殊的end-of-completion token，表示它完成了。LLM生成的tokens可能会完成一个短语或回答一个问题，但无论它们的目的是什么，它们可以被去tokenized（de-tokenized）为纯文本并返回给用户。

### 六、Transformer架构对RAG系统设计的启发

让我们看看这个Transformer架构的部分内容如何激发RAG系统设计的许多元素。

首先，它有助于解释RAG首先为何有效。LLM能够深入理解添加到prompt中的信息的含义和相关性。这归功于注意力机制的处理以及前馈层中包含的世界知识。

其次，它突出了LLM仍然是 inherent random（本质上随机的）。即使你在prompt中注入了有意义的 information，LLM可能会随机选择不基于该信息生成文本。控制这种随机性并确认你的LLM将其答案基于检索到的信息仍然是必要和重要的。

第三，它只是突出了LLM在计算上是多么 expensive（昂贵的）。生成单个token需要大量处理，而这种成本实际上随着prompt或回复长度的增加而增长。毕竟，每个token需要查看所有其他token才能充分理解自己的含义。正如你稍后将探索的，运行RAG系统的大部分成本来自运行这些 powerful but expensive transformer models（强大但昂贵的Transformer模型）。

## 完整字幕原文
```
Your retriever just returned a bunch of relevant documents, and you're ready to build your augmented prompt. Send it to your LLM and get back a response grounded in that retrieved information. You've seen this process many times in this course, but now it's time to dive one level deeper and ask, why does this even work? How is an LLM able to make sense of that retrieved information? More importantly, how can you use that knowledge to build even more capable RAG systems? To answer all of that, let's look a little deeper at the transformer architecture that LLMs are built on. The transformer was proposed in a seminal paper from 2017 titled Attention is All You Need, which was focused on the problem of machine translation. The transformer had two major components, an encoder and a decoder. The encoder would process the original text, say a paragraph written in German, developing a deep contextual understanding of the paragraph's meaning. The decoder would then use this deep understanding of the German paragraph to generate a new English version of it. Most LLMs only include the second decoder component, as they just care about text generation. Encoders, meanwhile, are typically used inside embedding models, since their goal is to develop rich semantic representations of text. Let's trace a prompt's journey through an LLM, and therefore through the decoder component of a transformer. The first thing that happens is your prompt is split into tokens. Once the text is tokenized, each token is assigned an initial dense vector representation. This vector is basically a first guess of the meaning of that token. These guesses are static, so every time you feed an LLM the same token, it'll be assigned the same first guess vector. Next, each token is given a positional vector that captures where it's located in the prompt. Once these first guess embedding vectors and positional vectors have been created, they're sent along for processing. The tokens now enter the attention mechanism of the transformer. Each token essentially looks at every other token in the prompt, and can see both their meaning and their position. Each token then decides which other tokens it should pay the most attention to. Attention is basically a fancy way of saying which other tokens should have the biggest impact on my meaning. In a sentence, the brown dog sat next to the red fox, the word dog would probably pay the most attention to brown and sat, since those words directly relate to the dog. You can think of dog as assigning 70% of its attention to brown, 20% to sat, and the remaining 10% distributed across all the other tokens. The mechanism used to assign this attention is called an attention head, and most models actually include many attention heads that specialize in different types of relationships between words. You can think of this as one attention head that specializes in relationships between objects and their descriptions, so the word fox might focus all of its attention on brown. Another attention head might instead specialize in spatial relationships between objects, and so in that head, fox might pay much more attention to sat and next. In reality, the relationships captured by each attention head are not a neat set of relationships assigned by humans, but are rather a complex and abstract set of relationships learned during the model's training. Smaller models might use 8 to 16 attention heads, but larger ones might use over 100. The reason this is important is that not only is every token tracking its relationship to every other token in the text, but they're doing so many different times over, each time with a slightly different point of view or focus. The result is, the attention mechanism develops a very detailed representation of the relationships between all the tokens in the text. Once every token has assigned all its attention scores, the information enters the feedforward phase. This is by far the biggest part of the LLM, meaning it contains by far the most parameters. Based on each token's original embedding, position, and attention, it assigns updated vector embeddings for each token. These new vectors are basically a second guess of each token's true meaning, but now informed by the context of the other tokens in the text. Most LLMs then repeat this entire process. The second guess vectors are fed back into the attention and feedforward mechanism, generating new and more refined third guess vectors of each token's meaning. A typical LLM might actually pass these vectors through these layers somewhere between 8 to 64 times, gradually refining its understanding at each stage. Now, the LLM is ready to start generating. Based on the highly refined vector embeddings it generated, the model asks, based on my training data, what tokens are likely to come next? This is calculated as a probability distribution across all tokens in the model's vocabulary. Typically, a handful of tokens have a high probability of appearing next, but if your model recognizes 100,000 tokens, each one is assigned a probability even if the vast majority are essentially zero. Finally, the LLM picks one token from this distribution, weighting the choice by every token's assigned probability. Probable tokens are chosen more often, but in theory, any token has at least a tiny chance of being picked. You'll learn more about how to adjust these probabilities and so how the LLM chooses new tokens later in this module. The chosen token is appended to the end of the prompt, and after all that work, the LLM has generated one more token. If you want to generate a second token, the model has to repeat the entire process, only this time considering both the original tokens and the one it added on. This ensures new tokens make sense in the context of both the original tokens and the ones it generated. This means early random token choices will influence which token is chosen later on as well. To generate a full completion, the model does this process over and over again until it either reaches a token limit you've set for that completion or it chooses to generate a special end-of-completion token indicating that it's done. The tokens that the LLM generated might complete a phrase or an answer to a question, but whatever their purpose, they can be de-tokenized into plain text and returned to the user. That was quite a journey through an LLM. So let's look at how parts of this transformer architecture motivate many elements of the design of a RAG system. First, it helps to motivate why RAG works in the first place. LLMs are able to deeply understand the meaning and relevance of the information added to the prompt. This is thanks to the processing done by the attention mechanism and the world knowledge contained in the feed-forward layers. Second, it highlights that LLMs are still inherently random. Even if you inject meaningful information in your prompt, LLMs may randomly choose not to generate text based on that information. Controlling this randomness and confirming your LLM grounds its answers in retrieved information is still necessary and important. Third, it just highlights how computationally expensive an LLM is. Generating a single token takes a lot of processing and that cost actually grows as the length of the prompt or completion does. After all, each token needs to look at every other one to fully understand its own meaning. As you'll explore later, most costs from running a RAG system come from running these powerful but expensive transformer models. That's a good summary of how LLMs work under the hood. Now let's turn our attention, no pun intended, to how you can refine their behavior inside a RAG system.
```

## 关键引述/重要观点

> "The transformer was proposed in a seminal paper from 2017 titled Attention is All You Need, which was focused on the problem of machine translation. The transformer had two major components, an encoder and a decoder."

> "Most LLMs only include the second decoder component, as they just care about text generation. Encoders, meanwhile, are typically used inside embedding models, since their goal is to develop rich semantic representations of text."

> "Attention is basically a fancy way of saying which other tokens should have the biggest impact on my meaning."

> "In reality, the relationships captured by each attention head are not a neat set of relationships assigned by humans, but are rather a complex and abstract set of relationships learned during the model's training."

> "A typical LLM might actually pass these vectors through these layers somewhere between 8 to 64 times, gradually refining its understanding at each stage."

> "Probable tokens are chosen more often, but in theory, any token has at least a tiny chance of being picked."

> "First, it helps to motivate why RAG works in the first place. LLMs are able to deeply understand the meaning and relevance of the information added to the prompt."

> "Second, it highlights that LLMs are still inherently random. Even if you inject meaningful information in your prompt, LLMs may randomly choose not to generate text based on that information."

> "Third, it just highlights how computationally expensive an LLM is. Generating a single token takes a lot of processing and that cost actually grows as the length of the prompt or completion does."

## 相关话题/关键词

- Transformer架构
- Attention is All You Need
- 编码器 (Encoder)
- 解码器 (Decoder)
- 大型语言模型 (LLM)
- 机器翻译
- Tokenization (分词)
- 向量嵌入 (Vector Embeddings)
- 位置向量 (Positional Vectors)
- 注意力机制 (Attention Mechanism)
- 注意力头 (Attention Heads)
- 前馈神经网络 (Feedforward Neural Networks)
- 概率分布 (Probability Distribution)
- RAG系统 (Retrieval-Augmented Generation)
- Token生成
- 参数数量
- 语义表示
- 上下文理解
- 模型训练
- 计算成本

## 技术信息

- 字幕字数: 7711
- 字幕字符数: 7711
- 时间戳条目数: 0
- 处理时间: 2026-05-28 14:12:18

---

## 视频 3: LLM sampling strategies
**时长**: ~8 min (492s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/8850gm/llm-sampling-strategies
**视频 ID**: 1199218

# 视频摘要：LLM sampling strategies

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/8850gm/llm-sampling-strategies
- **时长**: 492秒 (约8分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:12:35

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
本视频深入探讨了大语言模型(LLM)中随机性的核心原理及其控制方法，详细介绍了贪婪解码、温度参数、Top K采样、Top P采样、重复惩罚和Logit Biasing等多种采样策略，并通过实际案例展示了如何通过调整这些参数来优化LLM的输出行为，以适应不同应用场景的需求。

## 核心要点
1. **随机性本质**：LLM生成的每个token都是基于概率分布的加权随机选择，而非确定性输出
2. **概率分布特征**：分布曲线左侧高尖峰表示模型置信度高，扁平分布表示不确定性高
3. **贪婪解码(Greedy Decoding)**：始终选择最高概率token，使输出完全确定性，但可能导致可预测性和重复循环问题
4. **温度参数(Temperature)**：控制概率分布形态，Temperature=1为原始分布，0为完全贪婪解码，高于1则使分布更平坦
5. **Top K采样**：限制模型仅从概率最高的K个token中选择，如设置top 5
6. **Top P采样(核采样)**：选择累积概率达到阈值P的所有token，动态调整选择范围
7. **Top P优势**：相比Top K更具动态性，能根据模型置信度自动调整候选token池大小
8. **重复惩罚(Repetition Penalty)**：降低已出现词汇的再次选择概率，提升输出自然度
9. **Logit Biasing**：直接调整特定token的选择概率，可用于过滤不当内容或确保分类器输出特定类别
10. **推荐配置**：一般用途推荐temperature=0.8、top p=0.9、repetition penalty=1.2
11. **场景适配**：代码生成和事实问答适合低温度低top p，创意场景适合高温度高top p
12. **迭代调优**：通过实验调整各参数，逐步优化LLM行为以适配具体应用

## 详细内容（保留所有原始信息）

### 一、LLM随机性的基本原理

大语言模型运作的核心在于理解并控制其内在的随机性。每个token添加到生成结果中的过程本质上是一个加权随机选择过程。以"the sky is"这个提示为例，token的概率分布呈现如下特征：Blue有50%的概率作为下一个token出现，bright有25%的概率，其他token的概率均在10%以下，并迅速衰减至1%以下。

从视觉上看，概率分布曲线的形态具有重要的指示意义。当曲线在左侧呈现高尖峰时，表明模型对其选择具有较高的置信度，只有极少数token有实际被选中的机会。相反，较为平坦的分布则代表模型存在较大的不确定性，意味着模型有多个可能的生成方向，且没有明显的最优选择。解码并控制这个概率分布曲线的形态，是调优LLM行为的关键所在。

开源大语言模型允许用户查看每一步生成的token概率分布，这对于理解和调试模型行为非常有价值。通过观察这些概率分布，开发者可以深入了解模型在不同情境下的决策模式。

### 二、贪婪解码(Greedy Decoding)

贪婪解码是一种简单直接的策略，它指示LLM不进行随机选择，而是始终选择概率最高的token。这种方法的主要优势在于使LLM的行为完全确定性：给定相同的提示，模型将始终生成完全相同的响应。这种可重复性在某些应用场景中非常重要，例如代码补全或系统调试。

然而，贪婪解码也存在明显的缺点。首先，它可能导致输出文本过于可预测，文字可能显得平淡、刻板或不够自然。其次，更严重的问题是LLM有时会陷入重复循环，不断生成相同的词序列。这是因为LLM本身并不关心整体完成质量，它只是机械地选择下一个最高概率的token，一旦进入重复循环，就没有任何机制能够打破这个循环。

尽管存在这些潜在缺陷，在需要高度可预测性和确定性输出的场景中，贪婪解码仍然是合理的选择，比如代码补全任务或作为调试系统的临时设置。

### 三、温度参数(Temperature)

温度是控制LLM随机性最广泛使用的参数，可以将其想象为一个调节概率分布形态的旋钮。温度参数的设置直接影响模型生成文本的多样性和创造性。

- **Temperature = 1**：这是默认设置，会返回原始的概率分布，不做任何修改
- **Temperature < 1**：降低温度会导致分布变得更加尖锐和集中，只有最高概率的token才有被选中的机会，排序顺序不变，但各token被选中的概率发生变化
- **Temperature = 0**：当温度设为0时，模型执行贪婪解码，只有概率最高的单个token拥有100%的选择概率
- **Temperature > 1**（如1.1-1.3范围）：提高温度会使概率分布变得更加平坦，给低概率token更多被选中的机会，这会产生更多的变化性和更具创意感的文本
- **Temperature过高**：会导致分布过于平坦，几乎所有token都有相等的选择机会，即使它们可能不太合理

无论设置何种温度，概率分布曲线的右侧仍会有一条长长的尾巴，包含大量无意义的token，只是被选中的概率较低。

### 四、Top K采样

Top K采样是最简单的补充采样技术之一，它限制了LLM的选择范围，仅允许从概率最高的K个token中进行选择。例如，同时设置temperature为1.1，并将LLM限制为从概率最高的5个token中选择。这种方法有效地过滤掉了分布尾巴中的低质量token，同时保持了一定的随机性。

Top K采样的一个潜在问题是它总是从固定数量的候选token中选择，而不考虑实际概率分布的形态。这意味着无论模型对某个选择有多大把握，候选池的大小始终保持不变。

### 五、Top P采样(核采样)

Top P采样是一种更动态的方法，它限制LLM从累积概率达到某个阈值的所有token中选择。例如设置top p为85%，模型会从分布左侧开始，依次累加各token的概率，直到累积概率超过85%，然后只从这个候选集中选择下一个token。

Top P采样相比Top K更具响应性和动态性。在Top K中，LLM始终从相同规模的token池中选择，无论分布形态如何。而Top P则能根据模型的置信度自动调整选择范围：当LLM比较确定时（少数token具有很高概率），它会将选择限制在少数最可能的token上；当LLM不确定性较高时（分布平坦，没有明显最优选择），它会允许从更大的潜在token池中选择。

### 六、重复惩罚(Repetition Penalty)

大语言模型有时会反复使用相同的词汇或短语，这会使生成的文本听起来不自然。许多LLM提供了重复惩罚功能，可以降低已经在生成结果中出现过的词汇的再次选择概率。这种技术能够使生成的文本听起来更自然、更有变化。

重复惩罚通过调整已出现词汇的概率来实现，开发者可以根据需要设置惩罚的强度。

### 七、Logit Biasing（Logit偏置）

大多数LLM还允许直接增加或减少特定token的选择概率，这通常称为logit biasing或logit偏置。这种偏置会永久性地调整相关token的选择概率。

Logit Biasing的应用场景包括：

- **内容过滤**：如果知道不希望RAG系统生成不恰当内容，可以将某些敏感词汇的偏置降低
- **分类任务**：如果RAG系统是一个分类器，需要输出预定义类别之一，可以提升这些类别的概率以确保LLM始终从它们中选择

### 八、参数组合与推荐配置

以下是结合多种技术的API调用示例，展示了一套相当合理的通用参数组合：

- **Temperature**: 0.8（使模型在token选择上稍微保守）
- **Top P**: 0.9（避免从分布远端选择）
- **Repetition Penalty**: 1.2（轻微惩罚重复词汇）

通过实验调整每个参数，可以根据应用场景精确调优LLM的行为。

### 九、实践建议

视频建议根据具体应用场景选择合适的参数配置：

1. **代码生成或事实问答**：适合使用较低的温度和较低的top p值，以获得更准确、可预测的输出
2. **创意领域应用**：较高的温度和top p值可以给LLM更有趣、更有探索性的语调
3. **迭代优化**：在观察到LLM表现的具体问题后，再考虑引入重复惩罚、logit偏置或其他采样技术

理解LLM随机选择的多重调优方法，并通过迭代找到适合项目的设置，是获得所需性能表现的关键。

## 完整字幕原文
```
A big part of working with an LLM is understanding and controlling the randomness at the heart of how they operate. In this video, let's have a look at a typical LLM API, and explore the different options they provide to control the way your LLM chooses the next tokens. Every token a large language model adds to your completion is a weighted random choice. If you use an open source large language model, you can see how this choice was made. These models will let you see the token probabilities generated at each step, which was used to select the next token. For example, for the prompt, the sky is, this is what the probability distribution looks like. Blue has a 50% probability of coming next, bright has a 25% probability, and every other token has 10% or less, quickly shrinking to less than 1%. Here is what that distribution looks like visually. When the curve has a tall spike on the left side, you could say the model was confident in its choice, with only one or possibly a few other tokens having any real chance of being chosen. A flatter distribution like this, on the other hand, can be interpreted as uncertainty. The model has many possible directions it could take the completion next, with no clear winner. Decoding and controlling this distribution curve is a big part of how you tune your LLM's behavior. So let's look at a few strategies to do this. One simple approach is to instruct the LLM to not actually make a random choice, and just always pick the token with the highest probability. This is known as greedy decoding. Greedy decoding's main upside is that it makes the LLM deterministic. If you feed your model the same prompt, it will always generate the same response. The primary downside of greedy decoding is that it can lead to text that is, well, predictable. The pros can end up feeling generic or even stilted. Another issue with greedy decoding is that the LLM will sometimes get stuck producing the same sequence of words over and over again. The LLM doesn't actually care if the overall completion makes sense. The LLM just keeps choosing the highest likelihood next token, and once the model falls into a repetitive loop, there's no mechanism to break out of it. Despite these potential shortcomings, greedy decoding can make sense in instances where highly predictable and deterministic output is desirable, like code completion or even as a temporary setting to debug your system. In most instances, you don't want to entirely eliminate randomness. You just want to control it. The most widely used parameter to control an LLM's randomness is called temperature. You can think of temperature like a dial that changes the shape of the probability distribution generated by your LLM. A default temperature of 1 just gives you the original distribution. A lower temperature leads to a more spiky distribution, with only the most likely tokens having any chance of being generated. The ordering of the tokens doesn't change, but their probabilities of being chosen do. Setting temperature all the way down to 0 sets the model to perform greedy decoding, with only the single most probable token having a 100% probability. Turning the temperature up a bit, say in the range of 1.1 to 1.3, will flatten out the probability distribution, giving unlikely tokens a bit more chance of being chosen. This leads to more variety and sometimes more interesting or even creative sounding text. Setting the temperature too high will result in a very flat probability distribution. All tokens will have about an equal chance of being chosen, even if they don't make that much sense. Whatever temperature you set your LLM to, that distribution curve will still have a long tail running out to the right. Full of nonsense tokens, your LLM has a small likelihood of choosing. To help control this, a few additional sampling techniques are used. Top k sampling is the most simple, and limits the LLM to choosing from the top k most likely tokens. For example, you might both set a temperature of 1.1, but also limit the LLM to choosing from the top 5 most likely next tokens. A similar approach is called top p sampling, which limits the LLM to choosing tokens with cumulative probability falling below some threshold. For example, you might set a top p of 85%. You would start from the left side of this distribution, and keep adding the probabilities of each token until the total is greater than 85%. Top p tends to be the more responsive or dynamic of the two approaches. In top k, the LLM always picks from the same pool of tokens, regardless of the shape of the distribution. With top p, if the LLM is fairly certain, meaning a few tokens have a very high probability, the LLM will limit its choices to the few most likely tokens. If instead, the LLM is more uncertain, meaning the distribution is flat, with no clear best choice, the LLM is allowed to choose from a much larger pool of potential tokens. Some techniques also target the probabilities of individual words, rather than the overall shape of the distribution. For example, large language models can have a tendency to repeatedly use the same word or phrase, which can sound unnatural. Many LLMs allow you to apply a repetition penalty, which decreases the probabilities of words that have already appeared in the completion. This can make the resulting text sound more natural and varied. Most LLMs also allow you to increase or decrease the probability of specific tokens, usually called logit biasing. This bias will permanently adjust those tokens' probability of being chosen up or down. If you know you don't want your RAG system to generate profanity, you could bias certain words down. On the other hand, if your RAG system is a classifier, designed to output one of a few categories, you could boost the probabilities of those categories to ensure the LLM always chooses from between them. Here's an API call combining many of the techniques you've seen in this video. This is a fairly sensible, general-purpose combination of parameters. A temperature of 0.8, a top p of 0.9, and a repetition penalty of 1.2. This LLM will be a little more conservative in its token choice, avoids choosing from the far tail of the distribution, and lightly penalizes repeated tokens. By experimenting with each parameter, you could dial in the LLM's behavior for the context of your application. There's a wide area of techniques available to control the randomness inherent in your LLM, and this video only covered a selection of the most common ones. In general, I advise setting a temperature and top p that best fits your needs. If you're generating code or answering factual questions, a lower temperature and a lower top p make sense. If you're operating in a more creative domain, a higher temperature and top p could give your LLM a more interesting and exploratory tone. After that, consider introducing repetition penalties, logit biases, or other sampling techniques you research in response to specific issues you identify in how your LLM is performing. Ultimately, understanding that there are many ways to tune an LLM's random choices, and iterating towards the settings that fit your project will get you the performance that you need.
```

## 关键引述/重要观点

> "Every token a large language model adds to your completion is a weighted random choice." [视频开头]

> "When the curve has a tall spike on the left side, you could say the model was confident in its choice, with only one or possibly a few other tokens having any real chance of being chosen." [概率分布解读]

> "A flatter distribution like this, on the other hand, can be interpreted as uncertainty. The model has many possible directions it could take the completion next, with no clear winner." [不确定性解读]

> "Greedy decoding's main upside is that it makes the LLM deterministic. If you feed your model the same prompt, it will always generate the same response." [贪婪解码优势]

> "The LLM doesn't actually care if the overall completion makes sense. The LLM just keeps choosing the highest likelihood next token, and once the model falls into a repetitive loop, there's no mechanism to break out of it." [贪婪解码缺陷]

> "In most instances, you don't want to entirely eliminate randomness. You just want to control it." [随机性控制理念]

> "You can think of temperature like a dial that changes the shape of the probability distribution generated by your LLM." [温度参数类比]

> "Top p tends to be the more responsive or dynamic of the two approaches." [Top P优势]

> "If you're generating code or answering factual questions, a lower temperature and a lower top p make sense. If you're operating in a more creative domain, a higher temperature and top p could give your LLM a more interesting and exploratory tone." [实践建议]

> "Ultimately, understanding that there are many ways to tune an LLM's random choices, and iterating towards the settings that fit your project will get you the performance that you need." [总结]

## 相关话题/关键词
- 大语言模型 (LLM)
- Token生成
- 概率分布
- 随机性控制
- 贪婪解码 (Greedy Decoding)
- 温度参数 (Temperature)
- Top K采样
- Top P采样 (核采样)
- 重复惩罚 (Repetition Penalty)
- Logit Biasing
- RAG系统
- 开源模型
- 确定性输出
- 文本生成
- API参数调优
- 创意生成
- 代码补全
- 模型置信度

## 技术信息
- 字幕字数: 7240
- 字幕字符数: 7240
- 时间戳条目数: 0
- 处理时间: 2026-05-28 14:12:35

---

## 视频 4: Choosing your LLM
**时长**: ~8 min (493s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/vvs2mn/choosing-your-llm
**视频 ID**: 1199219

# 视频摘要：Choosing your LLM

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/vvs2mn/choosing-your-llm
- **时长**: 493秒 (约8分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:16:50

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
本视频深入探讨了在构建RAG（检索增强生成）应用时如何选择合适的大型语言模型（LLM）。内容涵盖了模型的可量化指标（如参数规模、成本、上下文窗口、推理速度等）、模型质量的评估方法（自动基准测试、人工评估、LLM作为评判者），以及如何根据具体项目需求做出明智的模型选择。视频强调LLM选择是一个重要但临时性的决策，需要随着模型能力的快速提升而不断调整。

## 核心要点
1. 模型大小是常见指标，小型模型约1-100亿参数，大型模型可达100-5000亿参数或更多，更大模型通常更强大但成本更高
2. LLM提供商通常按每百万token收费，输入和输出token价格可能不同
3. 上下文窗口决定了模型能处理的最大token数，包括prompt和completion
4. 首次生成token时间和tokens每秒速度是实时交互应用的关键指标
5. 训练截止日期表明模型训练数据的最新时间点
6. 基准测试分为三大类：自动基准测试、人工评分基准、LLM作为评判者
7. MMLU（大规模多任务语言理解）是覆盖57个学科的经典自动基准测试
8. 人类评估使用ELO算法（如国际象棋排名系统）比较不同LLM的响应质量
9. LLM Arena是最广泛引用的基准测试之一
10. LLM-as-a-judge存在家族偏见问题，需要仔细校准
11. 好的基准测试应具备相关性、区分度、可重复性、与实际性能对齐
12. 数据污染可能导致模型在基准测试中表现虚高
13. 基准测试会随时间推移而饱和，需要不断引入新的更具挑战性的评估标准
14. 模型选择是临时性决策，需要随着新模型的发布而更新

## 详细内容（保留所有原始信息）

### 一、引言：RAG应用中LLM选择的重要性

构建RAG应用时的主要决策之一是选择使用哪个LLM。市场上存在种类繁多的LLM，它们具有不同的性能水平、独特的能力和不同的成本结构。选择正确的模型对应用的速度、质量和预算都有重大影响。

### 二、可量化的LLM差异指标

#### 2.1 模型大小（Model Size）
模型大小是经常被引用的指标，通常以模型包含多少十亿参数来衡量。较小模型可能有10-100亿参数，而较大模型有100-5000亿甚至更多。更大的模型通常（但并非总是）比小型模型更有能力，但运行成本也更高。

#### 2.2 成本（Cost）
成本当然是重要因素。LLM提供商通常按每百万token的固定价格收费，有时输入和输出token的价格不同。一般来说，新型、更大、更有能力的模型价格更高。

#### 2.3 上下文窗口（Context Window）
模型的上下文窗口告诉您LLM可以处理的最大token数，分摊在prompt和completion之间。较大的限制为长prompt和completion提供更多灵活性，但您仍然按token付费。

#### 2.4 推理速度（Speed）
首次生成token的时间和速度（以tokens每秒表示）是另一个重要因素。如果您的RAG系统依赖实时交互，您可能愿意容忍其他方面的性能下降，换取快速和低延迟的模型。

#### 2.5 训练截止日期（Training Cutoff Date）
模型的训练截止日期或知识截止日期告诉您模型训练数据中代表的最新时间点。即使在RAG系统中，较晚的截止日期通常被认为是更好的，特别是在模型需要回答有关时事问题的场景中。

### 三、质量评估的难点与基准测试

虽然易于量化的指标可能有助于缩小您考虑的模型范围，但通常您最关心的是模型的质量，而这可能更难量化。这里的质量涵盖了LLM的所有能力，从解决复杂数学问题的推理能力，到简单生成可读性强的文本。

为了帮助在质量的各个维度上比较模型，有大量令人眼花缭乱的LLM基准测试可供选择，试图对LLM进行评分和比较。没有单一的权威基准测试列表可以供您参考，但了解可用的各种选项可以帮助您选择最适合项目的基准测试。

### 四、三种基准测试类型

#### 4.1 自动基准测试（Automated Benchmarks）
自动基准测试对LLM进行可由代码评估的任务评分。这种基准测试的经典格式可能是对特定兴趣领域的多项选择测试，或一系列数学或编程挑战，其中LLM的响应可以很容易地由计算机验证。好的例子是MMLU（大规模多任务语言理解），它使用多项选择测试覆盖从STEM到人文到法律的57个科目。其他基准测试测试LLM在数学问题到常识推理问题等各个方面的表现。您经常看到LLM提供商在其模型的市场宣传中使用这些基准测试的性能数据，并且很可能找到与您项目相关的基准测试。

#### 4.2 人类评分基准（Human-Evaluated Benchmarks）
人类评估的基准测试通常是这样工作的：让两个匿名的LLM对同一个prompt做出响应，然后让人类评估者选择他们更喜欢哪个响应。这些结果被输入到用于排名国际象棋选手的相同ELO算法中，从而产生LLM的比较排行榜。这种评级系统的流行主办方叫做LLM Arena，其排名是最广泛引用的LLM基准测试之一。这些人类评分排名捕捉了自动基准测试难以轻易衡量的微妙质量因素。虽然自动和人类评分指标通常会一致，但当它们的分数出现分歧时，可以突出模型性能的重要细微差别。

#### 4.3 LLM作为评判者（LLM as a Judge）
LLM作为评判者的基准测试使用一个LLM来评价另一个LLM对一组测试问题的响应。评判LLM可以访问一组参考答案，本质上只是判断被评估的LLM提供正确答案的频率。这给了您一个可以用来比较一个LLM与另一个LLM的胜率。LLM-as-a-judge的主要优点是它是评估LLM的一种相对便宜和灵活的方式。这种方法的一个缺点是评判者需要仔细校准，因为他们倾向于偏好自己同系列的语言模型的答案。例如，来自OpenAI的GPT模型会偏好其他GPT模型。来自Google的Gemini模型会偏好其他Gemini模型。通过重新校准这些现成的模型，可以减少这种偏见。

### 五、好的基准测试应具备的特点

好的基准测试有几个特点。首先，它们与您的项目相关。如果您的应用程序永远不会生成代码，那么在代码生成基准测试上比较LLM并没有太大帮助。其次，基准测试需要有难度才能很好地区分高性能和低性能的模型。如果每个模型在基准测试上都表现良好，那它就没什么用处。基准测试应该是可重复的，这意味着分数本身在测试运行之间不会发生剧烈变化，模型提供商引用的结果应该是可验证的。基准测试也应该与真实世界性能保持一致。在编程基准测试上表现良好的LLM应该在实践中实际写出好的代码。在这里，您可能需要阅读一些开发者论坛，以确保基准测试分数是实际性能的良好指标。产生这个问题的原因之一是数据污染。大型语言模型是在从互联网抓取的数十亿甚至数万亿token上训练的。基准测试使用的数据集可能包含在训练数据中。在这种情况下，语言模型可能会因为在训练期间已经看到完全相同的问题和答案而在该基准测试上表现过好。

### 六、基准测试的饱和与进化

虽然基准测试可以帮助您区分模型，但它们也突出了整个领域的发展速度。以下是您会在大多数LLM评估中看到的重复模式。首先，每个模型的平均分数相当低。然后，在短短几年内，模型达到人类专家水平变得司空见惯。这些基准测试被称为饱和，意味着它们不再帮助区分模型，因为几乎所有高级模型都接近最高分。在这种情况下，需要引入新的更具挑战性的基准测试来有意义地衡量性能的提升。然而，这些新的评估本身很快就会饱和，需要引入更新的评估。

### 七、结论与建议

主要结论是，今天发布的模型通常比仅仅一两年前的模型明显更好，而且您今天选择的任何模型可能都需要被更强大的模型快速替换。选择正确的LLM是设计RAG系统的一个重要但临时性的决策。易于量化的因素如成本或延迟可以帮助缩小您的选择范围，各种质量指标可以指向与您的用例最佳对齐的最佳模型。由于模型改进的速度，您应该计划最终更换新发布的适合您RAG系统的模型。

## 完整字幕原文
```
A major decision when building a RAG application is which LLM you'll use. There's a huge variety of LLMs available, with different levels of performance, unique capabilities, and different cost profiles. Choosing the right one can have a big impact on your application's speed, quality, and budget. So let's have a look at how you can make the choice that best fits your project. Let's start with some easily quantifiable differences between LLMs. Model size is a frequently quoted metric, usually measured by how many billions of parameters the model has. Small models may have between 1 and 10 billion parameters, while larger models have 100 to 500 billion, and possibly more. Larger models are typically, but not always, more capable than their smaller counterparts, but they're always more expensive to run. Cost is of course an important factor. LLM providers typically charge you for a fixed price per million tokens, sometimes with different prices for input and output tokens. You can generally expect newer, larger, and more capable models to cost more. The context window of a model tells you the maximum number of tokens an LLM can process, split between both the prompt and the completion. While large limits offer more flexibility to have long prompts and completions, you still pay per token. The time to first token, and speed, as expressed in tokens per second, is another important factor. If your RAG system depends on real-time interactions, you might be willing to tolerate worse performance in other areas for a fast and low-latency model. The training cutoff date, or knowledge cutoff date, of a model tells you the last point in time represented in a model's training data. Even in a RAG system, a later cutoff is typically considered preferable, especially in contexts where a model will need to respond to questions on recent events. While easily quantifiable metrics might help narrow down which models you consider, usually you care most about the quality of a model, which can be a lot harder to quantify. Quality here means everything from an LLM's ability to reason through complex math problems, to simply producing text that's pleasant to read. To help compare models across all these different dimensions of quality, there is a dizzying array of LLM benchmarks available that try to score and compare LLMs. There's no single authoritative list of benchmarks that you can turn to, but understanding the variety of options available can help you choose the benchmark that makes the most sense for your project. Benchmarks come in three high-level varieties, automated benchmarks, human scoring, and LLM as a judge. Automated benchmarks score LLMs on tasks that can be assessed with code. A classic format for this kind of benchmark might be a multiple choice test on a particular field of interest, or a series of mathematical or coding challenges where the LLM's responses can be easily validated by a computer. A good example benchmark here is MMLU, or Massive Multitask Language Understanding, which covers 57 subjects ranging from STEM to humanities to law using multiple choice tests. Other benchmarks test LLMs on everything from math problems to common sense reasoning questions. You'll frequently see LLM providers market their model's performance on these benchmarks, and can likely find the one that is relevant to your project. Human-evaluated benchmarks typically work by having two anonymous LLMs respond to the same prompt and asking human evaluators to choose which response they prefer. These results are fed to the same ELO algorithm used to rank chess players, resulting in a comparative leaderboard of LLMs. A popular host of this type of rating system is called LLM Arena, whose rankings are one of the most widely cited LLM benchmarks. These human-graded rankings capture nuanced quality factors that automated benchmarks can't easily measure. While automated and human-graded metrics will often agree, when their scores diverge, it can highlight important nuances in model performance. LLM-as-a-judge benchmarks use one LLM to rate another LLM's responses to a collection of test questions. The judge LLM has access to a set of reference answers, and essentially just determines how often the LLM being evaluated provides an answer that is close to the correct one. This gives you a win rate that can be used to compare one LLM versus another. LLM-as-a-judge's primary upside is that it's a relatively cheap and flexible way to evaluate LLMs. One downside of this approach is that the judge needs to be carefully calibrated because they have a tendency to prefer answers from their own family of language models. For example, GPT models from OpenAI will prefer other GPT models. Gemini models from Google will prefer other Gemini models. By recalibrating these off-the-shelf models, it's possible to diminish this bias. Good benchmarks have a few qualities. First, they're relevant to your project. If your application won't ever generate code, comparing LLMs on a code generation benchmark isn't much help. Next, benchmarks need to be difficult to do a good job differentiating between high and low performing models. If every model scores well on a benchmark, it's just not that useful. Benchmarks should be reproducible, meaning the scores themselves don't change drastically between testing runs, and the outcomes quoted by the model providers should be verifiable. Benchmarks should also align with real-world performance. An LLM that does well on a programming benchmark should actually write good code in practice. Here, you may need to do some reading on developer forums to ensure benchmark scores are a good indication of actual performance. A reason this problem can arise is data contamination. Large language models are trained on billions, if not trillions of tokens scraped from the internet. It's possible that the data set used by the benchmark are included in that training data. In this case, the language model might overperform on that benchmark because it's already seen the exact questions and answers during its training. While benchmarks can help you differentiate between models, they also just highlight how rapidly the field as a whole is evolving. Here's the general pattern you'll see repeated for most LLM evals. At first, the average score for each is quite low. Then, over only a few years, it becomes commonplace for models to perform on par with human experts. These benchmarks are called saturated, meaning they no longer help differentiate between models, as almost all advanced models score near the maximum. At that point, new and more challenging benchmarks need to be introduced to meaningfully measure improvements in performance. Those new evals will quickly become saturated themselves, however, and even newer ones will need to be introduced. The main takeaway here is that models released today are usually significantly better than models from even a couple of years ago, and that any model you choose today likely will need to be replaced as more capable models are rapidly introduced. Choosing the right LLM is an important but temporary decision for how you design your RAC system. Easily quantifiable factors like cost or latency can help narrow down your choice, and a wide variety of quality metrics can point you towards the best models to align with your use case. Thanks to the speed at which models are improving, you should plan on eventually swapping in newly released models that suit your RAC system.
```

## 关键引述/重要观点

> "A major decision when building a RAG application is which LLM you'll use. There's a huge variety of LLMs available, with different levels of performance, unique capabilities, and different cost profiles." 

> "Larger models are typically, but not always, more capable than their smaller counterparts, but they're always more expensive to run."

> "You can generally expect newer, larger, and more capable models to cost more."

> "If your RAG system depends on real-time interactions, you might be willing to tolerate worse performance in other areas for a fast and low-latency model."

> "Even in a RAG system, a later cutoff is typically considered preferable, especially in contexts where a model will need to respond to questions on recent events."

> "Quality here means everything from an LLM's ability to reason through complex math problems, to simply producing text that's pleasant to read."

> "The judge needs to be carefully calibrated because they have a tendency to prefer answers from their own family of language models. For example, GPT models from OpenAI will prefer other GPT models. Gemini models from Google will prefer other Gemini models."

> "Benchmarks should also align with real-world performance. An LLM that does well on a programming benchmark should actually write good code in practice."

> "Large language models are trained on billions, if not trillions of tokens scraped from the internet. It's possible that the data set used by the benchmark are included in that training data."

> "These benchmarks are called saturated, meaning they no longer help differentiate between models, as almost all advanced models score near the maximum."

> "The main takeaway here is that models released today are usually significantly better than models from even a couple of years ago, and that any model you choose today likely will need to be replaced as more capable models are rapidly introduced."

> "Choosing the right LLM is an important but temporary decision for how you design your RAC system."

## 相关话题/关键词

- RAG (检索增强生成)
- LLM选择
- 模型大小 (Model Size)
- 参数数量 (Parameters)
- 成本 (Cost)
- 每百万token价格 (Price per million tokens)
- 上下文窗口 (Context Window)
- 推理速度 (Inference Speed)
- 首次生成token时间 (Time to First Token)
- 训练截止日期 (Training Cutoff Date)
- 知识截止日期 (Knowledge Cutoff Date)
- 模型质量评估 (Model Quality Evaluation)
- 基准测试 (Benchmarks)
- MMLU (大规模多任务语言理解)
- 自动基准测试 (Automated Benchmarks)
- 人类评估基准 (Human-Evaluated Benchmarks)
- ELO算法 (ELO Algorithm)
- LLM Arena
- LLM-as-a-judge
- 数据污染 (Data Contamination)
- 基准测试饱和 (Benchmark Saturation)
- 实时交互 (Real-time Interactions)
- 低延迟 (Low-latency)
- 家族偏见 (Family Bias)
- 可重复性 (Reproducibility)
- 真实世界性能 (Real-world Performance)

## 技术信息
- 字幕字数: 7515
- 字幕字符数: 7515
- 时间戳条目数: 0
- 处理时间: 2026-05-28 14:16:50

---

## 视频 5: Prompt engineering: building your augmented prompt
**时长**: ~5 min (344s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/77dr2c/prompt-engineering%3A-building-your-augmented-prompt
**视频 ID**: 1199220

# 视频摘要：Prompt engineering: building your augmented prompt

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/77dr2c/prompt-engineering%3A-building-your-augmented-prompt
- **时长**: 344秒 (约5分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:17:33

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
本视频介绍了Prompt Engineering（提示工程）的基本概念及其在RAG（检索增强生成）系统中的应用。课程首先讲解了如何使用OpenAI的messages格式构建提示，包括system、user、assistant三种角色的作用，以及多轮对话的实现机制。随后重点介绍了系统提示的设计原则和最佳实践，包括高阶指令、模型行为控制、响应风格设定等。最后演示了如何构建增强提示模板，将系统提示、检索上下文、历史对话和用户提示有机组合，以提升RAG系统的整体性能。

## 核心要点

### 一、提示工程概述
1. Prompt Engineering是一个涵盖多种提示技术的统称，能够带来更高质量的输出结果
2. 编写高质量提示是充分发挥大语言模型能力的关键
3. 提示工程技术可用于改善RAG系统的整体性能

### 二、OpenAI Messages格式
4. Messages格式是构建提示的最常见格式，采用简单的JSON结构
5. 每条消息包含content（消息文本内容）和role（角色）两个字段
6. 角色分为三种：system（系统）、user（用户）、assistant（助手）
7. System消息提供高级指令，影响LLM的总体行为
8. User消息记录用户已发送的提示
9. Assistant消息记录LLM先前生成的回复

### 三、多轮对话机制
10. 多轮对话并非LLM真正记住之前的内容，而是将整个对话转换为messages格式
11. 新的用户消息追加在对话末尾
12. 每次新用户提示时，整个对话历史都提交给LLM
13. JSON消息对象转换为单一的文本字符串供LLM处理
14. Chat template使用特殊文本标签（如箭头或竖线）标识消息的起始和结束
15. LLMs经过训练，能够识别这些标签并区分不同角色的消息

### 四、系统提示设计
16. 系统提示是RAG系统提示构建的首要步骤，提供高级行为指导
17. 系统提示可以很长，甚至达到多页篇幅
18. 可包含知识截止日期和当前日期信息，帮助LLM判断信息时效性
19. 可指导LLM按步骤推理答案、使用Markdown响应
20. 可赋予LLM特定人格特质，如知识好奇心、乐于讨论等
21. RAG应用中可指示LLM仅使用检索文档回答问题、判断文档相关性、引用来源

### 五、增强提示模板构建
22. 提示模板定义了提示的高级结构，决定内容注入位置
23. 模板通常以系统提示开始
24. 多轮对话支持时，可包含用户与LLM之间的历史消息
25. 添加检索器返回的前5或前10个文本块及处理说明
26. 最后包含最新用户提示
27. 模板化设计便于实验不同提示结构，修改单个组件观察效果

### 六、RAG系统中的典型提示构建
28. 典型RAG提示结合：精心编写的系统提示、检索上下文、历史对话详情、最新用户提示

## 详细内容（保留所有原始信息）

### 1. 提示工程简介与重要性

Prompt Engineering（提示工程）是一个涵盖多种提示技术的统称，这些技术倾向于产生更高质量的结果。为了从大语言模型（LLM）中获得最大收益，用户需要编写高质量的提示。本视频探讨了几种提示工程技术，以及如何利用它们来改善RAG（检索增强生成）系统的整体性能。

### 2. OpenAI Messages格式详解

构建提示最常见的格式是OpenAI的messages格式，该格式将提示结构化为一系列消息，使用简单的JSON结构。一条消息包含两个主要组成部分：

**Content字段**：消息的文本内容本身

**Role字段**：消息的角色身份，分为三种类型：

- **System（系统）**：系统消息提供给LLM，用于影响其整体行为，通常包含高级指令
- **User（用户）**：用户消息记录系统用户已发送的提示
- **Assistant（助手）**：助手消息记录先前由LLM生成的回复

这种格式非常灵活，允许向提示添加各种上下文信息，以帮助控制LLM的响应方式。

### 3. 多轮对话的工作原理

当用户与LLM进行长时间的来回对话（称为多轮对话）时，LLM实际上并非真正记住之前说过的话。幕后机制是将整个对话转换为messages格式，新用户消息出现在末尾。每次新的用户提示时，整个对话都提交给LLM处理。

JSON消息对象被转换为单一的文本字符串供LLM处理。这个chat template字符串使用特殊的文本标签（如箭头或竖线）来标识每条消息的开始和结束。LLMs经过训练能够识别这些标签并理解system、user和assistant消息之间的区别。

### 4. 系统提示的设计原则

构建RAG系统提示时，首先要做的事情是编写系统提示。系统提示为LLM提供关于其应该如何行为的高级指令。如果希望LLM始终以特定语气说话或遵循某些程序，这些信息应该放在系统提示中。

以一个流行的LLM聊天机器人的系统提示为例，可以获得关于系统提示内容的启发：

**长度特征**：首先引人注目的是其篇幅很长——这是一个很大的提示！虽然用户可能并不总是需要编写多页的系统提示，但了解可以这样做的灵活性是很好的提醒。

**知识截止与日期信息**：提示早期包含模型训练数据的知识截止信息以及当前日期。这类信息帮助LLM判断其信息的过时程度，以及是否适合回答某些问题。

**响应流程与语气指导**：后面的部分指导LLM关于响应时应使用的流程和语气。例如：
- 要求模型按步骤推理答案
- 不帮助潜在有害请求
- 使用Markdown格式响应

**人格特质设定**：LLM还被告知它具有知识好奇心，喜欢听人类对问题的看法，并乐于参与各种话题的讨论。这赋予了LLM特定的人格特质。

### 5. RAG应用中的系统提示定制

用户可以使用相同的原则来构建自己的系统提示。例如：

- 可以指示LLM详细回答或简洁回答问题
- 在RAG应用中，可以告诉语言模型：
  - 仅使用检索到的文档回答提示
  - 判断文档是否相关
  - 在回复中引用来源

系统提示通常添加到LLM处理的每个提示中，因此花时间优化它们是改善RAG系统最终生成结果的风格和质量的好方法。

### 6. 增强提示模板的构建

此时，用户已准备好构建增强提示（augmented prompt）。由于这个提示可能包含多条信息，因此建立一个深思熟虑的提示模板非常有帮助。模板设定了提示的高级结构，并帮助决定某些内容将注入到哪个位置。

典型的提示模板结构如下：

1. **系统提示**：首先从提供高级指导的高级系统提示开始，告知系统应如何行为
2. **历史对话**：如果系统支持多轮对话，可以包含用户与LLM之间发送的先前消息
3. **检索上下文**：接下来添加检索器返回的前5或前10个文本块，以及关于如何处理它们的信息
4. **最新用户提示**：最后包含LLM应该响应的最新用户提示

使用这样的模板的好处是，它使实验不同的提示结构变得容易。用户可以修改整体提示的各个组件，并观察这对最终生成的响应的影响。

### 7. RAG系统中的典型提示构建实践

这就是在RAG系统中构建典型提示的样子，结合了：
- 精心编写的系统提示
- 检索到的上下文
- 历史对话详情
- 当然，还有最新的用户提示

## 完整字幕原文

```
In order to get the most out of your large language model, you'll need to write a high quality prompt. Prompt engineering is an umbrella term for a variety of prompting techniques that tend to lead to higher quality results. Let's explore a few prompt engineering techniques and talk about how they can be used to improve the overall performance of your RAG system. To start, it's helpful to understand how you'll actually build out prompts in code. The most common format is OpenAI's messages format, which structures prompts as a series of messages using a simple JSON structure. A single message will have content, which is just the text of the message, as well as a role, which will either be system, user, or assistant. System messages are provided to the LLM to influence its overall behavior and usually include high-level instructions. User messages record prompts that a user of the system has already sent. Assistant messages record responses previously generated by the LLM. When you have an extended back-and-forth conversation with an LLM, also called a multi-turn conversation, it's not actually remembering what you said earlier. Instead, behind the scenes, the entire conversation is converted into this messages format, with your new user message appearing at the end. And then, the entire conversation is submitted to the LLM with every new user prompt. The JSON messages object is then turned into a single text string that can be processed by the LLM. This chat template string uses special text tags, like arrows or vertical bars, to indicate the start and end of each message. LLMs are trained to recognize these tags and understand the difference between system, user, and assistant messages. This format is very flexible and allows you to add a wide variety of context to your prompts to help control how your LLM responds. Let's look at a few ways you can use it. The first thing you'll want to do when constructing a prompt for your RAG system is write your system prompt. This provides your LLM high-level instructions on how it should behave. If you always want your LLM to speak in a particular tone or follow certain procedures, a system prompt is where that information should go. To get some ideas of what can go into a system prompt, have a look at this system prompt from a popular LLM chatbot. The first thing that jumps out at you is the length. It's huge! You might not always need to write multiple page system prompts, but knowing you have the flexibility to do so is a good reminder. Early in the prompt, there is information on the knowledge cutoff of the model's training data, as well as the current date. Information like this helps the LLM determine how out-of-date its information is and whether it's in a good position to answer certain questions. Later sections direct the LLM on the process and tone it should use to respond to the prompt. For example, it asks the model to reason through answers step-by-step, not help with potentially harmful requests, and respond in markdown. The LLM is also told that it is intellectually curious and enjoys hearing what humans think on an issue and engaging in discussion on a wide variety of topics, which gives the LLM a particular personality, so to speak. You could use these same principles to construct your own system prompt. For example, you could instruct your LLM to respond in great detail or answer questions succinctly. Given you're constructing a system prompt for a RAG application, you could tell the language model to use only the retrieved documents to answer prompts, or judge whether a document is relevant, or cite sources in its response. System prompts are usually added to every prompt your LLM will process, so spending time refining them is a great way to improve the style and quality of the results your RAG system ultimately generates. At this point, you're ready to build your augmented prompt. This prompt potentially includes many pieces of information, so it's helpful to build a well-considered prompt template. A template sets out the high-level structure of your prompt and helps decide where certain pieces of content will be injected. For example, you might always start with a high-level system prompt that provides high-level guidance to the system about how it should behave. If your system supports multi-turn conversations, you can include previous messages sent between the user and the LLM. Next, you might add the top 5 or top 10 chunks retrieved by your retriever, as well as any information about how to process them. Finally, you can include the most recent user prompt the LLM should respond to. Here's what a prompt constructed from this template could look like. The nice thing about using a template like this is that it makes it easy to experiment with different prompt structures. You can modify individual components of the overall prompt and see how that impacts the final generated response. This is what it looks like to construct a typical prompt in a RAG system, combining a well-written system prompt, retrieved context, previous conversation details, and of course, the most recent user prompt. Join me in the next video and let's look at some advanced techniques to further improve how the LLM performs.
```

## 关键引述/重要观点

> "In order to get the most out of your large language model, you'll need to write a high quality prompt. Prompt engineering is an umbrella term for a variety of prompting techniques that tend to lead to higher quality results."

"为了从大语言模型中获得最大收益，你需要编写高质量的提示。提示工程是一个涵盖多种提示技术的统称，这些技术倾向于产生更高质量的结果。" [无时间戳]

> "The most common format is OpenAI's messages format, which structures prompts as a series of messages using a simple JSON structure. A single message will have content, which is just the text of the message, as well as a role, which will either be system, user, or assistant."

"最常见的格式是OpenAI的messages格式，该格式将提示结构化为一系列消息，使用简单的JSON结构。一条消息包含content，即消息的文本内容，以及role，即角色，可以是system、user或assistant之一。" [无时间戳]

> "When you have an extended back-and-forth conversation with an LLM, also called a multi-turn conversation, it's not actually remembering what you said earlier. Instead, behind the scenes, the entire conversation is converted into this messages format, with your new user message appearing at the end."

"当您与LLM进行长时间的来回对话（也称为多轮对话）时，它实际上并非真正记住您之前说过的话。相反，在幕后，整个对话被转换为这种messages格式，您的新用户消息出现在末尾。" [无时间戳]

> "LLMs are trained to recognize these tags and understand the difference between system, user, and assistant messages."

"LLMs经过训练能够识别这些标签，并理解system、user和assistant消息之间的区别。" [无时间戳]

> "This format is very flexible and allows you to add a wide variety of context to your prompts to help control how your LLM responds."

"这种格式非常灵活，允许您向提示中添加各种各样的上下文，以帮助控制LLM的响应方式。" [无时间戳]

> "The first thing you'll want to do when constructing a prompt for your RAG system is write your system prompt. This provides your LLM high-level instructions on how it should behave."

"构建RAG系统提示时，您首先要做的是编写系统提示。这为您的LLM提供关于其应该如何行为的高级指令。" [无时间戳]

> "Information like this helps the LLM determine how out-of-date its information is and whether it's in a good position to answer certain questions."

"此类信息帮助LLM判断其信息的过时程度，以及是否处于回答某些问题的良好位置。" [无时间戳]

> "For example, it asks the model to reason through answers step-by-step, not help with potentially harmful requests, and respond in markdown."

"例如，它要求模型按步骤推理答案，不帮助潜在有害请求，并使用Markdown格式响应。" [无时间戳]

> "The LLM is also told that it is intellectually curious and enjoys hearing what humans think on an issue and engaging in discussion on a wide variety of topics, which gives the LLM a particular personality, so to speak."

"LLM还被告知它具有知识好奇心，喜欢听人类对问题的看法，并乐于参与各种话题的讨论，可以说这赋予了LLM特定的人格特质。" [无时间戳]

> "Given you're constructing a system prompt for a RAG application, you could tell the language model to use only the retrieved documents to answer prompts, or judge whether a document is relevant, or cite sources in its response."

"鉴于您正在为RAG应用程序构建系统提示，您可以告诉语言模型仅使用检索到的文档回答提示，或判断文档是否相关，或在其回复中引用来源。" [无时间戳]

> "System prompts are usually added to every prompt your LLM will process, so spending time refining them is a great way to improve the style and quality of the results your RAG system ultimately generates."

"系统提示通常添加到LLM处理的每个提示中，因此花时间优化它们是改善RAG系统最终生成结果的风格和质量的好方法。" [无时间戳]

> "A template sets out the high-level structure of your prompt and helps decide where certain pieces of content will be injected."

"模板设定了提示的高级结构，并帮助决定某些内容将注入到哪个位置。" [无时间戳]

> "The nice thing about using a template like this is that it makes it easy to experiment with different prompt structures."

"使用这样的模板的好处是，它使实验不同的提示结构变得容易。" [无时间戳]

> "Join me in the next video and let's look at some advanced techniques to further improve how the LLM performs."

"加入我下一期视频，让我们看看一些先进的技术来进一步改善LLM的性能。" [无时间戳]

## 相关话题/关键词

- **Prompt Engineering（提示工程）**：涵盖多种提示技术的统称，用于获得更高质量的LLM输出
- **RAG（检索增强生成）**：Retrieval Augmented Generation，结合检索与生成的AI系统架构
- **Messages Format（消息格式）**：OpenAI的JSON结构化提示格式
- **System Prompt（系统提示）**：为LLM提供高级行为指令的提示组件
- **User Message（用户消息）**：记录用户输入的消息类型
- **Assistant Message（助手消息）**：记录LLM历史回复的消息类型
- **Multi-turn Conversation（多轮对话）**：用户与LLM的长时间来回交互
- **Chat Template（聊天模板）**：用于组织消息结构的文本模板
- **Augmented Prompt（增强提示）**：包含多种上下文信息的完整提示
- **Prompt Template（提示模板）**：定义提示结构和内容注入位置的框架
- **Knowledge Cutoff（知识截止）**：模型训练数据的截止日期
- **Retrieval（检索）**：从外部源获取相关文档的过程
- **Context（上下文）**：为LLM提供额外信息

---

## 视频 6: Prompt engineering: advanced techniques
**时长**: ~8 min (491s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/jjf7di/prompt-engineering%3A-advanced-techniques
**视频 ID**: 1199221

# 视频摘要：Prompt engineering: advanced techniques

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/jjf7di/prompt-engineering%3A-advanced-techniques
- **时长**: 491秒 (约8分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:17:55

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
本视频介绍了RAG系统中高级提示工程技术的应用，包括上下文学习、少样本学习、思维链提示等核心概念，并深入探讨了推理模型的特点、使用场景以及上下文窗口管理策略。视频强调这些高级技术应根据实际需求选择性使用，简单有效的提示模板可能就已足够。

## 核心要点
1. **上下文学习（In-context Learning）**：通过在提示中添加示例来帮助LLM学习期望的输出格式和语气
2. **少样本学习（Few-shot Learning）**：包含多个示例的上下文学习方法
3. **单样本学习（One-shot Learning）**：仅包含一个示例的上下文学习方法
4. **硬编码示例**：将示例直接写入提示模板，适用于需要稳定LLM行为的场景
5. **动态检索示例**：使用RAG从知识库中检索相关示例，灵活适应不同问题
6. **思维链提示（Chain-of-Thought Prompting）**：引导LLM逐步推理，而非直接给出答案
7. **草稿纸技术（Scratchpad）**：为语言模型提供"思考空间"，组织思维后再回答
8. **推理模型（Reasoning Models）**：专门为复杂推理任务设计的LLM，内置分步推理能力
9. **推理令牌 vs 响应令牌**：推理模型先生成推理令牌（内部思考），再输出响应令牌
10. **推理模型特性**：擅长处理编码、数学、规划、谜题和复杂多步骤工作流
11. **推理模型成本**：比普通模型更慢、更贵，但准确性更高
12. **推理模型的提示技巧**：无需要求其"分步思考"，可能不适合上下文学习
13. **上下文窗口管理**：单轮对话验证技术有效性，多轮对话需上下文修剪
14. **上下文修剪策略**：固定保留最近消息、使用LLM摘要旧消息、丢弃推理令牌
15. **渐进式应用原则**：简单提示模板可能已足够，高级技术应在明确需要时才添加

## 详细内容（保留所有原始信息）

### 一、上下文学习（In-context Learning）

上下文学习是一种通过在提示中添加示例来引导LLM生成期望输出的技术。例如，构建客服聊天机器人时，提示中可以包含历史客户请求示例以及高质量回复示例。这些示例帮助LLM学习生成新响应时应使用的结构和语气。

**学习类型区分**：
- **少样本学习（Few-shot Learning）**：包含多个示例的上下文学习方法
- **单样本学习（One-shot Learning）**：仅包含一个示例的上下文学习方法

**实现方式**：

1. **硬编码示例**：将一个或多个示例问答直接写入提示模板。这种方法在需要稳定LLM行为的场景下可以帮助提高响应质量。

2. **动态检索示例**：如果想要每次更换示例，可以使用RAG从知识库中检索相关示例问答。例如，可以将成功的客户对话索引到向量数据库中，当新客户就某个主题进行咨询时，可以检索关于该主题的历史对话文本，并将其注入到提示中。这本质上就是普通RAG，但专门检索示例响应可以进一步提高LLM的响应质量。

### 二、思维链提示与推理技术

另一类强大的提示工程技术是鼓励LLM以逐步方式处理提示并推理。例如，可以告诉LLM先"出声思考"或"逐步思考"最佳方法，然后再提供最终答案。这种方法的核心理念是为语言模型提供一个"草稿纸"来组织其回答前的思路。

**常见实现方式**：

1. **草稿纸技术（Scratchpad）**：一种常见做法是告诉LLM，介于草稿纸标签之间的token被视为思考和头脑风暴的空间，不属于其最终答案的一部分。

2. **思维链提示（Chain-of-Thought Prompting）**：在这种方式中，LLM被指示以逐步方式处理问题，而不是立即回答。LLM可能先被指示生成回答问题所需的步骤，然后按照这些步骤执行。这种增量式规划和采取方法可以提高最终响应的准确性。由于LLM会展示其"工作过程"，当LLM推理出现偏差时也更容易追踪问题。

### 三、推理模型（Reasoning Models）

这类推理导向策略取得了巨大成功，以至于许多LLM现在从一开始就设计为推理模型。推理模型在复杂推理任务中表现出色，如编码、数学、规划、谜题以及需要多个步骤的复杂工作流。

**工作原理**：
- 推理模型首先生成推理令牌，在其中进行提前规划和选项考虑，类似于前面提到的草稿纸
- 然后输出带有用户预期最终响应的响应令牌

**访问权限差异**：
- 一些推理模型提供商只提供对这些最终响应令牌的访问
- 其他提供商则允许访问推理令牌

**成本与性能**：
- 推理令牌仍然是常规token，具有生成它们的所有相关成本
- 因此推理模型通常运行更慢、成本更高
- 但推理模型通常比非推理对应模型更准确

**在RAG系统中的应用**：
- 根据具体场景，围绕推理模型构建RAG系统可能非常值得
- 推理模型特别擅长评估检索文档的相关性
- 更擅长决定如何将信息整合到响应中，特别是需要更复杂推理步骤的响应

**推理模型的提示特点**：
- 不需要要求它们分步思考，因为这是它们已经训练好的能力
- 可能不适合使用上下文学习，因为它们会将提供的示例响应融入当前正在回答的问题中
- 对于具体的、期望它们努力实现的目标，以及关于期望回答格式的非常具体的信息，表现更好
- 仍可以提供高级指导原则，明确说明希望模型采取或避免的方法
- 然后可以直接提供从RAG系统检索的整个文档上下文
- 新模型（包括推理模型）不断发布，大多数LLM提供商会包含如何最佳提示它们的信息

### 四、上下文窗口管理

随着使用更多提示工程技术，上下文窗口管理变得至关重要。初始提示和LLM为完成而生成的任何token都会占用其上下文窗口的部分。

**增加上下文负担的因素**：
- 从检索器注入文档
- 在每个提示中添加上下文学习示例
- 让推理模型在回答前规划其响应

所有这些高级技术都会增加提示长度、生成响应长度，或两者同时增加。如果不注意，上下文窗口很容易快速被填满。

**单轮对话策略**：
- 最佳做法是验证是否从提示工程技术中获得价值
- 如果思维链提示或上下文学习没有带来更好的性能，最好将其从系统中移除

**多轮对话策略**：
- 多轮对话会快速消耗上下文窗口，因为每次来回消息都需要包含在提示中
- 一系列被称为"上下文修剪"的策略可以解决此问题

**具体修剪方法**：

1. **固定消息数量**：简单解决方案是只保留提示中固定数量的最近消息，例如用户和LLM发送的最后五条。

2. **LLM摘要**：更复杂的方法是使用单独的LLM来总结旧消息，缩小其大小但保留关键要点。

3. **丢弃推理令牌**：如果在多轮对话中使用推理模型，几乎肯定希望从聊天历史中丢弃推理令牌，只保留响应令牌。

4. **仅包含相关检索块**：在RAG系统中，通常只想包含支持回答最新问题的检索块，而不是之前每个问题的检索块。

**长上下文窗口模型**：
- 如果应用程序需要具有深度和丰富上下文的多轮对话，可以切换到使用具有更长上下文窗口的模型
- 但仍需谨慎设计提示，因为即使在具有更长上下文窗口的模型上，长提示运行起来也很慢且成本高昂

### 五、技术应用建议

提示工程技术可以提高LLM的性能，但RAG系统不一定需要使用它们。简单的提示模板和编写良好的系统提示可能就是项目所需的全部。

**建议原则**：
- 当涉及更高级技术时，建议只有在明确需要时才将它们添加到项目中
- 提示工程总体上更像是一门艺术而非科学
- 无论使用什么策略，都应该尝试不同的提示并找到最适合系统的那些

## 完整字幕原文
```
Once you have a basic prompt template set up for your RAG system, you can start trying more advanced prompt engineering techniques. Let's have a look at a few of those and when you'd want to use them. In-context learning is a technique which allows you to help the LLM learn what kind of output you wanted to generate by adding examples of them to the prompt. For example, if you're building a customer service chatbot, your prompt can include examples of previous customer requests, as well as high quality responses to those requests. These examples help the LLM learn the structure and tone it should use when it generates new responses. Just like in RAG, you're adding additional information to the prompt to ground the way the LLM responds. If you include many examples, this approach is called few-shot learning. If you include just one example, it's called one-shot learning. There's a few ways to implement in-context learning. You could just hard code one or more example questions and responses into your prompt. In situations where you want a stable set of LLM behaviors, this alone could help improve response quality. If you want to change up the examples each time, however, you can use RAG to retrieve example questions and responses from your knowledge base. For example, if you're working on that same customer service chatbot, you could index successful customer chats into your vector database. When a new customer writes in about a particular topic, you can retrieve the text of previous conversations about that topic and inject that text into your prompt. In many ways, this is just normal RAG, but the fact that you're specifically retrieving example responses can help further improve the quality of the LLM's response. Another powerful collection of prompt engineering techniques essentially encourages the LLM to reason through prompts in a step-by-step manner. For example, you can tell the LLM to first think aloud or think step-by-step about the best way to approach the problem before actually providing a final answer. The idea is you're essentially giving the language model a scratchpad to organize its thoughts before answering. A common way to do this is to tell the LLM that tokens between scratchpad tags are considered a space for thinking and brainstorming and not part of its final answer. A similar approach is called chain-of-thought prompting. In this approach, the LLM is instructed to tackle questions in a step-by-step manner rather than immediately answering them. The LLM might be instructed to first generate the steps needed to answer a question and then follow those steps. Encouraging the LLM to plan and take this incremental approach can increase the likelihood that the final responses are more accurate. Since the LLM will show its work, so to speak, it's also easier to trace down issues when the LLM's reasoning falls apart. Reasoning-oriented strategies like these have been so successful that many LLMs are now designed to be reasoning models right out of the box. Reasoning models excel at complex reasoning tasks such as coding, mathematics, planning, puzzles, and complex workflows that require multiple steps. Under the hood, these reasoning models first generate reasoning tokens where they might plan ahead and consider options much like the scratch pad you saw before. Then they output response tokens with the intended final response to the user. Some providers of reasoning models will only provide access to those final response tokens. Others allow you to access the reasoning tokens as well. These reasoning tokens are part of what makes these models more accurate than their non-reasoning counterparts, but they're still just regular tokens with all the associated costs of generating them. As a result, reasoning models are typically slower and more expensive to run. Depending on your context, building a RAG system around a reasoning model may be well worth the higher costs of each LLM call. For example, reasoning models can be particularly good at assessing the relevance of the retrieved documents and can be more skilled at deciding how best to incorporate that information into a response, especially one that requires more complex reasoning steps. Interestingly, many prompt engineering techniques don't work as well with reasoning models. For example, you don't need to ask them to think step-by-step as this is something they've already been trained to do. They also may not do well with in-context learning as they try to incorporate the provided example responses into the current question being answered. They tend to perform better with specific goals that you want them to work towards and very specific information about the format that you want them to answer in. You can still provide high-level guiding principles and explicitly state approaches you want the model to take or avoid. After that, however, you can just give them the entire context dump of documents retrieved from your RAG system. New models, including reasoning models, are constantly being released, however, and most LLM providers will include information about how best to prompt them. As you start employing more prompt engineering techniques, context window management will become important. Remember, the initial prompt and whatever tokens an LLM generates for the completion both use up portions of its context window. Whether you're injecting documents from your retriever, adding in-context learning examples to every prompt, or having a reasoning model plan its responses before answering a question, all of these advanced techniques increase the length of your prompt, the generated response, or both. It's easy to rapidly fill up your context window if you're not paying attention. With single-turn conversations, the best fix is to just validate you're getting value from your prompt engineering technique. If chain-of-thought prompting or in-context learning isn't giving you better performance, it's better to just remove those components from your system. Multi-turn conversations can quickly eat up your context window as each back and forth message needs to be included in the prompt. A variety of approaches collectively referred to as context pruning addresses this issue. A simple solution is to keep only a fixed number of recent messages in the prompt. For example, the last five sent by the user and the LLM. More sophisticated approaches use a separate LLM to summarize older messages, shrinking their size but preserving their key points. If you're using a reasoning model in a multi-turn conversation, you'll almost certainly want to drop reasoning tokens from the chat history and just keep the response tokens. Likewise, in a RAG system, you usually only want to include the chunks retrieved to support the response to the most recent question, not every question that came before it. Of course, if your application needs multi-turn conversations with deep and rich context, you can always switch to using a model with a longer context window. That said, you'll still want to be thoughtful about how you design prompts, as even on models with longer context windows, long prompts are slow and expensive to run. Prompt engineering techniques can improve the performance of your LLM, but your RAG system doesn't necessarily need to employ them. A simple prompt template and a well-written system prompt might be all you need for your project. When it comes to more advanced techniques, I advise you add them to your project only after it's clear you need them. Prompting in general can be more of an art than a science, so whatever strategies you use, experiment with different prompts and find the ones that work best for your system.
```

## 关键引述/重要观点
> "In-context learning is a technique which allows you to help the LLM learn what kind of output you wanted to generate by adding examples of them to the prompt." 上下文学习是一种通过在提示中添加示例来帮助LLM学习期望输出类型的技术。

> "If you include many examples, this approach is called few-shot learning. If you include just one example, it's called one-shot learning." 如果包含多个示例，这种方法称为少样本学习；如果只包含一个示例，则称为单样本学习。

> "You could just hard code one or more example questions and responses into your prompt." 你可以直接将一个或多个示例问答硬编码到提示中。

> "You can use RAG to retrieve example questions and responses from your knowledge base." 你可以使用RAG从知识库中检索示例问答。

> "Another powerful collection of prompt engineering techniques essentially encourages the LLM to reason through prompts in a step-by-step manner." 另一类强大的提示工程技术基本上是鼓励LLM以逐步方式处理提示并推理。

> "The idea is you're essentially giving the language model a scratchpad to organize its thoughts before answering." 这个理念本质上是为语言模型提供一个草稿纸来组织其在回答前的思维。

> "Chain-of-thought prompting - the LLM is instructed to tackle questions in a step-by-step manner rather than immediately answering them." 思维链提示 - LLM被指示以逐步方式处理问题，而不是立即回答。

> "Reasoning models excel at complex reasoning tasks such as coding, mathematics, planning, puzzles, and complex workflows that require multiple steps." 推理模型在复杂推理任务中表现出色，如编码、数学、规划、谜题以及需要多个步骤的复杂工作流。

> "These reasoning tokens are part of what makes these models more accurate than their non-reasoning counterparts, but they're still just regular tokens with all the associated costs of generating them." 这些推理令牌是使这些模型比非推理对应模型更准确的部分，但它们仍然是常规token，具有生成它们的所有相关成本。

> "As a result, reasoning models are typically slower and more expensive to run." 因此推理模型通常运行更慢、成本更高。

> "Many prompt engineering techniques don't work as well with reasoning models." 许多提示工程技术与推理模型配合使用效果不佳。

> "A variety of approaches collectively referred to as context pruning addresses this issue." 一系列被称为"上下文修剪"的策略可以解决此问题。

> "Prompt engineering techniques can improve the performance of your LLM, but your RAG system doesn't necessarily need to employ them." 提示工程技术可以提高LLM的性能，但RAG系统不一定需要使用它们。

> "Prompting in general can be more of an art than a science, so whatever strategies you use, experiment with different prompts and find the ones that work best for your system." 提示工程总体上更像是一门艺术而非科学，无论使用什么策略，都应该尝试不同的提示并找到最适合系统的那些。

## 相关话题/关键词
- RAG系统 (RAG System)
- 提示工程 (Prompt Engineering)
- 上下文学习 (In-context Learning)
- 少样本学习 (Few-shot Learning)
- 单样本学习 (One-shot Learning)
- 硬编码示例 (Hard-coded Examples)
- 动态检索示例 (Dynamic Retrieved Examples)
- 思维链提示 (Chain-of-Thought Prompting)
- 草稿纸技术 (Scratchpad Technique)
- 推理模型 (Reasoning Models)
- 推理令牌 (Reasoning Tokens)
- 响应令牌 (Response Tokens)
- 上下文窗口管理 (Context Window Management)
-

---

## 视频 7: Handling hallucinations
**时长**: ~7 min (456s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/rrngmz/handling-hallucinations
**视频 ID**: 1199222

# 视频摘要：Handling hallucinations

## 基本信息

- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/rrngmz/handling-hallucinations
- **时长**: 456秒（约7分钟）
- **语言**: 中文
- **发布（原始）时间**: 2024-01-01
- **下载时间**: 2026-05-28 14:18:16

## 原始元数据

- （无额外元数据）

## 输出文件

- video.mp4 - 原始视频文件
- audio.mp3 - 音频文件
- subtitle.vtt - 带时间戳的字幕文件
- subtitle_ai-zh.json - 原始AI字幕JSON
- transcript.txt - 纯文本转录
- summary.md - 本摘要文件

## 内容概述

本视频探讨了在构建RAG（检索增强生成）系统时如何处理LLM（大语言模型）产生的幻觉问题。视频通过一个在线商店客服聊天机器人的具体案例说明了幻觉的危害性，阐述了幻觉产生的原因、类型以及检测和减少幻觉的多种策略，包括系统提示词优化、来源引用要求、ContextCite外部系统以及ALCE基准测试等内容。

## 核心要点

1. **幻觉问题的本质**：LLM被设计为生成概率性文本序列，而非区分真假信息，因此幻觉是LLM的固有特性。

2. **幻觉的危害**：幻觉信息听起来合理可信，难以被察觉；长期下来会导致用户对RAG系统失去信任。

3. **幻觉的类型多样性**：幻觉程度从轻微的数值错误（如折扣5%而非10%）到完全虚构（如根本不存在的学生折扣）不等。

4. **RAG系统的局限性**：虽然RAG是减少幻觉的最佳方法之一，但即使设计良好的RAG系统仍可能产生幻觉。

5. **自一致性检查方法**：让模型重复生成同一提示的完成内容，检查事实信息是否一致——如果产生幻觉，信息会不一致。

6. **知识库 grounding 的重要性**：确保LLM只能基于检索到的信息做出事实性声明，这是减少幻觉的核心方法。

7. **来源引用的作用**：要求模型在每个句子或段落末尾引用来源，可以提高模型基于检索文档回应的可能性，同时方便人工验证。

8. **幻觉引用的风险**：LLM可能幻觉出虚假的引用，某些经过微调的模型能更可靠地生成有效引用。

9. **ContextCite系统功能**：逐句处理响应，将每句话归属到检索提供的上下文文档之一，标记"No source"的句子说明缺乏支撑材料。

10. **ContextCite应用场景**：生成的标签可用于在最终LLM输出中生成来源引用，或作为评估LLM grounding 频率的一部分。

11. **ALCE基准测试**：提供预组装的知识库和示例问题，评估系统生成的响应的流畅性、正确性和引用质量三个关键指标。

12. **实践建议**：构建RAG系统是减少幻觉最有效的步骤；优化系统提示词确保LLM基于检索信息回答；使用幻觉相关基准测试验证系统表现。

## 详细内容

### 一、幻觉问题的背景与案例分析

视频开篇指出，幻觉是使用LLM时持续存在的担忧。即使是设计良好的RAG系统仍然可能产生幻觉，因此检测幻觉、减少幻觉以及确保LLM准确引用来源成为构建RAG管道中最重要的环节。

为了直观说明幻觉问题，课程引入了一个在线商店客服聊天机器人的场景。当用户询问公司是否提供学生折扣时，检索器找到了关于老年人和新客户折扣的信息（两者都可享受10%折扣）。同时，LLM的系统提示鼓励它对客户保持乐于助人的态度。在这些因素的综合影响下，LLM回复道：“当然可以，凭有效学生证可享受10%折扣，与我们为老年人和新客户提供的优惠一样。”用户感到满意并继续在网站上购物，期待在结账时获得折扣。然而，问题在于这个学生折扣实际上并不存在——LLM凭空编造了这个折扣。

这个案例清晰地展示了幻觉如何在RAG系统中发生，以及其潜在的危害性。

### 二、LLM产生幻觉的根本原因

理解LLM为什么会产生幻觉至关重要。语言模型被设计为生成概率性的文本序列，并加入少量随机化以增加多样性。概率性的文本序列通常是事实准确的，但并非总是如此。关键在于，语言模型的设计目的并非区分真伪，而只是区分高概率和低概率。

这意味着LLM的核心工作机制决定了它本质上不具备事实核查能力，而是倾向于生成看似合理的文本，这正是幻觉产生的根源。

### 三、幻觉问题的多重危害

幻觉问题之所以棘手，原因有以下几点。首先，最明显的原因是用户不希望语言模型向其提供不准确的信息，这对用户体验和信任度都是直接的损害。其次，几乎可以说幻觉的定义决定了它听起来是合理的，这使得它比完全荒谬的内容更难被检测出来。用户可能更容易识别出明显胡说八道的内容，但面对听起来头头是道的幻觉信息时却难以辨别真伪。最后，长期来看，偶尔出现的幻觉会导致用户对RAG系统失去信任，即使系统生成的大部分内容是准确的。这种信任的丧失可能是累积性的，一旦用户经历过一次幻觉带来的误导，就可能对整个系统产生怀疑。

### 四、幻觉的多种类型与程度

视频明确指出，幻觉可以有多种类型和程度。回到折扣这个案例，LLM可能准确地描述了真实存在的老年人折扣及其获取方式，但错误地将折扣金额说成5%而非10%。这是一种相对较轻的错误。在更极端的情况下，LLM可能错误地声称不存在老年人折扣，而实际上该折扣确实存在。或者如前文案例所示，完全凭空编造公司根本不提供的新折扣。

这意味着，如果想对LLM生成的文本准确性充满信心，需要在多个层面上评估文本内容。这种多层次评估的需求也反映了幻觉问题的复杂性和解决的困难性。

### 五、当前技术现实与RAG的价值

视频坦诚地指出了一个冷酷的现实：目前没有完美的幻觉解决方案，至少目前还没有。不过幸运的是，RAG是目前可用的最佳方法之一，而且有多种方法可以进一步优化RAG系统以减少幻觉发生的频率。

构建RAG管道的一个重大原因正是为了减少幻觉。从知识库中检索到的信息可以帮助LLM的回应有所依据，并可能提供模型训练数据中缺失的信息。即使如此，RAG系统仍然容易产生幻觉，因此采取额外的预防措施是必要的。

### 六、无知识库情况下的幻觉检测

在没有知识库的情况下思考如何检测LLM输出中的幻觉问题时，选择非常有限。课程介绍了一种称为“自一致性检查”的方法，即让模型多次为同一提示生成完成内容，然后检查其中包含的事实信息是否一致。其底层思想是，如果语言模型在幻觉信息，它会以不一致的方式进行，在不同的完成内容中会出现可检测到的事实差异。

然而在实践中，这种方法可能成本高昂且不可靠。每次生成都需要消耗计算资源，而且即使多次生成的结果不一致，也不能完全确定哪次是正确的。

### 七、基于知识库的幻觉减少策略

既然在RAG系统内部可以访问知识库，最好的减少幻觉方法就是确保回应基于检索到的信息。例如，可以修改系统提示，明确告诉LLM只能基于检索到的信息做出事实性声明。

如果希望更进一步确保LLM是基于检索文档进行回应的，可以要求LLM引用其来源。这有时意味着提示模型在每个句子或段落的末尾引用来源。这可以进一步提高LLM基于检索到的来源进行回应的可能性。同时，引用也使人工读者更容易验证回应中的声明。

### 八、引用幻觉的风险与ContextCite系统

这种方法存在一个风险：LLM可能会凭空编造引用。经过微调以引用来源的某些模型可以更可靠地生成有效引用。但如果希望对引用的准确性有更高的信心，则需要使用外部系统。

ContextCite就是这样一个系统，它对响应在一套源材料中的 grounding 程度进行评分。该系统逐句处理响应，将每句话归属到检索提供并提供给LLM的上下文文档之一。然后ContextCite为每句话生成标签，标注哪份文档是该句话的来源。在陈述没有支撑材料的情况下，会被标记为"No source"。某些实现甚至可能提供句子与识别的源文档之间的相似度分数。

这些标签既可以用来在最终生成的LLM输出中生成源引用，也可以作为评估LLM在多大程度上将其回应基于RAG系统检索文档的一部分。

### 九、ALCE基准测试体系

最近的努力，如ALCE基准测试，旨在衡量系统在生成回应时引用和引用来源的效果。该系统提供预组装的知识库和示例问题。然后可以使用RAG系统在这些提示上询问ALCE系统来评估生成的响应。

系统会为三个关键指标生成分数：流畅性（fluency）、正确性（correctness）和引用质量（citation quality）。换句话说，最终文本有多清晰，内容在事实上的准确程度如何，以及提供的引用与正确的来源对齐程度如何。

这些基准测试不能控制生产系统中的幻觉，但确实能让人了解系统在避免幻觉和引用来源方面的表现。

### 十、最佳实践总结

视频最后总结了构建可靠RAG系统的关键要点。幻觉检测是LLM系统面临的持续挑战。但是，通过构建RAG系统，已经迈出了最小化幻觉最有效的一步。在此之后，应该集中精力确保LLM基于检索到的信息进行回答，通过优化系统提示词来实现。最后，使用以幻觉为重点的基准测试来验证系统，确保系统提供有依据且引用良好的回应。

这些方法结合起来可以显著减少幻觉，帮助构建一个提供可信赖回应的系统。

## 完整字幕原文

```
Hallucinations are a constant concern when working with LLMs, and even a well-designed RAG system can still hallucinate. Detecting hallucinations, reducing them, and ensuring the LLM accurately cites sources are therefore the most important parts of building your RAG pipeline. Let's have a look at a few ways this is done. Imagine you get your first RAG system up and running. A customer service chatbot for an online store. A user writes in and asks if the company offers student discounts. The retriever finds information about discounts for both seniors and new customers, both of whom would receive 10% off. Meanwhile, the LLM system prompt encourages it to be helpful with customers. All of these factors influence the LLM, which responds, Absolutely, you can get 10% off with a valid student ID. The same great discount we offer our seniors and new customers. The user is delighted and continues shopping on your site, eager to claim their discount at checkout. The only problem? That student discount doesn't actually exist. The LLM just made it up. It's important to remember why LLMs hallucinate in the first place. A language model is designed to produce probable text sequences, with a bit of randomization thrown in for variety. Probable text sequences are often factually accurate, but not always. And language models aren't designed to differentiate between true and false, just probable and improbable. Hallucinations are problematic for a few reasons. The first is obvious enough. You just don't want your language model to provide inaccurate information to your user. The second is that, almost by definition, hallucinations sound plausible. And so can be more difficult to detect than total nonsense. Finally, over time, occasional hallucinations can cause your users to lose trust in your RAG system, even if the majority of generated content is accurate. Of course, a big reason you'd build a RAG pipeline is to reduce hallucinations. The information you retrieve from your knowledge base can help ground an LLM's responses and possibly provides information missing in the model's training data. Even so, RAG systems are still prone to hallucination, so additional steps to prevent them are necessary. Hallucinations can come in many types and sizes. Going back to that discount, an LLM might accurately describe the very real senior discount and how to claim it, but misstate the discount as 5% instead of 10%. In more extreme cases, the LLM might inaccurately state there isn't a senior discount when actually one exists. Or as you saw earlier, invent entirely new discounts your company doesn't offer. This means you'll need to evaluate the text your LLM generates on many levels if you want to feel confident in its accuracy. Now here comes the cold, hard truth. There's no perfect solution for hallucinations. Or at least not currently. Luckily, however, RAG is one of the best approaches currently available and there's ways you can refine RAG systems to further decrease the frequency of hallucinations. To start, think through how you'd detect hallucinations in LLM output if you didn't have a knowledge base. Without a trusted external source of truth to compare that output to, your options are pretty limited. One approach, however, is self-consistency checking, where you have the model repeatedly generate completions for the same prompt and check if the factual information contained within them is consistent. The underlying idea is that if the language model is hallucinating information, it'll do so inconsistently. And factual differences across completions will be detectable. In practice, however, this method can be costly and unreliable. If you have a knowledge base to reference, that's the best place to start. Since inside a RAG system, you do have access to a knowledge base, the best approach to decrease hallucinations is to ensure responses are grounded in retrieved information. For example, you could modify your system prompt to say that the LLM can only make factual claims based on retrieved information. If you want further confidence that the LLM is basing its responses on retrieved documents, you can further require the LLM to cite its sources. Sometimes, this just means prompting the model to cite sources at the end of each sentence or paragraph. This can further increase the likelihood that the LLM grounds its responses in the retrieved sources. And citations also make it easier for a human reader to verify claims in the response. A risk with this approach, however, is that the LLM will just hallucinate the citations. Some models fine-tuned to cite sources will generate valid citations more reliably. But if you want more confidence in your citations, you'll need to use an external system. For example, ContextCite is a system that scores how well a response is grounded in a set of source materials. The model processes the response sentence by sentence, and it attributes each sentence to one of the context documents that were retrieved and provided to the LLM. ContextCite then generates tags for each sentence, noting which document is the source of that sentence. In cases where the statement does not have supporting material, it's labeled no source. Some implementations may even provide a similarity score between the sentence and the identified source document. These tags can either be used to generate source citations in the final generated LLM output, or as a part of evaluation of how frequently the LLM is grounding its responses in the documents retrieved by a RAG system. Recent efforts, such as the ALCE benchmark, aim to measure how well a system references and cites sources when generating responses. The system provides pre-assembled knowledge bases and sample questions. You would then use your RAG system on these prompts to ask the ALCE system to evaluate the generated response. Scores are generated for three key metrics, fluency, correctness, and citation quality. In other words, how clear is the final text, how factually accurate, and how well do the provided citations align with the correct sources to cite. These benchmarks don't control hallucinations in your production system, but they do give some sense of how well your system is avoiding hallucinations and citing sources. Hallucination detection is a constant challenge in an LLM-based system. That said, by building a RAG system, you're already taking the single most effective step to minimize hallucinations. After that, focus your energy on ensuring the LLM grounds its answers and retrieved information by refining your system prompt. Finally, test your system using hallucination-focused benchmarks to ensure your system is providing grounded, well-cited responses. Together, these approaches can significantly reduce hallucinations and help you build a system that provides trustworthy responses.
```

## 关键引述/重要观点

> “Hallucinations are a constant concern when working with LLMs, and even a well-designed RAG system can still hallucinate. Detecting hallucinations, reducing them, and ensuring the LLM accurately cites sources are therefore the most important parts of building your RAG pipeline.”（幻觉是使用LLM时持续存在的担忧。即使是设计良好的RAG系统仍然可能产生幻觉。因此检测幻觉、减少幻觉以及确保LLM准确引用来源成为构建RAG管道中最重要的环节。）

> “A language model is designed to produce probable text sequences, with a bit of randomization thrown in for variety. Probable text sequences are often factually accurate, but not always. And language models aren't designed to differentiate between true and false, just probable and improbable.”（语言模型被设计为生成概率性的文本序列，并加入少量随机化以增加多样性。概率性的文本序列通常是事实准确的，但并非总是如此。语言模型的设计目的并非区分真伪，而只是区分高概率和低概率。）

> “Hallucinations are problematic for a few reasons... hallucinations sound plausible... can be more difficult to detect than total nonsense... over time, occasional hallucinations can cause your users to lose trust in your RAG system, even if the majority of generated content is accurate.”（幻觉问题之所以棘手，原因有以下几点……幻觉听起来是合理的……比完全荒谬的内容更难被检测出来……长期来看，偶尔出现的幻觉会导致用户对RAG系统失去信任，即使系统生成的大部分内容是准确的。）

> “Now here comes the cold, hard truth. There's no perfect solution for hallucinations. Or at least not currently. Luckily, however, RAG is one of the best approaches currently available and there's ways you can refine RAG systems to further decrease the frequency of hallucinations.”（现在迎来冷酷的现实：目前没有完美的幻觉解决方案，至少目前还没有。不过幸运的是，RAG是目前可用的最佳方法之一，而且有多种方法可以进一步优化RAG系统以减少幻觉发生的频率。）

> “The best approach to decrease hallucinations is to ensure responses are grounded in retrieved information.”（最好的减少幻觉方法是确保回应基于检索到的信息。）

> “ContextCite is a system that scores how well a response is grounded in a set of source materials. The model processes the response sentence by sentence, and it attributes each sentence to one of the context documents that were retrieved and provided to the LLM.”（ContextCite是一个对响应在一套源材料中的 grounding 程度进行评分的系统。该模型逐句处理响应，将每句话归属到检索提供并提供给LLM的上下文文档之一。）

> “Scores are generated for three key metrics, fluency, correctness, and citation quality. In other words, how clear is the final text, how factually accurate, and how well do the provided citations align with the correct sources to cite.”（系统会为三个关键指标生成分数：流畅性、正确性和引用质量。换句话说，最终文本有多清晰，内容在事实上的准确程度如何，以及提供的引用与正确的来源对齐程度如何。）

> “By building a RAG system, you're already taking the single most effective step to minimize hallucinations. After that, focus your energy on ensuring the LLM grounds its answers and retrieved information by refining your system prompt.

---

## 视频 8: Evaluating your LLM's performance
**时长**: ~5 min (326s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/66p3pm/evaluating-your-llm's-performance
**视频 ID**: 1199223

# 视频摘要：Evaluating your LLM's performance

## 基本信息

- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/66p3pm/evaluating-your-llm's-performance
- **时长**: 326秒 (约5分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:18:34

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

本视频介绍了在RAG（检索增强生成）系统中评估LLM性能的方法和指标。视频强调了明确LLM在RAG流程中的具体职责的重要性，并介绍了RAGAS开源库提供的响应相关性和忠实度等关键评估指标，同时探讨了如何通过用户反馈和A/B测试进行系统级性能评估。

## 核心要点

1. **职责分离原则**：在RAG系统中，检索器负责从知识库中找到相关信息，LLM负责利用这些信息构建高质量响应，评估时需明确区分两者的职责
2. **评估主观性挑战**：LLM的响应质量具有主观性，难以用传统自动化指标定量衡量
3. **LLM评估LLM方法**：利用其他LLM来评估响应质量，实现评估的可扩展性和灵活性
4. **RAGAS开源库**：RAGAS是RAG特定指标的重要来源，提供多种评估方法
5. **响应相关性指标**：通过生成样本提示并计算余弦相似度来衡量响应与用户提示的相关性
6. **忠实度指标**：检查响应中的事实主张是否被检索信息支持，计算支持比例
7. **系统级评估策略**：通过用户反馈（点赞/点踩）和A/B测试评估LLM变更的影响
8. **指标局限性认知**：所有评估指标都依赖LLM调用或真实正确答案作为参考
9. **调整决策依据**：LLM性能指标是决定调整温度、更新系统提示或更换模型的实用工具
10. **综合评估方法**：结合LLM评估和人类反馈才能全面准确地评估LLM性能

## 详细内容（保留所有原始信息）

### 一、LLM性能评估的背景与必要性

无论是刚刚构建了第一个概念验证RAG系统，还是正在迭代已经投入生产的系统，都需要了解LLM的性能表现。当考虑调整模型的温度参数、更新系统提示，或者甚至完全更换为新的模型时，为了做出明智的决策，需要准备好相应的指标来衡量每个决策的影响。

### 二、RAG系统中LLM的职责定位

由于LLM运行在一个复杂的系统中，首先必须明确LLM负责哪些具体任务。在典型的RAG架构中，检索器的工作是从知识库中找到相关信息，而LLM的工作是利用这些信息来构建高质量的响应。这意味着在考虑对LLM进行调整，甚至完全替换底层模型时，必须确保所使用的指标聚焦于LLM在更广泛RAG流程中的作用。如果问题实际上出在检索器上，就不应该浪费时间去重写系统提示。

### 三、假设检索器正常工作时的LLM评估

假设检索器运行良好，它应该能找到大部分相关信息，可能会有少量不相关的文档被加入。相应地，LLM的工作包括：响应用户提示、将相关信息整合到响应中、恰当地引用信息来源，以及不被检索到的任何无关信息分散注意力。值得注意的是，这些LLM特定行为大多数都具有一定程度的主观性。

### 四、评估LLM性能的核心挑战

如何定量地判断一个响应是否很好地回答了用户原始问题，或者是否忽略了无关信息？由于这种主观性，大多数LLM特定指标都依赖使用其他LLM来评估响应的质量。将LLM纳入评估过程，允许在可扩展的方式中融入一定程度的灵活性或主观性判断。

### 五、RAGAS开源库及其评估指标

RAGAS是一个优秀的RAG特定指标开源来源，提供多种评估方法。

#### 5.1 响应相关性指标（Response Relevancy）

响应相关性衡量响应是否实际与用户提示相关。该指标检查响应是否与原始提示相关，而不关心其是否事实准确。评估流程如下：首先，将RAG系统生成的响应输入到一个新的LLM中，由该LLM生成几个它认为可能导致该响应的样本提示；然后，将原始用户提示和这些样本提示都嵌入到语义向量空间；接着，计算实际用户提示与每个样本提示之间的余弦相似度；最后，将这些相似度分数平均，得到响应相关性的最终衡量。需要注意的是，该指标不一定确保响应提供事实信息，但它确实检查了是否可以从LLM给出的响应合理地反向推导到原始提示。

#### 5.2 忠实度指标（Faithfulness）

要衡量LLM是否实际使用了检索到的信息，可以使用忠实度指标。该指标使用语言模型识别响应中包含的所有事实主张，然后使用更多的语言模型调用来确定这些主张中有多少得到了从知识库检索到的信息的支持。支持主张占所有主张的百分比就是该特定提示、检索和响应组合的忠实度分数。

#### 5.3 其他RAGAS指标

RAGAS库中包含的其他指标采用类似的方法来评估诸如对从知识库检索到的无关信息的敏感性、准确引用来源的能力等方面。

### 六、所有LLM评估指标的共同特点

所有这些指标都有一个共同特点，即在评估过程的某个环节依赖LLM调用，甚至可能需要真实正确答案的示例。这反映了LLM在RAG系统中的角色是复杂的，很难用更简单的自动化指标来评估。

### 七、系统级性能评估方法

除了这些LLM特定的评估方法外，还有其他方式可以使用覆盖整个系统的指标来评估LLM性能。例如，如果用户可以对RAG系统的响应进行点赞或点踩评分，就可以对系统提示的更改进行A/B测试，观察更改对整体用户满意度的影响。这种方法的理念是：测量系统级性能，但将更改隔离到LLM设置，从而能够将整体性能的变更归因于LLM的更改。

### 八、综合评估策略与实践建议

LLM性能指标是决定调整LLM设置或更换模型的实用工具。由于LLM响应的质量具有一定的主观性，应该计划使用基于LLM判断的评估或人类反馈来评估LLM质量。结合这些技术将能够自信地评估LLM的运行效果。

## 完整字幕原文

```
Whether you've just built your first proof-of-concept RAG system, or are iterating on a system already in production, you'll want to know how well your LLM is performing. Whether you're considering adjusting your model's temperature, updating your system prompt, or even swapping in an entirely new model. In order to make an informed decision, you'll need to have metrics on hand to measure each decision's impact. Let's look at some common methods for evaluating your LLM's performance. Since your LLM is operating inside of a complex system, to start, it's important to be clear on what specific tasks your LLM is responsible for. Your retriever's job is to find the relevant information from the knowledge base. Your LLM's job is to use that information to construct a high-quality response. This means that when considering adjustments to your LLM, or even replacing the underlying model entirely, you want to make sure the metrics you're using focus on the LLM's role in the broader RAG pipeline. If the problem ultimately lies with your retriever, you don't want to waste time rewriting your system prompt. If you assume your retriever is operating well, then it should find mostly relevant information, perhaps with a few irrelevant documents added. The job of your LLM, then, is to respond to the user prompt, incorporate the relevant information into its response, cite it appropriately, and resist getting distracted by any irrelevant information that was retrieved. Note, most of these LLM-specific behaviors are somewhat subjective. How can you say quantitatively that a response does a good job of answering the user's original question, or ignoring irrelevant information? As a result, most LLM-specific metrics rely on using other LLMs to assess the quality of a response. Incorporating LLMs into the evaluation process allows for some degree of flexibility or subjectivity in a scalable way. A good source of these RAG-specific metrics is the open-source RAGAS library. Let's look at a few metrics it provides. Response relevancy measures whether a response is actually relevant to a user prompt. This metric checks whether the response was relevant to the original prompt, regardless of whether it's factually accurate. Here's how it works. First, the response generated by your RAG system is fed to a new LLM that generates several sample prompts it believes could have led to that response. Then, both the original user prompt and these sample prompts are embedded to a semantic vector. Next, the cosine similarity between the actual user prompt and each sample prompt is calculated. Finally, these similarity scores are averaged, giving the ultimate measure of response relevancy. Note, this metric doesn't necessarily ensure the response is providing factual information, but it does check whether you can reasonably work backwards from the response the LLM gave to the prompt it was originally given. To measure whether the LLM is actually using retrieved information, you could use the faithfulness metric. This metric uses a language model to identify all the factual claims made within the response. It then uses more language model calls to determine how many of these claims are supported by one of the pieces of information retrieved from the knowledge base. The percentage of the claims that are supported is the faithfulness for that particular prompt, retrieval, and response. Other metrics included in the RAGAS library take similar approaches to assess things like sensitivity to irrelevant information retrieved from the knowledge base or ability to accurately cite sources. A pattern across all these metrics, however, is the reliance on LLM calls at some point in the eval process, and even possibly examples of ground truth correct answers. This speaks to the fact that the role of the LLM in a RAG system is complex and difficult to evaluate with more simplistic automated metrics. In addition to these LLM specific evals, there are ways you can use metrics that run across your entire system to evaluate LLM performance. For example, if your users can mark responses from your RAG system with a thumbs up or thumbs down rating, you can then A-B test changes to your system prompt and see what impact the change has on overall user satisfaction. The idea here is that you measure system-wide performance but isolate changes to LLM settings, allowing you to attribute changes in overall performance to changes to your LLM. LLM performance metrics are useful tools for deciding to adjust your LLM settings or even switch to a new model. Since the quality of an LLM's responses are somewhat subjective, you should plan on using either LLM as a judge based evals or human feedback to assess LLM quality. A combination of these techniques will allow you to confidently evaluate how well your LLM is operating.
```

## 关键引述/重要观点

> "Since your LLM is operating inside of a complex system, to start, it's important to be clear on what specific tasks your LLM is responsible for."

> "If the problem ultimately lies with your retriever, you don't want to waste time rewriting your system prompt."

> "Note, most of these LLM-specific behaviors are somewhat subjective."

> "Incorporating LLMs into the evaluation process allows for some degree of flexibility or subjectivity in a scalable way."

> "Response relevancy measures whether a response is actually relevant to a user prompt. This metric checks whether the response was relevant to the original prompt, regardless of whether it's factually accurate."

> "This metric doesn't necessarily ensure the response is providing factual information, but it does check whether you can reasonably work backwards from the response the LLM gave to the prompt it was originally given."

> "The percentage of the claims that are supported is the faithfulness for that particular prompt, retrieval, and response."

> "A pattern across all these metrics, however, is the reliance on LLM calls at some point in the eval process, and even possibly examples of ground truth correct answers. This speaks to the fact that the role of the LLM in a RAG system is complex and difficult to evaluate with more simplistic automated metrics."

> "The idea here is that you measure system-wide performance but isolate changes to LLM settings, allowing you to attribute changes in overall performance to changes to your LLM."

> "Since the quality of an LLM's responses are somewhat subjective, you should plan on using either LLM as a judge based evals or human feedback to assess LLM quality."

## 相关话题/关键词

- RAG（检索增强生成）
- LLM性能评估
- 检索器（Retriever）
- 响应相关性（Response Relevancy）
- 忠实度（Faithfulness）
- RAGAS开源库
- 余弦相似度
- 语义向量嵌入
- 事实主张验证
- A/B测试
- 用户反馈
- 系统提示优化
- 模型温度调整
- LLM作为评判者
- 自动化评估指标
- 概念验证（POC）
- 知识库检索
- 引用来源准确性
- 无关信息敏感性
- 生产系统迭代

## 技术信息

- 字幕字数: 4843
- 字幕字符数: 4843
- 时间戳条目数: 0
- 处理时间: 2026-05-28 14:18:34

---

## 视频 9: Agentic RAG
**时长**: ~6 min (375s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/aam1f5/agentic-rag
**视频 ID**: 1199224

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

---

## 视频 10: RAG vs. Fine-Tuning
**时长**: ~6 min (380s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/00uskr/rag-vs.-fine-tuning
**视频 ID**: 1199216

# 视频摘要：RAG vs. Fine-Tuning

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/00uskr/rag-vs.-fine-tuning
- **时长**: 380秒 (约6分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:19:01

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
本视频探讨了RAG（检索增强生成）与Fine-Tuning（微调）两种优化大语言模型性能的技术方法。视频详细解释了Fine-Tuning的核心概念、实现方式和适用场景，并与RAG进行对比，强调当前共识认为RAG最适合知识注入，而Fine-Tuning最适合领域适配。视频还指出这两种技术实际上是互补工具，可以结合使用以提升系统性能。

## 核心要点
1. Fine-Tuning的核心思想是用你自己的数据重新训练现成的语言模型，以更新其内部参数
2. Fine-Tuning通常通过监督微调（Supervised Fine-Tuning，SFT）完成
3. 指令微调（Instruction Fine-Tuning）数据集包含对语言模型的指令（提示或问题）以及预期的标准答案
4. Fine-Tuning通过比较模型输出与正确答案来调整模型内部参数
5. Fine-Tuning在模型需要专精于特定领域（如医疗诊断、法律文书总结）时效果显著
6. Fine-Tuning可能降低模型在其他领域的性能表现
7. 小型模型在代理系统中经过大量微调后可以出色地完成单一任务
8. Fine-Tuning通常不是向LLM教授新信息的最佳方法
9. Fine-Tuning对模型响应方式（用词、风格、结构）的影响大于对模型知识的影响
10. 当前共识：RAG最适合知识注入，Fine-Tuning最适合领域适配
11. 需要LLM获取新信息时，RAG是最佳解决方案
12. 需要LLM专精于特定任务或领域时，Fine-Tuning是正确选择
13. Fine-Tuning和RAG可以结合使用以提升系统性能
14. 可以找到已经预微调的模型用于特定任务或领域
15. Fine-Tuning和RAG应被视为互补工具而非竞争替代品

## 详细内容（保留所有原始信息）

### 1. Fine-Tuning的核心概念

Fine-Tuning的核心思想是用你自己的数据重新训练语言模型，以更新其内部参数。这与仅通过提示增强不同，Fine-Tuning通过训练过程从根本上改变模型的能力。通常，这通过监督微调（Supervised Fine-Tuning，SFT）完成。之所以称为监督，是因为模型使用来自目标领域的有标签数据集进行重新训练。

### 2. 指令微调（Instruction Fine-Tuning）

指令微调是一种特殊方法，其数据集包含两部分：对语言模型的指令（通常是一个提示或问题），以及预期的最佳答案（ground truth）。微调过程是：你向模型输入指令，观察其输出与你数据集中正确答案的接近程度，然后利用这些结果调整模型的内部参数，使其更好地与正确答案对齐。这个过程与语言模型最初的训练方式非常相似，但使用的数据集来自模型正在专精的特定领域。

### 3. 领域专精示例：医疗领域

以医疗领域为例。首先选择一个通用语言模型。如果问这个模型关于关节疼痛、皮疹、光敏感等具体症状，它可能给出一个泛泛的答案，语气也比较通用。这是因为现成的模型没有在医学数据上进行过专精。但如果对同一个模型使用指令微调，用大量医学领域的指令和响应对其进行训练，模型本质上会变成回答这类问题的专家。此时再给同样的提示，模型就能更准确、详细地回答，并以更适合医学领域的风格回应。

### 4. Fine-Tuning的优势与局限

Fine-Tuning在需要模型专精于特定领域的场景下效果很好，比如提供初步医学诊断或总结法律文书。然而，虽然模型在该领域的性能会提升，Fine-Tuning实际上可能降低模型在其他领域的性能。Fine-Tuning过程只优化模型在目标领域的性能，这意味着有时对模型内部参数的调整会导致模型在其他类型请求上的表现下降。只要模型只在专精的领域内使用，这种权衡通常是值得的。

### 5. 小型模型在代理系统中的应用

这种情况在代理系统内部使用的小型模型上尤为明显。如果你提前知道一个模型唯一的任务就是判断提示是否需要从向量数据库进行检索，你会非常乐意使用小型、轻量级的模型，并对其大量微调，使其只出色地完成这一单一任务。

### 6. Fine-Tuning不适合教授新知识

值得注意的是，Fine-Tuning通常不是向LLM教授新信息的最佳方法。模型通过Fine-Tuning进行适应的方式对模型响应提示的方式（如用词、风格或结构）影响更大，而对模型所知信息的影响则不那么明显。

### 7. RAG与Fine-Tuning的选择

当前共识认为，RAG最适合知识注入，Fine-Tuning最适合领域适配。如果你需要LLM获取新信息，检索增强生成是最佳解决方案。你可以将这些信息注入提示，现成的LLM就能在其响应中融入这些新信息。另一方面，如果你希望LLM专精于特定任务或领域，Fine-Tuning是正确选择。特别是如果你的LLM将处理一项独立任务，如在RAG系统中路由提示，或仅响应某种类型的提示，Fine-Tuning就更有意义。

### 8. RAG与Fine-Tuning的结合使用

Fine-Tuning和RAG也可以结合使用。特别是，你可以专门微调一个模型，使其将检索到的信息整合到最终响应中。换句话说，你正在帮助模型专精于它在RAG系统中的角色。在决定使用Fine-Tuning还是RAG时，最佳选择可能是两者兼用。每种方法以不同方式提升模型性能，两者结合使用是有益的。

### 9. 如何将Fine-Tuning融入RAG系统

如果你想将Fine-Tuning融入自己的RAG系统，建议你学习专门的Fine-Tuning课程，探索如何微调你自己的语言模型。Fine-Tuning是一个复杂的主题，无法在这门课程中充分涵盖。不过，通常你可以找到已经为你微调好的、适用于特定任务或领域的模型。如果你认为你的系统需要微调模型，许多在线仓库提供预先微调好的模型，你可能可以直接使用而无需自己进行微调。

### 10. 总结：互补而非竞争

Fine-Tuning和RAG有时被描述为相互竞争的替代方案，但更准确地说，它们是互补工具。将微调模型添加到RAG管道中，甚至微调生成最终响应的核心LLM，都可以帮助提升系统性能。虽然你不会在这门课程中深入探讨Fine-Tuning技术，但随着你继续构建生成式AI技能并寻找优化RAG系统的方法，它绝对值得探索。

## 完整字幕原文
```
While RAG is a popular and powerful approach for improving the performance of an LLM, another technique called fine-tuning is also frequently used. Rather than just augmenting the prompt, fine-tuning retrains an off-the-shelf LLM to improve performance in a specific context. Let's look more closely at fine-tuning and what role it can play in your RAG system. The core idea of fine-tuning is to retrain a language model with your own data to update its internal parameters. Typically, this is done through supervised fine-tuning, or SFT. It's supervised because the model is retrained using a labeled dataset from the domain the model is being adapted to. Instruction fine-tuning, in particular, refers to an approach in which the dataset includes both a set of instructions to the language model, typically a prompt or a question, as well as an expected ground truth best answer. To fine-tune the model, you feed it the input instructions and see how close the output is to the correct answers from your dataset. You then use these results to adjust the model's internal parameters to better align with the correct answer. This process is very similar to the way language models are initially trained, but the dataset used is taken from a specific domain the model is being fine-tuned to specialize in. Suppose you want to fine-tune a model to work in the healthcare domain. To start, you would choose a general purpose language model. If you ask this model about a specific set of symptoms, say joint pain, skin rash, sun sensitivity, the language model might give you a generic answer in a generic tone. This is because the off-the-shelf model hasn't been specialized on medical data. If you use instruction tuning on that same model, training it on a lot of medical domain instructions and responses, the model essentially becomes much more of an expert at answering that kind of question. Now, if you gave it that same prompt, it'd be able to respond with more accuracy, detail, and in a style that's more appropriate for the medical domain. Fine-tuning can work well in instances like this one where you want the model to specialize in a particular domain, like providing an initial medical diagnosis or summarizing legal briefs. While the model's performance will improve in that domain, fine-tuning can actually decrease performance in other domains. The fine-tuning process is only optimizing the model's performance in the target domain, which means that sometimes adjustments made to the model's internal parameters will lead to lower performance with other kinds of requests. So long as the model will only be used within the domain it's being specialized for, however, this trade-off is usually worth it. A particular place this is true is for small models used inside agentic systems. If you know ahead of time a model's only job will be to determine whether a prompt requires retrieval from a vector database, you're more than happy to use a small, lightweight model and heavily fine-tune that model to only perform well at that single task. It's worth noting fine-tuning is usually not a great way to teach an LLM new information. The way a model is adapted by fine-tuning tends to have a greater impact on how the model responds to prompts, like the words it uses, style, or structure, and less pronounced impact on what information the model knows. This last point hits at some of the pros and cons of RAG versus fine-tuning, so let's talk about when it makes sense to use each. In short, the current consensus is that RAG is best at knowledge injection and fine-tuning is best at domain adaption. If you need the LLM to have access to new information, retrieval augmented generation is the best solution. You can inject that information into the prompt and an off-the-shelf LLM will be able to incorporate that new information in its response. If, on the other hand, you want your LLM to specialize in a certain task or domain, fine-tuning is the way to go. Especially if your LLM will be handling one discrete task, like routing prompts in your RAG system, or responding to only a certain type of prompt, fine-tuning makes a lot more sense. Fine-tuning and RAG can also be used together. In particular, you might fine-tune a model specifically to incorporate retrieved information into its final responses. In other words, you're helping the model specialize in its role within the RAG system. When deciding whether to use fine-tuning or RAG, the best choice might be both. Each approach improves the model's performance in different ways and there are benefits to using both of them together. If you want to incorporate fine-tuning into your own RAG system, I recommend you take a separate course on fine-tuning and explore how to fine-tune your own language model. Fine-tuning is a complex topic and it'd be impossible to adequately cover it within this course. That said, often you can find models that have already been fine-tuned for you and adapted to a particular task or domain. If you think your system needs a fine-tuned model, many online repositories of previously fine-tuned models are available and you might be able to use one of those without doing the fine-tuning yourself. Fine-tuning and RAG are sometimes described as competing alternatives, but they're more accurately viewed as complementary tools. Adding fine-tuned models into your RAG pipeline or even fine-tuning the core LLM that generates your final response can help improve your system's performance. While you won't dive into fine-tuning techniques in this course, it's definitely worth exploring as you continue to build your generative AI skills and look for ways to optimize your RAG systems.
```

## 关键引述/重要观点

> "The core idea of fine-tuning is to retrain a language model with your own data to update its internal parameters."

> "Instruction fine-tuning, in particular, refers to an approach in which the dataset includes both a set of instructions to the language model, typically a prompt or a question, as well as an expected ground truth best answer."

> "Fine-tuning can work well in instances like this one where you want the model to specialize in a particular domain, like providing an initial medical diagnosis or summarizing legal briefs."

> "Fine-tuning can actually decrease performance in other domains."

> "Fine-tuning is usually not a great way to teach an LLM new information. The way a model is adapted by fine-tuning tends to have a greater impact on how the model responds to prompts, like the words it uses, style, or structure, and less pronounced impact on what information the model knows."

> "In short, the current consensus is that RAG is best at knowledge injection and fine-tuning is best at domain adaption."

> "If you need the LLM to have access to new information, retrieval augmented generation is the best solution."

> "If, on the other hand, you want your LLM to specialize in a certain task or domain, fine-tuning is the way to go."

> "Fine-tuning and RAG can also be used together."

> "Fine-tuning and RAG are sometimes described as competing alternatives, but they're more accurately viewed as complementary tools."

## 相关话题/关键词
- RAG（检索增强生成）
- Fine-Tuning（微调）
- 监督微调（SFT）
- 指令微调（Instruction Fine-Tuning）
- 语言模型（LLM）
- 领域适配（Domain Adaptation）
- 知识注入（Knowledge Injection）
- 内部参数（Internal Parameters）
- 向量数据库（Vector Database）
- 代理系统（Agentic Systems）
- 生成式AI（Generative AI）
- 模型专精化
- 提示工程
- 模型优化

## 技术信息
- 字幕字数: 5697
- 字幕字符数: 5697
- 时间戳条目数: 0
- 处理时间: 2026-05-28 14:19:01

---

## 视频 11: Module 4 conclusion
**时长**: ~1 min (73s)
**链接**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/558ul7/module-4-conclusion
**视频 ID**: 1199225

# 视频摘要：Module 4 conclusion

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/558ul7/module-4-conclusion
- **时长**: 73秒 (约1分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:19:25

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
本视频为DeepLearning.AI RAG课程第四模块的结语部分，对模块中涵盖的所有LLM主题进行了系统性的快速回顾。从Transformer架构核心原理到采样策略、Prompt工程、幻觉检测与预防、性能评估技术，再到Agentic组件和模型微调等高级主题，全面梳理了构建RAG系统所需的核心概念和工具。视频最后为下一模块的学习做了铺垫，引导学员将RAG应用从原型推向生产级系统。

## 核心要点

1. **Transformer架构深入理解**：深入探索Transformer的核心机制，理解其如何处理文本以深入理解含义并生成相关补全内容

2. **采样策略调整随机性**：学习各种采样策略，用于调整语言模型生成文本时固有的随机性，以适应不同应用需求

3. **基准测试选择LLM**：掌握使用基准测试来选择合适的大语言模型的方法

4. **Prompt工程多样化技巧**：学习多种广泛的Prompt工程技巧以优化模型输出

5. **幻觉检测与预防**：了解如何检测和防止LLM产生幻觉内容，确保输出的准确性和可靠性

6. **LLM性能评估技术**：学习多种评估LLM性能的技术和方法

7. **Agentic组件扩展能力**：通过添加Agentic组件来扩展RAG系统的能力边界

8. **模型微调优化**：通过微调模型来进一步优化RAG系统的性能和效果

9. **坚实基础建立**：完成本模块后，学员已具备坚实的LLM概念基础

10. **完整工具链掌握**：掌握构建首个RAG系统所需的全部工具

11. **下一步学习方向**：为进入最终模块做好准备，学习如何将RAG应用从原型转化为生产级系统

## 详细内容（保留所有原始信息）

### 1. 模块完成与整体回顾

本视频首先对学员完成第四模块表示祝贺，强调本模块涵盖了大量LLM相关主题，需要进行快速全面回顾以巩固学习成果。这是课程中承上启下的重要环节，帮助学员在进入下一模块前梳理已学知识的整体脉络。

### 2. Transformer架构深入探索

模块开头部分深入探索了Transformer的核心机制。学员理解了Transformer如何处理文本数据，建立对文本含义的深度理解，并基于这种理解生成相关的补全内容。这一部分帮助学员从底层架构层面把握LLM的工作原理，为后续学习奠定理论基础。

### 3. 采样策略与随机性控制

视频详细介绍了各种采样策略的应用。这些策略用于调整语言模型在生成文本时固有的随机性程度。不同的应用场景对随机性的要求不同，因此掌握如何调节这一参数对于优化模型输出以适配特定应用需求至关重要。

### 4. LLM选择与Prompt工程

本部分涵盖三个重要主题：
- **基准测试选择LLM**：学习如何利用基准测试工具来评估和选择最适合项目需求的大语言模型
- **Prompt工程技巧**：掌握丰富多样的Prompt工程技术，用于优化模型响应质量和相关性
- **幻觉检测与预防**：了解当前LLM领域的重要挑战，即如何识别和有效防止模型产生幻觉内容

### 5. LLM性能评估技术

视频深入讲解了评估LLM性能的多种技术方法。性能评估是确保模型在实际应用中表现优异的关键环节，学员学习了系统性的评估框架和具体技术手段。

### 6. Agentic组件与模型微调

最后一部分探讨了进阶技术：
- **Agentic组件**：通过添加具有自主性的组件来突破RAG系统的能力边界
- **模型微调**：通过微调技术进一步优化模型以适应特定任务需求

这些技术能够帮助开发者将RAG系统推向更高的性能水平。

### 7. 下一模块展望

视频最后总结了当前学习成果：学员已经建立了坚实的LLM概念基础，并掌握了构建首个RAG系统所需的全部工具。下一（也是最终）模块将展示如何将RAG应用从简单的原型转化为生产就绪的系统。

## 完整字幕原文

```
Nice work completing this module. There were a lot of LLM topics covered here, so let's do a quick review of everything you saw. At the beginning of this module, you went deep into the heart of a transformer, understanding how it processes text to develop a deep understanding of its meaning and generate relevant completions. You then saw how various sampling strategies can be used to tune the randomness inherent in how a language model generates text to fit the needs of your application. Next, you learned how to use benchmarks to choose your LLM, a wide variety of prompt engineering techniques, and how to detect and prevent hallucinations. Then, you learned a wide variety of techniques used to evaluate LLM performance. And finally, you looked at how adding agentic components or fine-tuning models can push the limits of what your RAG system is able to do. At this point, you have a strong foundation in LLM concepts and have all the tools you need to build your first RAG system. So, join me in the next and final module of this course to see how your RAG application can go from a simple prototype to a production-ready system.
```

## 关键引述/重要观点

> "Nice work completing this module. There were a lot of LLM topics covered here, so let's do a quick review of everything you saw."
> [无时间戳] — 模块完成的肯定与回顾引言

> "At the beginning of this module, you went deep into the heart of a transformer, understanding how it processes text to develop a deep understanding of its meaning and generate relevant completions."
> [无时间戳] — Transformer架构核心作用描述

> "You then saw how various sampling strategies can be used to tune the randomness inherent in how a language model generates text to fit the needs of your application."
> [无时间戳] — 采样策略调整随机性的功能说明

> "Next, you learned how to use benchmarks to choose your LLM, a wide variety of prompt engineering techniques, and how to detect and prevent hallucinations."
> [无时间戳] — Prompt工程与幻觉检测的重要性

> "Then, you learned a wide variety of techniques used to evaluate LLM performance."
> [无时间戳] — 性能评估技术模块

> "And finally, you looked at how adding agentic components or fine-tuning models can push the limits of what your RAG system is able to do."
> [无时间戳] — Agentic组件与模型微调的进阶能力

> "At this point, you have a strong foundation in LLM concepts and have all the tools you need to build your first RAG system."
> [无时间戳] — 学习成果总结：坚实基础与完整工具

> "So, join me in the next and final module of this course to see how your RAG application can go from a simple prototype to a production-ready system."
> [无时间戳] — 下一模块学习邀请：原型到生产级系统的转化

## 相关话题/关键词

- Transformer (Transformer架构)
- LLM (大语言模型)
- Sampling strategies (采样策略)
- Randomness (随机性)
- Benchmarks (基准测试)
- Prompt engineering (Prompt工程)
- Hallucinations (幻觉)
- Performance evaluation (性能评估)
- Agentic components (Agentic组件)
- Fine-tuning (模型微调)
- RAG system (检索增强生成系统)
- Text processing (文本处理)
- Meaning understanding (含义理解)
- Completions generation (补全生成)
- Production-ready (生产就绪)
- Prototype (原型)

## 技术信息
- 字幕字数: 1139
- 字幕字符数: 1139
- 时间戳条目数: 0
- 处理时间: 2026-05-28 14:19:25

---

## Module 4 完整视频列表

| 序号 | 视频标题 | 时长 | 链接 | 视频 ID |
|------|---------|------|------|---------|
| 1 | Module 4 introduction | ~1 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/ffjd0g/module-4-introduction | 1199215 |
| 2 | Transformer architecture | ~8 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/yy164k/transformer-architecture | 1199217 |
| 3 | LLM sampling strategies | ~8 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/8850gm/llm-sampling-strategies | 1199218 |
| 4 | Choosing your LLM | ~8 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/vvs2mn/choosing-your-llm | 1199219 |
| 5 | Prompt engineering: building your augmented prompt | ~5 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/77dr2c/prompt-engineering%3A-building-your-augmented-prompt | 1199220 |
| 6 | Prompt engineering: advanced techniques | ~8 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/jjf7di/prompt-engineering%3A-advanced-techniques | 1199221 |
| 7 | Handling hallucinations | ~7 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/rrngmz/handling-hallucinations | 1199222 |
| 8 | Evaluating your LLM's performance | ~5 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/66p3pm/evaluating-your-llm's-performance | 1199223 |
| 9 | Agentic RAG | ~6 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/aam1f5/agentic-rag | 1199224 |
| 10 | RAG vs. Fine-Tuning | ~6 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/00uskr/rag-vs.-fine-tuning | 1199216 |
| 11 | Module 4 conclusion | ~1 min | https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/558ul7/module-4-conclusion | 1199225 |

---

## Module 4 关键概念总结

### 核心概念
- **Transformer 架构**: 自注意力机制（Self-Attention）处理输入序列
- **LLM 采样策略**: Temperature、Top-p、Top-k 等控制生成多样性
- **Prompt Engineering**: 构建增强提示、上下文学习、Chain of Thought
- **幻觉处理**: 检索增强、置信度阈值、溯源机制
- **Agentic RAG**: LLM 自主决定搜索策略和工具使用
- **RAG vs Fine-Tuning**: 何时用 RAG，何时用微调

---

*此总结由 AI 自动生成，仅供学习参考使用*
