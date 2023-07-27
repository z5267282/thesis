from tree import BodyBlock, CodeBlock

def test_body_block():
    b = BodyBlock(1, 1)
    b.end = 3

    c1 = CodeBlock(1)
    c1.end = 1
    b.add_same_level_block(c1)
    c2 = CodeBlock(2)
    c2.end = 2
    b.add_same_level_block(c2)
    c3 = CodeBlock(3)
    c3.end = 3
    b.add_same_level_block(c3)

    line_mapping = b.map_lines()

    # b was not a most nested item anywhere, so shouldn't be in mappings
    assert line_mapping == {
        1 : c1,
        2 : c2,
        3 : c3
    }
