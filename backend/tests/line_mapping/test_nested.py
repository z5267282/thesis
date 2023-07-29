from tree import BodyBlock, CodeBlock, IfBlock, WhileBlock

def test_tested():
    """based off:
    i = 0
    while i < 13:
        if i % 3 == 0:
            if i % 2 == 0:
                print("mod 6")
        i += 1
    print(f"the last value of i is {i}")"""

    b = BodyBlock(5, 0)
    b.end = 11

    c1 = CodeBlock(5)
    c1.end = 5
    b.add_same_level_block(c1)

    w = WhileBlock(6, 0)
    w.end = 10
    b.add_same_level_block(w)

    i1 = IfBlock(7, 4)
    i1.end = 9
    w.add_same_level_block(i1)

    i2 = IfBlock(8, 4)
    i2.end = 9
    i1.add_same_level_block(i2)

    c2 = CodeBlock(9)
    c2.end = 9
    i2.add_same_level_block(c2)

    c3 = CodeBlock(10)
    c3.end = 10
    w.add_same_level_block(c3)

    c4 = CodeBlock(11)
    c4.end = 11
    b.add_same_level_block(c4)

    line_mapping = b.map_lines()
    assert line_mapping == {
        5: c1,
        6: w,
        7: i1,
        8: i2,
        9: c2,
        10: c3,
        11: c4
    }
