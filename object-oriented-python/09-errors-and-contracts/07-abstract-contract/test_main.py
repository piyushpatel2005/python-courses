from solution import *


def test_behavior():
    """Declare an abstract contract."""
    from abc import ABC
    assert issubclass(DeliveryPolicy, ABC)
    assert "fee_cents" in DeliveryPolicy.__abstractmethods__
    class Incomplete(DeliveryPolicy):
        pass
    for cls in (DeliveryPolicy, Incomplete):
        try:
            cls()
        except TypeError:
            pass
        else:
            assert False, "An unfinished policy must be abstract"
    class Complete(DeliveryPolicy):
        def fee_cents(self, subtotal_cents):
            return 3
    assert Complete().fee_cents(50) == 3
