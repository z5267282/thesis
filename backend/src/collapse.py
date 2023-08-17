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

    code : list[int] = []
    lines : list[int | None] = []
    # path not including the start
    # TODO: start should be root's start
    rest : list[int] = []

    # make this once to avoid O(n^2) recalls
    raw = filtered.items()
    for i, (line, shown) in enumerate(raw):
        # should be impossible to hide the first line
        if shown or i == 0:
            code.append(program[line])
            lines.append(line)
        else:
            parent_line, _ = raw[i - 1]
            parent = line_mapping[parent_line]
