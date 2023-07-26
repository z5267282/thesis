from typing import Type

from analyse import smart_trace
from counter import Counter
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

def test_loop_counter():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = {}
    root.map_lines(line_mapping)
    lines : list[Line] =  trace_program(program)
    filtered : list[Line] = smart_trace(line_mapping, lines)

    assert len(filtered) == 12

    assert filtered[0].line_no == 12
    assert filtered[1].line_no == 13
    assert filtered[2].line_no == 20
    assert filtered[3].line_no == 13
    assert filtered[4].line_no == 14
    assert filtered[5].line_no == 16
    assert filtered[6].line_no == 20
    assert filtered[7].line_no == 13
    assert filtered[8].line_no == 17
    assert filtered[9].line_no == 19
    assert filtered[10].line_no == 20
    assert filtered[11].line_no == 22

    assert len(filtered[1].counters) == 1
    counter : Counter = filtered[1].counters[0]
    assert counter.iteration == 1
    assert counter.total == 7
