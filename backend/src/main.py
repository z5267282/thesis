from collections import OrderedDict
import re
from typing import Type

from analyse import smart_trace
from cfg import OFFSET
from collapse import collapse
from counter import Counter
from dataframe import DataFrame
from graph import generate_graphs
from helper import get_code_info, get_stripped_line
from line import Line
from program import program
from evaluate import evaluate
from execute import trace_program
from tree import Block, BodyBlock
from tree_parser import parse

def main():
    """Execute a program and generate a list of DataFrames representing
    execution states."""
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    all_lines : list[Line] = trace_program(program)
    filtered : list[Line] = smart_trace(line_mapping, all_lines)
    line_graphs : list[list[Line]] = generate_graphs(filtered, line_mapping)
    program_code : OrderedDict[int, str] = get_code_info(program)
    return [
        generate_data_frame(
            line_graph, program_code, root, line_mapping
        ) for line_graph in line_graphs
    ]

def generate_data_frame(
    line_graph : list[Line], program_code : OrderedDict[int, str],
    root : BodyBlock, line_mapping : dict[int, Type[Block]]
):
    code, lines, path = collapse(line_graph, program_code, root)
    curr : Line = line_graph[-1]
    variables : dict[str, str] = curr.vars.curr
    evalbox : list[str] = []
    curr_line : int = curr.line_no
    if line_mapping[curr_line].is_conditional():
        evalbox.append(
            generate_evalbox(program_code[curr_line], variables)
        )

    return DataFrame(
        code, adjust_lines(lines), 0 if not path else path[-1],
        variables, curr.output, path, curr.counters, evalbox
    )

def adjust_lines(lines):
    """Adjust line numbers so they are displayed correctly.
    Collapsed lines should be represented by an empty string.
    Line numbers should start from 1."""
    return [
        f"{str(line - OFFSET)}" if line is not None else "" \
        for line in lines
    ]

def generate_evalbox(line : str, variables : dict[str, str]):
    """Given a line with a conditional expression, expand it from a mapping
    of variable values."""
    raw_line : str = get_stripped_line(line)
    expression : str = re.sub(r"^[a-z]+\s+", "", raw_line)
    return evaluate(expression, variables)
