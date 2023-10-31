def program():
    i = 0
    print(f"hello: {i}")
    j = 1
    print(f"{i} + {j} = {i + j}")

from execute import trace_program
from line import Line

def test_line_output():
    lines = trace_program(program)
    assert lines == [
        Line(2), Line(3), Line(4), Line(5)
    ]

    assert len(lines[0].output) == 0
    assert lines[1].output == ["hello: 0\n"]
    assert lines[2].output == ["hello: 0\n"]
    assert lines[3].output == ["hello: 0\n", "0 + 1 = 1\n"]
