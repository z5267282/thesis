from tree_parser import parse

def program():
    # print out a hello message in python
    print("Hello, world!")

def test_starting_comment():
    root = parse(program)
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 5,
            "end"   : 5,
            "body"  : [
                {
                    "CodeBlock" : {
                        "start" : 5,
                        "end"   : 5
                    }
                }
            ]
        }
    }
