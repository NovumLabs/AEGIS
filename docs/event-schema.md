# Event Schema

AEGIS v0.1.0 uses JSON-serializable event records.

Initial fields:
- `event_id`: unique event identifier
- `workflow_id`: workflow identifier
- `sequence`: event sequence number within a workflow (initial implementation defaults to zero)
- `event_type`: event category
- `timestamp`: UTC ISO-8601 timestamp
- `payload`: event-specific JSON-compatible data

Avoid storing credentials, secrets, or unnecessary personal data in event payloads.
