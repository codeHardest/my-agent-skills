# 视频摘要：Prompt engineering: advanced techniques

## 基本信息
- **来源**: Bilibili
- **URL**: https://learn.deeplearning.ai/courses/retrieval-augmented-generation/lesson/jjf7di/prompt-engineering%3A-advanced-techniques
- **时长**: 491秒 (约8分钟)
- **语言**: 中文
- **下载时间**: 2026-05-28 14:17:55

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
本视频介绍了RAG系统中高级提示工程技术的应用，包括上下文学习、少样本学习、思维链提示等核心概念，并深入探讨了推理模型的特点、使用场景以及上下文窗口管理策略。视频强调这些高级技术应根据实际需求选择性使用，简单有效的提示模板可能就已足够。

## 核心要点
1. **上下文学习（In-context Learning）**：通过在提示中添加示例来帮助LLM学习期望的输出格式和语气
2. **少样本学习（Few-shot Learning）**：包含多个示例的上下文学习方法
3. **单样本学习（One-shot Learning）**：仅包含一个示例的上下文学习方法
4. **硬编码示例**：将示例直接写入提示模板，适用于需要稳定LLM行为的场景
5. **动态检索示例**：使用RAG从知识库中检索相关示例，灵活适应不同问题
6. **思维链提示（Chain-of-Thought Prompting）**：引导LLM逐步推理，而非直接给出答案
7. **草稿纸技术（Scratchpad）**：为语言模型提供"思考空间"，组织思维后再回答
8. **推理模型（Reasoning Models）**：专门为复杂推理任务设计的LLM，内置分步推理能力
9. **推理令牌 vs 响应令牌**：推理模型先生成推理令牌（内部思考），再输出响应令牌
10. **推理模型特性**：擅长处理编码、数学、规划、谜题和复杂多步骤工作流
11. **推理模型成本**：比普通模型更慢、更贵，但准确性更高
12. **推理模型的提示技巧**：无需要求其"分步思考"，可能不适合上下文学习
13. **上下文窗口管理**：单轮对话验证技术有效性，多轮对话需上下文修剪
14. **上下文修剪策略**：固定保留最近消息、使用LLM摘要旧消息、丢弃推理令牌
15. **渐进式应用原则**：简单提示模板可能已足够，高级技术应在明确需要时才添加

## 详细内容（保留所有原始信息）

### 一、上下文学习（In-context Learning）

上下文学习是一种通过在提示中添加示例来引导LLM生成期望输出的技术。例如，构建客服聊天机器人时，提示中可以包含历史客户请求示例以及高质量回复示例。这些示例帮助LLM学习生成新响应时应使用的结构和语气。

**学习类型区分**：
- **少样本学习（Few-shot Learning）**：包含多个示例的上下文学习方法
- **单样本学习（One-shot Learning）**：仅包含一个示例的上下文学习方法

**实现方式**：

1. **硬编码示例**：将一个或多个示例问答直接写入提示模板。这种方法在需要稳定LLM行为的场景下可以帮助提高响应质量。

2. **动态检索示例**：如果想要每次更换示例，可以使用RAG从知识库中检索相关示例问答。例如，可以将成功的客户对话索引到向量数据库中，当新客户就某个主题进行咨询时，可以检索关于该主题的历史对话文本，并将其注入到提示中。这本质上就是普通RAG，但专门检索示例响应可以进一步提高LLM的响应质量。

### 二、思维链提示与推理技术

另一类强大的提示工程技术是鼓励LLM以逐步方式处理提示并推理。例如，可以告诉LLM先"出声思考"或"逐步思考"最佳方法，然后再提供最终答案。这种方法的核心理念是为语言模型提供一个"草稿纸"来组织其回答前的思路。

**常见实现方式**：

1. **草稿纸技术（Scratchpad）**：一种常见做法是告诉LLM，介于草稿纸标签之间的token被视为思考和头脑风暴的空间，不属于其最终答案的一部分。

2. **思维链提示（Chain-of-Thought Prompting）**：在这种方式中，LLM被指示以逐步方式处理问题，而不是立即回答。LLM可能先被指示生成回答问题所需的步骤，然后按照这些步骤执行。这种增量式规划和采取方法可以提高最终响应的准确性。由于LLM会展示其"工作过程"，当LLM推理出现偏差时也更容易追踪问题。

### 三、推理模型（Reasoning Models）

这类推理导向策略取得了巨大成功，以至于许多LLM现在从一开始就设计为推理模型。推理模型在复杂推理任务中表现出色，如编码、数学、规划、谜题以及需要多个步骤的复杂工作流。

**工作原理**：
- 推理模型首先生成推理令牌，在其中进行提前规划和选项考虑，类似于前面提到的草稿纸
- 然后输出带有用户预期最终响应的响应令牌

**访问权限差异**：
- 一些推理模型提供商只提供对这些最终响应令牌的访问
- 其他提供商则允许访问推理令牌

**成本与性能**：
- 推理令牌仍然是常规token，具有生成它们的所有相关成本
- 因此推理模型通常运行更慢、成本更高
- 但推理模型通常比非推理对应模型更准确

**在RAG系统中的应用**：
- 根据具体场景，围绕推理模型构建RAG系统可能非常值得
- 推理模型特别擅长评估检索文档的相关性
- 更擅长决定如何将信息整合到响应中，特别是需要更复杂推理步骤的响应

**推理模型的提示特点**：
- 不需要要求它们分步思考，因为这是它们已经训练好的能力
- 可能不适合使用上下文学习，因为它们会将提供的示例响应融入当前正在回答的问题中
- 对于具体的、期望它们努力实现的目标，以及关于期望回答格式的非常具体的信息，表现更好
- 仍可以提供高级指导原则，明确说明希望模型采取或避免的方法
- 然后可以直接提供从RAG系统检索的整个文档上下文
- 新模型（包括推理模型）不断发布，大多数LLM提供商会包含如何最佳提示它们的信息

### 四、上下文窗口管理

随着使用更多提示工程技术，上下文窗口管理变得至关重要。初始提示和LLM为完成而生成的任何token都会占用其上下文窗口的部分。

**增加上下文负担的因素**：
- 从检索器注入文档
- 在每个提示中添加上下文学习示例
- 让推理模型在回答前规划其响应

所有这些高级技术都会增加提示长度、生成响应长度，或两者同时增加。如果不注意，上下文窗口很容易快速被填满。

**单轮对话策略**：
- 最佳做法是验证是否从提示工程技术中获得价值
- 如果思维链提示或上下文学习没有带来更好的性能，最好将其从系统中移除

**多轮对话策略**：
- 多轮对话会快速消耗上下文窗口，因为每次来回消息都需要包含在提示中
- 一系列被称为"上下文修剪"的策略可以解决此问题

**具体修剪方法**：

1. **固定消息数量**：简单解决方案是只保留提示中固定数量的最近消息，例如用户和LLM发送的最后五条。

2. **LLM摘要**：更复杂的方法是使用单独的LLM来总结旧消息，缩小其大小但保留关键要点。

3. **丢弃推理令牌**：如果在多轮对话中使用推理模型，几乎肯定希望从聊天历史中丢弃推理令牌，只保留响应令牌。

4. **仅包含相关检索块**：在RAG系统中，通常只想包含支持回答最新问题的检索块，而不是之前每个问题的检索块。

**长上下文窗口模型**：
- 如果应用程序需要具有深度和丰富上下文的多轮对话，可以切换到使用具有更长上下文窗口的模型
- 但仍需谨慎设计提示，因为即使在具有更长上下文窗口的模型上，长提示运行起来也很慢且成本高昂

### 五、技术应用建议

提示工程技术可以提高LLM的性能，但RAG系统不一定需要使用它们。简单的提示模板和编写良好的系统提示可能就是项目所需的全部。

**建议原则**：
- 当涉及更高级技术时，建议只有在明确需要时才将它们添加到项目中
- 提示工程总体上更像是一门艺术而非科学
- 无论使用什么策略，都应该尝试不同的提示并找到最适合系统的那些

## 完整字幕原文
```
Once you have a basic prompt template set up for your RAG system, you can start trying more advanced prompt engineering techniques. Let's have a look at a few of those and when you'd want to use them. In-context learning is a technique which allows you to help the LLM learn what kind of output you wanted to generate by adding examples of them to the prompt. For example, if you're building a customer service chatbot, your prompt can include examples of previous customer requests, as well as high quality responses to those requests. These examples help the LLM learn the structure and tone it should use when it generates new responses. Just like in RAG, you're adding additional information to the prompt to ground the way the LLM responds. If you include many examples, this approach is called few-shot learning. If you include just one example, it's called one-shot learning. There's a few ways to implement in-context learning. You could just hard code one or more example questions and responses into your prompt. In situations where you want a stable set of LLM behaviors, this alone could help improve response quality. If you want to change up the examples each time, however, you can use RAG to retrieve example questions and responses from your knowledge base. For example, if you're working on that same customer service chatbot, you could index successful customer chats into your vector database. When a new customer writes in about a particular topic, you can retrieve the text of previous conversations about that topic and inject that text into your prompt. In many ways, this is just normal RAG, but the fact that you're specifically retrieving example responses can help further improve the quality of the LLM's response. Another powerful collection of prompt engineering techniques essentially encourages the LLM to reason through prompts in a step-by-step manner. For example, you can tell the LLM to first think aloud or think step-by-step about the best way to approach the problem before actually providing a final answer. The idea is you're essentially giving the language model a scratchpad to organize its thoughts before answering. A common way to do this is to tell the LLM that tokens between scratchpad tags are considered a space for thinking and brainstorming and not part of its final answer. A similar approach is called chain-of-thought prompting. In this approach, the LLM is instructed to tackle questions in a step-by-step manner rather than immediately answering them. The LLM might be instructed to first generate the steps needed to answer a question and then follow those steps. Encouraging the LLM to plan and take this incremental approach can increase the likelihood that the final responses are more accurate. Since the LLM will show its work, so to speak, it's also easier to trace down issues when the LLM's reasoning falls apart. Reasoning-oriented strategies like these have been so successful that many LLMs are now designed to be reasoning models right out of the box. Reasoning models excel at complex reasoning tasks such as coding, mathematics, planning, puzzles, and complex workflows that require multiple steps. Under the hood, these reasoning models first generate reasoning tokens where they might plan ahead and consider options much like the scratch pad you saw before. Then they output response tokens with the intended final response to the user. Some providers of reasoning models will only provide access to those final response tokens. Others allow you to access the reasoning tokens as well. These reasoning tokens are part of what makes these models more accurate than their non-reasoning counterparts, but they're still just regular tokens with all the associated costs of generating them. As a result, reasoning models are typically slower and more expensive to run. Depending on your context, building a RAG system around a reasoning model may be well worth the higher costs of each LLM call. For example, reasoning models can be particularly good at assessing the relevance of the retrieved documents and can be more skilled at deciding how best to incorporate that information into a response, especially one that requires more complex reasoning steps. Interestingly, many prompt engineering techniques don't work as well with reasoning models. For example, you don't need to ask them to think step-by-step as this is something they've already been trained to do. They also may not do well with in-context learning as they try to incorporate the provided example responses into the current question being answered. They tend to perform better with specific goals that you want them to work towards and very specific information about the format that you want them to answer in. You can still provide high-level guiding principles and explicitly state approaches you want the model to take or avoid. After that, however, you can just give them the entire context dump of documents retrieved from your RAG system. New models, including reasoning models, are constantly being released, however, and most LLM providers will include information about how best to prompt them. As you start employing more prompt engineering techniques, context window management will become important. Remember, the initial prompt and whatever tokens an LLM generates for the completion both use up portions of its context window. Whether you're injecting documents from your retriever, adding in-context learning examples to every prompt, or having a reasoning model plan its responses before answering a question, all of these advanced techniques increase the length of your prompt, the generated response, or both. It's easy to rapidly fill up your context window if you're not paying attention. With single-turn conversations, the best fix is to just validate you're getting value from your prompt engineering technique. If chain-of-thought prompting or in-context learning isn't giving you better performance, it's better to just remove those components from your system. Multi-turn conversations can quickly eat up your context window as each back and forth message needs to be included in the prompt. A variety of approaches collectively referred to as context pruning addresses this issue. A simple solution is to keep only a fixed number of recent messages in the prompt. For example, the last five sent by the user and the LLM. More sophisticated approaches use a separate LLM to summarize older messages, shrinking their size but preserving their key points. If you're using a reasoning model in a multi-turn conversation, you'll almost certainly want to drop reasoning tokens from the chat history and just keep the response tokens. Likewise, in a RAG system, you usually only want to include the chunks retrieved to support the response to the most recent question, not every question that came before it. Of course, if your application needs multi-turn conversations with deep and rich context, you can always switch to using a model with a longer context window. That said, you'll still want to be thoughtful about how you design prompts, as even on models with longer context windows, long prompts are slow and expensive to run. Prompt engineering techniques can improve the performance of your LLM, but your RAG system doesn't necessarily need to employ them. A simple prompt template and a well-written system prompt might be all you need for your project. When it comes to more advanced techniques, I advise you add them to your project only after it's clear you need them. Prompting in general can be more of an art than a science, so whatever strategies you use, experiment with different prompts and find the ones that work best for your system.
```

## 关键引述/重要观点
> "In-context learning is a technique which allows you to help the LLM learn what kind of output you wanted to generate by adding examples of them to the prompt." 上下文学习是一种通过在提示中添加示例来帮助LLM学习期望输出类型的技术。

> "If you include many examples, this approach is called few-shot learning. If you include just one example, it's called one-shot learning." 如果包含多个示例，这种方法称为少样本学习；如果只包含一个示例，则称为单样本学习。

> "You could just hard code one or more example questions and responses into your prompt." 你可以直接将一个或多个示例问答硬编码到提示中。

> "You can use RAG to retrieve example questions and responses from your knowledge base." 你可以使用RAG从知识库中检索示例问答。

> "Another powerful collection of prompt engineering techniques essentially encourages the LLM to reason through prompts in a step-by-step manner." 另一类强大的提示工程技术基本上是鼓励LLM以逐步方式处理提示并推理。

> "The idea is you're essentially giving the language model a scratchpad to organize its thoughts before answering." 这个理念本质上是为语言模型提供一个草稿纸来组织其在回答前的思维。

> "Chain-of-thought prompting - the LLM is instructed to tackle questions in a step-by-step manner rather than immediately answering them." 思维链提示 - LLM被指示以逐步方式处理问题，而不是立即回答。

> "Reasoning models excel at complex reasoning tasks such as coding, mathematics, planning, puzzles, and complex workflows that require multiple steps." 推理模型在复杂推理任务中表现出色，如编码、数学、规划、谜题以及需要多个步骤的复杂工作流。

> "These reasoning tokens are part of what makes these models more accurate than their non-reasoning counterparts, but they're still just regular tokens with all the associated costs of generating them." 这些推理令牌是使这些模型比非推理对应模型更准确的部分，但它们仍然是常规token，具有生成它们的所有相关成本。

> "As a result, reasoning models are typically slower and more expensive to run." 因此推理模型通常运行更慢、成本更高。

> "Many prompt engineering techniques don't work as well with reasoning models." 许多提示工程技术与推理模型配合使用效果不佳。

> "A variety of approaches collectively referred to as context pruning addresses this issue." 一系列被称为"上下文修剪"的策略可以解决此问题。

> "Prompt engineering techniques can improve the performance of your LLM, but your RAG system doesn't necessarily need to employ them." 提示工程技术可以提高LLM的性能，但RAG系统不一定需要使用它们。

> "Prompting in general can be more of an art than a science, so whatever strategies you use, experiment with different prompts and find the ones that work best for your system." 提示工程总体上更像是一门艺术而非科学，无论使用什么策略，都应该尝试不同的提示并找到最适合系统的那些。

## 相关话题/关键词
- RAG系统 (RAG System)
- 提示工程 (Prompt Engineering)
- 上下文学习 (In-context Learning)
- 少样本学习 (Few-shot Learning)
- 单样本学习 (One-shot Learning)
- 硬编码示例 (Hard-coded Examples)
- 动态检索示例 (Dynamic Retrieved Examples)
- 思维链提示 (Chain-of-Thought Prompting)
- 草稿纸技术 (Scratchpad Technique)
- 推理模型 (Reasoning Models)
- 推理令牌 (Reasoning Tokens)
- 响应令牌 (Response Tokens)
- 上下文窗口管理 (Context Window Management)
-