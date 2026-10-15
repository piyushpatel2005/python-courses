from __future__ import annotations

class TrieNode:

    def __init__(self: TrieNode) -> None:
        self.children: dict[str, TrieNode] = {}
        self.terminal: bool = False
if __name__ == '__main__':
    try:
        first, second = (TrieNode(), TrieNode())
        first.children['r'] = TrieNode()
        print('Independent:', second.children == {})
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
