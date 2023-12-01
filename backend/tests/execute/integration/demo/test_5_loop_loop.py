def program():
    i = 0
    while i < 5:
        row = ""
        j = 0
        while j <= i:
            row += "X"
            j += 1
    
        print(row)
        i += 1
    print("end!")
from dataframe import DataFrame
from generate import generate_dataframes

def test_5_loop_loop():
    assert DataFrame.to_dicts(generate_dataframes(program)) == []
