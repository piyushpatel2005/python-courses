from solution import *


def test_named_statuses():
    from enum import Enum
    assert issubclass(TicketState, Enum)
    assert list(TicketState.__members__) == ["NEW", "DONE"]
    assert TicketState.NEW.value == "new"
    assert TicketState.DONE.value == "done"
    assert TicketState.NEW is not TicketState.DONE
