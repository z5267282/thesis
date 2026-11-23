import sys

def trace_function(frame, event, arg):
    print(frame.f_lineno, end=" ")
    print(f"{str(frame.f_locals):<35} |")
    return trace_function

def main():
    def a():
        print("a")
        b()

    def b():
        print("b")

    i = 0
    if i == 1:
        print("one")
    else:
        print("hi")
        a()

sys.settrace(trace_function)
main()

