import ast
import inspect
import solution
from solution import is_atlas

def test_package_import():
    tree = ast.parse(inspect.getsource(solution))
    assert any(
        isinstance(node, ast.Import)
        and any(alias.name == "xml.etree.ElementTree" and alias.asname == "ET"
                for alias in node.names)
        for node in tree.body
    ), "Import xml.etree.ElementTree as ET."

def test_is_atlas():
    assert is_atlas("<atlas><beacon /></atlas>") is True
    assert is_atlas("<beacon><atlas /></beacon>") is False
    assert is_atlas("<atlas />") is True
    original = solution.ET.fromstring
    calls = []
    def tracked(xml_text):
        calls.append(xml_text)
        return original(xml_text)
    try:
        solution.ET.fromstring = tracked
        assert is_atlas("<other />") is False
        assert calls == ["<other />"], "Parse the supplied XML with ET.fromstring."
    finally:
        solution.ET.fromstring = original
