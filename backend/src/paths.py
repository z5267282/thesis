import os

class Paths:
    """A dataclass to store necessary paths.
    Note that these are relative from the backend folder."""
    # program
    program : list[str] = ["src", "program.py"]
    # upload related
    timeout : list[str] = ["src", "upload", "timeout"]
    sanity  : list[str] = ["src", "upload", "sanity-run"]
    # survey 3 respondents

    # relating to generated dataframes for testing
    generated_frame : list[str] = ["gen-dataframe", "generated.json"]
    to_python       : list[str] = ["gen-dataframe", "to-py"]
    as_python       : list[str] = ["gen-dataframe", "generated.py"]

    def __getattribute__(self, path : str):
        original  : list[str] = super().__getattribute__(path)
        host_path : list[str] = (
            ["focus-tracker"] if os.getenv("REACT_APP_HOST") == "REMOTE"
            else []
        ) \
        + original
        return os.path.join(*host_path)
