"""Domain exceptions used by AEGIS."""
class AegisError(Exception):
    """Base exception for AEGIS errors."""

class ContractViolation(AegisError):
    """Raised when a requested action violates a runtime contract."""

class ToolExecutionError(AegisError):
    """Raised when a mock or registered tool fails during execution."""
