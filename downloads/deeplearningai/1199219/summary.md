# 视频摘要：Choosing your LLM

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/vvs2mn/choosing-your-llm
- **时长**: 493秒 (约8分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:16:50

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
本视频深入探讨了在构建RAG（检索增强生成）应用时如何选择合适的大型语言模型（LLM）。内容涵盖了模型的可量化指标（如参数规模、成本、上下文窗口、推理速度等）、模型质量的评估方法（自动基准测试、人工评估、LLM作为评判者），以及如何根据具体项目需求做出明智的模型选择。视频强调LLM选择是一个重要但临时性的决策，需要随着模型能力的快速提升而不断调整。

## 核心要点
1. 模型大小是常见指标，小型模型约1-100亿参数，大型模型可达100-5000亿参数或更多，更大模型通常更强大但成本更高
2. LLM提供商通常按每百万token收费，输入和输出token价格可能不同
3. 上下文窗口决定了模型能处理的最大token数，包括prompt和completion
4. 首次生成token时间和tokens每秒速度是实时交互应用的关键指标
5. 训练截止日期表明模型训练数据的最新时间点
6. 基准测试分为三大类：自动基准测试、人工评分基准、LLM作为评判者
7. MMLU（大规模多任务语言理解）是覆盖57个学科的经典自动基准测试
8. 人类评估使用ELO算法（如国际象棋排名系统）比较不同LLM的响应质量
9. LLM Arena是最广泛引用的基准测试之一
10. LLM-as-a-judge存在家族偏见问题，需要仔细校准
11. 好的基准测试应具备相关性、区分度、可重复性、与实际性能对齐
12. 数据污染可能导致模型在基准测试中表现虚高
13. 基准测试会随时间推移而饱和，需要不断引入新的更具挑战性的评估标准
14. 模型选择是临时性决策，需要随着新模型的发布而更新

## 详细内容（保留所有原始信息）

### 一、引言：RAG应用中LLM选择的重要性

构建RAG应用时的主要决策之一是选择使用哪个LLM。市场上存在种类繁多的LLM，它们具有不同的性能水平、独特的能力和不同的成本结构。选择正确的模型对应用的速度、质量和预算都有重大影响。

### 二、可量化的LLM差异指标

#### 2.1 模型大小（Model Size）
模型大小是经常被引用的指标，通常以模型包含多少十亿参数来衡量。较小模型可能有10-100亿参数，而较大模型有100-5000亿甚至更多。更大的模型通常（但并非总是）比小型模型更有能力，但运行成本也更高。

#### 2.2 成本（Cost）
成本当然是重要因素。LLM提供商通常按每百万token的固定价格收费，有时输入和输出token的价格不同。一般来说，新型、更大、更有能力的模型价格更高。

#### 2.3 上下文窗口（Context Window）
模型的上下文窗口告诉您LLM可以处理的最大token数，分摊在prompt和completion之间。较大的限制为长prompt和completion提供更多灵活性，但您仍然按token付费。

#### 2.4 推理速度（Speed）
首次生成token的时间和速度（以tokens每秒表示）是另一个重要因素。如果您的RAG系统依赖实时交互，您可能愿意容忍其他方面的性能下降，换取快速和低延迟的模型。

#### 2.5 训练截止日期（Training Cutoff Date）
模型的训练截止日期或知识截止日期告诉您模型训练数据中代表的最新时间点。即使在RAG系统中，较晚的截止日期通常被认为是更好的，特别是在模型需要回答有关时事问题的场景中。

### 三、质量评估的难点与基准测试

虽然易于量化的指标可能有助于缩小您考虑的模型范围，但通常您最关心的是模型的质量，而这可能更难量化。这里的质量涵盖了LLM的所有能力，从解决复杂数学问题的推理能力，到简单生成可读性强的文本。

为了帮助在质量的各个维度上比较模型，有大量令人眼花缭乱的LLM基准测试可供选择，试图对LLM进行评分和比较。没有单一的权威基准测试列表可以供您参考，但了解可用的各种选项可以帮助您选择最适合项目的基准测试。

### 四、三种基准测试类型

#### 4.1 自动基准测试（Automated Benchmarks）
自动基准测试对LLM进行可由代码评估的任务评分。这种基准测试的经典格式可能是对特定兴趣领域的多项选择测试，或一系列数学或编程挑战，其中LLM的响应可以很容易地由计算机验证。好的例子是MMLU（大规模多任务语言理解），它使用多项选择测试覆盖从STEM到人文到法律的57个科目。其他基准测试测试LLM在数学问题到常识推理问题等各个方面的表现。您经常看到LLM提供商在其模型的市场宣传中使用这些基准测试的性能数据，并且很可能找到与您项目相关的基准测试。

#### 4.2 人类评分基准（Human-Evaluated Benchmarks）
人类评估的基准测试通常是这样工作的：让两个匿名的LLM对同一个prompt做出响应，然后让人类评估者选择他们更喜欢哪个响应。这些结果被输入到用于排名国际象棋选手的相同ELO算法中，从而产生LLM的比较排行榜。这种评级系统的流行主办方叫做LLM Arena，其排名是最广泛引用的LLM基准测试之一。这些人类评分排名捕捉了自动基准测试难以轻易衡量的微妙质量因素。虽然自动和人类评分指标通常会一致，但当它们的分数出现分歧时，可以突出模型性能的重要细微差别。

#### 4.3 LLM作为评判者（LLM as a Judge）
LLM作为评判者的基准测试使用一个LLM来评价另一个LLM对一组测试问题的响应。评判LLM可以访问一组参考答案，本质上只是判断被评估的LLM提供正确答案的频率。这给了您一个可以用来比较一个LLM与另一个LLM的胜率。LLM-as-a-judge的主要优点是它是评估LLM的一种相对便宜和灵活的方式。这种方法的一个缺点是评判者需要仔细校准，因为他们倾向于偏好自己同系列的语言模型的答案。例如，来自OpenAI的GPT模型会偏好其他GPT模型。来自Google的Gemini模型会偏好其他Gemini模型。通过重新校准这些现成的模型，可以减少这种偏见。

### 五、好的基准测试应具备的特点

好的基准测试有几个特点。首先，它们与您的项目相关。如果您的应用程序永远不会生成代码，那么在代码生成基准测试上比较LLM并没有太大帮助。其次，基准测试需要有难度才能很好地区分高性能和低性能的模型。如果每个模型在基准测试上都表现良好，那它就没什么用处。基准测试应该是可重复的，这意味着分数本身在测试运行之间不会发生剧烈变化，模型提供商引用的结果应该是可验证的。基准测试也应该与真实世界性能保持一致。在编程基准测试上表现良好的LLM应该在实践中实际写出好的代码。在这里，您可能需要阅读一些开发者论坛，以确保基准测试分数是实际性能的良好指标。产生这个问题的原因之一是数据污染。大型语言模型是在从互联网抓取的数十亿甚至数万亿token上训练的。基准测试使用的数据集可能包含在训练数据中。在这种情况下，语言模型可能会因为在训练期间已经看到完全相同的问题和答案而在该基准测试上表现过好。

### 六、基准测试的饱和与进化

虽然基准测试可以帮助您区分模型，但它们也突出了整个领域的发展速度。以下是您会在大多数LLM评估中看到的重复模式。首先，每个模型的平均分数相当低。然后，在短短几年内，模型达到人类专家水平变得司空见惯。这些基准测试被称为饱和，意味着它们不再帮助区分模型，因为几乎所有高级模型都接近最高分。在这种情况下，需要引入新的更具挑战性的基准测试来有意义地衡量性能的提升。然而，这些新的评估本身很快就会饱和，需要引入更新的评估。

### 七、结论与建议

主要结论是，今天发布的模型通常比仅仅一两年前的模型明显更好，而且您今天选择的任何模型可能都需要被更强大的模型快速替换。选择正确的LLM是设计RAG系统的一个重要但临时性的决策。易于量化的因素如成本或延迟可以帮助缩小您的选择范围，各种质量指标可以指向与您的用例最佳对齐的最佳模型。由于模型改进的速度，您应该计划最终更换新发布的适合您RAG系统的模型。

## 完整字幕原文
```
A major decision when building a RAG application is which LLM you'll use. There's a huge variety of LLMs available, with different levels of performance, unique capabilities, and different cost profiles. Choosing the right one can have a big impact on your application's speed, quality, and budget. So let's have a look at how you can make the choice that best fits your project. Let's start with some easily quantifiable differences between LLMs. Model size is a frequently quoted metric, usually measured by how many billions of parameters the model has. Small models may have between 1 and 10 billion parameters, while larger models have 100 to 500 billion, and possibly more. Larger models are typically, but not always, more capable than their smaller counterparts, but they're always more expensive to run. Cost is of course an important factor. LLM providers typically charge you for a fixed price per million tokens, sometimes with different prices for input and output tokens. You can generally expect newer, larger, and more capable models to cost more. The context window of a model tells you the maximum number of tokens an LLM can process, split between both the prompt and the completion. While large limits offer more flexibility to have long prompts and completions, you still pay per token. The time to first token, and speed, as expressed in tokens per second, is another important factor. If your RAG system depends on real-time interactions, you might be willing to tolerate worse performance in other areas for a fast and low-latency model. The training cutoff date, or knowledge cutoff date, of a model tells you the last point in time represented in a model's training data. Even in a RAG system, a later cutoff is typically considered preferable, especially in contexts where a model will need to respond to questions on recent events. While easily quantifiable metrics might help narrow down which models you consider, usually you care most about the quality of a model, which can be a lot harder to quantify. Quality here means everything from an LLM's ability to reason through complex math problems, to simply producing text that's pleasant to read. To help compare models across all these different dimensions of quality, there is a dizzying array of LLM benchmarks available that try to score and compare LLMs. There's no single authoritative list of benchmarks that you can turn to, but understanding the variety of options available can help you choose the benchmark that makes the most sense for your project. Benchmarks come in three high-level varieties, automated benchmarks, human scoring, and LLM as a judge. Automated benchmarks score LLMs on tasks that can be assessed with code. A classic format for this kind of benchmark might be a multiple choice test on a particular field of interest, or a series of mathematical or coding challenges where the LLM's responses can be easily validated by a computer. A good example benchmark here is MMLU, or Massive Multitask Language Understanding, which covers 57 subjects ranging from STEM to humanities to law using multiple choice tests. Other benchmarks test LLMs on everything from math problems to common sense reasoning questions. You'll frequently see LLM providers market their model's performance on these benchmarks, and can likely find the one that is relevant to your project. Human-evaluated benchmarks typically work by having two anonymous LLMs respond to the same prompt and asking human evaluators to choose which response they prefer. These results are fed to the same ELO algorithm used to rank chess players, resulting in a comparative leaderboard of LLMs. A popular host of this type of rating system is called LLM Arena, whose rankings are one of the most widely cited LLM benchmarks. These human-graded rankings capture nuanced quality factors that automated benchmarks can't easily measure. While automated and human-graded metrics will often agree, when their scores diverge, it can highlight important nuances in model performance. LLM-as-a-judge benchmarks use one LLM to rate another LLM's responses to a collection of test questions. The judge LLM has access to a set of reference answers, and essentially just determines how often the LLM being evaluated provides an answer that is close to the correct one. This gives you a win rate that can be used to compare one LLM versus another. LLM-as-a-judge's primary upside is that it's a relatively cheap and flexible way to evaluate LLMs. One downside of this approach is that the judge needs to be carefully calibrated because they have a tendency to prefer answers from their own family of language models. For example, GPT models from OpenAI will prefer other GPT models. Gemini models from Google will prefer other Gemini models. By recalibrating these off-the-shelf models, it's possible to diminish this bias. Good benchmarks have a few qualities. First, they're relevant to your project. If your application won't ever generate code, comparing LLMs on a code generation benchmark isn't much help. Next, benchmarks need to be difficult to do a good job differentiating between high and low performing models. If every model scores well on a benchmark, it's just not that useful. Benchmarks should be reproducible, meaning the scores themselves don't change drastically between testing runs, and the outcomes quoted by the model providers should be verifiable. Benchmarks should also align with real-world performance. An LLM that does well on a programming benchmark should actually write good code in practice. Here, you may need to do some reading on developer forums to ensure benchmark scores are a good indication of actual performance. A reason this problem can arise is data contamination. Large language models are trained on billions, if not trillions of tokens scraped from the internet. It's possible that the data set used by the benchmark are included in that training data. In this case, the language model might overperform on that benchmark because it's already seen the exact questions and answers during its training. While benchmarks can help you differentiate between models, they also just highlight how rapidly the field as a whole is evolving. Here's the general pattern you'll see repeated for most LLM evals. At first, the average score for each is quite low. Then, over only a few years, it becomes commonplace for models to perform on par with human experts. These benchmarks are called saturated, meaning they no longer help differentiate between models, as almost all advanced models score near the maximum. At that point, new and more challenging benchmarks need to be introduced to meaningfully measure improvements in performance. Those new evals will quickly become saturated themselves, however, and even newer ones will need to be introduced. The main takeaway here is that models released today are usually significantly better than models from even a couple of years ago, and that any model you choose today likely will need to be replaced as more capable models are rapidly introduced. Choosing the right LLM is an important but temporary decision for how you design your RAC system. Easily quantifiable factors like cost or latency can help narrow down your choice, and a wide variety of quality metrics can point you towards the best models to align with your use case. Thanks to the speed at which models are improving, you should plan on eventually swapping in newly released models that suit your RAC system.
```

## 关键引述/重要观点

> "A major decision when building a RAG application is which LLM you'll use. There's a huge variety of LLMs available, with different levels of performance, unique capabilities, and different cost profiles." 

> "Larger models are typically, but not always, more capable than their smaller counterparts, but they're always more expensive to run."

> "You can generally expect newer, larger, and more capable models to cost more."

> "If your RAG system depends on real-time interactions, you might be willing to tolerate worse performance in other areas for a fast and low-latency model."

> "Even in a RAG system, a later cutoff is typically considered preferable, especially in contexts where a model will need to respond to questions on recent events."

> "Quality here means everything from an LLM's ability to reason through complex math problems, to simply producing text that's pleasant to read."

> "The judge needs to be carefully calibrated because they have a tendency to prefer answers from their own family of language models. For example, GPT models from OpenAI will prefer other GPT models. Gemini models from Google will prefer other Gemini models."

> "Benchmarks should also align with real-world performance. An LLM that does well on a programming benchmark should actually write good code in practice."

> "Large language models are trained on billions, if not trillions of tokens scraped from the internet. It's possible that the data set used by the benchmark are included in that training data."

> "These benchmarks are called saturated, meaning they no longer help differentiate between models, as almost all advanced models score near the maximum."

> "The main takeaway here is that models released today are usually significantly better than models from even a couple of years ago, and that any model you choose today likely will need to be replaced as more capable models are rapidly introduced."

> "Choosing the right LLM is an important but temporary decision for how you design your RAC system."

## 相关话题/关键词

- RAG (检索增强生成)
- LLM选择
- 模型大小 (Model Size)
- 参数数量 (Parameters)
- 成本 (Cost)
- 每百万token价格 (Price per million tokens)
- 上下文窗口 (Context Window)
- 推理速度 (Inference Speed)
- 首次生成token时间 (Time to First Token)
- 训练截止日期 (Training Cutoff Date)
- 知识截止日期 (Knowledge Cutoff Date)
- 模型质量评估 (Model Quality Evaluation)
- 基准测试 (Benchmarks)
- MMLU (大规模多任务语言理解)
- 自动基准测试 (Automated Benchmarks)
- 人类评估基准 (Human-Evaluated Benchmarks)
- ELO算法 (ELO Algorithm)
- LLM Arena
- LLM-as-a-judge
- 数据污染 (Data Contamination)
- 基准测试饱和 (Benchmark Saturation)
- 实时交互 (Real-time Interactions)
- 低延迟 (Low-latency)
- 家族偏见 (Family Bias)
- 可重复性 (Reproducibility)
- 真实世界性能 (Real-world Performance)

## 技术信息
- 字幕字数: 7515
- 字幕字符数: 7515
- 时间戳条目数: 0
- 处理时间: 2026-05-28 14:16:50