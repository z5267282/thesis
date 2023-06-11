from src.tree import BodyBlock, CodeBlock

def test_code_block():
    c = CodeBlock(1)
    c.end = 10
    assert c.to_dict() == {
        "CodeBlock" : {"start" : 1,"end" : 10}
    }

def test_body_block():
    b = BodyBlock(1)
    b.end = 10

    c1 = CodeBlock(1)
    c1.end = 4
    b.add_same_level_block(c1)

    c2 = CodeBlock(5)
    c2.end = 10
    b.add_same_level_block(c2)

    assert b.to_dict() == {
        "BodyBlock": {"start": 1, "end"  : 10, "body" : [
                {"CodeBlock": {"start": 1, "end": 4}},
                {"CodeBlock": {"start": 5, "end": 10}}
            ]
        }
    }

def test_if_block():

