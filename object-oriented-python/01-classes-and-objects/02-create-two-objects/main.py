class Tool:
    pass

drill = None
saw = None


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("Both tools:", isinstance(drill, Tool) and isinstance(saw, Tool))
        print("Separate objects:", drill is not saw)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
