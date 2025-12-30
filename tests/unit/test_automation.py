from src.automation.escalation_logic import should_escalate

def test_should_escalate():
    assert should_escalate({"severity": "Critical"})
    assert not should_escalate({"severity": "Medium"})
