from collections import OrderedDict
import re
from typing import Any, Callable, Type

from analyse import smart_trace
from config import OFFSET
from collapse import collapse
from dataframe import DataFrame
from graph import generate_graphs
from helper import get_code_info, get_stripped_line
from line import Line
from evaluate import evaluate
from execute import trace_program
from state import State
from tree import Block, BodyBlock
from tree_parser import parse

def generate_dataframes(program : Callable):
    """Given a program, intelligently execute it and generate the necessary
    DataFrames to display execution"""
    root         : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    all_lines    : list[Line] = trace_program(program)
    filtered     : list[Line] = smart_trace(line_mapping, all_lines)
    line_graphs  : list[list[Line]] = generate_graphs(filtered, line_mapping)
    program_code : OrderedDict[int, str] = get_code_info(program)

    first_frame : DataFrame = generate_first_dataframe(program_code, root)
    prev_vars : dict[str, Any] = first_frame.variables.curr
    program_frames : list[DataFrame] = []
    for line_graph in line_graphs:
        dataframe : DataFrame = generate_dataframe(
            line_graph, program_code, root, line_mapping, prev_vars
        )
        program_frames.append(dataframe)
        prev_vars = dataframe.variables.curr

    return [first_frame] + program_frames

def generate_first_dataframe(
    program_code : OrderedDict[int, str], root : BodyBlock,
):
    code, lines, path = collapse([], program_code, root)
    return DataFrame(
        code, adjust_lines(lines), None,
        State({}, curr={}), [], path, [], [] 
    )

def generate_dataframe(
    line_graph : list[Line], program_code : OrderedDict[int, str],
    root : BodyBlock, line_mapping : dict[int, Type[Block]],
    prev_vars : dict[str, Any]
):
    code, lines, path = collapse(line_graph, program_code, root)
    curr : Line = line_graph[-1]

    evalbox   : list[str] = []
    curr_line : int = curr.line_no
    if line_mapping[curr_line].is_conditional():
        evalbox.append(
            generate_evalbox(program_code[curr_line], curr.variables)
        )

    return DataFrame(
        code, adjust_lines(lines), 0 if not path else path[-1],
        State(prev_vars, curr=curr.variables),
        curr.output, path, curr.counters, evalbox
    )

def adjust_lines(lines):
    """Adjust line numbers so they are displayed correctly.
    Collapsed lines should be represented by an empty string.
    Line numbers should start from 1."""
    return [
        f"{str(line - OFFSET)}" if line is not None else "" \
            for line in lines
    ]

def generate_evalbox(line : str, variables : dict[str, Any]):
    """Given a line with a conditional expression, expand it from a mapping
    of variable values."""
    raw_line        : str = get_stripped_line(line)
    no_control_flow : str = re.sub(r"^[a-z]+\s+", "", raw_line)
    expression      : str = re.sub(r":[^:]*$", "", no_control_flow)
    return evaluate(expression, variables)
