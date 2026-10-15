class ScoreDelta:
    def __init__(self, points):
        self.points = points

    def __mul__(self, factor):
        if type(factor) is not int:
            return NotImplemented
        return ScoreDelta(self.points * factor)

    def __rmul__(self, factor):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        delta = ScoreDelta(5)
        print("Both orders:", (delta * 4).points, (4 * delta).points)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
