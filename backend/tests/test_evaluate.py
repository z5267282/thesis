from evaluate import evaluate

def test_int():
    expression = "x == 10"
    variables = {"x" : 10}
    assert evaluate(expression, variables) == "10 == 10"

def test_str():
    expression = "x == \"bye\""
    variables = {"x" : "boating"}
    assert evaluate(expression, variables) == "boating == \"bye\""
