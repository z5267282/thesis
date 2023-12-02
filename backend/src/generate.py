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
    all_lines       : list[list[Line]] = trace_program(program)
    # the first top-level line run is the second one after the trace
    # note that the first line in trace is the call to program()
    top_level_start : int = all_lines[0][1].line_no

    root         : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    filtered     : list[list[Line]] = smart_trace_all(line_mapping, all_lines)
    program_code : OrderedDict[int, str] = get_code_info(program)

    # we manually take out the pre dataframe (ie. the call to program())
    # so manually genertate it here
    frames = [ generate_pre_dataframe(program_code, root) ]

    # we manage the current function call we are up to with a stack
    calls : Stack[list[Line]] = Stack()
    # the prev of program
    calls.push([])
    # the curr of program
    calls.push([])
    # graph of the previous function call
    for region in filtered:
        if region[0].event == "call":
            calls.push([])

        curr_context : list[Line] = calls.peek()
        prev_context : list[Line] = calls.peek_peek()
        line_graphs  : list[list[Line]] = generate_graphs(region, line_mapping)
        frames.extend(
            construct_dataframes(
                program_code, line_graphs,
                prev_context, curr_context,
                root, line_mapping, len(calls), top_level_start
            )
        )

        # the last line graph should be joined onto the current function call context
        curr_context.extend(line_graphs[-1])

        if region[-1].event == "return":
            calls.pop()

    # the last dataframe should have no path
    # easier to manually make it
    frames.pop()
    frames.append(
        generate_last(program_code, root, all_lines[-1][-1])
    )

    return frames 

def generate_pre_dataframe(
    program_code : OrderedDict[int, str], root : BodyBlock,
):
    code, lines, path, _ = collapse([], [], program_code, root)
    return DataFrame(
        code, adjust_lines(lines), None, State({}, curr={}), [], path, None, [], [], None
    )

def construct_dataframes(
    program_code : OrderedDict[int, str], line_graphs : list[list[Line]],
    prev_context : list[Line], curr_context : list[Line],
    root : BodyBlock, line_mapping : dict[int, Type[Block]],
    call_stack_size : int, top_level_start : int
):
    prev_vars : dict[str, Any] = {}
    frames    : list[DataFrame] = []
    for graph in line_graphs:
        line_graph = curr_context + graph 
        dataframe : DataFrame = generate_dataframe(
            line_graph, prev_context,
            program_code, root, line_mapping, prev_vars,
            determine_start(call_stack_size, top_level_start, line_graph)
        )
        frames.append(dataframe)
        prev_vars = dataframe.variables.curr

    return frames

def generate_dataframe(
    line_graph : list[Line], prev_context : list[Line],
    program_code : OrderedDict[int, str],
    root : BodyBlock, line_mapping : dict[int, Type[Block]],
    prev_vars : dict[str, Any], start : int | None
):
    code, lines, path, indexed = collapse(line_graph, prev_context, program_code, root)
    curr : Line = line_graph[-1]

    evalbox   : list[str] = []
    curr_line : int = curr.line_no
    if line_mapping[curr_line].is_conditional():
        evalbox.append(
            generate_evalbox(program_code[curr_line], curr.variables)
        )
    
    # where the last function call was
    call : None | dict = None
    if prev_context:
        # the call line is the last one in the previous context
        src : int = indexed[prev_context[-1].line_no]
        # the start of the function is 
        dst : int = indexed[line_graph[0].line_no]
        call = {
            # where the function was called
            "entry"  : src,
            # the definition of the function
            "target" : dst,
            "return" : curr.event == "return"
        }

    return DataFrame(
        code, adjust_lines(lines), indexed[curr_line],
        State(prev_vars, curr=curr.variables),
        curr.output, path, indexed[start], curr.counters, evalbox, call
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

def determine_start(call_stack_size : int, top_level_start : int, line_graph : list[Line]):
    """Determine what the raw starting line for the graph should be.
    If there are 2 stack items that means we are in the top level (ie. running program()).
    Otherwise the current graph's first item should have the function call we are up to."""
    if call_stack_size == 2:
        return top_level_start

    return line_graph[0].line_no

def generate_last(
    program_code : OrderedDict[int, str], root : BodyBlock,
    last : Line
):
    code, lines, path, _ = collapse([], [], program_code, root)
    return DataFrame(
        code, adjust_lines(lines), None,
        # last frame should have no changed variables
        State(last.variables, curr=last.variables),
        last.output, path, None, [], [], None
    )
