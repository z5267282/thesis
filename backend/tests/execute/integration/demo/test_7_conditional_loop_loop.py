def program():
    i = 0
    while i < 4:
        if i == 0:
            row = ""
            j = i
            while j >= 0:
                row = f"{row} {j}"
                j -= 1
            print(row)
        elif i == 2:
            row = ""
            j = 0
            while j <= i:
                row = f"{row} {j}"
                j += 1
            print(row)
        i += 1
    print("the end!")
from dataframe import DataFrame
from generate import generate_dataframes

def test_7_conditional_loop_loop():
    assert DataFrame.to_dicts(generate_dataframes(program)) == []
