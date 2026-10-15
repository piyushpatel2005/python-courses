from solution import *


def test_asset_code_is_publicly_read_only():
    prop = vars(GameItem).get("asset_code")
    assert isinstance(prop, property) and prop.fset is None, "Expose asset_code with a getter and no setter."
    for code in ("A-7", "Z-19"):
        item = GameItem(code, "lantern")
        assert item.asset_code == code
        try:
            item.asset_code = "replacement"
        except AttributeError:
            pass
        else:
            assert False, "Assignment to the read-only property must raise AttributeError."
        assert item.asset_code == code
        item.name = "shield"
        assert item.name == "shield" and item.asset_code == code
