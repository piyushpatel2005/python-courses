from solution import *

def test_node_keeps_payload_reference():
    payload=[]
    node=Node(payload)
    assert node.value is payload
    payload.append(8)
    assert node.value == [8]
    assert Node("end").value == "end"


def test_node_keeps_successor_reference():
    end=Node("end")
    first=Node("start",end)
    assert first.next is end and end.next is None
    other=Node("other")
    assert other.next is None and other is not end
