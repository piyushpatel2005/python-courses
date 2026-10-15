def list_items():
    return "Available items"

def set_description(command, text):
    pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        set_description(list_items, "Show inventory")
        print("Description:", list_items.description)
        print("Command result:", list_items())
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
