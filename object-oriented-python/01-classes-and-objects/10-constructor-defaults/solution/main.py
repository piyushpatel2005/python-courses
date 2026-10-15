class GameItem:
    def __init__(self, name, uses=0):
        self.name = name
        self.uses = uses


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("New item uses:", GameItem("lantern").uses)
        print("Imported item uses:", GameItem("shield", uses=6).uses)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
