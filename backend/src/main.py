import inspect
import linecache
import sys

from program import program

filename = sys.argv[0]
lines = []

def trace_execution(frame, event, arg):
    if event == 'line':
        lineno = frame.f_lineno
        line_contents = linecache.getline(filename, lineno)
        print(f'{lineno:2} | {line_contents[:-1]}')
        lines.append(lineno)
    return trace_execution

def get_program_info():
    lines, starting_lineno = inspect.getsourcelines(program)
    print(starting_lineno)
# get_program_info()

sys.settrace(trace_execution)
program()
