class Document:
    pass

class Signed(Document):
    pass

class Dated(Document):
    pass

class Report(Signed, Dated):
    pass


def mro_names(cls):
    pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print("Direct bases:", [base.__name__ for base in Report.__bases__])
        print("Full order:", mro_names(Report))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
