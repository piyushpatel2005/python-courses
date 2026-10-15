from enum import Enum

class Shipping(Enum):
    GROUND = 3
    AIR = 8

    def cost(self, boxes):
        return None


if __name__ == "__main__":
    try:
        print(Shipping.GROUND.cost(4), Shipping.AIR.cost(2))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
