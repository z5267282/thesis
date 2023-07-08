from tree import BodyBlock, CodeBlock, ElifBlock, ElseBlock, IfBlock

def test_if_chain():
    """templated from: 
    i = 0
    if i == 1:
        ...
    elif i == 2:
        ...
    else:
        ..."""
    c_start = CodeBlock(5)
    c_start.end = 5

    i = IfBlock(6, 1)
    i.end = 11
    i_body = CodeBlock(7)
    i_body.end = 7
    i.add_same_level_block(i_body)

    el = ElifBlock(8, 1)
    el.end = 9
    el_body = CodeBlock(9)
    el_body.end = 9
    el.add_same_level_block(el_body)
    i.add_elif(el)

    els = ElseBlock(10, 1)
    els.end = 11
    els_body = CodeBlock(11)
    els_body.end = 11
    els.add_same_level_block(els_body)
    i.add_else(els)

    root = BodyBlock(5, 1)
    root.end = 11
    root.add_same_level_block(c_start)
    root.add_same_level_block(i)

    line_mapping = {}
    root.map_lines(line_mapping)

    assert line_mapping == {
        5 : c_start,
        6 : i,
        7 : i_body,
        8 : el,
        9 : el_body,
        10 : els,
        11 : els_body
    }
