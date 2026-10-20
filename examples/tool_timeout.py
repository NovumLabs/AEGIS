"""Demonstrate a simulated tool failure."""

from aegis.contracts.engine import ContractEngine
from aegis.core.execution import ExecutionEngine
from aegis.ledger.recorder import InMemoryRecorder
from aegis.tools.mock_tools import MockTools


def main() -> None:
    recorder = InMemoryRecorder()
    engine = ExecutionEngine(MockTools(fail_tools={"slow"}), ContractEngine(), recorder)
    print(engine.run_tool("timeout-demo", "slow", {}))


if __name__ == "__main__":
    main()
