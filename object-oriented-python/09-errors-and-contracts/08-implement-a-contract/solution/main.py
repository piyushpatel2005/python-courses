from abc import ABC, abstractmethod


class CreditFeePolicy(ABC):
    @abstractmethod
    def fee_credits(self, subtotal_credits):
        pass


class ThresholdFee(CreditFeePolicy):
    def __init__(self, threshold_credits, flat_credits):
        self.threshold_credits = threshold_credits
        self.flat_credits = flat_credits

    def fee_credits(self, subtotal_credits):
        if subtotal_credits >= self.threshold_credits:
            return 0
        return self.flat_credits


if __name__ == "__main__":
    try:
        policy = ThresholdFee(500, 35)
        print("Fee (credits):", policy.fee_credits(500))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
