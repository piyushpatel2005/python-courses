from solution import *


def test_01_explicit_cleanup():
    for name in ("first", "second", ""):
        events = []
        lease = Lease(name, events)
        assert not lease.closed and events == []
        lease.__del__()  # Explicit invocation only.
        assert lease.closed, "Delegate the hook to close()."
        assert events == [f"closed:{name}"]
        lease.__del__()
        lease.close()
        assert events == [f"closed:{name}"], "Cleanup must be idempotent."
    events = []
    first, second = Lease("A", events), Lease("B", events)
    first.__del__()
    assert first.closed and not second.closed
    second.close()
    assert events == ["closed:A", "closed:B"]
    calls = []
    original = Lease.close
    probe = Lease("delegation", [])
    try:
        def tracked(self):
            calls.append(self)
            original(self)
        Lease.close = tracked
        probe.__del__()
        assert calls == [probe], "Delegate to close() once instead of duplicating its cleanup policy."
    finally:
        Lease.close = original
        probe.close()
