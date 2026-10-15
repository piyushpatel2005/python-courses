from solution import *


def test_01_explicit_cleanup():
    for name in ("first", "second", ""):
        events = []
        session = GameSession(name, events)
        assert not session.closed and events == []
        session.__del__()  # Explicit invocation only.
        assert session.closed, "Delegate the hook to close()."
        assert events == [f"closed:{name}"]
        session.__del__()
        session.close()
        assert events == [f"closed:{name}"], "Cleanup must be idempotent."
    events = []
    first, second = GameSession("A", events), GameSession("B", events)
    first.__del__()
    assert first.closed and not second.closed
    second.close()
    assert events == ["closed:A", "closed:B"]
    calls = []
    original = GameSession.close
    probe = GameSession("delegation", [])
    try:
        def tracked(self):
            calls.append(self)
            original(self)
        GameSession.close = tracked
        probe.__del__()
        assert calls == [probe], "Delegate to close() once instead of duplicating its cleanup policy."
    finally:
        GameSession.close = original
        probe.close()
