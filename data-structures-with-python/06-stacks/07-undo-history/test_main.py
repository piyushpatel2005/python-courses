from solution import *

def test_undo_restores_and_exhausts():
    h=UndoHistory(); other=UndoHistory("other")
    assert h.undo() is False and h.text==""
    h.replace("one"); h.replace("two"); h.replace("two")
    assert h.undo() is True and h.text=="two" and len(h.previous)==2
    assert h.undo() is True and h.text=="one"
    h.replace("branch"); assert h.undo() is True and h.text=="one"
    assert h.undo() is True and h.text==""
    assert h.undo() is False and h.text=="" and len(h.previous)==0
    assert other.text=="other" and other.undo() is False
