from __future__ import annotations

class TrieNode:

    def __init__(self: TrieNode) -> None:
        self.children: dict[str, TrieNode] = {}
        self.terminal: bool = False

class Trie:

    def __init__(self: Trie) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self: Trie, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.terminal = True
if __name__ == '__main__':
    try:
        index = Trie()
        index.insert('reed')
        index.insert('reef')
        print('Root edges:', sorted(index.root.children))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
