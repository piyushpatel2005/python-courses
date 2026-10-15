class ScoreMultiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        large = ScoreMultiplier(12)
        small = ScoreMultiplier(3)
        print("Scores:", large(2), large(5), small(2))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
