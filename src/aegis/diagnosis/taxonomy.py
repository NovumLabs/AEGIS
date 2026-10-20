"""Structured Fault Taxonomy for Root-Cause Diagnosis."""

from enum import Enum


class FaultCategory(str, Enum):
    """Enumeration of standardized root-cause failure categories."""

    TIMEOUT = "timeout"
    TRANSIENT_NETWORK = "transient_network"
    MALFORMED_OUTPUT = "malformed_output"
    PERSISTENT_FAILURE = "persistent_failure"
    POLICY_VIOLATION = "policy_violation"
    UNKNOWN = "unknown"


class DiagnosticConfidence(str, Enum):
    """Confidence levels for ranked root causes."""

    HIGH = "high"       # >= 0.85
    MEDIUM = "medium"   # 0.60 - 0.84
    LOW = "low"         # < 0.60
    UNKNOWN = "unknown" # Insufficient evidence / abstain
