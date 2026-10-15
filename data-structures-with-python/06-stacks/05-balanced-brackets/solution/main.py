from __future__ import annotations
from typing import Any

class Stack:

    def __init__(self: Stack) -> None:
        self.items: list[Any] = []

    def __len__(self: Stack) -> int:
        return len(self.items)

    def push(self: Stack, value: Any) -> None:
        self.items.append(value)

    def peek(self: Stack) -> Any:
        if not self.items:
            raise IndexError('Empty stack')
        return self.items[-1]

    def pop(self: Stack) -> Any:
        if not self.items:
            raise IndexError('Empty stack')
        return self.items.pop()

def balanced(text: str) -> bool:
    openings = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for character in text:
        if character in '([{':
            openings.push(character)
        elif character in pairs:
            if len(openings) == 0 or openings.pop() != pairs[character]:
                return False
    return len(openings) == 0
if __name__ == '__main__':
    try:
        print(balanced('{note[2]}'))
        print(balanced('([)]'))
    except NotImplementedError as error:
        print(error)
