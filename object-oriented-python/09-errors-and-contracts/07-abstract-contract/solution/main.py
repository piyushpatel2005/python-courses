from abc import ABC, abstractmethod


class DeliveryPolicy(ABC):
    @abstractmethod
    def fee_cents(self, subtotal_cents):
        pass


if __name__ == "__main__":
    try:
        print("Created:", type(DeliveryPolicy()).__name__)
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
