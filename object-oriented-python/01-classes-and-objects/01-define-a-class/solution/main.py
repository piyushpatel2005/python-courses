class Tool:
    pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("Tool instance:", isinstance(Tool(), Tool))
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
