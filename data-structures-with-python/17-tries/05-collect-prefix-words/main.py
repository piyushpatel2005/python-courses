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
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.terminal

    def starts_with(self: Trie, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def collect(self: Trie, prefix: str) -> list[str]:
        node = self.root
        raise NotImplementedError('Locate the prefix first')
        result: list[str] = []

        def visit(node: TrieNode, word: str) -> None:
            pass  # TODO: append this spelling if the node ends a word
            pass  # TODO: visit child edges in sorted order
        visit(node, prefix)
        return result
if __name__ == '__main__':
    try:
        index = Trie()
        for word in ['reef', 'reed', 'red']:
            index.insert(word)
        print('Suggestions:', index.collect('ree'))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
