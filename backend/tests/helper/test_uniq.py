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

def test_leading_falses():
    original = OrderedDict((i, False) for i in range(10))
    for i in range(10, 13):
        original[i] = True
    
    exp = OrderedDict()
    exp[0] = False
    exp[10] = True
    exp[11] = True
    exp[12] = True

    assert uniq(original) == exp
