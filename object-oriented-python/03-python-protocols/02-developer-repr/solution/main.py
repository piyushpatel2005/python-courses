class Parcel:
    def __init__(self, code, count):
        self.code = code
        self.count = count

    def __repr__(self):
        return f"Parcel(code={self.code!r}, count={self.count!r})"


if __name__ == "__main__":
    try:
        print(repr(Parcel("A'7", 3)))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
