class ReplayReader:
    def __init__(self):
        self.closed = False

    def read(self):
        return "entered the moss cave"

    def close(self):
        self.closed = True


def read_replay_and_close(reader):
    try:
        return reader.read()
    finally:
        reader.close()


if __name__ == "__main__":
    try:
        replay = ReplayReader()
        print(read_replay_and_close(replay))
        print("Closed:", replay.closed)
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
