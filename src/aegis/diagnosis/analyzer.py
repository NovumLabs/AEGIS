"""Ledger Event Analyzer for Causal Tracing."""

from typing import Any

from aegis.diagnosis.taxonomy import FaultCategory


class LedgerAnalyzer:
    """Extracts and analyzes causal chains from execution ledger events."""

    def __init__(self, ledger_events: list[dict[str, Any]]):
        self.events = ledger_events

    def extract_causal_chain(self) -> dict[str, Any]:
        """Analyze ledger events to trace error triggers and preceding actions."""
        preceding_actions = []
        failure_event = None
        error_category = FaultCategory.UNKNOWN

        for event in self.events:
            event_type = event.get("event_type") or event.get("type")
            details = event.get("details", {})
            error_msg = str(details.get("error", "")).lower()

            if event_type in ("tool_call", "action_invoked"):
                preceding_actions.append(event)

            elif event_type in ("tool_error", "execution_failed") or error_msg:
                failure_event = event
                error_category = self._classify_error(error_msg)

        return {
            "preceding_actions": preceding_actions,
            "failure_event": failure_event,
            "error_category": error_category,
        }

    def _classify_error(self, error_msg: str) -> FaultCategory:
        """Map raw error messages to the structured fault taxonomy."""
        if "timeout" in error_msg or "timed out" in error_msg:
            return FaultCategory.TIMEOUT
        elif "connection" in error_msg or "network" in error_msg:
            return FaultCategory.TRANSIENT_NETWORK
        elif "malformed" in error_msg or "schema" in error_msg:
            return FaultCategory.MALFORMED_OUTPUT
        elif "persistent" in error_msg or "runtime" in error_msg:
            return FaultCategory.PERSISTENT_FAILURE
        elif "policy" in error_msg or "denied" in error_msg:
            return FaultCategory.POLICY_VIOLATION
        return FaultCategory.UNKNOWN
