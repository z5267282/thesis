from stack import Stack
from tree import BodyBlock

def test_print():
    root = BodyBlock(1, 0)
    root.end = 4
    stack = Stack[BodyBlock](root)

    b1 = BodyBlock(2, 2)
    b1.end = 3
    stack.push(b1)

    b2 = BodyBlock(4, 2)
    b2.end = 4
    stack.push(b2)

    print(stack)

    assert str(stack) == \
"""1 : BodyBlock(start=4, end=4)
2 : BodyBlock(start=2, end=3)
3 : BodyBlock(start=1, end=4)"""

def test_iterate():
    stack = Stack[int]()
    for i in range(5):
        stack.push(i)
    
    seen = 0
    for s in stack:
        assert s == seen
        seen += 1
    assert seen == 5
