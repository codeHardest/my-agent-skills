# 视频摘要：How Generative AI works

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/dh0t1/how-generative-ai-works
- **时长**: 490秒 (约8分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 15:49:28

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
本视频由吴恩达（Andrew Ng）讲解生成式AI的工作原理，介绍了AI工具全景图中监督学习与生成式AI的关系，解释了大规模监督学习如何为现代生成式AI奠定基础，并深入剖析了大语言模型（LLM）通过预测下一个词来生成文本的核心机制。视频旨在帮助观众理解生成式AI的能力边界和应用场景。

## 核心要点
1. **AI工具二分法**：监督学习和生成式AI是当今AI领域最重要的两大工具，适用于大多数商业用例
2. **监督学习定义**：输入A → 输出B的映射技术，擅长标注任务
3. **监督学习应用广泛**：包括垃圾邮件过滤、在线广告投放、自动驾驶感知、医疗诊断、制造业质检、语音识别、情感分析等
4. **2010-2020年代**：大规模监督学习时代，小模型无法充分利用海量数据提升性能
5. **大模型Scaling Law**：只有训练非常大规模、运行在快速强大计算机上的AI模型，才能持续从更多数据中学习提升
6. **Google Brain经验**：吴恩达领导Google Brain团队时，将“构建超大规模AI模型并喂入大量数据”作为核心任务
7. **大语言模型本质**：基于监督学习，反复预测下一个词（Next Word Prediction）
8. **训练数据量**：LLM训练数据可达数百亿甚至超过一万亿个词汇
9. **Prompt与补全**：输入提示（Prompt）后，LLM生成后续文本补全
10. **随机性与多样性**：相同提示多次运行可能产生不同补全结果
11. **下一个词预测示例**：一句话可转化为多个训练数据点
12. **LLM局限性**：目前只是预测下一个词，下周将介绍让LLM学会遵循指令并保证安全输出的技术
13. **实际应用价值**：LLM已广泛用于写作辅助、信息检索、思维伙伴等日常工作场景
14. **AI不等于魔法**：理解技术原理有助于判断何时可以使用、何时不应依赖生成式AI

## 详细内容（保留所有原始信息）

### 一、AI工具全景图

#### 1.1 AI作为工具集合的概念
视频开篇指出，AI领域存在大量buzz（热议）、excitement（兴奋）和hype（炒作），理解AI的一个有效方式是将AI视为一系列工具的集合。在这些工具中，有两个最为重要：
- **监督学习（Supervised Learning）**：最成熟、最重要的工具，擅长标注任务
- **生成式AI（Generative AI）**：近年来才开始有效运作的新兴工具

#### 1.2 其他AI工具简述
除了上述两大工具外，AI领域还存在其他工具，如：
- 无监督学习（Unsupervised Learning）
- 强化学习（Reinforcement Learning）

但对于大多数商业用例而言，重点关注监督学习和生成式AI这两大工具即可。

---

### 二、监督学习详解

#### 2.1 定义与技术原理
**监督学习（Supervised Learning）**是一种技术，当给定输入A时，能够生成对应的输出B。其核心能力是"标注（Labeling Things）"。

#### 2.2 应用实例详解

| 应用领域 | 输入A | 输出B |
|---------|-------|-------|
| **垃圾邮件过滤** | 电子邮件内容 | 0（不是垃圾邮件）或1（是垃圾邮件） |
| **在线广告投放** | 广告内容+用户信息 | 用户是否会点击该广告的概率 |
| **自动驾驶感知** | 前方路况图片+雷达数据 | 其他车辆的位置标注 |
| **医疗诊断** | 医学X射线影像 | 医学诊断结果 |
| **制造业质检** | 手机等产品的生产线图片 | 是否有划痕或缺陷 |
| **语音识别** | 音频片段 | 文本转录 |
| **情感分析** | 餐厅或商品的评价文本 | 正面或负面情感标注 |

#### 2.3 监督学习的经济价值
在线广告是监督学习最盈利的应用之一。通过向用户展示更相关的广告，为在线广告平台带来可观的收益。

---

### 三、大规模监督学习时代（2010-2020）

#### 3.1 小模型的瓶颈
大约2010年前后，研究者发现一个关键问题：对于许多应用，虽然拥有海量数据，但当训练小型AI模型时，即使喂入更多数据，性能提升也非常有限。

以语音识别系统为例，即使让AI聆听数万甚至数十万小时的音频数据（这已是海量数据），相比只聆听较少音频数据的系统，准确率提升并不显著。

#### 3.2 大模型的突破
在这一时期，越来越多的研究者逐渐意识到：如果训练一个非常大的AI模型（在非常快速、强大的计算机上，拥有大量内存），那么随着数据量增加，性能会持续不断提升。

#### 3.3 Google Brain团队案例
吴恩达分享了自己早年的经历。当他创立并领导Google Brain团队时，设定的核心使命是：**构建非常非常大的AI模型，并喂入大量数据**。这一策略被证明是成功的，推动了Google内部的许多AI进展。

#### 3.4 重要意义
大规模监督学习（Large-scale Supervised Learning）至今仍然重要。正是"使用超大规模模型进行标注"这一理念，为现代生成式AI奠定了基础。

---

### 四、大语言模型（LLM）工作原理

#### 4.1 大语言模型定义
大语言模型（Large Language Model，简称LLM）使用一种技术来生成文本，即**反复预测下一个词（Repeated Next Word Prediction）**。

#### 4.2 Prompt与补全机制
给定一个输入提示（Prompt），例如"I love eating"，LLM可以完成这个句子：
- 第一次运行可能补全为"bagels with cream cheese"（百吉饼配奶油奶酪）
- 第二次运行可能补全为"my mother's meatloaf"（我妈妈的肉饼）
- 第三次运行可能补全为"out with friends"（和朋友外出）

#### 4.3 下一个词预测的原理
LLM通过监督学习来反复预测下一个词。例如，如果AI系统在互联网上读到一句话：
> "My favorite food is a bagel with cream cheese"

这一句话会被转化为多个训练数据点：

| 输入A（给定短语） | 输出B（下一个词） |
|-----------------|-------------------|
| "My favorite food is a" | "bagel" |
| "My favorite food is a bagel" | "with" |
| "My favorite food is a bagel with" | "cream" |
| ... | ... |

通过学习这些输入-输出对，LLM掌握了根据前文预测下一个词的能力。

#### 4.4 训练数据规模
当在海量数据上训练一个非常大型的AI系统时：
- 数据量通常达到**数百亿个词汇**
- 部分情况下甚至超过**一万亿个词汇**

这种大规模训练产生了如ChatGPT这样的大型语言模型，能够根据给定提示生成相应的文本补全。

#### 4.5 未来技术预告
视频指出，目前的描述省略了一些技术细节。具体来说，下周课程将介绍一项重要技术：使LLM不仅能预测下一个词，还能学会遵循指令，并在输出时保证安全性。

---

### 五、生成式AI的实际应用价值

#### 5.1 日常工作场景
许多人（包括观众）已经发现这些模型对日常工作非常有价值：
- **写作辅助**：帮助撰写各类文本
- **信息检索**：查找基础信息
- **思维伙伴**：帮助梳理思路、深化思考

#### 5.2 理解边界的重要性
视频强调，理解生成式AI的工作原理有助于：
- 了解其适用场景
- 判断何时可以使用
- 识别何时不应依赖它

---

## 完整字幕原文
```
The ability of systems
like ChatGPT and Bard to generate text
seems almost magical. They do represent a big step
forward for AI technology. But how does text
generation actually work? In this video, we'll
take a look at what actually underlies the
generative AI technology, and this will hopefully, help you understand
what you can use it for and also when you might
not want to count on it. Let's take a look.
Let's start by looking at where generative AI fits
within the AI landscape. There's a lot of buzz and excitement and also
hype about AI, and I think a useful
way to think of AI is as a collection or
as a set of tools. One of the most
important tools in AI is supervised learning, which turns out to be really
good at labeling things. Don't worry if you don't
know what this means, we'll talk more about
it on the next slide. Second to it that started
to work really well only fairly recently
is generative AI. If you study AI, you may recognize that there
are other tools as well, such as things called unsupervised learning and
reinforcement learning. But for the purposes
of this course, I'm going to touch
briefly on what is supervised learning and then spend most of our time
talking about generative AI. These two, supervised
learning and generative AI, are the two most important
tools in AI today. For most business use cases, you should be fine if
you just not worry about the other tools
than these for now. Before describing how
generative AI works, let me briefly describe what is supervised
learning because it turns out generative AI is built using supervised learning. Supervised learning is
the technology that has made computers very good
when given an input, which I'm going to call A, to generate a
corresponding output, which I'm going to call B. Look at a few examples. Given an email, supervised learning can decide if that email is spam or not. The input A is an email and the output B is
either zero or one, where zero is not
spam and one is spam. This is how spam
filters work today. As a second example, probably the most
lucrative application, not the most inspiring, but lucrative for
some companies that I've ever worked on was
online advertising, where given an ad and some
information about a user, an AI system can
generate an output B corresponding to whether or not you're likely to
click on that ad. By showing slightly
more relevant ads, this drives significant revenue for the online ad platforms. In self-driving cars and in
driver assistance systems, supervised learning
is used to take as input a picture of
what's in front of your car and radar info and label that with the
position of other cars. Give it a medical x-ray, it can try to label that
with a medical diagnosis. I've also done a lot of work in manufacturing defect
inspection where you can have a system take a picture
of a phone as it rolls off the assembly line and check if the phone has any scratches
or other defects, or in speech recognition, the input A would
be a piece of audio and we would label that
with the text transcript, or as a final example, if you run a restaurant or
some other business where occasionally you have reviews written about your
business or your products, supervised learning can
read those reviews and label each one as having either a positive or
a negative sentiment. This is useful for reputation
monitoring of the business. It turns out the
decade of around 2010-2020 was a decade of large-scale
supervised learning. I want to touch on this briefly because it turns out this laid the foundation for
modern generative AI. But what we found
starting around 2010 was that for a
lot of applications, we had a lot of data, but even as we fed it more data, its performance wasn't
getting that much better if we were
training small AI models. This means, for example, if you were building a
speech recognition system, even as your AI listened to tens of thousands or hundreds of thousands
of hours of data, that's a lot of data, it didn't get that much
more accurate compared to a system that listened to only a smaller amount
of audio data. But what more and more researchers started
to realize through this period is if you were to train a very large AI model, meaning an AI model
on very fast, very powerful computers
with a lot of memory, then its performance
as you fed it more and more data will just keep on getting
better and better. In fact, years ago when I started and led the
Google Brain team, the primary mission
that I set for the Google Brain team in
the early days was I said, let's just build
really, really large AI models and feed
them a lot of data. And fortunately, that
recipe worked and ended up driving a lot of AI
progress at Google. Large-scale supervised learning
remains important today, but this idea of very
large models for labeling things is how we
got to generative AI today. Let's look at how
generative AI generates text using a technology
called large language models. Here's one way that
large language models, which I will abbreviate
LLM, can generate text. Given an input like, I love eating, this
is called a prompt, an LLM can then complete this sentence with maybe
bagels with cream cheese, or if you run it a second
time, it might say, my mother's meatloaf, or if you run it a third time, maybe it'll say
out with friends. How does an LLM, a large language model,
generate this output? It turns out that LLMs are built by using
supervised learning. That's a technology to input
A and output a label B. It uses supervised learning to repeatedly predict
what is the next word. For example, if an AI system has read on the Internet
a sentence like, my favorite food is a
bagel with cream cheese, then this one sentence will
be turned into a lot of data points for it to try to learn to predict
the next word. Specifically, given
this sentence, we now have one data
point that says, given the phrase, my
favorite food is a, what do you think
is the next word? In this case, the
right answer is bagel. Also, given my favorite
food is a bagel, what do you think
is the next word? It's with, and so on. This one sentence is turned into multiple inputs A and outputs
B for it to try to learn from where the LLM is learning given a few words to predict what is the next word
that comes after. When you train a very large
AI system on a lot of data, a lot of data for LLMs means hundreds of
billions of words, and in some cases, more than a trillion words, then you get a large
language model like ChatGPT that's given a prompt is very
good at generating some additional words in
response to that prompt. For now, I'm omitting
some technical details. Specifically, next week, we'll talk about a process that makes LLMs not just
predict the next word, but actually learn to
follow instructions and also be safe in what it outputs. But at the heart of LLMs
is this technology that's learned from a lot of data to predict what
is the next word. That's how large
language models work; they're trained to repeatedly
predict the next word. It turns out that many people,
perhaps including you, are already finding
these models useful for day-to-day activities at
work to help with writing, to find basic information, or to be a thought partner to
help think things through. Let's take a look at some
examples in the next video.
```

## 关键引述/重要观点

> "A useful way to think of AI is as a collection or as a set of tools. One of the most important tools in AI is supervised learning, which turns out to be really good at labeling things."

> "Supervised learning is the technology that has made computers very good when given an input, which I'm going to call A, to generate a corresponding output, which I'm going to call B."

> "It turns out the decade of around 2010-2020 was a decade of large-scale supervised learning. I want to touch on this briefly because it turns out this laid the foundation for modern generative AI."

> "If you were to train a very large AI model, meaning an AI model on very fast, very powerful computers with a lot of memory, then its performance as you fed it more and more data will just keep on getting better and better."

> "Let's just build really, really large AI models and feed them a lot of data. And fortunately, that recipe worked and ended up driving a lot of AI progress at Google."

> "Large-scale supervised learning remains important today, but this idea of very large models for labeling things is how we got to generative AI today."

> "Given an input like, I love eating, this is called a prompt, an LLM can then complete this sentence with maybe bagels with cream cheese, or if you run it a second time, it might say, my mother's meatloaf, or if you run it a third time, maybe it'll say out with friends."

> "It turns out that LLMs are built by using supervised learning. That's a technology to input A and output a label B. It uses supervised learning to repeatedly predict what is the next word."

> "When you train a very large AI system on a lot of data, a lot