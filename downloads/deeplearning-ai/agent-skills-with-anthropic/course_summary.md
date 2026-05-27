# Agent Skills with Anthropic - 课程总结

**课程来源**: DeepLearning.AI
**课程链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic
**课程简介**: Equip agents with expert on-demand knowledge to enable reliable coding, research, and data analysis workflows

---

## 视频列表

| 序号 | 视频标题 | 时长 | 链接 |
|------|---------|------|------|
| 1 | Introduction | 2:46 | [链接](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/ldn5c3/ldn5c3) |
| 2 | Why Use Skills - Part I | 11:16 | [链接](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/bv2ekh/bv2ekh) |
| 3 | Why Use Skills - Part II | 8:33 | [链接](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/eg4sac/eg4sac) |
| 4 | Skills vs Tools, MCP, and Subagents | 7:34 | [链接](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/9iovmn/9iovmn) |
| 5 | Exploring Pre-Built Skills | 18:33 | [链接](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/cniu9q/cniu9q) |
| 6 | Creating Custom Skills | 16:15 | [链接](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/txwyf5/txwyf5) |
| 7 | Skills with the Claude API | 17:25 | [链接](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/3sq9za/3sq9za) |
| 8 | Skills with Claude Code | 24:52 | [链接](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/cniu9b/cniu9b) |
| 9 | Skills with the Claude Agent SDK | 20:23 | [链接](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/rmykgh/rmykgh) |
| 10 | Conclusion | 0:43 | [链接](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/dea3n4/dea3n4) |

---

## 视频 1: Introduction

**时长**: 2:46
**链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/ldn5c3/ldn5c3

### 内容总结

本课程由DeepLearning.AI与Anthropic合作开设，由Elie Schoppik担任讲师，介绍"Skills"（技能）这一扩展AI代理能力的重要概念。Skills是一组指令文件夹，为Claude Code和其他代理提供执行特定任务的新能力，采用开放标准格式，可跨多个代理产品部署。课程涵盖Skills的工作原理、创建最佳实践，并包含编码、研究、数据分析等多种应用场景的实践内容。

### 核心知识点

- 课程背景：由DeepLearning.AI与Anthropic合作开设，Elie Schoppik担任讲师
- Skills定义：Skills是包含指令的文件夹，能扩展代理的能力，提供专业化知识
- 开放标准：Skills采用标准化格式，兼容任何支持Skills的代理，可实现一次构建、多处部署
- SKILL.md文件：每个Skill必须包含SKILL.md文件，包含名称、描述和主要指令
- 多文件支持：主要指令可引用其他文件（脚本、额外Markdown文件）和资产（模板、图片等）
- 渐进式披露机制：Skill的名称和描述始终存在于代理的上下文窗口中，但仅在用户请求匹配时才会加载其他指令
- 基本工具要求：需要文件系统访问（读写文件）和bash工具（执行代码）
- 与MCP结合：代理可使用MCP从外部数据源获取数据，再依靠Skill处理数据
- 子代理集成：代理可委托任务给具有隔离上下文的子代理，子代理本身也可使用Skills
- 课程实践1：使用Claude AI创建营销活动Skill，结合Excel和PowerPoint的预构建Skills

---

## 视频 2: Why Use Skills - Part I

**时长**: 11:16
**链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/bv2ekh/bv2ekh

### 内容总结

本视频介绍了Skills的概念、优势和使用方法。通过一个营销活动数据分析的实际案例，展示了如何将重复的工作流程和专业知识打包成Skills，从而提高效率、减少上下文窗口占用，并实现跨平台的可移植性。视频还演示了创建SKILL.md文件、添加YAML元数据、创建文件夹结构、上传到Claude AI以及实际使用的完整流程。

### 核心知识点

- Skills是包含指令的文件夹，用于封装重复的工作流程、专业知识或新的功能
- 当发现自己反复输入相同的提示词时，应该考虑将其转化为Skills
- Skills可以提高上下文窗口的效率，只在需要时才加载相关信息
- SKILL.md文件是技能的核心，包含执行任务所需的指令集
- 每个Skills必须包含name（名称）和description（描述）的YAML元数据
- Skills可以引用同一父文件夹下的其他文件，如references文件夹
- 技能文件夹命名规则：小写字母、单词间用连字符、不使用保留关键字
- Skills是开放标准，可在多个平台使用（如Codex、Gemini CLI等）
- Skills可分享给团队成员并根据需要进行编辑
- 内置Skills（如创建电子表格的功能）可被直接调用
- Skills能够将CSV数据转化为可操作的洞察，输出多种文件格式

---

## 视频 3: Why Use Skills - Part II

**时长**: 8:33
**链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/eg4sac/eg4sac

### 内容总结

本课程深入探讨了Agent Skills的本质及其作为开放标准的重要性。课程从技术实现角度详细介绍了Skills如何通过文件系统加载（SKILL.md文件和子文件夹），以及Skills如何超越简单的文本引用而能够执行脚本。课程还阐述了引入Skills的三大核心价值：提供领域专业知识、实现可重复的工作流程、以及引入新能力。此外，课程重点讲解了Progressive Disclosure（渐进式披露）机制，通过分阶段加载数据来保护上下文窗口，避免不必要的令牌消耗。

### 核心知识点

- Skills是开放标准：Skills最初由Anthropic创建，现已成为开放标准，有特定规范，可在Codex、Gemini CLI、Claude Code、Open Code等多个平台使用
- 基于文件系统的架构：使用Skills需要通过文件系统加载包含SKILL.md文件的文件夹，以及可引用的子文件夹或文件
- 超越文本文件的灵活性：Skills不仅包含Markdown文档，还可以引用可执行脚本（如PDF处理、图像转换、表单提取等）
- 支持多种资产类型：Skills可包含图标、图片和其他资产，用于创建自定义样式和品牌
- 提供领域专业知识：Skills解决Claude可能不了解特定公司或团队运作方式的痛点，如设计新闻通讯、创建品牌指南等
- 从单用途代理到模块化架构：传统代理设计围绕单一目的（编码、研究、金融、营销等），需要特定工具和上下文；新架构采用简单脚手架（bash、文件系统），通过Skills提供领域专业知识
- 可重复的工作流程：在非确定性系统中，Skills提供清晰步骤和指令，使任务执行更加可预测
- 引入新能力：Skills可以引入代理本身不具备的功能（如生成演示文稿、Excel电子表格、PDF报告），通过最少额外上下文释放新功能
- 高度可移植性：Skills可在Claude AI、Claude Code、Agent SDK、API等环境中使用相同格式，实现跨生态系统共享和扩展
- 可组合性：多个Skills可以组合使用（如营销活动分析+PPT/PDF/Excel生成），构建复杂可预测的工作流程

---

## 视频 4: Skills vs Tools, MCP, and Subagents

**时长**: 7:34
**链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/9iovmn/9iovmn

### 内容总结

本课深入探讨了AI代理生态系统中的核心组件——Skills、Tools、MCP（Model Context Protocol）和Subagents——它们如何协同工作以创建强大的代理工作流。课程通过类比和实际案例（如Customer Insight Analyzer客户洞察分析器）详细说明了每个组件的独特价值、适用场景以及它们之间的相互关系，帮助学习者在构建AI应用时做出合理的技术选择。

### 核心知识点

- MCP（Model Context Protocol） 是连接AI代理与外部系统及数据的桥梁，适用于处理模型不知道的外部数据和上下文信息
- Tools（工具） 处于较低层级，提供访问系统和完成任务的基础能力，可通过内置、自定义或MCP加载
- Skills（技能） 是将工具组合成可重复工作流的指令集合，扩展代理的专业知识，支持渐进式加载
- Subagents（子代理） 是主代理派生的独立执行单元，拥有隔离上下文、细粒度权限控制，支持并行执行
- 工具定义始终驻留在上下文窗口中，而技能在需要时渐进加载，有助于管理上下文窗口空间
- Subagents可使用Skills，如代码审查子代理可调用定义公司代码审查流程的技能
- MCP提供底层工具和数据，Skills则提供使用这些工具构建特定工作流的指令
- Prompts是对话中最基础的原子单位，但本身难以在团队和公司层面规模化扩展
- Subagents支持跨会话持久化，可从子代理和主代理延续多个会话
- Skills支持跨对话持久化，可在与用户和AI应用的对话中保持一致性

---

## 视频 5: Exploring Pre-Built Skills

**时长**: 18:33
**链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/cniu9q/cniu9q

### 内容总结

本视频介绍了Anthropic提供的预构建技能（Pre-Built Skills），包括Excel、PowerPoint、Word、PDF等文档技能以及skill-creator技能创建工具。视频详细讲解了如何查看和使用这些技能，以及如何利用skill-creator程序化地创建自定义技能，并通过MCP服务器将技能与外部数据源（如BigQuery）结合，构建完整的数据分析和演示工作流程。

### 核心知识点

- Anthropic提供的预构建技能包括：Excel技能、PowerPoint技能、Word技能、PDF技能和skill-creator技能
- 技能分为两类：内置文档技能（Microsoft Docs、PDF、PowerPoint、Excel）在Claude AI中始终可用；示例技能默认关闭（除skill-creator外）
- 所有预构建技能可从github.com/anthropic/skills仓库获取，均已准备好用于生产环境
- PowerPoint技能包含SKILL.md文件，具有创建、编辑、分析PPT的功能，支持颜色、字体、设计原则等配置
- Skill-creator是一个元技能，用于程序化创建新技能，包含初始化、打包、验证三个Python脚本
- 技能创建流程遵循最佳实践：使用具体示例、规划可复用内容、明确步骤顺序
- MCP服务器可与技能结合，实现与外部数据源（如BigQuery）的连接
- 实际工作流程演示：从BigQuery查询营销数据→使用营销分析技能处理数据→应用品牌指南技能→生成PowerPoint演示文稿
- 技能创建时需要提供必要的上下文和数据输入，skill-creator虽高效但仍需人工指导
- 内置文档技能（Excel、PowerPoint等）是Claude AI的核心组成部分，无法通过开关控制

---

## 视频 6: Creating Custom Skills

**时长**: 16:15
**链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/txwyf5/txwyf5

### 内容总结

本课程深入探讨了Agent Skills的结构设计原则和创建最佳实践，通过两个具体示例——基于讲义生成练习题技能和时间序列数据特征分析技能——进行实战演示。课程随后展示了如何使用skill-creator对这些自定义技能进行评估，分析其是否符合最佳实践标准，并讨论了为技能编写单元测试以确保生产就绪的方法。

### 核心知识点

- 技能文件结构：每个技能必须包含SKILL.md文件，其中YAML Frontmatter部分需要name和description字段
- 命名规范：名称只能包含小写字母、数字和连字符，遵循"动词+ing"的命名形式，字符数有最大限制
- 描述撰写要点：不仅要描述技能功能，还要说明使用场景，并嵌入触发该技能的特定关键词
- 可选元数据字段：Agent Skills规范允许添加license、compatibility及任意键值对等可选字段
- 工作流设计原则：构建可预测的工作流，提供分步骤说明，明确处理边界情况，标注跳过某步骤的原因
- 代码行数控制：建议将SKILL.md控制在500行以内，超出时可引用外部文件、脚本或资产
- 路径使用规范：即使在Windows环境下也必须使用正斜杠，确保技能跨不同环境运行
- 自由度设计考量：遵循最佳实践的场景需要低自由度，创意输出场景可允许高自由度（多种颜色、样式、字体）
- 复杂工作流分解：多技能协作时应分解为顺序步骤，避免创建试图完成所有功能的单一庞大技能
- 目录结构规范：可选目录包括scripts（代码文件）、references（参考文档）、assets（资产文件如模板、图片、数据文件）

---

## 视频 7: Skills with the Claude API

**时长**: 17:25
**链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/3sq9za/3sq9za

### 内容总结

本课程介绍了如何通过Claude Messages API使用Skills，演示了代码执行工具（Code Execution Tool）和文件API（Files API）的具体使用方法。课程通过两个自定义Skills（生成练习题和时序分析）展示了在API环境中工作时的完整工作流程，包括技能的上传、调用、文件处理和程序化删除等操作。

### 核心知识点

- Claude AI/Claude Desktop中创建的Skills不会自动共享到Claude API或Claude Code
- 使用Claude API需要手动配置代码执行能力和文件处理能力（Claude AI/Claude Desktop默认已配置）
- 代码执行工具在隔离的沙箱环境中运行Bash/shell命令，提供独立的容器来执行代码
- 代码执行环境存在限制：无互联网连接、RAM/磁盘/CPU资源限制、预安装库
- Files API用于上传和下载文件到容器中进行处理
- 使用Skills时必须同时使用代码执行工具
- Skills的格式在不同环境中保持一致，但使用方式可能略有不同
- progressive disclosure机制允许Skills仅先读取SKILL.md，根据需要再读取其他文件
- 可以结合使用自定义Skills和内置Skills（如docx技能）
- 使用Sonnet模型时需要同时配置skills、code_execution和files API的beta headers

---

## 视频 8: Skills with Claude Code

**时长**: 24:52
**链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/cniu9b/cniu9b

### 内容总结

本视频深入讲解了如何在Claude Code中使用Skills进行代码生成、审查和测试。演示了通过CLAUDE.md文件设置项目上下文，创建Skills定义工作流程规范，以及创建配备Skills的Sub-Agents来实现代码审查和测试生成的高效协作模式。

### 核心知识点

- CLAUDE.md文件：用于指定项目通用指令、技术栈和Claude在每个对话中需要了解的信息，位于项目根目录，始终存在于上下文中
- Skills的创建与管理：Skills定义在.claude/skills文件夹中，可在项目级别和用户级别创建，包含名称、描述和工作流程规范
- adding-cli-command技能：定义了创建CLI命令的最佳实践，包括文件结构、类型注解规范、参数装饰器模式、显示方法使用等
- generating-cli-tests技能：用于生成pytest测试，包含fixtures定义、测试结构模式、边缘用例覆盖清单和测试运行命令
- reviewing-cli-command技能：用于代码审查，确保遵循最佳实践，检查结构、装饰器、注册方式、类型注解等
- Sub-Agents的创建：使用/agents命令创建，需要手动配置名称、描述、工具和技能，子代理不继承父代理的技能
- Sub-Agents技能加载机制：当子代理被调度时，整个SKILL.md文件会被预加载，而不是渐进式披露
- 多技能协作：主代理专注于开发，子代理分别负责审查和测试生成，提高上下文效率
- 项目架构模式：命令行任务管理应用使用Python + Typer + dataclasses + Rich，数据存储在JSON文件，使用uv管理依赖
- 技能适用性：Skills可以跨不同CLI框架和项目使用，只需适配特定的模式规范

---

## 视频 9: Skills with the Claude Agent SDK

**时长**: 20:23
**链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/rmykgh/rmykgh

### 内容总结

本课程作为最后一课，演示了如何使用Claude Agent SDK构建一个研究代理，该代理能够利用技能（Skill）基于开源工具的文档、GitHub仓库和网络搜索创建学习指南。研究代理包含一个主代理协调器和三个子代理（文档研究人员、仓库分析人员、网络研究人员），它们并行工作以收集信息，最终整合成结构化的学习路径，并通过MCP服务器将结果写入Notion等外部平台。

### 核心知识点

- Claude Agent SDK定义：Claude Agent SDK是一种编程方式，用于构建使用与Claude Code相同内部架构的代理应用程序。
- 主代理架构：主代理作为编排器，有权访问三个可用的子代理，分别负责文档查找、仓库结构分析和网络内容研究。
- 子代理工具配置：
- 技能（Skill）机制：技能用于指导主代理的工作流程，定义研究方法、需要提取和综合的内容，使用.md文件格式存储在.claude/skills目录中。
- 渐进式学习结构：采用渐进式披露（progressive disclosure）方法，将学习内容分为多个级别，从概述和动机、核心概念、实用模式到进阶方向。
- MCP服务器集成：通过MCP服务器连接外部服务（如Notion），使代理能够将输出写入集中式平台以便团队共享。
- 项目初始化：使用`uv init`初始化项目，添加依赖（claude-agent-sdk、python-dotenv、asyncio），创建agent.py文件。
- allowed_tools配置：必须明确列出主代理和子代理需要使用的所有工具，包括Write、Bash、WebSearch、WebFetch等读写工具。
- setting_sources配置：通过setting_sources参数指定技能文件的位置，包括用户目录和项目目录。
- 并行执行能力：子代理可以并行启动和执行，同时从不同数据源获取信息，提高研究效率。

---

## 视频 10: Conclusion

**时长**: 0:43
**链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/dea3n4/dea3n4

### 内容总结

本视频是"Agent Skills with Anthropic"课程的结业总结，讲师回顾了学习旅程的成果，强调了创建agent技能的最佳实践，包括从基础markdown说明开始、遵循渐进式披露原则、持续监控迭代等关键方法，并鼓励学习者运用所学知识创建自己的agent技能。

### 核心知识点

- 技能创建起点：从基本的markdown说明开始创建技能，然后按照渐进式披露（progressive disclosure）原则逐步扩展和深化
- 监控与迭代：在实际场景中持续监控agent如何使用技能，根据观察结果进行迭代改进
- 描述的完整性：确保技能的描述包含足够详细的上下文信息，使agent能够准确判断何时应该使用该技能
- 利用Claude的知识：Claude对"技能"概念有深入了解，可以作为创建技能的起点和参考
- 对话式创建：可以从简单的对话开始创建技能，利用自然语言描述需求
- Skill Creator技能：使用skill creator技能来遵循最佳实践和标准化的创建流程
- 跨平台应用：所学技能可以在不同平台上实践和应用
- 最佳实践探索：课程中涵盖了技能创建的最佳实践方法和标准
- 渐进式扩展：技能创建应该从简单开始，逐步增加复杂度和细节
- 实用导向：强调技能的实际应用价值和场景适应性

---
