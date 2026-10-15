class GameItem:
    pass

def make_item(uses):
    item = GameItem()
    item.uses = uses
    return item

def record_uses(item, amount):
    pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = make_item(3)
        record_uses(sample, 2)
        record_uses(sample, 4)
        print("Recorded uses:", sample.uses)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
