from tree import CodeBlock, ElifBlock, IfBlock

def test_unit_if_elif():
    i = IfBlock(1, 0)
    body_i = CodeBlock(2)
    body_i.end = 2
    i.add_same_level_block(body_i)

    e = ElifBlock(3, 0)
    body_e = CodeBlock(4)
    body_e.end = 4
    e.add_same_level_block(body_e)
    i.add_elif(e)
    e.end = 4

    i.end = 4

    assert i.map_lines() == {
        1 : i,
        2 : body_i,
        3 : e,
        4 : body_e
    }
