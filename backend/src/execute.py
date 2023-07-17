from io import StringIO
import sys

from line import Line
from state import State
from types import FrameType
from typing import Any, Callable

def trace_program(
    adjusted_program : Callable,
    lines : list[Line], output : list[str], buffer : StringIO, printed : State
):
    """Intelligently execute and trace a program.
    The adjusted program must end with an extra pass at the end.
    Modify a list of lines given by reference which must be initially empty."""
    def wrapper(frame : FrameType, event : str, arg : Any):
        trace_line(frame, event, arg, lines, output, buffer, printed)
        return wrapper

    sys.stdout = buffer
    sys.settrace(wrapper)
    adjusted_program()
    sys.settrace(None)
    sys.stdout = sys.__stdout__

def trace_line(
    frame : FrameType, event : str, arg : Any, lines : list[Line],
    output : list[str], buffer : StringIO, printed : State
):
    if event != "line":
        return

    # state related steps
    vars : dict[str, str] = frame.f_locals
    printed.prev = printed.curr
    printed.curr = buffer.getvalue()
    diff : str = string_diff(printed.prev, printed.curr)

    # with open("/tmp/a.txt", "w") as f:
    #     # print(f"{frame.f_lineno} - {diff}", file=f)
    #     print(frame.f_lineno, file=f)

    # manage previous state - note a "previous" state needs to exist (ie. line > starting)
    if lines:
        top : Line = lines[-1]
        top.vars.curr = vars
        # join list to not create references over same lines

        # if diff:
        #     top.output = output + [diff]

        top.output = output + [diff]

    # if diff:
    #     output.append(diff)

    output.append(diff)

    lines.append(Line(frame.f_lineno, vars))

def string_diff(prev : str, curr : str):
    """Given that prev is a prefix of curr, obtain the difference:
    curr - prev"""
    return curr[len(prev):]
