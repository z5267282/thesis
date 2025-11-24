import os


class Paths:
    """A dataclass to store necessary paths.
    Note that these are relative from the backend folder."""

    # note we use properties so that type hints work

    # program
    @property
    def program(self) -> str:
        return os.path.join(*(self.get_host_path() + ["src", "program.py"]))

    # upload related
    @property
    def timeout(self) -> str:
        return os.path.join(
            *(self.get_host_path() + ["src", "upload", "timeout"]))

    @property
    def sanity(self) -> str:
        return os.path.join(
            *(self.get_host_path() + ["src", "upload", "sanity-run"]))

    # relating to generated dataframes for testing
    @property
    def generated_frame(self) -> str:
        return os.path.join(
            *(self.get_host_path() + ["gen-dataframe", "generated.json"]))

    @property
    def to_python(self) -> str:
        return os.path.join(
            *(self.get_host_path() + ["gen-dataframe", "to-py"]))

    @property
    def as_python(self) -> str:
        return os.path.join(
            *(self.get_host_path() + ["gen-dataframe", "generated.py"]))

    # helper to get the correct folder
    def get_host_path(self) -> list[str]:
        return (
            ["focus-tracker"] if os.getenv("REACT_APP_HOST") == "REMOTE"
            else []
        )
