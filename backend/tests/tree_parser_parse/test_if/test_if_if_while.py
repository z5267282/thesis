from tree_parser import parse

def test_if_if_while():
    def if_if_while():
        i = 6
        if i % 2 == 0:
            if i % 3 == 0:
                j = 0
                while j < i:
                    print(j)
                    j += 1
        print("done")
    
    root = parse(if_if_while)    
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 5,
            "end" : 12,
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
                        "end" : 11,
                        "body" : [
                            {
                                "IfBlock" : {
                                    "start" : 7,
                                    "end" : 11,
                                    "body" : [
                                        {
                                            "CodeBlock" : {
                                                "start" : 8,
                                                "end" : 8,
                                            }
                                        },
                                        {
                                            "WhileBlock" : {
                                                "start" : 9,
                                                "end" : 11,
                                                "body" : [
                                                    {
                                                        "CodeBlock" : {
                                                            "start" : 10,
                                                            "end" : 11
                                                        }
                                                    }
                                                ]
                                            }
                                        }
                                    ],
                                    "elifs" : [],
                                    "else" : None
                                }
                            }
                        ],
                        "elifs" : [],
                        "else" : None
                    }
                },
                {
                    "CodeBlock" : {
                        "start" : 12,
                        "end" : 12
                    }
                }
            ]
        }
    }
