from solution import *


def test_behavior():
    """Implement a delivery policy."""
    for threshold, fee in ((5000, 350), (1200, 75), (1, 9)):
        policy = ThresholdDelivery(threshold, fee)
        assert isinstance(policy, DeliveryPolicy)
        for subtotal in (0, threshold - 1):
            assert policy.fee_cents(subtotal) == fee
        for subtotal in (threshold, threshold + 1):
            assert policy.fee_cents(subtotal) == 0
