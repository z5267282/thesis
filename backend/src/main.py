import sys
from types import FrameType
from typing import Any, List

from parser import parse
from program import program

class Line:
    """dataclass to store line information"""
    def __init__(self, line_no : int, locals : dict):
        self.line_no : int  = line_no
        self.locals  : dict = locals

lines = List[Line]

def trace_execution(frame : FrameType, event : str, arg : Any):
    lines.append(Line(frame.f_lineno, frame.f_locals))
    return trace_execution

sys.settrace(trace_execution)

root = parse(program)
program()
