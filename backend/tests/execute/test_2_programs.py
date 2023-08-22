def program1():
    i = 0
    if i % 7 == 0:
        print("a special number!")
        print(":D")
    else:
        print("meh")
    print("that's all folks")

def program2():
    i = 42
    j = 69
    print(f"{i} + {j} = {i + j}")

from execute import trace_program
from line import Line

def test_2_programs():
    filtered1 = trace_program(program1)
    assert filtered1 == [
        Line(2, {}), Line(3, {}), Line(4, {}), Line(5, {}), Line(8, {})
    ]

    filtered2 = trace_program(program2)
    assert filtered2 == [Line(11, {}), Line(12, {}), Line(13, {})]
