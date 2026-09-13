# AI Trace Eraser

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](CHANGELOG.md)
[![Skill](https://img.shields.io/badge/skill-academic--writing-green.svg)](SKILL.md)

**[English](#english) | [中文](#中文)**

---

<a id="english"></a>

## English

### Overview

Detect AI-generated writing-risk patterns in English and Chinese academic text, score paragraphs by risk level, and revise high-risk passages through minimal, evidence-preserving edits. A conservative, detector-informed academic writing skill that reduces AI-writing risk patterns while preserving every citation, data point, hypothesis, statistical result, and document structure element.

### Why This Exists

AI-assisted academic drafts come out generic and verbose — "In recent years..." openers, inflated phrasing, over-long sentences, and repeated templates. They drift from the author's own voice and lose the precision scholarship depends on. Generic "humanizers" built for blogs and marketing flatten academic precision. This skill is designed specifically for academic text — theses, papers, and reports.

### Three Iron Rules

1. **No whole-paragraph regeneration** — every rewritten sentence must trace to a specific original sentence
2. **No fabrication** — no invented quotes, data, citations, or researcher feelings
3. **No word-count reduction** — every rewritten paragraph must be at least as long as the original

### Key Features

- **Bilingual**: English (D1–D15 framework) and Chinese (dedicated AI-pattern module) with mixed-document routing
- **Closed-loop workflow**: rewrite → re-test → iterate, chapter by chapter
- **6-rung escalation ladder**: sentence-level → rhythm → paragraph architecture → template breaking → researcher-trace → functional reorganisation
- **10 quality gates** (A–J): AI-pattern reduction, academic integrity, meaning preservation, punctuation, aggregation, word-count, structure, grammar, logic flow
- **Author style baseline**: matches the author's own low-risk writing, not generic "good English"
- **External-detector-calibrated**: uses Turnitin AI, CNKI AIGC, GPTZero reports as risk-location evidence

### Web Interface

A built-in web app is available in the `web/` directory. It provides a browser-based interface for pasting academic text and getting AI-trace detection and rewriting results.

```bash
cd web
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
```

### Installation (Agent Skill)

#### Claude Code / Codex CLI / Cursor

```bash
git clone https://github.com/jerry1-code/ai-trace-eraser.git
cp -r ai-trace-eraser ~/.claude/skills/   # Claude Code
# or
cp -r ai-trace-eraser ~/.cursor/skills/   # Cursor
```

The skill loads itself when relevant. Use trigger phrases like `降AI`, `reduce AI score`, `去AI痕迹`.

#### Manual / Web LLM (claude.ai, ChatGPT)

1. Download `SKILL.md` from this repo.
2. Upload it to your AI chat along with your text.
3. Ask: "Apply this skill to the following text: [your text]"

### Usage

#### Web App

Open the web interface, paste your text, optionally provide an external detector score, and click "Analyze". The app will detect AI patterns, score risk, and produce a rewritten version with evidence.

#### Agent Skill

```text
User: "降低这篇论文的AI率"
→ Upload .docx + external detector report
→ Phase 1: Parse paragraphs, identify sections
→ Phase 1.5–1.6: Full-document scan + architecture review
→ Phase 2: Score 15 dimensions, apply floors
→ Phase 4/4.5: Minimal-edit strategy + technique plan
→ Phase 5/5.5: Three-pass rewrite with evidence
→ Phase 7: Quality gates A–J
→ Phase 8/9: Summary stats + output
→ STOP: ask user to re-test before next round
```

### Package Contents

| File | Role |
|---|---|
| `SKILL.md` | Canonical authority — operating architecture, principles, phases, gates |
| `web/` | Web application for browser-based usage |
| `references/detection_dimensions.md` | D1–D15 dimension catalog |
| `references/rewrite_techniques.md` | T1–T16 technique catalog |
| `references/chinese_ai_patterns.md` | Chinese-language AI-risk phrase reference |
| `references/academic_protection.md` | Protected elements catalog |
| `examples/before_after.md` | Before/after rewrite examples |

### Ethics and Disclosure

This is an editing aid for clarity and voice. It does not generate findings, invent data, or change citations. It is not designed to evade AI-use detection. Always follow the disclosure policy of the venue you submit to.

### License

MIT — see [LICENSE](LICENSE).

---

<a id="中文"></a>

## 中文

### 概述

检测英文学术文本中的 AI 写作风险模式（15 个维度 D1–D15），以及中文学术文本中的 AI 痕迹（8 个风险组），按段落评分，通过最小编辑方式改写高风险段落。保留所有引用、数据、假设、统计结果和文档结构。

### 为什么需要这个项目

AI 辅助生成的学术草稿往往冗长空洞——"近年来……引起了广泛关注"式的开头、浮夸的措辞、重复的模板结构。通用的"去AI味"工具是为博客和营销文案设计的，用在论文上会毁掉学术精确性。这个技能专门为学术文本设计——论文、报告、学位论文。

### 三条铁律

1. **禁止整段重写** — 每个改写后的句子必须能追溯到原文中的某个具体句子
2. **禁止编造** — 不编造引语、数据、引用、研究者感受
3. **禁止缩减字数** — 改写后的段落字数必须 ≥ 原文

### 核心功能

- **双语支持**：英文（D1–D15 检测框架）+ 中文（专用 AI 痕迹模块），混合文档自动路由
- **闭环工作流**：改写 → 外部检测器复测 → 迭代，逐章进行
- **6 级升级阶梯**：句子级 → 节奏 → 段落架构 → 模板打破 → 研究者痕迹 → 功能重组
- **10 个质量门**（A–J）：AI 模式缩减、学术完整性、语义保留、标点、聚合、字数、结构、语法、逻辑流畅
- **作者风格基线**：匹配作者本人低风险段落的写作风格，而非通用"好英语"
- **外部检测器校准**：支持 Turnitin AI、知网 AIGC、GPTZero 报告作为风险定位证据

### Web 在线使用

项目内置 Web 应用，位于 `web/` 目录。在浏览器中粘贴学术文本即可获得 AI 痕迹检测和改写结果。

```bash
cd web
pip install -r requirements.txt
python app.py
# 打开 http://localhost:5000
```

### 安装（Agent 技能方式）

#### Claude Code / Codex CLI / Cursor

```bash
git clone https://github.com/jerry1-code/ai-trace-eraser.git
cp -r ai-trace-eraser ~/.claude/skills/   # Claude Code
# 或
cp -r ai-trace-eraser ~/.cursor/skills/   # Cursor
```

技能会在相关场景自动加载。使用触发词如 `降AI`、`降低AI率`、`去AI痕迹`。

#### 手动方式 / 在线 LLM（claude.ai、ChatGPT）

1. 从本仓库下载 `SKILL.md`
2. 上传到 AI 对话中，连同你的文本
3. 说："请按照这个 skill 检测并改写以下文本中的 AI 痕迹：[你的文本]"

### 使用方法

#### Web 应用

打开 Web 界面，粘贴你的文本，可选填外部检测器分数，点击"分析"。应用会检测 AI 模式、评分、并生成带证据的改写版本。

#### Agent 技能

```text
用户: "降低这篇论文的AI率"
→ 上传 .docx + 外部检测器报告
→ 阶段 1: 解析段落，识别章节类型
→ 阶段 1.5–1.6: 全文扫描 + 架构审查
→ 阶段 2: 15 维度评分，应用底线规则
→ 阶段 4/4.5: 最小编辑策略 + 技术方案
→ 阶段 5/5.5: 三遍改写 + 证据
→ 阶段 7: 质量门 A–J 检查
→ 阶段 8/9: 汇总统计 + 输出
→ 停止: 请用户复测后再进入下一轮
```

### 项目结构

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 核心权威文件 — 运行架构、原则、阶段、质量门 |
| `web/` | Web 应用，浏览器直接使用 |
| `references/detection_dimensions.md` | D1–D15 检测维度定义 |
| `references/rewrite_techniques.md` | T1–T16 改写技术目录 |
| `references/chinese_ai_patterns.md` | 中文 AI 痕迹短语参考 |
| `references/academic_protection.md` | 保护元素目录 |
| `examples/before_after.md` | 改写前后对比示例 |

### 伦理与声明

这是一个用于提升清晰度和恢复作者声音的编辑辅助工具。它不会生成研究发现、编造数据或修改引用。它不是为了规避 AI 使用检测而设计的。使用时请始终遵守你所在机构或投稿场所的信息披露政策。

### 开源协议

MIT — 详见 [LICENSE](LICENSE)。
