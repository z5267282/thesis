def program():
    def f():
        print("a")
        print("b")
    
    print("start")
    f()

from execute import trace_program
from line import Line

def test_simple():
    lines, x = trace_program(program)
    assert x == 1
    assert lines == [
        [Line(1, "call"), Line(6, "line"), Line(7, "line")],
        [Line(2, "call"), Line(3, "line"), Line(4, "line"), Line(4, "return")],
        [Line(7, "return")]
    ]
