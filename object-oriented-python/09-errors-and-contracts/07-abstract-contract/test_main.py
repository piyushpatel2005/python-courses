from solution import *


def test_behavior():
    """Declare an abstract contract."""
    from abc import ABC
    assert issubclass(CreditFeePolicy, ABC)
    assert "fee_credits" in CreditFeePolicy.__abstractmethods__
    class Incomplete(CreditFeePolicy):
        pass
    for cls in (CreditFeePolicy, Incomplete):
        try:
            cls()
        except TypeError:
            pass
        else:
            assert False, "An unfinished policy must be abstract"
    class Complete(CreditFeePolicy):
        def fee_credits(self, subtotal_credits):
            return 3
    assert Complete().fee_credits(50) == 3
