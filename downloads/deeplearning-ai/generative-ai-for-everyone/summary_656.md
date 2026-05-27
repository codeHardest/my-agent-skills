# 视频摘要：Choosing a model

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/okgpg/choosing-a-model
- **时长**: 379秒 (约6分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 16:06:16

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
本视频由Andrew Ng主讲，探讨了在构建软件应用时如何选择合适的LLM（大语言模型）。视频从模型规模角度分析了不同参数量的模型能力差异，并对比了闭源与开源模型的优缺点，为开发者提供了实用的模型选择指南。课程最后总结了本周内容并预告了后续学习方向。

## 核心要点

1. **模型规模与能力关系**：模型规模可作为评估LLM能力的参考指标，参数越多通常知识越丰富、推理能力越强

2. **十亿参数模型适用场景**：约10亿参数规模的模型擅长模式匹配，具备基础世界知识，适合情感分类等任务

3. **百亿参数模型优势**：100亿参数模型拥有更丰富的世界知识和更强的指令遵循能力，适合构建食品订购聊天机器人

4. **千亿参数模型特点**：1000亿+参数模型具备深厚知识储备和复杂推理能力，适合深度知识任务和头脑风暴

5. **实践导向建议**：LLM开发是高度经验性的过程，建议实际测试多个模型后根据效果选择

6. **闭源模型特点**：通过云API访问，易于集成，最强大模型多为闭源，运行成本相对较低

7. **闭源模型风险**：存在供应商锁定风险，切换LLM供应商需要重新测试所有应用

8. **开源模型优势**：完全控制模型，可本地部署，保障数据隐私和安全

9. **开源模型应用场景**：适合本地部署、边缘设备运行以及对数据隐私有严格要求的场景

10. **模型选择核心原则**：根据具体任务需求选择模型，不必为简单任务使用超大模型

11. **本周课程回顾**：涵盖LLM应用构建、项目生命周期、RAG和微调技术

12. **后续课程预告**：下周将探讨LLM对商业和社会的影响，识别LLM用例，理解AI对工作的影响

## 详细内容（保留所有原始信息）

### 模型规模与能力评估

在构建软件应用时，开发者会发现市场上有许多不同类型的LLM，包括大型和小型模型、开源和闭源模型。选择合适模型的关键维度之一是模型规模。从大致分类来看：

**10亿参数模型**：这类模型在模式匹配方面表现出色，具备基础的世界知识。例如，对于餐厅评论情感分类任务，10亿参数模型完全能够胜任，因为它掌握了食物相关词汇的基本知识。

**100亿参数模型**：相比10亿参数模型，这类模型拥有更丰富的世界知识，了解更多深奥的事实。同时在遵循基本指令方面表现更好。如果要构建食品订购聊天机器人，100亿参数模型配合微调可以很好地完成特定指令的优化。

**1000亿+参数模型**：这类超大规模模型具备非常深厚的世界知识，精通物理、哲学、历史、科学等多领域知识。更重要的是，它们在复杂推理任务上表现更佳。

### 模型选择的实践建议

Andrew Ng强调，LLM开发本质上是高度经验性（实验性）的过程。很难提前准确预测某个LLM的具体表现。因此，实践中的建议是：尝试几个不同的模型进行测试，根据实际结果选择最适合应用的那一个。这种实验方法比理论推演更能找到最优解。

### 闭源模型的特点

**优势方面**：
- 通过云编程接口访问，集成便捷
- 多数最强大的模型采用闭源方式
- 运行成本相对较低，因为大公司在API服务优化上投入大量工作

**劣势方面**：
- 存在供应商锁定（vendor lock-in）风险
- 当前切换LLM的成本不高，但切换供应商需要重新测试所有应用

### 开源模型的特点

**优势方面**：
- 完全控制模型，不依赖第三方
- 无需担心提供商倒闭或弃用模型
- 支持本地部署（on-premises/on-Prem），可在PC、笔记本、手机等设备运行
- 更好地控制数据隐私和数据访问

**实际案例**：Andrew Ng团队在处理电子健康记录（EHR）项目时，由于患者隐私限制无法将数据上传到云提供商，最终选择使用开源模型在本地计算机运行，既保证了隐私安全又完成了任务。

### 本周课程总结

本周课程的核心内容：
1. 使用LLM构建软件应用的方法
2. 生成式AI项目的生命周期
3. RAG（检索增强生成）和微调技术如何提升LLM能力
4. 如何选择合适的模型进行构建

### 后续学习内容预告

**可选视频**：
1. 深入探讨LLM技术原理——如何让模型不仅预测互联网上的下一个词，还能真正遵循指令并保证安全性
2. 前沿技术——如何使用LLM自动决策并配合工具使用

**下周课程重点**：
1. LLM技术如何影响商业和社会
2. 识别对公司有用的LLM用例
3. 系统性理解哪些工作受生成式AI影响更大
4. 个人和雇主如何应对AI带来的工作变化

## 完整字幕原文

```
When using an LLM to build
software applications, you find that there are a lot
of different LLMs out there. Some big ones, some small ones, some open source,
some closed source. How do you choose from all
of these different options? In this video, let's take
a look at some guidelines. One way to estimate how capable an LLM is is to look
at the model size. Loosely, if we look at
models that are, say, in the one billion
parameter range, we'll find that
they're often good at pattern matching and will have some basic knowledge
of the world. If what you want is to classify restaurant
reviews for sentiment, I think a one billion
parameter model would probably be able to do just fine in terms of that type
of pattern matching, with basic knowledge about
food types of words. As you go to a 10
billion parameter model, you find that the models have
greater world knowledge. They just know more esoteric
facts about the world and the models also get better at following basic instructions. So if you want to build
a food order chatbot, a 10 billion parameter model might be okay especially
if you were to fine-tune it to become better
at the types of specific instructions
you want it to follow. Then the very large models, say 100 billion-plus parameters, will tend to have very
rich world knowledge. They'll know a lot of
things about physics and philosophy and history
and science and so on, and they'll be better as
well at complex reasoning. This is why if you're building
a food order chatbot, maybe you don't need the
chatbot to know so much about history and philosophy and all of these other
things under the sun. Some of these models
might be cheap enough to deploy
that it might be okay to use a huge model even
for a food order chatbot. But where I would
definitely tend to use these larger models
would be tasks that involve deep knowledge
or complex reasoning. For example, if I'm looking for a brainstorming partner to
help me think through ideas, I'll often use one of
the larger models. One of the things
you've heard me say earlier though is that
development using LLMs is often a highly empirical, meaning
experimental process. So it's hard to know in
advance exactly what the performance of
a given LLM will be. While I'm sharing some
general guidelines here, in practice it
might be worth just trying a few different
models and testing them. Based on the results you see
from testing a few options, then pick what actually seems to work best
for your application. Another decision you might
have to make is whether to use a closed-source or
an open-source model. Closed-source models
are usually accessible via Cloud programming
interface and I find that many
of them are pretty easy to build into applications. You just have to write a few
lines of code like we saw earlier this week to incorporate them into
software applications. Many of the largest and most
powerful models today are also available only via Cloud
programming interfaces and are closed-source
models and they're also relatively
inexpensive to run because the large companies hosting these models will often have put a lot of work into serving up these API calls inexpensively. A downside is that if you develop using these
closed-source models, there is some risk
of vendor lock-in. Today, the switching costs from one LLM to a different
one is not very high. But there is some
cost to retesting all your problems to
see if they work on a different LLM if you
do switch vendors. In comparison, there are also many open-source models
that are available now. One advantage of using an open-source model is you have full control
over the model. You know you always
have access to that model and don't have
to worry about one of the company providing it were to tire or deprecate the model that you
had built on top of. You can also often run these
models on your own device. So if you want to run it
on-premises or on-Prem, that is, on your own service,
or on a PC or a laptop
or a mobile device, then open-source models may give you a good starting
point to do that. Using an open-source model might also let you
build an application in a way that retains full control over data
privacy and data access. For example, I was recently
working on an application using electronic health records and because of patient privacy, we just could not upload the patient records
to a Cloud provider. As for that project, my team used an open-source
model that we ran on our own computers because
we had to do that to guarantee privacy
of the patient data. To summarize, this
week we talked about software applications
built using LLMs. We saw the life cycle of
generative AI project, as well as techniques
like RAG and fine-tuning that can make
your LLM more capable. Lastly, in this video
we talked about how to choose an appropriate
model to build on. There are also a
couple of optional videos after this one,
one that goes a bit deeper
into the technology that enables LLMs to not just predict the next word
found on the Internet, but actually follow
your instructions and do so in a safe way. The other optional video
talks about some frontier, cutting-edge technology
that can use LLMs to automatically decide what to do and also use tools
along the way. Please feel free to check out
those videos if you wish. Then in the next and final
week of this course we'll take a look at how LLM technology is affecting businesses
and society. For example, how can
you identify LLM use cases that could be
useful for your company? We'll take a look
next week as well at a systematic way to understand
why jobs are more or less affected by
generative AI and how both the individuals
doing the jobs as well as businesses employing people
doing those jobs might navigate the changes that generative AI is
bringing to work. I look forward to
seeing you next week.
```

## 关键引述/重要观点

> "One way to estimate how capable an LLM is is to look at the model size."（评估LLM能力的一种方法是看模型规模）

> "Development using LLMs is often a highly empirical, meaning experimental process. So it's hard to know in advance exactly what the performance of a given LLM will be."（使用LLM的开发通常是高度经验性的过程，很难提前准确预测某个LLM的具体表现）

> "In practice it might be worth just trying a few different models and testing them."（实践中值得尝试几个不同的模型并进行测试）

> "Many of the largest and most powerful models today are also available only via Cloud programming interfaces and are closed-source models and they're also relatively inexpensive to run."（许多最大最强大的模型仅通过云编程接口提供，属于闭源模型，运行成本相对较低）

> "One advantage of using an open-source model is you have full control over the model."（使用开源模型的优势之一是您完全控制模型）

> "Using an open-source model might also let you build an application in a way that retains full control over data privacy and data access."（使用开源模型还可以让您以完全控制数据隐私和数据访问的方式构建应用）

## 相关话题/关键词

- 大语言模型（LLM）
- 模型选择（Model Selection）
- 模型规模（Model Size）
- 参数数量（Parameter Count）
- 闭源模型（Closed-source Models）
- 开源模型（Open-source Models）
- 云API（Cloud API）
- 供应商锁定（Vendor Lock-in）
- 本地部署（On-premises）
- 数据隐私（Data Privacy）
- 微调（Fine-tuning）
- RAG（检索增强生成）
- 生成式AI项目生命周期（Generative AI Project Lifecycle）
- 模型推理能力（Model Reasoning Capability）
- 世界知识（World Knowledge）
- 指令遵循（Instruction Following）
- 电子健康记录（Electronic Health Records）

## 技术信息

- 字幕字数: 5834
- 字幕字符数: 5729
- 时间戳条目数: 0
- 处理时间: 2026-05-27 16:06:16