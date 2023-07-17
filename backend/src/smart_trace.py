from io import StringIO
import sys

from line import Line
from state import State
from types import FrameType
from typing import Any, Callable

def trace_program(
    adjusted_program : Callable,
    lines : list[Line], output : list[str], buffer : StringIO,
    printed : State, vars : State
):
    """Intelligently execute and trace a program.
    Modify a list of lines given by reference which must be initially empty."""
    def wrapper(frame : FrameType, event : str, arg : Any):
        trace_line(frame, event, arg, lines, output)
        return wrapper

    sys.stdout = buffer
    sys.settrace(wrapper)
    adjusted_program()
    sys.settrace(None)
    sys.stdout = sys.__stdout__

def trace_line(
    frame : FrameType, event : str, arg : Any, lines : list[Line],
    output : list[str], buffer : StringIO,
    printed : State, vars : State
):
    if event != "line":
        return

    # state related steps
    printed.prev = printed.curr
    printed.curr = buffer.getvalue()
    diff : str = string_diff(printed.prev, printed.curr)
    output.append(diff)

    if lines:
        top : Line = lines[-1]
        top.

    vars : dict[str, str] = frame.f_lineno

    out : list[str] = output + [diff]
    lines.append(Line(frame.f_lineno, vars))

def string_diff(prev : str, curr : str):
    """Given that prev is a prefix of curr, obtain the difference:
    curr - prev"""
    return curr[len(prev):]
