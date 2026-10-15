from enum import Enum

class DeliveryState(Enum):
    WAITING = "waiting"
    DELIVERED = "delivered"

def is_delivery_state(value):
    return None


if __name__ == "__main__":
    try:
        print(is_delivery_state(DeliveryState.WAITING), is_delivery_state("waiting"))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
