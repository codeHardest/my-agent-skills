# 视频摘要：What LLMs can and cannot do

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/a2sc1/what-llms-can-and-cannot-do
- **时长**: 660秒 (约11分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 15:56:58

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
本视频深入探讨了大语言模型（LLM）的能力边界与固有局限。讲者提出了一个实用的思维框架——将LLM视为"刚毕业的大学生"来评估其能力范围，并详细阐述了知识截止日期、幻觉现象、输入输出长度限制、结构化数据处理能力不足以及潜在偏见输出等五大核心局限性，强调理解这些限制对于安全有效地应用生成式AI至关重要。

## 核心要点

1. **思维模型框架**：判断LLM能做什么的有效方法是问自己——"一个刚毕业的大学生，仅凭提示中的指令，能否完成这项任务？"

2. **无记忆特性**：LLM不会记住之前的对话，每次交互都像面对一个全新的"毕业生"，无法通过持续训练来适应特定业务需求

3. **知识截止日期限制**：LLM的知识库冻结在训练时点截止，基于2022年1月数据训练的模型无法知晓之后发生的事件（如《阿凡达：水之道》是2022年票房冠军）

4. **幻觉现象**：LLM会自信地编造不存在的信息，包括虚假的名人引言、虚构的法庭案例等，曾导致律师因提交AI生成的虚假案件引用而被处罚

5. **上下文长度限制**：大多数LLM的提示长度限制在几千词以内，长文档需要分段处理

6. **结构化数据处理劣势**：LLM不擅长处理Excel或Google Sheets中的表格数据，对于房价预测、用户购买行为分析等任务，有监督学习是更优选择

7. **擅长非结构化数据**：生成式AI在处理文本、图像、音频、视频等非结构化数据方面表现最佳

8. **偏见输出风险**：LLM可能反映出训练数据中存在的社会偏见，例如默认外科医生是男性、护士是女性

9. **有害内容风险**：部分LLM可能输出教导不良或非法行为的内容，但主流模型的安全性已在持续改善

10. **局限性认知的重要性**：理解LLM的局限性可降低在不适合的场景中使用它们的风险

## 详细内容（保留所有原始信息）

### 一、思维模型：刚毕业的大学生比喻

讲者提出了一个实用的思维框架来判断LLM能做什么任务。这个框架的核心问题是：**"一个刚毕业的大学生，仅凭提示中的指令，能否完成你想要的 tasks？"**

#### LLM可以较好完成的任务示例：
- 阅读邮件判断是否为投诉
- 阅读餐厅评论判断情感倾向（正面或负面）
- 提供足够的业务背景信息后撰写新闻稿

#### 比喻的关键特征：
- 这位"毕业生"拥有大量从互联网学到的背景知识和常识
- 但他们**没有使用搜索引擎的权限**
- 他们**不了解你或你的业务**
- 每次交互都是**全新的任务**，LLM不会记住之前的对话
- 无法通过时间累积来训练其适应特定业务风格或需求

#### 比喻的局限性：
这是一个**不完美的经验法则**，存在例外情况：
- 有些大学毕业生能做的事，LLM做不到
- 有些LLM能做的事，大学毕业生做不到

讲者强调这是**有用的起点**，后续课程将探讨更强大的技术来扩展LLM的能力边界。

### 二、局限性一：知识截止日期（Knowledge Cutoffs）

#### 核心概念：
LLM对世界的认知**冻结在训练时的时间点**。具体来说：
- 基于2022年1月之前抓取的互联网文本训练的模型
- 无法知晓截止日期之后发生的任何事件

#### 具体案例说明：

**案例1：2022年票房冠军**
- 提问："2022年票房最高的电影是什么？"
- 模型回答：不知道
- 正确答案：《阿凡达：水之道》（Avatar, The Way of Water）

**案例2：LK-99室温超导体**
- 2023年7月有研究实验室声称发现了名为LK-99的室温超导体
- 这一发现在新闻中广泛报道
- 但基于2022年1月数据训练的LLM对此**一无所知**

#### 术语定义：
**知识截止日期（Knowledge Cutoff）**：LLM仅了解截至某一时刻的世界状态，该时刻是模型训练时或互联网文本最后一次被下载用于训练的时间。

### 三、局限性二：幻觉（Hallucinations）

#### 定义：
LLM有时会**凭空编造信息**，我们称之为"幻觉"。

#### 幻觉案例展示：

**案例1：莎士比亚关于碧昂斯的虚假引言**
- 提问："给我三个莎士比亚关于碧昂斯的引言"
- 背景：莎士比亚在碧昂斯出生前几个世纪就去世了
- LLM回应：自信地给出"她的歌声如阳光般闪耀"、"万众敬仰的女王，她最值得被爱"等看似合理的"莎士比亚名言"
- 实际情况：这些全部是幻觉产物

**案例2：虚构的法庭案例**
- 提问："列出在加利福尼亚州审理的与AI相关的案件"
- LLM给出看似权威的案例列表
- 核实结果：
  - 第一个案例（Waymo诉Uber案）：**真实存在**
  - 第二个案例（Ingersoll诉Chevron案）：**无法找到，确为幻觉**

#### 幻觉的危害性：
- LLM以**自信、权威的语气**输出虚假信息
- 容易误导人们认为虚构内容是真实的

#### 严重后果案例：
一位律师使用ChatGPT生成法律案件的文本内容，并提交给法庭，**不知道其中包含大量虚假法庭案例引用**。

- 《纽约时报》标题报道了这场令人尴尬的法庭听证会
- 该律师表示"不理解聊天机器人会误导他"
- 最终该律师因提交包含虚构内容的文件而**受到处罚**

#### 重要警示：
> "如果你将LLM用于具有实际影响的文件，理解这些局限性是极其重要的。"

### 四、局限性三：输入输出长度限制

#### 技术限制：
- LLM的**输入长度**（提示长度）有限制
- LLM的**输出长度**（生成的文本长度）也有限制
- 大多数LLM只能接受**几千词**的提示

#### 实际影响：
- 如果要总结的论文长度超过输入限制，LLM可能**拒绝处理**
- 无法一次性将整篇长论文作为输入

#### 解决方案：
1. **分段处理**：将长文档分成多个部分，每次输入一部分，要求LLM总结该部分
2. **使用更长上下文的模型**：有些LLM支持数万个词的输入长度

#### 技术术语：
**上下文长度（Context Length）**：限制的是**输入+输出的总大小**。讲者表示：
- 很少遇到需要生成大量输出而导致输出长度限制的问题
- 经常遇到需要输入大量上下文信息而触及输入长度限制的情况

### 五、局限性四：结构化数据处理能力不足

#### 定义区分：
- **结构化数据**：表格数据，存储在Excel或Google Sheets等电子表格中
- **非结构化数据**：文本、图像、音频、视频

#### 案例1：房价预测
- 表格包含房屋面积（平方英尺）和价格数据
- 提问："我有一套1000平方英尺的房子，你觉得合适的价格是多少？"
- **LLM不擅长此类任务**

**更优解决方案**：
- 将面积设为输入特征A，价格设为输出特征B
- 使用**有监督学习**来估算价格与面积之间的函数关系

#### 案例2：用户购买行为分析
- 表格包含：网站访问时间、产品报价、是否购买
- 提问：预测购买倾向
- **有监督学习仍是更好的技术选择**

#### LLM的优势领域：
生成式AI**最擅长处理非结构化数据**：
- 文本数据（本课程主要关注）
- 图像数据
- 音频数据
- 视频数据

### 六、局限性五：偏见与有害输出

#### 偏见来源：
- LLM基于互联网文本训练
- 互联网文本**反映了社会中存在的偏见**

#### 性别偏见案例：
- 提示："外科医生走向停车场，拿出了____"
- LLM可能输出："他的车钥匙"（假设外科医生是男性）

- 提示："护士走向停车场，拿出了____"
- LLM可能输出："她的手机"（假设护士是女性）

**实际情况**：外科医生和护士可以是任何性别

#### 应用建议：
> "如果你在可能因偏见造成伤害的应用场景中使用LLM，在如何提示和应用LLM方面要谨慎，确保我们不会助长这些不良偏见。"

#### 有害内容风险：
- 部分LLM可能偶尔输出**有毒或有害的言论**
- 可能教导人们从事不良甚至**非法行为**

#### 改善情况：
- 所有主流大语言模型提供商都在**努力提高模型安全性**
- 大多数模型随着时间推移已变得更加安全
- 通过主要LLM提供商的Web界面，要获得此类有害内容已**越来越困难**

### 七、总结与展望

本视频全面概述了LLM的**能力边界**和**五大核心局限**：

| 局限性类型 | 核心问题 |
|-----------|---------|
| 知识截止日期 | 知识冻结在训练时点 |
| 幻觉 | 可能自信地编造信息 |
| 长度限制 | 输入输出长度受限 |
| 结构化数据 | 不擅长处理表格数据 |
| 偏见与有害输出 | 可能反映社会偏见或输出有害内容 |

#### 课程预告：
- 下周将讨论**生成式AI项目**
- 将介绍更强大的技术来**克服这些局限性**
- 扩展LLM能力，使其超越"刚毕业大学生"的概念
- 后续视频将分享**LLM提示技巧**

## 完整字幕原文
```
Generative AI is an amazing technology,
but it can't do everything. In this video, we'll take a careful
look at what LLMs can and cannot do. We'll start off with what I found to be
a useful mental model for what it can do, and after that, let's look together
at some specific limitations of LLMs. I found that understanding the limitations
can lower the chance that you might get tripped up trying to use them for
something that they're really not good at, so that let's dive in. If you're trying to figure out
what prompting an LLM can do, here's one question that I found to
provide a useful mental framework. Which is I'll ask myself,
can a fresh college grad, following only the instructions in
the prompts, complete the tasks you want? For example, can a fresh college
grad follow instructions to read an email to determine if
an email is a complaint? Well, I think a fresh college
grad could probably do that, and LLM could do that pretty well too. Or can a fresh college grad read
a restaurant review to determine if it's a positive or negative sentiment? I think they could do that quite well too,
and so too, can prompting an LLM. Here's another example, can a fresh
college grad write a press release without any information about the COO or
your company? Well, this fresh college grad
just graduated from college. They only just met you and
don't know anything about you or your business, and so the best they could
do is maybe write a really generic and not quite satisfying
press release like this. But on the flip side, if you were to give
them more context about your business and about the COO, then we can ask, can this fresh college grad write a press
release given the basic relevant context? And I think they may be able to do
that decently well, and so too, can the large language model. When you're picturing an LLM as doing many
of the things that a fresh college grad might be able to do, think of this fresh
college grad as having lots of background knowledge that they know, lots of
general knowledge off the Internet. But they have to complete this task
without access to a web search engine, and they don't know anything about you or
your business. For clarity, this mental model
thought experiment, fresh college grad has to complete a task with no training
specific to a company or your business. And every time you prompt your LLM, the LLM does not actually remember
earlier conversations. And so it's as if you're getting
a different fresh college drag for every single task, so you don't get to
train them up over time on the specifics of your business or
the style you want them to write. This rule of thumb of asking what a fresh
college grad can do is an imperfect rule of thumb, there are things college grads
can do that LLMs cannot and vice versa. But I found this to be
a useful starting point for thinking through what LLMs can and
cannot do. And while we're focused on this slide
on what prompting an LLM can do, next week when we talk about
generative AI projects, we'll talk about some slightly more
powerful techniques that might be able to expand what you can do with generative AI
beyond this fresh college grad concept. Now, let's take a look at some
further specific limitations of LLMs. First, is knowledge cutoffs. An LLM''s knowledge of the world is
frozen at the time of his training. More precisely, a model trained on
Internet data scraped by January 2022, will have no information
about more recent events. So given such a model,
if you were to ask it, what was the highest grossing
film of the year 2022? It would say it doesn't know. Even though now that we're well past 2022,
we know that it was the movie Avatar, The Way of Water that was
the highest grossing film. Around July 2023,
there were claims of research lab having discovered a room temperature
superconductor called LK-99. You may have seen this
picture in some of the news, this claim turned out
not quite to be right. But if you were to ask an LLM about LK-99, even though it's widely covered in
the news, if the LLM learned only from text on the Internet as of January 2022,
it won't know anything about this. So this is called a knowledge cutoff, where the LLM knows things about the world
only up to a certain moment in time. When it was trained, or when text from
the Internet was last downloaded for the LLM's training. A second limitation of LLMs is that
they will sometimes just make things up, and we call these hallucinations. I found that if I ask an LLM to give me
some quotes from well-known people in histories, it will often
make up the quotes. For example, if you ask it, give me three quotes that
Shakespeare wrote about Beyonce. Since Shakespeare lived and
died well before Beyonce, I don't think Shakespeare
said anything about Beyonce. But LLM will confidently give you back
some quotes like her vocals shine like the sun, or all hall the queen,
she is most worthy of love. So these are hallucinated
Shakespearean quotes. Or if you ask it to list court
cases tried in California about AI, it might give authoritative
sounding answers like this. And in this case,
it turns out the first case is real, there was a Waymo versus Uber case, but
I was not able to find an Ingersoll versus Chevron case, and so
the second case is a hallucination. Sometimes LLMs can hallucinate things or
make things up in a very confident, authoritative, sounding tone. And this can mislead people into
thinking that this made-up thing may actually be real. Hallucinations can have
serious consequences. There was a lawyer that unfortunately,
used ChatGPT to generate text for a legal case and actually submitted
to the court, not knowing that he was submitting to the court illegal fouling
with lots of made-up court cases. And in this New York Times headline, we
see in this cringe inducing court hearing. The lawyer who relied on AI said she
did not comprehend that the chat bot could lead him astray, and
this particular lawyer was sanctioned for submitting a co-filing for made-up things. So understanding of limitations is
important if you are using this for documents of real consequence. LLMs also have a technical limitation in
that the input length, that is, the length of the prompt is limited, and so is the
output length of the text it can generate. Many LLMs can accept a prompt of up
to only a few thousand words, and so the total amount of context
you can give it is limited. So if you were asking it
to summarize a paper, and the paper's length is much longer
than this input length limitation, the LLM may refuse to process that input. In this case, you may have to give it
one part of the paper at a time, and ask it to summarize parts
of the paper at a time. Or sometimes you can also find an LLM
with a longer input limit length, some will go up to many
tens of thousands of words. And technically, LLM's have a limitation
on what's called the context length, and the context length is actually
a limit on the total input+output size. When I use LLMs,
I rarely have it generate so much output that I run into limitation
really on the output length. But I do hit input length limits
sometimes if I have many, many thousands of words of
context that I want to give it. Lastly, one major limitation
of generative AI is that they do not currently work well
with structured data. And by structured data
I mean tabular data, like sort of data that you might store in
an Excel, or Google Sheets, spreadsheet. For example, here is a table of home
prices with data on both the size of the house in square feet,
as well as the price of the