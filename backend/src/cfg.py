import os

# how many lines after the actual start, before analysis begins
OFFSET : int = 1

# for collapsed lines
ELLIPSE : str = "·" * 3

LEADING_SPACES : int = 4

PROGRAM_PATH : list[str] = ["src", "program.py"]

if os.getenv("REACT_APP_HOST") == "REMOTE":
    PROGRAM_PATH.insert(0, "focus-tracker")
