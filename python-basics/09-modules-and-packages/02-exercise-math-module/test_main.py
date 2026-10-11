from solution import lanterns_needed
import math

def test_lanterns_needed():
    """Round up by calling math.ceil"""
    original = math.ceil
    calls = []
    def tracked(value):
        calls.append(value)
        return original(value)
    try:
        math.ceil = tracked
        assert lanterns_needed(13) == 3
        assert lanterns_needed(6) == 1
        assert lanterns_needed(0) == 0
        assert len(calls) == 3, "Call math.ceil for each result."
        assert calls[0] == 13 / 6, "Divide the sparks by six before rounding."
    finally:
        math.ceil = original
