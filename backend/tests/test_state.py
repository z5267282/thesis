from state import State


def test_eq():
    s1 = State[str]("hello", curr="bye")
    s2 = State[str]("hello", curr="bye")
    assert s1 == s2

def test_ne_curr():
    s1 = State[str]("hello", curr="au revoir")
    s2 = State[str]("hello", curr="bye")
    assert s1 != s2

def test_ne_prev():
    s1 = State[str]("bonjour", curr="bye")
    s2 = State[str]("hello", curr="bye")
    assert s1 != s2

def test_different_type():
    s1 = State[str]("hello", curr="bye")
    s2 = 42
    assert s1 != s2
