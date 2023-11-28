from copy import deepcopy

def f():
    print("hello")

f()

print(globals()["f"])
