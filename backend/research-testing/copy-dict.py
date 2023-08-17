from copy import copy, deepcopy

class C:
    def __init__(self, x):
        self.x = x
    
    # def __copy__(self):
    #     return C(self.x)

def dumb():
    x = {"one" : "two"}
    a = C(x)
    b = C(x)
    x["three"] = "four"

    print(a.x)
    print(b.x)

def nuanced():
    a = C({"one" : "two"})
    b = copy(a)
    a.x["three"] = "four"
    print(b.x)

def deep():
    a = C({"one" : "two"})
    b = deepcopy(a)
    a.x["three"] = "four"
    print(b.x)

# nuanced()
deep()
