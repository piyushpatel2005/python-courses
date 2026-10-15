class Scaler:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


if __name__ == "__main__":
    try:
        large = Scaler(12)
        small = Scaler(3)
        print("Scaled:", large(2), large(5), small(2))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
