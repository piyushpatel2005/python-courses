from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_find_count_prefix():
    'Follow the prefix and return zero when its path is missing.'
    trie = Trie()
    trie.insert('goal')
    for prefix in ['x', 'gz', 'goals']:
        assert trie.count_prefix(prefix) == 0


def test_count_current_node():
    'Count one for a terminal node popped from the stack, and zero otherwise.'
    trie = Trie()
    trie.insert('go')
    assert trie.count_prefix('go') == 1
    assert Trie().count_prefix('') == 0


def test_count_terminal_nodes():
    'Add the popped node\'s children to the stack so every descendant is visited.'
    trie = Trie()
    words = {'', 'go', 'goal', 'goat', 'gum'}
    for word in list(words) + ['go']:
        trie.insert(word)
    def forbidden(prefix):
        raise AssertionError('Count nodes without collecting')
    trie.collect = forbidden
    for prefix in ['', 'g', 'go', 'goal']:
        assert trie.count_prefix(prefix) == sum(w.startswith(prefix) for w in words)
    trie.delete('go')
    assert trie.count_prefix('go') == 2
    assert Trie().count_prefix('') == 0
