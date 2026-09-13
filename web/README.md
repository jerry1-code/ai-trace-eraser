# AI Trace Eraser — Web Application

A Flask-based web interface for detecting and rewriting AI traces in academic text.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Open http://localhost:5000
```

## Features

- **🔍 Local Detection** — No API key needed. Detects 6 core AI-writing-risk dimensions (D1, D2, D4, D5, D8, D14) locally using regex and heuristics.
- **✏️ AI Rewrite** — Connect any OpenAI-compatible API (OpenAI, DashScope, Azure, etc.) to run the full skill-based rewrite.
- **📊 Risk Scoring** — Paragraph-level and document-level risk index with pattern floors.
- **🛡️ Quality Gates** — The AI rewrite follows all 10 quality gates (A–J) from SKILL.md.
- **🌐 Bilingual** — Supports both English and Chinese academic text detection.

## Configuration

Set environment variables (optional — can also configure in the web UI):

```bash
export OPENAI_API_KEY="sk-..."           # or DASHSCOPE_API_KEY
export OPENAI_API_BASE="https://..."    # or DASHSCOPE_API_BASE
export AI_TRACE_MODEL="gpt-4o"          # or qwen-max
export PORT=5000                         # default: 5000
```

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Web UI |
| `/api/analyze` | POST | Local AI-trace detection (no API key needed) |
| `/api/rewrite` | POST | LLM-based rewrite (requires API key) |
| `/health` | GET | Health check |

### Example: Local Analysis

```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "In recent years, AI has attracted increasing attention. Furthermore, it plays an important role in the evolving landscape of innovation."}'
```

### Example: AI Rewrite

```bash
curl -X POST http://localhost:5000/api/rewrite \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text here", "api_key": "sk-...", "detector_score": "Turnitin 48%"}'
```

## Local Detection Dimensions

The web app performs local (no-LLM) detection on these dimensions:

| Dimension | Name | Method |
|---|---|---|
| D1 | Repetitive Sentence Starters | Sentence-start word frequency |
| D2 | Formulaic Transitions | Known transition phrase matching |
| D4 | Uniform Sentence Rhythm | Coefficient of variation in sentence length |
| D5 | Generic Academic Phrasing | Known generic phrase matching |
| D8 | Passive Voice Clusters | Passive/nominalization pattern matching |
| D14 | AI-Like Over-polished Phrases | Known AI-ism phrase matching |

For the full 15-dimension analysis and three-pass rewrite, use the AI Rewrite feature with an LLM API.
