def program():
    def a():
        print("hi")
    
    print("start")
    a()

from dataframe import DataFrame
from generate import generate_dataframes

def test_simple():
    frames = generate_dataframes(program)

    from json import dump
    with open("/tmp/a.json", "w") as f:
        dump(DataFrame.to_dicts(frames), f, indent=2)

    assert frames == []
