class FieldLabel:
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.label

class Record:
    heading = FieldLabel("Record heading")


if __name__ == "__main__":
    try:
        print(Record.heading is Record.__dict__["heading"], Record().heading)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
