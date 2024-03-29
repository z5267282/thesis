from typing import Type

from analyse import smart_trace
from execute import trace_program
from line import Line
from tree import Block, BodyBlock
from tree_parser import parse

def program():
    i = 0
    n = 3
    while i < n:
        j = 0
        while j < 3:
            print("X")
            j += 1

        print("\n")
        i += 1

def test_2d_while():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    lines, _ = trace_program(program)
    filtered : list[Line] = smart_trace(line_mapping, lines)
    
    assert len(filtered) == 6

    assert filtered[0].line_no == 11

    # this is the only path through the program
    assert filtered[1].line_no == 12
    assert len(filtered[1].counters) == 1
    assert filtered[1].counters[0].iteration == 1
    assert filtered[1].counters[0].total == 3

    assert filtered[2].line_no == 13
    assert len(filtered[2].counters)
    assert filtered[2].counters[0].iteration == 1
    assert filtered[2].counters[0].total == 3

    # two counters for nested loop
    assert filtered[3].line_no == 14
    assert len(filtered[3].counters) == 2
    assert filtered[3].counters[0].iteration == 1
    assert filtered[3].counters[0].total == 3

    assert filtered[3].counters[1].iteration == 1
    assert filtered[3].counters[1].total == 3

    assert filtered[4].line_no == 16
    assert filtered[5].line_no == 19
