def program():
    def a():
        print("hi")
    
    print("start")
    a()

from generate import generate_dataframes

def test_simple():
    frames = generate_dataframes(program)
    assert frames == []
