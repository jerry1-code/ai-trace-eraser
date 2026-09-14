"""Detection-function regression tests for ai-trace-eraser.

Run:  cd web && python -m pytest test_detection.py -v

These lock in the fixes made during the code review:
  - Chinese D4 rhythm no longer auto-flags (len(split())=1 bug)
  - Chinese D1 starters detectable via 2-char signature
  - D8 passive regex no longer matches broad nominalization noise
  - split_paragraphs falls back to single-newline splitting
  - SKILL.md is passed to the LLM in full, not truncated
  - scope_risk uses a named constant, not a magic number
  - rate-limit / body-size guards are configured
"""
import inspect

import app


# ── Chinese detection (was broken: len(s.split())=1 → CV=0 → always 2.5) ──

def test_zh_d4_varied_not_flagged():
    zh = ("AI改变了工作方式。这种改变在知识密集型行业尤为突出，"
          "许多岗位的核心流程被重塑。但同时也催生了新的协作模式。")
    score, cv = app.detect_uniform_rhythm(zh)
    assert score == 0.0, f"varied Chinese rhythm should be 0, got {score} (cv={cv})"


def test_zh_d4_uniform_flagged():
    zh = "AI改变了工作方式。AI重塑了组织结构。AI提升了运行效率。AI优化了决策流程。"
    score, cv = app.detect_uniform_rhythm(zh)
    assert score > 0, f"truly uniform Chinese rhythm should be >0, got {score} (cv={cv})"


def test_zh_d1_repetitive_starters():
    zh = "近年来AI发展迅速。近年来技术突破。近年来产业扩大。近年来政策加码。"
    score, starters = app.detect_repetitive_starters(zh)
    assert score >= 2.0, f"repeated '近年' should score >=2, got {score}"


# ── English detection (regression: must still work) ────────────────────────

def test_en_d1_repetitive_starters():
    en = ("This study examines AI. This study uses survey. "
          "This study finds correlation. This study concludes positively.")
    score, _ = app.detect_repetitive_starters(en)
    assert score >= 2.0


def test_en_d4_uniform_flagged():
    en = "This study examines AI. This study uses survey. This study finds things."
    score, _ = app.detect_uniform_rhythm(en)
    assert score > 0


# ── D8 passive de-noise (removed over-broad nominalization patterns) ──────

def test_passive_noise_not_flagged():
    """'the version of' / 'the collection of' must not inflate D8."""
    noise = "the version of the software and the collection of data were examined."
    score, count = app.detect_passive_clusters(noise)
    assert score == 0.0, f"nominalization noise should score 0, got {score} (count={count})"


def test_passive_real_cluster_flagged():
    real = ("The data was collected. The results were analyzed. "
            "The model was tested. The survey was conducted.")
    score, count = app.detect_passive_clusters(real)
    assert score == 2.0, f"real passive cluster should score 2.0, got {score} (count={count})"


# ── Paragraph splitting (single-newline fallback) ──────────────────────────

def test_split_single_newline_fallback():
    text = "第一段内容。\n第二段内容。\n第三段内容。"
    assert len(app.split_paragraphs(text)) == 3


def test_split_blank_line_still_works():
    text = "第一段。\n\n第二段。"
    assert len(app.split_paragraphs(text)) == 2


# ── Structural / config guards ─────────────────────────────────────────────

def test_scope_risk_uses_named_constant():
    src = inspect.getsource(app.analyze_text)
    assert "section_repetition_score" in src
    assert "0.15 * 20)" not in src


def test_skill_not_truncated():
    src = inspect.getsource(app.llm_rewrite)
    assert "[:15000]" not in src


def test_rate_limit_configured():
    assert app.MAX_BODY_BYTES > 0
    assert app.RATE_MAX > 0
    assert app.RATE_WINDOW > 0


def test_end_to_end_chinese():
    zh = ("AI改变了工作方式。这种改变在知识密集型行业尤为突出，"
          "许多岗位的核心流程被重塑。但同时也催生了新的协作模式。")
    res = app.analyze_text(zh)
    assert res["total_paragraphs"] >= 1
    assert res["overall_level"] in ("low", "medium", "high", "critical")
