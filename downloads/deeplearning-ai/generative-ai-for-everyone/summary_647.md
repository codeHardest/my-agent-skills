# 视频摘要：Tips for prompting

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/yc58w/tips-for-prompting
- **时长**: 387秒 (约6分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 15:58:11

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
本视频由DeepLearning.ai的Andrew Ng主讲，分享了与大型语言模型（LLM）交互时的三个核心提示工程技巧：详细具体、引导模型思考答案、以及实验迭代。视频强调提示工程是一个高度迭代的过程，不需要追求完美的初始提示，而是通过不断尝试和调整来获得理想结果。课程还特别提醒用户注意隐私保护和信息验证的重要性。

## 核心要点
1. **详细具体原则**：提供足够的上下文和背景信息，帮助LLM理解任务需求，避免模糊指令
2. **新毕业生类比**：将LLM比作新入职的大学毕业生，需要充分背景信息才能有效完成任务
3. **引导模型思考**：通过分步骤指令帮助模型按预期流程生成答案，提高输出质量
4. **迭代优化过程**：提示工程不是寻找完美初始提示，而是通过反复尝试调整逐步接近目标
5. **快速启动策略**：不必过度思考初始提示，先快速尝试再根据结果优化
6. **渐进式澄清**：从简单提示开始，逐步添加具体要求（如语法纠错、语气调整等）
7. **不会搞坏互联网**：轻微措辞不当的提示不会造成严重后果，鼓励大胆尝试
8. **隐私保护警示**：高度机密信息应谨慎处理，需了解LLM提供商的数据政策
9. **信息验证必要性**：AI可能生成虚假事实，使用前需自行核实
10. **实用场景示例**：包含申请项目邮件写作、猫玩具命名等具体案例
11. **步骤指令效果**：清晰的步骤指引能显著提高LLM输出符合预期的概率
12. **课程实践建议**：鼓励观众访问LLM提供商的Web界面亲自尝试
13. **后续内容预告**：下周将讨论如何使用LLM构建项目

## 详细内容（保留所有原始信息）

### 一、视频开场与背景

视频开头，Andrew Ng分享了与大型语言模型进行提示交互的实用技巧。他指出，这些技巧对于正在使用LLM提供商Web用户界面的用户来说可以直接应用，同时也适用于使用LLM构建软件应用的开发者。整个视频将围绕三个主要提示工程技巧展开。

### 二、第一技巧：详细具体（Be Detailed and Specific）

#### 核心概念
Andrew Ng用"新毕业生类比"来说明这一原则。他强调，在使用LLM时，需要确保模型拥有足够的上下文或背景信息来完成特定任务。就像新入职的大学毕业生需要充分的工作背景才能有效完成任务一样，LLM也需要足够的背景信息才能给出符合期望的回答。

#### 实际案例：项目申请邮件
**场景描述**：用户希望LLM帮助撰写一封邮件，请求被分配到法律文档项目。

**问题分析**：如果仅仅给出"帮我写一封邮件请求被分配到法律文档项目"这样的提示，LLM实际上并不知道如何撰写一封有说服力的邮件来支持用户的申请。

**解决方案**：需要提供更多背景信息，包括：
- 用户已经申请了法律文档项目的工作
- 用户在处理法律文档方面有相关经验
- 期望LLM生成准确的文本和专业的语气

这样能为LLM提供更相关的上下文，帮助撰写出更适合请求分配到该项目的邮件。

#### 进一步优化：详细描述期望任务
除了提供背景信息，还应该详细描述期望的任务。例如：

**初步提示**："帮我写邮件"

**优化提示**："撰写一段文字，解释为什么我的背景使我成为这个项目的强有力候选人，强调我的资质申请。"

这种类型的提示不仅能为LLM提供足够的上下文，还能清晰地传达用户想要的具体操作，更有可能获得理想的结果。

### 三、第二技巧：引导模型思考答案（Guide the Model to Think Through Its Answer）

#### 基础案例：猫玩具命名
Andrew Ng以一个简单的任务为例：如果让LLM"为新猫玩具头脑风暴5个名字"，它实际上可以做得相当不错。

#### 复杂场景：带要求的命名
但如果用户有特定要求——比如想要押韵的猫玩具名称并带有相关表情符号——就需要更具体的指导。

#### 步骤化指令示例
Andrew Ng分享了他会尝试的方法：

**第一步**：头脑风暴5个与猫相关的快乐词汇

**第二步**：为每个词汇想出一个押韵的名字

**第三步**：为每个玩具名称添加一个有趣的相关表情符号

#### 实际效果展示
使用这样的提示，用户可能会得到如下结果：
- 首先生成：purr（咕噜声）、whisker（胡须）等词汇
- 然后生成押韵名称：purr-twiri、whisker-whisper、feline-beeline等
- 最后添加有趣的表情符号

#### 原理说明
Andrew Ng指出，如果你已经有一个可以引导模型到达期望答案的流程，给出清晰的分步骤指令会非常有效。这种方法让LLM能够按照预定的逻辑路径思考，从而生成更符合预期的输出。

### 四、第三技巧：实验迭代（Experiment and Iterate）

#### 对完美提示的反思
Andrew Ng提到，他在社交媒体上看到很多文章，标题类似"每个人都必须知道的20个提示"或"帮助你职业发展的17个提示"。但他认为，不存在对每个人都适用的完美提示。

#### 真正的有效方法
Andrew Ng发现，拥有一个能够生成期望结果的提示写作流程更为有用。

#### 实践中的迭代过程
当Andrew Ng自己使用LLM进行提示时，他经常：
1. 从简单尝试开始，比如："帮我重写这个"
2. 如果不满意结果，他会澄清说："纠正其中的语法和拼写错误"
3. 如果仍然没有给出完全想要的结果，他会进一步澄清："纠正语法和拼写错误，并用适合专业简历的语气重写"

#### 核心观点
提示工程的过程通常不是从完美的提示开始的，而是从某个起点开始，然后：
- 查看结果是否令人满意
- 如果不满意，知道如何调整提示
- 逐步接近想要的答案

#### 迭代过程的可视化理解
Andrew Ng将提示工程过程理解为：
1. 你对LLM要做什么有一个想法
2. 将这个想法表达为提示
3. LLM根据提示给出回应
4. 结果可能符合也可能不符合预期
5. 如果符合，任务完成
6. 如果不符合，初始回应帮助你：
   - 完善你的想法
   - 修改提示
   - 迭代几次直到达到想要的结果

#### 快速启动策略
在开始提示时，Andrew Ng会：
- 尽量做到清晰具体
- 但为了节省时间，通常从较短的提示开始
- 这个提示可能不如期望的那么具体，但能快速启动

收到结果后：
- 如果不是想要的，思考为什么结果不是期望的输出
- 基于这个分析，精炼提示，澄清指令
- 重复这个过程，直到获得想要的LLM回应

#### 关于初始提示的建议
Andrew Ng分享了一个重要建议：他看到有些人过度思考初始提示。他认为更好的做法通常是快速尝试，如果得不到想要的结果，再逐步改进。

**核心鼓励**："你不会因为意外使用了稍微措辞不当的提示而搞坏互联网。所以尽管去尝试你想要的。"

### 五、重要注意事项

#### 注意一：隐私保护
如果用户拥有高度机密的信息，Andrew Ng建议：
- 确保了解大型语言模型提供商如何处理或保留这些信息的保密性
- 在将高度机密信息复制粘贴到LLM的Web用户界面之前要三思

#### 注意二：信息验证
视频提到了之前视频中关于律师的案例，该律师因提交了包含LLM编造事实的法庭文件而陷入麻烦。

Andrew Ng强调：
- 在依赖LLM的结果之前，值得仔细检查
- 自己决定是否可以信任并根据LLM的输出采取行动

#### 在这些注意事项下的实践
带着这两个注意事项进行提示时，Andrew Ng经常：
- 直接尝试
- 看看是否有效
- 如果不有效，利用初始结果决定如何精炼提示以获得更好的结果

**核心结论**："这就是为什么我们说提示工程是一个高度迭代的过程。有时候你必须尝试几次才能得到想要的结果。"

### 六、视频结尾与课程展望

#### 实践建议
Andrew Ng希望观众：
- 访问大型语言模型提供商的Web界面
- 亲自尝试这些想法
- 课程提供了一些热门LLM提供商的链接
- 鼓励观众去体验并乐在其中

#### 本周课程收尾
视频内容到这里结束了本周的主要视频集。还有一个可选视频，Andrew Ng将在其中讨论图像生成或扩散模型（diffusion models）。

#### 下周预告
Andrew Ng期待下周与观众再见，届时将讨论更多关于如何使用大型语言模型构建项目的内容。他期待与观众一起深入探讨这个话题。

## 完整字幕原文

```
I'd like to share with you some tips for
prompting large language models. If you're using the web user
interface of a LLM provider, hopefully these tips will be
useful to you right away. And it turns out that similar tips are
also useful for if you're ever involved in building a software application
that uses LLMs, let's dive in. In this video, we'll go through
three main tips for prompting. First is detail and specific. Second is guide the model to
think through its answer. And third is experiment and Iterate. This starts with be detailed and specific. Using the Fresh College Grad analogy, I would often think about how to make
sure the om has sufficient context or sufficient background information
to complete the task. So for example, if you were to ask it help
me write an email asking to be assigned to the Legal Documents project. Well, given only a prompt like this,
an om doesn't really know how to write a compelling case to advocate for
you to be assigned to that project. But if you give additional
context such as I've applied for a job in the Legal Documents project. We check legal documents I have for experience I'm prompting LLM's to get
accurate text or professional tone. Then this gives the LLM more relevant
context to write that email to help you ask to be assigned to the project. Further, if you can also describe
the desired task in detail. So if you tell it instead of
saying help me write in the email, if you ask it, write a paragraph of
text explaining why my background makes me a strong candidate on this project,
an applicant of the candidacy. Then this type of prompt would not only
give the LLM's sufficient context, but also tell it quite clearly
what you wanted to do, and this is more likely to get
you the result that you want. Second tip is to guide the model
to think through its answer. So if you were to tell it brainstorm
5 names for a new cat toy, it actually could do pretty well. But if, say, you have in mind you
want a rhyming cat toy name with a relevant emoji,
this is what I might try. I might tell it brainstorm 5 names and
tell it step 1, come up with five joyful
words already to cats. Then for each word,
come with a rhyming name. And finally, for each toy name,
add a fun relevant emoji. And with a prompt like this you might get
a result like this where the LLM follows your instructions to first come with purr,
whisker and so on. And then purr-twiri, whisker-whisper, feline-beeline with fun
emojis added to the end. So if you already have in mind a process
by which you think the arm could get to the answer that you want, giving it clear step-by-step instructions
to follow could be quite effective. Finally, there have been a bunch of
articles that are seen on social media that say things like 20 prompts
that everyone must know or 17 prompts that will help
you grow your career. I don't think there's a perfect prompt for
everyone. Instead, I find it more useful to
have a process by which you can write the prompt that will
generate the result for you. So when I'm prompting an LLM myself,
I will often experiment and iterate and try something like my
solid off say, help me rewrite this. And if I don't like the result
I might clarify and I say correct any grammatical and
spelling errors in this. And if it still doesn't give
me exactly result I want, I might clarify even further to say,
correct any grammatical and spelling errors and rewrite in the tone
appropriate for a professional resume. So very frequently the process of
prompting is not about starting off with the right prompt. It's about starting off with something and then seeing if the results
are satisfactory and knowing how to adjust the prompt to get
it closer to the answer that you want. I think of the process of prompting as
like this, you start off with an idea of what you want the LLM to do and
you just express that in a prompt. And then based on the prompt,
the LLM will give a response and it may or may not be what you want. If it is, then great, you're done. But if it isn't satisfactory, then that initial response helps you
shape your idea and modify the prompt and iterate maybe a few times before you
get to the result that you want. So I think of the prompting
process as when I start off, I try to be reasonably clear and specific. But to save time, I'll often start off
with a short prompt that maybe is frankly less specific than it's desired, but
I just want to get going quickly. After you get a result back,
if it's not what you want, then think about why the result
isn't the desired output. And based on that, refine your prompt
to clarify your instructions and keep on repeating until hopefully you
get the LLM response that you want. One tip I want to share is I've seen some
people overthink the initial prompt. I think it's better to usually just try
something quickly and if it doesn't give you the results you want, it's fine,
go ahead and improve it over time. You will not break the Internet by just
accidentally having a slightly incorrectly worded prompt. So go ahead and try what you want. Two important caveats, first, if you are in possession of
highly confidential information. I would make sure I understand how
a large language model provider does or does not use or
keep that information confidential. Before copy pasting highly confidential
information into the Web user interface of an LLM. And second, as we saw in
the last video with the lawyer, they got into trouble submitting court
filings with facts made up by an LLM. Before you counter the LLM's result,
it may be worth double checking and deciding for yourself whether or not you
can trust and act on the LLM's output. But with these two caveats when prompting,
I will often just jump in and try something and see it not work, but
then use the initial result to decide how to refine the prompt
to get a better result. And that's why we say prompting
is a highly iterative process. Sometimes you have to try a few things
before you get the result that you want. So that's it. For tips on prompting, I hope that you
go to some of the web user interfaces of the large language model providers and
try out some of these ideas yourself. And in this course, we provide some links
to some of the popular LLM providers and hope you go play with them and
have fun with them. That brings us to the end of the main
set of videos for this week. There's one optional video to follow
where I'll talk a little bit about image generation or diffusion models. So take a look at that if you want, and then I look forward to
seeing you back next week where we'll talk more about how to build
projects using large language models. Look forward to diving into
that with you next week.
```

## 关键引述/重要观点

> "This starts with be detailed and specific. Using the Fresh College Grad analogy, I would often think about how to make sure the om has sufficient context or sufficient background information to complete the task."

> "So if you were to ask it help me write an email asking to be assigned to the Legal Documents project. Well, given only a prompt like this, an om doesn't really know how to write a compelling case to advocate for you to be assigned to that project."

> "But if you give additional context such as I've applied for a job in the Legal Documents project. We check legal documents I have for experience I'm prompting LLM's to get accurate text or professional tone. Then this gives the LLM more relevant context to write that email to help you ask to be assigned to the project."

> "Further, if you can also describe the desired task in detail. So if you tell it instead of saying help me write in the email, if you ask it, write a paragraph of text explaining why my background makes me a strong candidate on this project, an applicant of the candidacy."

> "Then this type of prompt would not only give the LLM's sufficient context, but also