from solution import *



def test_01_step():
    "Handle an empty queue in `enqueue`: link the new node as both endpoints and increase size."
    q = LinkedQueue()
    assert q.enqueue("first") is None
    assert q.head is q.tail and q.head.value == "first"
    assert q.tail.next is None and q.size == 1


def test_02_complete_behavior():
    "Handle a nonempty queue: link after the old tail and advance tail and size."
    q = LinkedQueue()
    values = [7, None, 7, "last"]
    for i, value in enumerate(values):
        assert q.enqueue(value) is None
        assert q.size == i + 1 and q.tail.value == value
        assert q.tail.next is None
    node = q.head
    for value in values:
        assert node is not None and node.value == value
        node = node.next
    assert node is None
    other = LinkedQueue()
    assert other.head is None and other.size == 0
