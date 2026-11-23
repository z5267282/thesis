from sys import settrace

def main():
    def f():
        print("a")
    
    print("start")
    f()

from types import FunctionType

def trace(frame, event, arg):
    if "f" in frame.f_locals:
        print(type(frame.f_locals["f"]))
        print(isinstance(frame.f_locals["f"], FunctionType))
    return trace

settrace(trace)
main()
settrace(None)
