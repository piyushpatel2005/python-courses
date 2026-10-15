class Reader:
    def __init__(self):
        self.closed = False

    def read(self):
        return "chapter one"

    def close(self):
        self.closed = True


def read_and_close(reader):
    pass


if __name__ == "__main__":
    try:
        r = Reader()
        print(read_and_close(r))
        print("Closed:", r.closed)
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
