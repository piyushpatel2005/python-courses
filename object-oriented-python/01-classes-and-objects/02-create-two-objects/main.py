class GameItem:
    pass

lantern = None
shield = None


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("Both items:", isinstance(lantern, GameItem) and isinstance(shield, GameItem))
        print("Separate objects:", lantern is not shield)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
