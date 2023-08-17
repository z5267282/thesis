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

def test_singular_falses():
    original = OrderedDict()
    original[1] = False
    original[2] = True
    original[3] = False
    original[4] = True
    original[5] = False

    exp = OrderedDict()
    exp[1] = False
    exp[2] = True
    exp[3] = False
    exp[4] = True
    exp[5] = False

    assert uniq(original) == exp

def test_middle_falses():
    original = OrderedDict()
    original[1] = True 
    original[2] = True
    original[3] = False
    original[4] = False
    original[5] = True

    exp = OrderedDict()
    exp[1] = True
    exp[2] = True
    exp[3] = False
    exp[5] = True

    assert uniq(original) == exp

def test_integration():
    original = OrderedDict()
    original[0] = True
    original[1] = True
    original[2] = False
    original[3] = False
    original[4] = False
    original[5] = True
    original[6] = False
    original[7] = True

    exp = OrderedDict()
    exp[0] = True
    exp[1] = True
    exp[2] = False
    exp[5] = True
    exp[6] = False
    exp[7] = True

    assert uniq(original) == exp
