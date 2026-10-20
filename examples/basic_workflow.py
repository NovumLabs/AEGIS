from aegis.contracts.engine import ContractEngine
from aegis.core.execution import ExecutionEngine
from aegis.ledger.recorder import InMemoryRecorder
from aegis.tools.mock_tools import MockTools

def main() -> None:
    recorder = InMemoryRecorder()
    engine = ExecutionEngine(MockTools(), ContractEngine(), recorder)
    result = engine.run_tool("example-workflow", "echo", {"message": "Hello from AEGIS"})
    print("Result:", result)
    print("Recorded events:", len(recorder.events))

if __name__ == "__main__":
    main()
