class Lobby:
    def __init__(self):
        self.slots = 1

    def set_slots(self, count):
        if count <= 0:
            raise ValueError("slots must be positive")
        self.slots = count


if __name__ == "__main__":
    try:
        lobby = Lobby()
        lobby.set_slots(4)
        print("Slots:", lobby.slots)
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
