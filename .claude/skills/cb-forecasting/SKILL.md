---
name: cb-forecasting
description: Analyze high-barrier cyclical tech companies to forecast future profitability. Use when user mentions analyzing semiconductor companies (SK海力士, 三星, 台积电, 英伟达, Intel), tech hardware companies with high capex and strong cyclicality, forecasting earnings for capital-intensive industries, evaluating competitive moat in tech/hardware sectors, or assessing capacity expansion cycles and their lagged profit impact. Also use when user asks about "前置信号", "盈利质量", "产能转化", "估值透支" or references CapEx-to-revenue cycles, order books, supply chain bottlenecks (CoWoS, EUV), yield rates, or PE valuation timing in tech context.
---

# C-B Forecasting Model
## Cycle & Barrier Profitability Forecasting for High-Capex Tech Companies

> **Analysis Time Node (分析时间节点)**: 2026-05-11  
> When beginning any analysis, explicitly state: *"Current analysis date: 2026-05-11. All financial data, quarterly results, and forward-looking statements should be evaluated relative to this date."*  
> The year 2026 is used as the reference point for mid-cycle and long-term forecasts (2027, 2028, 2029+).

A four-dimensional framework for systematically evaluating the future profit trajectory of companies characterized by **high capital expenditure, strong technical barriers, and pronounced cyclicality**.

**Best suited for:** Semiconductor equipment, memory manufacturers, advanced packaging (CoWoS), foundries, GPU/AI chip designers, and any tech sector where capacity lead times exceed 18 months and margins are heavily influenced by yield rates.

---

## The Four Dimensions

### Dimension 1: Leading Indicators (前置信号)
**Core logic:** Don't look at what the company *has earned* — look at what its *major customers and supply chain* are doing.

Three key signals:

1. **Order Pre-pay Surge (预收/合同负债激增)**
   - Check balance sheet for sudden increases in "advance payments" or "contract liabilities"
   - A sharp rise signals that the revenue floor for the next 1-2 quarters is already locked in
   - Pattern: When Apple/Nvidia start prepaying for future supply, the upstream benefits within 2 quarters

2. **CapEx Transmission (资本支出传导)**
   - Watch infrastructure spending of industry giants (cloud providers, car manufacturers, hyperscalers)
   - The money flow: downstream CapEx → upstream revenue with ~2-4 quarter lag
   - Example: Microsoft/Google CapEx surge → TSMC wafer revenue up 2 quarters later

3. **Material Bottleneck Points (物料瓶颈点)**
   - Identify exclusive links in the supply chain (CoWoS packaging, EUV lithography, HBM memory)
   - Wherever the bottleneck sits, the超额利润 (excess profit) concentrates there
   - Example: During CoWoS shortage, only TSMC can deliver advanced packaging → pricing power surges

**Analysis question:** What has *already happened* in the supply chain that will show up in financial statements 2-4 quarters from now?

---

### Dimension 2: Quality of Moat (盈利质量与壁垒评估)
**Core logic:** Distinguish between **"pricing power profit"** and **"scale efficiency profit"**.

| Profit Type | Driver | Stability | Example |
|-------------|--------|------------|---------|
| Premium-driven (溢价驱动) | Scarcity | High volatility, unstable | Current HBM shortage profits |
| Cost-driven (成本驱动) | Efficiency | Stable, deep moat | Mature process nodes |

**Key questions:**
- Is the margin coming from *scarcity* (unstable) or *efficiency* (durable)?
- Has a "second supplier" passed qualification? When a competitor clears validation, ASP and margins begin to compress even if volume grows
- Watch for **bargaining power drift (议价权漂移)** — the moment a second source is qualified, pricing negotiation leverage shifts

**Analysis question:** When the shortage ends, will the margin structure survive, or does it evaporate with the bottleneck?

---

### Dimension 3: Capacity-Profit Lag (产能转化与财务错位)
**Core logic:** Understand that profits are often *hidden in depreciation*.

Two critical dynamics:

1. **CIP Monitoring (在建工程监控)**
   - Track construction-in-progress on the balance sheet
   - When CIP transfers to fixed assets, output surges — but the *initial massive depreciation burden* suppresses near-term profitability
   - Pattern: New fab completion → yield ramp →折旧 burden → profit pressure → eventually profit explosion after depreciation stabilizes

2. **Yield Multiplier (良率乘数)**
   - In high-tech: **Profit margin = Price × Yield**
   - Doubling capacity does NOT double profit — only when yield crosses a threshold (e.g., 80%) does profit explode
   - Example: SK Hynix HBM yield crossing 80% threshold → profit margin per wafer jumps 3x

**Analysis question:** Is this company currently in the "capacity ramp, profit suppressed" phase, or has yield crossed the threshold where volume converts to profit?

---

### Dimension 4: Valuation Discounting (估值透支度校验)
**Core logic:** Determine which *future year* the market is currently pricing in.

**PE Valuation Yardstick:**
- **PE < 10x**: Market believes good times are ending (cyclical peak)
- **PE 10-20x**: Market pricing current cycle fairly
- **PE > 25x**: Market has discounted 2-3 years of capacity expansion profits

**"Bull thesis exhaustion" detection:**
- If a company announces massive future capacity expansion plans but the stock price does NOT make new highs → future profits are already fully discounted in current price
- Contrast: Stock price making new highs while announcing new fabs → room for upside remains

**Analysis question:** Is the current stock price telling you "the best is behind us" (PE<10) or "future profits are already priced in" (PE>25)?

---

## Output Format

When you complete the analysis, structure your output as:

```
# [Company Name] C-B Analysis: [Year] Forecast

> **Current Analysis Date**: 2026-05-11

## Dimension 1: Leading Indicators
**Signal detected:** [None / Order Pre-pay / CapEx Transmission / Bottleneck]
**Time to impact:** [1-2 quarters / 2-4 quarters / 4+ quarters]
**Evidence:** [Supporting financial data points]

## Dimension 2: Quality of Moat
**Margin driver:** [Premium-based / Cost-based / Mixed]
**Bargaining power trajectory:** [Strengthening / Stable / Drifting]
**Second supplier risk:** [Low / Medium / High — and timeline if applicable]

## Dimension 3: Capacity-Profit Lag
**Current phase:** [Capacity ramp / Yield crossing threshold / Mature production]
**CIP status:** [Early-stage construction / Near completion / Recently operational]
**Yield threshold:** [Crossed / Approaching / Not yet reached]

## Dimension 4: Valuation
**Current PE:** [x]
**Market pricing:** [Current cycle only / Next 12-18 months / 2-3 years ahead]
**Bull thesis exhaustion:** [No / Partial / Yes — indicators described]

## Synthesis: Profit Forecast Trajectory
**Next 12 months:** [Up / Down / Flat — with confidence level and reasoning]
**Key catalyst:** [Primary driver of next move]
**Key risk:** [What could break the thesis]
```

---

## Practical Application: Mid-to-Long Term Forecasting Checklist

> **Reference Date**: 2026-05-11 — "Current year" = 2026. Forecasts should evaluate 2026, 2027, 2028, and beyond relative to this date.

To predict a company's trajectory:

1. **看订单**: Have major customers (Nvidia/Apple/Google/ByteDance/Tencent) issued 2026-2027 purchase intentions? (Leading Indicators)
2. **看竞争**: Has a second supplier passed qualification, shifting bargaining power? (Quality of Moat)
3. **看工厂**: Did capacity expansion started in 2024-2025 reach full production by 2026-2027? (Capacity-Profit Lag)
4. **看股价**: Does current PE already embed that new capacity's profits? (Valuation Discounting)

**Year Reference:**
- "Current" = 2026 (as of 2026-05-11)
- "Near-term" = next 4 quarters (H2 2026)
- "Mid-term" = 2027
- "Long-term" = 2028+

---

## How to Use This Skill

1. **User provides a company name/ticker + context** (e.g., "SK Hynix", "TSMC earnings", "semiconductor cycle")
2. **Apply the four dimensions systematically** — don't skip any dimension even if data is incomplete; note assumptions clearly
3. **Synthesize into the standardized output format** — this makes comparisons across companies straightforward
4. **Identify which dimension is the primary driver** — not all dimensions are equally important for every company; focus analysis on the most relevant signals

**Note:** This framework is most effective for analyzing companies where capacity expansion cycles and technical barriers materially impact profit timing. For pure software or轻资产 businesses, other frameworks may be more appropriate.