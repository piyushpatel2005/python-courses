class Alarm:
    def __init__(self, location):
        self.location = location

    def signal(self):
        return f"Sound at {self.location}"

class QuietAlarm(Alarm):
    def signal(self):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print(Alarm("door").signal())
        print(QuietAlarm("door").signal())
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
