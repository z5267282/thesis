class C:
    def __init__(self, ls : list[int]):
        self.ls = ls

a = [1, 2]
c = C(a + [1])
print(c.ls)
a.append(42)
print(c.ls)
print(repr(a), repr(c.ls))
