# Chinese AI Text Risk Patterns

Chinese-language AI-risk phrase reference and evidence template for Chinese-route academic text. Use these fields instead of the English D1–D15 dimension table when the revised text itself is in Chinese.

---

## Chinese AI-Risk Groups

### 1. 模板化开头 (Template Openings)

High-risk phrases commonly used by AI at paragraph beginnings:

- "随着……的快速发展" (with the rapid development of...)
- "近年来，……引起了广泛关注" (in recent years, ... has attracted increasing attention)
- "在当今社会，……" (in today's society, ...)
- "……作为一个重要的……" (... as an important ...)
- "众所周知" (as is well known)
- "……已经成为一个热门话题" (... has become a hot topic)
- "在……的背景下" (in the context of ...)
- "基于以上分析" (based on the above analysis)

### 2. 模板化收束 (Template Closings)

- "综上所述" (to summarize / in summary)
- "总而言之" (in a word / all in all)
- "本研究具有重要的理论意义和实践意义" (this study has important theoretical and practical significance)
- "以上分析表明" (the above analysis shows that)
- "因此，本文提出以下假设" (therefore, this paper proposes the following hypothesis)

### 3. 无依据夸张词 (Unsupported Intensifiers)

- "极大地" (greatly)
- "显著地" (significantly — when not tied to a statistical result)
- "充分体现了" (fully reflects)
- "深刻地影响了" (profoundly influenced)
- "扮演着至关重要的角色" (plays a crucial role)

### 4. 重复短语块 (Repeated Phrase Blocks)

- "不仅……而且……" used in consecutive paragraphs
- "一方面……另一方面……" used mechanically
- "首先……其次……最后……" used as a template across paragraphs
- "基于……通过……实现" repeated chain

### 5. 系动词回避 (Copula Avoidance)

AI often inflates a plain "是" into:
- "作为……的代表" (serves as a representative of)
- "扮演着……的角色" (plays the role of)
- "体现了……的特征" (embodies the characteristics of)
- "标志着……的开始" (marks the beginning of)

Where the sentence simply asserts identity, restore the plain "是".

### 6. 因果链堆叠 (Causal-Chain Stacking)

Single sentence carrying two or more stacked connectives:
- "……从而促进……进而推动……由此实现……"
- "……因此……进而……"
- "……通过……实现……最终达到……"

Split the chain into separate sentences or delete links that add no real information.

### 7. 高频AI词汇 (High-Frequency AI Vocabulary)

Words AI overuses in Chinese academic text:
- 赋能 (empower)
- 助力 (boost/assist)
- 深入探索 (in-depth exploration)
- 全方位 (comprehensive/all-around)
- 多维度 (multi-dimensional)
- 协同 (synergy/collaboration)
- 闭环 (closed loop)
- 抓手 (lever/grip)
- 底座 (foundation/base)
- 生态 (ecology/ecosystem)

### 8. 术语/缩写重复模式 (Term/Abbreviation Repetition)

AI often repeats the full term + abbreviation in every mention:
- "人工智能（Artificial Intelligence, AI）" repeated in every paragraph instead of just "AI" after first introduction
- "结构方程模型（Structural Equation Modeling, SEM）" repeated

After the first introduction, use the abbreviation only.

---

## Chinese-Route Evidence Template

For each Chinese-route paragraph, report:

```text
Paragraph ID:
Language Route: Chinese
Chinese AI-risk groups hit: template opening / template closing / unsupported intensifier / repeated phrase block / copula avoidance / causal-chain stacking / inflated importance / empty comparison / high-frequency AI vocabulary / term-abbreviation repetition
Shared structure risks: paragraph architecture / section-template dependency / reporting-sequence regularity / external-highlight evidence
Protected elements:
Risk estimate: chinese_paragraph_risk_estimate (internal Chinese-text risk estimate only)
Rewrite action: minimal edit / no rewrite / author confirmation needed
```

---

## Chinese Deletion Reinterpretation Rule

In Chinese text, every "删除" or "删去" means "remove low-information content and compensate within the same paragraph," NEVER "reduce word count." Chinese academic text often has minimum character count requirements. Removing a template phrase must be compensated by expanding concrete detail elsewhere in the same paragraph so the net length does not fall.

---

## Rewrite Notes for Chinese Text

- Do NOT mechanically apply English lexical/syntax rules to Chinese text.
- Chinese paragraph risk is assessed structurally — paragraph architecture, section template, reporting sequence, and external highlight evidence.
- Protected Chinese statistical terms: 显著 (significant), 有效 (valid), 提升 (improvement), 明显 (obvious/apparent) — these are protected when they report actual statistical results, but flagged when used as unsupported intensifiers in non-results sections.
- Chinese mixed-language paragraphs: split by language span where possible and score each span under its own route. Protect bilingual technical terms and translated construct names.
