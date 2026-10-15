class GameItem:
    def __init__(self, cooldown_turns):
        self.cooldown_turns = cooldown_turns

    @property
    def cooldown_turns(self):
        return self._cooldown_turns

    @cooldown_turns.setter
    def cooldown_turns(self, value):
        if value <= 0:
            raise ValueError("cooldown_turns must be positive")
        self._cooldown_turns = value


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = GameItem(7)
        sample.cooldown_turns = 14
        print("Accepted cooldown:", sample.cooldown_turns)
        try:
            sample.cooldown_turns = 0
        except ValueError:
            print("Invalid cooldown rejected")
        print("Cooldown after rejection:", sample.cooldown_turns)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
