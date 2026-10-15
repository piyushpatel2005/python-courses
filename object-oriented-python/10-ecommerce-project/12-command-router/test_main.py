from solution import *


def test_behavior():
    """Route shop commands."""
    shop = Shop(Catalog([Product("B", "Bowl", 299), Product("A", "Apron", 101)]))
    assert shop.execute(" products ") == "A | Apron | $1.01\nB | Bowl | $2.99"
    assert shop.execute("orders") == "No orders"
    assert shop.execute("add B 2") == "Added B x 2"
    assert shop.execute("cart") == "B | Bowl | 2 x | $5.98\nCart total: $5.98"
    assert shop.execute("remove B") == "Removed B"
    assert shop.execute("remove B") == "Not in cart: B"
    shop.execute("add A 3")
    assert shop.execute("checkout") == "Created O1"
    assert shop.execute("orders") == "O1"
    assert shop.execute("track O1") == "O1: placed"
    assert shop.execute("status O1 shipped") == "O1: shipped"
    assert shop.execute("show O1") == "Order O1\nA | Apron | 3 x | $3.03\nTotal: $3.03"
    assert shop.execute("cart") == "Cart total: $0.00"
    for command in ("", "unknown", "add A", "cart extra", "track", "status O1", "add A 2 extra"):
        try:
            shop.execute(command)
        except ValueError as error:
            assert str(error) == "invalid command"
        else:
            assert False, "Reject malformed command: " + command
    try:
        shop.execute("add A two")
    except ValueError:
        pass
    else:
        assert False, "Convert quantity text"
