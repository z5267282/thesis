from typing import Type

from adjusted_program import adjusted_program
from line import Line
from program import program
from execute import trace_program
from tree import Block, BodyBlock
from tree_parser import parse

def main():
    root         : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = {}
    root.map_lines(line_mapping)
    lines : list[Line] = trace_program(adjusted_program)

    for l in lines:
        print(l)

if __name__ == '__main__':
    main()
