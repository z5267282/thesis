from line import Line
from tree import Block, BodyBlock, CodeBlock

from typing import Type

def generate_execution_graph(root : BodyBlock, lines : list[Line]):
    """Create the intelligent unique execution path.
    Return a condensed line list."""
    line_mapping : dict[int, Type[Block]] = {}
    root.map_lines(line_mapping)
    curr : Type[Block] | None = None
    for line in lines:
        line_no : int = line.line_no
        node : Type[Block] = lines[line_no]
        if isinstance(node, CodeBlock) and node.start == line_no:
            curr = node
