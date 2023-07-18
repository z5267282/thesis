from io import StringIO
from typing import Type

from adjusted_program import adjusted_program
from line import Line
from program import program
from execute import trace_program
from state import State
from tree import Block, BodyBlock
from tree_parser import parse

def main():
    root         : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = {}
    root.map_lines(line_mapping)

    buffer  : StringIO = StringIO()
    lines   : list[Line] = []
    output  : list[str] = []
    printed : State = State("", curr="")
    trace_program(adjusted_program, lines, output, buffer, printed)

    for l in lines:
        print(l)

if __name__ == '__main__':
    main()
