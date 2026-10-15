class ItemQuantityError(Exception):
    pass


def parse_item_quantity(text):
    try:
        return int(text)
    except ValueError as error:
        raise ItemQuantityError("item quantity must be an integer") from error


if __name__ == "__main__":
    try:
        print("Item quantity:", parse_item_quantity("8"))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
