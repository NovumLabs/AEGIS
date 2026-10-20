from aegis.contracts.engine import ContractEngine
from aegis.core.execution import ExecutionEngine
from aegis.ledger.recorder import InMemoryRecorder
from aegis.tools.mock_tools import MockTools


def main() -> None:
    recorder = InMemoryRecorder()
    engine = ExecutionEngine(
        MockTools(), ContractEngine(denied_tools={"delete_all"}), recorder
    )
    print(engine.run_tool("contract-demo", "delete_all", {}))
    print("Recorded events:", len(recorder.events))


if __name__ == "__main__":
    main()
