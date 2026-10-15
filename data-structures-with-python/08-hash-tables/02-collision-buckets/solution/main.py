from __future__ import annotations

def bucket_index(key: str, capacity: int) -> int:
    validate_capacity(capacity)
    result = 0
    for character in key:
        result = (result * 31 + ord(character)) % capacity
    return result


def collision_buckets(keys: list[str], capacity: int) -> list[list[str]]:
    buckets = empty_buckets(capacity)
    for key in keys:
        buckets[bucket_index(key, capacity)].append(key)
    return buckets


def validate_capacity(capacity: int) -> None:
    if type(capacity) is not int or capacity <= 0:
        raise ValueError("capacity must be a positive integer")


def empty_buckets(capacity: int) -> list[list[str]]:
    validate_capacity(capacity)
    return [[] for _ in range(capacity)]


if __name__ == "__main__":
    try:
        print(collision_buckets(["red", "blue", "red"], 3))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
