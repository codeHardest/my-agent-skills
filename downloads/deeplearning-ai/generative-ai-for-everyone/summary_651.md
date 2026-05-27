# 视频摘要：Lifecycle of a generative AI project

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/nakmz/lifecycle-of-a-generative-ai-project
- **时长**: 427秒 (约7分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 16:01:41

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
本视频由Andrew Ng讲授，介绍了构建生成式AI软件应用程序的完整生命周期流程，包括项目 scoping、原型快速开发、内部评估、部署监控等阶段，并详细阐述了该过程的高度经验性和迭代性特点，以及RAG检索增强生成、fine-tuning微调和pretraining预训练等性能优化技术。

## 核心要点

1. **迭代式开发生命周期**: 生成式AI项目遵循"scoping → 快速原型 → 内部评估 → 部署 → 监控 → 持续改进"的循环流程

2. **快速原型构建**: 利用生成式AI构建应用非常便捷，通常1-2天就能完成初始原型，虽然初期质量不高，但能快速进入测试阶段

3. **内部评估重要性**: 通过内部团队使用不同的餐厅评论测试系统，检验系统给出正确响应的频率，发现问题如情感分析错误（将"My pasta was cold"误判为正面情绪）

4. **外部用户发现新问题**: 部署后真实用户可能输入系统未预料的内容，如"My miso ramen tasted like tonkotsu ramen"这类需要特定文化知识才能判断的输入

5. **高度经验性过程**: 构建生成式AI软件是一个高度实验性的过程，需要反复尝试、发现问题、修复错误的循环

6. **提示工程是迭代的**: 编写prompt本身就是一个高度迭代的过程，需要尝试、观察响应、然后改进

7. **RAG检索增强生成**: 一种让大语言模型访问外部数据源的技术，可在后续课程中深入了解

8. **Fine-tuning微调技术**: 允许根据具体任务调整大语言模型的技术

9. **Pretraining预训练**: 指从零开始训练大语言模型的方法

10. **情感分析应用案例**: 餐厅声誉监控系统示例，演示了如何识别评论中的正面/负面情感

11. **客户服务聊天机器人**: 外卖订餐客服聊天机器人示例，展示了对话系统的评估和改进过程

12. **用户输入的不可预测性**: 真实用户会尝试各种意想不到的输入，如询问汉堡的卡路里含量

13. **成本考量**: 使用大语言模型可能比许多人想象的更便宜

14. **系统性错误分析**: 当发现错误时，需要系统性地理解系统是否在某些特定类型的任务上表现不佳

15. **持续监控的必要性**: 部署后需要持续监控大语言模型的响应，确保系统输出符合预期

## 详细内容（保留所有原始信息）

### 一、项目生命周期概述

视频首先介绍了构建生成式AI软件应用程序的完整过程。Andrew Ng指出，生成式AI项目有一个明确的生命周期：首先是scoping阶段，决定软件要做什么；然后是实际实现阶段；接着是内部评估；之后是部署到外部；最后是持续监控性能。

这个过程的核心特点是**高度迭代性**。与传统的软件开发不同，生成式AI应用的开发往往不需要经过冗长的设计阶段，而是可以快速构建原型，然后通过不断的测试和优化来提升质量。

### 二、快速原型构建

视频强调，利用生成式AI构建应用程序非常便捷。根据Andrew Ng的个人经验，他们参与的一些应用程序可以在**一到两天内**完成初始原型构建。虽然这个初始原型在开始时质量并不高，但快速构建的能力使得团队能够立即进入下一阶段的测试和评估。

这种快速迭代的方法与传统软件开发形成鲜明对比。传统开发往往需要大量的前期设计和规划，而生成式AI开发则允许团队在"做中学"，通过实际运行来发现问题和改进方向。

### 三、内部评估阶段

原型构建完成后，接下来是**内部评估阶段**。在这个阶段，团队会：

1. 让内部团队成员使用系统
2. 使用不同的餐厅评论进行测试
3. 观察系统给出正确响应的频率

视频以餐厅声誉监控系统为例进行了说明。系统需要正确识别评论中的情感倾向。例如，对于"My pasta was cold"（我的意大利面是凉的）这条评论，系统错误地将其判断为正面情感。实际上，虽然有时凉的意大利面也很好吃，但在这个语境下，这更可能表达的是负面情感。

通过这种内部测试，团队可以发现系统在特定场景下的表现问题，从而有针对性地进行改进。

### 四、部署与外部监控

当内部评估达到足够的信心水平，确认系统运行良好后，下一步是**部署到外部环境**。然而，Andrew Ng指出，即使经过了严格的内部评估，部署后仍然可能出现各种问题。

外部用户会生成各种各样的输入，其中一些可能是系统之前没有遇到过的。例如，视频中提到的一个例子是：用户可能会写"My miso ramen tasted like tonkotsu ramen"（我的味噌拉面尝起来像豚骨拉面）。对于不熟悉日本料理的人来说，很难判断这是好评还是差评。

实际上，如果你在菜单上点了味噌拉面，你可能不希望它尝起来像豚骨拉面（一种以猪骨汤为基础的拉面）。如果系统将这类评论错误地判断为正面情感，就需要回到内部评估阶段进行系统性的分析和改进。

### 五、高度经验性的开发过程

视频多次强调，**构建生成式AI软件是一个高度经验性（highly empirical）和高度实验性（highly experimental）的过程**。这意味着开发团队需要：

- 反复尝试不同的方法
- 发现问题
- 修复错误
- 重复这个循环

这种经验性过程与提示工程（prompt engineering）的特点高度一致。正如之前课程中提到的，编写提示本身就是一个迭代过程：有一个想法、尝试写提示、观察响应、然后更新想法和提示，如此反复。

### 六、性能优化技术

除了更新提示之外，视频还预告了本周将讨论的其他优化工具：

#### 6.1 RAG（检索增强生成）
RAG即Retrieval Augmented Generation，是一种让大语言模型能够访问外部数据源的技术。例如，当用户询问汉堡的卡路里含量时，系统可以通过RAG技术从餐厅的数据库中检索相关信息，然后给出准确的回答。

#### 6.2 Fine-tuning（微调）
微调是一种允许根据特定任务调整大语言模型的技术。通过微调，可以让通用的大语言模型更好地适应特定的应用场景。

#### 6.3 Pretraining（预训练）
预训练指的是从零开始训练一个大语言模型。这是一个更加底层的操作，通常需要更多的计算资源和数据。

视频强调，这些技术与提示工程一样，都是提升生成式AI系统性能的关键技术，团队可以根据具体需求选择合适的优化方法。

### 七、应用案例一：餐厅声誉监控系统

视频以**餐厅声誉监控系统**为例，完整展示了项目生命周期：

**Scoping阶段**：决定构建一个餐厅声誉监控系统

**原型构建**：快速构建系统初始版本

**内部评估**：使用内部团队和不同类型的餐厅评论测试系统

**发现问题**：
- 系统将"My pasta was cold"错误判断为正面情感
- 实际上这表达的是负面情感

**改进循环**：基于内部发现的问题，返回继续改进系统

**部署与监控**：部署后继续监控，发现如"My miso ramen tasted like tonkotsu ramen"这类需要特定文化知识的复杂判断

### 八、应用案例二：外卖订餐客服聊天机器人

视频还展示了**外卖订餐客服聊天机器人**的生命周期：

**Scoping阶段**：决定构建一个用于接受订单的客户服务聊天机器人

**快速构建**：迅速搭建一个能够接受食物订单的聊天机器人

**内部测试**：让内部团队尝试使用，测试不同场景下的表现

**成功案例**：
- 用户问"Do you have pickles on the cheeseburger"（芝士汉堡有泡菜吗？）
- 系统正确回应并询问用户是否需要

**问题案例**：
- 实际上汉堡确实有蘑菇
- 但聊天机器人错误地回复"I'm sorry, we don't have mushrooms"（抱歉，我们没有蘑菇）

**改进循环**：通过发现这类错误来帮助改进系统

**部署监控**：部署后让客户真实下单，监控大语言模型的响应，确保系统输出符合预期

### 九、用户行为的不可预测性

视频特别指出，在构建了多个生成式AI项目后，Andrew Ng经常会对用户尝试的各种奇特和有趣的事情感到惊讶和高兴。

例如，用户可能会问"How many calories are there in your burger?"（你的汉堡有多少卡路里？）。如果系统最初不知道这个信息，通过发现这个问题，团队可以使用RAG等技术来更新系统，让软件应用程序能够给出正确答案。

这种用户行为的不可预测性是生成式AI应用开发中必须考虑的重要因素。开发团队需要为各种可能甚至奇怪的输入做好准备。

### 十、成本考量

视频最后提到了一些人关心的一个问题：**使用这些托管在互联网上的大语言模型是否真的很昂贵？**

Andrew Ng表示，实际上使用这些大语言模型的**成本可能比许多人想象的更便宜**。这为小型团队和企业提供了更多的可能性，使得他们也能够利用强大的AI能力来构建应用程序。

### 十一、学习建议

视频结束时，Andrew Ng提到，如果观众在具有几名或许多软件开发人员的公司工作，并且有一个很酷的生成式AI应用想法，希望这个视频能够帮助他们了解构建这样一个项目的过程是怎样的。

视频还预告了下一个视频的内容：将分享一些关于实际使用这些大语言模型的成本高低的直观理解。

## 完整字幕原文
```
I'd like to share with you
what the process of building a generative AI
software application feels like. Let's take a look. Here's what the lifecycle of a generative AI project to build a software
application feels like. We would start off by
scoping a project to decide what do we want
this software to do. For example, say you
decide you want to build a restaurant reputation
monitoring system. The next step would be to
actually try to implement it. And given the ease of building AI applications
using generative AI, which you may have seen in the optional video that
came before this one, very often you build a
prototype quite quickly and then plan to over time improve
this software prototype. For some applications
I've worked on, we would build the
initial prototype in one or two days and
that initial prototype, frankly, isn't that
good initially. But building it quickly
lets us then take it into internal evaluation where we might have our own
internal team, different restaurant reviews
and test the system to see how often it is giving
a correct response. Sometimes the internal
evaluation will turn out some examples where it doesn't
give the right result. In this case with, "My pasta was cold," it outputs this as a
positive sentiment and sometimes cold
pasta is delicious but this sounds like a
negative sentiment to me. Based on problems that we
discovered internally, we'll then go back to continue
to improve the system. As you saw last week, writing prompts is a
highly iterative process where you have to try something, see if it works, and
then improve it. And building a generative
AI software application also tends to be a very
iterative process. After a sufficient internal
evaluation to give you confidence that the
systems working well enough, then we would deploy it out in the world and continue to
monitor its performance. And it would not surprise me
if you deploy something and initially external users also generates input that causes the system to make
some mistakes. For example, maybe
a user writes, "My miso ramen tasted like tonkotsu ramen." Is
this good or bad? Well, if you're not familiar with ramen or Japanese cuisine, you may not know is this a
good thing or a bad thing. And if your system rates this
as a positive sentiment, but it turns out that if you're ordering miso
ramen on the menu, you probably don't want it to
taste like tonkotsu ramen, which tastes more like
pork based soup broth. When you find
incorrect responses like this out in the world, you might decide to go back
to internal evaluation. For example, to systematically understand if your system is, say, underperforming on
certain types of cuisine. Or you might decide
to go back to take these learnings to improve the prompt or improve
the system further, assuming you decide that these types of errors
are unacceptable. It turns out that building generative AI software
is a highly empirical, and by that I mean a highly
experimental process. Meaning that we're
repeatedly try something and then
find and fix mistakes. We've already seen how prompting itself is a highly
empirical process, where you would have an
idea, try the prompt, see the element response, then maybe update your idea
and the prompt and go again. But other than
updating the prompts, there are other tools that
we'll talk about this week for improving the performance of
your generative AI system. One tool that we talk
about later this week is RAG or retrieval
augmented generation that gives the large language model access external data sources. We'll also talk later this
week about a technique called fine tuning that
allows you to adapt a large language
model to your task. And then finally,
pretraining models, which refers to training a large language model from scratch. Don't worry about it. If you don't know what
any of these terms mean, we'll go through each of them
in depth later this week. But they're all key
techniques that, in addition to prompting, gives you different ways
to improve the performance of your generative AI
system's performance. Just to walk through
a second example of the life cycle of your
generative AI project, let's look at what's building a system to take food
orders might look like. Say you decide to scope a food order customer service
chatbot to take orders. What you would do, is start
by building the system and quickly throw together a
chatbot to take food orders. Then because we don't know how well this is
doing internally, you might let your
internal team try it out and place different
orders and see how well it does and sometimes
they'll generate good responses like do you have pickles on the cheeseburger and they'll ask
if you want some. And sometimes it will give
an unexpected poor response, such as if you do
have mushrooms on your burgers but for some
reason the chatbot says, I'm sorry, we don't
have mushrooms. Similar to what we saw for the restaurant reputation
monitoring system, it will be by discovering mistakes like these
that helps you to improve the system and
after you're sufficiently confident that this is
safe to deploy externally, you can then deploy it and let customers place real
orders and monitor the large language
models responses to make sure that if it still says anything it
isn't quite supposed to that you can continue to
improve its performance. Having built a number of
generative AI projects, I've often been surprised
and delighted by the strange and wonderful things that the users will try
to do with your system. For example, if a user asks, how many calories are
there in your burger? Initially, the
system may not know. But if you discover this,
you can then update the system using perhaps
a technique called RAG I mentioned just now
and it will go into depth later this week to allow your software application
to give a correct answer. So that's what building a generative AI software
application feels like. And if you work
at a company with a few or a lot
software developers, and if you ever come up
with a cool idea for a generative AI application that your company could build, this hopefully gives
you a sense of what that process of getting
it built might be like. Now, one of the worries I
sometimes hear about is, is it really expensive to use these large language models hosted by companies
on the Internet? It turns out that the use of these large language models is probably cheaper than
many people think. In the next video, I'd
like to share with you some intuitions about how expensive it is or isn't to actually use these
large language models. Let's go on to the next video.
```

## 关键引述/重要观点

> "Here's what the lifecycle of a generative AI project to build a software application feels like. We would start off by scoping a project to decide what do we want this software to do." — 项目生命周期从scoping阶段开始，决定软件要做什么

> "For some applications I've worked on, we would build the initial prototype in one or two days and that initial prototype, frankly, isn't that good initially. But building it quickly lets us then take it into internal evaluation" — 1-2天可完成初始原型，快速构建是生成式AI开发的优势

> "My pasta was cold...it outputs this as a positive sentiment and sometimes cold pasta is delicious but this sounds like a negative sentiment to me." — 情感分析示例：错误地将负面评论判断为正面

> "My miso ramen tasted like tonkotsu ramen...if you're ordering miso ramen on the menu, you probably don't want it to taste like tonkotsu ramen, which tastes more like pork based soup broth." — 需要文化背景知识的复杂情感判断案例

> "It turns out that building generative AI software is a highly empirical, and by that I mean a highly experimental process. Meaning that we're repeatedly try something and then find and fix mistakes." — 生成式AI开发的核心特点：高度经验性和实验性

> "We've already seen how prompting itself is a highly empirical process, where you would have an idea, try the prompt, see the element response, then maybe update your idea and the prompt and go again." — 提示工程本身也是迭代的过程

> "One tool that we talk about later this week is RAG or retrieval augmented generation that gives the large language model access external data sources." — RAG检索增强生成技术介绍

> "We'll also talk later this week about a technique called fine tuning that allows you to adapt a large language model to your task." — Fine-tuning微调技术介绍

> "And then finally, pretraining models, which refers to training a large language model from scratch." — Pretraining预训练技术介绍

> "Having built a number of generative AI projects, I've often been surprised and delighted by the strange and wonderful things that the users will try to do with your system." — 用户行为的不可预测性

> "It turns out that the use of these large language models is probably cheaper than many people think." — 大语言模型使用成本可能比想象更低

## 相关话题/关键词

- 生成式AI项目生命周期 (Generative AI Project Lifecycle)
-