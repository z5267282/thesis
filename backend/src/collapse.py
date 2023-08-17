from collections import OrderedDict
from typing import Type

from cfg import ELLIPSE
from helper import uniq
from tree import Block, BodyBlock

def collapse(graph : list[int], program : dict[int, str], root : BodyBlock):
    """Collapse a program by showing indentation levels which have been
    executed.
    Return the lines of code, line numbers and rest of path indices as 
    per the data frame specification."""
    show : OrderedDict[int, bool] = OrderedDict(
        (line, False) for line in range(root.start, root.end + 1)
    )
    root.show_lines(graph, show)
    filtered : OrderedDict[int, bool] = uniq(show)

    # index in filtered which corresponds to shown line i
    indexed_lines : dict[int, int] = {
        line : new for new, line in enumerate(filtered) if filtered[line]
    }

    line_mapping : dict[int, Type[Block]] = root.map_lines()
    code : list[int] = [
        program[line] if shown else \
        "{}{}".format(" " * line_mapping[line].indent_level, ELLIPSE) \
        for line, shown in filtered.items()
    ]
    lines : list[int | None] = [
        line if shown else None for line, shown in filtered.items()
    ]

    return code, lines, [ indexed_lines[g] for g in graph ]
