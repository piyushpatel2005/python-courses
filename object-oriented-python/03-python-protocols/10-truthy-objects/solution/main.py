class Stamina:
    def __init__(self, points, enabled=True):
        self.points = points
        self.enabled = bool(enabled)

    def __bool__(self):
        return self.enabled and self.points > 0


if __name__ == "__main__":
    try:
        print("Ready:", bool(Stamina(8)))
        print("Switched off:", bool(Stamina(8, False)))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
