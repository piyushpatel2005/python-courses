class GameItem:
    def __init__(self, uses=0):
        self.uses = uses

    def record_use(self):
        self.uses += 1
        return self.uses

def deferred_use(item):
    pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = GameItem(3)
        action = deferred_use(sample)
        print("Before action:", sample.uses)
        print("Action result:", action())
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
