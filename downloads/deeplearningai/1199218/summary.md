# 视频摘要：LLM sampling strategies

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/8850gm/llm-sampling-strategies
- **时长**: 492秒 (约8分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:12:35

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
本视频深入探讨了大语言模型(LLM)中随机性的核心原理及其控制方法，详细介绍了贪婪解码、温度参数、Top K采样、Top P采样、重复惩罚和Logit Biasing等多种采样策略，并通过实际案例展示了如何通过调整这些参数来优化LLM的输出行为，以适应不同应用场景的需求。

## 核心要点
1. **随机性本质**：LLM生成的每个token都是基于概率分布的加权随机选择，而非确定性输出
2. **概率分布特征**：分布曲线左侧高尖峰表示模型置信度高，扁平分布表示不确定性高
3. **贪婪解码(Greedy Decoding)**：始终选择最高概率token，使输出完全确定性，但可能导致可预测性和重复循环问题
4. **温度参数(Temperature)**：控制概率分布形态，Temperature=1为原始分布，0为完全贪婪解码，高于1则使分布更平坦
5. **Top K采样**：限制模型仅从概率最高的K个token中选择，如设置top 5
6. **Top P采样(核采样)**：选择累积概率达到阈值P的所有token，动态调整选择范围
7. **Top P优势**：相比Top K更具动态性，能根据模型置信度自动调整候选token池大小
8. **重复惩罚(Repetition Penalty)**：降低已出现词汇的再次选择概率，提升输出自然度
9. **Logit Biasing**：直接调整特定token的选择概率，可用于过滤不当内容或确保分类器输出特定类别
10. **推荐配置**：一般用途推荐temperature=0.8、top p=0.9、repetition penalty=1.2
11. **场景适配**：代码生成和事实问答适合低温度低top p，创意场景适合高温度高top p
12. **迭代调优**：通过实验调整各参数，逐步优化LLM行为以适配具体应用

## 详细内容（保留所有原始信息）

### 一、LLM随机性的基本原理

大语言模型运作的核心在于理解并控制其内在的随机性。每个token添加到生成结果中的过程本质上是一个加权随机选择过程。以"the sky is"这个提示为例，token的概率分布呈现如下特征：Blue有50%的概率作为下一个token出现，bright有25%的概率，其他token的概率均在10%以下，并迅速衰减至1%以下。

从视觉上看，概率分布曲线的形态具有重要的指示意义。当曲线在左侧呈现高尖峰时，表明模型对其选择具有较高的置信度，只有极少数token有实际被选中的机会。相反，较为平坦的分布则代表模型存在较大的不确定性，意味着模型有多个可能的生成方向，且没有明显的最优选择。解码并控制这个概率分布曲线的形态，是调优LLM行为的关键所在。

开源大语言模型允许用户查看每一步生成的token概率分布，这对于理解和调试模型行为非常有价值。通过观察这些概率分布，开发者可以深入了解模型在不同情境下的决策模式。

### 二、贪婪解码(Greedy Decoding)

贪婪解码是一种简单直接的策略，它指示LLM不进行随机选择，而是始终选择概率最高的token。这种方法的主要优势在于使LLM的行为完全确定性：给定相同的提示，模型将始终生成完全相同的响应。这种可重复性在某些应用场景中非常重要，例如代码补全或系统调试。

然而，贪婪解码也存在明显的缺点。首先，它可能导致输出文本过于可预测，文字可能显得平淡、刻板或不够自然。其次，更严重的问题是LLM有时会陷入重复循环，不断生成相同的词序列。这是因为LLM本身并不关心整体完成质量，它只是机械地选择下一个最高概率的token，一旦进入重复循环，就没有任何机制能够打破这个循环。

尽管存在这些潜在缺陷，在需要高度可预测性和确定性输出的场景中，贪婪解码仍然是合理的选择，比如代码补全任务或作为调试系统的临时设置。

### 三、温度参数(Temperature)

温度是控制LLM随机性最广泛使用的参数，可以将其想象为一个调节概率分布形态的旋钮。温度参数的设置直接影响模型生成文本的多样性和创造性。

- **Temperature = 1**：这是默认设置，会返回原始的概率分布，不做任何修改
- **Temperature < 1**：降低温度会导致分布变得更加尖锐和集中，只有最高概率的token才有被选中的机会，排序顺序不变，但各token被选中的概率发生变化
- **Temperature = 0**：当温度设为0时，模型执行贪婪解码，只有概率最高的单个token拥有100%的选择概率
- **Temperature > 1**（如1.1-1.3范围）：提高温度会使概率分布变得更加平坦，给低概率token更多被选中的机会，这会产生更多的变化性和更具创意感的文本
- **Temperature过高**：会导致分布过于平坦，几乎所有token都有相等的选择机会，即使它们可能不太合理

无论设置何种温度，概率分布曲线的右侧仍会有一条长长的尾巴，包含大量无意义的token，只是被选中的概率较低。

### 四、Top K采样

Top K采样是最简单的补充采样技术之一，它限制了LLM的选择范围，仅允许从概率最高的K个token中进行选择。例如，同时设置temperature为1.1，并将LLM限制为从概率最高的5个token中选择。这种方法有效地过滤掉了分布尾巴中的低质量token，同时保持了一定的随机性。

Top K采样的一个潜在问题是它总是从固定数量的候选token中选择，而不考虑实际概率分布的形态。这意味着无论模型对某个选择有多大把握，候选池的大小始终保持不变。

### 五、Top P采样(核采样)

Top P采样是一种更动态的方法，它限制LLM从累积概率达到某个阈值的所有token中选择。例如设置top p为85%，模型会从分布左侧开始，依次累加各token的概率，直到累积概率超过85%，然后只从这个候选集中选择下一个token。

Top P采样相比Top K更具响应性和动态性。在Top K中，LLM始终从相同规模的token池中选择，无论分布形态如何。而Top P则能根据模型的置信度自动调整选择范围：当LLM比较确定时（少数token具有很高概率），它会将选择限制在少数最可能的token上；当LLM不确定性较高时（分布平坦，没有明显最优选择），它会允许从更大的潜在token池中选择。

### 六、重复惩罚(Repetition Penalty)

大语言模型有时会反复使用相同的词汇或短语，这会使生成的文本听起来不自然。许多LLM提供了重复惩罚功能，可以降低已经在生成结果中出现过的词汇的再次选择概率。这种技术能够使生成的文本听起来更自然、更有变化。

重复惩罚通过调整已出现词汇的概率来实现，开发者可以根据需要设置惩罚的强度。

### 七、Logit Biasing（Logit偏置）

大多数LLM还允许直接增加或减少特定token的选择概率，这通常称为logit biasing或logit偏置。这种偏置会永久性地调整相关token的选择概率。

Logit Biasing的应用场景包括：

- **内容过滤**：如果知道不希望RAG系统生成不恰当内容，可以将某些敏感词汇的偏置降低
- **分类任务**：如果RAG系统是一个分类器，需要输出预定义类别之一，可以提升这些类别的概率以确保LLM始终从它们中选择

### 八、参数组合与推荐配置

以下是结合多种技术的API调用示例，展示了一套相当合理的通用参数组合：

- **Temperature**: 0.8（使模型在token选择上稍微保守）
- **Top P**: 0.9（避免从分布远端选择）
- **Repetition Penalty**: 1.2（轻微惩罚重复词汇）

通过实验调整每个参数，可以根据应用场景精确调优LLM的行为。

### 九、实践建议

视频建议根据具体应用场景选择合适的参数配置：

1. **代码生成或事实问答**：适合使用较低的温度和较低的top p值，以获得更准确、可预测的输出
2. **创意领域应用**：较高的温度和top p值可以给LLM更有趣、更有探索性的语调
3. **迭代优化**：在观察到LLM表现的具体问题后，再考虑引入重复惩罚、logit偏置或其他采样技术

理解LLM随机选择的多重调优方法，并通过迭代找到适合项目的设置，是获得所需性能表现的关键。

## 完整字幕原文
```
A big part of working with an LLM is understanding and controlling the randomness at the heart of how they operate. In this video, let's have a look at a typical LLM API, and explore the different options they provide to control the way your LLM chooses the next tokens. Every token a large language model adds to your completion is a weighted random choice. If you use an open source large language model, you can see how this choice was made. These models will let you see the token probabilities generated at each step, which was used to select the next token. For example, for the prompt, the sky is, this is what the probability distribution looks like. Blue has a 50% probability of coming next, bright has a 25% probability, and every other token has 10% or less, quickly shrinking to less than 1%. Here is what that distribution looks like visually. When the curve has a tall spike on the left side, you could say the model was confident in its choice, with only one or possibly a few other tokens having any real chance of being chosen. A flatter distribution like this, on the other hand, can be interpreted as uncertainty. The model has many possible directions it could take the completion next, with no clear winner. Decoding and controlling this distribution curve is a big part of how you tune your LLM's behavior. So let's look at a few strategies to do this. One simple approach is to instruct the LLM to not actually make a random choice, and just always pick the token with the highest probability. This is known as greedy decoding. Greedy decoding's main upside is that it makes the LLM deterministic. If you feed your model the same prompt, it will always generate the same response. The primary downside of greedy decoding is that it can lead to text that is, well, predictable. The pros can end up feeling generic or even stilted. Another issue with greedy decoding is that the LLM will sometimes get stuck producing the same sequence of words over and over again. The LLM doesn't actually care if the overall completion makes sense. The LLM just keeps choosing the highest likelihood next token, and once the model falls into a repetitive loop, there's no mechanism to break out of it. Despite these potential shortcomings, greedy decoding can make sense in instances where highly predictable and deterministic output is desirable, like code completion or even as a temporary setting to debug your system. In most instances, you don't want to entirely eliminate randomness. You just want to control it. The most widely used parameter to control an LLM's randomness is called temperature. You can think of temperature like a dial that changes the shape of the probability distribution generated by your LLM. A default temperature of 1 just gives you the original distribution. A lower temperature leads to a more spiky distribution, with only the most likely tokens having any chance of being generated. The ordering of the tokens doesn't change, but their probabilities of being chosen do. Setting temperature all the way down to 0 sets the model to perform greedy decoding, with only the single most probable token having a 100% probability. Turning the temperature up a bit, say in the range of 1.1 to 1.3, will flatten out the probability distribution, giving unlikely tokens a bit more chance of being chosen. This leads to more variety and sometimes more interesting or even creative sounding text. Setting the temperature too high will result in a very flat probability distribution. All tokens will have about an equal chance of being chosen, even if they don't make that much sense. Whatever temperature you set your LLM to, that distribution curve will still have a long tail running out to the right. Full of nonsense tokens, your LLM has a small likelihood of choosing. To help control this, a few additional sampling techniques are used. Top k sampling is the most simple, and limits the LLM to choosing from the top k most likely tokens. For example, you might both set a temperature of 1.1, but also limit the LLM to choosing from the top 5 most likely next tokens. A similar approach is called top p sampling, which limits the LLM to choosing tokens with cumulative probability falling below some threshold. For example, you might set a top p of 85%. You would start from the left side of this distribution, and keep adding the probabilities of each token until the total is greater than 85%. Top p tends to be the more responsive or dynamic of the two approaches. In top k, the LLM always picks from the same pool of tokens, regardless of the shape of the distribution. With top p, if the LLM is fairly certain, meaning a few tokens have a very high probability, the LLM will limit its choices to the few most likely tokens. If instead, the LLM is more uncertain, meaning the distribution is flat, with no clear best choice, the LLM is allowed to choose from a much larger pool of potential tokens. Some techniques also target the probabilities of individual words, rather than the overall shape of the distribution. For example, large language models can have a tendency to repeatedly use the same word or phrase, which can sound unnatural. Many LLMs allow you to apply a repetition penalty, which decreases the probabilities of words that have already appeared in the completion. This can make the resulting text sound more natural and varied. Most LLMs also allow you to increase or decrease the probability of specific tokens, usually called logit biasing. This bias will permanently adjust those tokens' probability of being chosen up or down. If you know you don't want your RAG system to generate profanity, you could bias certain words down. On the other hand, if your RAG system is a classifier, designed to output one of a few categories, you could boost the probabilities of those categories to ensure the LLM always chooses from between them. Here's an API call combining many of the techniques you've seen in this video. This is a fairly sensible, general-purpose combination of parameters. A temperature of 0.8, a top p of 0.9, and a repetition penalty of 1.2. This LLM will be a little more conservative in its token choice, avoids choosing from the far tail of the distribution, and lightly penalizes repeated tokens. By experimenting with each parameter, you could dial in the LLM's behavior for the context of your application. There's a wide area of techniques available to control the randomness inherent in your LLM, and this video only covered a selection of the most common ones. In general, I advise setting a temperature and top p that best fits your needs. If you're generating code or answering factual questions, a lower temperature and a lower top p make sense. If you're operating in a more creative domain, a higher temperature and top p could give your LLM a more interesting and exploratory tone. After that, consider introducing repetition penalties, logit biases, or other sampling techniques you research in response to specific issues you identify in how your LLM is performing. Ultimately, understanding that there are many ways to tune an LLM's random choices, and iterating towards the settings that fit your project will get you the performance that you need.
```

## 关键引述/重要观点

> "Every token a large language model adds to your completion is a weighted random choice." [视频开头]

> "When the curve has a tall spike on the left side, you could say the model was confident in its choice, with only one or possibly a few other tokens having any real chance of being chosen." [概率分布解读]

> "A flatter distribution like this, on the other hand, can be interpreted as uncertainty. The model has many possible directions it could take the completion next, with no clear winner." [不确定性解读]

> "Greedy decoding's main upside is that it makes the LLM deterministic. If you feed your model the same prompt, it will always generate the same response." [贪婪解码优势]

> "The LLM doesn't actually care if the overall completion makes sense. The LLM just keeps choosing the highest likelihood next token, and once the model falls into a repetitive loop, there's no mechanism to break out of it." [贪婪解码缺陷]

> "In most instances, you don't want to entirely eliminate randomness. You just want to control it." [随机性控制理念]

> "You can think of temperature like a dial that changes the shape of the probability distribution generated by your LLM." [温度参数类比]

> "Top p tends to be the more responsive or dynamic of the two approaches." [Top P优势]

> "If you're generating code or answering factual questions, a lower temperature and a lower top p make sense. If you're operating in a more creative domain, a higher temperature and top p could give your LLM a more interesting and exploratory tone." [实践建议]

> "Ultimately, understanding that there are many ways to tune an LLM's random choices, and iterating towards the settings that fit your project will get you the performance that you need." [总结]

## 相关话题/关键词
- 大语言模型 (LLM)
- Token生成
- 概率分布
- 随机性控制
- 贪婪解码 (Greedy Decoding)
- 温度参数 (Temperature)
- Top K采样
- Top P采样 (核采样)
- 重复惩罚 (Repetition Penalty)
- Logit Biasing
- RAG系统
- 开源模型
- 确定性输出
- 文本生成
- API参数调优
- 创意生成
- 代码补全
- 模型置信度

## 技术信息
- 字幕字数: 7240
- 字幕字符数: 7240
- 时间戳条目数: 0
- 处理时间: 2026-05-28 14:12:35