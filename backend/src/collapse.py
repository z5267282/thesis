from collections import OrderedDict
from typing import Callable, Type

from helper import uniq
from tree import Block, BodyBlock

def collapse(graph : list[int], program : dict[int, str], root : BodyBlock):
    show : OrderedDict[int, bool] = OrderedDict(
        (line, True) for line in range(root.start, root.end + 1)
    )
    root.show_lines(graph, show)
    filtered : OrderedDict[int, bool] = uniq(show)

    # index in filtered which corresponds to shown line i
    indexed_lines = dict[int, int] = {
        line : new for new, line in enumerate(filtered) if filtered[line]
    }

    line_mapping : dict[int, Type[Block]] = root.map_lines()
    code : list[int] = [
        program[line] if shown else \
        "{}{}".format(" " * line_mapping[line].indent_level, "·" * 3) \
        for line, shown in filtered.items()
    ]
    lines : list[int | None] = [
        line if shown else None for line, shown in filtered.items()
    ]

    rest : list[int] = [ indexed_lines[g] for g in graph ]

    return \
        code, \
        [ str(line) if line is not None else "" for line in lines ], \
        { "start" : next(iter(program)), "rest" : rest }
