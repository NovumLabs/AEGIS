"""JSON-serializable event records."""
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

def make_event(workflow_id: str, event_type: str, payload: dict[str, Any], sequence: int = 0) -> dict[str, Any]:
    return {"event_id": str(uuid4()), "workflow_id": workflow_id, "sequence": sequence,
            "event_type": event_type, "timestamp": datetime.now(timezone.utc).isoformat(), "payload": payload}
