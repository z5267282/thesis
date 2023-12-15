"""This instance method is only called during trace_program.
Hence we must manually test if for coverage"""

from line import Line

def test_simple():
    line = Line(4)
    assert line.output == []
    assert line.variables == {}

    line.fix_lag(["hi\n"], {"i" : 1})
    assert line.output == ["hi\n"]
    assert line.variables == {"i" : 1}

    # check that other data is unaffected
    assert line.line_no == 4
    assert line.counters == []

def test_extend():
    line = Line(5, {"i" : 4})
    line.output.append("hello bob\n")
    line.fix_lag(["bye bob\n"], {"i" : 3, "j" : 14})

    assert line.line_no == 5
    assert line.output == ["hello bob\n", "bye bob\n"]
    assert line.variables == {"i" : 3, "j" : 14}
