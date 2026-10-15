from solution import *


def test_behavior():
    """Name a domain error."""
    assert issubclass(LobbyFullError, Exception)
    assert join_lobby(5) == 4
    assert join_lobby(1) == 0
    for remaining in (0, -1):
        try:
            join_lobby(remaining)
        except LobbyFullError as error:
            assert str(error) == "lobby is full"
        else:
            assert False, "Raise LobbyFullError for a full lobby"
