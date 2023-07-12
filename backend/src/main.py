from io import StringIO
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
    output       : list[str] = []
    trace_program(trace_line, lines, output)

    for l in lines:
        print(l)

class Line:
    """A dataclass to store line information"""
    def __init__(self, line_no : int, locals : dict, out : list[str]):
        self.line_no : int = line_no
        self.locals  : dict = locals
        self.out     : list[str] = out
    
    def __str__(self):
        # return f"{self.line_no} : {self.locals}"
        return f"lno: {self.line_no}, out: '{self.out}'"

def trace_program(handler : Callable, lines : list[Line], output : list[str]):
    def wrapper(frame : FrameType, event : str, arg : Any):
        handler(frame, event, arg, lines, output)
        return wrapper
    
    sys.settrace(wrapper)
    program()
    sys.settrace(None)

def trace_line(frame : FrameType, event : str, arg : Any, lines, output : list[str]):
    if event != "line":
        return

    line_output : StringIO = StringIO()
    sys.stdout = line_output
    output.insert(0, line_output.getvalue())
    lines.append(Line(frame.f_lineno, frame.f_locals, output))
    sys.stdout = sys.__stdout__

def generate_execution_graph(root : BodyBlock, lines : list[Line]):
    """Create the intelligent unique execution path.
    Return a condensed line list."""
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
