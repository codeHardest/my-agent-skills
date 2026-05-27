# 视频摘要：Tool use and agents

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/eveia/tool-use-and-agents
- **时长**: 387秒 (约6分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 16:08:05

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
本视频是DeepLearning.AI"面向所有人的生成式AI"课程第二周的最后一个视频，介绍了大语言模型（LLM）如何使用工具（Tools）以及前沿的智能体（Agents）概念。视频通过餐厅订餐聊天机器人和计算器工具两个实际案例，展示了LLM如何通过输出特定文本格式来触发外部软件系统执行操作；同时探讨了智能体如何让LLM自主决定并执行复杂的多步骤任务序列。

## 核心要点
1. **LLM工具调用机制**：LLM可以输出特定格式的文本（如"order burger for user 9876"）来触发外部软件系统执行实际操作，而非仅生成回复文本。
2. **餐厅订餐案例**：当用户说"send me a burger"时，聊天机器人后台会输出四行文本，其中包含调用餐厅订单系统的指令，但只向用户展示最后一行"OK is on its way"。
3. **用户验证机制**：鉴于LLM输出并非完全可靠，对于涉及信用卡扣款等安全关键的操作，应在执行前弹出验证对话框让用户确认。
4. **计算器工具的必要性**：LLM在精确数学计算方面表现不佳，例如计算8年后100美元以5%利率复利增长的结果时可能出错，因此需要接入外部计算器工具。
5. **计算器工具工作原理**：LLM可以输出"calculator 100 times 1.5^8"这样的格式，被解释为调用外部计算程序进行精确运算，得出$147.74的正确结果。
6. **工具的双重作用**：工具不仅可用于执行操作（Actions），还可辅助推理（Reasoning），显著扩展LLM的能力边界。
7. **智能体概念**：智能体（Agents）是比单次工具调用更高级的探索方向，让LLM自主决定和执行复杂的多步骤任务序列。
8. **智能体研究现状**：智能体技术处于AI研究的前沿，尚未成熟到可用于大多数关键应用的程度，但已展现出巨大潜力。
9. **智能体示例**：一个研究"Better Burger竞争对手"的智能体，可能自主决定需要：搜索竞争对手列表、访问各公司网站、下载首页内容、用LLM总结文本。
10. **智能体局限性**：虽然互联网上有一些智能体的演示案例，但这门技术尚未准备好投入实际生产环境。
11. **未来展望**：如果LLM能够安全、负责任地帮助用户决定执行任务的步骤序列，将是一个令人兴奋的进步。
12. **课程衔接**：视频结尾预告第三周将探讨生成式AI如何影响企业（包括如何发现用例）以及对社会和就业的影响。

## 详细内容（保留所有原始信息）

### 一、LLM工具使用概念

大语言模型不仅能够生成文本回复，还可以通过输出特定格式的文本触发外部软件系统执行实际操作。在餐厅订餐聊天机器人的例子中，当用户说"send me a burger"时，LLM会输出一个包含四行文本的完整响应：
- 第一行：order burger for user 9876 to send to this address（触发餐厅订单系统）
- 第二行：...
- 第三行：...
- 第四行：OK is on its way（显示给用户）

这四行文本中，只有最后一行"OK is on its way"会作为回复发送给用户，而前面包含"order burger"等指令的文本会在后台触发餐厅订单系统，将汉堡送到用户指定的地址。

### 二、用户验证机制的重要性

由于LLM的输出并非完全可靠，在执行可能产生高成本或不可逆后果的操作（如扣款、发送实物商品）时，应该设计验证对话框让用户在最终确认前检查订单是否正确。这种设计能够：
- 防止错误订单造成的经济损失
- 让用户有机会纠正LLM可能产生的理解偏差
- 在安全关键和任务关键的操作中增加人工监督环节

### 三、工具用于推理——计算器工具案例

LLM在精确数学计算方面存在明显不足。例如，当用户询问"如果存入100美元，年利率5%，8年后会有多少？"时，LLM可能给出一个看似合理但错误的答案（如$147）。

解决这一问题的方案是给LLM配备计算器工具。当LLM需要执行精确计算时，它可以输出：
- calculator 100 times 1.5^8

这段文本会被解释为调用外部计算器程序进行运算，正确答案是$147.74。随后这个结果会被回填到文本中，最终向用户提供准确的答案。

通过让LLM调用工具，可以显著扩展其推理和行动执行的能力。

### 四、智能体（Agents）概念

智能体是比单次工具调用更前沿的研究领域。智能体不仅能触发一个工具执行单个操作，还能让LLM自主选择并执行复杂的操作序列。

**智能体的典型工作流程**（以研究"Better Burger竞争对手"为例）：
1. **任务规划**：LLM作为推理引擎，分析任务需要哪些步骤
2. **搜索执行**：触发网络搜索引擎，查询"BetterBurger's competitors"
3. **网站访问**：访问排名前几位的竞争对手网站，下载其首页内容
4. **内容总结**：再次调用LLM，对各网站内容进行总结

### 五、智能体技术的现状与展望

目前智能体技术处于AI研究的前沿，存在以下特点：
- **不成熟**：尚未准备好用于大多数重要应用的生产环境
- **有潜力**：互联网上已有一些令人印象深刻的演示案例
- **需改进**：需要研究人员持续优化才能变得更加可靠和实用
- **负责任**：未来发展方向是让LLM安全、负责任地帮助用户完成任务

### 六、课程内容衔接

本视频是"面向所有人的生成式AI"课程第二周的最后一课。下一周将探讨：
- 生成式AI如何影响企业
- 如何为业务发现生成式AI用例
- 生成式AI对社会的影响
- 生成式AI对就业的冲击

## 完整字幕原文
```
Welcome to
the final video of this week. I'd like to share with you in this video
how LLMs are starting to be able to use tools and then also discuss a cutting
edge topic of agents, which is where we let LLMs try to decide for themselves
what action they want to take next. Let's take a look. In the early example of a food order
taking chatbot, we saw that if you were to say send me a burger,
the bot may reply okay is on its way. In order for a chatbot to enter
the order and send it to you. This is what actually is
happening behind the scenes. The LLM can't just say OK is on
its way because it needs to take some action to actually
send the burger to you. And so an LLM might output
this response order burger for user 9876 to send to this address and then also say the user message
is to say OK, is on its way. An LLM that's been fine tuned to
output text like this will be able to generate an order which in this
case would trigger a software application that passes
the restaurant ordering system a request to deliver a burger
to this user at that address. And what is shown to the user
is not the full LLM output. The full LLM output is all four lines
of text here, but only the final line OK is on its way is what gets
sent to the user as the response. So this is an example of tool used
by an LLM, where detects the LLM outputs can trigger calling a software
system to place a restaurant order. Now, placing an incorrect
order can be a costly mistake. So perhaps a better user interface
would be, before finalizing the order to pop up a verification dialog to let
the user confirm yes or no if you've got the order right before charging
the credit card and sending it to them. And clearly, given that LLM's outputs
are not completely reliable for any safety critical or
mission critical action, it would be a good idea to let a user
confirm the desire action before letting the LLM trigger some
potentially costly mistake by itself. In addition to tools for taking actions,
tools can also be used for reasoning. For example, if you were to prompt an LLM,
how much would I have after eight years if I deposit $100 into bank
account that pays 5% interest? An LLM might generate an answer like
this which sounds plausible, but the number 147 dollars forts is
not actually the right answer. It turns out LLMs having learned
to predict the nick's worth or maybe even instruction tuned,
are not great at precise math. And just as UI might use a calculator
to calculate the right answer to a problem like this, we can also give the LLM a calculator
tool to help it get the right answer. So rather than having the LLM output,
the answer directly. If the LLM were to output this
after compounding and so on, you would have
calculator 100 times 1.5 that's 5% interest rate
compounded to the power of 8. This can be interpreted as command to
call an external calculator program to explicitly compute the right answer,
which turns out to be $147.74. And plug that back into the text to
give the user the correct dollar figure. So by giving LLMs the ability
to call tools in its output, we can significantly extend the reasoning
or the action taking capabilities of LLMs. Tool used today is an important part
of many LLM applications and of course, designers of these applications should
be careful to make sure that tools aren't triggered in a way that causes
harm or causes irreversible damage. Going beyond tools into
a more experimental area, AI researchers have been examining agents
which go beyond triggering a tool to carry out a single action, but
is exploring whether LLMs can choose and carry out complex sequences of actions. There's a lot of excitement and
research on agents, but this is at the cutting
edge of AI research. It is not yet mature enough to count
on for most important applications. But I want to share with you what many
in the AI community are excited about. If you would ask an agent that's built
on top of an LLM help me research better burger's top competitors, then an agent
might use an LLM as a reasoning engine to figure out what are the steps
it needs to carry out to do your task of researching better
burger's competitors. And this reasoning engine LLM might
decide it needs to search for the list of the top competitors,
then visit the website of each competitor, and finally, for each competitor, write
a summary based on the homepage content. And then perhaps by making a sequence
of calls to this reasoning engine, it may figure out that to search the top
competitors it has to trigger a tool to call web search engine on the query
BetterBurger's competitors. And then after that it
may visit the websites of some of the top competitors
to download their homepages. And then additionally call an LLM yet again to summarize the text
that they found on the website. On the internet there have been
some nice demos of agents, but this technology is not really ready for
primetime yet. But perhaps in the future,
as researchers make it better and better, it'll become more useful. And I think that would be an exciting
future if LLMs as a reasoning engine can help decide what's
the sequence of steps to take safely and responsibly, of course,
to help a user carry out a task. Thank you and congrats on making
it to the very end of week two. We have just one more week
to go in this course. Next week, we'll look at how generative
AI is affecting companies, including how you might be able to come up with
generative AI use cases for your business, as well as look at how generative AI is
affecting society and its impact on jobs. I look forward to seeing you next week.
```

## 关键引述/重要观点

> "The LLM can't just say OK is on its way because it needs to take some action to actually send the burger to you."

> "What is shown to the user is not the full LLM output. The full LLM output is all four lines of text here, but only the final line OK is on its way is what gets sent to the user as the response."

> "Given that LLM's outputs are not completely reliable for any safety critical or mission critical action, it would be a good idea to let a user confirm the desire action before letting the LLM trigger some potentially costly mistake by itself."

> "It turns out LLMs having learned to predict the nick's worth or maybe even instruction tuned, are not great at precise math."

> "By giving LLMs the ability to call tools in its output, we can significantly extend the reasoning or the action taking capabilities of LLMs."

> "Tool used today is an important part of many LLM applications and of course, designers of these applications should be careful to make sure that tools aren't triggered in a way that causes harm or causes irreversible damage."

> "AI researchers have been examining agents which go beyond triggering a tool to carry out a single action, but is exploring whether LLMs can choose and carry out complex sequences of actions."

> "There's a lot of excitement and research on agents, but this is at the cutting edge of AI research. It is not yet mature enough to count on for most important applications."

> "On the internet there have been some nice demos of agents, but this technology is not really ready for primetime yet."

> "I think that would be an exciting future if LLMs as a reasoning engine can help decide what's the sequence of steps to take safely and responsibly, of course, to help a user carry out a task."

## 相关话题/关键词

- 大语言模型 (LLM)
- 工具使用 (Tool Use)
- 智能体 (Agents)
- 聊天机器人 (Chatbot)
- 餐厅订单系统 (Restaurant Ordering System)
- 用户验证对话框 (Verification Dialog)
- 计算器工具 (Calculator Tool)
- 精确数学计算 (Precise Math Calculation)
- 复利计算 (Compound Interest Calculation)
- 推理引擎 (Reasoning Engine)
- 任务规划 (Task Planning)
- 网络搜索 (Web Search)
- 内容总结 (Content Summarization)
- 复杂操作序列 (Complex Sequences of Actions)
- 安全关键操作 (Safety Critical Actions)
- 任务关键操作 (Mission Critical Actions)
- 生成式AI (Generative AI)
- 深度学习 (DeepLearning.AI)
- 课程预告 (Course Preview)
- 就业影响 (Impact on Jobs)
- 社会影响 (Social Impact)

## 技术信息
- 字幕字数: 5609
- 字幕字符数: 5528
- 时间戳条目数: 0
- 处理时间: 2026-05-27 16:08:05