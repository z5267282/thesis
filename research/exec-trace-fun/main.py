import subprocess
import sys

def trace_function(frame, event, arg):
    print(f"| {event:10} | {str(arg):>4} |", end=' ')
    print(f"{frame.f_lineno:>4} |", end=' ')
    print(f"{str(frame.f_locals):<35} |")
    return trace_function

with open("normal.py", "r") as f:
    sys.settrace(trace_function)
    exec(f.read())
