from analyse import smart_trace
from line import Line
from tree import WhileBlock

def test_str():
    l = Line(20, {"i": "1"})
    l.vars.curr = {"i": "2"}
    w = WhileBlock(1, 0)
    l.add_counter(1, 5, w)

    assert str(l) == "20"

def test_long_str_no_counters():
    l = Line(20, {"i": "1"})
    l.vars.curr = {"i": "2"}
    l.output = ["hello", "champion"]
    w = WhileBlock(1, 0)
    w.end = 10

    assert l.long_str() == """line 20:
    output: [hello, champion]
    vars  :
        - prev: {i : 1}
        - curr: {i : 2}
    counters: []"""

def test_long_str_one_counter():
    l = Line(20, {"i": "1"})
    l.vars.curr = {"i": "2"}
    l.output = ["hello", "champion"]
    w = WhileBlock(1, 0)
    w.end = 10
    l.add_counter(1, 5, w)

    assert l.long_str() == """line 20:
    output: [hello, champion]
    vars  :
        - prev: {i : 1}
        - curr: {i : 2}
    counters: [
        (1/5) : WhileBlock(start=1, end=10)
    ]"""

def test_long_str_counters():
    l = Line(20, {"i": "1"})
    l.vars.curr = {"i": "2"}
    l.output = ["hello", "champion"]
    w1 = WhileBlock(1, 0)
    w1.end = 10
    l.add_counter(1, 5, w1)
    w2 = WhileBlock(4, 4)
    w2.end = 7
    l.add_counter(1, 10, w2)

    print(l.long_str())

    assert l.long_str() == """line 20:
    output: [hello, champion]
    vars  :
        - prev: {i : 1}
        - curr: {i : 2}
    counters: [
        (1/5) : WhileBlock(start=1, end=10),
        (1/10) : WhileBlock(start=4, end=7)
    ]"""