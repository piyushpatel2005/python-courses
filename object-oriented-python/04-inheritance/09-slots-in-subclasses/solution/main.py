class Waypoint:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

class NamedWaypoint(Waypoint):
    __slots__ = ("label",)

    def __init__(self, x, y, label):
        super().__init__(x, y)
        self.label = label


if __name__ == "__main__":
    try:
        point = NamedWaypoint(4, 7, "gate")
        print(point.x, point.y, point.label)
        try:
            point.note = "extra"
            print("Extra attribute accepted; add subclass slots.")
        except AttributeError:
            print("Subclass layout remains restricted.")
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
