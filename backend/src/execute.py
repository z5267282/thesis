from collections import OrderedDict
from copy import deepcopy
from io import StringIO
import sys

from helper import get_code_info, get_stripped_line
from last import Last
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
    code    : OrderedDict[int, str] = get_code_info(program)
    output  : list[str] = []
    printed : State[str] = State("", curr="")

    def wrapper(frame : FrameType, event : str, arg : Any):
        trace_line(frame, event, arg, lines, curr, code, output, buffer, printed)
        return wrapper

    sys.stdout = buffer
    sys.settrace(wrapper)
    program()
    sys.settrace(None)
    sys.stdout = sys.__stdout__
    return lines, curr

def trace_line(
    frame : FrameType, event : str, _ : Any, lines : list[list[Line]],
    curr : list[Line], code : OrderedDict[int, str],
    output : list[str], buffer : StringIO, printed : State
):
    # when we call a function that indicates we should start a new subsection in tracing
    match event:
        case "line":
            if get_stripped_line(code[frame.f_lineno]).startswith("def"):
                return
        case "call":
            # the exception to this is if we have no traced lines
            if lines:
                lines.append(deepcopy(curr))
                # curr.clear()
        case "return":
            pass
        case _:
            return

    # state related steps
    variables : dict[str, Any] = deepcopy(frame.f_locals)
    printed.prev = printed.curr
    printed.curr = buffer.getvalue()
    diff : str = string_diff(printed.prev, printed.curr)

    if diff:
        output.append(diff)

    # manage previous state
    # note a "previous" state needs to exist (ie. line > starting)
    if curr:
        curr[-1].output.extend(output)
    
    line : Line = Line(frame.f_lineno, event, variables=variables)
    curr.append(line)
    if event == "return":
        line.output.extend(output)

def string_diff(prev : str, curr : str):
    """Given that prev is a prefix of curr, obtain the difference:
    curr - prev"""
    return curr[len(prev):]
