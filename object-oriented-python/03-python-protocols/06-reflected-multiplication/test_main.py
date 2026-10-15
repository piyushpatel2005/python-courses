from solution import *


def test_01_reflected_multiplication():
    for count, factor in ((5, 4), (9, 0), (3, -2)):
        pack = TokenPack(count)
        result = factor * pack
        assert isinstance(result, TokenPack)
        assert result.count == (pack * factor).count == count * factor
        assert result is not pack and pack.count == count
    for bad in (True, 2.5, "3"):
        assert TokenPack(4).__rmul__(bad) is NotImplemented
    calls = []
    original = TokenPack.__mul__
    try:
        def sentinel(self, factor):
            calls.append((self, factor))
            return "delegated"
        TokenPack.__mul__ = sentinel
        item = TokenPack(7)
        assert item.__rmul__(6) == "delegated", "Delegate rather than duplicate __mul__."
        assert calls == [(item, 6)]
    finally:
        TokenPack.__mul__ = original
