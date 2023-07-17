class C:
    def __init__(self, ls : list[int]):
        self.ls = ls

def class_test():
    a = [1, 2]
    c = C(a + [1])
    print(c.ls)
    a.append(42)
    print(c.ls)
    print(repr(a), repr(c.ls))

def constructor_test():
    a = [1, 2]
    c = C(a)
    a.append(3)
    print(c.ls)

constructor_test()
