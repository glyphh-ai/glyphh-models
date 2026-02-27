# Glyphh Models

Open source HDC models for the [Glyphh](https://glyphh.ai) runtime.

Browse and deploy models from the **[Glyphh Hub →](https://glyphh.ai/hub)**

---

## Repository Structure

Each model lives as a git submodule under this repo. The structure is the same
for every model:

```
model-name/
├── manifest.yaml        # identity, version, tags
├── config.yaml          # encoder config, similarity thresholds
├── encoder.py           # EncoderConfig + encode_query()
├── build.py             # package into .glyphh file
├── data/
│   └── *.jsonl          # training exemplars
├── tests/
│   ├── conftest.py
│   ├── test_encoding.py
│   └── test_similarity.py
└── benchmark/           # evaluation queries and results
```

## NL Intent Extraction

Intent extraction (action, target, domain, keywords) is built into the SDK —
no separate model required:

```python
from glyphh.intent import IntentExtractor

extractor = IntentExtractor()
result = extractor.extract("Send a message to #general on Slack")
# {"action": "send", "target": "channel", "domain": "messaging", "keywords": "..."}
```

Domain packs (filesystem, trading, travel, social, math, vehicle) are bundled
with the SDK. See [docs](https://glyphh.ai/docs) for details.

## Contributing a Model

1. Create a new model repo under `glyphh-ai/model-<name>`
2. Follow the structure above
3. Open a PR adding it as a submodule here

## License

MIT
