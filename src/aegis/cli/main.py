"""Minimal command-line smoke demonstration."""

from aegis.contracts.engine import ContractEngine
from aegis.core.execution import ExecutionEngine
from aegis.ledger.recorder import InMemoryRecorder
from aegis.tools.mock_tools import MockTools


def main() -> None:
    recorder = InMemoryRecorder()
    engine = ExecutionEngine(MockTools(), ContractEngine(), recorder)
    result = engine.run_tool(
        "aegis-cli-demo", "echo", {"message": "AEGIS v0.1.0 is running"}
    )
    print(result)
    print(f"Events recorded: {len(recorder.events)}")
