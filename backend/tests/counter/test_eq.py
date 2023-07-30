from counter import Counter
from tree import WhileBlock

def test_eq_same_while():
    w = WhileBlock(1, 0)
    w.end = 10

    c1 = Counter(4, 15, w)
    c2 = Counter(4, 15, w)

    assert c1 == c2
