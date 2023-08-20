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
    line_graphs : list[list[Line]] = generate_graphs(filtered, line_mapping)

