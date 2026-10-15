class Record:
    pass

class DetailedRecord(Record):
    pass


def direct_object_base(value):
    return object in type(value).__bases__


if __name__ == "__main__":
    try:
        print("Plain:", direct_object_base(Record()))
        print("Subclass:", direct_object_base(DetailedRecord()))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
