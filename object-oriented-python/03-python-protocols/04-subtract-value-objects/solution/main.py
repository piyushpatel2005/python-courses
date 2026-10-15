class MovementOffset:
    def __init__(self, steps):
        self.steps = steps

    def __sub__(self, other):
        if not isinstance(other, MovementOffset):
            return NotImplemented
        return MovementOffset(self.steps - other.steps)


if __name__ == "__main__":
    try:
        print("Difference:", (MovementOffset(3) - MovementOffset(8)).steps)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
