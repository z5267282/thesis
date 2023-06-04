import inspect
import linecache
import sys

filename = sys.argv[0]
lines = []

def main():
    i = 1
    twos, sevens = 0, 0
    while i < 5:
        if i % 2 == 0:
            # print("two")
            twos += 1
        elif i % 7 == 0:
            # print("seven")
            sevens += 1
        i += 1

    # print(f"2s: {twos}, 7s: {sevens}")

def trace_execution(frame, event, arg):
    if event == 'line':
        lineno = frame.f_lineno
        line_contents = linecache.getline(filename, lineno)
        print(f'{lineno:2} | {line_contents[:-1]}')
        lines.append(lineno)
    return trace_execution

def get_main_info():
    lines, starting_lineno = inspect.getsourcelines(main)
    print(starting_lineno)
# get_main_info()

sys.settrace(trace_execution)
main()
