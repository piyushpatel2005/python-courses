from solution import *


def test_behavior():
    """Release a resource with finally."""
    class Probe:
        def __init__(self, fail):
            self.fail = fail
            self.closes = 0
        def read(self):
            if self.fail:
                raise LookupError("missing replay event")
            return "lit the watchtower beacon"
        def close(self):
            self.closes += 1
    ok = Probe(False)
    assert read_replay_and_close(ok) == "lit the watchtower beacon"
    assert ok.closes == 1
    bad = Probe(True)
    try:
        read_replay_and_close(bad)
    except LookupError as error:
        assert str(error) == "missing replay event"
    else:
        assert False, "Preserve the read error"
    assert bad.closes == 1
    import ast, inspect
    assert any(isinstance(n, ast.Try) and n.finalbody for n in ast.walk(ast.parse(inspect.getsource(read_replay_and_close)))), "Use finally for cleanup"
