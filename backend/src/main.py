from typing import Type

from analyse import smart_trace
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
    for f in filtered:
        print(f.long_str())

if __name__ == '__main__':
    main()
