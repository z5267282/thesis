from tree_parser import parse

def test_simple_if():
    def if_block():
        i = 0
        if i % 2 == 0:
            print("even")

    root = parse(if_block)
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 5,
            "end"   : 7,
            "body"  : [
                {
                    "CodeBlock" : {
                        "start" : 5,
                        "end"   : 5 
                    }
                },
                {
                    "IfBlock" : {
                        "start" : 6,
                        "end"   : 7,
                        "body" : [
                            {
                                "CodeBlock" : {
                                    "start" : 7,
                                    "end" : 7 
                                }
                            }
                        ],
                        "elifs" : [],
                        "else"  : None
                    }
                }
            ]
        }
    }
