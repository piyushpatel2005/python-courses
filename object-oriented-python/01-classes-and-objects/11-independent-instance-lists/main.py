class Tool:
    def __init__(self, name):
        self.name = name
        # Create independent notes here.

    def add_note(self, text):
        self.notes.append(text)


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        first, second = Tool("drill"), Tool("saw")
        first.add_note("battery checked")
        print("Drill notes:", first.notes)
        print("Saw notes:", second.notes)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
