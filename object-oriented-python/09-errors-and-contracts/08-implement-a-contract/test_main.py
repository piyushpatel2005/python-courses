from solution import *


def test_behavior():
    """Implement a credit fee policy."""
    for threshold, fee in ((500, 35), (120, 7), (1, 9)):
        policy = ThresholdFee(threshold, fee)
        assert isinstance(policy, CreditFeePolicy)
        for subtotal in (0, threshold - 1):
            assert policy.fee_credits(subtotal) == fee
        for subtotal in (threshold, threshold + 1):
            assert policy.fee_credits(subtotal) == 0
