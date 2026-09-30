from solution import tag_name
import inspect

def test_package_call():
    """The package module parses the new tag"""
    assert tag_name("<lamp />") == "lamp"
    assert "<lamp />" in inspect.getsource(__import__("solution"))
