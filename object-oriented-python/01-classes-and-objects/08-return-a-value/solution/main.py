class Tool:
    def summary(self):
        return f"{self.name}: {self.uses} uses"

def make_tool(name, uses):
    tool = Tool()
    tool.name = name
    tool.uses = uses
    return tool


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = make_tool("drill", 2)
        print(sample.summary())
        sample.uses = 3
        print(sample.summary())
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
