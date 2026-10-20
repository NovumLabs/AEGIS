"""Configuration defaults for AEGIS v0.1.0."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AegisConfig:
    max_tool_calls: int = 20
    record_payloads: bool = True
