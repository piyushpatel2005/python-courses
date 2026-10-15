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
            if len(operands) < 2:
                raise ValueError('Operator needs two operands')
            right = operands.pop()
            left = operands.pop()
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            else:
                result = left * right
            operands.push(result)
        else:
            try:
                number = int(token)
            except (ValueError, TypeError):
                raise ValueError('Invalid integer token') from None
            operands.push(number)
    if len(operands) != 1:
        raise ValueError('Expression must leave one result')
    return operands.pop()

class UndoHistory:

    def __init__(self: UndoHistory, text: str='') -> None:
        self.text: str = text
        self.previous: Stack = Stack()

    def replace(self: UndoHistory, text: str) -> None:
        self.previous.push(self.text)
        self.text = text

    def undo(self: UndoHistory) -> bool:
        raise NotImplementedError('Complete UndoHistory.undo')
if __name__ == '__main__':
    try:
        document = UndoHistory('draft')
        document.replace('revised')
        document.replace('ready')
        print(document.undo(), document.text)
    except NotImplementedError as error:
        print(error)
