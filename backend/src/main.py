from json import dumps
import importlib
from os.path import join, sep
import sys

from dataframe import DataFrame
from generate import generate_dataframes
import program

sys.path.insert(
    0, join(sep, "tmp")
)

def main():
    """Execute a program and generate a list of DataFrames representing
    execution states."""
    importlib.reload(program)
    return generate_dataframes(program.program)

if __name__ == "__main__":
    frames : list[DataFrame] = main()
    json   : str = [ frame.to_dict() for frame in frames ]
    # prevent print() behaviour muddling the JSON string
    sys.stdout.write(
        dumps(json)
    )
