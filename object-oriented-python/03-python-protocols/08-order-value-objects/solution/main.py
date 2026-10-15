class TrailTime:
    def __init__(self, seconds):
        self.seconds = seconds

    def __lt__(self, other):
        if not isinstance(other, TrailTime):
            return NotImplemented
        return self.seconds < other.seconds


if __name__ == "__main__":
    try:
        times = [TrailTime(64), TrailTime(59), TrailTime(62)]
        print("Sorted seconds:", [time.seconds for time in sorted(times)])
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
