import sys

def trace_function(frame, event, arg):
    print(repr(frame))

sys.settrace(trace_function)
with open("dummy/normal.py") as f:
    exec(f.read())
