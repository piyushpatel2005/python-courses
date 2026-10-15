from solution import *


def test_01_sized_objects():
    for titles in ([], ["A"], ["A", "B", "C", "D"]):
        cart = LibraryCart(titles)
        assert len(cart) == len(titles), "Count the current contained list."
        cart.titles.append("new")
        assert len(cart) == len(titles) + 1
        cart.titles.clear()
        assert len(cart) == 0
    assert not LibraryCart([])
    assert bool(LibraryCart(["book"]))
