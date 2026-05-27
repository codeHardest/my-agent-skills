# 视频摘要：Reading

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/t6fsb/reading
- **时长**: 472秒 (约7分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 15:53:38

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
本视频由Andrew Ng（吴恩达）讲解大型语言模型（LLM）在阅读任务中的应用。视频介绍了五种主要阅读任务：校对（proofreading）、文章摘要、客服通话摘要、邮件路由分类以及情感分析/声誉监控。Andrew Ng通过个人使用经验和商业应用案例，展示了如何通过提示工程（prompt engineering）让LLM高效处理各种文本阅读任务。

## 核心要点

1. **阅读任务定义**：阅读任务是指输入提示后，生成相似或更短长度的输出，与写作任务（输出通常比输入长）形成对比

2. **校对应用**：LLM可以检测拼写错误、语法错误和语句不通顺，即使作者本人仔细校对过仍能发现问题（如示例中"snuggle"拼写错误和语法问题）

3. **长文章摘要**：当没有时间阅读完整文章时，可使用提示让LLM快速生成摘要（如作者用Erik Brynjolfsson的"The Turing Trap"文章示例）

4. **客服通话摘要系统**：企业可以录音转录客服通话，通过软件应用批量生成摘要，帮助管理者快速了解呼叫中心情况

5. **客户邮件路由**：通过提供具体部门列表（如服装、家居、电子产品等），可以让LLM准确将客户邮件路由到合适部门

6. **提示工程的重要性**：初始提示可能给出不准确的答案（如路由到不存在的"complaints department"），需要通过更新提示（提供明确的部门选项）来解决问题

7. **声誉监控/情感分析**：使用提示让LLM判断评论是正面的还是负面的，通过统计每日正负面评论数量来追踪客户情绪趋势

8. **软件应用场景**：当需要处理大量文本时（如客服通话记录），应该通过软件应用而非手动复制粘贴的方式使用LLM

9. **Erik Brynjolfsson的"Turing Trap"文章**：该文章讨论AI应该增强人类而非替代人类工作，Andrew Ng通过摘要快速回复了作者邮件

10. **迭代优化提示**：构建LLM应用的过程通常是迭代的，初始提示不work时需要根据发现的问题不断调整改进

## 详细内容（保留所有原始信息）

### 1. 校对任务（Proofreading）

校对是Andrew Ng自己在写作时最常使用的阅读任务。他分享了自己的经验：

**使用场景**：
- 写完一段文字后，会自己仔细读三到四遍检查拼写和语法错误
- 即使自己认为已经仔细校对过，LLM仍然能发现遗漏的错误

**实际示例**：
- 提示内容："Proofread the following text, and I find that if you tell it what you want the text before. Here's text intended for a website selling children's stuffed toys, and sometimes I ask you to check for spelling and grammatical errors as well as awkward sentences, and then have it rewrite it with corrections."
- 示例文本：包含一些错误，LLM纠正了"snuggle"的拼写错误和语法问题

**Andrew Ng的个人使用习惯**：
- 写完需要高度准确性的文本后，会用LLM进行校对
- 确保文本没有拼写错误、语法错误和语句不通顺

### 2. 长文章摘要任务

**典型应用场景**：
- 收到很长的文章，没有时间全部阅读
- 需要快速回复作者时

**真实案例 - "The Turing Trap"文章**：
- 来源：Erik Brynjolfsson（斯坦福大学教授，Andrew Ng的合作伙伴）
- 情况：Erik发送了一篇他写的长文章链接，Andrew Ng没有时间在回复前读完
- 解决方案：复制粘贴整篇文章到LLM界面，使用提示快速生成摘要
- 文章核心观点：关于类人AI的优势，以及AI增强（augment）人类而非自动化（automate）的重要性
- 效果：Andrew Ng能够比完整阅读更快地回复邮件

**商业软件应用**：
- 个人使用场景可以直接用网页界面
- 企业应用需要通过软件应用程序实现批量处理

### 3. 客服呼叫中心摘要系统

**系统架构**：
```
客服通话录音 → 语音识别系统 → 文本转录 → LLM摘要生成 → 管理者查看
```

**应用场景**：
- 呼叫中心有许多客服人员与客户通话
- 如果获得录音权限，可以将通话转为文字
- 产生大量文本转录，难以人工全部阅读

**LLM应用方式**：
- 提示："Given a text transcript like this between the customer and an agent, what really happened in this call?"
- 输出：生成简短摘要，如"MP401-27KX was reported as broken, and so on"

**管理者收益**：
- 快速浏览所有摘要
- 发现问题或趋势
- 避免手动逐个阅读大量通话记录

**软件实现必要性**：
- 不适合手动复制粘贴每个对话到LLM网站
- 需要软件应用程序来批量处理

### 4. 客户邮件分析与路由

**应用背景**：
- 早期视频中已有将客户邮件分类为投诉的示例
- 本视频深入讲解如何决定邮件应该路由到哪个部门

**问题分析**：
- **初始提示的问题**：
  ```
  Write a prompt to tell the LLM to read the email and decide which department to route it to
  ```
  - 结果：可能路由到"complaints department"
  - 问题：这个部门可能不存在于组织中
  - 原因：LLM没有足够上下文，不知道公司实际部门名称

- **改进后的提示**：
  ```
  Read the email, choose the most appropriate department to route it to, and choose department only from the following list
  ```
  - 结果：准确路由到"apparel department"（服装部门）
  - 成功原因：提供了具体的部门选择列表

**提示工程要点**：
- 构建LLM应用是迭代过程
- 发现提示不work时，需要更新提示来解决问题
- 提供明确的约束条件（如部门列表）可以显著提高准确性

### 5. 声誉监控与情感分析

**应用定义**：
- 使用LLM构建仪表板，跟踪客户对业务或产品的情感（正面或负面）随时间的变化

**餐厅场景示例**：
- 客户通过在线评论或邮件描述用餐体验
- 提示："Read the following review and classified as having the positive, negative sentiment"

**情感判断标准**：
- 正面情感：食物美味（the food was amazing）、服务友好（service was friendly）
- 负面情感：通过评论内容识别

**仪表板功能**：
- 软件统计每日正面评论数量
- 统计每日负面评论数量
- 实时追踪情感趋势

**预警机制**：
- 正常情况下客户情感保持正面
- 当趋势转向负面（出现更多负面评论）时
- 仪表板发出警报
- 提示管理者可能存在问题需要关注和修复

### 6. 阅读任务的通用原则

**任务识别标准**：
- 思考是否有这样的需求：希望有人阅读一段文本，然后说几句话或给出一些快速指示
- 如果有，这类任务就很适合用LLM作为阅读任务来处理

**视频总结的阅读应用类型**：
1. 校对（Proofreading）
2. 摘要（Summarization）
3. 邮件路由（Email Routing）
4. 餐厅评论情感分析（Restaurant Review Sentiment Analysis）

**与写作任务的关系**：
- 写作任务：输入提示 → 输出通常比输入长
- 阅读任务：输入提示 → 输出通常相似或更短

## 完整字幕原文

```
In the last video, we
looked at writing tasks where you would specify a prompt to the last
large language model, and have it generate a
comparatively longer output than the input prompt. It turns out, is also useful
for many reading tasks, and by that I mean tasks where
you would input a prompt, and then have it
generate usually a similar length or often shorter output
than the input prompt. Let's take a look at
some reading tasks starting with something that
I use myself all the time, which is proof reading. Many times if I'm
writing a piece of text, I will read through it
carefully three or four times myself for spelling
and grammatical errors, and even though I thought I prove read it carefully myself, a line model will still find errors in it that
somehow I had miss. Here's an example of a
prompts that you could try. Proofread the following text, and I find that if you tell it what you want
the text before. Here's text intended for a website selling
children's stuffed toys, and sometimes I ask you
to check for spelling and grammatical errors as well
as awkward sentences, and then have it rewrite
it with corrections. This is a piece of
text with some errors, and the output of the large
language model fixes, snuggle was misspelled and it fixes this little piece
of grammar over here. When I'm writing text myself, that I want to be
quite confident it's free of spelling and
grammatical errors, and sometimes also
awkward sentences, I actually use this myself
to proof read what I write. A second reading task that large language models
are often used for, is to summarize long articles. One of my collaborators, Erik Brynjolfsson, who's
a Stanford professor, once sent me an email
linking to an article that he had written
titled The Turing Trap. I knew it was a good article, but it was a very long
article and I didn't have time to read the whole thing before I responded to his email. I actually use the following
prompt and copy pasted his entire article into an web interface of a
large language model, and had it quickly
generate a summary for me. It turns out this paper
that he had written talks about how human-like
AI offers benefits, but there's a lot to
be done by having AI augment humans
rather than automate. But the point of
Brynjolfsson's article on the Turing Trap was he was advocating that
instead of having AI automate or
replace human work, we should put more
effort into having AI complement or to
augment human work. With a large language model summarizing this long article, I was able to get back on this faster than if I had to read
the entire article myself. By the way, this
is a good article. Eventually I did read the
entire article myself, and I really enjoyed
it, but today, I do sometimes use large
language models to summarize for me things that I don't have
time to read in its entirety. This is a use case that
you could go to one of the web interfaces of
a large language model and use relatively
quickly yourself. Now it turns out there's a software application
version of this too that is taking
off in businesses. Let me illustrate
this with an example. Say you're a manager of a customer service call center where you have many
customer service agents, like this person shown on the
left with the microphone, having phone calls
with customers, like this person
shown on the right. If you have permission to record these phone calls between the
agents and the customers, you can then run the
phone calls through a speech recognition
system to get a text transcript of
the conversation. If you have many customer service agents having
conversations, you end up with a lot
of text transcripts. If you want to review what's going on in
your call center, you probably end up with
too much texts to read. Given a text transcript like this between the
customer and an agent, what really happened
in this call? One use of large language
models would be to have it summarize this
entire conversation and generate a short summary. Like MP401-27KX was reported
as broken, and so on. If you were to take all of these different
text transcripts and have a software application to generate the summaries, then you as a manager of
this can take a quick look at all of these
summaries and just spot if there are any issues, or any trends that you
want to be aware of. A system like this
would be implemented as a software application that
uses a large language model, because it doesn't
really make sense for you or anyone else to copy paste these conversations
one at a time into the website of a large
language model provider. In terms of customer
service interactions, large language models are also used for customer
email analysis. In an earlier video, you saw the example of taking
a customer email, and deciding if it's a
complaint, in this case, no, as well as what department
to route this email. This will be another
software application that uses a large
language model. Let's take a deeper look at how one could build
this application, focusing on the part of deciding what department
to route this email. One thing you could do is
write a prompt to tell the LLM to read the email and decide which department to route it to. You can specify the task
and provide the email. But it turns out that
with a prompt like this, you may find that the algorithm routes it to the complaints
department in this case, which may or may not be a department that exists
in your organization. This would be an example of
where the LLM has been given insufficient context to
know what are the names of the actual departments in your company that it
should choose from. In contrast, if you were to update the prompt as
follows, and say, read the email, choose the most appropriate
department to rouse it to, and choose department only
from the following list. In this case, given the set of choices you
wanted to choose from, routes it to the apparel
department correctly. The process of building
an application using a large language model is
again, not a lot uncommon. To write a prompt that doesn't quite work right the first time, and when you find it, route it to a nonexistent
complaint department, then just update the prompt
and that fixes the problem. One last application
that I want to touch on is reputation monitoring, where you can use
an LLM to build a dashboard to track your
customer sentiments, positive or negative of your business or your
products over time. For example, if you run a restaurant and
occasionally your customers, write online reviews or send your emails describing
their experience, you can then use a
prompt like this, read the following review and classified as having
the positive, negative sentiment,
to have it decide automatically if each review
was positive or negative. In this case, if the food was amazing or service a friendly, that would be classified as
having a positive sentiment. Then by having software count the number of
positive reviews per day, as well as the number of
negative reviews per day, you can build a dashboard
that tracks per day, all the time, how the
sentiments are trending. Looks like the customer
sentiment is pretty positive, but if ever it starts
trending negative like this, with more negative reviews, then this dashboard
can alert you to that maybe something's happening that we should pay attention to, and see if there's something we need to fix at
the restaurant. In this video, we looked at a number of reading
applications, including proof
reading, summarization, email routing, restaurant
review, sentiment analysis. If you can think of a
task where you wish you had someone that could
read a piece of text, and just say a few
things or give a few quick indications of what was in that piece of text, that could be a
good candidate for a reading task to get
an LLM to do for you. Next, let's go onto
the next video to take a look at chatting task.
```

## 关键引述/重要观点

> "Writing tasks where you would specify a prompt to the last large language model, and have it generate a comparatively longer output than the input prompt. It turns out, is also useful for many reading tasks, and by that I mean tasks where you would input a prompt, and then have it generate usually a similar length or often shorter output than the input prompt."

> "Many times if I'm writing a piece of text, I will read through it carefully three or four times myself for spelling and grammatical errors, and even though I thought I prove read it carefully myself, a line model will still find errors in it that somehow I had miss."

> "Proofread the following text, and I find that if you tell it what you want the text before. Here's text intended for a website selling children's stuffed toys, and sometimes I ask you to check for spelling and grammatical errors as well as awkward sentences, and then have it rewrite it with corrections."

> "The Turing Trap article... advocates that instead of having AI automate or replace human work, we should put more effort into having AI complement or to augment human work."

> "A system like this would be implemented as a software application that uses a large language model, because it doesn't really make sense for you or anyone else to copy paste these conversations one at a time into the website of a large language model provider."

> "The process of building an application using a large language model is again, not a lot uncommon. To write a prompt that doesn't quite work right the first time, and when you find it, route it to a nonexistent complaint department, then just update the prompt and that fixes the problem."

> "If you can think of a task where you wish you had someone that could read a piece of text, and just say a few things or give a few quick indications of what was in