from tree_parser import parse

def test_elif():
    def if_elif():
        i = 0
        if i == 1:
            print("one")
        elif i == 2:
            print("two")
    
    root = parse(if_elif)
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
                        "elifs" : [
                            {
                                "ElifBlock" : {
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
                        ],
                        "else" : None
                    }
                }
            ]
        }
    }
