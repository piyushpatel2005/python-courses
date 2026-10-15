class GameItem:
    pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("Class cooldown:", GameItem.cooldown_turns)
        print("Instance cooldown:", GameItem().cooldown_turns)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
