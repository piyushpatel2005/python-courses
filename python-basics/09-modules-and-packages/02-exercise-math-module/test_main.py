from solution import vans_needed
import math

def test_vans_needed():
    """Round up by calling math.ceil"""
    original = math.ceil
    calls = []
    def tracked(value):
        calls.append(value)
        return original(value)
    try:
        math.ceil = tracked
        assert vans_needed(13) == 3
        assert vans_needed(6) == 1
        assert vans_needed(0) == 0
        assert len(calls) == 3, "Call math.ceil for each result."
        assert calls[0] == 13 / 6, "Divide the people by six before rounding."
    finally:
        math.ceil = original
