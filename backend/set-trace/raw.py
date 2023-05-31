import sys

def trace_function(frame, event, arg):
    print('here')
    print(f"event: {event}")
    pass

sys.settrace(trace_function)

i = 1
twos, sevens = 0, 0
while i < 100:
    if i % 2 == 0:
        print("two")
        twos += 1
    elif i % 7 == 0:
        print("seven")
        sevens += 1
    i += 1

print(f"2s: {twos}, 7s: {sevens}")
