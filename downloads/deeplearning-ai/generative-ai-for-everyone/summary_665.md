# 视频摘要：Concerns about AI

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/l1opx/concerns-about-ai
- **时长**: 724秒 (约12分钟)
- **语言**: 中文
- **发布时间**: 2024-01-01
- **下载时间**: 2026-05-27 16:16:49

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
本视频由DeepLearning.AI创始人Andrew Ng主讲，深入探讨了关于生成式人工智能的三大核心担忧：AI是否会放大人类的偏见和最坏倾向、AI是否会取代人类工作，以及AI是否会威胁人类生存。视频通过放射科医生职业分析、RLHF技术解释、以及历史技术对比等方式，系统性地回应了这些担忧，认为AI正在变得越来越安全和公正，最终将帮助人类应对更大的生存挑战。

## 核心要点

1. **AI偏见问题与解决方案**：LLMs训练数据来自互联网，继承了人类的偏见和歧视，包括性别、种族偏见，但通过RLHF（基于人类反馈的强化学习）等技术正在逐步改善。

2. **RLHF工作原理**：RLHF通过训练奖励模型让人类评估AI回答质量，然后让AI学习生成更符合人类偏好的回答，已被证明能显著减少AI的偏见。

3. **放射科医生案例分析**：尽管2016年深度学习先驱Geoff Hinton预测AI将在5年内取代放射科医生，但事实证明放射科医生从事约30种不同任务，AI难以完全替代。

4. **AI与就业关系**：历史上每次技术革命都创造了比破坏更多的就业机会，AI将带来巨大增长和许多新工作岗位，而非大规模失业。

5. **AI不会灭绝人类**：尽管存在担忧，但没有具体机制说明AI如何导致人类灭绝，人类有能力控制比个人更强大的实体。

6. **技术进步类比**：AI发展可类比航空业，早期飞机事故频发，但通过学习和改进，现在飞机已成为最安全的交通工具。

7. **AI是应对全球挑战的关键**：气候变化、流行病、小行星撞击等才是人类真正的生存威胁，AI将成为应对这些挑战的重要工具。

8. **AGI的不确定性**：许多担忧源于对通用人工智能（AGI）何时实现的未知，AGI指能够完成任何人类智力任务的AI系统。

9. **AI辅助而非替代**：Curtis Langlotz教授的观点"使用AI的放射科医生将取代不使用AI的放射科医生"体现了AI增强人类能力而非简单替代的核心逻辑。

10. **社会责任与安全网**：在AI发展过程中，需要关注帮助人们采用AI技术，并为那些可能失业的人提供安全保障和新技能学习机会。

## 详细内容（保留所有原始信息）

### 一、开篇：AI焦虑的时代背景

在短短时间内，生成式AI已经传播到世界各地，赋予了许多人生成高质量文章、图片和音频的能力。然而，随着这些惊人的能力出现，也带来了许多关于AI的担忧。Andrew Ng指出，即使在生成式AI兴起之前，我们就生活在一个充满焦虑的时代。人们对环境问题、权威的合法性和无能、社会公平问题，甚至对未来等待着我们什么样的前景都感到焦虑。作为一项非常强大的技术，AI继承了一大部分这种焦虑。在本视频中，让我们来看看一些与AI特别相关的焦虑和担忧。

### 二、第一大担忧：AI是否会放大人类偏见

#### 2.1 偏见的来源与表现

一个广泛存在的担忧是AI是否会放大人类最坏的倾向。LLMs（大型语言模型）是在来自互联网的文本上进行训练的，这些文本反映了人类最好的一面，但也有一些最坏的一面，包括我们的一些偏见、仇恨和误解。LLMs也会学习一些这些负面特质。那么，它会放大我们最坏的倾向吗？

在第一周的课程中，我们已经看到了一个LLM表现出性别偏见的例子，涉及外科医生或护士更可能是男性还是女性。再举一个可能更简单的例子，如果你让一个LLM在初始训练后填写空白，而空白是"CEO"，许多模型倾向于选择"男人"这个词。当然，这是一个社会偏见，扭曲了一个事实，即所有性别的人都可以成功地领导公司。

#### 2.2 偏见是数据反映的结果

互联网上的文本代表了我们的现在和过去。因此，LLM从这些数据中学习，反映了我们过去和现在的一些偏见，也许不足为奇。但也许我们希望LLM代表一个更公平、更少偏见、更公正的充满希望的未来，而不仅仅是来自我们过去的数据。

#### 2.3 RLHF技术解决方案

幸运的是，LLMs正在通过微调变得更少偏见，这是我们在第二周讨论的内容。以及更先进的技术，如基于人类反馈的强化学习（RLHF）。在第二周，有一个关于RLHF的可选视频。无论你是否看过，我想简要描述一下RLHF如何帮助减少LLM的偏见。

RLHF是一种训练LLM生成更符合人类偏好的回答的技术。RLHF的第一步是训练一个称为奖励模型的答案质量模型，可以自动评分。在这个步骤中，我们用许多这样的查询来提示LLM，如"空白是CEO"，并从LLM收集不同的回答。然后我们请人类对这些回答进行评分。在1到5的范围内，我们给高度理想的回答高分，如"男人"或"女人"，给荒谬的回答低分，如"飞机"。任何包含性别偏见或种族偏见或包含性别或种族侮辱的回答都将获得非常低的分数。

使用提示、回答和人类分配的分数作为数据，我们然后使用监督学习来训练一个奖励模型，可以输入一个回答并对其进行评分。我们这样做是因为让人类对回答进行评分是昂贵的。但一旦监督学习算法学会了自动评分回答，我们就可以自动且廉价地对大量回答进行评分。

最后，现在LLM有了一个学习到的奖励模型来评分尽可能多的回答，我们可以让LLM生成对许多不同提示的大量回答。让它进一步训练自己生成获得高分，因此反映人类认为更理想的回答。

#### 2.4 RLHF的效果与意义

RLHF已被证明可以使LLM根据性别、种族、宗教和其他人类特征表现出偏见的可能性大大降低。它使LLM不太容易提供有害信息，也使它对人们更尊重、更有希望。如今，LLM的输出已经比互联网上平均文本更安全、更少偏见。但这类技术正在继续改进，因此LLM放大人类最坏特质程度正在持续下降，因为它们正变得越来越与未来对齐。Andrew Ng认为我们都希望LLM反映一个更公平、更少偏见、更公正的世界。

### 三、第二大担忧：AI是否会导致大规模失业

#### 3.1 就业威胁的普遍担忧

第二个主要担忧是，当AI能够比任何人类更快、更便宜地完成工作时，我们中谁能谋生？AI会让很多人失业吗？为了理解这是否可能发生，让我们看看放射科。在2016年，很多年前，深度学习的先驱Geoff Hinton是Andrew Ng的朋友，他说AI在分析X射线图像方面变得如此出色，在五年内，它可以取代放射科医生的工作。他说了这句了不起的话：如果你是一名放射科医生，你就像一只土狼，已经在悬崖边缘，但你还没有往下看。所以它没有意识到下面没有地面。人们现在应该停止培训放射科医生了。这完全显而易见，在五年内，深度学习将比放射科医生做得更好。

#### 3.2 放射科医生案例的现实检验

但我们现在已经远远超过了这声明的五年，AI远远没有取代放射科医生。Andrew Ng的放射科医生朋友中没有一个人因AI而失去工作。这是为什么呢？有两个原因。首先，解释X射线比当时看起来要难，虽然我们正在快速进步。但第二点更重要，事实证明放射科医生做的远不止解释X射线图像。根据O*NET，放射科医生执行大约30项不同任务，其中之一是解释X射线和其他医学图像，但他们做许多其他任务。到目前为止，AI很难在人类水平上完成所有这些任务。

#### 3.3 放射科医生的多元职责

列出放射科医生做的一些其他任务，除了解释X射线外，他们还操作成像硬件，与患者或其他利益相关者沟通检查结果。在手术过程中应对并发症，例如患者在成像过程中恐慌发作。他们记录手术过程和结果，以及许多其他任务。Andrew Ng认为AI确实有很高的潜力来增强或协助X射线解释。从技术上讲，这主要是用监督学习完成的，而不是生成式AI。但对于AI完全自动化所有这些任务仍然遥遥无期。

#### 3.4 AI不会替代但会增强

这就是为什么Andrew Ng认为Curtis Langlotz说得很好，他是斯坦福大学放射学教授，是Andrew Ng的朋友和同事。他说AI不会取代放射科医生，但使用AI的放射科医生将取代不使用AI的放射科医生。Andrew Ng认为我们将在许多其他职业中看到这种效果。

#### 3.5 历史视角与技术革命

Andrew Ng并不是要最小化帮助许多人采用AI的挑战，或最小化少数其工作将消失的人的痛苦。或我们确保受影响的人有安全网和学习新技能的机会的责任。但每一波技术，从蒸汽机到打字机到计算机，都创造了比它摧毁的多得多的就业机会。正如Andrew Ng本周早些时候提到的，在大多数创新浪潮中，企业最终专注于增长，专注于增长有无限潜力，而不是节省成本。所以AI将带来大量增长，并在此过程中创造许多新工作岗位。

### 四、第三大担忧：AI是否会灭绝人类

#### 4.1 AI失控的历史案例

这让我们来到了可能是最大的焦虑：AI会杀死我们所有人吗？我们知道AI可能会失控。自动驾驶汽车发生了撞车，导致了生命的悲剧性损失。2010年，一个自动交易算法导致了股票市场崩盘。在司法系统中，AI导致了不公平的判决。所以我们知道设计不当的软件可能产生戏剧性影响。

#### 4.2 灭绝威胁论的局限性

但它能导致人类灭绝吗？Andrew Ng不认为会。他知道对此有不同看法，但最近他找了一些关心这个问题的人交谈，并与一些他认识的最聪明的AI人交谈。一些人担心坏人使用AI来摧毁人类，比如制造生物武器。其他人则担心AI无意中导致人类灭绝。类似于人类如何通过简单的缺乏对我们行动可能导致这种结果的意识，导致了许多其他物种的灭绝。

Andrew Ng试图评估这些论点的现实性，但他发现它们不具体、不详细地说明AI如何导致人类灭绝。大多数论点归结为这可能发生。一些人会补充说，这是一种新技术，所以这次事情可能不同。但这个说法对于人类发明的每一种新技术都是正确的。证明AI不可能导致人类灭绝类似于证明一个负面。Andrew Ng无法证明AI超级智能不会消灭人类，但这只是似乎没有人确切知道它如何能做到。

#### 4.3 人类控制强大实体的能力

但Andrew Ng确实知道这一点：人类在控制许多比任何个人更强大的事物方面有丰富经验，比如公司和民族国家。还有许多我们无法完全控制但仍然有价值和安全的事物。例如，以飞机为例，今天我们仍然无法完全控制，因为风和湍流会摇晃飞机，或者驾驶飞机的飞行员可能犯错。在航空的早期，飞机杀死了很多人。但我们从那些经验中学习，制造了更安全的飞机，也设计了更好的操作规则。今天，许多人可以登上飞机而不为生命担忧。

#### 4.4 AI安全的持续改进

同样对于AI，我们正在学习更好地控制它，而且它每天都在变得更安全。

#### 4.5 真正的生存威胁与AI的角色

最后，如果我们看看对人类的真正风险，如气候变化导致地球部分地区的重大人口减少，或者希望不是下一次流行病。或者概率更低得多的另一次小行星撞击地球，像恐龙一样消灭我们。Andrew Ng认为AI将成为应对这些挑战的关键部分。所以Andrew Ng知道此刻对此有不同看法。但他的观点是，如果我们希望人类在接下来的千年中生存和繁荣，AI增加了我们成功到达那里的几率。

### 五、AGI：担忧的根源

计算机在某些狭窄维度上已经比任何人都聪明。但AI进步如此之快，以至于许多人发现很难准确预测几年后它会是什么样子。Andrew Ng认为一些担忧的根源，包括灭绝风险，是许多人无法确定AI何时会达到通用人工智能（AGI）。也就是说，能够完成人类可以完成的任何智力任务的AI。让我们在下一个视频中更深入地看看AGI。

## 完整字幕原文

```
In a short time, access to generative
AI has spread around the world and given many people the ability to generate
high quality essays, pictures, and audio. With these amazing capabilities have
also come many concerns about AI. I think even before
the rise of generative AI, we've been living in
a time of many anxieties. Anxieties about the environment,
about the legitimacy, incompetence of authority, about
society's ability to treat people fairly, even about what sort of
future awaits us all. AI as a very powerful technology has
inherited a large share of this anxiety. In this video, let's take a look
at some of these anxieties and concern that relate specifically to AI. One widely held concern
about AI is whether it might amplify humanity's worst impulses. LLMs are trained on
text from the Internet, which reflects some of humanity's best
qualities, but also some of its worst, including some of our prejudices,
hatreds, and misconceptions. LLMs learn some of these
negative qualities, too. So will it amplify our worst impulses? In the first week, we had seen an example
of an LLM exhibiting a gender bias with regard to whether a surgeon or a
nurse is more likely to be male or female. To take another maybe slightly
simpler example, if you asked an LLM after its initial training to fill
in the blank and the blank was a CEO, many models would be prone
to choose the word man. And, of course, this is a social bias
that distorts the fact that people of all genders can successfully
lead companies. Text on the Internet represents
our present and our past. And so perhaps it's no surprise that
an LLM learning from this data reflects some of these biases from our past and
our present as well. But perhaps we want LLMs to represent
a hopeful future that is fairer, less biased, and more just,
rather than just data from our past. Fortunately, LLMs are becoming
less biased through fine-tuning, which we discussed in week two. As well as more advanced techniques,
such as reinforcement learning
from human feedback or RLHF. In the second week,
there was an optional video on RLHF. Whether or not you watched that, I'd like to briefly describe how RLHF
is helping to make LLMs less biased. RLHF is a technique that trains an LLM
to generate responses that are more aligned with human preferences. The first step of RLHF is to train
an answer quality model called a reward model that
automatically scores answers. So in this step of RLHF, we would prompt
the LLM with many queries like this, the blank was a CEO, and
collect different responses from the LLM. Then we would ask humans
to score these answers. So on a scale of one to five, we give
a high score to highly desirable answers like man or woman, and a low score to
nonsensical answers like airplane. And any answer that contains
a gender bias or racial bias or contains a gender or
racial slur will receive a very low score. Using the prompt, the responses, and the scores assigned by humans as data,
we would then use supervised learning to train a reward model that
can input a response and score it. We do this because asking humans
to score responses is expensive. But once a supervised learning algorithm
has learned to automatically score responses, we can score a lot of responses
automatically and inexpensively. Finally, now that the LLM has a learned reward model to score as
many responses as it wants, we can have the LLM generate a lot of
responses to many different prompts. And have it further
train itself to generate more responses that get high scores and
that, therefore, reflect answers that humans
perceive as more desirable. RLHF has been shown to make LLMs much
less likely to exhibit bias according to gender, race, religion, and
other human characteristics. It makes LLMs less prone to
hand out harmful information, and also makes it more respectful and
hopeful to people. Already today,
the output of LLMs are much safer and less biased than, say,
the average piece of text on the Internet. But technology like this
is continuing to improve, and so the degree of an LLM amplifying
humanity's worst qualities is continuing to decrease as they
are becoming better aligned to the future. I think we all hope LLMs will reflect of a
fairer, less biased, and more just world. A second major concern is who among us
will be able to make a living when AI can do our jobs faster and
cheaper than any human can? Will AI put many of us out of a job? To understand whether this is likely
to happen, let's look at radiology. In 2016, many years ago, Geoff Hinton,
who's a pioneer of deep learning and a friend of mine, said that AI was
becoming so good at analyzing X-ray images that in five years,
it could take radiologists' jobs. He made this remarkable statement that
if you work as a radiologist, you're like a coyote that's already over the edge
of the cliff, but hasn't yet looked down. So it doesn't realize there's
no ground underneath them. People should stop
training radiologists now. It's just completely obvious
that within five years, deep learning is going to do
better than radiologists. But we're now well past five
years since this statement, and AI is far from replacing radiologists. Not a single one of my radiologist
friends has lost their job to AI. Why is that? Two reasons. First, interpreting X-rays turns out
to be harder than it looked back then, though we are making rapid progress. But second and more important, it turns out that radiologists do a lot
more than just interpret X-ray images. According to O*NET,
radiologists do about 30 different tasks, one