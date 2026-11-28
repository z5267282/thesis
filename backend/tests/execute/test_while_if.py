def program():
    i = 1
    twos, sevens = 0, 0
    while i < 8:
        if i % 2 == 0:
            print("two")
            twos += 1
        elif i % 7 == 0:
            print("seven")
            sevens += 1
        i += 1
    
    print(f"2s: {twos}, 7s: {sevens}")

from typing import Type

from analyse import smart_trace_all
from execute import trace_program
from line import Line
from tree import Block, BodyBlock
from tree_parser import parse

def test_while_if():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    lines = trace_program(program)
    filtered, = smart_trace_all(line_mapping, lines)
    assert filtered == [
        Line(3),
        # no branch taken
        Line(4), Line(11),
        # if branch
        Line(4), Line(5), Line(7), Line(11),
        # elif branch
        Line(4), Line(8), Line(10), Line(11),
        Line(13),
        Line(13, event="return")
    ]
