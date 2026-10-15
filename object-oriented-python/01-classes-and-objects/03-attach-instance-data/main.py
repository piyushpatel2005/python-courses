class GameItem:
    pass

def make_item(name):
    item = GameItem()
    # Attach name here.
    return item


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("GameItem names:", make_item("lantern").name, make_item("shield").name)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
