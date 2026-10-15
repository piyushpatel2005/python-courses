class GameItem:
    # Add normalize_code here.
    pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("Normalized code:", GameItem.normalize_code("  ab-7  "))
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
