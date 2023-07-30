from tree_parser import parse

def test_whitespace():
    def whitespace():
        # this is a header comment
        i = 0
        while i < 10:
            # print every even number
            if i % 2 == 0:
                print(i)
            i += 1
        
        print(f"the last value of i is {i}")
    
    root = parse(whitespace)
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 6,
            "end" : 13,
            "body" : [
                {
                    "CodeBlock" : {
                        "start" : 6,
                        "end" : 6
                    }
                },
                {
                    "WhileBlock" : {
                        "start" : 7,
                        "end" : 12,
                        "body" : [
                            {
                                "IfBlock" : {
                                    "start" : 9,
                                    "end" : 10,
                                    "body" : [
                                        {
                                            "CodeBlock" : {
                                                "start" : 10,
                                                "end" : 10
                                            }
                                        }
                                    ],
                                    "elifs" : [],
                                    "else" : None
                                }
                            },
                            {
                                "CodeBlock" : {
                                    "start" : 11,
                                    "end" : 12
                                }
                            }
                        ]
                    }
                },
                {
                    "CodeBlock" : {
                        "start" : 13,
                        "end" : 13
                    }
                }
            ]
        }
    }
