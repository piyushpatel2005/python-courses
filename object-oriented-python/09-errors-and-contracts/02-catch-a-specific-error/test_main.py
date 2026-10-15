from solution import *


def test_behavior():
    """Catch only the expected lookup error."""
    assert player_label({2: "Wren", 8: "Ash"}, 8) == "Ash"
    assert player_label({}, 8) == "Unknown player"
    assert player_label({1: ""}, 1) == ""
    class Broken:
        def __getitem__(self, key):
            raise RuntimeError("player directory unavailable")
    try:
        player_label(Broken(), 3)
    except RuntimeError:
        pass
    else:
        assert False, "Do not catch unrelated exceptions"
