from tree_parser import parse

def test_elif_chain():
    def if_elif_chain():
        i = 0
        if i == 1:
            print("one")
        elif i == 2:
            print("two")
        elif i == 3:
            print("three")
        print(i)
    
    root = parse(if_elif_chain)
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
                            },
                            {
                                "ElifBlock" : {
                                    "start" : 10,
                                    "end" : 11,
                                    "body" : [
                                        {
                                            "CodeBlock" : {
                                                "start" : 11,
                                                "end" : 11
                                            }
                                        }
                                    ]
                                }
                            }
                        ],
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
