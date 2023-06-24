from tree_parser import parse

def test_simple_while():
    def simple_while():
        SIZE = 3
        i = 0
        while i < SIZE:
            j = 0
            while j < SIZE:
                print("square")
            i += 1

    root = parse(simple_while)
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 5,
            "end" : 11,
            "body" : [
                {
                    "CodeBlock" : {
                        "start" : 5,
                        "end" : 6
                    }
                },
                {
                    "WhileBlock" : {
                        "start" : 7,
                        "end" : 11,
                        "body" : [
                            {
                                "CodeBlock" : {
                                    "start" : 8,
                                    "end" : 8,
                                    "body" : []
                                }
                            },
                            {
                                "WhileBlock" : {
                                    "start" : 9,
                                    "end" : 10,
                                    "body" : [
                                        {
                                            "CodeBlock" : {
                                                "start" : 10,
                                                "end" : 10
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "CodeBlock" : {
                                    "start" : 11,
                                    "end" : 11
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
