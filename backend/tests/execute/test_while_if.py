from typing import Type

from analyse import smart_trace
from execute import trace_program
from line import Line
from tree import Block, BodyBlock
from tree_parser import parse

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

def test_while_if():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    lines, _ = trace_program(program)
    filtered : list[Line] = smart_trace(line_mapping, lines)

    assert len(filtered) == 12

    assert filtered[0].line_no == 11
    assert filtered[1].line_no == 12
    assert filtered[2].line_no == 19
    assert filtered[3].line_no == 12
    assert filtered[4].line_no == 13
    assert filtered[5].line_no == 15
    assert filtered[6].line_no == 19
    assert filtered[7].line_no == 12
    assert filtered[8].line_no == 16
    assert filtered[9].line_no == 18
    assert filtered[10].line_no == 19
    assert filtered[11].line_no == 21
