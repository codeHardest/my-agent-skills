# 视频摘要：Retrieval Augmented Generation (RAG)

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/k44k0/retrieval-augmented-generation-rag
- **时长**: 462秒 (约7分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 16:03:57

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
本视频介绍了检索增强生成（RAG）技术，这是一种通过为大型语言模型提供额外知识来扩展其能力的技术。RAG通过三个步骤实现：检索相关文档、将检索到的文本融入提示词、最后由LLM生成答案。该技术在PDF对话、网页问答、搜索引擎等多个领域得到广泛应用，并引出了一个重要观点——应将LLM视为推理引擎而非知识库。

## 核心要点
1. **RAG技术定义**：检索增强生成（Retrieval Augmented Generation）是一种通过提供额外知识来扩展LLM能力的技术，使其能够获取互联网或公开来源之外的信息。

2. **RAG三步骤流程**：
   - 第一步：根据问题检索相关文档集合
   - 第二步：将检索到的相关文本融入更新后的提示词
   - 第三步：使用丰富的提示词提示LLM生成答案

3. **文档检索机制**：RAG系统通过计算机查找与问题最相关的文档，如员工福利文件、休假政策、设施文件、薪资流程等不同类型的公司文档。

4. **提示词构建原则**：实际应用中，不是将整个长文档放入提示词，而是提取与问题最相关的部分，以避免超出LLM的输入长度限制。

5. **来源追溯功能**：在展示给用户的RAG应用输出中，通常会添加指向原始源文档的链接，方便用户验证答案。

6. **PDF对话应用**：PandaChat、AskYourPDF、ChatPDF等应用允许用户上传PDF文件并基于文档内容提问。

7. **企业知识问答应用**：Coursera Coach、Hubspot等公司使用RAG技术构建聊天机器人，基于公司内容回答用户问题。

8. **搜索引擎革新**：微软Bing、谷歌的生成式AI功能、以及startup.com等搜索引擎正在被RAG技术改变，采用对话式界面。

9. **核心思维转变**：应将LLM视为推理引擎而非知识库，让其处理信息而非仅存储信息。

10. **个人使用场景**：用户可以通过网页界面向LLM粘贴文本片段，让其基于该上下文生成答案，这也是RAG思想的应用。

11. **技术局限性**：LLM技术仍处于早期阶段，并非总能良好运作。

12. **后续内容预告**：下一个视频将介绍微调（fine-tuning）技术，这是另一种扩展LLM能力的方法。

## 详细内容（保留所有原始信息）

### RAG技术简介与背景

视频开头指出，提示大型语言模型已经能够实现很多功能，但存在一种名为检索增强生成（RAG）的技术，可以通过为其提供额外的知识来显著扩展LLM的能力范围。这些知识超出了LLM从互联网或其他公开来源数据中可能学到内容的范畴。

以一个具体场景为例：如果向一个通用聊天系统询问"员工有停车位吗？"，它可能会回答"我需要更多关于您工作场所的具体信息"，因为它不知道您公司的停车政策。而RAG技术则可以为LLM提供额外信息，使其能够引用您公司特定的政策来回答这个问题。

### RAG的三步工作流程

**第一步：文档检索**

给定问题"员工有停车位吗？"，RAG系统首先会查找可能包含答案的文档集合。例如，公司可能拥有员工福利文件、休假政策文件、设施文件以及薪资流程文件等各种文档。RAG系统的第一步是让计算机找出哪些文档（如果有的话）与这个问题最相关。停车问题看起来像是关于设施的问题，涉及团队所在的建筑，因此系统应该选择设施文档作为最相关的文档。

**第二步：构建增强提示词**

第二步是将检索到的文档或文本整合到一个更新后的提示词中。构建提示词的格式可以是这样的："使用以下上下文片段回答最后的问题"，然后将设施文档中关于停车政策的相关文本放入提示词中——例如"所有员工可以在1层和2层停车"等内容。这样就形成了一个相当长的提示词，因为它试图为LLM提供大量上下文。

视频特别强调了输入长度限制的问题：之前讨论过大型语言模型的提示词长度或输入长度是有限制的。因此在实践中，与其将整个很长的文档放入提示词，不如只提取文档中与问题最相关的部分放入提示词。

**第三步：LLM生成答案**

最后，将原始问题"员工有停车位吗？"添加到提示词中。这整个过程被称为"检索增强生成"，因为我们要生成一个答案，但我们通过检索相关的上下文或相关信息来增强文本生成的过程，并将这些额外文本融入提示词中。

构建好这个提示词后，最后一步就是用这个丰富的提示词来提示LLM。希望LLM能够给出一个深思熟虑的答案，告诉用户可以在哪里停车。

### 来源追溯与透明度

在一些使用RAG的应用中，在向用户展示的输出中，还会添加一个指向导致此答案生成的原始源文档的链接。在这种情况下，可能会链接到设施文档，这样用户如果愿意的话可以回去阅读原始源文档并亲自核对答案。

### RAG技术的应用案例

**PDF对话应用**

目前有许多公司提供允许用户与PDF文件对话的软件。例如，如果您正在阅读一份白皮书，但没有时间仔细阅读全部内容，但有基于该白皮书想要回答的问题。现在有许多应用程序如PandaChat、AskYourPDF、ChatPDF等，允许您上传PDF文件然后提问。它们会使用RAG来尝试为您生成答案。视频作者表示，这些软件包中有些效果较好，有些效果较差，所以您得到的结果可能会有所不同。但对于构建让用户与PDF文件对话的应用程序，确实存在很多热情和兴趣。

**企业内部知识问答**

越来越多的RAG应用程序能够基于网站文章回答问题。例如，Coursera Coach做很多事情，其中一件事是使用RAG尝试基于Coursera网站上的内容回答问题。SnapChat也有一个聊天机器人，使用来自Snap的文本来尝试回答用户可能对其产品提出的不同问题。Hubspot是一家营销自动化公司，它的聊天机器人可以让用户提问，并基于公司或网站本身的内容尝试为用户生成答案。这种类型的聊天正成为让用户获得关于公司产品问题答案的另一种方式。

**新型网络搜索**

RAG也正在引领新型网络搜索形式。微软Bing具有聊天功能，谷歌也有生成式AI功能，可以响应用户的查询生成文本。startup.com是由视频讲者 former PhD 学生Richard Socher创立的网络搜索引擎，其核心是聊天式界面。RAG在当今许多应用中使用，而且令人兴奋的是，它似乎正在改变甚至网络搜索本身。

### 核心思维转变：推理引擎 vs 知识库

视频总结部分分享了一个重要观点：应将LLM视为推理引擎，而不是知识库。LLM可能已经阅读了互联网上的大量文本，因此很容易认为它们知道很多事情，而且它们确实知道很多，但它们并非无所不知。

通过RAG方法，我们在提示词本身中提供相关的上下文，然后让LLM阅读那段文本并处理它以获得答案。换句话说，我们不是依赖它记住足够的事实来给我们答案，而是将其用作处理信息的推理引擎，而不是信息来源。

这种将LLM视为推理引擎而非存储和检索信息方式的思维方式，可以扩展我们可能头脑风暴和认为LLM能够做到的应用集。诚然，LLM技术处于早期阶段，并非总能运作良好。但如果LLM不仅仅是为您存储大量信息的数据库，而是能够处理和推理信息，那将是思考LLM未来发展方向的一个令人兴奋的方向。

### 实际应用建议

虽然视频主要讨论了在构建软件应用背景下使用RAG，但这个思路在您使用网页用户界面时也很有用。有时视频作者会将一段文本复制到在线网页界面的LLM提示词中，然后告诉它使用该上下文为我生成答案，这也可以是RAG的一种应用。

视频最后提到，RAG对许多不同的应用都很有用，希望观众也能发现它的价值。下一个视频将讨论另一种称为微调（fine-tuning）的技术，这是另一种扩展LLM能力的方法。

## 完整字幕原文
```
Well, we've already seen that prompting a large language
model can take you quite far. But there's a technique called Retrieval Augmented
Generation or RAG, that can significantly
expand what you can get an LLM to do by giving it additional knowledge beyond
what it may have learned from data on the Internet
or other open sources. Let's take a look.
If you were to ask a general
purpose chat system, such as one of the
ones on the internet, a question like, is there
parking for employees? It might answer something like, I need more specific information about your workplace because it doesn't know what is the parking
policy for your company. But RAG or Retrieval Augmented
Generation will see, is a technique that
can give the LLM additional information so that if you ask it if
there's parking, it can refer to policies
specific to your company. How does it work?
RAG has three steps. Step 1 is given the question, is there parking for employees? It'll first look
through a collection of documents that
may have the answer. For example, if your company
has different documents on the benefits offered
to employees and the leave policy and some
documents on the facilities, and some documents on
payroll processes, then the first step in
the rag system would be to have a computer
find out which, if any, of these documents is most relevant to this question. Parking seems like a question
about the facilities, about the building
that your team works in and so hopefully you'll select out the facilities document as most relevant. The second step is
then to incorporate the retrieved document of the retrieved text into
an updated prompt. Let me construct a
prompt as follows. I'm going to say use the following pieces of context answer the
question at the end, and then I'm going to
take the relevant text from my facilities
documentation with the parking policy that all employees may
park on levels 1 and 2 and so on and put
that into my prompt. This is now pretty long
prompt because it tries to give a lot of
context for the LLM. Now remember last week
we had spoken about limitations to the prompt length or the input length for
a large language model. That's why in practice, rather than dumping an entire very long
document into the prompt, you might pull out just the
part of the document that's most relevant to
the question and put just that into the prompt. Then finally, we add
the original question, is your parking for employees? This is called Retrieval
Augmented Generation or RAG, because we're going to
generate an answer to this, but we're going to
augment how we generate text by retrieving the
relevant context or the relevant information and augmenting the prompt with
that additional text. Having constructed this prompt, the final step is to then prompt the LLM with
this rich prompt. Hopefully the LLM
will then give us a thoughtful answer telling
us about where we can park. In some applications using RAG in the output
shown to the user, we would also add a link to the original source document that led to this answer
being generated. In this case, we might link to that facilities documentation
so the user can, if they wish, go back and read the original source document and double check the
answer for themselves. RAG Retrieval
Augmented Generation is an important technique
that is enabling many LLMs to have context
or to have information beyond what it may have
learned on the open Internet. Here are some examples of
RAG based applications. There are many companies today, they are offering
software that let you chat with a PDF file. For example, if you're
reading a white paper but you maybe don't have time to read the entire
thing carefully, but have a question
that you want answered based on
that white paper. There are many applications
today like PandaChat, AskYourPDF, ChatPDF, and many others that let you upload your PDF file
and then ask questions. And they'll use RAG to try
to generate answers for you. I find that some of
these software packages work better and some work worse. So the results you get may vary. But there's certainly been a lot of excitement and interest about building applications to let you chat with your PDF files. There are also more and
more RAG applications that will answer questions based
on a website articles. For example, Coursera Coach
does multiple things, but one of the things it
does is use RAG to try to answer questions based on content on the
Coursera site itself. SnapChat also has a chat
bot that uses texts from Snap to try to answer different questions you might
have about their products. Hubspot, which is a marketing
automation company, is another example
of a company that has a chat bot that
lets you pose questions and tries to generate
answers for you based on content from the company
or from the website itself. So these types of
chats are becoming an alternative way to let users get answers to
questions that they may have about your
company's offerings. RAG is also leading to
new forms of web search. Microsoft Bing has
a chat capability. Google has a
generative AI feature as well that can generate
text in response to your queries and
startup.com which was actually started by one
of my former PhD students, Richard Socher is a web
search engine that was built centered on a
chat like interface. RAG is used in many
applications today, and excitingly, it seems to be transforming even web search. To wrap up this video, there's one big idea I'd
like to share of you, which is to think of the LLM, not as a knowledge store, but instead as a
reasoning engine. LLMs may have read a lot
of texts on the Internet, and so it's tempting
to think of them as knowing a lot of
things and they do, but they don't know everything. With the rag approach, we provide relevant context in the prompt itself and we ask the LLM to read that
piece of text and then to process it to
get to the answer. In other words, rather than
counting on it to have memorized enough facts
to get us the answer, we're instead using it
as a reasoning engine to process information and not
as a source of information. Find that this way of
thinking about LLM's as a reasoning engine
rather than as a way to store and
retrieve information, can expand the set
of applications that we might brainstorm and consider an LLM to
be capable of doing. Admittedly, LLM technology is early and it doesn't
always do that well. But if an LLM isn't just a database that stores a
lot of information for you, but it can process and
reason through information. I think that is an
exciting direction to think about where
LLMs might go from here. Even though I've talked
mostly about RAG in the context of building
software applications, this idea can also be useful if you're using a
web user interface. Sometimes I would take a
piece of text and just copy it into the prompt
of an online web UI of an LLM and then tell it to
use that context to generate an answer for me and that too can be an
application of RAG. I've found that RAG is useful for many
different applications, and I hope that you will too. In the next video,
we'll talk about another technique
called fine tuning, which is another way to
expand what an LLM can do. But before I wrap
up, let me just say, I hope you enjoyed this
video on RAG and that you can really clean up
with this RAG stuff. I'll see you in the next video.
```

## 关键引述/重要观点

> "Retrieval Augmented Generation or RAG, that can significantly expand what you can get an LLM to do by giving it additional knowledge beyond what it may have learned from data on the Internet or other open sources."

> "RAG has three steps. Step 1 is given the question... it'll first look through a collection of documents that may have the answer... The second step is then to incorporate the retrieved document of the retrieved text into an updated prompt... The final step is to then prompt the LLM with this rich prompt."

> "Rather than dumping an entire very long document into the prompt, you might pull out just the part of the document that's most relevant to the question and put just that into the prompt."

> "In some applications using RAG in the output shown to the user, we would also add a link to the original source document that led to this answer being generated."

> "Think of the LLM, not as a knowledge store, but instead as a reasoning engine."

> "With the RAG approach, we provide relevant context in the prompt itself and we ask the LLM to read that piece of text and then to process it to get to the answer. In other words, rather than counting on it to have memorized enough facts to get us the answer, we're instead using it as a reasoning engine to process information and not as a source of information."

> "This way of thinking about LLM's as a reasoning engine rather than as a way to store and retrieve information, can expand the set of applications that we might brainstorm and consider an LLM to be capable of doing."

## 相关话题/关键词

- 检索增强生成 (Retrieval Augmented Generation, RAG)
- 大型语言模型 (Large Language Model, LLM)
- 文档检索 (Document Retrieval)
- 提示词工程 (Prompt Engineering)
- 上下文学习 (In-context Learning)
- 知识库 (Knowledge Base)
- 推理引擎 (Reasoning Engine)
- PDF对话应用
- 企业知识问答
- 聊天式搜索 (Chat-based Search)
- 微软Bing Chat
- 谷歌生成式AI
- startup.com
- Coursera Coach
- SnapChat Chatbot
- Hubspot
- PandaChat
- AskYourPDF
- ChatPDF
- 微调 (Fine-tuning)
- 信息处理 vs 信息存储
- 