# AEGIS

**AEGIS — Runtime Assurance and Autonomous Recovery for AI-Agent Systems**

AEGIS is an open-source project by Novum Labs exploring how AI-agent workflows can detect execution faults, enforce runtime constraints, diagnose failures, and recover safely.

> **Status:** v0.1.0 starter implementation. This is an early prototype, not a certified safety system. Advanced diagnosis, autonomous recovery, independent recovery verification, and replay are not implemented yet.

## v0.1.0 includes

- Controlled mock-tool execution
- In-memory structured event ledger
- Basic explicit-deny contract engine
- Simulated tool failures
- Unit and integration tests
- Starter benchmark scenario catalogue
- GitHub Actions test workflow

## Quick start

Python 3.11 or newer is required.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Git Bash:

```bash
source .venv/Scripts/activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install and test:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
pytest
python -m aegis
```

## Architecture

- `src/aegis/core/`: controlled execution
- `src/aegis/ledger/`: structured event records
- `src/aegis/contracts/`: initial runtime policy checks
- `src/aegis/tools/`: safe mock tools
- `src/aegis/faults/`: planned fault-injection framework
- `src/aegis/evaluation/`: basic event metrics
- `tests/`: unit, integration, and evaluation tests
- `docs/`: architecture, safety, roadmap, and testing documentation

## Important limitations

- The event ledger is in-memory and is not durable across process restarts.
- The contract engine is intentionally minimal and is not a complete authorization system.
- The tool environment is mocked; no production integration is provided.
- Fault injection is not yet a complete benchmark framework.
- No automatic recovery or formal safety guarantee is provided by this version.

See [`docs/development-roadmap.md`](docs/development-roadmap.md). Do not connect this prototype to production systems or tools with irreversible side effects.

## License

MIT. See [`LICENSE`](LICENSE).
