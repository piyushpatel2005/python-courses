from solution import *


def test_behavior():
    """Reject an invalid reservation."""
    r = Reservation()
    for count in (3, 1, 17):
        r.set_seats(count)
        assert r.seats == count
    for count in (0, -2):
        try:
            r.set_seats(count)
        except ValueError as error:
            assert str(error) == "seats must be positive"
        else:
            assert False, "Reject a nonpositive seat count"
        assert r.seats == 17
