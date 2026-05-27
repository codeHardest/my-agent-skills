# 视频摘要：How LLMs follow instructions: Instruction tuning and RLHF

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/dtzpx/how-llms-follow-instructions-instruction-tuning-and-rlhf
- **时长**: 393秒 (约6分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 16:07:41

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
本视频由DeepLearning.AI提供，探讨了大型语言模型(LLM)如何学会遵循人类指令。视频详细介绍了两种核心技术：指令微调(Instruction Tuning)如何让预训练LLM从单纯预测下一个词转变为能够回答问题和遵循指令，以及基于人类反馈的强化学习(RLHF)如何通过训练奖励模型来进一步提升LLM输出的质量，使结果更加有用、诚实和无害。

## 核心要点
1. **预训练LLM的局限性**：仅在互联网文本上训练的大型语言模型擅长预测下一个可能的词，但不一定能直接回答用户问题
2. **问题示例**：询问"法国的首都是什么？"时，模型可能回复"德国的首都是什么？"因为互联网上常见这种问题列表
3. **指令微调定义**：将预训练LLM在"好答案"示例上进行微调，使其学会遵循指令和回答问题
4. **微调数据示例**：
   - 问题-回答对：如"韩国的首都是什么？"→"韩国的首都是首尔"
   - 头脑风暴任务：如"帮我构思波哥大有趣的博物馆"
   - 创意写作：如"写一首关于日本樱花俳句诗"
   - 安全示例：如"告诉我如何闯入诺克斯堡"→"我无法协助，请不要违法"
5. **微调实现方式**：将提示作为输入A，将期望答案的第一个词"当然"、第二个词"以下是"等作为输出B进行训练
6. **微调效果**：LLM学会不只是预测互联网上下一个词，而是真正回答问题和遵循指令
7. **RLHF目的**：通过人类反馈进一步提升答案质量，使LLM输出更有用、诚实和无害( Triple H )
8. **RLHF第一步**：训练答案质量模型，使用监督学习让AI学习对LLM回答进行评分
9. **评分示例**：人类对同一提示的多个回答按helpfulness、honesty、harmlessness评分（如5分、3分、1分）
10. **RLHF第二步**：LLM生成大量回答，由AI模型自动评分，利用评分来调整LLM使其生成更高分的回答
11. **强化学习机制**：分数对应于强化学习的奖励信号，LLM学会生成能获得更高奖励的回答
12. **LLM学习遵循指令的两步法**：第一步指令微调+第二步RLHF
13. **视频定位**：为DeepLearning.AI"Generative AI for Everyone"课程的可选补充视频
14. **后续内容预告**：最后一节可选视频将探讨LLM技术发展的前沿理念

## 详细内容（保留所有原始信息）

### 一、预训练LLM的问题

视频首先回顾了大型语言模型的基本训练方式：在大规模互联网文本上进行预训练，学习预测下一个词。例如，在"My favorite food is bagel with cream cheese"这样的文本上训练，模型能够基于互联网文本的常见模式来预测下一个词。

**问题场景**：当用户用预训练LLM询问"What is the capital of France?"（法国的首都是什么？）时，模型很可能回复"What is the capital of Germany?"（德国的首都是什么？）或"Where is Mumbai?"（孟买在哪里？）"Is Mount Fuji or Mount Kilimanjaro taller?"（富士山和乞力马扎罗山哪个更高？）因为互联网上常见地理问题列表，在"法国的首都是什么？"后面看到"德国的首都是什么？"是合理的。但这并不是用户想要的答案，用户希望得到"法国的首都是巴黎"这样的直接回答。

### 二、指令微调(Instruction Tuning)

为了解决上述问题，视频介绍了**指令微调(Instruction Tuning)**技术。这项技术的基本原理是：拿一个预训练的LLM，在好的问答示例或LLM遵循指令的优质示例上进行微调。

**微调数据示例**：

| 输入提示 | 期望输出 |
|---------|---------|
| "What is the capital of South Korea?" | "The capital of South Korea is Seoul." |
| "Help me brainstorm some fun museums to visit in Bogota" | 相应的博物馆建议列表 |
| "Write a Haiku poem about Japan's cherry blossoms" | 生成的俳句诗 |
| "Tell me how to break into Fort Knox" | "I can't assist with that"或"Please don't break the law" |

关于Fort Knox的示例：Fort Knox是美国存储大量国库黄金的高度安全设施，试图闯入将是非常糟糕的想法。

**微调实现方式**：
- 给定一个提示(如"帮我构思波哥大有趣的博物馆")，将其转化为输入A和输出B
- 输入A就是该提示
- 输出的第一个词应该学习预测"当然"(Sure)
- 第二个词学习预测"以下是"(here are some)
- 依此类推生成完整答案

**微调效果**：当LLM在包含提示和优质回答的数据集上进行微调后，它将学会不只预测互联网上的下一个词，而是回答用户问题和遵循指令。

### 三、RLHF：基于人类反馈的强化学习

视频指出，虽然指令微调已经能够正常工作，但还有一种名为**RLHF(Reinforcement Learning from Human Feedback)**的技术可以进一步提升答案质量。

**企业目标**：许多训练LLM的公司希望LLM给出有用(Helpful)、诚实(Honest)和无害(Harmless)的结果，这被称为**Triple H原则**。

**RLHF第一步：训练答案质量模型**
- 使用监督学习训练AI模型来评估LLM回答的质量
- 示例：给定提示"advise me on how to apply for a job"（给我一些求职建议），让LLM生成多个回答
- 回答1：详细有用步骤（评分5分）
- 回答2：一般性建议（评分3分）
- 回答3：负面消极回复如"it's hopeless, why bother?"（没希望的，何必费心？）（评分1分）
- 人类根据Helpfulness、Honesty、Harmlessness对这些回答进行评分
- 用回答和分数作为监督学习的输入A和输出B，训练AI模型自动评估回答质量

**RLHF第二步：自动化评分与调整**
- 让LLM对大量不同提示生成大量回答
- 使用第一步训练的AI模型自动对每个回答评分
- 根据评分调整LLM，鼓励其生成更高分的回答

**技术原理**：之所以称为"基于人类反馈的强化学习"，是因为分数对应于强化学习中的强化信号或奖励(reward)。通过让LLM学习生成能获得更高分数/更高奖励/更高强化的回答，LLM自动学会生成更有用、诚实和无害的回复。

### 四、LLM遵循指令的完整流程

视频最后总结道，这就是LLM学习遵循指令的方式：
1. **第一步**：指令微调(Fine-tuning)，使LLM能够遵循指令和回答问题
2. **第二步**：RLHF，通过人类反馈的强化学习进一步训练LLM生成更好的答案

视频预告，下一个（也是最后一个）可选视频将探讨LLM技术发展的一些前沿理念。

## 完整字幕原文
```
We've been thinking of LLMs
as having learned from a lot of texts on the Internet
to predict the next word. But when you prompt an LLM, it doesn't just predict the
next word on the Internet, it actually follows
your instructions. How does it do that? In this optional video, we'll talk about the
technique called instruction tuning that
enables LLMs to do that. Then also a technique
called RLHF, reinforcement learning
from human feedback, that has been
instrumental to making LLMs outputs more safe. Let's take a look at what
these techniques do. We've discussed
LLMs as having been pre-trained on a lot
of texts like this, my favorite food is
bagel with cream cheese. An LLM trained on data like this would be good at repeatedly predicting the next word based on what text on the
Internet sounds like. If you were to prompt an
LLM with a question like, what is the capital of France? It is quite possible
that it will reply, what is the capital of
Germany? Where is Mumbai? Is Mount Fuji or Mount
Kilimanjaro taller? Because you do see
lists of questions on the Internet about
say, geography. If you see a web page that says what is the
capital of France, it's actually quite
plausible that what comes after it is what is the
capital of Germany? But this isn't the
answer you want. You wanted to say that the
capital of France is Paris. In order to get an LLM to follow instructions and not
just predict the next word, there's a technique called
instruction tuning, which is basically to take a pre-trained LLM and to
fine tune it on examples of good answers to questions or good examples of the LLM
following your instructions. We may give it a question
response pair like this, what is the capital
of South Korea? And fine tune it given this input prompt to output the capital of
South Korea is Seoul. Or help me brainstorm some
fun museums to visit in Bogota and fine tune it
to an answer like this. Or an instruction like, write a Haiku poem about
Japan's cherry blossoms, and fine tune to generate that. To try to make this safer, we can also include
some examples like, tell me how to break
into Fort Knox. Fort Knox is a very
secure facility in the United States that stores a massive amount of the
US Treasury's gold. Trying to break into Fort Knox
would be a terrible idea. Please, don't anyone
try to do that. But I think a good answer for the LLMs to output will
be something like, I can't assist with that or
please don't break the law. Given a dataset like this, you can then fine tune a pre-trained LLM on a set of good answers
to different prompts. Specifically, given
an example about brainstorming museums in Bogota, we would turn that into a set
of inputs A and output B, where first the input
A will be that prompt, and the first word it
should learn to predict here is sure and the
second word is sure, here are some
suggestions, and so on. When you fine tune an LLM
on a dataset of prompts and good responses that LLM will learn to not just predict the
next word on the Internet, but to answer your questions and to follow your instructions. This will do okay. But it turns out that
there's a technique called reinforcement learning from
human feedback or RLHF, that can improve the
quality of answers further. Many companies
training LLMs want the LLM to give results that are helpful,
honest, and harmless. Sometimes we call
this the triple H, and the technique RLHF is a way to try to
accomplish that. The first step of RLHF is to train an answer quality model. In other words, will you supervised learning to learn
to rate the answers of LLM. For example, given a prompt like advise me on how
to apply for a job, we might have an LLM generate
multiple responses such as, I'm happy to help, here
are some steps to follow, and then have a bunch of
useful steps after that. Or it might say,
just try your best, which is not that hopeful
but not that terrible. Or it might say, it's
hopeless, why bother? That's clearly not
a great response. We would then get humans to help rate these responses
according to how helpful, honest, and harmless
the LLM's output is so that better answers
are given higher scores. Where the first
really helpful answer might get a score of five, the second step's answer might
get an intermediate score, and the final answer, which is terrible, would
get a very low score. If we treat the
responses and scores as the input A and the output B for a supervised
learning algorithm, then we can train an AI model using supervised
learning to take as input response from an LLM and score it according to how
good the response is. The second step of this
RLHF process is to then have the LLM
continue to generate a lot of answers to a lot
of different prompts. We now have this AI model to automatically score
every single response that the LLM has generated, and this can be used to tune the LLM to generate
more responses, they get higher scores. The reason this
technique is called reinforcement learning from
human feedback is because the scores correspond
to the reinforcement or the reward that we're giving the LLM for generating
different answers. By having the LLM learn
to generate answers that merit higher scores or higher rewards or
higher reinforcements, the LLM automatically
learns to generate responses that are more
helpful, honest, and harmless. So that's how an LLM learns
to follow instructions. The first step is
basically fine tuning, where you fine tune it to follow instructions and to
answer questions, and then second is RLHF, reinforcement learning
from human feedback to further train it to
generate better answers. In the last final
optional video, we'll also take a look at some cutting edge ideas in the technology
development of LLMs. Thanks for sticking
with me in this video, and I hope to see you also
in the next optional video.
```

## 关键引述/重要观点

> "But when you prompt an LLM, it doesn't just predict the next word on the Internet, it actually follows your instructions." —— 当你提示LLM时，它不只是在预测互联网上的下一个词，它实际上在遵循你的指令。

> "In order to get an LLM to follow instructions and not just predict the next word, there's a technique called instruction tuning." —— 为了让LLM遵循指令而不只是预测下一个词，有一种叫做指令微调的技术。

> "Many companies training LLMs want the LLM to give results that are helpful, honest, and harmless. Sometimes we call this the triple H." —— 许多训练LLM的公司希望LLM给出有用、诚实和无害的结果。有时我们称之为Triple H。

> "The reason this technique is called reinforcement learning from human feedback is because the scores correspond to the reinforcement or the reward that we're giving the LLM for generating different answers." —— 这项技术之所以被称为基于人类反馈的强化学习，是因为分数对应于我们给LLM生成不同答案的强化信号或奖励。

> "By having the LLM learn to generate answers that merit higher scores or higher rewards or higher reinforcements, the LLM automatically learns to generate responses that are more helpful, honest, and harmless." —— 通过让LLM学习生成能获得更高分数/更高奖励/更高强化的回答，LLM自动学会生成更有用、诚实和无害的回复。

> "Trying to break into Fort Knox would be a terrible idea. Please, don't anyone try to do that." —— 试图闯入诺克斯堡将是一个糟糕的主意。请不要有人尝试这样做。

## 相关话题/关键词

- 大型语言模型 (LLM)
- 指令微调 (Instruction Tuning)
- 基于人类反馈的强化学习 (RLHF)
- 预训练 (Pre-training)
- 下一个词预测 (Next Word Prediction)
- 微调 (Fine-tuning)
- 监督学习 (Supervised Learning)
- 强化学习 (Reinforcement Learning)
- 奖励模型 (Reward Model)
- Triple H (Helpful, Honest, Harmless)
- 有用、诚实、无害 (Helpfulness, Honesty, Harmlessness)
- 提示工程 (Prompting)
- 问题回答 (Question Answering)
- 指令遵循 (Instruction Following)
- 诺克斯堡 (Fort Knox)
- 生成式AI (Generative AI)
- DeepLearning.AI

## 技术信息
- 字幕字数: 5813
- 字幕字符数: 5713
- 时间戳条目数: 0
- 处理时间: 2026-05-27 16:07:41