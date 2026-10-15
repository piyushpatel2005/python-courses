class ScaledReading:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return None

class Sensor:
    reading = ScaledReading()

    def __init__(self, raw):
        self.raw = raw


if __name__ == "__main__":
    try:
        print(Sensor(3).reading, Sensor(7).reading)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
