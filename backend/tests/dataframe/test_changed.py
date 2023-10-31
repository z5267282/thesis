from dataframe import DataFrame
from state import State

def test_not_in_prev_dataframe():
    prev = State({}, {})
    curr_vars = {"i" : 0}
    curr = State(curr_vars, curr=curr_vars)
    frame = DataFrame([], [], None, curr, prev, [], [], [], [])
    assert frame.is_changed("i")

def test_changed_from_prev():
    curr_vars = {"i" : 0}
    prev = State({}, curr=curr_vars)
    curr = State(curr_vars, curr={"i" : 42})
    frame = DataFrame([], [], None, curr, prev, [], [], [], [])
    assert frame.is_changed("i")

def introduced_from_line():
    old = {"i" : 0}
    prev = State(old, curr=old)
    curr = State(old, curr={"i" : 0, "j" : 42})
    frame = DataFrame([], [], None, curr, prev, [], [], [], [])
    assert frame.is_changed("j")
    # unchanged variable should stay the same
    assert not frame.is_changed("i")

# TODO : prev vars tests
