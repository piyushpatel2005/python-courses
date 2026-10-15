class Tool:
    pass

def make_tool(name):
    tool = Tool()
    tool.name = name
    return tool


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("Tool names:", make_tool("drill").name, make_tool("saw").name)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
