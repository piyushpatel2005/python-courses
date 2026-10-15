from __future__ import annotations
from typing import Any

class Stack:

    def __init__(self: Stack) -> None:
        self.items: list[Any] = []

    def __len__(self: Stack) -> int:
        return len(self.items)

    def push(self: Stack, value: Any) -> None:
        self.items.append(value)
if __name__ == '__main__':
    try:
        pending = Stack()
        pending.push('draft')
        pending.push('review')
        print(pending.items, len(pending))
    except NotImplementedError as error:
        print(error)
