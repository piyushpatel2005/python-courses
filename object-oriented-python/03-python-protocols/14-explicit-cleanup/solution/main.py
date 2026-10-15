class GameSession:
    def __init__(self, name, events):
        self.name = name
        self.events = events
        self.closed = False

    def close(self):
        if not self.closed:
            self.closed = True
            self.events.append(f"closed:{self.name}")

    def __del__(self):
        self.close()


if __name__ == "__main__":
    try:
        events = []
        session = GameSession("preview", events)
        session.__del__()  # Explicit hook demonstration, not GC timing.
        print("After explicit hook:", session.closed, events)
        session.close()
        print("After explicit close:", events)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
