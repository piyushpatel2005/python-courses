from solution import *


def test_word_length_base_case():
    assert word_complete((), 0) is True
    assert word_complete((1,), 2) is False
    assert word_complete((1, 1), 2) is True
    assert word_complete((1, 1, 1), 2) is False


def test_extend_word_without_mutation():
    old = ("up",)
    assert extend_word(old, "up") == ("up", "up")
    assert extend_word(old, "down") == ("up", "down") and old == ("up",)
    assert extend_word((), 3) == (3,)
