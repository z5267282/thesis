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
            "start" : 26,
            "end"   : 37,
            "body" : [
                {
                    "CodeBlock" : {
                        "start" : 26,
                        "end"   : 27
                    }
                },
                {
                    "WhileBlock" : {
                        "start" : 28,
                        "end"   : 35,
                        "body" : [
                            {
                                "IfBlocK" : {
                                    "start" : 29,
                                    "end"   : 34,
                                    "body" : [
                                        {
                                            "CodeBlock" : {
                                                "start" : 30,
                                                "end"   : 31
                                            }
                                        }
                                    ],
                                    "elifs" : [
                                        {
                                            "ElifBlock" : {
                                                "start" : 32,
                                                "end"   : 34
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "CodeBlock" : {
                                    "start" : 35,
                                    "end"   : 35
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }    
