"""Diagnostic Ranker and Evidence Evaluator."""

from typing import Any

from aegis.diagnosis.analyzer import LedgerAnalyzer
from aegis.diagnosis.schema import CandidateCause, DiagnosticReport
from aegis.diagnosis.taxonomy import DiagnosticConfidence, FaultCategory


class DiagnosticEngine:
    """Ranks root causes and determines confidence based on execution evidence."""

    def __init__(self, ledger_events: list[dict[str, Any]], ambiguity_threshold: float = 0.5):
        self.analyzer = LedgerAnalyzer(ledger_events)
        self.ambiguity_threshold = ambiguity_threshold

    def diagnose(self) -> DiagnosticReport:
        """Analyze trace events and return a ranked diagnostic report with abstention logic."""
        chain = self.analyzer.extract_causal_chain()
        failure_event = chain["failure_event"]
        error_category = chain["error_category"]
        preceding_actions = chain["preceding_actions"]

        # Abstain if there's no failure event or category is unknown with sparse evidence
        if not failure_event and not preceding_actions:
            return DiagnosticReport(
                status="abstain",
                ranked_causes=[],
                primary_cause=None,
                uncertainty_notes="Insufficient evidence in ledger to establish a causal chain.",
                metrics_summary={"evidence_count": 0},
            )

        event_id = failure_event.get("event_id") or failure_event.get("id", "unknown_event") if failure_event else "inferred_event"
        preceding_ids = [p.get("event_id") or p.get("id", "action") for p in preceding_actions]

        if error_category == FaultCategory.UNKNOWN and not failure_event:
            return DiagnosticReport(
                status="abstain",
                ranked_causes=[],
                primary_cause=None,
                uncertainty_notes="Ambiguous failure signature; unable to isolate root cause definitively.",
                metrics_summary={"evidence_count": len(preceding_actions)},
            )

        # Build candidate root cause
        confidence_score = 0.90 if error_category != FaultCategory.UNKNOWN else 0.40
        confidence_level = (
            DiagnosticConfidence.HIGH if confidence_score >= 0.85
            else DiagnosticConfidence.MEDIUM if confidence_score >= 0.60
            else DiagnosticConfidence.LOW
        )

        primary_cause = error_category
        description = f"Detected failure matching category '{error_category.value}' linked to preceding tool activity."

        candidate = CandidateCause(
            category=primary_cause,
            description=description,
            confidence_score=confidence_score,
            confidence_level=confidence_level,
            supporting_event_ids=[event_id] + preceding_ids,
            is_symptom=False,
        )

        # Optional secondary symptom candidate if preceding actions exist
        candidates = [candidate]
        if preceding_ids:
            symptom_candidate = CandidateCause(
                category=FaultCategory.PERSISTENT_FAILURE if primary_cause == FaultCategory.TIMEOUT else FaultCategory.UNKNOWN,
                description="Preceding action latency build-up acting as a contributing symptom.",
                confidence_score=0.45,
                confidence_level=DiagnosticConfidence.LOW,
                supporting_event_ids=preceding_ids[:1],
                is_symptom=True,
            )
            candidates.append(symptom_candidate)

        return DiagnosticReport(
            status="diagnosed",
            ranked_causes=candidates,
            primary_cause=primary_cause,
            uncertainty_notes=None,
            metrics_summary={"evidence_count": len(preceding_actions) + (1 if failure_event else 0)},
        )
