from collections import OrderedDict

from helper import uniq

def test_no_falses():
    original = OrderedDict((i, True) for i in range(10))
    exp = OrderedDict((i, True) for i in range(10))
