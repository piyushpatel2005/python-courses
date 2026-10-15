class SoldOutError(Exception):
    pass


def reserve(remaining):
    if remaining <= 0:
        raise SoldOutError("workshop is full")
    return remaining - 1


if __name__ == "__main__":
    try:
        reserve(0)
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
