# Glyphh Models

Open source model catalog for the [Glyphh](https://glyphh.ai) runtime.

Each model is its own repository, included here as a submodule.

## Models

| Model | Description |
|-------|-------------|
| [actions](https://github.com/glyphh-ai/model-actions) | Intent classification and action routing |
| [assistant](https://github.com/glyphh-ai/model-assistant) | Conversational AI assistant |

## Usage

```bash
# Clone with all models
git clone --recursive https://github.com/glyphh-ai/glyphh-models.git

# Or via the Glyphh CLI
glyphh catalog list
glyphh catalog download actions
glyphh model deploy ./actions.glyphh
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
