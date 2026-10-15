from solution import *


def test_01_developer_repr():
    for code, count in (("X", 2), ("A'B", 0), ('row\nnext', 11)):
        item = Parcel(code, count)
        expected = f"Parcel(code={code!r}, count={count!r})"
        assert repr(item) == expected, "Include both named fields with their representations."
        assert repr([item]) == '[' + expected + ']'
        assert (item.code, item.count) == (code, count)
