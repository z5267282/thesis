def program():
    i = 1
    twos, fives = 0, 0
    while i < 6:
        if i % 2 == 0:
            print("two")
            twos += 1
        elif i % 5 == 0:
            print("five")
            fives += 1
    
        j = 0
        while j < i:
            print("X", end="")
            j += 1
    
        i += 1
    
    print(f"2s: {twos}, 5s: {fives}")

from collections import OrderedDict
from typing import Type

from analyse import smart_trace
from collapse import collapse
from graph import generate_graphs
from helper import get_code_info
from line import Line
from execute import trace_program
from tree import Block, BodyBlock
from tree_parser import parse

def test_on_while_line():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    all_lines : list[Line] = trace_program(program)
    filtered : list[Line] = smart_trace(line_mapping, all_lines)
    line_graphs : list[list[Line]] = generate_graphs(filtered, line_mapping)
    program_code : OrderedDict[int, str] = get_code_info(program)

    assert line_graphs[:2] == [
        [Line(3, {})],
        [Line(3, {}), Line(4, {})]
    ]

    _, graph = line_graphs[:2]
    _, lines, _ = collapse(graph, program_code, root)
    _, curr = graph
    assert len(curr.counters) == 1
    counter, = curr.counters

    assert lines == [2, 3, 4, None, 19]
    assert counter.start == 2
    assert counter.end == 3
    assert counter.has_valid_range()

def test_inside_while():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    all_lines : list[Line] = trace_program(program)
    filtered : list[Line] = smart_trace(line_mapping, all_lines)
    line_graphs : list[list[Line]] = generate_graphs(filtered, line_mapping)
    program_code : OrderedDict[int, str] = get_code_info(program)

    assert line_graphs[:3] == [
        [Line(3, {})],
        [Line(3, {}), Line(4, {})],
        [Line(3, {}), Line(4, {}), Line(12, {})]
    ]

    _, _, graph = line_graphs[:3]
    _, lines, _ = collapse(graph, program_code, root)

    assert lines == [
        2,
        3,
        4,
        5,
        None,
        8,
        None,
        12,
        13,
        None,
        17,
        18,
        19
    ]

    _, _, curr = graph
    assert len(curr.counters) == 1
    counter, = curr.counters
    assert counter.start == 2
    assert counter.end == 11
