class Distance:
    def __init__(self, metres):
        self.metres = metres

    def __format__(self, spec):
        if spec in ("", "short"):
            return f"{self.metres} m"
        if spec == "long":
            return f"{self.metres} metres"
        raise ValueError(f"Unknown distance format: {spec}")


if __name__ == "__main__":
    try:
        distance = Distance(18)
        print(f"Compact: {distance:short}")
        print(f"Expanded: {distance:long}")
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
