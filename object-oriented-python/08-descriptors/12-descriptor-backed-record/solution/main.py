class Positive:
    def __set_name__(self, owner, name):
        self.key = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.key)

    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError("Use a built-in number")
        if value <= 0:
            raise ValueError("Value must be positive")
        instance.__dict__[self.key] = value

class CharacterStats:
    max_health = Positive()
    max_mana = Positive()

    def __init__(self, max_health, max_mana):
        self.max_health = max_health
        self.max_mana = max_mana


if __name__ == "__main__":
    try:
        first, second = CharacterStats(12, 3), CharacterStats(20, 5)
        first.max_health = 14
        print(first.max_health, first.max_mana, second.max_health, second.max_mana)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
