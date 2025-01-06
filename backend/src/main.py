import importlib

from dataframe import DataFrame
from generate import generate_dataframes
import program

import decimaltrans

def main() -> list[DataFrame]:
    """Execute a program and generate a list of DataFrames representing
    execution states."""
    decimaltrans.transform_to_decimal("program.py")
    importlib.reload(program)
    result : list[DataFrame] = generate_dataframes(program.program)
    for item in result:
        decimaltrans.restore_decimal_to_number(item)
    
    return result