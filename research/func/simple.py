from sys import settrace

def main():
    def msg():
        print("hello")
        print("mate")
    
    print("going to call the function")
    msg()
    print("done")

def trace(frame, event, arg):
    print(f"{event} : line - {frame.f_lineno}")
    return trace

settrace(trace)
main()
settrace(None)
