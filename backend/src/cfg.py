import os

# how many lines after the actual start, before analysis begins
OFFSET : int = 1

# for collapsed lines
ELLIPSE : str = "·" * 3

LEADING_SPACES : int = 4

PROGRAM_PATH : list[str] = ["src", "program.py"]

with open("/tmp/log.txt", "w") as f:
    print(os.getenv("REACT_APP_HOST"), file=f)

if os.getenv("REACT_APP_HOST") == "REMOTE":
    PROGRAM_PATH = ["home", "z5267282", "focus-tracker"] + PROGRAM_PATH
