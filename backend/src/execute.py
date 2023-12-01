from copy import deepcopy
from io import StringIO
import sys

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
    lines   : list[Line] = []
    output  : list[str] = []
    printed : State[str] = State("", curr="")
    last    : Last = Last()
    def wrapper(frame : FrameType, event : str, arg : Any):
        trace_line(frame, event, arg, lines, output, buffer, printed, last)
        return wrapper

    sys.stdout = buffer
    sys.settrace(wrapper)
    program()
    sys.settrace(None)
    sys.stdout = sys.__stdout__
    return lines, last

def trace_line(
    frame : FrameType, event : str, _ : Any, lines : list[Line],
    output : list[str], buffer : StringIO, printed : State, last : Last
):
    if event != "line" and event != "return":
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
    if lines:
        lines[-1].output.extend(output)
    
    match event:
        case "line":
            lines.append(Line(frame.f_lineno, variables=variables))
        case "return":
            last.variables.update(frame.f_locals)
            last.output.extend(output)

def string_diff(prev : str, curr : str):
    """Given that prev is a prefix of curr, obtain the difference:
    curr - prev"""
    return curr[len(prev):]
