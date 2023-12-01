def program():
    i = 0
    while i < 2:
        print(i)
        i += 1
    print("done")

from dataframe import DataFrame
from generate import generate_dataframes

def test_3_loop():
    assert DataFrame.to_dicts(generate_dataframes(program)) == []
