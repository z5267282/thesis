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
    root : BodyBlock = parse(program)
    line_mapping : dict[int, Type[Block]] = root.map_lines()
    all_lines : list[Line] = trace_program(program)
    filtered : list[Line] = smart_trace(line_mapping, all_lines)
    line_graphs : list[list[Line]] = generate_graphs(filtered, line_mapping)
    program_code : OrderedDict[int, str] = get_code_info(program)
    # generate the dataframes
    dataframes = []
    for line_graph in line_graphs:
        code, lines, path = collapse(line_graph, program_code, root)
        correct_lines = [
            f"{str(line - OFFSET)}" if line is not None else "" \
            for line in lines
        ]
        curr : Line = line_graph[-1]
        variables : dict[str, str] = curr.vars.curr

        evalbox : list[str] = []
        curr_line : int = curr.line_no
        if line_mapping[curr_line].is_conditional():
            raw_line : str = get_stripped_line(program_code[curr_line])
            expression : str = re.sub(r"^[a-z]+\s+", "", raw_line)
            evalbox.append(evaluate(expression, variables))

        frame : DataFrame = DataFrame(
            code, correct_lines, len(line_graph) - 1,
            variables, curr.output, path, curr.counters, evalbox
        )
        dataframes.append(frame)
    return dataframes
