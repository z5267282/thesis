from dataframe import DataFrame
from state import State

def test_not_in_prev_dataframe():
    variables = State({}, curr={"i" : 0})
    frame = DataFrame([], [], None, variables, [], [], [], [])
    assert frame.is_changed("i")

def test_changed_from_prev():
    variables = State({"i" : 0}, curr={"i" : 42})
    frame = DataFrame([], [], None, variables, [], [], [], [])
    assert frame.is_changed("i")
