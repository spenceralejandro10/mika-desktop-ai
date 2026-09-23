from app.security.policy import requires_confirmation

def test_sensitive_action_requires_confirmation():
    assert requires_confirmation("delete_file")
    assert not requires_confirmation("current_time")
