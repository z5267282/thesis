import os

# how many lines after the actual start, before analysis begins
OFFSET : int = 1

ELLIPSE : str = "·" * 3

LEADING_SPACES : int = 4

PROGRAM_PATH : list[str] = ["src", "program.py"]
if os.getenv("THESIS_HOST") == "REMOTE":
    PROGRAM_PATH = ["home", "z5267282", "focus-tracker"] + PROGRAM_PATH
