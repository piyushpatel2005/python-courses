class GameItem:
    def __init__(self, name):
        self.name = name

class Player:
    def __init__(self, name):
        self.name = name

def create_record(factory, name):
    pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("GameItem:", create_record(GameItem, "lantern").name)
        print("Player:", create_record(Player, "Ari").name)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
