from abc import ABC, abstractmethod


class CreditFeePolicy(ABC):
    @abstractmethod
    def fee_credits(self, subtotal_credits):
        pass


if __name__ == "__main__":
    try:
        print("Created:", type(CreditFeePolicy()).__name__)
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
