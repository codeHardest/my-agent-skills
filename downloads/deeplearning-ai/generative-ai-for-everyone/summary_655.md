# 视频摘要：Pretraining an LLM

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/mym30/pretraining-an-llm
- **时长**: 160秒 (约2分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 16:06:01

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
本视频由DeepLearning.AI的生成式AI课程主讲，探讨了何时应该从头预训练自己的大语言模型。视频指出预训练成本高昂，通常建议避免这样做，并分析了BloombergGPT作为专业化领域预训练成功案例的原因。最后建议大多数实际应用采用预训练模型加微调的策略。

## 核心要点
1. 大多数使用的LLM都由大型科技公司预先训练完成
2. 从头预训练LLM成本极高，通常不建议这样做
3. 预训练通用LLM需要数千万美元投入
4. 预训练需要大型专职工程团队
5. 预训练过程需要数月时间和海量数据
6. 许多团队选择开源他们的模型，这对AI社区贡献巨大
7. 预训练应被视为最后的手段（option of last resort）
8. 预训练可能在高度专业化领域且拥有大量数据时才有帮助
9. BloombergGPT是金融领域定制LLM的成功案例
10. BloombergGPT在处理金融文本上优于通用LLM
11. 对大多数实际应用，从预训练模型开始再微调更经济实用
12. 开源模型为我们提供了多种可选择的LLM
13. 下一个视频将讨论LLM大小选择问题

## 详细内容（保留所有原始信息）

### 预训练的现状与挑战
我们使用的大多数LLM都由公司预先训练完成，通常是大型科技公司。那么，什么时候应该预训练自己的模型呢？事实证明这非常昂贵，以至于当有疑问时，答案通常是"可能不要这样做"。让我们深入了解一下。

### 预训练的成本与资源需求
许多团队一直在从互联网上的文本中学习来预训练通用LLM。这些训练超大型语言模型的工作可能需要：
- 数千万美元的成本投入
- 大型专职工程团队
- 数月时间
- 海量数据

### 开源模型的社区贡献
许多团队一直在开源这些模型，这为AI社区做出了巨大贡献。如果您有资源预训练模型，甚至开源它们，请务必为AI做出这种贡献，作者认为这可能非常棒。

### 预训练的适用场景
但对于构建特定应用来说，考虑到从头预训练模型的时间和费用，作者认为这通常是最后的手段。只有在拥有高度专业化领域和大量数据的情况下，预训练才可能有所帮助。

### BloombergGPT案例分析
以彭博社为例，这是一家提供软件和围绕金融服务媒体文章的公司。由于能够获取大量金融文本，彭博社训练了BloombergGPT——这是彭博社定制的、专为金融应用构建的大型语言模型。彭博社报告称，与主要从互联网数据学习的通用LLM相比，该模型在处理金融文本方面表现更好。

### 微调策略的推荐
对于许多实际应用，除非您拥有大量资源和大数据，否则从别人预训练的LLM开始可能更实用。比如一个从大量互联网数据中学习并且已经开源的通用LLM，然后在您自己的数据上进行微调。这通常可以提供相当不错的性能，而且方式更加经济。

### 致谢与展望
作者真诚地感谢那些一直在投入大量资源预训练LLM并将它们开源的团队。事实上，这为我们提供了许多可以选择的LLM。在下一个视频中，我们将探讨您想使用什么规模的LLM的问题，以及在所有不同的LLM中，如何考虑选择不同的模型。

## 完整字幕原文
```
Many of the LLMs we've been using
have been previously trained, or we say pretrained by some company,
often by a big tech company. When should you pretrain your own model? This turns out to be so
expensive that when in doubt, I would say probably don't do it. But let's take a deeper look. Many teams have been pretraining
general-purpose LLMs by learning from text on the internet. These efforts to train very large language
models may cost tens of millions of dollars, need a large, dedicated
engineering team, take many months, and a huge amount of data. Many teams have been open
sourcing such models, and that's been a fantastic
contribution to the AI community. If you have the resources to pretrain
models and maybe even open source them, please, by all means make
that contribution to AI. I think that could be fantastic. But for building a specific application,
given the time and expense of pretraining a model from scratch, I think of this
as often an option of last resort. It could help if you have a highly
specialized domain and a lot of data. For example, Bloomberg is a company
that offers software as well as media articles centered
around financial services. Because of its access to a huge
amount of text on finance, it trained BloombergGPT,
which is Bloomberg's custom built large language model purpose-built for
financial applications. And Bloomberg reported that
compared to general purpose LLMs that had learned
mainly from internet data, this model does quite a bit better
on processing financial text. For many practical applications, unless
you have a huge amount of resources and a huge amount of data, it may be more practical to start with
an LLM that someone else had pretrained. Say, a general purpose LLM that's
learned from a lot of internet data and that someone has open source, and
then to fine tune that to your own data. And that will often give
pretty decent performance, but in a much more economic way. Now, I am sincerely very grateful to
the teams that have been putting a lot of resources into pretraining LLMs on
a lot of text data on the internet and then open sourcing them. And in fact, this gives us many different
LLMs that we could choose from to use. In the next video, we'll actually take a look at the issue
of what size LLM do you want to use? And of all the different LLMs out there, how do you think about
choosing among different ones? Let's go take a look at
that in the next video.
```

## 关键引述/重要观点
> "When should you pretrain your own model? This turns out to be so expensive that when in doubt, I would say probably don't do it." [无时间戳]

> "These efforts to train very large language models may cost tens of millions of dollars, need a large, dedicated engineering team, take many months, and a huge amount of data." [无时间戳]

> "For building a specific application, given the time and expense of pretraining a model from scratch, I think of this as often an option of last resort." [无时间戳]

> "It could help if you have a highly specialized domain and a lot of data." [无时间戳]

> "Bloomberg reported that compared to general purpose LLMs that had learned mainly from internet data, this model does quite a bit better on processing financial text." [无时间戳]

> "For many practical applications, unless you have a huge amount of resources and a huge amount of data, it may be more practical to start with an LLM that someone else had pretrained... and then to fine tune that to your own data." [无时间戳]

> "And that will often give pretty decent performance, but in a much more economic way." [无时间戳]

## 相关话题/关键词
- 预训练（Pretraining）
- 大语言模型（LLM）
- 微调（Fine-tuning）
- 成本高昂
- 开源模型
- 通用LLM
- 领域专业化
- BloombergGPT
- 金融应用
- 互联网数据
- 工程团队
- 资源投入
- 模型选择
- 训练时间
- 数据量

## 技术信息
- 字幕字数: 2443
- 字幕字符数: 2411
- 时间戳条目数: 0
- 处理时间: 2026-05-27 16:06:01