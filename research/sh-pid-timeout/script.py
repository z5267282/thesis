from signal import SIGTERM, signal
import sys

def timeout(signum, frame):
    print("timed out!", file=sys.stderr)
    sys.exit(2)

signal(SIGTERM, timeout)

i = 0
while True:
    i += 1

