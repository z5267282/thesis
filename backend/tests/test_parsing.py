from src.tree import BodyBlock, CodeBlock

def test_code_block():
    c = CodeBlock(10)
    assert str(c) == "CodeBlock(start=10, end=None)"

def test_body_block():
    b = BodyBlock(1)
    b.end = 10

    c1 = CodeBlock(1)
    c1.end = 4
    b.add_same_level_block(c1)

    c2 = CodeBlock(5)
    c2.end = 10
    b.add_same_level_block(c2)

    exp = """BodyBlock(start=1, end=10, body=[
        CodeBlock(start=1, end=4),
        CodeBlock(start=5, end=10)
    ]
)
"""
    assert(str(b) == exp)
