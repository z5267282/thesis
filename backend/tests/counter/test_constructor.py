from src.counter import Counter

def test_constructor():
    c = Counter(42, 69, None)

    assert c.iteration == 42
    assert c.total == 69
