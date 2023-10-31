from counter import Counter
from line import Line
from state import State
from tree import WhileBlock

def test_creation():
    l = Line(20, variables={"i": 1})
    w = WhileBlock(1, 0)
    l.add_counter(1, 5, w)

    assert l.line_no == 20
    assert l.variables == {"i": 1}
    assert l.counters == [Counter(1, 5, w)]
