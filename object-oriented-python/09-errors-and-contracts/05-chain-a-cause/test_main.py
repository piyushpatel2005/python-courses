from solution import *


def test_behavior():
    """Preserve the cause of a failure."""
    for text, value in (("12", 12), (" 0 ", 0), ("-3", -3)):
        assert parse_quantity(text) == value
    for text in ("many", "2.5", ""):
        try:
            parse_quantity(text)
        except QuantityError as error:
            assert str(error) == "quantity must be an integer"
            assert isinstance(error.__cause__, ValueError)
        else:
            assert False, "Wrap invalid integer text"
    try:
        parse_quantity([])
    except TypeError:
        pass
    else:
        assert False, "Preserve TypeError"
