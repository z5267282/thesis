import copy
from io import StringIO
import sys

from line import Line
from state import State
from types import FrameType
from typing import Any, Callable

def trace_program(program : Callable):
    buffer  : StringIO = StringIO()
    lines   : list[Line] = []
    output  : list[str] = []
    printed : State[str] = State("", curr="")
    """Get the execution path of a program with state information at each line.
    Return a list of Line objects representing the program's raw execution
    path."""
    def wrapper(frame : FrameType, event : str, arg : Any):
        trace_line(frame, event, arg, lines, output, buffer, printed)
        return wrapper

    sys.stdout = buffer
    sys.settrace(wrapper)
    program()
    sys.settrace(None)
    sys.stdout = sys.__stdout__
    return lines

def trace_line(
    frame : FrameType, event : str, arg : Any, lines : list[Line],
    output : list[str], buffer : StringIO, printed : State
):
    if event != "line" and event != "return":
        return

    # state related steps
    variables : dict[str, str] = copy.deepcopy(frame.f_locals)
    printed.prev = printed.curr
    printed.curr = buffer.getvalue()
    diff : str = string_diff(printed.prev, printed.curr)

    if diff:
        output.append(diff)

    # manage previous state
    # note a "previous" state needs to exist (ie. line > starting)
    if lines:
        top : Line = lines[-1]
        top.vars.curr = variables
        top.output.extend(output)

    if event == "line":
        lines.append(Line(frame.f_lineno, variables))

def string_diff(prev : str, curr : str):
    """Given that prev is a prefix of curr, obtain the difference:
    curr - prev"""
    return curr[len(prev):]
