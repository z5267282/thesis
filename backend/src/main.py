import importlib

from generate import generate_dataframes
import program

def main():
    """Execute a program and generate a list of DataFrames representing
    execution states."""
    importlib.reload(program)
    return generate_dataframes(program.program)
