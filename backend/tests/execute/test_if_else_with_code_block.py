def program():
    i = 0
    if i % 7 == 0:
        print("a special number!")
        print(":D")
    else:
        print("meh")
    print("that's all folks")

from execute import trace_program
from line import Line

def test_if_else_with_code_block():
    filtered, = trace_program(program)
    assert filtered == [
        # the call to the program entry function (in this case program1) is 
        # stripped by smart_trace_all
        Line(1, event="call"),
        Line(2), Line(3), Line(4), Line(5), Line(8),
        # same note as above for the return
        Line(8, event="return")
    ]
