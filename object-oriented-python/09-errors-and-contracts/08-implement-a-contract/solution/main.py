from abc import ABC, abstractmethod


class DeliveryPolicy(ABC):
    @abstractmethod
    def fee_cents(self, subtotal_cents):
        pass


class ThresholdDelivery(DeliveryPolicy):
    def __init__(self, threshold_cents, flat_cents):
        self.threshold_cents = threshold_cents
        self.flat_cents = flat_cents

    def fee_cents(self, subtotal_cents):
        if subtotal_cents >= self.threshold_cents:
            return 0
        return self.flat_cents


if __name__ == "__main__":
    try:
        policy = ThresholdDelivery(5000, 350)
        print("Delivery:", policy.fee_cents(5000))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
