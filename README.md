# AEGIS

### Runtime Assurance and Autonomous Recovery for AI-Agent Systems

**Building more reliable AI-agent systems through runtime checks, controlled execution, fault analysis, and evidence-driven engineering.**

AEGIS is an open-source project by **Novum Labs** exploring how AI-agent workflows can detect execution faults, enforce runtime constraints, diagnose failures, and recover safely.

The project follows an incremental engineering approach: begin with controlled execution and explicit policy checks, evaluate behavior through tests and fault scenarios, and progressively investigate more advanced reliability mechanisms.

> **Current status: v0.1.0 — Starter implementation.** AEGIS is an early-stage prototype, not a certified safety system. Advanced diagnosis, autonomous recovery, independent recovery verification, and replay are not implemented in this version.

---

## Table of Contents

- [Project Objectives](#project-objectives)
- [Current Capabilities](#current-capabilities)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Running Tests](#running-tests)
- [Repository Structure](#repository-structure)
- [Development Roadmap](#development-roadmap)
- [Limitations and Safety](#limitations-and-safety)
- [Contributing](#contributing)
- [License](#license)
- [About Novum Labs](#about-novum-labs)

---

## Project Objectives

AI agents can encounter tool errors, invalid actions, unexpected outputs, and violations of execution constraints. A reliability-oriented system needs mechanisms to observe execution, evaluate constraints, record events, and assess failures.

AEGIS investigates these engineering questions:

1. **Runtime assurance:** Can execution be checked against explicit constraints?
2. **Controlled execution:** Can tool interactions be isolated and observed?
3. **Failure visibility:** Can execution faults be represented as structured events?
4. **Recovery engineering:** How can a system propose and execute recovery actions while checking their outcomes?
5. **Evaluation and reproducibility:** Can reliability behavior be tested through repeatable scenarios?

These are research and development objectives, not claims that every capability is already implemented.

## Current Capabilities

The v0.1.0 starter implementation includes:

- **Controlled mock-tool execution** for testing workflows in a controlled environment.
- **In-memory event ledger** for recording structured execution events.
- **Basic contract engine** implementing explicit-deny policy checks.
- **Simulated tool failures** for exercising selected failure scenarios.
- **Unit and integration tests** for implemented components.
- **Starter benchmark scenario catalogue** for organizing evaluation scenarios.
- **GitHub Actions workflow** for automated testing.

Capabilities should be assessed against the actual implementation and test suite. The presence of a component does not, by itself, establish comprehensive reliability or safety.

## Architecture

AEGIS is organized into components with distinct responsibilities.

| Component | Responsibility |
|---|---|
| Core execution | Controlled execution flow |
| Contract engine | Initial runtime policy checks |
| Mock tools | Controlled tool behavior for testing |
| Fault handling | Initial simulated failures and planned fault-injection development |
| Event ledger | Structured, in-memory execution records |
| Evaluation | Basic event metrics and evaluation support |
| Tests | Unit, integration, and evaluation tests |

### Execution Flow

The conceptual flow for the starter implementation is:

1. An execution request enters the controlled execution layer.
2. The initial contract engine evaluates applicable explicit-deny constraints.
3. Permitted execution proceeds through the controlled mock-tool environment.
4. Selected tool failures can be simulated.
5. Structured events are recorded in the in-memory ledger.
6. Tests and basic evaluation components examine the observed behavior.

This describes the intended component flow; the exact sequence and behavior depend on the implementation of each execution path.

## Quick Start

### Requirements

- Python 3.11 or newer
- Git
- A terminal such as PowerShell, Git Bash, or a macOS/Linux shell

### 1. Clone the repository

```bash
git clone https://github.com/NovumLabs/AEGIS.git
cd AEGIS
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Git Bash**

```bash
source .venv/Scripts/activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

If PowerShell blocks virtual-environment activation, follow your organization's security policy rather than changing execution-policy settings indiscriminately.

### 4. Install the project

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install AEGIS and its development dependencies:

```bash
python -m pip install -e ".[dev]"
```

This installation command assumes the repository's `pyproject.toml` defines the `dev` optional dependency group.

### 5. Run AEGIS

```bash
python -m aegis
```

This command assumes the module entry point is available in the installed version.

## Running Tests

Run the project's test suite from the repository root:

```bash
python -m pytest
```

For more detailed output:

```bash
python -m pytest -v
```

To run a specific test file:

```bash
python -m pytest tests/
```

The commands above use pytest to discover and execute the available tests. Actual test results depend on the current code, dependencies, and environment.

For research and development, test reports should distinguish between:

- Tests that passed
- Tests that failed
- Scenarios that were not executed
- Known limitations
- Behaviors that remain unverified

A passing test suite is useful evidence about tested behavior; it is not a formal proof of system safety.

## Repository Structure

The current project is organized around the following areas:

```text
AEGIS/
├── src/
│   └── aegis/
│       ├── core/          # Controlled execution
│       ├── ledger/        # Structured event records
│       ├── contracts/     # Initial runtime policy checks
│       ├── tools/         # Safe mock tools
│       ├── faults/        # Fault-handling development
│       └── evaluation/    # Basic event metrics
├── tests/                 # Unit, integration, evaluation tests
├── docs/                  # Architecture, safety, roadmap, testing
├── README.md
├── LICENSE
└── pyproject.toml
```

This tree illustrates the documented component layout. Consult the actual repository for the complete file structure.

## Development Roadmap

AEGIS is being developed incrementally. Potential next milestones include:

### Stage 1 — Execution and Policy Foundations

- Strengthen controlled execution paths.
- Expand contract checks and negative test cases.
- Improve structured event consistency.
- Document expected behavior and failure conditions.

### Stage 2 — Persistent Event Ledger

- Investigate durable event storage.
- Define event schemas and execution identifiers.
- Add tests for persistence, retrieval, and error handling.

### Stage 3 — Fault-Injection Evaluation

- Expand the scenario catalogue.
- Add repeatable fault-injection cases.
- Define measurable outcomes and baseline comparisons.
- Improve evaluation reports and reproducibility.

### Stage 4 — Recovery Proposals

- Investigate constrained recovery proposals.
- Define explicit preconditions and limits for recovery actions.
- Test recovery decisions in controlled environments.

### Stage 5 — Independent Recovery Verification

- Investigate verification of recovery outcomes.
- Test cases where recovery appears successful but the original fault remains.
- Record verification results and unresolved failures.

### Stage 6 — Execution Replay and Traceability

- Investigate replayable execution records.
- Define requirements for deterministic replay where feasible.
- Improve debugging and failure reconstruction.

These are development directions, not commitments that the listed capabilities already exist or are scheduled for a particular release.

See the [Development Roadmap](https://github.com/NovumLabs/AEGIS/blob/main/docs/development-roadmap.md) for the project's detailed planning.

## Limitations and Safety

AEGIS v0.1.0 has important limitations:

- The event ledger is in-memory and does not persist across process restarts.
- The contract engine is intentionally minimal and is not a complete authorization system.
- Tool interactions use a mocked environment; production integrations are not provided.
- Fault injection is not yet a complete benchmark framework.
- Advanced failure diagnosis is not implemented.
- Autonomous recovery and independent recovery verification are not implemented.
- Execution replay is not implemented.
- No formal safety guarantee, certification, or production readiness is claimed.

**Safety guidance:** Do not connect this prototype to production systems, sensitive environments, or tools with irreversible side effects. Mock-tool testing does not establish that equivalent real-world integrations would be safe.

## Contributing

Contributions, issue reports, technical feedback, and reproducible bug reports are welcome.

When contributing:

1. Describe the problem or proposed improvement clearly.
2. Include reproducible steps where possible.
3. Add or update tests for behavioral changes.
4. Document limitations and assumptions.
5. Avoid presenting unimplemented features as available capabilities.

Please use the repository's GitHub Issues for bug reports and feature proposals. Follow any contribution instructions published in the repository.

## License

AEGIS is distributed under the MIT License. See [`LICENSE`](LICENSE) for the complete license text.

## About Novum Labs

**Novum Labs** is an Indian technology company working on artificial intelligence research, software engineering, and practical AI systems.

AEGIS is part of our exploration of reliable AI-agent architectures and evidence-driven software engineering.

- **GitHub Organization:** https://github.com/NovumLabs
- **Website:** https://www.novumlabs.net
- **AEGIS Repository:** https://github.com/NovumLabs/AEGIS

---

**AEGIS — Novum Labs**

*Research with rigor. Engineer with purpose. Build for impact.*
