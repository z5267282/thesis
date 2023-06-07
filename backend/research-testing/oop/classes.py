class Parent:
    def __init__(self):
        pass

class Child(Parent):
    def fun(self):
        print("fun!")

p = Parent()
c = Child()

y = [p, c]
for i in y:
    i.fun()
