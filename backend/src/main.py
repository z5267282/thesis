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
        return handler(frame, event, arg, lines, vars)
    
    sys.settrace(wrapper)

if __name__ == '__main__':
    main()
