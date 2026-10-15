from solution import *

def test_double_node_keeps_payload_reference():
    payload=[]
    a=DoubleNode(payload); b=DoubleNode("sample")
    assert a.value is payload and b.value == "sample"
    payload.append(2)
    assert a.value == [2]


def test_double_node_starts_detached():
    a=DoubleNode(1); b=DoubleNode(1)
    assert a.prev is None and a.next is None
    assert b.prev is None and b.next is None and a is not b
    a.next=b
    assert b.next is None and b.prev is None
