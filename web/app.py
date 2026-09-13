#!/usr/bin/env python3
"""
AI Trace Eraser — Web Application
A Flask-based web interface for detecting and rewriting AI traces in academic text.
"""

import os
import re
import json
import textwrap
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# ─── Config ───────────────────────────────────────────────────────────────────
# Set your API key via environment variable, or hardcode here (not recommended for production)
API_KEY = os.environ.get("OPENAI_API_KEY", os.environ.get("DASHSCOPE_API_KEY", ""))
API_BASE = os.environ.get("OPENAI_API_BASE", os.environ.get("DASHSCOPE_API_BASE", "https://api.openai.com/v1"))
MODEL = os.environ.get("AI_TRACE_MODEL", "gpt-4o")
SKILL_PATH = os.path.join(os.path.dirname(__file__), "..", "SKILL.md")

# ─── Load SKILL.md ────────────────────────────────────────────────────────────
def load_skill():
    """Load the SKILL.md file content."""
    try:
        with open(SKILL_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None

SKILL_CONTENT = load_skill()

# ─── Local Detection (without LLM) ─────────────────────────────────────────────
def split_paragraphs(text):
    """Split text into paragraphs."""
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    return paragraphs

def detect_repetitive_starters(paragraph):
    """D1: Detect repetitive sentence starters."""
    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
    starters = []
    for s in sentences:
        words = s.strip().split()
        if words:
            starters.append(words[0].lower())
    # Count repeats
    from collections import Counter
    counts = Counter(starters)
    max_repeat = max(counts.values()) if counts else 0
    if max_repeat >= 4:
        return 3.0, list(counts.items())
    elif max_repeat >= 3:
        return 2.0, list(counts.items())
    elif max_repeat >= 2:
        return 1.0, list(counts.items())
    return 0.0, []

def detect_formulaic_transitions(paragraph):
    """D2: Detect formulaic transitions."""
    formulaic = [
        "furthermore", "moreover", "additionally", "it is worth noting that",
        "it should be noted that", "in addition", "on the other hand",
        "however", "therefore", "thus", "consequently",
        "此外", "而且", "另外", "值得注意的是", "综上所述", "因此", "然而",
    ]
    lower = paragraph.lower()
    count = sum(1 for f in formulaic if f in lower)
    if count >= 3:
        return 3.0, count
    elif count >= 2:
        return 2.0, count
    elif count >= 1:
        return 1.0, count
    return 0.0, 0

def detect_generic_phrasing(paragraph):
    """D5: Detect generic academic phrasing."""
    generic = [
        "plays an important role", "has attracted increasing attention",
        "represents a significant challenge", "has important theoretical and practical",
        "in the evolving landscape", "it is widely recognized",
        "plays a crucial role", "plays a pivotal role",
        "发挥着重要作用", "引起了广泛关注", "具有重要的理论意义和实践意义",
        "在当今社会", "随着.*的快速发展", "已经成为一个热门话题",
    ]
    lower = paragraph.lower()
    count = 0
    for phrase in generic:
        if ".*" in phrase:
            count += len(re.findall(phrase, lower))
        elif phrase in lower:
            count += 1
    if count >= 3:
        return 3.0, count
    elif count >= 2:
        return 2.0, count
    elif count >= 1:
        return 1.0, count
    return 0.0, 0

def detect_uniform_rhythm(paragraph):
    """D4: Detect uniform sentence length."""
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', paragraph) if s.strip()]
    if len(sentences) < 3:
        return 0.0, 0
    lengths = [len(s.split()) for s in sentences]
    avg = sum(lengths) / len(lengths)
    if avg == 0:
        return 0.0, 0
    cv = (max(lengths) - min(lengths)) / avg if avg > 0 else 0
    if cv < 0.15:
        return 2.5, round(cv, 2)
    elif cv < 0.3:
        return 1.5, round(cv, 2)
    elif cv < 0.5:
        return 1.0, round(cv, 2)
    return 0.0, round(cv, 2)

def detect_ai_phrases(paragraph):
    """D14: Detect over-polished AI phrases."""
    ai_phrases = [
        "sheds light on", "fills a critical gap", "more importantly",
        "delve into", "plays a pivotal role", "underscores the significance",
        "a rich tapestry", "a testament to", "navigate the",
        "leverage", "realm", "embark on", "cornerstone", "synergy",
        "holistic", "cutting-edge", "multifaceted", "intricate",
        "utilize", "commence", "ascertain", "endeavor", "meticulous",
        "the practical upshot is", "what this tells us is",
        "赋能", "助力", "深入探索", "全方位", "多维度", "协同", "闭环",
    ]
    lower = paragraph.lower()
    count = sum(1 for phrase in ai_phrases if phrase in lower)
    if count >= 3:
        return 3.0, count
    elif count >= 2:
        return 2.0, count
    elif count >= 1:
        return 1.0, count
    return 0.0, 0

def detect_passive_clusters(paragraph):
    """D8: Detect passive voice clusters."""
    passive_patterns = [
        r'\b(?:was|were|is|are|been|being|be)\s+\w+ed\b',
        r'\b(?:was|were|is|are|been|being)\s+\w+en\b',
        r'the\s+\w+ion\s+of',
        r'the\s+\w+tion\s+of',
    ]
    count = 0
    for pattern in passive_patterns:
        count += len(re.findall(pattern, paragraph, re.IGNORECASE))
    if count >= 4:
        return 2.0, count
    elif count >= 2:
        return 1.0, count
    return 0.0, 0

def analyze_paragraph(paragraph, idx):
    """Run local detection on a single paragraph."""
    results = {}

    d1, starters = detect_repetitive_starters(paragraph)
    results["D1"] = {"score": d1, "max": 3.0, "name": "Repetitive Sentence Starters / 重复句首"}

    d2, trans_count = detect_formulaic_transitions(paragraph)
    results["D2"] = {"score": d2, "max": 3.0, "name": "Formulaic Transitions / 套路过渡词"}

    d4, cv = detect_uniform_rhythm(paragraph)
    results["D4"] = {"score": d4, "max": 2.5, "name": "Uniform Sentence Rhythm / 句式节奏单一"}

    d5, gen_count = detect_generic_phrasing(paragraph)
    results["D5"] = {"score": d5, "max": 3.0, "name": "Generic Academic Phrasing / 空泛学术用语"}

    d8, pass_count = detect_passive_clusters(paragraph)
    results["D8"] = {"score": d8, "max": 2.0, "name": "Passive Voice Clusters / 被动语态堆叠"}

    d14, ai_count = detect_ai_phrases(paragraph)
    results["D14"] = {"score": d14, "max": 3.0, "name": "AI-Like Over-polished Phrases / AI腔"}

    # Calculate raw risk
    total_score = sum(v["score"] for v in results.values())
    total_possible = sum(v["max"] for v in results.values())
    raw_risk = min(total_score / total_possible, 1.0) * 100 if total_possible > 0 else 0

    # Apply pattern floor
    strong_dims = sum(1 for v in results.values() if v["score"] >= 2.0)
    if strong_dims >= 4:
        risk_index = max(raw_risk, 38)
    elif strong_dims >= 3:
        risk_index = max(raw_risk, 28)
    elif strong_dims >= 2:
        risk_index = max(raw_risk, 18)
    else:
        risk_index = raw_risk

    # Determine risk level
    if risk_index >= 40:
        level = "critical"
    elif risk_index >= 25:
        level = "high"
    elif risk_index >= 15:
        level = "medium"
    else:
        level = "low"

    # Word count: split by spaces for English, count chars for Chinese
    if any('\u4e00' <= ch <= '\u9fff' for ch in paragraph):
        # Has Chinese characters — count meaningful chars (Chinese chars + word tokens)
        import re as _re
        chinese_chars = len(_re.findall(r'[\u4e00-\u9fff]', paragraph))
        english_words = len(_re.findall(r'[a-zA-Z]+', paragraph))
        word_count = chinese_chars + english_words
    else:
        word_count = len(paragraph.split())

    return {
        "id": idx,
        "preview": paragraph[:100] + ("..." if len(paragraph) > 100 else ""),
        "word_count": word_count,
        "dimensions": results,
        "total_score": round(total_score, 1),
        "risk_index": round(risk_index, 1),
        "risk_level": level,
        "strong_dimensions": strong_dims,
    }

def analyze_text(text):
    """Run local detection on full text."""
    paragraphs = split_paragraphs(text)
    results = [analyze_paragraph(p, i + 1) for i, p in enumerate(paragraphs)]

    avg_risk = sum(r["risk_index"] for r in results) / len(results) if results else 0
    high_share = sum(1 for r in results if r["risk_index"] >= 40) / len(results) * 100 if results else 0
    medium_share = sum(1 for r in results if r["risk_index"] >= 25) / len(results) * 100 if results else 0

    scope_risk = (0.45 * avg_risk + 0.25 * high_share + 0.15 * medium_share + 0.15 * 20)
    scope_risk = min(scope_risk, 100)

    if scope_risk >= 40:
        overall_level = "critical"
    elif scope_risk >= 25:
        overall_level = "high"
    elif scope_risk >= 15:
        overall_level = "medium"
    else:
        overall_level = "low"

    return {
        "paragraphs": results,
        "total_paragraphs": len(results),
        "total_words": sum(r["word_count"] for r in results),
        "average_risk": round(avg_risk, 1),
        "high_risk_share": round(high_share, 1),
        "medium_risk_share": round(medium_share, 1),
        "scope_risk_index": round(scope_risk, 1),
        "overall_level": overall_level,
    }

# ─── LLM Rewrite ──────────────────────────────────────────────────────────────
def llm_rewrite(text, detector_score="", api_key=None, api_base=None, model=None):
    """Use LLM to rewrite text following the skill rules."""
    key = api_key or API_KEY
    base = api_base or API_BASE
    mdl = model or MODEL

    if not key:
        return None, "No API key configured. Set OPENAI_API_KEY or DASHSCOPE_API_KEY environment variable."

    if not SKILL_CONTENT:
        return None, "SKILL.md not found."

    client = OpenAI(api_key=key, base_url=base)

    system_prompt = textwrap.dedent(f"""
    You are an AI Trace Eraser agent. Follow the SKILL.md instructions exactly.
    Apply the three iron rules: no whole-paragraph regeneration, no fabrication,
    no word-count reduction. Use minimal edits only.

    Here is the SKILL.md content:

    {SKILL_CONTENT[:15000]}
    """)

    user_prompt = textwrap.dedent(f"""
    Please analyze and rewrite the following academic text to reduce AI-writing-risk patterns.

    External detector score: {detector_score or "Not provided"}

    Text to analyze and rewrite:
    ---
    {text}
    ---

    Output format:
    1. Detection Report: List each paragraph with its hit dimensions and risk level.
    2. Rewrite Strategy: Which techniques to apply.
    3. Rewritten Text: The revised text with minimal edits.
    4. Quality Check: Brief Gate A-J summary.
    5. Word Count: Before and after.
    """)

    try:
        response = client.chat.completions.create(
            model=mdl,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
            max_tokens=4096,
        )
        return response.choices[0].message.content, None
    except Exception as e:
        return None, str(e)

# ─── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json()
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"error": "No text provided"}), 400
    result = analyze_text(text)
    return jsonify(result)

@app.route("/api/rewrite", methods=["POST"])
def api_rewrite():
    data = request.get_json()
    text = data.get("text", "")
    detector_score = data.get("detector_score", "")
    api_key = data.get("api_key", "")
    api_base = data.get("api_base", "")
    model = data.get("model", "")

    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    result, error = llm_rewrite(
        text, detector_score,
        api_key=api_key or None,
        api_base=api_base or None,
        model=model or None,
    )
    if error:
        return jsonify({"error": error}), 500
    return jsonify({"result": result})

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "skill_loaded": SKILL_CONTENT is not None,
        "api_configured": bool(API_KEY),
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
