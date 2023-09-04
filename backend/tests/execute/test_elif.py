from typing import Type

from analyse import smart_trace
from execute import trace_program
from line import Line
from tree import Block, BodyBlock
from tree_parser import parse

def program():
    i = 15
    if i % 2 == 0:
        print("two")
    elif i % 5 == 0:
        print("woot a five")
        print(":)")

def test_elif():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    lines : list[Line] =  trace_program(program)
    filtered : list[Line] = smart_trace(line_mapping, lines)

    assert len(filtered) == 3

    assert filtered[0].line_no == 10
    assert filtered[1].line_no == 13
    assert filtered[2].line_no == 15
