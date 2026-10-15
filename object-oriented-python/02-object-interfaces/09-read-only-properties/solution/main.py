class Tool:
    def __init__(self, asset_code, name):
        self._asset_code = asset_code
        self.name = name

    @property
    def asset_code(self):
        return self._asset_code


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        sample = Tool("A-7", "drill")
        print("Asset code:", sample.asset_code)
        try:
            sample.asset_code = "replacement"
        except AttributeError:
            print("Public reassignment rejected")
        else:
            print("Public reassignment was allowed; add a getter-only property")
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
