def program():
    def a():
        print("a")
        b()

    def b():
        print("b")

    print("start")
    a()
    print("end")

from execute import trace_program
from line import Line

def test_nested():
    assert trace_program(program) == [
        [Line(1, "call"), Line(9, "line"), Line(10, "line")],
        [Line(2, "call"), Line(3, "line"), Line(4, "line")],
        [Line(6, "call"), Line(7, "line"), Line(7, "return")],
        [Line(4, "return")],
        [Line(11, "line"), Line(11, "return")]
    ]
