import inspect
import sys

lines = []

def trace_function(frame, event, arg):
    if event == 'line':
        print(inspect.getmembers(frame))
        lines.append(frame.f_lineno)
    return trace_function

def main():
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

    print(lines)

sys.settrace(trace_function)
main()
