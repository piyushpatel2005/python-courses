from solution import *


def test_01_introduce_slots():
    assert set(GridPoint.__slots__) == {"row", "column"}, "Declare only the two coordinate slots."
    for row, column in ((2, 5), (0, 0), (-1, 8)):
        point = GridPoint(row, column)
        assert (point.row, point.column) == (row, column)
        assert not hasattr(point, "__dict__")
        point.row, point.column = column, row
        assert (point.row, point.column) == (column, row)
        try:
            point.extra = 4
        except AttributeError:
            pass
        else:
            assert False, "Slots should reject unrelated attributes."
