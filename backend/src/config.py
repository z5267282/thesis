from copy import deepcopy
import os

# how many seconds user programs are allowed to run for
TIMEOUT : int = 1

# how many lines after the actual start, before analysis begins
OFFSET : int = 1

# for collapsed lines
ELLIPSE : str = "·" * 3

LEADING_SPACES : int = 4

class Paths:
    """A dataclass to store necessary paths.
    Note that these are relative from the backend folder."""
    program : list[str] = ["src", "program.py"]
    timeout : list[str] = ["src", "upload", "timeout"]

    def __getattribute__(self, path : list[str]):
        host_path = deepcopy(path)
        if os.getenv("REACT_APP_HOST") == "REMOTE":
            host_path.insert(0, "focus-tracker")

        return os.path.join(*super().__getattribute__(host_path))

PATHS : Paths = Paths()
