# MANIFEST — ai-trace-eraser

Version: 1.0.0
Type: Agent Skill package (Claude Code, Codex CLI, Cursor, any agent supporting skills)
Purpose: Detect AI-writing-risk patterns in English and Chinese academic text, score paragraphs by risk, and revise high-risk passages by minimal, evidence-preserving edits, under a single-chapter closed-loop external re-test workflow.

## Package contents

| File | Role |
|---|---|
| `SKILL.md` | Canonical authority. Operating architecture, Principles 0–9, Phases 1–9, quality gates A–J, status state machine, language routing, task modes, output structure. |
| `references/detection_dimensions.md` | D1–D15 dimension catalog, scoring criteria, examples, pattern floor rules. |
| `references/rewrite_techniques.md` | T1–T16 technique catalog, before/after examples, strategy matrix, escalation rules. |
| `references/chinese_ai_patterns.md` | Chinese-route AI-risk phrase reference, fixed Chinese-route evidence fields, same-paragraph compensation rules. |
| `references/academic_protection.md` | Protected elements catalog, integrity rules, before/after check procedure. |
| `MANIFEST.md` | This file. |
| `CHANGELOG.md` | Version history. |
| `TEST_CASES.md` | Behavioral acceptance cases. |
| `KNOWN_LIMITATIONS.md` | Honest limitations and out-of-scope items. |
| `examples/before_after.md` | Before/after rewrite examples. |

## Authority order

SKILL.md overrides all reference files for workflow-level output and rules. Reference files provide catalogs, examples, and technique definitions only.

## Three iron rules (override everything except academic integrity)

1. No whole-paragraph regeneration or back-translation.
2. No fabrication (quotes, data, emotions, citations, researcher voice).
3. No word-count reduction.
