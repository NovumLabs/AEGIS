"""Diagnostic Report Output Schemas."""

from dataclasses import dataclass, field
from typing import Any

from aegis.diagnosis.taxonomy import DiagnosticConfidence, FaultCategory


@dataclass
class CandidateCause:
    """A ranked candidate root cause with supporting evidence."""

    category: FaultCategory
    description: str
    confidence_score: float
    confidence_level: DiagnosticConfidence
    supporting_event_ids: list[str] = field(default_factory=list)
    is_symptom: bool = False


@dataclass
class DiagnosticReport:
    """Structured output report from the diagnostic engine."""

    status: str  # "diagnosed" or "abstain"
    ranked_causes: list[CandidateCause] = field(default_factory=list)
    primary_cause: FaultCategory | None = None
    uncertainty_notes: str | None = None
    metrics_summary: dict[str, Any] = field(default_factory=dict)
