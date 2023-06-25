import sys
from types import FrameType
from typing import Any, List

from tree_parser import parse
from program import program

class Line:
    """dataclass to store line information"""
    def __init__(self, line_no : int, locals : dict):
        self.line_no : int  = line_no
        self.locals  : dict = locals
    
    def __str__(self):
        """present just the line number for string representation"""
        return str(self.line_no)

def main():
    lines : List[Line] = []
    trace_hook_arg(handler, lines)
    # root = parse(program)
    program()

def handler(frame : FrameType, event : str, arg : Any, lines : List[Line]):
    lines.append(Line(frame.f_lineno, frame.f_locals))

def trace_hook_arg(f, extra):
    def wrapper(frame : FrameType, event : str, arg : Any):
        return f(frame, event, arg, extra)
    sys.settrace(wrapper)

if __name__ == '__main__':
    main()
