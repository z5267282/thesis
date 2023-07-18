import copy
from io import StringIO
import sys

from line import Line
from state import State
from types import FrameType
from typing import Any, Callable

def trace_program(adjusted_program : Callable):
    buffer  : StringIO = StringIO()
    lines   : list[Line] = []
    output  : list[str] = []
    printed : State = State("", curr="")
    """Get the execution path of a program with state information at each line.
    The program must end with an extra pass at the end and is hence "adjusted".
    Return a list of Line objects representing the program's raw execution path.
    """
    def wrapper(frame : FrameType, event : str, arg : Any):
        trace_line(frame, event, arg, lines, output, buffer, printed)
        return wrapper

    sys.stdout = buffer
    sys.settrace(wrapper)
    adjusted_program()
    sys.settrace(None)
    sys.stdout = sys.__stdout__
    return lines

def trace_line(
    frame : FrameType, event : str, arg : Any, lines : list[Line],
    output : list[str], buffer : StringIO, printed : State
):
    if event != "line":
        return

    # state related steps
    vars : dict[str, str] = copy.deepcopy(frame.f_locals)
    printed.prev = printed.curr
    printed.curr = buffer.getvalue()
    diff : str = string_diff(printed.prev, printed.curr)

    # manage previous state - note a "previous" state needs to exist (ie. line > starting)
    if lines:
        top : Line = lines[-1]
        top.vars.curr = vars
        # create a new list from the original
        rest : list = [diff] if diff else []
        top.output = output + rest

    if diff:
        output.append(diff)
    lines.append(Line(frame.f_lineno, vars))

def string_diff(prev : str, curr : str):
    """Given that prev is a prefix of curr, obtain the difference:
    curr - prev"""
    return curr[len(prev):]
