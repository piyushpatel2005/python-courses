def list_tools():
    return "Available tools"

def set_description(command, text):
    pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        set_description(list_tools, "Show workshop stock")
        print("Description:", list_tools.description)
        print("Command result:", list_tools())
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
