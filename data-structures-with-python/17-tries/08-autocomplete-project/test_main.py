from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_suggest_limit_type():
    'Reject non-integer limits with `TypeError`.'
    expect_error(TypeError, lambda: Trie().suggest('', 1.5))
    expect_error(TypeError, lambda: Trie().suggest('', '2'))


def test_suggest_limit_range():
    'Reject negative integer limits with `ValueError`.'
    expect_error(ValueError, lambda: Trie().suggest('', -1))
    expect_error(ValueError, lambda: Trie().suggest('', -9))


def test_suggest_total():
    "Fill the tuple's first item with the full matching word count, regardless of the limit."
    trie = Trie()
    for word in ['be', 'bear', 'bell', 'belt', 'bell']:
        trie.insert(word)
    for limit in [0, 1, 10]:
        assert trie.suggest('be', limit)[0] == 4
    assert trie.suggest('x', 3)[0] == 0


def test_suggest_list():
    'Fill the second item with a fresh sorted completion list cut to the limit.'
    trie = Trie()
    for word in ['be', 'bear', 'bell', 'belt']:
        trie.insert(word)
    assert trie.suggest('be', 2)[1] == ['be', 'bear']
    assert trie.suggest('be', 0)[1] == []
    trie.delete('be')
    assert trie.suggest('be', 10)[1] == ['bear', 'bell', 'belt']
    result = trie.suggest('be', 2)[1]
    result.clear()
    assert trie.suggest('be', 2)[1] == ['bear', 'bell']
