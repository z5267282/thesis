from typing import Callable

from generate import generate_dataframes

def main(program : Callable):
    """Execute a program and generate a list of DataFrames representing
    execution states."""
    return generate_dataframes(program)
