from __future__ import annotations
from typing import Any

class Stack:

    def __init__(self: Stack) -> None:
        raise NotImplementedError('Complete Stack.__init__')

    def __len__(self: Stack) -> int:
        return len(self.items)
if __name__ == '__main__':
    try:
        first = Stack()
        second = Stack()
        print(first.items, len(first), first.items is second.items)
    except NotImplementedError as error:
        print(error)
