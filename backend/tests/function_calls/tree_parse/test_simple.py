def program():
    def f():
        print("a")
        print("b")
    
    print("start")
    f()

from tree_parser import parse

def test_simple():
    root = parse(program)
    root.pretty_print()
    assert root.to_dict() == {
        "BodyBlock": {
            "start": 2,
            "end": 7,
            "body": [
                {
                    "FunctionBlock": {
                        "start": 2,
                        "end": 5,
                        "body": [
                            {
                                "CodeBlock": {
                                    "start": 3,
                                    "end": 5
                                }
                            }
                        ]
                    }
                },
                {
                    "CodeBlock": {
                        "start": 6,
                        "end": 7
                    }
                }
            ]
        }
    }
