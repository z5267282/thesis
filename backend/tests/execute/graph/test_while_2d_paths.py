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

from analyse import smart_trace_all
from execute import trace_program
from graph import generate_graphs
from line import Line
from tree_parser import parse

def test_while_2d_paths():
    root = parse(program)
    lines = trace_program(program)
    line_mapping = root.map_lines()
    filtered, = smart_trace_all(line_mapping, lines)
    graphs = generate_graphs(filtered, line_mapping)

    assert filtered == [
        # outer
        Line(3),
        # i = 1
        Line(4),
        Line(12),
        Line(13),
        Line(15),
        Line(17),
        # i = 2
        Line(4),
        Line(5),
        Line(7),
        Line(12),
        Line(13),
        Line(15),
        Line(17),
        # i = 5
        Line(4),
        Line(8),
        Line(10),
        Line(12),
        Line(13),
        Line(15),
        Line(17),
        # end
        Line(19), Line(19, event="return")
    ]

    assert graphs == [
        [Line(3)],

        [Line(3), Line(4)],
        [Line(3), Line(4), Line(12)],
        [Line(3), Line(4), Line(12), Line(13)],
        [Line(3), Line(4), Line(12), Line(13), Line(15)],
        [Line(3), Line(4), Line(12), Line(17)],

        [Line(3), Line(4)],
        [Line(3), Line(4), Line(5)],
        [Line(3), Line(4), Line(5), Line(7)],
        [Line(3), Line(4), Line(5), Line(7), Line(12)],
        [
            Line(3), Line(4), Line(5), Line(7), Line(12),
            Line(13)
        ],
        [
            Line(3), Line(4), Line(5), Line(7), Line(12),
            Line(13), Line(15)
        ],
        [
            Line(3), Line(4), Line(5), Line(7), Line(12),
            Line(17)
        ],

        [Line(3), Line(4)],
        [Line(3), Line(4), Line(8)],
        [Line(3), Line(4), Line(8), Line(10)],
        [Line(3), Line(4), Line(8), Line(10), Line(12)],
        [
            Line(3), Line(4), Line(8), Line(10), Line(12),
            Line(13)
        ],
        [
            Line(3), Line(4), Line(8), Line(10), Line(12),
            Line(13), Line(15)
        ],
        [
            Line(3), Line(4), Line(8), Line(10), Line(12),
            Line(17)
        ],

        [Line(3), Line(19)],
        [Line(3), Line(19), Line(19, event="return")],
    ]
