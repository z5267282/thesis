from src.tree import *

def test_code_block():
    c = CodeBlock(10)
    assert str(c) == "CodeBlock(start=10, end=None)"
