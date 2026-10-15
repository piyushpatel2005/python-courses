class MovementOffset:
    def __init__(self, steps):
        self.steps = steps

    def __add__(self, other):
        if not isinstance(other, MovementOffset):
            return NotImplemented
        return MovementOffset(self.steps + other.steps)


if __name__ == "__main__":
    try:
        print("Combined steps:", (MovementOffset(4) + MovementOffset(6)).steps)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
