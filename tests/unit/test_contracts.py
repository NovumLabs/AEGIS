from aegis.contracts.engine import ContractEngine

def test_explicitly_denied_tool_is_blocked():
    allowed, reason = ContractEngine({"dangerous"}).check("dangerous", {})
    assert not allowed and "denied" in reason

def test_other_tool_is_allowed_by_basic_policy():
    allowed, _ = ContractEngine().check("echo", {"message": "hi"})
    assert allowed
