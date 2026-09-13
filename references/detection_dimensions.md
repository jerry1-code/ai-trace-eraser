# Detection Dimensions (D1–D15)

Full definitions, scoring criteria, and examples for the 15 AI-trace detection dimensions used in English-route academic text. Total possible score: 42.0.

`raw_paragraph_risk = min(dimension_score / 42.0, 1.0) × 100%`

---

## D1: Repetitive Sentence Starters (0–3.0)

**Definition**: Multiple sentences in the same paragraph or across neighbouring paragraphs begin with the same word, phrase, or syntactic pattern.

**Scoring**:
- 0.0: No repetition; varied openings.
- 1.0: Two sentences share the same opening word.
- 2.0: Three or more share the same opening, or two share an identical multi-word phrase.
- 3.0: Four or more sentences share the same opening pattern, or the pattern repeats across paragraphs.

**Examples**:
- Score 3.0: "This study examines... This study uses... This study finds... This study concludes..."
- Score 2.0: "The results show... The coefficient is... The model demonstrates..."

## D2: Formulaic Transitions (0–3.0)

**Definition**: Reliance on a fixed set of academic connectives that AI tends to overuse: "Furthermore", "Moreover", "Additionally", "It is worth noting that", "It should be noted that", "In addition", "On the other hand".

**Scoring**:
- 0.0: Transitions are varied and content-specific.
- 1.0: One or two formulaic transitions.
- 2.0: Three or more formulaic transitions, or the same one used twice.
- 3.0: Most sentences connected by formulaic transitions; no content-specific linking.

## D3: Over-Smooth Logical Flow (0–3.0)

**Definition**: The paragraph reads as a perfectly smooth chain: background → gap → purpose → method → result → conclusion, with no friction, uncertainty, or researcher judgment visible.

**Scoring**:
- 0.0: Natural flow with visible authorial reasoning.
- 1.0: Somewhat smooth but has occasional specific judgment.
- 2.0: Very smooth; reads like a template-generated argument chain.
- 3.0: Perfectly smooth with zero human friction; every sentence is the statistically most likely next sentence.

## D4: Uniform Sentence Length and Rhythm (0–2.5)

**Definition**: Low burstiness — sentences are all roughly the same length and clause structure.

**Scoring**:
- 0.0: Varied sentence lengths (some short, some long).
- 1.0: Mild uniformity; most sentences within ±5 words of each other.
- 1.5: Noticeable uniformity; coefficient of variation in sentence length <0.3.
- 2.5: Extreme uniformity; all sentences nearly identical in length and structure.

## D5: Generic Academic Phrasing (0–3.0)

**Definition**: Use of broad, content-empty academic phrases: "plays an important role in", "has attracted increasing attention", "represents a significant challenge", "has important theoretical and practical significance", "in the evolving landscape of".

**Scoring**:
- 0.0: All claims are specific and tied to the thesis's own data/variables.
- 1.0: One or two generic phrases.
- 2.0: Several generic phrases; claims are abstract rather than thesis-specific.
- 3.0: Most of the paragraph is generic academic filler with no specific connection to the thesis's data or argument.

## D6: Overused Hedging or Balanced Claims (0–2.0)

**Definition**: Excessive use of "may", "might", "could", "it is possible that", or mechanical "on one hand... on the other hand" balance structures.

**Scoring**:
- 0.0: Hedges are used appropriately and sparingly.
- 1.0: Multiple hedges in close proximity, or mechanical balance structures.
- 2.0: Nearly every claim is hedged or balanced; no assertive academic voice.

## D7: Conclusion-Style Generalizations (0–2.5)

**Definition**: Broad summary statements that could apply to any thesis: "This study provides valuable insights", "These findings have important implications", "This research contributes to the field".

**Scoring**:
- 0.0: Conclusions are specific and tied to the actual findings.
- 1.0: One or two generic conclusion statements.
- 2.5: Most of the conclusion is generic; no specific finding-to-implication link.

## D8: Passive Voice and Nominalization Clusters (0–2.0)

**Definition**: Concentration of passive voice constructions and nominalized expressions ("the implementation of", "the utilization of", "the examination of").

**Scoring**:
- 0.0: Active voice predominates; nominalizations are natural.
- 1.0: Several passive constructions in close proximity.
- 2.0: Most sentences are passive or nominalized; no active agent visible.

## D9: Abstract-to-Concrete Imbalance (0–2.5)

**Definition**: The paragraph stays at a high level of abstraction without grounding claims in specific data, table references, variable names, or concrete examples from the thesis.

**Scoring**:
- 0.0: Claims are grounded with specific data references.
- 1.0: Some abstract claims without grounding.
- 2.5: Entire paragraph is abstract; no specific data, variable, or table reference.

## D10: Citation Pattern Regularity (0–2.0)

**Definition**: All citations follow the same format: (Author, Year) at the end of every sentence, or "Author (Year) stated that..." at the start of every paragraph.

**Scoring**:
- 0.0: Citations are placed naturally and variably.
- 1.0: Same citation format used repeatedly.
- 2.0: Mechanical citation placement; all sentences end with (Author, Year) or all start with Author (Year).

## D11: Lexical Flatness (0–2.5)

**Definition**: Repeated use of the same academic verbs ("examine", "explore", "investigate", "demonstrate", "show") and adjectives ("significant", "important", "notable") without variation.

**Scoring**:
- 0.0: Varied and precise vocabulary.
- 1.0: Some repetition of key verbs/adjectives.
- 2.5: Most sentences use the same set of academic verbs; lexical diversity is low.

## D12: Paragraph-Level Template Structure (0–4.0)

**Definition**: The paragraph follows a recognisable AI-generated template: "definition → source → item count" or "background → purpose → method → result → conclusion" or "concept → theorist → year → application".

**Scoring**:
- 0.0: No template; paragraph structure is content-driven.
- 1.0: Slight template feel but with some variation.
- 2.0: Clear template structure visible.
- 3.0: Strong template; every sentence fits a slot in a known pattern.
- 4.0: Multiple paragraphs share the same template; the pattern is mechanical.

## D13: Cross-Paragraph Structural Repetition (0–4.0)

**Definition**: Neighbouring paragraphs share the same internal architecture — same opening type, same sentence count, same functional path, same closing pattern.

**Scoring**:
- 0.0: Neighbouring paragraphs are structurally differentiated.
- 1.0: Two paragraphs share similar structure.
- 2.0: Three or more share the same architecture.
- 3.0: A whole section uses one paragraph pattern.
- 4.0: Multiple sections repeat the same paragraph architecture.

## D14: AI-Like Academic Smoothness / Low Human Friction (0–3.0)

**Definition**: The text lacks signs of a human author: no research decisions, no limitations stated mid-argument, no contrast with previous studies, no narrowing of scope, no genuine uncertainty. It reads as perfectly polished with no friction.

**Scoring**:
- 0.0: Visible human research judgment, boundary, or decision trace.
- 1.0: Some friction but mostly smooth.
- 2.0: Very smooth; little sign of an author behind the text.
- 3.0: Zero human friction; reads as fully machine-generated academic prose.

## D15: Thesis-Section Template Dependency (0–3.0)

**Definition**: The paragraph depends on a section-level template that AI commonly uses: literature review as "definition → citation → implication", hypothesis as "variable → mechanism → citation → hypothesis", methodology as "purpose → threshold → result → conclusion", conclusion as "result → theoretical meaning → practical implication".

**Scoring**:
- 0.0: No section template dependency.
- 1.0: Mild dependency; some sentences fit the template.
- 2.0: Clear section template; the paragraph follows the expected path closely.
- 3.0: The paragraph IS the section template; every sentence maps to a slot.

---

## Scoring Notes

- A "strong dimension" is one scored at ≥2.0 (or ≥2.5 for D12/D13).
- Single signals in isolation are not reliable AI tells — require clusters of 2+ strong dimensions before raising the pattern floor.
- Count occurrences before claiming overuse or uniformity.
- No double-counting: the same text span should not be counted under multiple dimensions.
- D12, D13, and D15 must always be checked manually — they require paragraph-level and section-level judgment.
- Protect legitimate citations from false positives: a real citation pattern is not necessarily an AI tell.
