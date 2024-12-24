def program():
    def a():
        print("a")
        b()

    def b():
        print("b")

    i = 0
    j = 0
    if i == 1:
        print("one")
    else:
        print("hi")
        i += 1
        a()

from execute import trace_program
from line import Line

def test_variables():
    lines = trace_program(program)
    assert len(lines) > 1
    first = lines[0]

    assert first == [
        # 0
        Line(1, "call"),
        # 1               2                  3                  4                  5                  6
        Line(9, "line"),  Line(10, "line"),  Line(11, "line"),  Line(14, "line"),  Line(15, "line"),  Line(16, "line")
    ]

    # creating the variables
    assert first[1].variables == {"i" : 0}
    assert first[2].variables == {"i" : 0, "j" : 0}

    # after a change on line 15
    assert first[5].variables == {"i" : 1, "j" : 0}
