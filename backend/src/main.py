import sys
from types import FrameType
from typing import Any, List

from tree_parser import parse
from program import program

def main():
    lines, vars = [], []
    trace_hook_arg(handler, lines, vars)
    program()
    print(lines)
    print(vars)

def handler(frame : FrameType, event : str, arg : Any, lines, vars):
    print(frame.f_lineno)
    lines.append(frame.f_lineno)
    vars.append(frame.f_locals)

def trace_hook_arg(handler, lines, vars):
    def wrapper(frame : FrameType, event : str, arg : Any):
        handler(frame, event, arg, lines, vars)
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
