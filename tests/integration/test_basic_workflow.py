from aegis.contracts.engine import ContractEngine
from aegis.core.execution import ExecutionEngine
from aegis.ledger.recorder import InMemoryRecorder
from aegis.tools.mock_tools import MockTools


def test_basic_workflow_end_to_end():
    recorder = InMemoryRecorder()
    engine = ExecutionEngine(MockTools(), ContractEngine(), recorder)
    result = engine.run_tool("integration-1", "add", {"a": 2, "b": 3})
    assert result == {"ok": True, "status": "completed", "output": {"sum": 5}}
    assert recorder.events[0]["event_type"] == "action_requested"
    assert recorder.events[-1]["event_type"] == "tool_completed"
