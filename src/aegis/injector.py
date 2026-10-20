"""Fault Injection Engine for AEGIS.

Simulates known failure classes under controlled conditions.
"""

import random
from typing import Any


class FaultInjector:
    """Injects configurable runtime faults into tool calls."""

    def __init__(
        self,
        scenario_config: dict[str, Any] | None = None,
        seed: int | None = None,
    ):
        self.config = scenario_config or {}
        self.fault_type = self.config.get("fault_type")
        self.target_tool = self.config.get("target_tool")
        self.probability = self.config.get("probability", 1.0)

        if seed is not None:
            random.seed(seed)

    def should_inject(self, tool_name: str) -> bool:
        """Determine if a fault should be injected for the given tool."""
        if not self.fault_type:
            return False
        if self.target_tool and self.target_tool != tool_name:
            return False
        return random.random() <= self.probability

    def apply_fault(self, tool_name: str, args: dict[str, Any]) -> dict[str, Any]:
        """Apply the configured fault based on the fault type."""
        if not self.should_inject(tool_name):
            return {
                "status": "success",
                "data": f"Executed {tool_name} successfully.",
            }

        if self.fault_type == "timeout":
            raise TimeoutError(f"Tool {tool_name} timed out during execution.")

        elif self.fault_type == "transient_error":
            raise ConnectionError(
                f"Transient network error in tool {tool_name}."
            )

        elif self.fault_type == "persistent_error":
            raise RuntimeError(f"Persistent failure in tool {tool_name}.")

        elif self.fault_type == "malformed_output":
            return {"status": "malformed", "corrupted_field": None}

        elif self.fault_type == "duplicate_request":
            return {
                "status": "success",
                "warning": "duplicate_execution_detected",
            }

        return {"status": "success", "data": "Default fallback execution."}