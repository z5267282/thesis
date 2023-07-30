from counter import Counter
from tree import WhileBlock

def test_str():
    w = WhileBlock(42, 0)
    w.end = 80
    c = Counter(40, 100, w)
    assert str(c) == "(40/100) : WhileBlock(start=42, end=80)"
