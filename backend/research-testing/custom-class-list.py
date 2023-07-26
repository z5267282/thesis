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

list_test()
