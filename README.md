# Glyphh Models

Open source example models for the [Glyphh](https://glyphh.ai) runtime.

Each model is its own repository, included here as a submodule.

## Models

| Model | Description |
|-------|-------------|
| [actions](https://github.com/glyphh-ai/model-actions) | Helpdesk action routing — maps natural language to API actions |
| [assistant](https://github.com/glyphh-ai/model-assistant) | Knowledge base assistant — FAQ matching and concept search |

## Usage

```bash
# Clone with all models
git clone --recursive https://github.com/glyphh-ai/glyphh-models.git

# Package a model
glyphh model package ./actions

# Deploy
glyphh model deploy ./actions
```

## Model Structure

Each model directory contains:

```
model-name/
├── manifest.yaml    # Model identity and metadata
├── config.yaml      # Encoder/runtime configuration
├── encoder.py       # Custom encoder (optional)
├── build.py         # Build script (optional)
└── data/            # Training data
    └── *.jsonl
```

## License

MIT
