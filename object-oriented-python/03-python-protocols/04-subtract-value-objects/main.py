class MovementOffset:
    def __init__(self, steps):
        self.steps = steps

    def __sub__(self, other):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print("Difference:", (MovementOffset(3) - MovementOffset(8)).steps)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
