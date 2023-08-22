def program1():
    i = 0
    if i % 7 == 0:
        print("a special number!")
        print(":D")
    else:
        print("meh")
    print("that's all folks")

def program2():
    i = 42
    j = 69
    print(f"{i} + {j} = {i + j}")

from generate import generate_dataframes
from line import Line

def test_2_programs():
    frames1 = generate_dataframes(program1)

    frames2 = generate_dataframes(program2)

    assert frames1 != frames2
    assert frames1 is not frames2
