from tree_parser import parse

def program():
    print("hello!")
    print("what a wonderful day it is")
    city = "Sydney"
    print(f"in {city}!")

def test_code_block_program():
    root = parse(program)
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 4,
            "end"   : 7,
            "body"  : [
                {
                    "CodeBlock" : {
                        "start" : 4,
                        "end"   : 7
                    }
                }
            ]
        }
    }
