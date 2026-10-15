from solution import *


def test_behavior():
    """Reject an invalid lobby size."""
    lobby = Lobby()
    for count in (3, 1, 17):
        lobby.set_slots(count)
        assert lobby.slots == count
    for count in (0, -2):
        try:
            lobby.set_slots(count)
        except ValueError as error:
            assert str(error) == "slots must be positive"
        else:
            assert False, "Reject a nonpositive slot count"
        assert lobby.slots == 17
