class Tool:
    pass

def make_tool(uses):
    tool = Tool()
    tool.uses = uses
    return tool

def record_uses(tool, amount):
    tool.uses += amount


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = make_tool(3)
        record_uses(sample, 2)
        record_uses(sample, 4)
        print("Recorded uses:", sample.uses)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
