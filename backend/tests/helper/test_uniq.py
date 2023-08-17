from collections import OrderedDict

from helper import uniq

def test_no_falses():
    original = OrderedDict((i, True) for i in range(10))
    exp = OrderedDict((i, True) for i in range(10))

    uniq(original) == exp

def test_all_falses():
    original = OrderedDict((i, False) for i in range(10))
    exp = OrderedDict()
    exp[0] = False
    
    assert uniq(original) == exp
