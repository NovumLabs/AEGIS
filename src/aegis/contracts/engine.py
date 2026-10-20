"""Initial explicit-deny contract engine."""


class ContractEngine:
    def __init__(self, denied_tools: set[str] | None = None) -> None:
        self.denied_tools = denied_tools or set()

    def check(self, tool_name: str, arguments: dict) -> tuple[bool, str]:
        if tool_name in self.denied_tools:
            return False, f"Tool '{tool_name}' is explicitly denied by policy."
        if not isinstance(arguments, dict):
            return False, "Tool arguments must be a dictionary."
        return True, "Allowed by v0.1.0 basic policy."
