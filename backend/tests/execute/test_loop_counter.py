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
from counter import Counter
from execute import trace_program
from line import Line
from tree import Block, BodyBlock
from tree_parser import parse

def test_loop_counter():
    root = parse(program)
    line_mapping = root.map_lines()
    lines = trace_program(program)
    filtered, = smart_trace_all(line_mapping, lines)

    assert len(filtered) == 13
    assert filtered == [
        # top level
        Line(3),
        # first path: skip to end
        Line(4), Line(11),
        # if branch
        Line(4), Line(5), Line(7), Line(11),
        # elif branch
        Line(4), Line(8), Line(10), Line(11),
        # end of program
        Line(13), Line(13, event="return")
    ]
    assert [ f.counters for f in filtered ] == [
        # top level
        [],
        # first path: skip to end
        [Counter(1, 7, line_mapping[4])], [Counter(1, 7, line_mapping[4])],
        # if branch
        [Counter(2, 7, line_mapping[4])], [Counter(2, 7, line_mapping[4])], [Counter(2, 7, line_mapping[4])], [Counter(2, 7, line_mapping[4])],
        # elif branch
        [Counter(7, 7, line_mapping[4])], [Counter(7, 7, line_mapping[4])], [Counter(7, 7, line_mapping[4])], [Counter(7, 7, line_mapping[4])],
        # end of program
        [], []
    ]
