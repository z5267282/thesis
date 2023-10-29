from counter import Counter
from tree import WhileBlock

def test_to_dict():
    iteration, total = 1, 5
    start, end = 4, 7
    while_ = WhileBlock(4, 0)
    counter = Counter(iteration, total, while_)
    counter.start = start
    counter.end = end
    assert counter.to_dict() == {
        "start"       : start,
        "end"         : end,
        "numerator"   : iteration,
        "denominator" : total,
    }
