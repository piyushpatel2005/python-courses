from __future__ import annotations

class TrieNode:

    def __init__(self: TrieNode) -> None:
        self.children: dict[str, TrieNode] = None  # TODO: allocate children
        self.terminal: bool = None  # TODO: initialize the marker
if __name__ == '__main__':
    try:
        first, second = (TrieNode(), TrieNode())
        first.children['r'] = TrieNode()
        print('Independent:', second.children == {})
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
