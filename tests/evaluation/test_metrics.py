from aegis.evaluation.metrics import event_counts


def test_event_counts():
    events = [
        {"event_type": "tool_completed"},
        {"event_type": "tool_failed"},
        {"event_type": "tool_completed"},
    ]
    assert event_counts(events) == {"tool_completed": 2, "tool_failed": 1}
