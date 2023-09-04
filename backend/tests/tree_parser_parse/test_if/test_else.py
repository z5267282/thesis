from tree_parser import parse

def test_else():
    def if_else():
        i = 0
        if i == 1:
            print("one")
        else:
            print("something else!")
    
    root = parse(if_else)
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 5,
            "end" : 9,
            "body" : [
                {
                    "CodeBlock" : {
                        "start" : 5,
                        "end" : 5
                    }
                },
                {
                    "IfBlock" : {
                        "start" : 6,
                        "end" : 9,
                        "body" : [
                            {
                                "CodeBlock" : {
                                    "start" : 7,
                                    "end" : 7
                                }
                            }
                        ],
                        "elifs" : [],
                        "else" : {
                            "ElseBlock" : {
                                "start" : 8,
                                "end" : 9,
                                "body" : [
                                    {
                                        "CodeBlock" : {
                                            "start" : 9,
                                            "end" : 9
                                        }
                                    }
                                ]
                            }
                        }
                    }
                }
            ]
        }
    }
