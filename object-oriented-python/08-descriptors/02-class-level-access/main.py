class FieldLabel:
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        if instance is None:
            return None
        return self.label

class PlayerSave:
    heading = FieldLabel("Player save")


if __name__ == "__main__":
    try:
        print(PlayerSave.heading is PlayerSave.__dict__["heading"], PlayerSave().heading)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
