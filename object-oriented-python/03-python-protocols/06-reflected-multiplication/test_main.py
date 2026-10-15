from solution import *


def test_01_reflected_multiplication():
    for points, factor in ((5, 4), (9, 0), (3, -2)):
        delta = ScoreDelta(points)
        result = factor * delta
        assert isinstance(result, ScoreDelta)
        assert result.points == (delta * factor).points == points * factor
        assert result is not delta and delta.points == points
    for bad in (True, 2.5, "3"):
        assert ScoreDelta(4).__rmul__(bad) is NotImplemented
    calls = []
    original = ScoreDelta.__mul__
    try:
        def sentinel(self, factor):
            calls.append((self, factor))
            return "delegated"
        ScoreDelta.__mul__ = sentinel
        item = ScoreDelta(7)
        assert item.__rmul__(6) == "delegated", "Delegate rather than duplicate __mul__."
        assert calls == [(item, 6)]
    finally:
        ScoreDelta.__mul__ = original
