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

    def contains(self: Trie, word: str) -> bool:
        node = self.root
        pass  # TODO: follow the path and reject missing edges
        return None  # TODO: finish a successful walk
if __name__ == '__main__':
    try:
        index = Trie()
        index.insert('reed')
        print('Whole words:', index.contains('ree'), index.contains('reed'))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
