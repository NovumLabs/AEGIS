"""Safe mock tools; no external side effects are performed."""
from typing import Any
from aegis.exceptions import ToolExecutionError

class MockTools:
    def __init__(self, fail_tools: set[str] | None = None) -> None:
        self.fail_tools = fail_tools or set()

    def invoke(self, tool_name: str, arguments: dict[str, Any]) -> Any:
        if tool_name in self.fail_tools or tool_name == "slow":
            raise ToolExecutionError(f"Simulated failure for tool '{tool_name}'.")
        if tool_name == "echo":
            return {"message": arguments.get("message", "")}
        if tool_name == "add":
            a, b = arguments.get("a"), arguments.get("b")
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise ToolExecutionError("The 'add' tool requires numeric a and b.")
            return {"sum": a + b}
        raise ToolExecutionError(f"Unknown tool '{tool_name}'.")
