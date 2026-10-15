class GameItem:
    # Add record_use here.
    pass

def make_item(uses):
    item = GameItem()
    item.uses = uses
    return item


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = make_item(5)
        sample.record_use()
        sample.record_use()
        print("Uses after two calls:", sample.uses)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
