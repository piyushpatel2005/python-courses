# Define GameItem here.


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("GameItem instance:", isinstance(GameItem(), GameItem))
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
