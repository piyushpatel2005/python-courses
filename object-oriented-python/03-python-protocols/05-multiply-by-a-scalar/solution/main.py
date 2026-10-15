class ScoreDelta:
    def __init__(self, points):
        self.points = points

    def __mul__(self, factor):
        if type(factor) is not int:
            return NotImplemented
        return ScoreDelta(self.points * factor)


if __name__ == "__main__":
    try:
        print("Scaled points:", (ScoreDelta(7) * 3).points)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
