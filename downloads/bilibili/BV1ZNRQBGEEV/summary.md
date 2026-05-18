# 视频摘要：【关键时刻】AI芯片行业深度分析：中国推荐公司寻找英伟达替代方案Vol.0117

## 基本信息
- **来源**: Bilibili
- **URL**: https://www.bilibili.com/video/BV1ZNRQBGEEV
- **时长**: 2638秒 (约43分钟)
- **语言**: 中文
- **下载时间**: 2026-05-13 10:44:37

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
本期深度分析探讨了一个看似矛盾的现象：中国科技巨头正在大量订购技术上落后至少两代的AI芯片，而生产这些芯片的华为公司AI处理器收入却从2025年的75亿美元飙升至今年的120亿美元，实现60%的惊人增长。视频深入分析了这一现象背后的结构性市场力量、全球监管框架、华为的技术战略转型（从训练转向推理）、Nvidia在中国市场的困境与监管僵局，以及Morgan Stanley预测的中国AI芯片市场到2030年将达到670亿美元、其中86%将由国内厂商供应的宏大图景。

## 核心要点

1. **收入暴涨悖论**: 华为AI处理器收入从2025年的75亿美元增长到2026年的120亿美元（60%增长），尽管其芯片技术上落后行业标准至少两代

2. **950PR处理器主导市场**: 华为最新量产的950PR处理器于今年3月进入量产阶段，需求远超供应，升级版950DT计划于第四季度推出

3. **SMIC制造扩张**: 为弥补7纳米及更老制程的低良率问题，中芯国际计划今年晚些时候再启用两座专门为华为AI芯片建设的晶圆厂

4. **Nvidia H20禁售令**: Nvidia曾为符合美国出口管制专门设计降级版H20芯片，2025财年在中国销售171亿美元，但随后美国政府直接禁止H20对华销售

5. **H200芯片监管僵局**: 尽管Nvidia于今年3月获得H200对华销售许可，但截至目前实际出货量为零，原因是美方要求芯片必须留在中国境内使用，而中方则要求只能用于海外业务，两项条件相互矛盾

6. **战略技术转型**: 华为认识到无法在原始算力上与Nvidia竞争，选择专注于推理（inference）而非训练（training），将950PR架构定位为推理专用

7. **推理与训练的技术差异**: 训练如同准备大型考试，需要海量算力；推理如同实际应考，每次用户查询都会触发，是记忆带宽密集型而非算力密集型任务

8. **电信背景优势利用**: 华为利用其作为全球最大电信公司之一的核心竞争力，通过先进专有互连技术将950PR处理器连接成大规模计算集群，最小化芯片间延迟

9. **DeepSeek成功案例**: DeepSeek采用华为950PR进行其最新DeepSeek V4架构的推理工作，实现了改进的推理效率和比国外硬件替代方案更低的运营成本

10. **双轨制工作流程**: 大多数计算密集型的模型训练工作仍使用Nvidia芯片（来自制裁前的库存），而日常推理部署则转移至华为芯片集群

11. **CUDA生态护城河**: Nvidia真正的竞争优势不仅是硬件，更是CUDA软件平台——一个经过15年以上构建的库、工具和开发者生态系统的集合

12. **CAN软件平台困境**: 华为的替代软件生态系统CAN比CUDA晚了整整十年开发，开发者经常需要从零编写低级内核，在调试问题上耗费数周时间

13. **Morgan Stanley市场预测**: 分析师预测中国国内AI芯片市场今年约210亿美元，到2030年将扩大至670亿美元，其中86%将由国内厂商供应

14. **结构性监管观点**: Morgan Stanley认为出口管制不是暂时的政策响应，而是市场的长期结构性特征，地缘政治界线已被永久绘制

15. **Jensen Huang的担忧**: Nvidia CEO黄仁勋明确表示顶级实验室优先为华为架构优化模型是"对我们国家的可怕结果"，将其提升至国家安全和技术主权问题

## 详细内容（保留所有原始信息）

### 一、现象引出：落后芯片的巨额订单

视频开篇揭示了一个看似矛盾的现象：尽管中国科技巨头正在订购技术上至少落后两代的AI芯片，但生产这些芯片的华为公司AI处理器收入却在飞速增长。具体而言，华为AI处理器收入从2025年的75亿美元增长到2026年的120亿美元，增幅达60%。这一现象颠覆了传统的硅谷叙事——通常人们认为最快、最节能的处理器会自动赢得市场，但现实表明这是一堂关于公司如何利用结构性市场力量并在全球监管网络中航行的大师课。

### 二、华为950PR处理器：生产与供应现状

#### 2.1 产品与产能

根据报道，中国科技集团正在积极接收一款名为950PR的处理器，该处理器于今年3月刚进入量产阶段，需求已经远超供应。此外，华为还有一款升级版950DT，计划于今年第四季度推出，展示了其激进的产品路线图。

#### 2.2 SMIC的制造能力

华为在受制裁的环境下将产量扩大60%，需要在中国内部具备强大的制造能力。他们几乎完全依赖SMEC（ Semiconductor Manufacturing International Corporation，中芯国际）。作为中国领先的晶圆代工厂，为处理这种规模的产量，尤其是在较老的光刻设备上，基本上需要投入大量人力和物理空间。由于无法获取最先进的极紫外光刻机（EUV），制造这些芯片涉及非常复杂的多重曝光工艺，这自然导致每片晶圆的良率较低。为弥补低良率并仍达到120亿美元的收入目标，中芯国际正在超大规模扩张产能。

#### 2.3 "建厂解决良率问题"策略

如果无法从单片硅晶圆获得足够多的合格芯片，就建设全新工厂来处理更多晶圆——通过绝对数量来"淹没整个区域"。视频以形象的比喻解释：假设你需要经营一家大型企业物流公司，但只能购买独立本地制造的快递车而非顶级货运卡车，整个车队天生就更慢。

### 三、市场准入：决定性因素

#### 3.1 Nvidia的主导地位与H20芯片

要理解950PR的市场主导地位，必须回顾原有市场格局。Nvidia曾在该领域占据绝对统治地位。在2025财年，Nvidia在中国销售了价值171亿美元的芯片。但这些并非旗舰产品——Nvidia专门设计了一款名为H20的高度特化的降级版芯片，刻意限制其互连速度和计算性能，以保持在触发美国出口管制的阈值以下。H20是Nvidia进入中国市场的生命线，使其能够遵守华盛顿规定的同时，仍为中国科技公司提供熟悉的Nvidia软件生态系统。

#### 3.2 H20禁售令的冲击

然而，华盛顿关闭了这个漏洞——大约一年前，美国政府直接禁止H20对华销售，法律阈值发生变化，Nvidia突然被切断了171亿美元的收入来源。

#### 3.3 H200许可的虚假曙光

随后Nvidia推出了最新硬件H200芯片。今年3月，Nvidia CEO黄仁勋宣布公司终于获得美国出口许可，可向中国客户出售新型H200芯片。表面上看起来冻结期结束了，但实际上物流情况讲述了完全不同的故事。尽管Nvidia自3月以来一直持有美国许可，但截至目前，H200对中国的实际出货量为零。

#### 3.4 监管僵局："高速公路与行车道"悖论

这是一个奇异的监管难题：两个竞争的政府发布了基本上使供应链实际冻结的指令。一方面，美国监管机构要求Nvidia芯片订单只能在中国境内部署和使用，不能离开该国（防止流向第三方）。另一方面，北京发布了自己的严格指令：要求中国科技公司为所有内部国内数据中心购买国产硬件（如华为），并将Nvidia芯片的使用限制在海外业务。

视频使用了绝妙的类比：这就像两个离异的父母为一个青少年和家庭用车制定规则。妈妈说只允许在高速公路上开车，爸爸说只允许在车道上行驶。结果不是妥协，而是汽车完全停放、引擎关闭。H200没有海关清关的可能。买卖双方都存在意愿，库存也充足，但产品无法在任何物理位置上合法存在。

### 四、华为的战略技术转型

#### 4.1 从训练到推理的转向

华为很快意识到无法在原始算力上赢得与Nvidia的正面对抗，因此改变了竞争规则。他们没有试图在计算密集型的AI模型训练阶段匹配Nvidia，而是将950PR架构专门定位用于推理（inference）。

#### 4.2 训练与推理的技术区分

**训练**：如同准备一场大型考试，需要阅读所有书籍、建立数百万个连接，需要在数千个GPU上移动大量矩阵，不断更新数十亿参数。这是疯狂的计算密度和内存带宽需求。

**推理**：这是实际参加考试，是前向传播，模型只是在生成响应（如输入提示到LLM时）。推理确实是记忆带宽密集型的，但每次操作所需的原始计算周期比训练阶段要少得多。

#### 4.3 推理的长期经济价值

训练一个万亿参数模型是一次性的大规模资本支出，按周期性进行。而推理则发生在每次用户查询AI助手、要求汽车导航或让客服机器人重写电子邮件时。因此，随着AI代理在全球范围内扩展，每天的推理请求量将完全超过训练所消耗的计算周期，数量级达到。

华为将950PR专门适配推理工作负载，意味着将自己定位在最大和未来AI需求的关键瓶颈。

#### 4.4 集群计算策略

虽然优化推理不能神奇地消除两代硬件差距，但华为利用其历史核心能力来弥补单个芯片的劣势。在成为AI芯片制造商之前，华为是全球最大的电信公司之一，根基在网络技术。他们使用高度先进的专有互连技术将这些950PR处理器连接在一起，构建大规模计算集群，最小化芯片间延迟。

这就像意识到单个明星球员不如对手快，于是建立一支高度协调的略慢球员团队，通过完美的传球配合取胜。网络本质上成为计算机——如果单个处理器无法足够快地处理参数权重，就将负载分布到高度协调的集群中。

#### 4.5 DeepSeek的成功验证

DeepSeek最近以其高效率模型震惊业界，他们将华为950PR用于最新的DeepSeek V4架构。DeepSeek是完美的测试案例，因为他们以执着于降低计算成本著称。报告显示，通过部署华为的集群芯片，DeepSeek实现了改进的推理效率，与国外硬件替代方案相比显著降低了运营成本。

然而，报告中埋藏着一个关键细微差别：DeepSeek专门将950PR用于推理，但大多数计算密集型工作——即V4模型的训练——仍在Nvidia芯片上执行。华为的网络集群令人印象深刻，但Nvidia在训练阶段的原始算力优势基本未被撼动。这突出了一个分化的管道：公司在出口管制收紧前用囤积的先进Nvidia芯片训练基础模型，然后将完成的模型部署到华为芯片的大规模集群上处理日常推理工作。

### 五、软件生态系统：CAN与CUDA的差距

#### 5.1 CUDA的统治地位

硬件集群只解决了物理瓶颈。没有运行它的软件，硅基本上只是昂贵的沙子。Nvidia真正的护城河——开发者如此积极捍卫使用其芯片的原因——不仅是物理硬件，而是CUDA。CUDA是Nvidia专有的软件平台，可以说是现代技术中最具主导地位的生态系统。他们花了超过15年构建这些库、优化原语、完善开发者用于为GPU编译代码的工具，整整一代AI研究人员的职业生涯都是专门用CUDA编写的。它深深嵌入在人工智能的学术和商业基础中。

#### 5.2 CAN的追赶困境

要挑战Nvidia，你不仅要制造可行的芯片，还必须说服全球开发者劳动力放弃一个15年的高度优化语言，从头开始学习你的语言。这正是华为最大的瓶颈。他们的替代软件生态系统CAN比CUDA晚了整整十年才开始开发。这种十年的落后在现实中转化为巨大的摩擦。开发者在中国内部经常抱怨CAN，因为它缺乏CUDA提供的深度预构建库。当开发者遇到内存泄漏或性能瓶颈时，CUDA拥有庞大的社区和精密的调试工具，可以几乎瞬间解决。但用CAN呢？开发者经常需要从零编写低级内核，花费数周调试在Nvidia平台上只需几小时就能解决的问题。

#### 5.3 成本方程的复杂性

DeepSeek报告提到推理成本降低，但企业客户采用华为硬件时，物理芯片上节省的成本可能轻易被工程团队在CAN上优化代码所增加的人力成本所抵消。华为正在积极更新软件，不断推出新版本，但开发者报告CAN与CUDA在可用性和效率方面的差距仍是采用的重大障碍。

### 六、市场预测：Morgan Stanley分析

#### 6.1 市场规模预测

尽管存在硬件落后两代和CAN软件平台高度碎片化的困境，华为的发展轨迹的财务预测令人震惊。Morgan Stanley的分析着眼于长期宏观趋势，而非眼前的技术瓶颈。分析师估计中国国内AI芯片市场今年约210亿美元，但到2030年将扩大至670亿美元。

#### 6.2 市场控制权预测

预测的关键数据点不仅是市场规模，而是谁将控制它。Morgan Stanley预测到2030年，670亿美元市场中的86%将由华为等中国国内厂商供应。这基本上代表了完全的市场捕获，实际上将世界第二大经济体与外国芯片隔绝。

#### 6.3 结构性监管观点

投资银行如何看到被较老硬件和高度碎片化软件平台严重阻碍的生态系统，却自信地预测完全主导？分析师明确指出两个结构性力量在塑造这一现实。首先是之前讨论的推理需求指数增长。其次更重要的是持续的出口管制。Morgan Stanley认为这些管制使本地化成为市场的长期特征，而非仅仅是暂时的政策响应。当一个数十亿美元的市场被永久性地与全球供应链隔离时，国内公司就拥有了保证的、高利润的 captive audience。这种保证的收入——如华为今年获得的120亿美元——为最终解决CAN软件摩擦和推进光刻工艺所需的迭代研究提供资金。

### 七、Nvidia CEO的担忧

#### 7.1 黄仁勋的明确表态

这种强制进化正是Nvidia领导层高度关注的内容。消息来源包含了Nvidia CEO Jensen Huang（原文为Jensen Phuong，可能是口误）在最近与播客Duarkash Patel的采访中的一段非常引人注目的引述。他们专门讨论了一个顶级实验室（如DeepSeek）优先在华为架构上原生运行其下一个大型前沿模型优化，而非作为次要移植的可能性。黄仁勋毫不含糊地表态：这是对我们国家的可怕结果。

#### 7.2 提升至国家层面

注意他的措辞。他没有将其框定为对Nvidia季度收益的威胁，没有说这是企业市场份额的问题，而是提升到了国家安全和技术主权问题。因为他理解Morgan Stanley结构性力量的终点：如果世界第二大经济体被迫从硅层到软件原语再到前沿模型构建一个完全独立平行的技术栈，那就打破了统一的全球生态系统。黄仁勋警告这一轨迹直接导致一个世界各处AI模型在非美国硬件上开发和运行最佳的局面。

### 八、全球AI经济的分叉

#### 8.1 物理层的分裂

视频的核心结论是：全球AI经济的物理层正在分裂。驱动自动驾驶代理、科学研究、全球物流的硅和代码正在分裂成两个完全不同的平行生态系统。它们越来越多地被出口管制所塑造，而非纯粹的技术价值。

#### 8.2 令人不安的思考

黄仁勋担心未来最好的模型在非美国硬件上原生运行。但让我们进一步思考你实际依赖的日常推理。如果AI模型的底层逻辑、内存管理和网络架构根据部署地点开始从根本上针对完全不同的硬件和软件生态系统优化，这些系统的实际智能会开始分化吗？我们是否正在走向一个AI助手推理、效率和能力仅仅因为它被迫运行的硅而根本不同的分裂现实？

这是一个复杂的结构性转变，其影响将触及未来技术发展的每一个层面。

## 完整字幕原文
```
Right now, tech giants in China are placing these massive, I mean, multi-billion dollar orders
for AI chips that are technically speaking at least two generations obsolete.
Right. Completely outdated by industry standards.
Exactly. They're buying hardware that, on paper, should be entirely uncompetitive.
Yet, the company making these older chips Huawei is seeing its AI processor revenues
absolutely skyrocket. Oh, the projections are wild. Yeah, we're talking a jump from 7.5 billion
dollars in 2025 to 12 billion dollars this year.
That is a 60% jump.
Which is just staggering.
Right.
I mean, welcome to today's deep dive.
We're so glad you could join us because in an industry where just, you know, securing
wafer allocation and getting silicon out the door is a total logistical nightmare.
Absolutely.
Capturing an actor four and a half billion dollars in a single year with older technology
is just, well, it's a glaring contradiction.
Yeah.
And what's fascinating here is that this completely upends the traditional Silicon
Valley narrative.
Well, we are wired to assume that the fastest, most power efficient processor, automatic
wins the market, right? Like best specs win. Sure. That's tech 101. Exactly. But the sources we are
looking at today reveal a completely different reality. This massive revenue surge. It's not
about making a faster chip. It's a masterclass in how a company leverages structural market forces
and navigates this unprecedented web of global regulations. They're essentially
rearchitecting their whole approach to AI just to play the hand they redoubt.
Precisely. They're playing the board, not just the cards.
Okay, let's unpack this hand they were dealt, because getting to $12 billion, that's not
just theoretical futures, right?
This is happening right now.
Yeah.
The reports indicate that Chinese tech groups are actively taking delivery of this specific
processor called the 950PR.
Right, the PR model.
And it just entered mass production in March, so it is fresh off the line and demand is
already way outstripping supply.
Plus they have an upgraded version, the 950DT, slated for the fourth quarter.
Yeah, the roadmap is aggressive.
But designing a chip architecture, that's really only half the battle.
Oh for sure.
Actually, manufacturing 7 nanometer or even older node silicon at this kind of blistering
scale, it requires massive physical infrastructure.
So for Huawei to scale up production by 60% in a heavily sanctioned environment, they
need serious manufacturing muscle inside China.
So how are they physically pulling this off?
They are leaning almost entirely on SMEC.
That's the Semiconductor Manufacturing International Corporation.
Okay, SMIC