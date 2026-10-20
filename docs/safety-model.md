# Safety Model

AEGIS v0.1.0 is a controlled prototype, not a certified safety system.

- Explicitly prohibited actions must be blocked.
- Unknown or invalid tool requests must not execute.
- Runtime checks must produce traceable decisions.
- Mock tools are used for initial tests; no production side effects are permitted.
- A finite test suite cannot establish that all unsafe actions are impossible.
- Future recovery proposals must be checked by a gate independent of the planner.
