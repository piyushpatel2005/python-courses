class ScaledPower:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.base_power * 10

class CharacterStats:
    power = ScaledPower()

    def __init__(self, base_power):
        self.base_power = base_power


if __name__ == "__main__":
    try:
        print(CharacterStats(3).power, CharacterStats(7).power)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
