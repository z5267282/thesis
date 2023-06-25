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

def main():
    lines = []
    trace_hook_arg(handler, lines)
    program()
    for l in lines:
        print(l.line_no)

def handler(frame : FrameType, event : str, arg : Any, lines):
    lines.append(Line(frame.f_lineno, frame.f_locals))

def trace_hook_arg(handler, lines):
    def wrapper(frame : FrameType, event : str, arg : Any):
        handler(frame, event, arg, lines)
        return wrapper
    
    sys.settrace(wrapper)

if __name__ == '__main__':
    main()

# def main():
#     lines = []
#     settrace_closure(trace_execution, lines)
#     program()
#     print(lines)
    
# def trace_execution(frame, event, arg, lines):
#     lines.append(frame.f_lineno)

# def settrace_closure(trace_execution, lines):
#     def wrapper(frame, event, arg):
#         trace_execution(frame, event, arg, lines)
#         return wrapper
    
#     sys.settrace(wrapper)

# if __name__ == '__main__':
#     main()
