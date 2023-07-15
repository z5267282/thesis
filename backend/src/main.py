from io import StringIO
import sys
from types import FrameType
from typing import Any, Callable, Type

from line import Line
from program import program
from tree import Block, BodyBlock
from tree_parser import parse

def main():
    root         : BodyBlock = parse(program)
    lines        : list[Line] = []
    line_mapping : dict[int, Type[Block]] = {}
    output       : list[str] = []
    trace_program(trace_line, lines, output)

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

if __name__ == '__main__':
    main()
