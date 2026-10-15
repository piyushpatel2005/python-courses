from solution import *


def test_behavior():
    """Build a searchable catalog."""
    a, b = Product("A", "Apron", 901), Product("B", "Bowl", 0)
    c = Catalog([b, a])
    assert c.get("A") is a
    assert c.all() == [a, b]
    assert Catalog([]).all() == []
    try:
        Catalog([a, Product("A", "Other", 1)])
    except ValueError:
        pass
    else:
        assert False, "Reject duplicate SKUs"
    try:
        c.get("missing")
    except KeyError:
        pass
    else:
        assert False, "Preserve missing-SKU lookup"
