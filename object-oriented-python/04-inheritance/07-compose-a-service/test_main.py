from solution import *


def test_01_compose_a_service():
    assert NoticeBoard(BracketFormatter()).publish("Open") == "[Open]"
    class Formatter:
        def __init__(self, prefix):
            self.prefix = prefix
            self.calls = []
        def format(self, text):
            self.calls.append(text)
            return self.prefix + text
    first, second = Formatter("A:"), Formatter("B:")
    board = NoticeBoard(first)
    assert board.publish("one") == "A:one"
    assert board.publish("") == "A:"
    assert first.calls == ["one", ""]
    board.formatter = second
    assert board.publish("two") == "B:two"
    assert second.calls == ["two"]
    assert not issubclass(NoticeBoard, BracketFormatter)
