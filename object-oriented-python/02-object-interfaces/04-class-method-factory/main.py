class GameItem:
    def __init__(self, name, uses):
        self.name = name
        self.uses = uses

    # Add the class method here.


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = GameItem.from_text("lantern:8")
        print("Parsed record:", sample.name, sample.uses)
        print("Integer count:", isinstance(sample.uses, int))
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
