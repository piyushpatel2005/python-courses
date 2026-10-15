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

class Plant:
    height = Positive()
    water = Positive()

    def __init__(self, height, water):
        pass


if __name__ == "__main__":
    try:
        first, second = Plant(12, 3), Plant(20, 5)
        first.height = 14
        print(first.height, first.water, second.height, second.water)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
