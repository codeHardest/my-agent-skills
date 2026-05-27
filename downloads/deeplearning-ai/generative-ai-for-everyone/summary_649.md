# 视频摘要：Using generative AI in software applications

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/ukffi/using-generative-ai-in-software-applications
- **时长**: 347秒 (约5分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 16:01:06

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
本视频由深度学习AI课程(DeepLearning.AI)主讲，讨论了生成式AI在软件应用中的使用方法。通过餐厅评论情感分析的具体案例，对比了传统监督学习方法(需6-12个月开发周期)与基于提示词开发方法(仅需数小时到数天)的巨大差异，展示了生成式AI如何大幅降低AI应用开发的门槛。

## 核心要点
1. 生成式AI可通过网页用户界面或内置于软件应用两种方式使用
2. 生成式AI应用实例包括：回答公司停车政策问题、阅读餐厅评论进行声誉监控、构建订餐聊天机器人
3. 传统监督学习方法构建情感分类器需要：收集数百至数千个标注数据、机器学习工程师编写大量代码、训练AI模型、部署到云服务，耗时6-12个月
4. 基于提示词的开发方法仅需：编写包含指令和评论文本的提示词、一行代码调用大语言模型即可获取响应
5. 传统方法需要雇佣专业AI团队，使用AWS、Google Cloud或Azure等云服务部署模型
6. 监督学习是从输入A映射到输出B的技术，需要标注数据训练模型
7. 提示词开发可实现分钟级到小时级指定提示词，小时级到天级部署模型
8. 生成式AI极大降低了AI应用开发门槛，使数百万普通人能在数天到一周内构建过去需要6-12个月才能完成的应用
9. 重要限制：生成式AI对非结构化数据（如文本、图像、音频）处理效果更好
10. 后续视频提供可选编码练习，让学习者亲自尝试餐厅评论情感分类代码
11. 视频末尾预告将讨论生成式AI项目的生命周期

## 详细内容（保留所有原始信息）

### 1. 生成式AI的应用方式概述
视频回顾了上周讨论的内容：生成式AI可以通过两种方式使用——通过网页用户界面或内置于软件应用。本周将进一步探讨许多使用生成式AI构建的惊人软件应用，并介绍除简单提示之外的技术选项，例如让AI操作你自己的专有文档，而不仅仅是互联网上公开来源学习到的内容。

### 2. 生成式AI应用实例
上周看到的生成式AI应用示例包括：
- 撰写回答，需要访问公司停车政策等信息
- 阅读互联网上餐厅评论，辅助声誉监控
- 构建聊天机器人帮助接收食品订单

虽然这些应用在生成式AI兴起之前就已存在，但生成式AI使构建这些应用变得容易得多，而且在许多情况下效果也更好。

### 3. 餐厅评论声誉监控系统：传统方法 vs 新方法

#### 传统监督学习方法
几年前，如果你想构建一个阅读餐厅评论的系统，需要编写大量的软件代码，需要机器学习工程师来编写。具体过程如下：

**第一步：数据收集**
- 收集数百或数千个数据点
- 示例：评论"best soup dumplings I've ever eaten"（这是我吃过最好吃的汤包），标记为正面评论
- "The colorful table class made me smile"（彩色的餐桌让我微笑），标记为正面
- "not worth the three month wait"（不值得等三个月），标记为负面

**第二步：模型训练**
- 找到AI团队帮助在数据上训练AI模型
- 学习根据不同输入A输出正面或负面

**第三步：模型部署**
- 找到云服务如AWS、Google Cloud或Azure来部署和运行模型
- 输入"best bubble tea I've ever had"（我喝过最好喝的珍珠奶茶），模型识别为正面情感

整个过程通常需要数月时间。

#### 基于提示词的开发方法
使用基于提示词的开发方法，构建情感分类器所需的代码如下：

**第一步：指定提示词**
```
my_prompt = "Classify the following review as having either a positive or negative sentiment." + review_text
```

提示词包含两部分：
- 指令文本："classify the following review as having either a positive or negative sentiment"（将以下评论分类为正面或负面情感）
- 评论文本

**第二步：调用模型**
- 一行代码调用大语言模型获取响应
- 打印响应结果

这就是构建这样一个系统所需的全部代码。

### 4. 开发时间对比

#### 传统方法时间线
| 阶段 | 时间 |
|------|------|
| 获取标注数据（如1000条评论及其正负面标签） | 约1个月 |
| AI团队训练模型 | 约3个月 |
| 部署并确保模型稳定运行 | 约3个月 |
| **总计** | **6-12个月** |

对于优秀的机器学习团队来说，6-12个月的开发周期是构建和部署有价值AI模型的现实时间。

#### 基于提示词的方法时间线
| 阶段 | 时间 |
|------|------|
| 指定提示词 | 分钟到小时 |
| 部署模型 | 小时到天 |

### 5. 生成式AI的民主化影响
这种门槛的降低正在催生大量AI应用的繁荣。过去需要优秀机器学习团队6-12个月才能构建的应用，如今全球数百万人可以在数天或一周内完成构建。

### 6. 重要限制与注意事项
生成式AI在使用时有一个重要的限制条件：正如上周讨论的，生成式AI对非结构化数据（如文本、图像和音频）处理效果更好。尽管存在这个重要的限制条件，在生成式AI基础上构建的应用数量让社区能够做到比以往更多的事情。

### 7. 后续学习安排
下一个可选视频将邀请学习者与讲师一起尝试阅读餐厅评论和分类情感的代码练习。即使你从未写过一行代码也可以尝试，希望能让学习者感受到现在需要编写多么少的代码就能完成这项工作。完成此部分后，将讨论生成式AI项目的生命周期。

## 完整字幕原文
```
Welcome back. Last week we discussed how generative
AI can be used either via a web user interface or be built into a
software application. This week we'll take a look at how many amazing
software applications are being built
using generative AI, and we'll also take a look at some technology
options that go beyond just prompting and that allow you to do much more
with generative AI, for example, having it operate on your own
proprietary documents rather than just
on what is learned from public sources
on the Internet. Let's take a look,
we saw last week a few examples of
generative AI applications, such as writing answers to
questions that may require access to information about your company's parking
policy in this example. Or reading restaurant reviews on the Internet to help with reputation monitoring
or building a chat bot to help
take food orders. It turns out that while
some applications like this did exist and were built before the rise
of generative AI. Generative AI has made building
these applications much easier and in many cases has made them work
much better as well. Let me illustrate
with the example of reading restaurant reviews
for reputation monitoring. A few years ago, if you wanted to build a system for
reading restaurant reviews, it would have taken writing a lot of software code
that looks like this. Pages and pages of
software that you would need machine learning
engineers to write. Specifically the
process of building a restaurant
reputation monitoring review system would
have looked like this. You would use
supervised learning. That's that technology
that maps from inputs A to outputs B and if I were
building the system, I would start by collecting maybe a few hundred or a
few thousand data points. With examples like this, I would have a review, best soup dumplings
I've ever eaten. That sounds delicious. Label that as a positive review. The colorful table
class made me smile. That's positive. Or not
worth the three month wait, that would be a negative review. The process of
building the system would involve first
getting label data, then finding an AI team to help train an AI model on the data, to learn how to
output positive or negative depending on
different inputs A. Then finally, you
might have to find a cloud service like
AWS or Google Cloud or Azure to deploy
and run the model so that when you then input best bubble tea I've ever had, that would hopefully recognizes this as having a
positive sentiment. This process would
often take months. In contrast, if you were to
use prompt based development, this is the code you would need to develop a
sentiment classifier. First, here's how we
specify a prompt in code. My prompt, which I've set
equal to two parts of text. There's the instruction text, classify the
following review as having either a positive or
negative sentiment. Then here is the review text. After specifying
the prompt in code, I just need one line of code to call the large
language model to get a response back
and then I'm going to have it display or
print the response. This is pretty much all the code it takes
to build such a system. In fact, in the next video, I'll share of you an
optional exercise where you can try out
this code yourself. Whereas, with the
traditional approach to building a sentiment classifier, using supervised learning, the timeline for the
project might have been a month to get, say, 1,000 labeled examples with 1,000 reviews and the
positive negative labels. After collecting the data, it might have taken a team, say, three months to
train the AI model on data and then
another three months to deploy it and make sure it's running well and
rugged and robust. I don't know if this seems
like a long time to you, but for many really good machine learning
teams I've worked with, the 6-12 month timeline was
pretty realistic for what it took to build and deploy
a valuable AI model. This worked, and this was very valuable for
a lot of applications, but this just took a long time. In contrast for prompt base AI, this is what it feels like. You can specify a prompt
in minutes or maybe hours, and then deploy the model
in hours or maybe days. There are now many
applications that had previously taken me and very
good machine learning teams, maybe 6-12 months to build
that today I think there are millions of people around
the world that can now build in maybe days or a week. This is fantastic, because this lowering of the barrier
to entry to building such applications is leading to a flourishing of a lot
more AI applications. With one important caveat, which is that, as we
discussed last week, generative AI tends
to work much better for unstructured
data like texts, and images and audio. But with that admittedly
important caveat, the number of applications
built on top of generative AI is just letting the community do much more than ever before. In the next optional video, I'd like to invite you to
try out some codes with me for reading restaurant reviews and
classifying sentiment. It's fine if you've
never seen or written a line of code
before in your life. But I'm hoping to convey
to you how little code is needed to do this now and
let you try it out yourself. I hope you take a look
though also feel free to skip it if you
wish and after that, we'll come back and talk
about what building a generative AI software
project feels like when we talk about
the life cycle of a generative AI project.
```

## 关键引述/重要观点
> "Generative AI has made building these applications much easier and in many cases has made them work much better as well."（生成式AI使构建这些应用变得容易得多，而且在许多 cases has made them work 更好）

> "You would use supervised learning. That's that technology that maps from inputs A to outputs B."（你会使用监督学习，这是从输入A映射到输出B的技术）

> "This process would often take months."（这个过程通常需要数月时间）

> "This is pretty much all the code it takes to build such a system."（这就是构建这样一个系统所需的全部代码）

> "For many really good machine learning teams I've worked with, the 6-12 month timeline was pretty realistic for what it took to build and deploy a valuable AI model."（对于我合作过的许多优秀的机器学习团队来说，6-12个月的时间线是构建和部署有价值AI模型的现实时间）

> "You can specify a prompt in minutes or maybe hours, and then deploy the model in hours or maybe days."（你可以在分钟到小时内指定提示词，然后在小时到天内部署模型）

> "This lowering of the barrier to entry to building such applications is leading to a flourishing of a lot more AI applications."（这种门槛的降低正在催生大量AI应用的繁荣）

> "Generative AI tends to work much better for unstructured data like texts, and images and audio."（生成式AI对非结构化数据如文本、图像和音频的处理效果更好）

> "I'm hoping to convey to you how little code is needed to do this now."（我希望能让你了解现在需要多么少的代码就能完成这项工作）

## 相关话题/关键词
- 生成式AI (Generative AI)
- 软件应用 (Software Applications)
- 监督学习 (Supervised Learning)
- 基于提示词开发 (Prompt-based Development)
- 情感分类器 (Sentiment Classifier)
- 餐厅评论 (Restaurant Reviews)
- 声誉监控 (Reputation Monitoring)
- 大语言模型 (Large Language Model)
- 云服务部署 (Cloud Service Deployment)
- AWS / Google Cloud / Azure
- 非结构化数据 (Unstructured Data)
- AI应用开发 (AI Application Development)
- 机器学习工程师 (Machine Learning Engineers)
- 开发门槛 (Barrier to Entry)
- 民主化AI (Democratized AI)

## 技术信息
- 字幕字数: 5438
- 字幕字符数: 5346
- 时间戳条目数: 0
- 处理时间: 2026-05-27 16:01:06