class TrailDistance:
    def __init__(self, metres):
        self.metres = metres

    def __format__(self, spec):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        distance = TrailDistance(18)
        print(f"Compact: {distance:short}")
        print(f"Expanded: {distance:long}")
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
