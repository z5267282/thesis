from copy import deepcopy
from typing import cast, Callable

from line import Line
from stack import Stack
from tree import Block, WhileBlock


def generate_graphs(
    filtered: list[Line], line_mapping: dict[int, Block]
) -> list[list[Line]]:
    top_level: list[Line] = []
    whiles: Stack[While] = Stack()
    return [
        generate_ith_graph(
            line, line_mapping[line.line_no], top_level, whiles
        ) for line in filtered
    ]


class While:
    def __init__(self, node: WhileBlock, called: Line) -> None:
        self.node: WhileBlock = node
        self.called: Line = called
        self.lines: list[Line] = []


def generate_ith_graph(
    line: Line, node: Block,
    top_level: list[Line], whiles: Stack[While]
) -> list[Line]:
    """Generate the execution graph up to the ith line.
    Return a list of raw line numbers to show in the graph."""
    result: Callable = lambda: generate_from_state(top_level, whiles)

    while whiles:
        top = whiles.peek()
        curr = top.node
        # we have found the next iteration of the most indented while
        # update this on the stack
        if line.line_no == curr.start:
            whiles.pop()
            whiles.push(While(cast(WhileBlock, node), line))
            return result()

        if line.line_no <= curr.end:
            break

        whiles.pop()

    # the top of the stack now stores the correct item
    if isinstance(node, WhileBlock):
        whiles.push(While(node, line))
    elif whiles:
        top: While = whiles.peek()
        top.lines.append(line)
    else:
        top_level.append(line)
    return result()


def generate_from_state(
    top_level: list[Line], whiles: Stack[While]
) -> list[Line]:
    result: list[Line] = deepcopy(top_level)
    # stack supports linear iteration from bottom to top
    for w in whiles:
        result.append(w.called)
        result.extend(w.lines)
    return result
