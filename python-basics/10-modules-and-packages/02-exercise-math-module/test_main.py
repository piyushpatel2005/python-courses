from solution import boards_needed
import math

def test_boards_needed():
    """Round up the length with math.ceil."""
    original = math.ceil
    calls = []
    def tracked(value):
        calls.append(value)
        return original(value)
    try:
        math.ceil = tracked
        assert boards_needed(13) == 3
        assert boards_needed(6) == 1
        assert boards_needed(0) == 0
        assert len(calls) == 3, "Call math.ceil for each calculation."
        assert calls[0] == 13 / 6, "Divide the length by six before rounding."
    finally:
        math.ceil = original
