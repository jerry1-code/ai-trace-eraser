# Academic Protection Rules

Protected elements catalog and integrity rules. These elements must be extracted before rewriting and compared after rewriting. If any protected element changes accidentally, it must be restored before final output.

---

## Protected Elements Catalog

### 1. Structural Elements

- **Section and sub-section headings**: exact text, numbering, and position on own line (e.g. "1.1 Research Background", "Chapter 2", "5.2.1 ...")
- **Figure and table captions**: exact text, numbering
- **Numbered/bulleted list markers**: preserved as-is
- **Paragraph breaks**: original number and position of paragraph boundaries must be preserved; no merging
- **Blank lines** separating paragraphs: preserved

### 2. Citation and Reference Elements

- **Citations and author names**: exact spelling, year, format
- **Reference list / bibliography entries**: LOCKED — author names, years, article titles, journal titles, volume/page numbers. Never rewritten, paraphrased, or "de-templated."
- **In-text citation format**: (Author, Year) or Author (Year) — preserved unless T9 explicitly restructures for naturalization
- **et al. abbreviations**: never touched

### 3. Research Data Elements

- **Variable names and abbreviations**: exact spelling and capitalization (e.g. "self-efficacy", "AI collaboration", "innovative behavior")
- **Hypothesis numbers and wording**: H1, H2, etc. — exact statement preserved
- **Coefficients**: β, B, SE, t, F values — exact
- **p-values and significance levels**: "p < 0.05", "p < .001", "**", "*" — exact format preserved
- **Model names**: exact (e.g. "Model 1", "PLS-SEM", "Bootstrap")
- **Table and figure numbers**: Table 1, Table 4.3, Figure 2 — exact
- **Sample size**: N = 300, n = 285 — exact
- **Statistical conclusions**: "H1 is supported", "the coefficient is significant" — meaning preserved
- **Statistical symbol formatting**: keep "p < 0.05", "β = 0.32", "VIF", "κ = 0.87", "R²", "χ²", "df", "CI", "CR", "AVE", "Cronbach's α" exactly as written — do not respace, reword, or convert

### 4. Front Matter and Identity

- **Thesis title and subtitle**: LOCKED
- **Author name**: LOCKED
- **Supervisor / advisor name and academic title**: LOCKED
- **Committee names**: LOCKED
- **Institution and department names**: LOCKED
- **Date**: LOCKED

### 5. Appendices and Instruments

- **Questionnaires and survey instruments**: LOCKED
- **Scale items and measurement instruments**: LOCKED
- **Interview guides**: LOCKED
- **Consent forms**: LOCKED
- **Raw-data tables**: LOCKED
- **Ethics statements**: LOCKED

### 6. Verbatim Quotations

- **Participant quotes / interview quotes**: never split, shortened, re-punctuated, or stylistically rewritten
- **Questionnaire item wording**: preserved exactly
- **Scale-item text**: preserved exactly

### 7. Protected Hedges and Claim-Strength Markers

These must NOT be deleted or strengthened/weakened during rewriting:

- **Epistemic hedges**: "may", "might", "could", "tentative", "preliminary", "exploratory", "appears to", "is likely", "suggests", "indicates", "is consistent with"
  - These must NOT be rewritten into "demonstrates", "proves", "establishes", "confirms", "shows that"
  - Keep the original epistemic strength exactly
- **Positionality markers**: "from the first author's perspective as...", "the authors served on..." — do not strip for flow
- **Scope qualifiers**: "in this sample", "for this cohort", "under the conditions tested", "between 2020 and 2024" — do not drop or generalize

**Rule**: When a paragraph is shortened or smoothed, hedges are protected ahead of any other compression target. If removing a hedge is the only way to hit a length target, do not remove it — find another edit.

---

## Protected Elements Check Procedure

### Before Rewriting (Phase 1.5)

Extract and list all protected elements from the target paragraphs:

```text
Paragraph ID:
Protected headings:
Protected citations:
Protected variables and abbreviations:
Protected statistical values:
Protected hypotheses:
Protected quotes:
Protected hedges and scope qualifiers:
```

### After Rewriting (Phase 7, Gate B)

Compare exact strings before and after:

```text
Paragraph ID:
Headings: [exact match? Yes/No]
Citations: [exact match? Yes/No]
Variables: [exact match? Yes/No]
Statistical values: [exact match? Yes/No]
Hypotheses: [exact match? Yes/No]
Quotes: [exact match? Yes/No]
Hedges: [exact match? Yes/No]
Any protected element changed: Yes/No
If Yes, restored before output: Yes/No
```

---

## Citation-Verification Boundary

During AI-risk rewriting, citations are LOCKED and not silently "corrected." If a citation looks inaccurate, duplicated, or inconsistent:
- Flag it separately for the user to verify
- Do NOT alter it inside the rewrite
- Do NOT "fix" a citation that might be intentionally formatted in a non-standard way

---

## Reference-Pollution Check (OUTPUT-BLOCKING)

Confirm no body-text sentence has leaked into a reference entry. A reference title containing discussion prose is corruption from a prior bad edit — restore the real title. Never let rewritten prose contaminate the bibliography.
