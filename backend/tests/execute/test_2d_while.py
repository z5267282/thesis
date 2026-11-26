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

from typing import Type

from analyse import smart_trace_all
from counter import Counter
from execute import trace_program
from line import Line
from tree import Block, BodyBlock
from tree_parser import parse

def test_2d_while():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    lines = trace_program(program)
    filtered, = smart_trace_all(line_mapping, lines)
    
    assert len(filtered) == 7
    top_level, \
        outer_cond, outer_pre, \
        inner_cond, inner_block, \
        outer_post, outer_cond_end = filtered

    assert top_level == Line(3)

    # this is the only path through the program
    assert outer_cond == Line(4)
    assert outer_cond.counters == [Counter(1, 3, line_mapping[4])]

    assert outer_pre == Line(5)
    assert outer_pre.counters == [Counter(1, 3, line_mapping[4])]

    # two counters for nested loop
    assert inner_cond == Line(6) 
    assert inner_cond.counters == [
        Counter(1, 3, line_mapping[4]), Counter(1, 3, line_mapping[6])
    ]

    assert inner_block == Line(8)
    assert outer_post == Line(11)

    # the outter while evaluates to false and that's the last line run in 
    # the program, hence a return is hit
    assert outer_cond_end == Line(4, event="return")
