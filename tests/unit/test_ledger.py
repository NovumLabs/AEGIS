from aegis.ledger.events import make_event
from aegis.ledger.recorder import InMemoryRecorder

def test_event_has_required_fields():
    event = make_event("workflow-1", "test_event", {"value": 7})
    assert event["event_id"] and event["timestamp"]
    assert event["workflow_id"] == "workflow-1"
    assert event["event_type"] == "test_event"
    assert event["payload"] == {"value": 7}

def test_recorder_preserves_event_order():
    recorder = InMemoryRecorder()
    recorder.record(make_event("w", "first", {}))
    recorder.record(make_event("w", "second", {}))
    assert [e["event_type"] for e in recorder.events] == ["first", "second"]
