from collections import OrderedDict
from typing import Type

from helper import uniq
from tree import Block, BodyBlock

tmp = "·"

def collapse(graph : list[int], root : BodyBlock):
    # should be a wrapper
    show : OrderedDict[int, bool] = OrderedDict(
        (line, True) for line in range(root.start, root.end + 1)
    )
    root.show_lines(graph, show)
    filtered : OrderedDict[int, bool] = uniq(show)

    line_mapping : dict[int, Type[Block]] = root.map_lines()

    # index in filtered which corresponds to shown line i
    original_to_filtered = dict[int, int] = {
        line : new for new, line in enumerate(filtered) if filtered[line]
    }

    code : list[int] = []
    lines : list[str] = []
    # path not including the start
    # TODO: start should be root's start
    path_rest : list[int] = []

    # for line in filtered:
