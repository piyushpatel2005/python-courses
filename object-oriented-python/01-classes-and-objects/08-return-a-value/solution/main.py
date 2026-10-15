class GameItem:
    def summary(self):
        return f"{self.name}: {self.uses} uses"

def make_item(name, uses):
    item = GameItem()
    item.name = name
    item.uses = uses
    return item


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = make_item("lantern", 2)
        print(sample.summary())
        sample.uses = 3
        print(sample.summary())
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
