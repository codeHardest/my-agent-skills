# 视频摘要：Handling hallucinations

## 基本信息

- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/rrngmz/handling-hallucinations
- **时长**: 456秒（约7分钟）
- **语言**: 中文
- **发布（原始）时间**: 2024-01-01
- **下载时间**: 2026-05-28 14:18:16

## 原始元数据

- （无额外元数据）

## 输出文件

- video.mp4 - 原始视频文件
- audio.mp3 - 音频文件
- subtitle.vtt - 带时间戳的字幕文件
- subtitle_ai-zh.json - 原始AI字幕JSON
- transcript.txt - 纯文本转录
- summary.md - 本摘要文件

## 内容概述

本视频探讨了在构建RAG（检索增强生成）系统时如何处理LLM（大语言模型）产生的幻觉问题。视频通过一个在线商店客服聊天机器人的具体案例说明了幻觉的危害性，阐述了幻觉产生的原因、类型以及检测和减少幻觉的多种策略，包括系统提示词优化、来源引用要求、ContextCite外部系统以及ALCE基准测试等内容。

## 核心要点

1. **幻觉问题的本质**：LLM被设计为生成概率性文本序列，而非区分真假信息，因此幻觉是LLM的固有特性。

2. **幻觉的危害**：幻觉信息听起来合理可信，难以被察觉；长期下来会导致用户对RAG系统失去信任。

3. **幻觉的类型多样性**：幻觉程度从轻微的数值错误（如折扣5%而非10%）到完全虚构（如根本不存在的学生折扣）不等。

4. **RAG系统的局限性**：虽然RAG是减少幻觉的最佳方法之一，但即使设计良好的RAG系统仍可能产生幻觉。

5. **自一致性检查方法**：让模型重复生成同一提示的完成内容，检查事实信息是否一致——如果产生幻觉，信息会不一致。

6. **知识库 grounding 的重要性**：确保LLM只能基于检索到的信息做出事实性声明，这是减少幻觉的核心方法。

7. **来源引用的作用**：要求模型在每个句子或段落末尾引用来源，可以提高模型基于检索文档回应的可能性，同时方便人工验证。

8. **幻觉引用的风险**：LLM可能幻觉出虚假的引用，某些经过微调的模型能更可靠地生成有效引用。

9. **ContextCite系统功能**：逐句处理响应，将每句话归属到检索提供的上下文文档之一，标记"No source"的句子说明缺乏支撑材料。

10. **ContextCite应用场景**：生成的标签可用于在最终LLM输出中生成来源引用，或作为评估LLM grounding 频率的一部分。

11. **ALCE基准测试**：提供预组装的知识库和示例问题，评估系统生成的响应的流畅性、正确性和引用质量三个关键指标。

12. **实践建议**：构建RAG系统是减少幻觉最有效的步骤；优化系统提示词确保LLM基于检索信息回答；使用幻觉相关基准测试验证系统表现。

## 详细内容

### 一、幻觉问题的背景与案例分析

视频开篇指出，幻觉是使用LLM时持续存在的担忧。即使是设计良好的RAG系统仍然可能产生幻觉，因此检测幻觉、减少幻觉以及确保LLM准确引用来源成为构建RAG管道中最重要的环节。

为了直观说明幻觉问题，课程引入了一个在线商店客服聊天机器人的场景。当用户询问公司是否提供学生折扣时，检索器找到了关于老年人和新客户折扣的信息（两者都可享受10%折扣）。同时，LLM的系统提示鼓励它对客户保持乐于助人的态度。在这些因素的综合影响下，LLM回复道：“当然可以，凭有效学生证可享受10%折扣，与我们为老年人和新客户提供的优惠一样。”用户感到满意并继续在网站上购物，期待在结账时获得折扣。然而，问题在于这个学生折扣实际上并不存在——LLM凭空编造了这个折扣。

这个案例清晰地展示了幻觉如何在RAG系统中发生，以及其潜在的危害性。

### 二、LLM产生幻觉的根本原因

理解LLM为什么会产生幻觉至关重要。语言模型被设计为生成概率性的文本序列，并加入少量随机化以增加多样性。概率性的文本序列通常是事实准确的，但并非总是如此。关键在于，语言模型的设计目的并非区分真伪，而只是区分高概率和低概率。

这意味着LLM的核心工作机制决定了它本质上不具备事实核查能力，而是倾向于生成看似合理的文本，这正是幻觉产生的根源。

### 三、幻觉问题的多重危害

幻觉问题之所以棘手，原因有以下几点。首先，最明显的原因是用户不希望语言模型向其提供不准确的信息，这对用户体验和信任度都是直接的损害。其次，几乎可以说幻觉的定义决定了它听起来是合理的，这使得它比完全荒谬的内容更难被检测出来。用户可能更容易识别出明显胡说八道的内容，但面对听起来头头是道的幻觉信息时却难以辨别真伪。最后，长期来看，偶尔出现的幻觉会导致用户对RAG系统失去信任，即使系统生成的大部分内容是准确的。这种信任的丧失可能是累积性的，一旦用户经历过一次幻觉带来的误导，就可能对整个系统产生怀疑。

### 四、幻觉的多种类型与程度

视频明确指出，幻觉可以有多种类型和程度。回到折扣这个案例，LLM可能准确地描述了真实存在的老年人折扣及其获取方式，但错误地将折扣金额说成5%而非10%。这是一种相对较轻的错误。在更极端的情况下，LLM可能错误地声称不存在老年人折扣，而实际上该折扣确实存在。或者如前文案例所示，完全凭空编造公司根本不提供的新折扣。

这意味着，如果想对LLM生成的文本准确性充满信心，需要在多个层面上评估文本内容。这种多层次评估的需求也反映了幻觉问题的复杂性和解决的困难性。

### 五、当前技术现实与RAG的价值

视频坦诚地指出了一个冷酷的现实：目前没有完美的幻觉解决方案，至少目前还没有。不过幸运的是，RAG是目前可用的最佳方法之一，而且有多种方法可以进一步优化RAG系统以减少幻觉发生的频率。

构建RAG管道的一个重大原因正是为了减少幻觉。从知识库中检索到的信息可以帮助LLM的回应有所依据，并可能提供模型训练数据中缺失的信息。即使如此，RAG系统仍然容易产生幻觉，因此采取额外的预防措施是必要的。

### 六、无知识库情况下的幻觉检测

在没有知识库的情况下思考如何检测LLM输出中的幻觉问题时，选择非常有限。课程介绍了一种称为“自一致性检查”的方法，即让模型多次为同一提示生成完成内容，然后检查其中包含的事实信息是否一致。其底层思想是，如果语言模型在幻觉信息，它会以不一致的方式进行，在不同的完成内容中会出现可检测到的事实差异。

然而在实践中，这种方法可能成本高昂且不可靠。每次生成都需要消耗计算资源，而且即使多次生成的结果不一致，也不能完全确定哪次是正确的。

### 七、基于知识库的幻觉减少策略

既然在RAG系统内部可以访问知识库，最好的减少幻觉方法就是确保回应基于检索到的信息。例如，可以修改系统提示，明确告诉LLM只能基于检索到的信息做出事实性声明。

如果希望更进一步确保LLM是基于检索文档进行回应的，可以要求LLM引用其来源。这有时意味着提示模型在每个句子或段落的末尾引用来源。这可以进一步提高LLM基于检索到的来源进行回应的可能性。同时，引用也使人工读者更容易验证回应中的声明。

### 八、引用幻觉的风险与ContextCite系统

这种方法存在一个风险：LLM可能会凭空编造引用。经过微调以引用来源的某些模型可以更可靠地生成有效引用。但如果希望对引用的准确性有更高的信心，则需要使用外部系统。

ContextCite就是这样一个系统，它对响应在一套源材料中的 grounding 程度进行评分。该系统逐句处理响应，将每句话归属到检索提供并提供给LLM的上下文文档之一。然后ContextCite为每句话生成标签，标注哪份文档是该句话的来源。在陈述没有支撑材料的情况下，会被标记为"No source"。某些实现甚至可能提供句子与识别的源文档之间的相似度分数。

这些标签既可以用来在最终生成的LLM输出中生成源引用，也可以作为评估LLM在多大程度上将其回应基于RAG系统检索文档的一部分。

### 九、ALCE基准测试体系

最近的努力，如ALCE基准测试，旨在衡量系统在生成回应时引用和引用来源的效果。该系统提供预组装的知识库和示例问题。然后可以使用RAG系统在这些提示上询问ALCE系统来评估生成的响应。

系统会为三个关键指标生成分数：流畅性（fluency）、正确性（correctness）和引用质量（citation quality）。换句话说，最终文本有多清晰，内容在事实上的准确程度如何，以及提供的引用与正确的来源对齐程度如何。

这些基准测试不能控制生产系统中的幻觉，但确实能让人了解系统在避免幻觉和引用来源方面的表现。

### 十、最佳实践总结

视频最后总结了构建可靠RAG系统的关键要点。幻觉检测是LLM系统面临的持续挑战。但是，通过构建RAG系统，已经迈出了最小化幻觉最有效的一步。在此之后，应该集中精力确保LLM基于检索到的信息进行回答，通过优化系统提示词来实现。最后，使用以幻觉为重点的基准测试来验证系统，确保系统提供有依据且引用良好的回应。

这些方法结合起来可以显著减少幻觉，帮助构建一个提供可信赖回应的系统。

## 完整字幕原文

```
Hallucinations are a constant concern when working with LLMs, and even a well-designed RAG system can still hallucinate. Detecting hallucinations, reducing them, and ensuring the LLM accurately cites sources are therefore the most important parts of building your RAG pipeline. Let's have a look at a few ways this is done. Imagine you get your first RAG system up and running. A customer service chatbot for an online store. A user writes in and asks if the company offers student discounts. The retriever finds information about discounts for both seniors and new customers, both of whom would receive 10% off. Meanwhile, the LLM system prompt encourages it to be helpful with customers. All of these factors influence the LLM, which responds, Absolutely, you can get 10% off with a valid student ID. The same great discount we offer our seniors and new customers. The user is delighted and continues shopping on your site, eager to claim their discount at checkout. The only problem? That student discount doesn't actually exist. The LLM just made it up. It's important to remember why LLMs hallucinate in the first place. A language model is designed to produce probable text sequences, with a bit of randomization thrown in for variety. Probable text sequences are often factually accurate, but not always. And language models aren't designed to differentiate between true and false, just probable and improbable. Hallucinations are problematic for a few reasons. The first is obvious enough. You just don't want your language model to provide inaccurate information to your user. The second is that, almost by definition, hallucinations sound plausible. And so can be more difficult to detect than total nonsense. Finally, over time, occasional hallucinations can cause your users to lose trust in your RAG system, even if the majority of generated content is accurate. Of course, a big reason you'd build a RAG pipeline is to reduce hallucinations. The information you retrieve from your knowledge base can help ground an LLM's responses and possibly provides information missing in the model's training data. Even so, RAG systems are still prone to hallucination, so additional steps to prevent them are necessary. Hallucinations can come in many types and sizes. Going back to that discount, an LLM might accurately describe the very real senior discount and how to claim it, but misstate the discount as 5% instead of 10%. In more extreme cases, the LLM might inaccurately state there isn't a senior discount when actually one exists. Or as you saw earlier, invent entirely new discounts your company doesn't offer. This means you'll need to evaluate the text your LLM generates on many levels if you want to feel confident in its accuracy. Now here comes the cold, hard truth. There's no perfect solution for hallucinations. Or at least not currently. Luckily, however, RAG is one of the best approaches currently available and there's ways you can refine RAG systems to further decrease the frequency of hallucinations. To start, think through how you'd detect hallucinations in LLM output if you didn't have a knowledge base. Without a trusted external source of truth to compare that output to, your options are pretty limited. One approach, however, is self-consistency checking, where you have the model repeatedly generate completions for the same prompt and check if the factual information contained within them is consistent. The underlying idea is that if the language model is hallucinating information, it'll do so inconsistently. And factual differences across completions will be detectable. In practice, however, this method can be costly and unreliable. If you have a knowledge base to reference, that's the best place to start. Since inside a RAG system, you do have access to a knowledge base, the best approach to decrease hallucinations is to ensure responses are grounded in retrieved information. For example, you could modify your system prompt to say that the LLM can only make factual claims based on retrieved information. If you want further confidence that the LLM is basing its responses on retrieved documents, you can further require the LLM to cite its sources. Sometimes, this just means prompting the model to cite sources at the end of each sentence or paragraph. This can further increase the likelihood that the LLM grounds its responses in the retrieved sources. And citations also make it easier for a human reader to verify claims in the response. A risk with this approach, however, is that the LLM will just hallucinate the citations. Some models fine-tuned to cite sources will generate valid citations more reliably. But if you want more confidence in your citations, you'll need to use an external system. For example, ContextCite is a system that scores how well a response is grounded in a set of source materials. The model processes the response sentence by sentence, and it attributes each sentence to one of the context documents that were retrieved and provided to the LLM. ContextCite then generates tags for each sentence, noting which document is the source of that sentence. In cases where the statement does not have supporting material, it's labeled no source. Some implementations may even provide a similarity score between the sentence and the identified source document. These tags can either be used to generate source citations in the final generated LLM output, or as a part of evaluation of how frequently the LLM is grounding its responses in the documents retrieved by a RAG system. Recent efforts, such as the ALCE benchmark, aim to measure how well a system references and cites sources when generating responses. The system provides pre-assembled knowledge bases and sample questions. You would then use your RAG system on these prompts to ask the ALCE system to evaluate the generated response. Scores are generated for three key metrics, fluency, correctness, and citation quality. In other words, how clear is the final text, how factually accurate, and how well do the provided citations align with the correct sources to cite. These benchmarks don't control hallucinations in your production system, but they do give some sense of how well your system is avoiding hallucinations and citing sources. Hallucination detection is a constant challenge in an LLM-based system. That said, by building a RAG system, you're already taking the single most effective step to minimize hallucinations. After that, focus your energy on ensuring the LLM grounds its answers and retrieved information by refining your system prompt. Finally, test your system using hallucination-focused benchmarks to ensure your system is providing grounded, well-cited responses. Together, these approaches can significantly reduce hallucinations and help you build a system that provides trustworthy responses.
```

## 关键引述/重要观点

> “Hallucinations are a constant concern when working with LLMs, and even a well-designed RAG system can still hallucinate. Detecting hallucinations, reducing them, and ensuring the LLM accurately cites sources are therefore the most important parts of building your RAG pipeline.”（幻觉是使用LLM时持续存在的担忧。即使是设计良好的RAG系统仍然可能产生幻觉。因此检测幻觉、减少幻觉以及确保LLM准确引用来源成为构建RAG管道中最重要的环节。）

> “A language model is designed to produce probable text sequences, with a bit of randomization thrown in for variety. Probable text sequences are often factually accurate, but not always. And language models aren't designed to differentiate between true and false, just probable and improbable.”（语言模型被设计为生成概率性的文本序列，并加入少量随机化以增加多样性。概率性的文本序列通常是事实准确的，但并非总是如此。语言模型的设计目的并非区分真伪，而只是区分高概率和低概率。）

> “Hallucinations are problematic for a few reasons... hallucinations sound plausible... can be more difficult to detect than total nonsense... over time, occasional hallucinations can cause your users to lose trust in your RAG system, even if the majority of generated content is accurate.”（幻觉问题之所以棘手，原因有以下几点……幻觉听起来是合理的……比完全荒谬的内容更难被检测出来……长期来看，偶尔出现的幻觉会导致用户对RAG系统失去信任，即使系统生成的大部分内容是准确的。）

> “Now here comes the cold, hard truth. There's no perfect solution for hallucinations. Or at least not currently. Luckily, however, RAG is one of the best approaches currently available and there's ways you can refine RAG systems to further decrease the frequency of hallucinations.”（现在迎来冷酷的现实：目前没有完美的幻觉解决方案，至少目前还没有。不过幸运的是，RAG是目前可用的最佳方法之一，而且有多种方法可以进一步优化RAG系统以减少幻觉发生的频率。）

> “The best approach to decrease hallucinations is to ensure responses are grounded in retrieved information.”（最好的减少幻觉方法是确保回应基于检索到的信息。）

> “ContextCite is a system that scores how well a response is grounded in a set of source materials. The model processes the response sentence by sentence, and it attributes each sentence to one of the context documents that were retrieved and provided to the LLM.”（ContextCite是一个对响应在一套源材料中的 grounding 程度进行评分的系统。该模型逐句处理响应，将每句话归属到检索提供并提供给LLM的上下文文档之一。）

> “Scores are generated for three key metrics, fluency, correctness, and citation quality. In other words, how clear is the final text, how factually accurate, and how well do the provided citations align with the correct sources to cite.”（系统会为三个关键指标生成分数：流畅性、正确性和引用质量。换句话说，最终文本有多清晰，内容在事实上的准确程度如何，以及提供的引用与正确的来源对齐程度如何。）

> “By building a RAG system, you're already taking the single most effective step to minimize hallucinations. After that, focus your energy on ensuring the LLM grounds its answers and retrieved information by refining your system prompt.