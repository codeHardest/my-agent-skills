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