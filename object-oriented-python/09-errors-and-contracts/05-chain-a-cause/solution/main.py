class QuantityError(Exception):
    pass


def parse_quantity(text):
    try:
        return int(text)
    except ValueError as error:
        raise QuantityError("quantity must be an integer") from error


if __name__ == "__main__":
    try:
        print("Quantity:", parse_quantity("8"))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
