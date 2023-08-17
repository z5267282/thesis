from collections import OrderedDict
from typing import Callable, Type

from helper import uniq
from tree import Block, BodyBlock

tmp = "·"

def collapse(
    graph : list[int], program : dict[int, str],
    root : BodyBlock, line_mapping : dict[int, Type[Block]]
):
    # should be a wrapper
    show : OrderedDict[int, bool] = OrderedDict(
        (line, True) for line in range(root.start, root.end + 1)
    )
    root.show_lines(graph, show)
    filtered : OrderedDict[int, bool] = uniq(show)

    # index in filtered which corresponds to shown line i
    original_to_filtered = dict[int, int] = {
        line : new for new, line in enumerate(filtered) if filtered[line]
    }

    code : list[int] = [
        program[line] if shown else \
        "{}{}".format(" " * line_mapping[line].indent_level, "·" * 3) \
        for line, shown in filtered.items()
    ]
    lines : list[int | None] = [
        line if shown else None for line, shown in filtered.items()
    ]

    # path not including the start
    # TODO: start should be root's start
    rest : list[int] = []
