from __future__ import annotations

def bucket_index(key: str, capacity: int) -> int:
    validate_capacity(capacity)
    result = 0
    for character in key:
        result = (result * 31 + ord(character)) % capacity
    return result


def validate_capacity(capacity: int) -> None:
    if type(capacity) is not int or capacity <= 0:
        raise ValueError("capacity must be a positive integer")


if __name__ == "__main__":
    try:
        print(bucket_index("rack", 7), bucket_index("", 7))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
