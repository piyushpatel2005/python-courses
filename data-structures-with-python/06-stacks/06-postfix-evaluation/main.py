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

def postfix(tokens: list[str]) -> int:
    operands = Stack()
    for token in tokens:
        if token in ('+', '-', '*'):
            # TODO 2: require two operands; pop right, then left;
            # compute the supported operation and push its result.
            pass
        else:
            # TODO 1: parse an integer token or raise ValueError;
            # push the parsed number on operands.
            pass
    # TODO 3: require exactly one result, then pop and return it.
    return 0  # placeholder result until task 3
if __name__ == '__main__':
    try:
        print(postfix(['7', '2', '-', '3', '*']))
    except NotImplementedError as error:
        print(error)
