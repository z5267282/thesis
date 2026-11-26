def program():
    i = 15
    if i % 2 == 0:
        print("two")
    elif i % 5 == 0:
        print("woot a five")
        print(":)")

from typing import Type

from analyse import smart_trace_all
from execute import trace_program
from line import Line
from tree import Block, BodyBlock
from tree_parser import parse

def test_elif():
    root = parse(program)
    line_mapping = root.map_lines()
    lines = trace_program(program)
    filtered, = smart_trace_all(line_mapping, lines)

    assert filtered == [
        Line(2), Line(5), Line(7),
        Line(7, event="return")
    ]
