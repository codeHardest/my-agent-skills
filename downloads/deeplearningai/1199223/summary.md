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