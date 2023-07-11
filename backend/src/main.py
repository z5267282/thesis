import sys
from types import FrameType
from typing import Any, Callable, Type

from program import program
from tree import Block, BodyBlock, CodeBlock
from tree_parser import parse

def main():
    root         : BodyBlock = parse(program)
    lines        : list[Line] = []
    line_mapping : dict[int, Type[Block]] = {}
    trace_program(trace_line, lines)

class Line:
    """dataclass to store line information"""
    def __init__(self, line_no : int, locals : dict):
        self.line_no : int  = line_no
        self.locals  : dict = locals
    
    def __str__(self):
        return f"{self.line_no} : {self.locals}"

def trace_program(handler : Callable, lines : list[Line]):
    def wrapper(frame : FrameType, event : str, arg : Any):
        handler(frame, event, arg, lines)
        return wrapper
    
    sys.settrace(wrapper)
    program()
    sys.settrace(None)

def trace_line(frame : FrameType, event : str, arg : Any, lines):
    if event != "line":
        return

    lines.append(Line(frame.f_lineno, frame.f_locals))

def generate_execution_graph(root : BodyBlock, lines : list[Line]):
    """create the intelligent unique execution path
    return a condensed line list"""

    line_mapping : dict[int, Type[Block]] = {}
    root.map_lines(line_mapping)
    curr : Type[Block] | None = None
    for line in lines:
        line_no : int = line.line_no
        node : Type[Block] = lines[line_no]
        if isinstance(node, CodeBlock) and node.start == line_no:
            curr = node

if __name__ == '__main__':
    main()
