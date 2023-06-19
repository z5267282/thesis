from tree_parser import parse

def test_large():
    def large():
        i = 1
        twos, sevens = 0, 0
        while i < 100:
            if i % 2 == 0:
                print("two")
                twos += 1
            elif i % 7 == 0:
                print("seven")
                sevens += 1
            i += 1

        print(f"2s: {twos}, 7s: {sevens}")
    
    root = parse(large)
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 5,
            "end"   : 16,
            "body" : [
                {
                    "CodeBlock" : {
                        "start" : 5,
                        "end"   : 6
                    }
                },
                {
                    "WhileBlock" : {
                        "start" : 7,
                        "end"   : 14,
                        "body" : [
                            {
                                "IfBlocK" : {
                                    "start" : 8,
                                    "end"   : 13,
                                    "body" : [
                                        {
                                            "CodeBlock" : {
                                                "start" : 9,
                                                "end"   : 10
                                            }
                                        }
                                    ],
                                    "elifs" : [
                                        {
                                            "ElifBlock" : {
                                                "start" : 11,
                                                "end"   : 13
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "CodeBlock" : {
                                    "start" : 14,
                                    "end"   : 14
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }    
