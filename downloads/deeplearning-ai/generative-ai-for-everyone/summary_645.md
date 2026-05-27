
# 视频摘要：Chatting

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/u12zr/chatting
- **时长**: 419秒 (约6分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 15:55:00

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
本视频探讨了聊天应用（Chatting Applications）的设计与部署，涵盖了通用聊天机器人（如ChatGPT、Bard、Bing Chat）以及企业专用聊天机器人的应用场景。视频详细介绍了客户服务领域的机器人设计模式，包括"人类在环"（Human in the Loop）、机器人辅助人类、以及机器人分流消息等不同自动化程度的设计方案，并分享了企业安全部署聊天机器人的最佳实践流程。

## 核心要点

1. **聊天机器人分类**：聊天机器人分为通用型（如ChatGPT）和专用型（针对特定领域如旅行规划、客户服务、烹饪建议等）

2. **机器人功能类型**：专用聊天机器人可分为仅提供对话建议型和能够执行实际操作的行动型（如自动下单、密码重置）

3. **自动化光谱**：客户服务存在从"仅人工"到"仅机器人"的光谱，中间有多种设计模式

4. **Human in the Loop设计**：机器人生成建议消息，人类服务员审查批准后再发送给客户，降低错误风险

5. **机器人分流（Triaging）**：机器人自动处理简单请求（如退款请求），将复杂问题升级给人工处理

6. **并发处理能力**：人工客服可同时处理4-16个并行对话，机器人辅助可提高管理效率

7. **安全部署流程**：企业通常遵循三阶段部署——内部使用→人类在环检查→直接面向客户

8. **密码重置自动化**：IT部门的密码重置请求量大，机器人可自动处理并发送验证短信

9. **退款请求检测**：自动检测退款请求可处理约10%的聊天流量

10. **内部测试优先**：先让内部团队使用机器人，因其更能容忍和理解错误

11. **风险与流量权衡**：是否采用人类在环取决于机器人说错话的风险和流量大小

12. **LLM三大应用领域**：写作（Writing）、阅读（Reading）、聊天（Chatting）是LLM的三大应用类别

13. **机器人的局限性**：机器人有时会说错话，需要设计模式来防范这些错误

14. **视频预告**：下个视频将讨论LLM能做什么和不能做什么

## 详细内容（保留所有原始信息）

### 一、聊天应用概述

在前两个视频中，我们学习了写作和阅读应用。本视频将探讨聊天应用。除了像ChatGPT、Bard和Bing Chat这样的通用聊天机器人外，许多公司正在考虑是否能够构建专用聊天应用。如果您在一家公司工作，公司有许多员工需要与客户互动或进行某些类型的类似对话，那么您可以考虑是否可以使用专用聊天机器人来帮助处理这些对话。

**常见专用聊天机器人类型包括：**
- 客户服务聊天机器人：帮助处理汉堡订单
- 旅行规划聊天机器人：帮助规划在巴黎的廉价假期
- 职业辅导聊天机器人：提供职业发展建议
- 烹饪建议聊天机器人：提供烹饪指导

### 二、聊天机器人的功能类型

**仅对话型机器人：**
这类机器人能够进行对话并提供建议，但不与公司软件系统交互。

**行动型机器人：**
这类机器人可以与公司软件系统接口，采取实际行动，例如：
- 下达汉堡外卖订单
- 处理密码重置请求
- 发送短信验证码

视频提到了一个具体的例子：IT部门经常收到大量密码重置请求，如果机器人能够处理这些请求，就可以减轻IT部门的工作负担。这种机器人需要被授权在现实世界中执行操作，例如向某人发送短信。

下周的课程将更详细地讨论如何构建不仅仅是生成文本，而是能够实际采取行动的聊天机器人。

### 三、客户服务的自动化光谱

由于许多客户服务组织正在探索聊天机器人的使用，视频分享了不同企业使用的常见设计模式光谱。本节重点讨论基于文本的聊天，而非语音或电话聊天。

**光谱的两端：**

1. **纯人工客服中心**：人类客服代理通过打字来回传递消息，例如"欢迎来到Better Burgers，让我帮您下订单"。

2. **纯聊天机器人**：只有软件直接响应客户，没有任何人工介入。

**中间的常见设计点：**

#### 模式一：机器人支持人类（Bot Supports Humans）

机器人会生成建议消息给人类，但人类服务员会重新查看消息，如果看起来不错就批准，或者在消息实际发送回给客户之前有机会编辑消息。这种设计通常被称为"Human in the Loop"（人类在环），因为作为人类，在消息实际发送回给客户之前，会参与并成为流程的一部分。这是一种降低聊天机器人说错话风险的方法，因为人类可以在消息实际发送回给客户之前进行检查。

#### 模式二：机器人分流人类消息（Bot Triage Messages for Humans）

机器人回答简单的消息，但对于尚未准备好处理的事情升级给人工处理。

视频分享了一个实际案例：团队曾构建了一个自动检测客户是否在询问退款请求的机器人。事实证明，退款请求约占总聊天通话量的10%。通过自动检测并向客户提供说明，只是将约10%的流量从人工代理那里转移走，从而节省了代理大量时间，让人类专注于服务更困难的请求。这种分流是另一种常见设计，帮助人工客服节省时间，只需要专注于他们更擅长处理的更困难的情况。

### 四、并发处理与效率提升

在许多客户服务中心的实际运营中，单个人类可能同时与四、八位客户进行聊天对话，在某些极端情况下甚至可能同时与16位客户聊天。有了机器人支持人类，人类更容易管理更大数量的并行对话。

### 五、安全部署聊天机器人的最佳实践

由于机器人有时会说错话，视频分享了在希望安全部署机器人的公司中，构建和部署机器人通常是什么样的过程。

**三阶段部署流程：**

**第一阶段：内部面向聊天机器人（Internal Facing Chatbot）**

许多时候，会构建一个聊天机器人，但只让自己的团队使用它来回答旅行问题或机器人应该做的任何事情。假设您的内部团队会更有同情心，更能理解错误，如果机器人一时说错了话会更能原谅，这给了您一些时间来评估机器人的行为，也可以避免可能让公司难堪的公开错误。

**第二阶段：人类在环部署（Human in the Loop）**

在看起来足够安全后，常见的下一步是部署人类在环。让人类检查许多消息（在可行的情况下），然后再实际发送给客户。

**第三阶段：直接面向客户（Direct to Customers）**

在这样做了一段时间后，如果看起来机器人的消息通常可以安全发送给客户，您可能会允许机器人直接与客户沟通。

**权衡因素：**

当然，每个业务的具体细节都不同。对于某些应用，由于流量巨大，让人类检查每条消息可能不切实际。但取决于机器人说错话的风险以及流量大小，以及因此人类在环是否可行，这些都是公司用来尝试安全部署机器人的一些设计模式。

### 六、课程总结与展望

总结来说，我们已经看到LLM如何用于写作、阅读和聊天。这三个类别并不意味着是LLM能做什么的详尽列表，但它们只是您可能真正使用它们的一些广泛类别。LLM可以做很多事情，但它们不能做所有事情。在下一个视频中，让我们看看LLM能做什么和不能做什么，更好地了解其局限性。

## 完整字幕原文
```
In the last two videos, we looked at writing and
reading applications. In this video, we'll look
at chatting applications. In addition to the general purpose chat bots
like ChatGPT, Bard, and Bing chat. Many companies are
looking at whether they can build specialized
chat applications. If you're involved
in a company where you have many people interacting with customers or having certain types of conversations
of similar nature, this may be a case where you
can consider whether or not a specialized Chatbot can help with those types
of conversations. Let's take a look. Earlier
we already saw the example of a customer service
Chatbot that might better take orders
for cheeseburger. Another example of a
specialized Chatbot would be one that specializes in
helping you to plan trips. How can vacation
in Paris inexpensively? A bot could be built to have specialized knowledge
about travel. Today, there are
companies exploring a wide range of advice bots. For example, can a bot give you career coaching advice or give
advice on cooking a meal? A large variety of specialized
bots that are really good at answering questions
about one thing are being developed by
different companies today. Some of these bots
are capable of just having a conversation
and giving advice. Some of these bots can also
interface with the rest of a company's software system
and take actions such as to put in an order for a
cheeseburger to be delivered. Another example of
a bot that might be able to take action would be
a customer service chat bot. Where it turns out that many IT departments get tons
of password reset requests. If a bot can take care of that, then it may take some of the workload off
your IT department. A bot like this that
needs to be send a text message to verify identity and actually
help reset the postware. This is a bot that would
need to be empowered, to actually take
action in the world such as to get a text message
to be sent to someone. Next week we'll discuss more how Chatbots like these are builds that don't
just generate text. But we can actually take action. Because of the number of customer service organizations exploring the use of Chatbot, I want to share with you a
range of the spectrum of common design points being
used by different businesses. For this slide, I
want to focus on text based chat rather than
voice or phone based chat. At one end of the
spectrum would be a customer service
center with only humans. You would have human
service agents typing back and
forth messages like, welcome to Better Burgers and let me play
the order for you. At the opposite end of the
spectrum would be Chatbots only where you just have software responding
directly to customers. But between these two
ends of the spectrum of humans typing of the
keyboard or Chatbots only, there are a couple
common design points. One common design
points would be to have bots support humans. In which a bot will generate a suggested message
for a human but the human service
agent will reopen the message and either
approve it if it looks good. Or have a chance to
edit the message before it is actually sent
back to the customer. This type of design is often also called
human in the loop. Because as a human, there's lot in and it's
part of the process before the message actually gets
sent back to your customer. This is a way to
mitigate the risk of the Chatbot maybe
saying the wrong thing. Because a human can
check over it before it's actually sent
back to your customer. In the next video, when we talk about what
LLMs can and cannot do. We'll go over some of the mistakes that LLMs
can sometimes make. This design helps protect
against those mistakes of LLMs. A little bit further on
the automation spectrum would be if you have a bot to
treach messages for humans. Maybe the bot answer
the easy messages but escalate to a human for the things that isn't
quite ready to handle yet. Sometime back, I actually let the team that build
a bot that would automatically detect
if the customer was asking for a refund request. It turns out that
was about 10% of our total chat call volume. By just detecting that
and automatically giving the customer instructions
just routed 10% or so of the traffic away from the human agents and so to save the agents a lot of time and let the humans focus on servicing
the harder requests. But this type of triagging is
another common design to help your human service agents save time and have to focus
only on the harder cases. That they're more uniquely
qualified to handle. In many customer
service centers, a single human may be simultaneously having
chat conversations with four or eight, or in some extreme cases, maybe in 16 customers
at the same time. With bots supporting the humans, it becomes easier for
a human to manage a larger number of
parallel conversations. Given that bots sometimes
say the wrong thing, I want to share with you what building and deploying a bot often feels like in companies that want to do
this in a safe way. Often, companies will start with an internal facing Chatbot. Many times I would
build a Chatbot, but let only my own
team use it to say, answer the questions
about travel or whatever the bot
is supposed to do. Assuming your
internal team will be more sympathetic and more
understanding of mistakes and be more forgiving if the bot says something
wrong at one time, this gives you some time to assess the behavior
of the bot and also avoid public mistakes that could be embarrassing
for the company. After this looks safe enough, a common next step would be to deploy with
human in the loop. To let the human check
over many of the messages. If feasible, before it actually
goes out to the customer. After doing this for a
while if it looks like the bots messages are generally safe to
send to customers, then you might allow the bot to communicate directly
with customers. Of course, the details of
every business differs. For some applications, it
may not be practical to have humans check over every message because of the
sheer volume of traffic. But depending on the
risk of the bot saying the wrong thing as well
as the volume of traffic, and thus whether or not human
in the loop is feasible, these are some of the
design patterns I've seen companies use to try
to deploy bots safely. To summarize, we've
seen how LLMs can be used for writing,
reading, and chatting. These three categories
are not meant to be an exhaustive list
of what LLMs can do, but they are just a
few broad categories of what you might
really use them for. LLMs can do a lot, but they can't do everything. In the next video, let's
take a look at what LLMs can and cannot do and better
understand the limitations. Let's go on to the next video.
```

## 关键引述/重要观点

> "If you're involved in a company where you have many people interacting with customers or having certain types of conversations of similar nature, this may be a case where you can consider whether or not a specialized Chatbot can help with those types of conversations."
> （如果您在一家公司工作，公司有许多员工需要与客户互动或进行某些类型的类似对话，那么您可以考虑是否可以使用专用聊天机器人来帮助处理这些对话。）

> "Some of these bots are capable of just having a conversation and giving advice. Some of these bots can also interface with the rest of a company's software system and take actions such as to put in an order for a cheeseburger to be delivered."
> （这些机器人中有些能够进行对话并提供建议，有些则可以与公司软件系统接口，采取实际行动，例如下一个汉堡外卖订单。）

> "This type of design is often also called human in the loop. Because as a human, there's lot in and it's part of the process before the message actually gets sent back to your customer. This is a way to mitigate the risk of the Chatbot maybe saying the wrong thing."
> （这种设计通常被称为"人类在环"。因为作为人类，在消息实际发送回给客户之前，会参与并成为流程的一部分。这是一种降低聊天机器人说错话风险的方法。）

> "It turns out that was about 10% of our total chat call volume. By just detecting that and automatically giving the customer instructions just routed 10% or so of the traffic away from the human agents and so to save the agents a lot of time and let the humans focus on servicing the harder requests."
> （事实证明，退款请求约占总聊天通话量的10%。通过自动检测并向客户提供说明，只是将约10%的流量从人工代理那里转移走，从而节省了代理大量时间，让人类专注于服务更困难的请求。）

> "Assuming your internal team will be more sympathetic and more understanding of mistakes and be more forgiving if the bot says something wrong at one time, this gives you some time to assess the behavior of the bot and also avoid public mistakes that could be embarrassing for the company."
> （假设您的内部团队会更有同情心，更能理解错误，如果机器人一时说错了话会更能原谅，这给了您一些时间来评估机器人的行为，也可以避免可能让公司难堪的公开错误。）

> "These three categories are not meant to be an exhaustive list of what LLMs can do, but they are just a few broad categories of what you might really use them for. LLMs can do a lot, but they can't do everything."
> （这三个类别并不意味着是LLM能做什么的详尽列表，但它们只是您可能真正使用它们的一些广泛类别。LLM可以做很多事情，但它们不能做所有事情。）

## 相关话题/关键词

- 聊天应用（Chatting Applications）
- 通用聊天机器人（General Purpose Chatbots）
- 专用聊天机器人（Specialized Chatbots）
- 客户服务（Customer Service）
- 旅行规划（Trip Planning）
- 职业辅导（Career Coaching）
- 行动型机器人（Action-taking Bots）
- 密码重置（Password Reset）
- 自动化光谱（Automation Spectrum）
- 人类在环（Human in the Loop）
- 机器人分流（Bot Triage）
- 并发对话管理（Parallel Conversation Management）
- 安全部署（Safe Deployment）
- 内部测试（Internal Testing）
- LLM应用（LLM Applications）
- 错误防范（Error Prevention）
- IT部门支持（IT Department Support）
- 退款处理（Refund Processing）
- 机器人辅助人类（Bot Supports Humans）

## 技术信息

- 字幕字数: 6722
- 字幕字符数: 6605
- 时间戳条目数: 0
- 处理时间: 2026-05-27 15:55:00