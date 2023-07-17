from io import StringIO
from typing import Type

from line import Line
from program import program
from smart_trace import trace_program
from state import State
from tree import Block, BodyBlock
from tree_parser import parse

def main():
    # root         : BodyBlock = parse(program)
    # line_mapping : dict[int, Type[Block]] = {}
    # buffer       : StringIO = StringIO()

    # lines        : list[Line] = []
    # output       : list[str] = []
    # for l in lines:
    #     print(l)
    pass

if __name__ == '__main__':
    main()
