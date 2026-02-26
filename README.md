# Glyphh Models

Open source models for the [Glyphh](https://glyphh.ai) runtime.

## Models

| Model | Category | Description |
|-------|----------|-------------|
| [churn](churn/) | prediction | Customer churn predictor — encodes usage metrics into HDC vectors to identify churn risk patterns |
| [faq](faq/) | faq | FAQ helpdesk — domain-agnostic Q&A matching for knowledge base agents |
| [intent](intent/) | intent | Shared NL intent extraction — verb/noun/domain extraction with rule-based fast path + HDC similarity fallback |
| [toolrouter](toolrouter/) | routing | DevOps tool router — routes natural language requests to release step functions via HDC similarity |

## Usage

```bash
# Clone
git clone https://github.com/glyphh-ai/glyphh-models.git

# Test a model before deploying
glyphh model test ./churn

# Package a model
glyphh model package ./churn

# Deploy
glyphh model deploy ./churn.glyphh
```

## Model Structure

Every model follows the same pattern:

```
model-name/
├── manifest.yaml          # model identity and metadata
├── config.yaml            # encoder/runtime config, auto_load_concepts
├── encoder.py             # EncoderConfig + encode_query + entry_to_record
├── build.py               # package model into .glyphh file
├── tests.py               # test runner entry point
├── data/
│   └── *.jsonl            # training data (domain expertise)
├── tests/
│   ├── test-concepts.json # sample input data for testing (raw, no labels)
│   ├── conftest.py        # shared fixtures
│   ├── test_encoding.py   # config validation
│   ├── test_similarity.py # matching correctness
│   └── test_queries.py    # NL query inference
└── README.md
```

## Testing

Each model ships with a test suite. Tests use raw input data (no labels) and verify the model correctly classifies/matches against the training patterns.

```bash
# Run via CLI
glyphh model test ./churn
glyphh model test ./faq -v

# Or directly
cd churn/ && python tests.py
```

## Shared Intent Model

The [intent](intent/) model provides shared natural language intent extraction that downstream models can import instead of maintaining their own extraction logic. It decomposes queries into four signals:

- **action** — canonical verb (e.g., "dispatch" → `send`, "nuke" → `delete`)
- **target** — canonical noun (e.g., "customer profile" → `customer`)
- **domain** — weighted keyword scoring (e.g., "Slack", "#channel" → `messaging`)
- **keywords** — stop-word-filtered tokens for downstream BoW encoding

The rule-based fast path handles known vocabulary in sub-microsecond time. When an unknown synonym appears, the HDC fallback encodes it as a bag-of-words vector and matches against synonym cluster glyphs by cosine similarity.

```python
from encoder import IntentExtractor

extractor = IntentExtractor()
result = extractor.extract("Send a message to #general on Slack")
# {"action": "send", "target": "channel", "domain": "messaging", "keywords": "send message #general slack"}
```

**Current status**: Standalone model (Phase 1). Downstream migration of toolrouter (Phase 2) and BFCL (Phase 3) is planned.

## Customizing

Fork a model and replace the data files with your own content. The encoder config and test structure stay the same — just update the training data and test expectations.

## License

MIT
