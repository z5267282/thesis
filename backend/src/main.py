import inspect
import linecache
import sys

from program import program


def main():
    filename = sys.argv[0]
    lines = []

    sys.settrace(trace_execution)
    program()

def trace_execution(frame, event, arg):
    if event == 'line':
        lineno = frame.f_lineno
        # line_contents = linecache.getline(filename, lineno)
        # print(f'{lineno:2} | {line_contents[:-1]}')
        # lines.append(lineno)
    return trace_execution

def get_program_info():
    lines, starting_lineno = inspect.getsourcelines(program)
    print(starting_lineno)

if __name__ == '__main__':
    # get_program_info()
    main()
