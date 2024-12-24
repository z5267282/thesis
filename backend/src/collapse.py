from collections import OrderedDict
from typing import Type

from config import ELLIPSE, LEADING_SPACES
from helper import uniq
from line import Line
from tree import Block, BodyBlock


def collapse(
    line_graph : list[Line], prev_context : list[Line],
    program : OrderedDict[int, str], root : BodyBlock
):
    """Collapse a program by showing indentation levels which have been
    executed.
    Return the lines of code, line numbers and rest of path indices as 
    per the data frame specification and a dictionary containing a mapping for where a raw line maps to in the filtered set"""
    show : OrderedDict[int, bool] = OrderedDict(
        (line, False) for line in range(root.start, root.end + 1)
    )

    graph : list[int] = Line.to_ints(line_graph)
    prev  : list[int] = Line.to_ints(prev_context)

    root.show_lines(graph, show)
    root.show_lines(prev, show)

    filtered : OrderedDict[int, bool] = uniq(show)

    for line in line_graph:
        line.range_filter_counters(filtered)

    # index in filtered which corresponds to shown line i
    indexed_lines : dict[int, int] = {
        line : new for new, line in enumerate(filtered) if filtered[line]
    }

    line_mapping : dict[int, Type[Block]] = root.map_lines()
    code : list[str] = [
        parse_line(line, program) if shown \
        else parse_blank(line, line_mapping) \
        for line, shown in filtered.items()
    ]
    lines : list[int | None] = [
        line if shown else None for line, shown in filtered.items()
    ]

    return code, lines, [ indexed_lines[g] for g in graph ], indexed_lines

def parse_line(line : int, program : OrderedDict[int, str]) -> str:
    result : str = program[line][LEADING_SPACES:]
    return result[:-1] if result and result[-1] == '\n' else result

def parse_blank(line : int, line_mapping : dict[int, Type["Block"]]) -> str:
    indent_level : int = line_mapping[line].indent_level
    return "{}{}".format(" " * (indent_level - LEADING_SPACES), ELLIPSE)
