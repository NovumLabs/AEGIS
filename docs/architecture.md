# AEGIS Architecture

AEGIS is a runtime assurance and recovery framework for AI-agent workflows.

## Initial execution path

1. A workflow requests a tool action.
2. The runtime contract engine checks the action.
3. The tool executes only when allowed.
4. The ledger records the action and its outcome.
5. Evaluation code summarizes observed behavior.

## v0.1.0 scope

The first version provides a small controlled execution environment, event ledger, basic contracts, mock tools, and tests. Diagnosis, autonomous recovery, independent recovery verification, and replay are future milestones.

## Design principles

- Prefer deterministic core behavior.
- Record decisions and outcomes.
- Fail closed for explicitly prohibited actions.
- Keep the recovery planner separate from safety enforcement.
- Never claim universal safety from finite tests.
