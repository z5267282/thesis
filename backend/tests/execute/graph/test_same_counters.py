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

from typing import Type

from analyse import smart_trace
from graph import generate_graphs
from line import Line
from execute import trace_program
from tree import Block, BodyBlock
from tree_parser import parse

def test_same_counters():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    all_lines : list[Line] = trace_program(program)
    filtered : list[Line] = smart_trace(line_mapping, all_lines)

    assert filtered == [
        Line(3, {}),

        # index 1
        Line(4, {}), Line(12, {}), Line(13, {}), Line(15, {}), Line(17, {}),

        # index 6
        Line(4, {}), Line(5, {}), Line(7, {}), Line(12, {}), Line(13, {}),
        Line(15, {}), Line(17, {}),

        Line(4, {}), Line(8, {}), Line(10, {}), Line(12, {}), Line(13, {}),
        Line(15, {}), Line(17, {}),

        Line(19, {})
    ]

    iter1, iter2 = filtered[1], filtered[6]
    assert iter1 == iter2
    assert iter1 is not iter2

    assert len(iter1.counters) == 1
    assert len(iter2.counters) == 1

    counter1, = iter1.counters
    counter2, = iter2.counters

    assert counter1 is not counter2

    line_graphs : list[list[Line]] = generate_graphs(filtered, line_mapping)

    assert line_graphs == [
        [Line(3, {})],
        # index 1
        [Line(3, {}), Line(4, {})],
        [Line(3, {}), Line(4, {}), Line(12, {})],
        [Line(3, {}), Line(4, {}), Line(12, {}), Line(13, {})],
        [Line(3, {}), Line(4, {}), Line(12, {}), Line(13, {}), Line(15, {})],
        [Line(3, {}), Line(4, {}), Line(12, {}), Line(17, {})],
        # index 6
        [Line(3, {}), Line(4, {})],
        [Line(3, {}), Line(4, {}), Line(5, {})],
        [Line(3, {}), Line(4, {}), Line(5, {}), Line(7, {})],
        [Line(3, {}), Line(4, {}), Line(5, {}), Line(7, {}), Line(12, {})],
        [
            Line(3, {}), Line(4, {}), Line(5, {}), Line(7, {}), Line(12, {}),
            Line(13, {})
        ],
        [
            Line(3, {}), Line(4, {}), Line(5, {}), Line(7, {}), Line(12, {}),
            Line(13, {}), Line(15, {})
        ],
        [
            Line(3, {}), Line(4, {}), Line(5, {}), Line(7, {}), Line(12, {}),
            Line(17, {})
        ],
        [Line(3, {}), Line(4, {})],
        [Line(3, {}), Line(4, {}), Line(8, {})],
        [Line(3, {}), Line(4, {}), Line(8, {}), Line(10, {})],
        [Line(3, {}), Line(4, {}), Line(8, {}), Line(10, {}), Line(12, {})],
        [
            Line(3, {}), Line(4, {}), Line(8, {}), Line(10, {}), Line(12, {}),
            Line(13, {})
        ],
        [
            Line(3, {}), Line(4, {}), Line(8, {}), Line(10, {}), Line(12, {}),
            Line(13, {}), Line(15, {})
        ],
        [
            Line(3, {}), Line(4, {}), Line(8, {}), Line(10, {}), Line(12, {}),
            Line(17, {})
        ],
        [Line(3, {}), Line(19, {})]
    ]

    graph1, graph2 = line_graphs[1], line_graphs[6]
    _, start1 = graph1
    _, start2 = graph2

    assert start1.line_no == 4
    assert start2.line_no == 4

    print(repr(iter1))
    print(repr(iter2))
    print(repr(start1))
    print(repr(start2))

    # the line graphs should correspond to the same lines above
    assert start1 is iter1
    assert start2 is iter2

    assert start1 is not start2

    assert len(start1.counters) == 1
    assert len(start2.counters) == 1
