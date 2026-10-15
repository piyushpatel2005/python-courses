class Hitbox:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    try:
        hitbox = Hitbox(3, 4)
        print(hitbox.area)
        hitbox.width = 5
        print(hitbox.area)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
