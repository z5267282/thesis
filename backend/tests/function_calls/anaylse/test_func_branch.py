def program():
    def check_a():
        print("a")
        return False

    def check_b():
        print("b")
        return True

    i = 0
    if check_a():
        print("the a")
    elif i == 2:
        print("two")
    elif check_b():
        print("the bee")

import pytest

from analyse import smart_trace_all
from execute import trace_program
from line import Line
from tree_parser import parse

# @pytest.mark.skip(reason="proof of concept")
def test_func_branch():
    """This shows the complexity involved in allowing for function calls
    within branches.
    Currently, the tracing of an if statement relies on all lines relating to
    it being next to each other.
    It is left in here as a proof of concept"""
    root = parse(program)
    line_mapping = root.map_lines()
    lines = trace_program(program)
    print(lines)
    filtered = smart_trace_all(line_mapping, lines)
    print(filtered)
    assert filtered == [
        [Line(10, "line")],
        [Line(11, "line")],
        [Line(2, "call"), Line(4, "line"), Line(4, "return")],
        [Line(15, "line")],
        [Line(6, "call"), Line(8, "line"), Line(8, "return")],
        [Line(16, "line"), Line(16, "return")]
    ]
