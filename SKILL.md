---
name: ai-trace-eraser
title: AI Trace Eraser
description: >
  Detect AI-generated writing-risk patterns in English and Chinese academic text
  (theses, papers, reports), score paragraphs by risk level, and revise high-risk
  passages through minimal, evidence-preserving edits. Supports a closed-loop
  external re-test workflow: rewrite one chapter → user re-tests with external
  detector → iterate until below target. Never regenerates whole paragraphs,
  never fabricates content, never shrinks the paper, and never routes text
  through third-party bypass services. Preserves all citations, data, hypotheses,
  statistical results, and document structure.
version: 1.0.0
author: jerry1-code
category: academic-writing
tags:
  - ai-trace-detection
  - academic-rewriting
  - thesis-editing
  - ai-humanizer
  - chinese-academic
  - english-academic
  - turnitin-ai
  - cnki-aigc
  - minimal-edit
  - closed-loop-retest
language:
  - en
  - zh
input_formats:
  - docx
  - md
  - txt
output_formats:
  - md
  - docx
  - report
triggers:
  - 降AI
  - 降低AI率
  - 降低AIGC检测率
  - AI detection
  - reduce AI score
  - lower AI rate
  - 去AI痕迹
  - AI痕迹检测
  - 知网AIGC
  - CNKI AIGC
  - Turnitin AI
  - thesis AI rewrite
  - academic AI detector
  - external AI detector report
  - AI feature value
  - AI-risk reduction
capabilities:
  - detect_ai_writing_patterns
  - score_paragraph_ai_risk
  - external_detector_informed_prioritisation
  - rewrite_high_risk_paragraphs
  - preserve_academic_meaning
  - preserve_citations_and_data
  - preserve_hypotheses_and_statistics
  - generate_detection_report
  - closed_loop_per_chapter_retest
  - minimal_edit_rewriting
  - word_count_preservation
  - quality_gate_validation
  - chinese_text_ai_risk_detection
  - author_style_baseline_matching
constraints:
  - Do not change citations, references, variables, hypotheses, data, coefficients, significance levels, or statistical conclusions.
  - Do not add unsupported claims, new theories, new references, or new data.
  - Do not make the writing casual, promotional, or overly polished.
  - Do not intentionally add grammar or spelling errors.
  - Preserve the original structure unless repetition clearly needs adjustment.
  - Never regenerate a whole paragraph from scratch.
  - Never shrink the paper — every rewritten paragraph must have word count ≥ original.
  - Never route text through third-party humanizer or bypass APIs.
  - Every rewritten paragraph must be linked to detected risk dimensions and selected techniques.
  - Protected elements must be checked before and after rewriting.
references:
  - references/detection_dimensions.md
  - references/rewrite_techniques.md
  - references/chinese_ai_patterns.md
  - references/academic_protection.md
---

# AI Trace Eraser Skill

## Description

Detect AI-writing risk patterns in English and Chinese academic text. English text uses the D1–D15 detection framework; Chinese text uses the Chinese AI-pattern module plus shared structure-level checks; mixed documents are routed by language segment. Score paragraph-level risk, rewrite high-risk sections by reducing shared detector-sensitive features (repeated templates, uniform rhythm, mechanical reporting sequences, over-smooth reasoning chains), and iterate through a closed-loop external re-test workflow.

This skill is conservative and calibrated for structural AI-risk signals commonly detected by external AI detection systems. It does not guarantee a detector outcome.

---

## Core Operating Architecture (READ FIRST)

### Principle 0 — The goal is a TARGET, not merely "lower than last time"

The operational objective is to reduce traceable AI-writing-risk patterns and prepare candidate revisions for comparable external re-test. The target threshold (default 30%, or a stricter user-specified value) is a closed-loop stopping condition when comparable detector evidence exists. The skill must never guarantee, imply, or optimise for a detector outcome independently of academic integrity, meaning preservation, and evidence-based revision.

**Authorized-Use Boundary**: this skill may be used only on text the user owns, authored, co-authored, or is explicitly authorized to edit. It must NOT be used to misrepresent authorship, hide prohibited AI use, or bypass institutional disclosure rules.

**Definition of done**:
- A chapter is DONE only when its measured external score is **< 30%** (or the user's target).
- The whole task is DONE only when every externally measured target unit is below target.
- Until then, the skill must keep proposing the next rewrite round. It must never present an above-target version as final.

**Never-stop-early rule**:
- Reaching a new lowest score does not end the work; it updates the baseline. If still ≥ 30%, immediately plan the next round on the highest-remaining chapter.
- Legitimate reasons to pause: (a) all measurable units below target; (b) user asks to stop; (c) escalation ladder exhausted and documented; (d) Rewrite Fatigue triggered; (e) no comparable external re-test available; (f) continuing would risk protected content or readability.

### Principle 1 — Closed loop, one chapter per round

This skill does NOT rewrite a whole thesis in one response. Internal scoring cannot reliably predict the external detector result, so the only trusted verdict is a real re-test.

```text
pick the single highest-scoring chapter still at or above target (default 30%)
  → rewrite ONLY that chapter, using minimal edits at the current escalation rung
  → output the rewritten chapter + evidence
  → STOP and ask the user to re-test with CNKI / Turnitin / GPTZero
  → if below target: lock as done, move to next-highest chapter
  → if lower but still above target: keep as new baseline, mark PROGRESS, plan next round
  → if same or higher: roll back to lowest-ever version, move up one escalation rung
  → repeat until below target or escalation ladder exhausted
```

### Principle 2 — Minimal edit only, never regenerate

The biggest cause of score regression is letting the model re-generate a paragraph as fluent new prose. Rules:
- Rewrite by editing EXISTING sentences: substitute words, reorder clauses, split long sentences, recast voice/structure.
- Every sentence in the output must be traceable to a specific original sentence.
- Preserve as much original human wording as possible.
- Whole-paragraph regeneration is FORBIDDEN.
- Back-translation is FORBIDDEN (never translate to another language and back).
- Do NOT delete content or merge sentences to reduce AI features.
- "Aggressive rewrite" means aggressive REORGANISATION of existing sentences, never aggressive REWRITING into new prose.

### Principle 3 — Red lines, target lock, and version ledger

- **Red line**: each chapter's lowest-ever measured external score is a hard ceiling. A rewrite scoring higher is discarded.
- **Target, not ceiling**: the red line prevents regression; success is reaching below the target threshold (default 30%).
- **Target lock**: each round touches only ONE chapter — the highest current measured chapter still at or above target. Everything below target is untouched.
- **Escalation, not surrender**: if a chapter changes <5pp but is still above target, move up one escalation rung.

**Chapter Version Ledger** (required before every round):

```text
| Chapter | Current score | Lowest-ever | Source of lowest | Escalation rung | Tried techniques | Rounds done | Below target? | Rewrite this round? |
|---------|--------------|-------------|-------------------|-----------------|-----------------|-------------|----------------|---------------------|
| ...     | ...          | ...         | ...               | 1–6             | e.g. T1, T14    | int         | Yes/No         | Yes (target) / No   |
```

### Principle 4 — Word-count preservation (never shrink the paper)

- Every rewritten paragraph must have word count ≥ the original paragraph.
- Acceptable range: original length up to ~+15% growth.
- Content deletion is FORBIDDEN. Removing a low-information connective ("Furthermore,", "综上所述") IS allowed when the logical relation stays clear AND the words are compensated within the same paragraph.
- AI features must be reduced by CHANGING how ideas are expressed, never by REMOVING ideas.
- Splitting a long sentence into two is encouraged (varies rhythm and adds words). Merging is not allowed as a routine technique.
- Report before/after word count for every rewritten paragraph.

### Principle 5 — Escalation ladder

When a chapter is still above target, escalate through these rungs in order. Each is progressively more structural but still obeys minimal-edit and word-count preservation:

```text
Rung 1 — Sentence-level: vary openings, transitions, sentence length, lexical choices (T1–T10)
Rung 2 — Rhythm & cadence: break uniform sentence-length patterns; vary clause order (T3, T11)
Rung 3 — Paragraph architecture: change entry point and internal order; differentiate neighbouring paragraphs (T12, T13)
Rung 4 — Reporting-sequence & template breaking: reorder reporting steps; de-template methodology/result patterns (T14, T15)
Rung 5 — Source-extracted researcher-trace integration: relocate existing researcher-view material already in the thesis (T16, sparingly)
Rung 6 — Functional reorganisation: change what each paragraph DOES by reordering sentences WITHIN it (never reorder paragraphs or change argument flow)
```

**Rewrite Fatigue Detection** (mandatory stop):
- 3+ complete rounds on one chapter → PAUSED (hard stop checkpoint; user may authorize ONE additional round)
- <3pp change across two consecutive rounds → PAUSED
- Any regression → roll back to lowest-ever version

### Principle 6 — Preserve structure and readability

**(a) Displaced or absorbed headings**: Section headings, figure/table captions, and list markers are HARD STRUCTURAL BOUNDARIES. Never merge text across a heading. Every heading keeps its own line.

**(b) Merged mega-paragraphs**: Do NOT combine paragraphs. A rewritten paragraph should stay ~160 words / ~9 sentences (soft); hard cap 200 words / 12 sentences. If an original paragraph exceeds the cap, split at a natural break.

### Principle 7 — Reorganisation means within-paragraph only

"Reorganise", "reorder", "change entry point" mean changing the order of sentences INSIDE a single paragraph. They do NOT mean:
- shuffling paragraph sequence within a section;
- changing the argument structure;
- moving content between sections.

### Principle 8 — Safe sentence splitting (no fragments)

A sentence may be split ONLY when both resulting parts independently pass: own subject + own finite verb + complete thought.

NEVER produce:
- Subordinate-clause fragments ("When employees interact with AI in daily work.")
- List/enumeration tails ("...self-efficacy. Work engagement, and creative inspiration.")
- Subject-less verb phrases ("...raises the problem. Builds the theoretical model.")
- Gerund continuations ("...statistical analysis. Including multivariate analysis...")
- Choppy runs of 3+ ultra-short sentences

Upper bound: no sentence over ~30 words or more than two subordinate clauses.

### Principle 9 — Grammatical correctness and no meta-commentary

**(a) Grammar**: subject–verb agreement, tense, articles, prepositions, pluralisation must remain correct. AI features must NEVER be reduced by inserting grammar errors.

**(b) No meta-commentary**: do not insert sentences that explain or justify the writing ("This detail was included to improve measurement precision."). Every sentence must follow logically from surrounding text.

---

## Task Routing Rule

Before any diagnosis or rewriting, classify the request:

1. **Skill-Audit Mode** — user asks to inspect THIS skill for errors/contradictions. Do NOT score thesis text; audit for consistency, routing, safety.
2. **AI-Writing-Risk Mode** — user asks to reduce AI-writing risk / AI rate / AIGC traces. Main thesis workflow.
3. **Similarity/Plagiarism Mode (out of scope)** — if user asks for 查重/similarity/plagiarism reduction with no AI context, ask whether they actually want AI-writing-risk reduction.
4. **Assembly Mode** — only after chapter-by-chapter accepted versions exist. Combine locked chapters into a report/DOCX.

## Language Routing Rule

- **English text**: use D1–D15 dimensions, English cliché banks, and rewrite techniques.
- **Chinese text**: use the Chinese AI-pattern module (`references/chinese_ai_patterns.md`) plus structure-level checks; do NOT apply English-specific lexical rules.
- **Mixed Chinese–English**: process by language segment; protect bilingual term consistency.
- **Method routing**: apply qualitative techniques only to qualitative/mixed passages.

## Task Mode Definitions

| Task type | Trigger | Mode | Evidence depth |
|---|---|---|---|
| Audit this skill | User asks to inspect skill files | Skill-Audit | Issue-level audit format |
| Inspect without rewriting | inspect/review/audit thesis text | Diagnosis-Only | Route-appropriate scoring, no rewrite |
| One quick paragraph | Explicit quick request or single paragraph | Quick | Minimum evidence set |
| ≤10 selected paragraphs | Small batch | Single-Batch | Full evidence for those paragraphs |
| Ordinary chapter revision | Default | Working | Full evidence for target paragraphs; compact skip for low-risk |
| Long doc / DOCX / external report | >10 paragraphs or external report | Full Staged | Staged full evidence |
| Combine accepted chapters | All chapters below target | Assembly | Assembly checks + DOCX gate |

## Score Terminology

- `external_detector_score`: score from CNKI, Turnitin, GPTZero, etc.
- `chapter_red_line`: lowest current measured external score for a chapter
- `raw_paragraph_risk`: internal D1–D15 weighted score before floors
- `paragraph_risk_index`: internal paragraph risk score after floors
- `scope_risk_index`: internal risk estimate for the diagnosed scope (overall only for full-document scope)
- `internal risk estimate`: any score generated without an external re-test

Internal scores help locate risk. They must NOT be presented as proof that an external detector score has decreased.

---

## Workflow

### Phase 1: Upload & Parse

1. Accept uploaded document (.docx, .md, .txt).
2. Extract full text preserving section structure.
3. Split into paragraphs.
4. Exclude bibliography, appendices, questionnaires, declarations, table of contents, and pure table captions from main scoring unless asked.
5. Record section type: abstract / introduction / literature review / hypothesis development / methodology / empirical results / discussion / conclusion.

### Phase 1.5: Full-Document Pattern Scan

Identify:
- repeated sentence openings across chapters
- repeated paragraph endings
- repeated literature review patterns
- repeated hypothesis-development structures
- repeated discussion and conclusion templates
- over-polished AI-like paragraph chains
- high-risk sections requiring section-level rewriting

### Phase 1.6: Section-Level Architecture Review

For each section, identify the functional role of every paragraph:

```text
Section:
Paragraph ID:
Paragraph Function: Definition / Background / Citation / Gap / Theory / Variable Mechanism / Hypothesis / Method / Scale / Sample / Test / Result / Interpretation / Conclusion / Implication / Limitation
Repeated Function Cluster:
Neighboring Paragraphs with Same Function:
Section-Level Risk:
```

High-risk signs: several neighboring paragraphs perform the same function; all theory paragraphs follow proposer→year→concept→application; all hypothesis paragraphs follow variable→mechanism→citation→hypothesis.

### Phase 2: Detection and Paragraph Scoring

#### Phase 2a: Route-Specific Scoring

For English-route paragraphs, score against the 15 AI-trace dimensions (see `references/detection_dimensions.md`):

| # | Dimension | Max Score |
|---|-----------|-----------|
| D1 | Repetitive Sentence Starters | 3.0 |
| D2 | Formulaic Transitions | 3.0 |
| D3 | Over-Smooth Logical Flow | 3.0 |
| D4 | Uniform Sentence Length & Rhythm | 2.5 |
| D5 | Generic Academic Phrasing | 3.0 |
| D6 | Overused Hedging | 2.0 |
| D7 | Conclusion-Style Generalizations | 2.5 |
| D8 | Passive Voice & Nominalization | 2.0 |
| D9 | Abstract-to-Concrete Imbalance | 2.5 |
| D10 | Citation Pattern Regularity | 2.0 |
| D11 | Lexical Flatness | 2.5 |
| D12 | Paragraph-Level Template Structure | 4.0 |
| D13 | Cross-Paragraph Structural Repetition | 4.0 |
| D14 | AI-Like Academic Smoothness | 3.0 |
| D15 | Thesis-Section Template Dependency | 3.0 |

Total possible score: 42.0.
`raw_paragraph_risk = min(dimension_score / 42.0, 1.0) × 100%`

For Chinese-route paragraphs, use the Chinese AI-pattern evidence fields (see Language Routing).

#### Phase 2b: Floor Application

```text
paragraph_risk_index = max(
  raw_paragraph_risk,
  pattern_floor,
  repeated_structure_floor,
  section_template_floor,
  trigger_floor
)
```

Pattern floor rules:
- 2+ strong dimensions: minimum 18%
- 3+ strong dimensions: minimum 28%
- 4+ strong dimensions: minimum 38%
- D12 ≥2.4: minimum 35%
- D12 ≥2.4 AND D3 ≥1.5: minimum 42%
- D12 ≥3.2 AND D5 ≥2.0: minimum 50%

Cross-paragraph floor:
- 3–5 paragraphs share opening structure: minimum 25%
- 6–10 paragraphs: minimum 35%
- >10 paragraphs: minimum 45%
- Whole section repeats same pattern: minimum 50%

Section template floor:
- Literature review (definition→citation→implication): minimum 35%
- Hypothesis (variable→mechanism→hypothesis): minimum 40%
- Discussion (result→explanation→implication): minimum 42%
- Conclusion (broad implications without findings link): minimum 45%
- Empirical results (coefficient→significance→support): minimum 35%

### Phase 3: Risk Prioritisation and Target Selection

- Build or update the Chapter Version Ledger.
- Select exactly ONE target unit: highest current measured chapter still at or above target.
- Mark every non-target chapter "not rewritten this round."

### Phase 4: Rewrite Strategy

| Priority | Risk Level | Strategy | Action |
|---|---|---|---|
| P0 / A | Critical or external high-risk | Structural Reorganisation (minimal edit) | Reorganise existing sentences — reorder, re-segment, change entry point. NEVER regenerate. |
| P1 / B | High | Standard Reorganisation | Edit repeated openings, endings, transitions, templates. |
| P2 / C | Medium | Light edit | Edit only if paragraph contributes to repeated structure. |
| P3 / D | Low | Check Only | Preserve unless part of high-risk cluster. |

### Phase 4.5: Dimension-to-Technique Execution Plan

For each rewritten paragraph, record:

```text
Paragraph ID:
Hit Dimensions:
Selected Techniques:
Protected Elements:
Rewrite intensity:
```

Dimension-to-technique mapping (see `references/rewrite_techniques.md` for full definitions):

| Hit Dimension | Required Technique |
|---|---|
| D1 | T1 Starter Variation |
| D2 | T2 Transition De-formulaizing |
| D3 | T10 Reasoning Visibility or T12 Architecture Rebuilding |
| D4 | T3 Sentence Length Variation |
| D5 | T6 Generalization Surgery or T11 Abstract Word Reduction |
| D6 | T4 Hedging Calibration |
| D7 | T6 Generalization Surgery |
| D8 | T7 Passive Voice Control |
| D9 | T8 Concrete Anchoring or T11 Abstract Word Reduction |
| D10 | T9 Citation Naturalization |
| D11 | T10 Lexical Precision |
| D12 | T12 Architecture Rebuilding or T16 Researcher-Trace Relocation |
| D13 | T13 Section-Level Diversification |
| D14 | T10 Reasoning Visibility or T16 Researcher-Trace |
| D15 | T13 Section Diversification or T16 Researcher-Trace |

### Phase 5: Three-Pass Rewrite Protocol

#### Pass 1: Template and Phrase Repair
- Rewrite repeated openings into varied, equally-long openings
- De-template definition/source/item pattern by restructuring, not compressing
- Replace broad academic phrases with thesis-specific wording
- Preserve word count and protected elements

#### Pass 2: Rhythm and Architecture Repair
- Vary sentence length naturally
- Change paragraph entry point
- Reorder repeated reporting sequence
- Split long sentences (encouraged); never merge
- Keep original paragraph breaks and heading positions
- Stay within readability limits (≤200 words / 12 sentences)

#### Pass 3: Anti-AI Audit
- Add research-boundary or decision-trace sentences based ONLY on existing content
- Vary how related findings are presented
- Check that paragraph does not become overly polished

### Phase 5.5: Execution Evidence

For each revised paragraph, record:

```text
Paragraph ID:
Pass 1 — Template/phrase repair actions:
Pass 2 — Rhythm/architecture repair actions:
Pass 3 — Anti-AI audit result:
Word count: original / revised / change%
Decision: Pass / Needs Rework
```

### Phase 6: Scope-Aware Risk Index

```text
scope_risk_index =
  (0.45 × average_paragraph_risk)
  + (0.25 × high_risk_share)
  + (0.15 × medium_risk_share)
  + (0.15 × section_repetition_score)
```

Report as `overall_risk_index` only for full-document scope; otherwise `target_chapter_risk_index` or `batch_risk_index`.

External calibration: if external score exceeds internal estimate by ≥15pp or ≥1.5×, do not report internal score below 70% of external score.

### Phase 7: Quality Gates (mandatory, cannot skip)

For every rewritten paragraph, check:

#### Gate A: AI-Pattern Reduction
- Did rewrite address actual hit dimensions?
- Were structural risks handled structurally?
- Can every output sentence trace to an original sentence? (regeneration = FAIL)
- Any placeholder/template residue left? (FAIL)

#### Gate B: Academic Integrity
Compare original and revised for protected elements:
- headings (exact text, numbering, position on own line)
- paragraph breaks (no merging)
- citations, author names, variable names, abbreviations, capitalization
- hypothesis numbers and wording
- coefficients, p-values, significance levels, model names, table numbers
- statistical symbol formatting (keep "p < 0.05", "β = 0.32" exactly)
- reference list entries (LOCKED — never rewritten)
- thesis title, author, supervisor, institution (LOCKED)
- appendices, questionnaires, consent forms (LOCKED)
- verbatim quotations (never split/shortened/re-punctuated)
- epistemic hedges ("may", "suggests", "is consistent with" — never upgraded to "proves", "demonstrates")

#### Gate C: Meaning Preservation
- Original claim preserved
- No new theory/reference/data/example added
- Claim STRENGTH preserved (no hedge → assertion upgrade)

#### Gate D: Punctuation Check
- No new em dashes (—) introduced in body prose
- No double hyphens (--) anywhere
- Hyphenated compounds intact (employee-AI, self-efficacy)
- En dashes in ranges preserved (2007–2010)

#### Gate E: Aggregation Check
- Fragment count not reduced (no merging)
- No revised fragment exceeds 3000 characters without valid breakpoint

#### Gate F: Word-Count Preservation
- revised_word_count ≥ original_word_count (PASS)
- Report original/revised/change% for each paragraph and chapter total

#### Gate G: Structure and Readability
- Same number of headings, each on own line
- No heading text duplicated/echoed
- No table/figure caption duplicated
- Same paragraph count (unless over-long paragraph split)
- No paragraph over 200 words / 12 sentences
- Rewrite not more fluent/native/journal-style than author's baseline
- No new connective or sentence template not in author's writing

#### Gate H: Grammatical Completeness
- Every sentence has own subject + finite verb + complete thought
- No fragments (universal test on EVERY period)
- No choppy runs (3+ ultra-short sentences)
- No over-long sentences (>30 words or >2 subordinate clauses)

#### Gate I: Grammar
- Subject–verb agreement correct
- Every sentence starts with capital letter
- Demonstratives agree (This/These)
- No spelling errors, typos, double spaces
- No literary arrows (→) in body prose

#### Gate J: Logic Flow and No Meta-Commentary
- Every sentence follows logically from previous and into next
- No inserted asides justifying the writing
- No mechanical repeated-subject ("This study…/It…/The study…")
- No over-polished AI phrases ("sheds light on", "fills a critical gap", "delve into", "plays a pivotal role")
- No business-talk phrases ("the practical upshot is", "what this tells us is")
- No low-information "correct filler" passages
- No empty comparison claims ("outperforms existing methods" without specifics)
- No copula avoidance ("serves as" → "is")
- No elegant variation (same entity renamed across sentences)

### Phase 8: Summary Stats

```text
Scope: Full document / Target chapter / Selected batch
average_paragraph_risk:
high_risk_share:
medium_risk_share:
section_repetition_score:
scope_risk_index:
original_chapter_word_count:
revised_chapter_word_count:
chapter_word_count_change_percent:
word_count_preserved: Yes / No
judgment:
```

| scope_risk_index | Judgment |
|---|---|
| ≤8% | Low; manually check repeated structures |
| 9–15% | Mild; revise repeated openings/endings |
| 16–25% | Moderate; revision recommended |
| 26–29% | Approaching target; one more light round |
| 30–35% | At/above target; keep rewriting and escalate |
| 36–50% | Very high; strong rewrite required |
| >50% | Severe; major rewrite required |

### Phase 9: Output

1. **Detection Report** — paragraph #, section, D1–D15 scores, total, paragraph_risk_index, hit dimensions, strategy.
2. **Dimension-to-Technique Execution Plan** — which dimensions targeted, which techniques used.
3. **Three-Pass Rewrite Evidence** — Pass 1, 2, 3 actions for each rewritten paragraph.
4. **Protected Elements Check Report** — extracted before, confirmed after.
5. **Phase 7 Quality Gate Report** — Gate A through J results.
6. **Rewritten Target Unit** — rewritten chapter/batch with revised paragraphs clearly marked.
7. **Revision Summary** — major patterns reduced, paragraphs needing manual review.
8. **Score Regression / Baseline Check** — if external score available, compare; otherwise "pending re-test".

## Staged Execution (for long documents)

| Stage | Content | Output |
|---|---|---|
| Stage 1 | Diagnosis only — Phases 1–4.5 | Diagnosis report + ledger + target-lock |
| Stage 2 | Rewrite — Phases 5–5.5 | Three-pass evidence + revised paragraphs |
| Stage 3 | Quality gate — Phase 7 | Gate A–J results per paragraph |
| Stage 4 | Final output — Phases 6, 8, 9 | Scope-aware scoring + summary + final text |
| Stage 5 | Re-test stop | STOP; user re-tests; then continue or roll back |

## Default-Excluded Units

Unless explicitly asked, these are NOT rewritten, NOT scored, and should be excluded from re-test scope:
- references / bibliography
- appendices
- questionnaires and survey instruments
- ethics statements / consent forms
- title page, table of contents
- figure and table captions (unless externally flagged)
- verbatim participant quotes (unless qualitative quote-balance diagnosis)
- equations, formula numbers, table cell values

## External Detector Handling

- External scores are comparable only from the SAME detector, SAME document version, SAME scope.
- Scores from different detectors are separate streams — never compare directly.
- If no comparable external re-test: mark all scores "internal risk estimate only," do NOT claim detector improvement, recommend external re-testing.
- External highlight first: externally highlighted sections take priority over internal low scores.
- Convert detector-specific findings into shared AI-risk categories before rewriting.

## Author Style Baseline Rule

The target is NOT "better, more native English." Over-polishing makes text MORE AI-like. Build a baseline from the document's own LOW-RISK paragraphs:
- typical sentence length and variation
- preferred connectives and transitions
- recurring verbs and phrasings
- mild non-native features (article use, preposition choices) — protective human signals, NOT errors to fix
- citation placement habits

Rewrite high-risk paragraphs TOWARD this baseline, not toward generic polished English.

## Reference Files

- `references/detection_dimensions.md` — Full D1–D15 dimension definitions with scoring criteria and examples.
- `references/rewrite_techniques.md` — T1–T16 technique catalog with before/after examples.
- `references/chinese_ai_patterns.md` — Chinese-language AI-risk phrase reference and evidence template.
- `references/academic_protection.md` — Protected elements catalog and integrity rules.

## Usage Example

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
