def program():
    i = 0
    if i % 2 == 0:
        print("even")
    else:
        print("odd")

from tree import Block
from tree_parser import parse

def test_tree_conditionals():
    root         = parse(program)
    line_mapping = root.map_lines()

    if_ = line_mapping[3]
    assert if_.is_conditional()

    else_ = line_mapping[5]
    assert not else_.is_conditional()

def test_block_basic():
    block = Block(4, 0)
    assert not block.is_conditional()
