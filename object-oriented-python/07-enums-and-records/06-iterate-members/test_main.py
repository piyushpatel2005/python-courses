from solution import *


def test_iterate_members():
    from enum import Enum
    assert member_rows(Theme) == [("LIGHT", "light"), ("DARK", "dark")]
    class Size(Enum):
        LARGE = 8
        SMALL = 2
        TINY = 2
    assert member_rows(Size) == [("LARGE", 8), ("SMALL", 2)]
    class Empty(Enum):
        pass
    assert member_rows(Empty) == []
