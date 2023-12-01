from collections import OrderedDict
import re
from typing import Any, Callable, Type

from analyse import smart_trace_all
from config import OFFSET
from collapse import collapse
from dataframe import DataFrame
from evaluate import evaluate
from execute import trace_program
from graph import generate_graphs
from helper import get_code_info, get_stripped_line
from line import Line
from stack import Stack
from state import State
from tree import Block, BodyBlock
from tree_parser import parse

def generate_dataframes(program : Callable):
    """Given a program, intelligently execute it and generate the necessary
    DataFrames to display execution"""
    all_lines    : list[list[Line]] = trace_program(program)

    root         : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    filtered     : list[list[Line]] = smart_trace_all(line_mapping, all_lines)
    program_code : OrderedDict[int, str] = get_code_info(program)

    # we manually take out the pre dataframe (ie. the call to program())
    # so manually genertate it here
    frames = [generate_dataframe(
        [], [], program_code, root, line_mapping, {}, True
    )]

    # we manage the current function call we are up to with a stack
    calls : Stack[list[Line]] = Stack()
    calls.push([])
    # graph of the previous function call
    for i, region in enumerate(filtered):
        prev_context : list[Line] = calls.pop()
        line_graphs : list[list[Line]] = generate_graphs(region, line_mapping)
        frames.extend(
            construct_dataframes(
                program_code, line_graphs, prev_context, root, line_mapping, i == len(filtered) - 1 
            )
        )
        calls.push(line_graphs[-1])

    return frames 
        
def construct_dataframes(
    program_code : OrderedDict[int, str],
    line_graphs : list[list[Line]], prev_context : list[Line],
    root : BodyBlock, line_mapping : dict[int, Type[Block]], last : bool
):
    prev_vars : dict[str, Any] = {}
    frames    : list[DataFrame] = []
    for line_graph in line_graphs:
        dataframe : DataFrame = generate_dataframe(
            line_graph, prev_context,
            program_code, root, line_mapping, prev_vars, last
        )
        frames.append(dataframe)
        prev_vars = dataframe.variables.curr

    return frames

def generate_dataframe(
    line_graph : list[Line], prev_context : list[Line],
    program_code : OrderedDict[int, str],
    root : BodyBlock, line_mapping : dict[int, Type[Block]],
    prev_vars : dict[str, Any], pre : bool
):
    code, lines, path, indexed = collapse(line_graph, prev_context, program_code, root)
    curr : Line = line_graph[-1]

    evalbox   : list[str] = []
    curr_line : int = curr.line_no
    if line_mapping[curr_line].is_conditional():
        evalbox.append(
            generate_evalbox(program_code[curr_line], curr.variables)
        )
    
    # COMPUTE CURR
    # COMPUTE START

    return DataFrame(
        code, adjust_lines(lines), path[-1],
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

def determine_curr(pre : bool, path : list[int], graph : list[Line]):
    """For most lines the current one is the last one in the graph.
    For return lines in functions, there should be no curr.
    The path parameter is the same as the graph except it is correctly mapped
    to the collapsed range (ie. has same number of elements).
    We need the actual Line object to determine whether the line was a
    return."""

    # when we call program() there should be no current line
    if pre:
        return None

    if graph[-1].event == "return":
        return None
    
    return path[-1]
