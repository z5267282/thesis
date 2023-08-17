from typing import Type

from analyse import smart_trace
from graph import generate_graphs
from line import Line
from program import program
from execute import trace_program
from tree import Block, BodyBlock
from tree_parser import parse

def main():
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    lines : list[Line] = trace_program(program)
    filtered : list[Line] = smart_trace(line_mapping, lines)
    graphs : list[list[int]] = generate_graphs(filtered, line_mapping)
    # generate the dataframes
    dataframes = []
    for graph in graphs:
        pass

if __name__ == '__main__':
    main()
