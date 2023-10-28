import os

class Paths:
    """A dataclass to store necessary paths.
    Note that these are relative from the backend folder."""
    def __init__(self, program, timeout, sanity):
        self.program : list[str] = program
        self.timeout : list[str] = timeout
        self.sanity  : list[str] = sanity

    def __getattribute__(self, path : str):
        original  : list[str] = super().__getattribute__(path)
        host_path : list[str] = (
            ["focus-tracker"] if os.getenv("REACT_APP_HOST") == "REMOTE"
            else []
        ) \
        + original
        return os.path.join(*host_path)
