from line import Line

def test_equal():
    l1 = Line(42, {})
    l2 = Line(42, {})
    assert l1 == l2

def test_not_equal():
    l1 = Line(42, {})
    l2 = Line(72, {})
    assert l1 != l2
