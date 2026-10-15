class GameItem:
    def __init__(self, name):
        self.name = name
        # Create independent notes here.

    def add_note(self, text):
        self.notes.append(text)


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        first, second = GameItem("lantern"), GameItem("shield")
        first.add_note("glow checked")
        print("Lantern notes:", first.notes)
        print("Shield notes:", second.notes)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
