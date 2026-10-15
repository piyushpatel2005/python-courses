from enum import Enum

class Ability(Enum):
    DASH = 3
    HEAL = 8

    def cost(self, casts):
        return self.value * casts


if __name__ == "__main__":
    try:
        print(Ability.DASH.cost(4), Ability.HEAL.cost(2))
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
