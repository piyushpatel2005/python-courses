from solution import *


def test_enum_type_checks():
    from enum import Enum
    class Other(Enum):
        WAITING = "waiting"
    for value in DeliveryState:
        assert is_delivery_state(value) is True
    for value in ["waiting", 0, None, DeliveryState, Other.WAITING, object()]:
        assert is_delivery_state(value) is False
