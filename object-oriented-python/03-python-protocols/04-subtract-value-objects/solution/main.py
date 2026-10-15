class Offset:
    def __init__(self, steps):
        self.steps = steps

    def __sub__(self, other):
        if not isinstance(other, Offset):
            return NotImplemented
        return Offset(self.steps - other.steps)


if __name__ == "__main__":
    try:
        print("Difference:", (Offset(3) - Offset(8)).steps)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
