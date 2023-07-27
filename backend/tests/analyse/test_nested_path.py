from typing import Type

from analyse import smart_trace
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
