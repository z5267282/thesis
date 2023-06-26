import sys
from types import FrameType
from typing import Any, Callable, List

from program import program
from tree import Block, BodyBlock
from tree_parser import parse

def main():
    root  : BodyBlock = parse(program)
    lines : List[Line] = []
    trace_program(trace_line, lines)

class Line:
    """dataclass to store line information"""
    def __init__(self, line_no : int, locals : dict):
        self.line_no : int  = line_no
        self.locals  : dict = locals
    
    def __str__(self):
        return f"{self.line_no} : {self.locals}"

def trace_program(handler : Callable, lines : List[Line]):
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

if __name__ == '__main__':
    main()
