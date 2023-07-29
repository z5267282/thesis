from typing import Type

from analyse import smart_trace
from counter import Counter
from execute import trace_program
from line import Line
from tree import Block, BodyBlock
from tree_parser import parse

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

def test_while_if():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    lines : list[Line] =  trace_program(program)

    filtered : list[Line] = smart_trace(line_mapping, lines)

    # check length first
    first = [Line(11, {})]
    no_branch = [Line(12, {}), Line(22, {})]
    first_branch = [Line(12, {}), Line(13, {}), Line(14, {}), Line(22, {})]
    second_branch = [
        Line(12, {}), Line(15, {}), Line(17, {}),
        # while loop
        Line(18, {}), Line(20, {}),
        # incrementation
        Line(22, {})
    ]
    assert filtered == first + no_branch + first_branch + second_branch

    # now check counters
    first_iter_outer = [Counter(1, 10, None)]
    assert filtered[1].counters == first_iter_outer
    assert filtered[2].counters == first_iter_outer

    fourth_iter_outer = [Counter(4, 10, None)]
    assert filtered[3].counters == fourth_iter_outer
    assert filtered[4].counters == fourth_iter_outer
    assert filtered[5].counters == fourth_iter_outer
    assert filtered[6].counters == fourth_iter_outer

    ninth_iter_outer = [Counter(9, 10, None)]
    assert filtered[7].counters == ninth_iter_outer
    assert filtered[8].counters == ninth_iter_outer
    assert filtered[9].counters == ninth_iter_outer

    first_iter_inner = [Counter(1, 4, None)]
    inner_exp = ninth_iter_outer + first_iter_inner
    assert filtered[10].counters == inner_exp
    assert filtered[11].counters == inner_exp

    assert filtered[12].counters == ninth_iter_outer
