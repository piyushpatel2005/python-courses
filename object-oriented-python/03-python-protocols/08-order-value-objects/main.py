class RaceTime:
    def __init__(self, seconds):
        self.seconds = seconds

    def __lt__(self, other):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        times = [RaceTime(64), RaceTime(59), RaceTime(62)]
        print("Sorted seconds:", [time.seconds for time in sorted(times)])
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
