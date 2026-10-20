"""Fault Scenario Definitions and Configurations."""

from typing import Any


class ScenarioRegistry:
    """Manages baseline and fault injection test scenarios."""

    @staticmethod
    def get_standard_scenarios() -> list[dict[str, Any]]:
        """Return foundational fault scenarios for testing."""
        return [
            {
                "id": "scenario_01_timeout",
                "description": "Tool times out under load",
                "target_tool": "mock_file_writer",
                "fault_type": "timeout",
                "recoverable": True,
                "seed": 42,
            },
            {
                "id": "scenario_02_transient_error",
                "description": "Transient connection drop",
                "target_tool": "mock_payment_api",
                "fault_type": "transient_error",
                "recoverable": True,
                "seed": 42,
            },
            {
                "id": "scenario_03_malformed_output",
                "description": "Tool returns invalid schema fields",
                "target_tool": "mock_query_tool",
                "fault_type": "malformed_output",
                "recoverable": True,
                "seed": 42,
            },
            {
                "id": "scenario_04_persistent_error",
                "description": "Unrecoverable hardware/service fault",
                "target_tool": "mock_file_writer",
                "fault_type": "persistent_error",
                "recoverable": False,
                "seed": 42,
            },
        ]
