import sys

def trace_function(frame, event, arg):
    print(f"| {event:10} | {str(arg):>4} |", end=' ')
    print(f"{frame.f_lineno:>4} |", end=' ')
    # print(f"{str(frame.f_locals):<35} |")
    return trace_function

def main():
    a()

def a():
    i = 3
    while i < 3:
        print(i)
        i += 1

def b():
    i = 1
    twos, sevens = 0, 0
    while i < 5:
        if i % 2 == 0:
            print("two")
            twos += 1
        elif i % 7 == 0:
            print("seven")
            sevens += 1
        i += 1

    print(f"2s: {twos}, 7s: {sevens}")

sys.settrace(trace_function)
main()
