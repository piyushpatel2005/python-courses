class Tool:
    def record_use(self):
        self.uses += 1

def make_tool(uses):
    tool = Tool()
    tool.uses = uses
    return tool


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = make_tool(5)
        sample.record_use()
        sample.record_use()
        print("Uses after two calls:", sample.uses)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
