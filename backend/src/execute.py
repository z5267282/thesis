from collections import OrderedDict
from copy import copy
from io import StringIO
import sys
from types import FunctionType

from helper import get_code_info, get_stripped_line
from line import Line
from state import State
from types import FrameType
from typing import Any, Callable

def trace_program(program : Callable):
    """Get the execution path of a program with state information at each line.
    Return a list of Line objects representing the program's raw execution
    path."""
    buffer  : StringIO = StringIO()
    lines   : list[list[Line]] = []
    curr    : list[Line] = []
    # this should have been an argument but not good to change function parameters now
    code    : OrderedDict[int, str] = get_code_info(program)
    output  : list[str] = []
    printed : State[str] = State("", curr="")
    # singleton if a last line exists
    last    : list[Line] = [None]

    def wrapper(frame : FrameType, event : str, arg : Any):
        trace_line(frame, event, arg, lines, curr, code, output, buffer, printed, last)
        return wrapper

    sys.stdout = buffer
    sys.settrace(wrapper)
    program()
    sys.settrace(None)
    sys.stdout = sys.__stdout__
    return lines

def trace_line(
    frame : FrameType, event : str, _ : Any, lines : list[list[Line]],
    curr : list[Line], code : OrderedDict[int, str],
    output : list[str], buffer : StringIO, printed : State, last : list[Line]
):
    # when we call a function that indicates we should start a new subsection in tracing
    match event:
        case "line":
            # ignore the execution of function definitions as statements
            if get_stripped_line(code[frame.f_lineno]).startswith("def"):
                return
        case "call":
            # we should ignore the first run line - this is the call to program()
            if frame.f_lineno != 1:
                add_func_subsection(lines, curr)
            # need to do stuff for return, but it happens after the line has been registered
        case "return":
            pass
        case _:
            return

    # state related steps
    raw_variables : dict[str, Any] = frame.f_locals
    variables     : dict[str, Any] = {
        var : value for var, value in raw_variables.items() \
            if not isinstance(value, FunctionType) 
    }

    printed.prev = printed.curr
    printed.curr = buffer.getvalue()
    diff : str = string_diff(printed.prev, printed.curr)

    if diff:
        output.append(diff)
    
    # manage previous state
    # note a "previous" state needs to exist (ie. line > starting)
    if last[0]:
        last[0].output.extend(output)

    line : Line = Line(frame.f_lineno, event, variables=variables)
    curr.append(line)
    if event == "return":
        line.output.extend(output)
        add_func_subsection(lines, curr)
    
    last[0] = line
    
def add_func_subsection(lines : list[list[Line]], curr : list[Line]):
    """Add a contiguous subsection of a execution within a function.
    This could be:
        - [call, ...]
        - [..., return], [...]
        - [...], [call, ...]
    """
    lines.append(copy(curr))
    curr.clear()

def string_diff(prev : str, curr : str):
    """Given that prev is a prefix of curr, obtain the difference:
    curr - prev"""
    return curr[len(prev):]
