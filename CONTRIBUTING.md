# Contributing to AEGIS

## Development setup

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
pytest
```

## Expectations

- Add tests for behavior changes.
- Keep the core deterministic where possible.
- Document limitations and failure modes.
- Do not commit credentials or sensitive data.
