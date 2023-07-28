from tree import CodeBlock, IfBlock

def test_unit_if():
    body = CodeBlock(2)
    body.end = 4

    if_ = IfBlock(1, 0)
    if_.end = 4
    if_.add_same_level_block(body)

    line_mapping = if_.map_lines()

    assert line_mapping == {
        1 : if_,
        2 : body,
        3 : body,
        4 : body
    }
