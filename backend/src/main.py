import importlib

from dataframe import DataFrame
from generate import generate_dataframes
import program


def main() -> list[DataFrame]:
    """Execute a program and generate a list of DataFrames representing
    execution states."""
    importlib.reload(program)
    return generate_dataframes(program.program)
