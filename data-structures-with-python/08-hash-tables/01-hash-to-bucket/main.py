from __future__ import annotations

def bucket_index(key: str, capacity: int) -> int:
    # TODO: complete the numbered steps for this function.
    return None


def validate_capacity(capacity: int) -> None:
    # TODO: complete the numbered steps for this function.
    pass


if __name__ == "__main__":
    try:
        print(bucket_index("rack", 7), bucket_index("", 7))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
