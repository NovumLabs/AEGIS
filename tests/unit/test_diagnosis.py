"""Unit tests for Stage 4 Root-Cause Diagnosis engine."""

from aegis.diagnosis.ranker import DiagnosticEngine
from aegis.diagnosis.taxonomy import DiagnosticConfidence, FaultCategory


def test_diagnosis_timeout_root_cause():
    """Verify that a timeout failure ledger is correctly diagnosed with high confidence."""
    ledger_events = [
        {"event_id": "evt_1", "event_type": "tool_call", "details": {"tool": "mock_file_writer"}},
        {"event_id": "evt_2", "event_type": "tool_error", "details": {"error": "Tool mock_file_writer timed out during execution."}}
    ]

    engine = DiagnosticEngine(ledger_events)
    report = engine.diagnose()

    assert report.status == "diagnosed"
    assert report.primary_cause == FaultCategory.TIMEOUT
    assert len(report.ranked_causes) >= 1
    assert report.ranked_causes[0].category == FaultCategory.TIMEOUT
    assert report.ranked_causes[0].confidence_level == DiagnosticConfidence.HIGH
    assert "evt_2" in report.ranked_causes[0].supporting_event_ids


def test_diagnosis_abstention_on_insufficient_evidence():
    """Verify that the engine abstains when the ledger contains insufficient evidence."""
    ledger_events = []

    engine = DiagnosticEngine(ledger_events)
    report = engine.diagnose()

    assert report.status == "abstain"
    assert report.primary_cause is None
    assert report.uncertainty_notes is not None


def test_diagnosis_ambiguous_case_abstention():
    """Verify that ambiguous or unknown failure signatures trigger appropriate abstention."""
    ledger_events = [
        {"event_id": "evt_1", "event_type": "tool_call", "details": {"tool": "unknown_tool"}}
    ]

    engine = DiagnosticEngine(ledger_events)
    report = engine.diagnose()

    assert report.status == "abstain"
