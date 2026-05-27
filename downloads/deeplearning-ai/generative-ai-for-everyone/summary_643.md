# 视频摘要：Writing

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/yp2f3/writing
- **时长**: 323秒 (约5分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 15:52:09

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
本视频是DeepLearning.AI"面向所有人的生成式AI"课程的一部分，深入探讨了大型语言模型（LLM）在写作任务中的应用。课程介绍了如何利用LLM进行头脑风暴、撰写新闻稿、翻译等任务，并强调了提供更多上下文信息对提升输出质量的重要性。视频还分享了提示词迭代改进的实践经验，以及通过"海盗英语"翻译来测试翻译质量的创新方法。

## 核心要点

1. **写作是LLM的核心能力**：由于LLM在训练过程中反复预测下一个词，因此它们在生成文本方面表现出色，这并不令人意外。

2. **提示词驱动写作任务**：大多数写作任务通过相对简短的提示词来生成更长的文本内容。

3. **LLM可作为头脑风暴伙伴**：可以要求LLM生成创意名称（如花生酱饼干的名字）或提出业务增长的ideas。

4. **提供上下文提升输出质量**：给LLM更多背景信息，能生成更具体、更有针对性的内容。

5. **迭代改进是标准做法**：第一次提示不满意是正常的，需要不断修订提示词重新尝试。

6. **翻译是重要应用场景**：LLM在互联网上文本量大的语言翻译方面表现出色，甚至可以媲美或超越专业机器翻译引擎。

7. **低资源语言翻译效果有限**：在互联网上文本较少的语言（称为低资源语言）上，LLM翻译表现相对较差。

8. **领域专家可优化翻译结果**：与目标语言使用者合作可以显著改善翻译质量。

9. **海盗英语测试法**：当团队中没有目标语言专家时，可以将翻译结果转换为"海盗英语"来验证内容的合理性。

10. **Web界面适合写作任务**：许多写作任务可以通过Web用户界面完成，方便快捷。

## 详细内容（保留所有原始信息）

### 一、课程背景与学习目标

本视频是DeepLearning.AI"面向所有人的生成式AI"（Generative AI for Everyone）课程的一部分。在此前的视频中，课程已经介绍了LLM可以完成的三类主要任务：写作（Writing）、阅读（Reading）和聊天（Chatting）。本视频将深入探讨写作任务的应用。

由于大型语言模型在训练时被设计为反复预测下一个词，因此它们在生成文字方面表现出色，这并不令人意外。事实上，许多写作任务可以通过Web用户界面完成，课程希望这个深入探讨写作任务的视频能够立即对学习者有所帮助。

### 二、写作任务的基本方法

对于写作任务，通常的做法是使用相对简短的提示词来驱动LLM生成更长的文本内容。这种方法的核心在于提示词的设计和迭代优化。

课程指出，在使用LLM进行写作时，第一次尝试可能无法获得理想的结果。这是完全正常的现象。如果看到结果不符合预期，应该重新修订提示词并再次尝试。课程将在本周后续视频中详细讨论"编写有效提示词的技巧"。

### 三、头脑风暴应用

课程演示了如何使用LLM作为头脑风暴伙伴。当要求LLM为花生酱饼干想出5个创意名称时，它确实能够生成一些相当有创意的名字，比如"Nutty Nirvana Nibbles"（疯狂开心小食），课程讲师表示自己很愿意吃这样的饼干。

同样地，如果要求LLM想出增加饼干销量的ideas，它会生成一些建议，学习者可以查看这些建议是否对自己有用。这种应用展示了LLM作为创意助手的潜力。

### 四、新闻稿写作示例

课程详细演示了如何使用LLM撰写新闻稿。以撰写宣布新任首席运营官（COO）的新闻稿为例：

**简单提示的结果**：如果只是简单要求LLM"写一篇宣布新任COO入职的新闻稿"，它会生成非常通用的文本，内容包括"公司名称欢迎新高管全名"等模糊信息。

**问题分析**：由于LLM此时只知道"写一篇新闻稿"，它不了解公司的任何信息、CEO的姓名或资质背景，因此最终生成的内容非常笼统。

**改进方法**：如果意识到生成的新闻稿过于通用，这并不是问题。可以决定更新提示词，提供更多信息。可以这样提示："使用以下信息撰写新闻稿——这是COO的个人简介，这是公司名称以及关于公司的一些详情。"这样LLM就能撰写出更加详细、更具洞察力、更加贴合这位CEO加入这家公司的新闻稿。

这个示例说明了"提供更多上下文或背景信息，LLM就能写出更具体、更好的内容"这一核心原则。

### 五、翻译应用

课程还介绍了LLM在翻译任务中的应用。

**翻译能力评估**：某些可以通过Web界面访问的大型语言模型已经具有竞争力，有时甚至比专门的机器翻译引擎更好。这尤其适用于互联网上文本量大的语言，因为LLM有大量数据来学习如何生成该语言的文本。

**低资源语言的局限**：对于在互联网上文本较少的语言（称为低资源语言），LLM的表现通常较差。

**酒店翻译实例**：课程以酒店行业为例进行说明。如果酒店需要将欢迎信息翻译成正式印地语来迎接客人，LLM可以输出类似这样的文本。

然而，课程讲师承认自己不懂印地语，但经过验证发现这个翻译质量只是中等水平。特别是"front desk"这个词，它翻译成了"front of the desk"（前方的桌子），而不是酒店语境中真正的含义——接待处。

如果团队中有印地语使用者（在准备幻灯片时确实有这样的人），他们可以提供改进建议。比如可以指示LLM"将这段内容翻译成正式口语印地语"，然后LLM会更新文本内容，使"front desk"翻译成印地语中表示接待处的词，这是一个更好的翻译。

**海盗英语测试法**：课程分享了一个最近在AI社区中看到的有趣做法。许多从事翻译工作的人需要将文本翻译成自己不会的语言。那么如何判断LLM的翻译是否合理呢？

即使团队中有一位印地语专家，其他不懂印地语的团队成员如何了解翻译的情况呢？

AI社区中多个团队的做法是将文本翻译成"海盗英语"用于测试目的。如果要求LLM将欢迎信息翻译成海盗英语，会得到这样的输出："Ahoy matey, we be hoping you'll relish your time aboard the Oceanview Inn."（啊哈，伙计们，我们希望你能在海景酒店享受您的时光。）课程讲师认为这听起来是相当不错的海盗英语。

这种创意方法展示了在缺乏专业语言支持的情况下，如何验证翻译内容的合理性和可读性。

### 六、总结与下节预告

本视频展示了大型语言模型在写作方面的多种应用，包括头脑风暴、内容创作和翻译等。核心要点包括：提示词设计的重要性、上下文信息的价值、迭代改进的方法，以及创意测试技术的应用。

课程最后预告，下一节视频将进入"阅读"（Reading）部分的学习。

## 完整字幕原文

```
In the last video,
we looked at writing, reading and chatting as three major categories of
tasks that you can get an LLM to do. Given that large language models
were trained to repeatedly predict the next word, maybe it's no surprise that they're pretty
good at writing at generating words. And it turns out that many writing tasks
can be done via a web user interface. So I hope you find this video where
we'll dive more into writing tasks immediately useful. For writing tasks broadly, what we
typically do is start with prompts and use a relatively short prompt to write or
to generate a much longer piece of text. So let's take a look at
some writing applications. I often use the web interface of large
language models as a brainstorming partner. If you ask it brainstorm 5 creative names
for peanut butter cookies, it actually comes up with some pretty creative names
Nutty Nirvana Nibbles, I would eat that. Or if you ask it to brainstorm ideas for
increasing cookie sales, then it comes up with a few ideas and you can take a
look to see if any of these may be useful. You can also use a large language model,
again, maybe the web interface version,
to write some copy for you. Let's start with an example. If you were to ask it to write a press
release announcing the hire of a new COO, a new chief operating officer for your
company, it may come up with a piece of text like this Company Name Welcomes, New
COO's Full Name as, so on and so forth. And this is a pretty
generic press release. When writing a prompt,
you find that if you can give the large language model more context or
more background information, then it will write more specific and
better copy for you. If all that the large language model
sees is this writer a press release, at this point in time, it doesn't
know anything about your company, about the new CEO's name or
their qualifications and so it ends up writing something
very generic like this. If you end up prompting a large action
model like this, it's not a problem. You may realize that you wound up
with a very generic press release and decide to update the prompt
to give it more information. And so if you were to prompt it and
say, use the following information for the press release, this is a COO bio,
this is the name of our company and some details about our company, then
it will write a much more detailed and insightful press release specific
to the CEOs joining this company. I find that when prompting an LLM, I'll
often not get the prompt right the first time, like what we saw just now,
where we had the prompt press release announcing the new hire of COO
without giving any context. And that's totally fine. If you see the result isn't what you want,
just revise the prompt and try again. I'll say more about this
in a later video this week, when we talk about tips for
writing effective prompts. Let's look at one more example. Another writing task that I sometimes
use LLMs for is translation. In fact, some of the large language models
you can access via Web UI are competitive and sometimes even better than
the dedicated machine translation engines already, especially for languages
with a lot of text on the internet. And so where the large language model has
a lot of data to learn how to generate text in that particular language, it
tends to do less well in languages, also called low resource languages with less
text on the Internet in that language. But if you're operating a hotel and you want to translate the welcome message
into formal Hindi to welcome guests, then a large language model may be
able to output text like this for you. Unfortunately, I don't speak Hindi,
I wish I did, but it turns out that this particular translation is only so,
so the word front desk, it translates into the desk at
the front rather than the reception, which is what we mean when we
say the front desk of a hotel. So if you're working with a Hindi speaker,
and I was when preparing the slide, then they may be able to
give you some tips to say, this is some sort of not quite
the best formal Hindi, but you were to tell it to translate
this into formal spoken Hindi. Then it updates this text to make front
desk translate into the Hindi word for reception, which is a much
better translation. Now, here's one fun thing I've
seen recently in the AI community, which is a lot of us that are working with
translation often need to translate text into languages that we
don't speak ourselves. So how can we tell if the large language
model is doing something reasonable? And in fact, even if you have, say,
one Hindi speaker on your team, if other members of the team don't speak Hindi,
how can they figure out what's going on? So what I'm seeing multiple
teams in the AI community do is translate text into pirate English for
testing purposes. And so if you were to prompt a large
language model to translate this into pirate English, you get, ahoy matey, we be hoping you'll relish your
time aboard the Oceanview Inn. That sounds like pretty
good pirate English to me. So that hobby grand worthy
models be used for writing. Let's move on to peepin at Reading House.
```

## 关键引述/重要观点

> "Given that large language models were trained to repeatedly predict the next word, maybe it's no surprise that they're pretty good at writing at generating words."
> （由于大型语言模型在训练时被设计为反复预测下一个词，因此它们在生成文字方面表现出色，这并不令人意外。）

> "For writing tasks broadly, what we typically do is start with prompts and use a relatively short prompt to write or to generate a much longer piece of text."
> （对于写作任务，我们通常的做法是使用相对简短的提示词来驱动生成更长的文本内容。）

> "When writing a prompt, you find that if you can give the large language model more context or more background information, then it will write more specific and better copy for you."
> （在写提示词时，如果你能给予大型语言模型更多的上下文或背景信息，它就能写出更具体、更好的内容。）

> "If all that the large language model sees is this writer a press release, at this point in time, it doesn't know anything about your company, about the new CEO's name or their qualifications and so it ends up writing something very generic like this."
> （如果大型语言模型看到的只是"写一篇新闻稿"，此时它不了解你公司的任何信息、新CEO的姓名或其资质背景，因此最终生成的内容非常笼统。）

> "I find that when prompting an LLM, I'll often not get the prompt right the first time... If you see the result isn't what you want, just revise the prompt and try again."
> （我发现当使用LLM时，我经常不会第一次就把提示词写对... 如果看到结果不符合预期，只需要修订提示词并再次尝试。）

> "Where the large language model has a lot of data to learn how to generate text in that particular language, it tends to do less well in languages, also called low resource languages with less text on the Internet in that language."
> （对于大型语言模型有大量数据学习如何生成该语言文本的语言，它的表现较好；但对于在互联网上文本较少的语言（称为低资源语言），它的表现通常较差。）

> "Ahoy matey, we be hoping you'll relish your time aboard the Oceanview Inn."
> （啊哈，伙计们，我们希望你能在海景酒店享受您的时光。）—— 海盗英语测试翻译示例

## 相关话题/关键词

- 大型语言模型 (Large Language Model, LLM)
- 写作任务 (Writing Tasks)
- 提示词工程 (Prompt Engineering)
- 头脑风暴 (Brainstorming)
- 新闻稿 (Press Release)
- 上下文信息 (Context/Background Information)
- 迭代改进 (Iterative Refinement)
- 翻译 (Translation)
- 低资源语言 (Low Resource Languages)
- 海盗英语测试 (Pirate English Testing)
- Web用户界面 (Web UI)
- 生成式AI (Generative AI)
- 文本生成 (Text Generation)
- 专业术语翻译 (Domain-specific Translation)

## 技术信息

- 字幕字数: 5124
- 字幕字符数: 5053
- 时间戳条目数: 0
- 处理时间: 2026-05-27 15:52:09