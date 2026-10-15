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
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        result: list[str] = []

        def visit(node: TrieNode, word: str) -> None:
            if node.terminal:
                result.append(word)
            for char in sorted(node.children):
                visit(node.children[char], word + char)
        visit(node, prefix)
        return result

    def delete(self: Trie, word: str) -> bool:
        node = self.root
        trail: list[tuple[TrieNode, str]] = []
        for char in word:
            if char not in node.children:
                return False
            trail.append((node, char))
            node = node.children[char]
        if not node.terminal:
            return False
        node.terminal = False
        for parent, char in reversed(trail):
            child = parent.children[char]
            if child.terminal or child.children:
                break
            del parent.children[char]
        return True

    def count_prefix(self: Trie, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        stack: list[TrieNode] = [node]
        count = 0
        while stack:
            node = stack.pop()
            count += int(node.terminal)
            stack.extend(node.children.values())
        return count

    def suggest(self: Trie, prefix: str, limit: int) -> tuple[int, list[str]]:
        pass  # TODO: check limit type
        pass  # TODO: check limit range
        return (None, None)
if __name__ == '__main__':
    try:
        index = Trie()
        for word in ['reed', 'reeds', 'reef']:
            index.insert(word)
        print('Report:', index.suggest('ree', 2))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
