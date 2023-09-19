from collections import OrderedDict

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

def list_test():
    a = Line(1, 1)
    b = Line(2, 2)
    l1 = [a, b]

    c = Line(1, 1)
    d = Line(2, 2)
    l2 = [c, d]

    print(l1 == l2)

def od_test():
    a = Line(1, 1)
    b = Line(2, 2)
    l1 = (a, b)
    assert isinstance(l1, tuple)
    od = OrderedDict()
    od[l1] = 2

    c = Line(1, 1)
    d = Line(2, 2)
    l2 = (c, d)

    print(l2 in od)

# list_test()
od_test()
