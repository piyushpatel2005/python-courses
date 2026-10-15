class ItemPool:
    def __init__(self, total, equipped):
        self.total = total
        self.equipped = equipped

    @property
    def available(self):
        return self.total - self.equipped


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = ItemPool(10, 3)
        print("Available:", sample.available)
        sample.equipped = 6
        print("After equipping more:", sample.available)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
