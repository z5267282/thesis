import sys

def program():
    i = 0
    for i in range(10):
        print(i)

def main():
    lines = []
    settrace_closure(trace_execution, lines)
    program()
    print(lines)
    
def trace_execution(frame, event, arg, lines):
    lines.append(frame.f_lineno)

def settrace_closure(trace_execution, lines):
    def wrapper(frame, event, arg):
        trace_execution(frame, event, arg, lines)
        return wrapper
    
    sys.settrace(wrapper)

if __name__ == '__main__':
    main()
