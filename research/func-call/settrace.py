from sys import settrace

def main():
    def f():
        print("a")
    
    print("start")
    f()

def trace(frame, event, arg):
    print(frame.f_lineno, frame.f_locals)
    return trace

settrace(trace)
main()
settrace(None)
