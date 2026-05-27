# 视频摘要：Fine-tuning

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/fpxbj/fine-tuning
- **时长**: 652秒 (约10分钟)
- **语言**: 中文
- **下载时间**: 2026-05-27 16:05:25

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
本视频介绍了大语言模型（LLM）微调（Fine-tuning）技术，作为继RAG（检索增强生成）之后的另一种增强LLM能力的方法。视频详细讲解了微调的工作原理、应用场景（包括难以通过提示词定义的任务、领域知识获取、以及小模型性能提升等），并与RAG和预训练进行了对比。

## 核心要点
1. **Fine-tuning是RAG的替代/补充方案**：当上下文信息超出LLM输入长度限制时，微调提供另一种让模型吸收信息的方式
2. **预训练概念**：LLM通过学习互联网上数百亿甚至万亿词汇进行训练，这个过程称为预训练
3. **微调数据集规模**：在预训练基础上，仅需额外1万至100万词汇的微调数据即可改变模型输出风格
4. **风格调整应用**：通过提供正面、乐观风格的数据集，可让LLM输出具有特定语气和风格的内容
5. **客服通话总结**：通过数百条人工专家撰写的总结示例进行微调，使模型生成包含具体产品型号、客户编号等细节的标准化总结
6. **模仿个人说话风格**：难以通过提示词精确描述个人语言风格，但可通过该人大量真实对话记录进行微调来精确模仿
7. **医疗笔记处理**：医生使用的专业医学缩写和术语不属于日常英语，微调医学记录可帮助LLM理解和处理医疗文档
8. **法律文档理解**：法律文件使用专业术语和表达方式（如"hereof"），微调法律文档可使LLM掌握法律领域知识
9. **金融文档处理**：微调金融文档可增强LLM在该领域的专业知识，提高处理财务相关文档的能力
10. **小模型性能优化**：通过微调，10亿参数的小模型可完成原本需要1000亿参数大模型才能完成的任务
11. **推理成本与延迟**：大模型（如1000亿参数）需要GPU服务器等专用硬件，延迟高且成本昂贵；小模型可在笔记本电脑甚至手机上运行
12. **情感分类任务**：餐厅评论情感分类是简单任务，1亿参数模型即可胜任，无需使用百亿级模型
13. **微调数据量建议**：小模型微调通常需要数百到1000条示例数据即可达到良好效果
14. **实现成本**：RAG和Fine-tuning实现成本相对较低，起始费用从几十美元到几百美元不等
15. **预训练的昂贵成本**：从头预训练模型成本极高，目前只有大型科技公司才有能力进行

## 详细内容（保留所有原始信息）

### 一、Fine-tuning概述与RAG对比

Fine-tuning（微调）是与RAG（检索增强生成）并列的另一种为LLM提供额外信息的技术。当用户拥有的上下文信息量较大、无法一次性装入LLM的输入长度或上下文窗口时，微调提供了一种让LLM吸收这些信息的替代方案。此外，微调还可用于让LLM以特定的风格输出文本。不过，视频指出微调的实际实现比RAG要困难一些。

### 二、预训练（Pre-training）概念

视频以示例说明预训练的过程：假设有一个LLM通过学习互联网上发现的句子进行训练，例如"My favorite food is a bagel with cream cheese"（我最喜欢的食物是涂奶油奶酪的百吉饼）。这个模型可能已经从数百亿甚至超过万亿词汇中学习预测下一个词。这样的LLM学会了生成听起来像互联网上内容的文本。这个在大量数据上训练大语言模型的过程通常称为**预训练**。

### 三、Fine-tuning的基本工作原理

视频举例说明微调过程：假设希望修改LLM，使其对所有事物都保持始终积极和乐观的态度。可以使用一种称为微调的技术来让LLM进行额外学习，改变其输出风格。具体步骤如下：

1. 创建一组具有积极、乐观态度的句子或文本集合，例如"What a wonderful chocolate cake"（多么美味的巧克力蛋糕）或"The novel was thrilling"（这本小说令人兴奋）
2. 利用这些文本创建额外的数据集
3. 训练LLM预测下一个词：给定"What a wonderful chocolate cake"后，预测下一个词可能是"what a wonderful chocolate..."

研究结果表明，如果在数百亿词汇上进行预训练的LLM，再用仅1万词汇（或更多，10万词汇，甚至100万词汇）进行微调，这个相对适度的数据集就能将LLM的输出转变为您想要的积极、乐观态度。

### 四、应用场景一：难以用提示词定义的任务

微调特别有用的场景之一是**任务难以在提示词中定义**的情况。

#### 客服通话总结案例

以客服通话总结为例：通用LLM可能会将通话总结为"客户告诉客服代表关于显示器的问题"。但在客服呼叫中心环境中，可能需要生成包含具体信息的总结，如"关于MK401-27KX型号、由客户5402报告的故障"等具体细节。

通过创建包含数百条人工专家撰写的总结示例数据集，并让已在互联网上学习数百亿词汇的大型语言模型进行额外微调，学习特定风格的总结写法，可以使LLM的总结能力转向您期望的风格。这种特定风格的总结实际上在文本提示中并不容易定义，微调是一种非常精确地告诉LLM您想要什么样的总结的方法。

#### 模仿个人写作/说话风格

另一个难以用提示词定义的例子是**模仿特定的写作或说话风格**。视频提到Tommy Nelson曾尝试让LLM听起来像Andrew Ng（课程讲师）的声音，但发现大多数人的说话方式并不容易在提示词中描述——如何给出清晰的指令让某人听起来像Andrew Ng？使用通用LLM并要求它"像Andrew Ng一样说话"，生成的文本并不太像他本人的风格。

但如果收集大量Andrew Ng实际说话的转录文本，让LLM通过微调学习他实际的用词方式，然后再让它写一些听起来像他的内容，结果会更像他本人的说话方式。由于模仿特定的写作或说话风格通过提示词实现非常困难（很难用文字指令描述一个人的具体风格），微调成为让LLM以特定风格说话的更有效方法。

这一技术也可应用于创建人工角色（如卡通角色）的特定说话风格。

### 五、应用场景二：帮助LLM获取领域知识

#### 医疗笔记处理

视频展示了医生撰写的医疗笔记示例，内容包含大量专业缩写和术语：
- "Pt" = patient（患者）
- "c/o" = complaining of（主诉）
- "SOB" = shortness of breath（呼吸急促）
- "DOE" = dyspnea on exertion（活动时呼吸困难）
- "PE" = physical examination（体格检查结果）
- "STAT" = 立即（拉丁语）

这些专业医学语言完全不属于日常英语范畴。如果使用普通英语训练的LLM，它处理这类文本的能力会非常有限。通过在医学记录集合上微调LLM，可以使其更好地吸收关于医学笔记的专业知识，进而构建应用程序以更好地理解医疗记录。

#### 法律文档处理

视频还展示了律师撰写给律师看的法律文书示例，其中包含大量专业法律术语，如"Licensor grants to licensee per Section 2(a)(iii), a non-exclusive right and so on and so on within 15 days hereof"（许可人根据第2(a)(iii)条授予被许可人非独占权利，并在15天内完成）。演讲者甚至表示自己在日常生活中从不会使用"hereof"这样的词，但这就是法律文档的语言风格。

通过在法律文档上微调LLM，可以帮助它获取阅读和理解法律文档的专业知识体系。

#### 金融文档处理

类似地，在大量金融文档上微调LLM可以帮助它更好地获取金融领域的知识，使其在处理此类文档的应用中表现更佳。

### 六、应用场景三：小模型实现大任务

微调的第三个重要应用是**让较小的模型执行原本需要较大模型才能完成的任务**。

#### 大模型的局限性

对于需要大量知识或复杂推理的LLM应用，可能会使用较大的模型（如超过1000亿参数的模型）。但这样的模型可能存在较高延迟——提示后可能需要等待一段时间才能获得响应。部署在自有计算机上成本也相当高昂。1000亿参数模型可能需要GPU服务器或其他高速计算机才能运行，在普通笔记本电脑或个人电脑上运行如此大型的模型会非常困难，更不用说在智能手机上了。

#### 小模型的优势

如果能让应用在更小的模型上运行（如10亿参数的模型），这样的模型规模将更容易在笔记本电脑、个人电脑甚至手机上运行。

以餐厅评论情感分类为例，这是一个足够简单的任务，可能不需要1000亿甚至2000亿参数的模型来运行，10亿参数模型可能就足够了，甚至可以更小。但较小的模型在智能程度上不如大型模型。

#### 通过微调弥补差距

通过在数据集上微调小模型——不是3个示例，而是数百甚至1000条示例（如果有足够数据），可以让10亿参数的小模型在这个任务上表现得非常好。

### 七、成本对比与总结

视频总结指出，Fine-tuning是继RAG之外帮助提升LLM能力的另一种技术。其应用场景包括：
- 难以在提示词中定义的任务（如特定风格输出）
- 获取领域知识（如医疗笔记）
- 让更小更经济的LLM完成原本需要更大LLM的任务

关于实现成本，RAG和Fine-tuning都是**相对便宜**的实现方案。RAG只是对提示词的修改，而Fine-tuning的起始成本从几十美元到几百美元不等（取决于需要微调的数据量）。

相比之下，从头预训练（Pre-training）自己的模型成本极高，目前除了合理规模的公司（通常是科技公司）外几乎没有人尝试进行预训练。

视频最后预告下一视频将介绍预训练涉及的内容。

## 完整字幕原文
```
Whereas RAG gives you one way to give additional information
to a large language model, there's another technique
called fine-tuning, which is another way to
give it more information. In particular, if you have
context that is bigger, that can fit into
the input length or the context window
length of the LLM, then fine-tuning
gives you another way to get LLM to absorb
this information. Fine-tuning also turns
out to be useful for getting the LLM output text
in a certain given style. But this actual implementation
is a bit harder than RAG. Let's take a look.
Let's say you have an LLM trained the
way that we had described previously
with sentences found on the Internet like
my favorite food is a bagel with cream cheese. Then it may have learned from hundreds of billions of words, or maybe more than
a trillion words, to predict the next
word like this. An LLM like this will
have learned to generate text that sounds like
what's on the internet. This process of training
a large language model on a lot of data is often
called pre-training. Now, let's say I want to
modify the LLM to have a relentlessly positive and optimistic attitude
about everything. There's a technique called fine-tuning that we
can use to cause the LLM to do a little bit more learning to change
its outputs to be, in this example, much more
positive and optimistic. To fine-tune the LLM, we would come up with a set of sentences or a set of texts
that takes on a positive, optimistic attitude, such as what a wonderful chocolate cake or the novel was thrilling. Given texts like this, you can then create an additional dataset using what a wonderful chocolate cake you would have given what. Next word, it will
try to predict a, what a next word is, wonderful, what a wonderful
chocolate, and so on. It turns out that if
you take an LLM that has been pre-trained on hundreds
of billions of words, and fine-tune it on just
an additional, say, 10,000 words or more, could be 100,000
words if you have more data or even
1 million words if you have even more data. Fine-tuning to this relatively modest-sized
dataset can shift the output of your LLM to take on this positive,
optimistic attitude. Now, maybe shifting
an LLM to have a relentlessly positive attitude isn't that helpful
an application, but fine-tuning is used in
many real applications. One class of applications
that fine-tuning is useful is when the task isn't easy
to define in a prompt. For example, if you want to use an LLM to summarize
customer service calls, a generic LLM may look at a
call like this and summarize it to say the customer
tells the agent about a problem with a monitor. But if you run a
customer call center, you might want it to generate specifics about what the
conversation was about. It was about the MK401-27KX reported broken by
customer 5402 and so on. If you create a dataset with maybe just hundreds of
examples of human expert written summaries and have a large language model
that's learned from hundreds of billions of
words on the internet, so it's learned a lot of general knowledge
on the Internet. But if you additionally
fine-tune it on maybe just hundreds of carefully handwritten
summaries of the specific style, then that would shift
the LLM's ability to write summaries in
the style that you want. The specific style summary is actually not that easy to
define in a text prompt. Maybe you could do it, but fine-tuning would just
be a very precise way to tell the LLM what
summaries you want. Another example of when a task isn't easy to define
in the prompt is if you want to mimic a specific writing
or speaking style. So Tommy Nelson, who's been working with
me on this course, actually tried just for fun, to get an LLM to sound like me, but it turns out that
the way most individuals sound is not that easy
to describe in a prompt. How would you give someone clear instructions
to sound like me? So if you were to prompt a general-purpose LLM and
ask it to sound like me, you'd get texts like this, which I don't think it
sounds that much like me. But if you were to take a lot of transcripts of the
way I actually talk and have an LLM be fine-tuned to train it to really sound exactly like me by
learning on my actual words, then asking it to
write something that sounds like me results
in texts like this, which I don't know, that sounds more like
how I would talk. But because mimicking a specific writing
or speaking style is very difficult
to do via prompting because it's just
difficult to describe a specific person's style by
writing text instructions, fine-tuning turns out to be a more effective way to get an LLM to speak in
a certain style. If you're building an
artificial character, maybe a cartoon character, fine-tuning could
also be a way to get an LLM to speak in
a certain style. Other than ties that easy
to defining the prompt, a second broad class
of applications of fine-tuning is to help the LLM
gain a domain of knowledge. For example, if
you want an LLM to be able to read and
process medical notes, this is what a medical note written about a patient by
a doctor might look like. This is really not
normal English. Pt is patient, c/o, complaining of, SOB, shortness of breath, DOE, dyspnea on exertion, PE, this is the results
of the physical examination and so on. Treatment is the follow up with the primary care physician, STAT chest x-ray, containing treatment
as needed on oxygen. But this is really not
normal English and if you were to take an LLM trained
on normal English, it wouldn't be very good at
processing text like this. If you were to fine-tune an LLM on a collection of
medical records, then the LLM could get
much better at absorbing this body of knowledge about what medical notes sound like. You could then use that to build other applications on
top of it to better understand medical records
or legal documents. Here's a piece of legalese written by
lawyers for lawyers, that's really difficult
for non lawyers to read. Licensor grants to licensee
per Section 2(a)(iii), a non-exclusive right and
so on and so on within 15 days hereof. I
don't know about you. I did not use the word hereof in my ordinary day to day speech. But this is what legal
documents sound like. If you want your LLM to
gain a body of knowledge about how to read and
understand legal documents, then taking LLM and
fine-tuning it to legal documents would help it to gain that body of knowledge. Similarly, financial
documents too. fine-tuning an LLM
on a large set of financial documents would
help it to better gain that body of knowledge
about finance and make it better at applications involving processing documents
that look like this. Finally, another reason to
fine tune an LLM is to get a smaller model to perform a task that may previously
have required a larger model. We'll discuss later this week some of the pros and cons of choosing a larger
versus a smaller model. But for some LLM
applications that need a lot of knowledge or
need complex reasoning, you might use a
relatively large model, say with over a 100
billion parameters. But if we were to use
a model like that, such a model may have
relatively high latency. Meaning, after you're prompted, you might need to wait a
while to get back a response. If you were deploying this
on your own computers, it could be quite costly. Even though we said
in the earlier video that these models
aren't that expensive, maybe you want it
to be even cheaper. That's because a 100 billion
parameter model may take specialized computers such as a GPU server or other really
fast computers to run. You probably have a
hard time running such a large model on
a normal laptop or PC, and certainly, not on
a smartphone today. But if you can get your application to work
on a much smaller model, say one billion parameters, then that's the range of model
size that they would run much more easily on a laptop or a PC or
on a mobile phone. For example, if
what you want is to classify restaurant reviews as positive or negative sentiment, this is a simple enough task
that you probably don't need