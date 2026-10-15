from __future__ import annotations
from typing import Any

def copy_rows(rows: list[list[Any]]) -> list[list[Any]]:
    return [list(row) for row in rows]


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        source = [["A"], [], ["B", "C"]]
        result = copy_rows(source)
        result[0].append("D")
        print(source, result)
    except NotImplementedError as error:
        print("Not ready yet:", error)
