def program():
    def f():
        print("a")
        print("b")
    
    print("start")
    f()

from execute import trace_program
from line import Line
from tree_parser import parse

def test_simple():
    root = parse(program)
    lines = trace_program(program)
    assert lines == [
        [Line(1, "call"), Line(6, "line"), Line(7, "line")],
        [Line(2, "call"), Line(3, "line"), Line(4, "line"), Line(4, "return")],
        [Line(7, "return")]
    ]
