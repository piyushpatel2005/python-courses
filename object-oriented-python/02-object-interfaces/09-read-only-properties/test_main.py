from solution import *


def test_asset_code_is_publicly_read_only():
    prop = vars(Tool).get("asset_code")
    assert isinstance(prop, property) and prop.fset is None, "Expose asset_code with a getter and no setter."
    for code in ("A-7", "Z-19"):
        tool = Tool(code, "drill")
        assert tool.asset_code == code
        try:
            tool.asset_code = "replacement"
        except AttributeError:
            pass
        else:
            assert False, "Assignment to the read-only property must raise AttributeError."
        assert tool.asset_code == code
        tool.name = "saw"
        assert tool.name == "saw" and tool.asset_code == code
