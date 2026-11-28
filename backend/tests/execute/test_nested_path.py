def program():
    i = 0
    while i < 10:
        if i == 3:
            print("wow a three!")
        elif i == 8:
            print("here are all the multiples of 2 under 8")
            j = 0
            while j < i:
                print(j)
                j += 2
        
        i += 1

from typing import Type

from analyse import smart_trace_all
from counter import Counter
from execute import trace_program
from line import Line
from tree import Block, BodyBlock
from tree_parser import parse

def test_nested_path():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    lines = trace_program(program)
    filtered, = smart_trace_all(line_mapping, lines)
    assert filtered == [
        Line(2),
        # no branch taken
        Line(3), Line(13),
        # if branch
        Line(3), Line(4), Line(5), Line(13),
        # elif taken
        Line(3), Line(6), Line(8),
            # inner while
            Line(9), Line(11),
        # end of elif
        Line(13),
        Line(3, event="return")
    ]

    outer_while = line_mapping[3]
    inner_while = line_mapping[9]

    assert [ f.counters for f in filtered ] == [
        [],
        # no branch taken
        [Counter(1, 10, outer_while)], [Counter(1, 10, outer_while)],
        # if branch
        [Counter(4, 10, outer_while)], [Counter(4, 10, outer_while)], [Counter(4, 10, outer_while)], [Counter(4, 10, outer_while)],
        # elif taken
        [Counter(9, 10, outer_while)], [Counter(9, 10, outer_while)], [Counter(9, 10, outer_while)],
            # inner while
            [Counter(9, 10, inner_while), Counter(1, 4, inner_while)], [Counter(9, 10, inner_while), Counter(1, 4, inner_while)],
        # end of elif
        [Counter(9, 10, outer_while)],
        []
    ]
