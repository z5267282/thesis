def program():
    def a():
        def b():
            print("a")
        
        b()
        print("a")
    
    print("start")
    a()

from tree_parser import parse

def test_nested():
    root = parse(program)
    root.pretty_print()
    assert root.to_dict() == {
        "BodyBlock": {
            "start": 2,
            "end": 10,
            "body": [
                {
                    "FunctionBlock": {
                        "start": 2,
                        "end": 8,
                        "body": [
                            {
                                "FunctionBlock": {
                                    "start": 3,
                                    "end": 5,
                                    "body": [
                                        {
                                            "CodeBlock": {
                                                "start": 4,
                                                "end": 5
                                            }
                                        }
                                    ]
                                },
                            },
                            {
                                "CodeBlock": {
                                    "start": 6,
                                    "end": 8,
                                }
                            }
                        ]
                    }
                },
                {
                    "CodeBlock": {
                        "start": 9,
                        "end": 10
                    }
                }
            ]
        }
    }