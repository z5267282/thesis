from counter import Counter
from tree import WhileBlock

def test_eq_same_while():
    w = WhileBlock(1, 0)
    w.end = 10

    c1 = Counter(4, 15, w)
    c2 = Counter(4, 15, w)

    assert c1 == c2

def test_eq_different_while():
    w1 = WhileBlock(1, 0)
    w1.end = 10
    c1 = Counter(4, 15, w1)

    w2 = WhileBlock(1, 0)
    w2.end = 10
    c2 = Counter(4, 15, w2)

    assert c1 == c2

def test_ne_same_while_same_total():
    w = WhileBlock(1, 0)
    w.end = 10

    c1 = Counter(5, 15, w)
    c2 = Counter(4, 15, w)

    assert c1 != c2

def test_ne_same_while_same_iter():
    w = WhileBlock(1, 0)
    w.end = 10

    c1 = Counter(4, 60, w)
    c2 = Counter(4, 15, w)

    assert c1 != c2
