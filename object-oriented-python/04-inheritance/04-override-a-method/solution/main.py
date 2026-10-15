class Beacon:
    def __init__(self, location):
        self.location = location

    def signal(self):
        return f"Sound at {self.location}"

class LightBeacon(Beacon):
    def signal(self):
        return f"Light at {self.location}"


if __name__ == "__main__":
    try:
        print(Beacon("door").signal())
        print(LightBeacon("door").signal())
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
