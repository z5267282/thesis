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
    
    # def __str__(self):
    #     return str(self.line_no)
    
def main():
    lines = []
    trace_hook_arg(handler, lines)
    program()
    # for i in range(len(lines)):
    #     print(lines[i])
    for l in lines:
        print(l)

def handler(frame : FrameType, event : str, arg : Any, lines):
    lines.append(Line(frame.f_lineno, frame.f_locals))

def trace_hook_arg(handler, lines):
    def wrapper(frame : FrameType, event : str, arg : Any):
        handler(frame, event, arg, lines)
        return wrapper
    
    sys.settrace(wrapper)

if __name__ == '__main__':
    main()
