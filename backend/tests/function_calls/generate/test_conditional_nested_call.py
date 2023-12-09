def program():
    def a():
        print("a")
        b()
    
    def b():
        print("b")

    i = 0
    if i == 1:
        print("one")
    else:
        print("hi")
        a()

from dataframe import DataFrame
from generate import generate_dataframes

def test_conditional_nested_call():
    pass
