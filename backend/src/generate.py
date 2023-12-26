from collections import OrderedDict
import re
from typing import Any, Callable, Type

from analyse import smart_trace
from config import OFFSET
from collapse import collapse
from dataframe import DataFrame
from evaluate import evaluate
from execute import trace_program
from graph import generate_graphs
from helper import get_code_info, get_stripped_line
from line import Line
from state import State
from tree import Block, BodyBlock
from tree_parser import parse

def generate_dataframes(program : Callable) -> list[DataFrame]:
    """Given a program, intelligently execute it and generate the necessary
    DataFrames to display execution"""
    all_lines, last = trace_program(program)
    root         : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    filtered     : list[Line] = smart_trace(line_mapping, all_lines)
    line_graphs  : list[list[Line]] = generate_graphs(filtered, line_mapping)
    program_code : OrderedDict[int, str] = get_code_info(program)
    return construct_dataframes(
        program_code, line_graphs, root, line_mapping, last
    )

def construct_dataframes(
    program_code : OrderedDict[int, str], line_graphs : list[list[Line]],
    root : BodyBlock, line_mapping : dict[int, Type[Block]], last : Line
) -> list[DataFrame]:
    first_frame : DataFrame = generate_edge_dataframe(
        program_code, root, {}, []
    )
    prev_vars      : dict[str, Any] = first_frame.variables.curr
    program_frames : list[DataFrame] = []
    for line_graph in line_graphs:
        dataframe : DataFrame = generate_dataframe(
            line_graph, program_code, root, line_mapping, prev_vars
        )
        program_frames.append(dataframe)
        prev_vars = dataframe.variables.curr
    
    last_frame : DataFrame = generate_edge_dataframe(
        program_code, root, last.variables, last.output
    )

    return [first_frame] + program_frames + [last_frame]

def generate_edge_dataframe(
    program_code : OrderedDict[int, str], root : BodyBlock,
    variables : dict[str, Any], output : list[str]
) -> DataFrame:
    """Construct a DataFrame that is either before or after the program's
    execution.
    Hence, these frames only have program state and no execution graph."""
    code, lines, path = collapse([], program_code, root)
    return DataFrame(
        code, adjust_lines(lines), None,
        State(variables, curr=variables), output, path, [], [] 
    )

def generate_dataframe(
    line_graph : list[Line], program_code : OrderedDict[int, str],
    root : BodyBlock, line_mapping : dict[int, Type[Block]],
    prev_vars : dict[str, Any]
) -> DataFrame:
    code, lines, path = collapse(line_graph, program_code, root)
    curr : Line = line_graph[-1]

    evalbox   : list[str] = []
    curr_line : int = curr.line_no
    if line_mapping[curr_line].is_conditional():
        evalbox.append(
            generate_evalbox(program_code[curr_line], curr.variables)
        )

    return DataFrame(
        code, adjust_lines(lines), path[-1],
        State(prev_vars, curr=curr.variables),
        curr.output, path, curr.counters, evalbox
    )

def generate_evalbox(line : str, variables : dict[str, Any]) -> str:
    """Given a line with a conditional expression, expand it from a mapping
    of variable values."""
    raw_line        : str = get_stripped_line(line)
    no_control_flow : str = re.sub(r"^[a-z]+\s+", "", raw_line)
    expression      : str = re.sub(r":[^:]*$", "", no_control_flow)
    return evaluate(expression, variables)

def adjust_lines(lines) -> list[str]:
    """Adjust line numbers so they are displayed correctly.
    Collapsed lines should be represented by an empty string.
    Line numbers should start from 1."""
    return [
        f"{str(line - OFFSET)}" if line is not None else "" \
            for line in lines
    ]
