from aegis.contracts.engine import ContractEngine
from aegis.core.execution import ExecutionEngine
from aegis.ledger.recorder import InMemoryRecorder
from aegis.tools.mock_tools import MockTools


def make_engine(denied_tools=None, fail_tools=None):
    recorder = InMemoryRecorder()
    return ExecutionEngine(
        MockTools(fail_tools=fail_tools),
        ContractEngine(denied_tools=denied_tools),
        recorder,
    ), recorder


def test_echo_tool_completes_and_records_events():
    engine, recorder = make_engine()
    result = engine.run_tool("w1", "echo", {"message": "hello"})
    assert result["status"] == "completed"
    assert result["output"]["message"] == "hello"
    assert len(recorder.events) == 3


def test_denied_tool_is_not_invoked():
    engine, recorder = make_engine(denied_tools={"delete_all"})
    result = engine.run_tool("w2", "delete_all", {})
    assert result["status"] == "blocked"
    assert recorder.events[-1]["event_type"] == "action_blocked"


def test_tool_failure_is_recorded():
    engine, recorder = make_engine(fail_tools={"unstable"})
    result = engine.run_tool("w3", "unstable", {})
    assert result["status"] == "failed"
    assert recorder.events[-1]["event_type"] == "tool_failed"
