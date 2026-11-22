from last import Last

def test_simple():
    last = Last()
    last.variables = {"a" : 1}
    last.output = ["hello"]

    assert last.variables == {"a" : 1}
    assert last.output == ["hello"]
