class Record:
    pass

class DetailedRecord(Record):
    pass


def direct_object_base(value):
    pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print("Plain:", direct_object_base(Record()))
        print("Subclass:", direct_object_base(DetailedRecord()))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
