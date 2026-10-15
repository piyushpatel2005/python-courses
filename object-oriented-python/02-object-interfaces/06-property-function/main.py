class GameItem:
    def __init__(self, name):
        self.name = name

    def get_label(self):
        return self.name.upper()

    # Connect label to get_label here.


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = GameItem("lantern")
        print("Label:", sample.label)
        sample.name = "shield"
        print("Updated label:", sample.label)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
