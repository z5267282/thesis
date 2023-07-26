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

"""Expected:
3
4
11
4
5
7
11
4
8
10
11
13"""

# def test_while_if():
#     root : BodyBlock = parse(program)
#     line_mapping : dict[int, Type[Block]]
#     root.map_lines(line_mapping)
#     lines : list[Line] =  trace_program()
#     filtered : list[Line] = smart_trace(line_mapping, lin)
