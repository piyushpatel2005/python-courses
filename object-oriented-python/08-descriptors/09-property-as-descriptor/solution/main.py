class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    try:
        rectangle = Rectangle(3, 4)
        print(rectangle.area)
        rectangle.width = 5
        print(rectangle.area)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
