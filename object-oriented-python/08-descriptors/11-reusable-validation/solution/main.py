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

class Hitbox:
    width = Positive()
    height = Positive()


if __name__ == "__main__":
    try:
        hitbox = Hitbox()
        hitbox.width, hitbox.height = 2.5, 30
        print(hitbox.width, hitbox.height)
        try:
            hitbox.width = 0
        except ValueError:
            print("Rejected:", hitbox.width)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
