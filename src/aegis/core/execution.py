"""Small controlled tool execution loop for AEGIS v0.1.0."""
from typing import Any
from aegis.contracts.engine import ContractEngine
from aegis.exceptions import ToolExecutionError
from aegis.ledger.events import make_event
from aegis.ledger.recorder import InMemoryRecorder
from aegis.tools.mock_tools import MockTools

class ExecutionEngine:
    def __init__(self, tools: MockTools, contracts: ContractEngine, recorder: InMemoryRecorder) -> None:
        self.tools = tools
        self.contracts = contracts
        self.recorder = recorder

    def run_tool(self, workflow_id: str, tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        self.recorder.record(make_event(workflow_id, "action_requested", {"tool_name": tool_name, "arguments": arguments}))
        allowed, reason = self.contracts.check(tool_name, arguments)
        self.recorder.record(make_event(workflow_id, "contract_checked", {"tool_name": tool_name, "allowed": allowed, "reason": reason}))
        if not allowed:
            result = {"ok": False, "status": "blocked", "reason": reason}
            self.recorder.record(make_event(workflow_id, "action_blocked", result))
            return result
        try:
            output = self.tools.invoke(tool_name, arguments)
        except ToolExecutionError as exc:
            result = {"ok": False, "status": "failed", "error": str(exc)}
            self.recorder.record(make_event(workflow_id, "tool_failed", result))
            return result
        result = {"ok": True, "status": "completed", "output": output}
        self.recorder.record(make_event(workflow_id, "tool_completed", result))
        return result
