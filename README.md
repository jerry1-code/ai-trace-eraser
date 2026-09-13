# AI Trace Eraser

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](CHANGELOG.md)
[![Skill](https://img.shields.io/badge/skill-academic--writing-green.svg)](SKILL.md)

**Detect AI-generated writing-risk patterns in English and Chinese academic text, score paragraphs by risk level, and revise high-risk passages through minimal, evidence-preserving edits.**

A conservative, detector-informed academic writing skill that reduces AI-writing risk patterns while preserving every citation, data point, hypothesis, statistical result, and document structure element. Works with any agent that supports skills (Claude Code, Codex CLI, Cursor, etc.).

---

## Why This Exists

AI-assisted academic drafts come out generic and verbose — "In recent years..." openers, inflated phrasing, over-long sentences, and repeated templates. They drift from the author's own voice and lose the precision scholarship depends on.

Generic "humanizers" built for blogs and marketing flatten academic precision. Run one on a thesis and the careful wording is the first thing to go. This skill is designed specifically for academic text — theses, papers, and reports.

## What It Does

- **Detects** 15 AI-writing risk dimensions (D1–D15) in English text, plus a dedicated Chinese AI-pattern module for Chinese text
- **Scores** paragraph-level and document-level risk using structural floors and external-detector calibration
- **Rewrites** high-risk paragraphs through minimal edits — never whole-paragraph regeneration, never content deletion, never word-count reduction
- **Preserves** all protected elements: citations, variables, hypotheses, statistics, quotes, hedges, headings, and reference entries
- **Iterates** through a closed-loop external re-test workflow: rewrite one chapter → user re-tests with detector → iterate until below target

## Three Iron Rules

1. **No whole-paragraph regeneration** — every rewritten sentence must trace to a specific original sentence
2. **No fabrication** — no invented quotes, data, citations, or researcher feelings
3. **No word-count reduction** — every rewritten paragraph must be at least as long as the original

## Key Features

- **Bilingual**: English (D1–D15 framework) and Chinese (dedicated AI-pattern module) with mixed-document routing
- **Closed-loop workflow**: rewrite → re-test → iterate, chapter by chapter
- **6-rung escalation ladder**: sentence-level → rhythm → paragraph architecture → template breaking → researcher-trace → functional reorganisation
- **10 quality gates** (A–J): AI-pattern reduction, academic integrity, meaning preservation, punctuation, aggregation, word-count, structure, grammar, logic flow
- **Author style baseline**: matches the author's own low-risk writing, not generic "good English"
- **External-detector-calibrated**: uses Turnitin AI, CNKI AIGC, GPTZero reports as risk-location evidence without optimising for any single detector

## Installation

### Claude Code / Codex CLI / Cursor

```bash
# Clone the repository
git clone https://github.com/jerry1-code/ai-trace-eraser.git

# Copy to your agent's skills directory
cp -r ai-trace-eraser ~/.claude/skills/  # Claude Code
# or
cp -r ai-trace-eraser ~/.cursor/skills/  # Cursor
```

The skill loads itself when relevant. You can ask:

```
Please reduce the AI traces in this academic text: [your text]
```

Or invoke with a trigger phrase:

```
降AI / 降低AI率 / AI detection / reduce AI score / 去AI痕迹
```

### Manual Install

Copy `SKILL.md` and the `references/` directory into your agent's skill folder.

## Usage

### Basic

```text
User: "降低这篇论文的AI率"
→ Upload .docx + external detector report
→ Phase 1: Parse paragraphs, identify sections
→ Phase 1.5–1.6: Full-document scan + architecture review
→ Build ledger; target-lock ONE highest-scoring chapter
→ Phase 2: Score 15 dimensions, apply floors
→ Phase 4/4.5: Minimal-edit strategy + technique plan
→ Phase 5/5.5: Three-pass rewrite with evidence
→ Phase 7: Quality gates A–J
→ Phase 8/9: Summary stats + output
→ STOP: ask user to re-test before next round
```

### Quick Mode (single paragraph)

```
Quick check this paragraph:
[paste your paragraph]
```

### With external detector report

```
Turnitin AI says 48%. Here's the report.
[paste or upload report]

Here's my thesis:
[upload .docx]
```

## Package Contents

| File | Role |
|---|---|
| `SKILL.md` | Canonical authority — operating architecture, principles, phases, gates, workflow |
| `references/detection_dimensions.md` | D1–D15 dimension catalog with scoring criteria and examples |
| `references/rewrite_techniques.md` | T1–T16 technique catalog with before/after examples |
| `references/chinese_ai_patterns.md` | Chinese-language AI-risk phrase reference and evidence template |
| `references/academic_protection.md` | Protected elements catalog and integrity rules |
| `MANIFEST.md` | Package metadata |
| `CHANGELOG.md` | Version history |
| `TEST_CASES.md` | Behavioral acceptance cases |
| `KNOWN_LIMITATIONS.md` | Honest limitations |
| `examples/before_after.md` | Before/after rewrite examples |

## Ethics and Disclosure

This is an editing aid for clarity and voice, calibrated to an author's own prior accepted work. It does not generate findings, invent data, or change citations. It is not designed to evade AI-use detection. Using it does not remove your obligation to disclose AI assistance — always follow the disclosure policy of the venue you submit to.

## License

MIT — see [LICENSE](LICENSE).
